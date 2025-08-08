import io
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image

WEBP_QUALITY = int(os.getenv("WEBP_QUALITY", "85"))


def _webp_name(file_name: str) -> str:
    root, _ = os.path.splitext(file_name)
    return root + ".webp"


def _convert_image_to_webp(src_path: str, dst_path: str) -> None:
    # Read original via storage
    with default_storage.open(src_path, "rb") as f:
        img = Image.open(f)
        img.load()

    # Convert to RGB if needed
    if img.mode in ("RGBA", "P"):
        background = Image.new("RGBA", img.size, (255, 255, 255, 0))
        background.paste(img, mask=img.split()[3] if img.mode == "RGBA" and len(img.getbands()) == 4 else None)
        img = background.convert("RGBA")
    # WebP supports RGBA, but to reduce size we often use RGB unless transparency is present
    has_alpha = img.mode in ("LA", "RGBA")
    if not has_alpha and img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    out = io.BytesIO()
    img.save(out, format="WEBP", quality=WEBP_QUALITY, method=6)
    out.seek(0)

    # Save via storage; overwrite if exists: delete first to ensure replacement
    if default_storage.exists(dst_path):
        default_storage.delete(dst_path)
    default_storage.save(dst_path, ContentFile(out.read()))


@receiver(post_save)
def auto_generate_webp(sender, instance, **kwargs):
    """
    Generic post_save receiver that scans any model instance for ImageField values
    and ensures a sibling .webp file exists in the same storage.
    """
    # Only act on real model subclasses
    if not isinstance(instance, models.Model):
        return

    for field in instance._meta.get_fields():
        if isinstance(field, models.ImageField):
            try:
                file_field = getattr(instance, field.name)
            except Exception:
                continue
            if not file_field:
                continue
            file_name = getattr(file_field, "name", None)
            if not file_name:
                continue

            webp_name = _webp_name(file_name)
            try:
                if not default_storage.exists(webp_name):
                    _convert_image_to_webp(file_name, webp_name)
            except Exception:
                # Fail silently to avoid interrupting save flow
                # Consider adding logging if a logger is configured
                continue
