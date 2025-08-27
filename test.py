import mdformat


def test_mdformat_recover_urls():
    md = """# TEST

- [title](./en.md)
- [title](./中文.md)
- [title](./日本語.md)
- [title](./العربية.md)

- [title](#en)
- [title](#中文)
- [title](#日本語)
- [title](#العربية)

## en

## 中文

## 日本語

## العربية

"""

    print(repr(md))
    print(repr(mdformat.text(md, extensions=["recover-urls"])))
    assert mdformat.text(md, extensions=["recover-urls"]) == md
