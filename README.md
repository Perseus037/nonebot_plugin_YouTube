<div align="center">
  <img src="https://github.com/Perseus037/data/blob/master/youtube.png" width="280" height="280" alt="YouTube视频解析图标" >

# noneBot-plugin-YouTube

_ 一个多功能的youtube视频解析nonebot2插件 _

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<!-- <a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb.svg" alt="wakatime">
</a> -->

<br />

<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-uma.svg" alt="license">
</a>

</div>

<div align="left">

## 📖 介绍

实现youtube视频链接解析，并输出封面和标题信息

给asmr群的烤肉man和群友写的，目前仍处于开发状态。

ps：有任何问题或建议可以直接提issue或者发email到qq邮箱，我会尽快解决/实现喵。

## 💿 安装

开发中，没发包，无法使用包管理器安装。

如果使用gitclone安装的话，请将文件下载到site—package文件夹下，
然后打开 nonebot2 项目根目录下的 `pyproject.toml` 文件,在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入nonebot_plugin_babattleline即可

<!--
<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot_plugin_batarot
```
-->

</details>

<details open>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>pip</summary>

```bash
pip install nonebot_plugin_batarot
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot_plugin_batarot
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot_plugin_batarot
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot_plugin_batarot
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_batarot"
]
```

</details>

## ⚙️ 配置

无需配置，开箱即用。

## 🎉 使用

检测到youtube链接后自动发送一条消息，包含YouTube视频封面和标题
 
## 📞 制作者

### 黑纸折扇 [Perseus037] (https://github.com/Perseus037)

QQ：1209228678

## 🙏 感谢

### student_2333 (https://github.com/lgc2333) 对于我学习编写插件和配置qqbot等过程中的无私帮助

## 📝 更新日志

### 0.1.0
- 实现最基本的功能，检测到youtube链接后输出视频封面和标题
