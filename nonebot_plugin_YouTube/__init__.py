import re
import base64
import requests

from io import BytesIO

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from nonebot.plugin import PluginMetadata

__version__ = "0.1.1.post1"
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_Youtube",
    description="Youtube多功能视频解析",
    usage="使用：检测到YouTube视频链接自动触发",
    homepage="https://github.com/Perseus037/nonebot_plugin_YouTube",
    type="application",
    config=None,
    supported_adapters={"~onebot.v11"},
)

#正则表达式匹配链接，增设shorts类型的链接
youtube_regex = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([0-9A-Za-z_-]{11})"
youtube_handler = on_regex(youtube_regex, priority=5)

# 输入 YouTube Data API 密钥
youtube_api_key = "在这里输入你的api密匙"

# 使用全分辨率的预览图
use_max_resolution_thumbnails = False

# 视频简介最大长度
description_maximun_length = 200

# 若使用代理，请填写在下方
proxies = {
    # "https": "http://ip:port",
    # "http" : "http://ip:port"
}

# Youtube视频种类对照表，ref: https://qiita.com/nabeyaki/items/c3d0421538c8faacb130
categoriesIdInfo = {
    "1" : "Film & Animation",
    "2" : "Autos & Vehicles",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "19": "Travel & Events",
    "20": "Gaming",
    "22": "People & Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology"
}


@youtube_handler.handle()
async def handle_youtube_link(bot: Bot, event: MessageEvent):
    message_text = event.get_plaintext()
    video_id = extract_youtube_id(message_text)

    if video_id:
        video_info = get_youtube_video_info(video_id, youtube_api_key)
        if video_info:
            image_base64 = get_image_base64(video_info['thumbnail'])

            if image_base64:
                await youtube_handler.finish(wrap_youtube_event(image_base64, video_info))
            else:
                await youtube_handler.finish("无法获取视频封面。")
        else:
            await youtube_handler.finish("无法获取视频信息。")
    else:
        await youtube_handler.finish("未检测到有效的 YouTube 链接。")


def wrap_youtube_event(image_base64, vedio_info: dict):
    # 将视频信息打包成消息
    info_string = '\n'.join([
        f"标题 : {vedio_info['title']}",
        f'播放 : {vedio_info["viewCount"]} | 喜欢 : {vedio_info["likeCount"]} | 收藏 : {vedio_info["favoriteCount"]}',
        f"类型 : {vedio_info['category']} | 频道 : {vedio_info['channelTitle']} | 日期 : {vedio_info['publishedAt']}",
        f'标签 : {", ".join([i for i in vedio_info["tags"]])}',
        f"简介 : {vedio_info['description']}"
    ])
    return MessageSegment.image(f'base64://{image_base64}') + "\n" + info_string


def extract_youtube_id(url: str):
    # 使用正则表达式提取视频ID
    regex = r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([0-9A-Za-z_-]{11})"
    matches = re.search(regex, url)

    if matches:
        print(matches.group(1))
        return matches.group(1)

    return None


def get_youtube_video_info(video_id: str, api_key: str):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&part=statistics&id={video_id}&key={api_key}&part=snippet"
    response = requests.get(url, proxies=proxies, timeout=3)

    if response.status_code == 200:
        return_dict = {}
        
        data = response.json()
        items = data.get("items")

        if items and len(items) > 0:
            item = items[0]["snippet"]
            statistics = items[0]["statistics"]
            if use_max_resolution_thumbnails:
                item["thumbnails"] = item["thumbnails"]["maxres"]
            else:
                item["thumbnails"] = item["thumbnails"]["high"]
            
            prefix = ''
            if  item['liveBroadcastContent'] == 'live':
                prefix ='【直播】 ' 
                
            
            if len(item['description']) > description_maximun_length:
                item['description'] = item['description'][:description_maximun_length] + '\n...'
                
            
            return {
                # 视频标题
                "title": prefix + item["title"],
                # 视频略缩图
                "thumbnail": item["thumbnails"]["url"],
                # 视频标签
                "tags": item["tags"][:10] if 'tags' in item else '无',
                # 简介
                "description": item["description"] if 'description' in item else '无',
                # 频道名
                "channelTitle": item["channelTitle"],
                # 视频分区
                "category": categoriesIdInfo[item['categoryId']],
                # 时间
                "publishedAt": item["publishedAt"].split("T")[0],
                # 播放数
                "viewCount": statistics["viewCount"],
                # 获赞数
                "likeCount": statistics['likeCount'],
                # 收藏数
                "favoriteCount": statistics['favoriteCount'],
                # 评论数
                "commentCount": statistics['commentCount']
            }

    return None


def get_image_base64(image_url: str):
    response = requests.get(image_url, proxies=proxies, timeout=3)

    if response.status_code == 200:
        return base64.b64encode(BytesIO(response.content).read()).decode()
    return None
