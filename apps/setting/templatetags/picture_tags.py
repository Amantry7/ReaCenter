from django import template
from django.utils.html import format_html
from django.core.files.storage import default_storage
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
import os

register = template.Library()


def _webp_candidate(url: str) -> str:
    root, ext = os.path.splitext(url)
    if not ext:
        return url
    return f"{root}.webp"


def _to_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)

@register.simple_tag
def render_picture(image_field, alt="", css_class="", width=None, height=None, fetchpriority=None, lazy=True, decoding="async"):
    """
    Renders <picture> with webp <source> if a sibling .webp exists next to the original file.
    Falls back to plain <img> if webp is not present or image_field empty.
    """
    if not image_field:
        return ""
    try:
        original_url = image_field.url
    except Exception:
        return ""

    webp_url = _webp_candidate(original_url)

    # Check existence of webp in storage
    # Convert URL to storage-relative path when possible
    storage_path = getattr(image_field, 'name', None) or original_url
    webp_storage_path = os.path.splitext(storage_path)[0] + '.webp'
    has_webp = default_storage.exists(webp_storage_path)

    attrs = []
    if css_class:
        attrs.append(f'class="{css_class}"')
    if alt is None:
        alt = ""
    attrs.append(f'alt="{alt}"')
    if width:
        attrs.append(f'width="{width}"')
    if height:
        attrs.append(f'height="{height}"')
    if fetchpriority in {"high", "low", "auto"}:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    if _to_bool(lazy):
        attrs.append('loading="lazy"')
    if isinstance(decoding, str) and decoding in {"async", "auto", "sync"}:
        attrs.append(f'decoding="{decoding}"')

    img_tag = f"<img src=\"{original_url}\" {' '.join(attrs)}>"

    if has_webp:
        html = f"<picture><source srcset=\"{webp_url}\" type=\"image/webp\">{img_tag}</picture>"
        return mark_safe(html)
    return mark_safe(img_tag)


@register.simple_tag
def render_static_picture(static_path, alt="", css_class="", width=None, height=None, fetchpriority=None, lazy=True, decoding="async"):
    """
    Renders <picture> for a STATIC file path. If a sibling .webp exists in staticfiles, adds a webp <source>.
    Usage: {% render_static_picture 'assets/images/logo.png' alt='Logo' %}
    """
    if not static_path:
        return ""

    # URLs for original and potential webp
    original_url = static(static_path)
    webp_static_path = os.path.splitext(static_path)[0] + '.webp'

    # Check existence via staticfiles storage
    has_webp = False
    try:
        has_webp = staticfiles_storage.exists(webp_static_path)
    except Exception:
        has_webp = False

    webp_url = static(webp_static_path) if has_webp else None

    attrs = []
    if css_class:
        attrs.append(f'class="{css_class}"')
    if alt is None:
        alt = ""
    attrs.append(f'alt="{alt}"')
    if width:
        attrs.append(f'width="{width}"')
    if height:
        attrs.append(f'height="{height}"')
    if fetchpriority in {"high", "low", "auto"}:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    if _to_bool(lazy):
        attrs.append('loading="lazy"')
    if isinstance(decoding, str) and decoding in {"async", "auto", "sync"}:
        attrs.append(f'decoding="{decoding}"')

    img_tag = f"<img src=\"{original_url}\" {' '.join(attrs)}>"
    if has_webp and webp_url:
        html = f"<picture><source srcset=\"{webp_url}\" type=\"image/webp\">{img_tag}</picture>"
        return mark_safe(html)
    return mark_safe(img_tag)
