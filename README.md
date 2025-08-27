# mdformat-recover-urls

> 适用于 [mdformat](https://github.com/executablebooks/mdformat) 的插件：  
> **恢复**相对链接与锚点中的原始非 ASCII 字符，不做百分号转义。  
> 规则：**凡是以 `.` 开头或以 `#` 开头** 的链接，保留原样（不转义）。

## 利用

隨 `mdformat` 安裝

## 開發

```bash
uv sync

uv run pytest ./test.py
```

## 💡 背景

`mdformat`（经由 `markdown-it-py`）会将 URL 中的非 ASCII 字符百分号转义。  
例如以下写法：

```markdown
[title](./中文.md)
[title](#章节)
```

会被格式化为：

```markdown
[title](./%E4%B8%AD%E6%96%87.md)
[title](#%E7%AB%A0%E8%8A%82)
```

但在不少文档站点（如 VitePress 等）中，需要 **保持文件名和锚点原样**。
本插件的作用是：**对所有以 `.` 开头（相对路径）或以 `#` 开头（锚点）的链接，恢复原始字符，不做转义**。

## ✅ 支持示例

输入：

```markdown
- [title](./en.md)
- [title](./中文.md)
- [title](./日本語.md)
- [title](./العربية.md)

- [title](#en)
- [title](#中文)
- [title](#日本語)
- [title](#العربية)
```

输出（保持原样，不转义）：

```markdown
- [title](./en.md)
- [title](./中文.md)
- [title](./日本語.md)
- [title](./العربية.md)

- [title](#en)
- [title](#中文)
- [title](#日本語)
- [title](#العربية)
```
