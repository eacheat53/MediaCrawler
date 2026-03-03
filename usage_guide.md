# MediaCrawler 使用说明

## 快速开始

### 环境准备

```bash
# 激活虚拟环境
.venv/Scripts/Activate.ps1

# 或直接使用 uv run（无需激活虚拟环境）
uv run main.py --help
```

---

## CLI 命令格式

```bash
uv run main.py [OPTIONS]
```

### 核心参数

| 参数 | 可选值 | 说明 |
|---|---|---|
| `--platform` | `xhs` `dy` `ks` `bili` `wb` `tieba` `zhihu` | 目标平台 |
| `--type` | `search` `detail` `creator` | 爬取模式 |
| `--urls` | URL字符串（逗号分隔） | 直接指定目标URL，覆盖配置文件 |
| `--keywords` | 关键词（逗号分隔） | search 模式的搜索关键词 |
| `--lt` | `qrcode` `phone` `cookie` | 登录方式 |
| `--get_comment` | `true` / `false` | 是否爬取评论 |
| `--get_sub_comment` | `true` / `false` | 是否爬取二级评论 |
| `--save_data_option` | `json` `csv` `db` `sqlite` `excel` | 数据保存格式 |

---

## 三种爬取模式

### 1. `detail` — 指定帖子下载

下载指定视频/图集的内容。URL 来源：`--urls` 参数 或 配置文件中的 `*_SPECIFIED_ID_LIST`。

```bash
# 下载单个抖音视频/图集
uv run main.py --platform dy --type detail --urls "https://www.iesdouyin.com/share/video/7607137357246244581/"

# 下载多个（逗号分隔）
uv run main.py --platform dy --type detail --urls "https://www.douyin.com/video/xxx,https://v.douyin.com/yyy/"

# 也支持直接填纯 ID
uv run main.py --platform dy --type detail --urls "7607137357246244581"
```

### 2. `creator` — 创作者主页爬取

爬取指定创作者发布的所有作品。URL 来源：`--urls` 参数 或 配置文件中的 `*_CREATOR_ID_LIST`。

```bash
# 爬取某个抖音创作者的所有作品
uv run main.py --platform dy --type creator --urls "https://www.douyin.com/user/MS4wLjABAAAAxxx"
```

### 3. `search` — 关键词搜索

按关键词搜索并爬取结果。

```bash
# 搜索关键词
uv run main.py --platform dy --type search --keywords "Python教程,编程入门"
```

---

## 配置文件 vs CLI 参数

> [!IMPORTANT]
> CLI 参数**优先于**配置文件。传入 `--urls` 时会直接覆盖配置文件中定义的 ID 列表。

| 优先级 | 来源 | 说明 |
|---|---|---|
| 🥇 高 | CLI `--urls` | 命令行直接传入，立即生效 |
| 🥈 低 | `config/dy_config.py` | 配置文件中的 `DY_SPECIFIED_ID_LIST` 等 |

### 配置文件路径

```
config/
├── base_config.py       # 全局基础配置（平台、模式、代理、浏览器等）
├── dy_config.py         # 抖音平台配置（ID 列表）
├── xhs_config.py        # 小红书平台配置
├── ks_config.py         # 快手平台配置
├── bilibili_config.py   # B站平台配置
├── weibo_config.py      # 微博平台配置
├── tieba_config.py      # 贴吧平台配置
└── zhihu_config.py      # 知乎平台配置
```

### 关键全局配置 (`base_config.py`)

```python
ENABLE_CDP_MODE = True     # 是否使用 CDP 模式（推荐开启，反检测更强）
HEADLESS = False           # 是否无头模式
ENABLE_GET_MEIDAS = True   # 是否下载媒体文件（图片/视频）
ENABLE_GET_COMMENTS = False # 是否爬取评论
SAVE_DATA_OPTION = "json"  # 数据保存格式
```

---

## 数据输出

下载的数据保存在 `data/` 目录下：

```
data/
└── douyin/
    ├── json/              # 帖子元数据（JSON格式）
    ├── images/            # 图集图片
    │   └── {aweme_id}/    # 按作品ID分文件夹
    │       ├── 000.jpeg
    │       ├── 001.jpeg
    │       └── ...
    └── videos/            # 视频文件
        └── {aweme_id}/
            └── video.mp4
```

---

## 常用命令速查

```bash
# 查看帮助
uv run main.py --help

# 抖音：下载指定图集
uv run main.py --platform dy --type detail --urls "URL"

# 抖音：爬取创作者所有作品
uv run main.py --platform dy --type creator --urls "创作者主页URL"

# 抖音：搜索关键词
uv run main.py --platform dy --type search --keywords "关键词1,关键词2"

# 小红书：下载指定笔记
uv run main.py --platform xhs --type detail --urls "笔记URL"

# 保存为 Excel 格式
uv run main.py --platform dy --type detail --urls "URL" --save_data_option excel
```
