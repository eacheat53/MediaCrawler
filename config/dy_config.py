# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/config/dy_config.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# Douyin platform configuration
PUBLISH_TIME_TYPE = 0

# Specify DY video URL list (supports multiple formats)
# Supported formats:
# 1. Full video URL: "https://www.douyin.com/video/7525538910311632128"
# 2. URL with modal_id: "https://www.douyin.com/user/xxx?modal_id=7525538910311632128"
# 3. The search page has modal_id: "https://www.douyin.com/root/search/python?modal_id=7525538910311632128"
# 4. Short link: "https://v.douyin.com/drIPtQ_WPWY/"
# 5. Pure video ID: "7280854932641664319"
DY_SPECIFIED_ID_LIST = [
    # "https://www.douyin.com/video/7525538910311632128",
]

# Specify DY creator URL list (supports full URL or sec_user_id)
# Supported formats:
# 1. Complete creator homepage URL: "https://www.douyin.com/user/MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE?from_tab_name=main"
# 2. sec_user_id: "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE"
DY_CREATOR_ID_LIST = [
    "https://www.douyin.com/user/MS4wLjABAAAAc8ys-j0GmPG7aKrFDde43dcPNc1ag1i69-kUlcvAm6fovmxaO1C_0GX6KEoAhNt4?from_tab_name=main&vid=7654559078303920613",
]

# 是否开启按热度指标排序下载（仅在CRAWLER_TYPE为creator时生效）
DY_CREATOR_DOWNLOAD_SORT_BY_PLAY_COUNT = True

# 排序指标选项: 'play_count' (播放量), 'digg_count' (点赞数), 'comment_count' (评论数), 'share_count' (分享数), 'collect_count' (收藏数)
# 注意：抖音网页版公开接口返回的 play_count 字段通常恒为 0，因此推荐使用 'digg_count' (点赞数) 进行热度排序。
DY_CREATOR_DOWNLOAD_SORT_FIELD = "digg_count"

# 排序后，只下载排名前 N 的作品
DY_CREATOR_DOWNLOAD_TOP_N = 9
