import random
import string

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 生成一个随机字符串，默认长度为10
random_string = generate_random_string()
print(random_string)

import requests
import base64
import json

def get_api_res(text):
    # 设置API访问地址和参数
    url = "http://43.225.216.222:23456/voice/vits"
    headers = {
        "Content-Type": "application/json",
        # "X-API-KEY": "65782ec6a113515a1f11b2d0c58a090f7c769c79e287e20037fd9c2647d74650"
    }
    data = {
        "text": text,
        "id": 25,
        "format": "wav",
        "lang": "auto",
        "length": 0.8,
        "noise": 0.667, 
        "noisew": 0.8,
        "max": 50,
        "streaming": False
    }
    
    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # 解析响应结果
    result = response.json()
    if result["code"] == 200:
        audio_data = base64.b64decode(result["data"]["audio"])
        # t = generate_random_string()
        # with open(f"text{t}.wav", "wb") as f:
        #     f.write(audio_data)
        print(f"语音合成成功,音频文件已保存为 {text}.wav")
    else:
        print(f"语音合成失败,错误信息: {result['message']}")
    return text

get_api_res("这是一个测试语句")


import pandas as pd
import time
from openai import OpenAI
from retrying import retry
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置OpenAI API
openai_api_key = "EMPTY"
openai_api_base = "http://221:2080/v1"

@retry(stop_max_attempt_number=3, wait_fixed=2000)  # 最多重试3次，每次重试间隔2秒
def process_question(question):
    return get_api_res(question)
    # try:
    #     client = OpenAI(
    #         api_key=openai_api_key,
    #         base_url=openai_api_base,
    #     )

    #     chat_response = client.chat.completions.create(
    #         model="Qwen/Qwen1.5-7B-Chat-AWQ",
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {"role": "user", "content": question},
    #         ]
    #     )
    #     return chat_response.choices[0].message.content
    # except Exception as e:
    #     print(f"处理问题时发生错误：{e}")
    #     return ""  # 返回空字符串作为默认值

def process_questions(input_file, output_file, num_threads):
    results = []
    total_answer_length = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        questions = [question.strip() for question in file if question.strip()]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(process_question, question): question for question in questions}
        for future in as_completed(futures):
            question = futures[future]
            answer = future.result()
            answer_length = len(answer)  # 计算answer的长度
            total_answer_length += answer_length  # 累加answer的长度
            results.append([question, answer, answer_length])

    df = pd.DataFrame(results, columns=['Question', 'Answer', 'Answer Length'])

    df.to_excel(output_file, index=False)

    return total_answer_length

def main(input_filename, output_filename, num_threads):
    start_time = time.time()
    total_answer_length = process_questions(input_filename, output_filename, num_threads)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"处理整个文件耗时：{total_time:.2f}秒")
    print(f"生成的全部answer的总长度为：{total_answer_length}个字符")

if __name__ == '__main__':
    input_filename = 'quest.txt'  # 输入文件名
    output_filename = 'processed_quest.xlsx'  # 输出文件名
    num_threads = 20  # 线程数
    main(input_filename, output_filename, num_threads)