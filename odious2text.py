import os
from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
from pydub import AudioSegment
import logging

logging.basicConfig(level=logging.INFO)

def audio_to_text_vosk(audio_file, model_path):
    SetLogLevel(-1)  # 禁用 Vosk 日志输出

    # 检查模型是否存在
    if not os.path.exists(model_path):
        logging.error(f"模型不存在: {model_path}")
        return "模型不存在，无法识别音频"

    try:
        model = Model(model_path)
        logging.info(f"成功加载模型: {model_path}")
    except Exception as e:
        logging.error(f"加载模型失败: {str(e)}")
        return "加载模型失败，无法识别音频"
    
    # 如果是 m4a 文件，先转换为 wav
    if audio_file.endswith('.m4a'):
        audio = AudioSegment.from_file(audio_file, format="m4a")
        wav_file = audio_file.replace('.m4a', '.wav')
        audio.export(wav_file, format="wav")
    else:
        wav_file = audio_file

    # 打开音频文件
    wf = wave.open(wav_file, "rb")
    
    # 创建识别器
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # 读取音频数据
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    # 获取识别结果
    result = json.loads(rec.FinalResult())

    # 如果创建了临时 wav 文件，删除它
    if audio_file.endswith('.m4a'):
        os.remove(wav_file)

    return result['text']

def process_audio_files(input_dir, output_dir, model_path):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(('.wav', '.mp3', '.flac', '.aiff', '.m4a')):  # 支持的音频格式
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
            
            try:
                # 转换音频到文字
                result = audio_to_text_vosk(input_path, model_path)
                
                # 将结果写入文本文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                
                logging.info(f"处理完成: {filename}")
            except Exception as e:
                logging.error(f"处理 {filename} 时出错: {str(e)}")

# 使用示例
input_directory = "odious"
output_directory = "odiousOut"
model_path = "../odious2text/vosk-models/vosk-model-cn-0.22"
process_audio_files(input_directory, output_directory, model_path)
