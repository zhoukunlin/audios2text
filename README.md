# Odious2Text

Odious2Text 是一个强大的 Python 项目，利用 Vosk 语音识别模型将音频文件转换为文本。

> 注意：此项目专注于语音到文本的转换，不具备说话人识别功能。

## 主要特性

- 支持多种音频格式（.wav, .mp3, .flac, .aiff, .m4a）
- 采用中文 Vosk 模型进行高精度语音识别
- 支持批量处理音频文件
- 将识别结果以文本形式保存

## 安装指南

1. 克隆仓库并进入项目目录：
   ```
   git clone https://github.com/zhoukunlin/odious2text.git
   cd odious2text
   ```

2. 创建并激活虚拟环境：
   
   macOS 和 Linux：
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
   Windows：
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. 安装所需依赖：
   ```
   pip install vosk pydub
   ```

4. 下载中文 Vosk 模型：
   
   项目默认包含一个小型模型（`vosk-models/zh-CN`）。如需更高精度，可下载约 1.3GB 的大型模型：

   ```
   curl -C - -L https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip -o vosk-model-cn-0.22.zip
   unzip vosk-model-cn-0.22.zip -d vosk-models/
   ```

   注意事项：
   - `-C -` 参数支持断点续传
   - 解压后将模型放入 `vosk-models/` 目录，与 `zh-CN/` 同级
   - 使用大型模型时，需修改 `odious2text.py` 中的模型路径

## 使用方法

1. 将待处理音频文件放入 `odious` 文件夹。

2. 确保 `odious2text.py` 中的模型路径正确：
   ```python
   model_path = "../odious2text/vosk-models/vosk-model-cn-0.22"
   ```

3. 运行脚本：
   ```
   python3 odious2text.py
   ```

4. 转换后的文本文件将保存在 `odiousOut` 文件夹中。

## 项目结构

- `odious2text.py`：主程序脚本
- `odious/`：输入音频文件目录
- `odiousOut/`：输出文本文件目录
- `vosk-models/`：Vosk 模型存储目录
- `.venv/`：Python 虚拟环境

## 注意事项

- 请确保正确安装并配置 FFmpeg，以支持各种音频格式。安装命令：
  - macOS: `brew install ffmpeg`
  - Ubuntu: `sudo apt-get install ffmpeg`
  - Windows: 下载 FFmpeg 并添加到系统路径

- 处理大量或长时间的音频文件可能需要较长时间，请耐心等待。

- 项目使用的 Vosk 模型配置如下：

## 许可证

[MIT License](https://opensource.org/licenses/MIT)

## 更多

更多应用欢迎访问我的个人网站：

[zapps.pro](https://zapps.pro)

[zhoukunlin.com.cn](https://zhoukunlin.com.cn)
