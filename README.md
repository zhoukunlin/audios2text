# Audio2Text

Audio2Text 是一个强大的 Python 项目，利用 Vosk 语音识别模型将音频文件转换为文本。

> 注意：此项目专注于语音到文本的转换，不具备说话人识别功能。

## 主要特性

- 支持多种音频格式（.wav, .mp3, .flac, .aiff, .m4a）
- 采用中文 Vosk 模型进行高精度语音识别
- 支持批量处理音频文件
- 将识别结果以文本形式保存

## 安装指南

1. 克隆仓库并进入项目目录：
   ```
   git clone https://github.com/zhoukunlin/audios2text.git
   cd audios2text
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

   ```
   curl -C - -L https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip -o vosk-model-cn-0.22.zip
   unzip vosk-model-cn-0.22.zip -d vosk-models/
   ```

   注意事项：
   - `-C -` 参数支持断点续传
   - 解压后将模型放入 `vosk-models/` 目录

## 使用方法

1. 将待处理音频文件放入 `audio` 文件夹。

2. 运行脚本：
   ```
   python3 audio2text.py
   ```

3. 转换后的文本文件将保存在 `audioOut` 文件夹中。

## 项目结构

- `audio2text.py`：主程序脚本
- `audio/`：输入音频文件目录
- `audioOut/`：输出文本文件目录
- `vosk-models/`：Vosk 模型存储目录
- `.venv/`：Python 虚拟环境

## 注意事项

- 请确保正确安装并配置 FFmpeg，以支持各种音频格式。安装命令：
  - macOS: `brew install ffmpeg`
  - Ubuntu: `sudo apt-get install ffmpeg`
  - Windows: 下载 FFmpeg 并添加到系统路径

- 处理大量或长时间的音频文件可能需要较长时间，请耐心等待。

- 如果遇到 "模型不存在" 的错误，请检查以下几点：
  1. 确保已下载并解压 Vosk 模型到 `vosk-models` 目录。
  2. 检查模型文件夹的权限，确保程序有读取权限。

- 首次运行时，模型加载可能需要一些时间，这是正常现象。

- 对于较大的音频文件，可能需要更多的内存和处理时间。

- 如果遇到与模型配置相关的错误，程序会自动删除 `mfcc.conf` 和 `model.conf` 文件。这不会影响模型的性能，因为 Vosk 会使用默认的配置。

- 如果仍然遇到 "Failed to find feature config file" 错误，请确保模型文件夹中包含所有必要的文件。您可以尝试重新下载并解压模型文件。

- 确保您的 Python 环境中安装了正确版本的 Vosk 库。您可以尝试更新 Vosk：
  ```
  pip install --upgrade vosk
  ```

## 许可证

[MIT License](https://opensource.org/licenses/MIT)

## 更多

更多应用欢迎访问我的个人网站：

[zapps.pro](https://zapps.pro)

[zhoukunlin.com.cn](https://zhoukunlin.com.cn)

## 贡献

欢迎提交问题和拉取请求。对于重大更改，请先开issue讨论您想要更改的内容。

## 致谢

感谢 Vosk 项目提供的优秀语音识别模型。
