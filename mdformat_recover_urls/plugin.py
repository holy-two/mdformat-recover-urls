import re
from typing import Mapping
from urllib.parse import unquote

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

_MD_REL_LINK = re.compile(r"^(?:\.|#).*", re.IGNORECASE)
_PCT = re.compile(r"%[0-9A-Fa-f]{2}")


def update_mdit(mdit: MarkdownIt) -> None:
    return


def _is_pct_encoded(s: str) -> bool:
    """Check if the string contains any percent-encoded sequences."""
    return bool(_PCT.search(s))


def _unquote_url(url: str) -> str:
    """Unquote URL if it's a relative link or a fragment."""
    if isinstance(url, str) and _MD_REL_LINK.match(url):
        url = unquote(url) if _is_pct_encoded(url) else url
    return url


def _recover_urls(node: RenderTreeNode, context: RenderContext) -> str:
    """Recover percent-encoded URLs in link nodes."""
    title = "".join(child.render(context) for child in (node.children or []))
    url = _unquote_url(node.attrs.get("href", ""))
    return f"[{title}]({url})"


RENDERERS: Mapping[str, Render] = {
    "link": _recover_urls,
}


# XXX mdformat-recover-urls and mdformat-toc plugins are not compatible. See:
# https://github.com/hukkin/mdformat-toc/issues/19
# https://github.com/holy-two/mdformat-recover-urls/pull/2
# https://github.com/hukkin/mdformat/issues/312#issuecomment-1586025822
# So we're going to monkey-patch mdformat-toc's link rendering.
try:
    from mdformat_toc import plugin

    # Save the original function.
    original_func = plugin._maybe_add_link_brackets

    def _patched_maybe_add_link_brackets(link: str) -> str:
        """Force unquoting of URLs slugs in mdformat-toc."""
        return original_func(_unquote_url(link))

    # Use our patched version instead of the original one.
    plugin._maybe_add_link_brackets = _patched_maybe_add_link_brackets

# Do nothing if mdformat-toc is not installed.
except ImportError:
    pass
