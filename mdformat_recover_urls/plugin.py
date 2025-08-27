import re
from urllib.parse import unquote
from typing import Mapping
from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

_MD_REL_LINK = re.compile(r"^(?:\.|#).*", re.IGNORECASE)
_PCT = re.compile(r"%[0-9A-Fa-f]{2}")


def update_mdit(mdit: MarkdownIt) -> None:
    return


def _is_pct_encoded(s: str) -> bool:
    return bool(_PCT.search(s))


def _recover_urls(node: RenderTreeNode, context: RenderContext) -> str:
    title = node.content or ""
    url = node.attrs.get("href", "")
    if type(url) is str and _MD_REL_LINK.match(url):
        url = unquote(url) if _is_pct_encoded(url) else url
    return f"[{title}]({url})"


RENDERERS: Mapping[str, Render] = {
    "link": _recover_urls,
}
