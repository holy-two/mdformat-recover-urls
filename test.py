from textwrap import dedent

import mdformat


def test_mdformat_recover_urls():
    original = dedent("""\
        # TEST

        - [Relative path](./中文.md)
        - [URL fragment](#中文)
        - [概述](#%E6%A6%82%E8%BF%B0)

        ## 中文

        ## 概述
        """)

    expected = dedent("""\
        # TEST

        - [Relative path](./中文.md)
        - [URL fragment](#中文)
        - [概述](#概述)

        ## 中文

        ## 概述
        """)

    formatted = mdformat.text(original, extensions=["recover-urls"])

    print("原文:", repr(original))
    print("格式化:", repr(formatted))

    assert formatted == expected


def test_mdformat_toc_no_conflicts():
    original = dedent("""\
        ## Contents

        <!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

        - [Contents](#contents)
        - [授权](#%E6%8E%88%E6%9D%83)
          - [RBAC 框架](#rbac-%E6%A1%86%E6%9E%B6)
          - [ABAC 框架](#abac-框架)
          - [Macaroons](#macaroons)
        - [OAuth2 & OpenID](#oauth2--openid)

        <!-- mdformat-toc end -->

        ## 策略模型

        ### RBAC 框架

        ### ABAC 框架

        ### Macaroons

        ## OAuth2 & OpenID
        """)

    expected = dedent("""\
        ## Contents

        <!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

        - [Contents](#contents)
        - [策略模型](#策略模型)
          - [RBAC 框架](#rbac-框架)
          - [ABAC 框架](#abac-框架)
          - [Macaroons](#macaroons)
        - [OAuth2 & OpenID](#oauth2--openid)

        <!-- mdformat-toc end -->

        ## 策略模型

        ### RBAC 框架

        ### ABAC 框架

        ### Macaroons

        ## OAuth2 & OpenID
        """)

    formatted = mdformat.text(original, extensions=["recover-urls", "toc"])

    print("原文:", repr(original))
    print("格式化:", repr(formatted))

    assert formatted == expected
