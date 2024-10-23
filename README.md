# Odious2Text

Odious2Text 是一个使用 Vosk 语音识别模型将音频文件转换为文本的 Python 项目。
> 注意：此项目只能将语音转换为文本，不能识别说话人。

## 功能

- 支持多种音频格式 (.wav, .mp3, .flac, .aiff, .m4a)
- 使用中文 Vosk 模型进行语音识别
- 批量处理音频文件
- 将识别结果保存为文本文件

## 安装

1. 克隆此仓库:
   ```
   git clone https://github.com/zhoukunlin/odious2text.git
   cd odious2text
   ```

2. 创建并激活虚拟环境:
   
   对于 macOS 和 Linux:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
   对于 Windows:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. 安装依赖:
   ```
   pip install vosk pydub
   ```

4. 下载中文 Vosk 模型（如果项目中未包含）：
   ```
   curl -C - -L https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip -o vosk-model-cn-0.22.zip
   unzip vosk-model-cn-0.22.zip -d vosk-models/
   ```
   注意：
   - 使用 `-C -` 参数支持断点续传，如果下载中断可以继续从断点处下载。
   - 下载完成记得解压，并且是在`vosk-models/` 目录下，如果不是请手动复制粘贴过去。

## 使用方法

1. 将待处理的音频文件放入 `odious` 文件夹。

2. 确保 `odious2text.py` 中的模型路径正确：
   ```python
   model_path = "/path/to/your/vosk-model-cn-0.22"
   ```

3. 运行脚本:
   ```
   python3 odious2text.py
   ```

4. 处理后的文本文件将保存在 `odiousOut` 文件夹中。

## 项目结构

- `odious2text.py`: 主程序脚本
- `odious/`: 存放输入音频文件的文件夹
- `odiousOut/`: 存放输出文本文件的文件夹
- `vosk-models/`: 存放 Vosk 模型的文件夹
- `.venv/`: Python 虚拟环境

## 注意事项

- 确保已正确安装并配置 FFmpeg，以支持各种音频格式的处理。您可以使用以下命令安装 FFmpeg：
  - macOS: `brew install ffmpeg`
  - Ubuntu: `sudo apt-get install ffmpeg`
  - Windows: 下载 FFmpeg 并将其添加到系统路径

- 处理大量或长时间的音频文件可能需要较长时间，请耐心等待。

- 此项目使用的 Vosk 模型配置如下：

```vosk-models/zh-CN/conf/model.conf
startLine: 1
endLine: 10
```

## 许可证

[MIT License](https://opensource.org/licenses/MIT)

## 更多

更多应用欢迎访问我的个人网站：

[zapps.pro](https://zapps.pro)

[zhoukunlin.com.cn](https://zhoukunlin.com.cn)
