import mdformat


def test_mdformat_recover_urls():
    md = """# TEST

- [title](./中文.md)
- [title](#中文)

## 中文
"""

    formatted = mdformat.text(md, extensions=["recover-urls"])

    print("原文:", repr(md))
    print("格式化:", repr(formatted))

    assert "./中文.md" in formatted
    assert "#中文" in formatted
