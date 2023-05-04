<div class="title" align=center>
    <h1>vits-simple-api</h1>
	<div>Simply call the vits api</div>
    <br/>
    <br/>
    <p>
        <img src="https://img.shields.io/github/license/Artrajz/vits-simple-api">
    	<img src="https://img.shields.io/badge/python-3.9%7C3.10-green">
        <a href="https://hub.docker.com/r/artrajz/vits-simple-api">
            <img src="https://img.shields.io/docker/pulls/artrajz/vits-simple-api"></a>
    </p>
        <a href="https://github.com/Artrajz/vits-simple-api/blob/main/README.md">English</a>|<a href="https://github.com/Artrajz/vits-simple-api/blob/main/README_zh.md">中文文档</a>
    <br/>
</div>




# Feature

- [x] VITS语音合成
- [x] VITS语音转换
- [x] HuBert-soft VITS模型
- [x] W2V2 VITS / emotional-vits维度情感模型
- [x] 加载多模型
- [x] 自动识别语言并处理，支持自定义语言类型范围
- [x] 自定义默认参数
- [x] 长文本批处理
- [x] GPU加速推理
- [ ] SSML语音合成标记语言
- [ ] 根据模型的cleaner设置语言类型识别的范围（可能会移除原本的自定义语言类型范围）

<details><summary>Update Logs</summary><pre><code>
<h2>2023.5.2</h2>
<p>增加w2v2-vits/emotional-vits模型支持，修改了speakers映射表并添加了对应模型支持的语言</p>
<h2>2023.4.23</h2>
<p>增加api key鉴权，默认禁用，需要在config.py中启用</p>
<h2>2023.4.17</h2>
<p>修改单语言的cleaner需要标注才会clean，增加GPU加速推理，但需要手动安装gpu推理环境</p>
<h2>2023.4.12</h2>
<p>项目由MoeGoe-Simple-API更名为vits-simple-api，支持长文本批处理，增加长文本分段阈值max</p>
<h2>2023.4.7</h2>
<p>增加配置文件可自定义默认参数，本次更新需要手动更新config.py，具体使用方法见config.py</p>
<h2>2023.4.6</h2>
<p>加入自动识别语种选项auto，lang参数默认修改为auto，自动识别仍有一定缺陷，请自行选择</p>
<p>统一POST请求类型为multipart/form-data</p>
</code></pre></details>


## demo

- `https://api.artrajz.cn/py/voice/vits?text=你好,こんにちは&id=142`
- 激动：`https://api.artrajz.cn/py/voice/w2v2-vits?text=こんにちは&id=3&emotion=111`
- 小声：`https://api.artrajz.cn/py/voice/w2v2-vits?text=こんにちは&id=3&emotion=2077`

# 部署

## Docker部署

### 镜像拉取脚本

```
bash -c "$(wget -O- https://raw.githubusercontent.com/Artrajz/vits-simple-api/main/vits-simple-api-installer-latest.sh)"
```

- 镜像大小为5GB，安装完成后为8GB，请准备足够的硬盘空间。
- 在拉取完成后，需要导入VITS模型才能使用，请根据以下步骤导入模型。

### 下载VITS模型

将模型放入`/usr/local/vits-simple-api/Model`

<details><summary>Folder structure</summary><pre><code>
├─g
│      config.json
│      G_953000.pth
│
├─louise
│      360_epochs.pth
│      config.json
│      hubert-soft-0d54a1f4.pt
│
├─Nene_Nanami_Rong_Tang
│      1374_epochs.pth
│      config.json
│
└─Zero_no_tsukaima
        1158_epochs.pth
        config.json
</code></pre></details>


### 修改模型路径

Modify in  `/usr/local/vits-simple-api/config.py` 

<details><summary>config.py</summary><pre><code>
For each model, the filling method is as follows 模型列表中每个模型的填写方法如下
example 示例:
MODEL_LIST = [
    #VITS
    [ABS_PATH+"/Model/Nene_Nanami_Rong_Tang/1374_epochs.pth", ABS_PATH+"/Model/Nene_Nanami_Rong_Tang/config.json"],
    [ABS_PATH+"/Model/Zero_no_tsukaima/1158_epochs.pth", ABS_PATH+"/Model/Zero_no_tsukaima/config.json"],
    [ABS_PATH+"/Model/g/G_953000.pth", ABS_PATH+"/Model/g/config.json"],
    #HuBert-VITS
    [ABS_PATH+"/Model/louise/360_epochs.pth", ABS_PATH+"/Model/louise/config.json", ABS_PATH+"/Model/louise/hubert-soft-0d54a1f4.pt"],
]
</code></pre></details>

### 启动

`docker compose up -d`

或者重新执行拉取脚本

### 镜像更新

重新执行docker镜像拉取脚本即可

## 虚拟环境部署

### Clone

`git clone https://github.com/Artrajz/vits-simple-api.git`

###  下载python依赖

推荐使用python的虚拟环境，python版本 >= 3.9

`pip install -r requirements.txt`

windows下可能安装不了fasttext,可以用以下命令安装，附[wheels下载地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext)

```
#python3.10 win_amd64
pip install https://github.com/Artrajz/archived/raw/main/fasttext/fasttext-0.9.2-cp310-cp310-win_amd64.whl
#python3.9 win_amd64
pip install https://github.com/Artrajz/archived/raw/main/fasttext/fasttext-0.9.2-cp39-cp39-win_amd64.whl
```

### 下载VITS模型

将模型放入 `/path/to/vits-simple-api/Model`

<details><summary>文件夹结构</summary><pre><code>
├─g
│      config.json
│      G_953000.pth
│
├─louise
│      360_epochs.pth
│      config.json
│      hubert-soft-0d54a1f4.pt
│
├─Nene_Nanami_Rong_Tang
│      1374_epochs.pth
│      config.json
│
└─Zero_no_tsukaima
        1158_epochs.pth
        config.json
</code></pre></details>

### 修改模型路径

在 `/path/to/vits-simple-api/config.py` 修改

<details><summary>config.py</summary><pre><code>
For each model, the filling method is as follows 模型列表中每个模型的填写方法如下
example 示例:
MODEL_LIST = [
    #VITS
    [ABS_PATH+"/Model/Nene_Nanami_Rong_Tang/1374_epochs.pth", ABS_PATH+"/Model/Nene_Nanami_Rong_Tang/config.json"],
    [ABS_PATH+"/Model/Zero_no_tsukaima/1158_epochs.pth", ABS_PATH+"/Model/Zero_no_tsukaima/config.json"],
    [ABS_PATH+"/Model/g/G_953000.pth", ABS_PATH+"/Model/g/config.json"],
    #HuBert-VITS
    [ABS_PATH+"/Model/louise/360_epochs.pth", ABS_PATH+"/Model/louise/config.json", ABS_PATH+"/Model/louise/hubert-soft-0d54a1f4.pt"],
]
</code></pre></details>

### 启动

`python app.py`

# GPU 加速

## windows

### 安装CUDA

查看显卡最高支持CUDA的版本

```
nvidia-smi
```

以CUDA11.7为例，[官网](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)

### 安装GPU版pytorch

CUDA11.7对应的pytorch是用这个命令安装

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

对应版本的命令可以在[官网](https://pytorch.org/get-started/locally/)找到

## Linux

安装过程类似，但我没有相应的环境所以没办法测试

# API

## GET

#### speakers list 

- GET http://127.0.0.1:23456/voice/speakers

  返回id对应角色的映射表

#### voice vits

- GET http://127.0.0.1/voice?text=text

  其他参数不指定时均为默认值

- GET http://127.0.0.1/voice?text=[ZH]text[ZH][JA]text[JA]&lang=mix

  lang=mix时文本要标注

- GET http://127.0.0.1/voice?text=text&id=142&format=wav&lang=zh&length=1.4

  文本为text，角色id为142，音频格式为wav，文本语言为zh，语音长度为1.4，其余参数默认

#### check

- GET http://127.0.0.1:23456/voice/check?id=0&model=vits

## POST

- python

```python
import re
import requests
import os
import random
import string
from requests_toolbelt.multipart.encoder import MultipartEncoder

abs_path = os.path.dirname(__file__)
base = "http://127.0.0.1:23456"


# 映射表
def voice_speakers():
    url = f"{base}/voice/speakers"

    res = requests.post(url=url)
    json = res.json()
    for i in json:
        print(i)
        for j in json[i]:
            print(j)


# 语音合成 voice vits
def voice_vits(text, id=0, format="wav", lang="auto", length=1, noise=0.667, noisew=0.8, max=50):
    fields = {
        "text": text,
        "id": str(id),
        "format": format,
        "lang": lang,
        "length": str(length),
        "noise": str(noise),
        "noisew": str(noisew),
        "max": str(max)
    }
    boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {"Content-Type": m.content_type}
    url = f"{base}/voice"

    res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)


# 语音转换 hubert-vits
def voice_hubert_vits(upload_path, speaker_id, format="wav", length=1, noise=0.667, noisew=0.8):
    upload_name = os.path.basename(upload_path)
    upload_type = f'audio/{upload_name.split(".")[1]}'  # wav,ogg

    with open(upload_path, 'rb') as upload_file:
        fields = {
            "upload": (upload_name, upload_file, upload_type),
            "speaker_id": str(speaker_id),
            "format": format,
            "length": str(length),
            "noise": str(noise),
            "noisew": str(noisew),
        }
        boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        m = MultipartEncoder(fields=fields, boundary=boundary)
        headers = {"Content-Type": m.content_type}
        url = f"{base}/voice/hubert-vits"

        res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)

# 维度情感模型 w2v2-vits
def voice_w2v2_vits(text, id=0, format="wav", lang="auto", length=1, noise=0.667, noisew=0.8, max=50, emotion=0):
    fields = {
        "text": text,
        "id": str(id),
        "format": format,
        "lang": lang,
        "length": str(length),
        "noise": str(noise),
        "noisew": str(noisew),
        "max": str(max),
        "emotion": str(emotion)
    }
    boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {"Content-Type": m.content_type}
    url = f"{base}/voice/w2v2-vits"

    res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)


# 语音转换 同VITS模型内角色之间的音色转换
def voice_conversion(upload_path, original_id, target_id):
    upload_name = os.path.basename(upload_path)
    upload_type = f'audio/{upload_name.split(".")[1]}'  # wav,ogg

    with open(upload_path, 'rb') as upload_file:
        fields = {
            "upload": (upload_name, upload_file, upload_type),
            "original_id": str(original_id),
            "target_id": str(target_id),
        }
        boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        m = MultipartEncoder(fields=fields, boundary=boundary)

        headers = {"Content-Type": m.content_type}
        url = f"{base}/voice/conversion"

        res = requests.post(url=url, data=m, headers=headers)

    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
```

## API KEY

在config.py中设置`API_KEY_ENABLED = True`以启用，api key填写：`API_KEY = "api-key"`。

启用后，GET请求中使用需要增加参数api_key，POST请求中使用需要在header中添加参数`X-API-KEY`。

# Parameter

## VITS语音合成

| Name          | Parameter | Is must | Default | Type  | Instruction                                                  |
| ------------- | --------- | ------- | ------- | ----- | ------------------------------------------------------------ |
| 合成文本      | text      | true    |         | str   |                                                              |
| 角色id        | id        | false   | 0       | int   |                                                              |
| 音频格式      | format    | false   | wav     | str   | wav,ogg,silk                                                 |
| 文本语言      | lang      | false   | auto    | str   | auto为自动识别语言模式，也是默认模式。lang=mix时，文本应该用[ZH] 或 [JA] 包裹, |
| 语音长度/语速 | length    | false   | 1.0     | float | 调节语音长度，相当于调节语速，该数值越大语速越慢             |
| 噪声          | noise     | false   | 0.667   | float |                                                              |
| 噪声偏差      | noisew    | false   | 0.8     | float |                                                              |
| 分段阈值      | max       | false   | 50      | int   | 按标点符号分段，加起来大于max时为一段文本。max<=0表示不分段。 |

## VITS 语音转换

| Name       | Parameter   | Is must | Default | Type | Instruction            |
| ---------- | ----------- | ------- | ------- | ---- | ---------------------- |
| 上传音频   | upload      | true    |         | file | wav or ogg             |
| 源角色id   | original_id | true    |         | int  | 上传文件所使用的角色id |
| 目标角色id | target_id   | true    |         | int  | 要转换的目标角色id     |

## HuBert-VITS 语音转换

| Name          | Parameter  | Is must | Default | Type  | Instruction                                      |
| ------------- | ---------- | ------- | ------- | ----- | ------------------------------------------------ |
| 上传音频      | upload     | true    |         | file  |                                                  |
| 目标角色id    | speaker_id | true    |         | int   |                                                  |
| 音频格式      | format     | true    |         | str   | wav,ogg,silk                                     |
| 语音长度/语速 | length     | true    |         | float | 调节语音长度，相当于调节语速，该数值越大语速越慢 |
| 噪声          | noise      | true    |         | float |                                                  |
| 噪声偏差      | noisew     | true    |         | float |                                                  |

## W2V2-VITS

| Name          | Parameter | Is must | Default | Type  | Instruction                                                  |
| ------------- | --------- | ------- | ------- | ----- | ------------------------------------------------------------ |
| 合成文本      | text      | true    |         | str   |                                                              |
| 角色id        | id        | false   | 0       | int   |                                                              |
| 音频格式      | format    | false   | wav     | str   | wav,ogg,silk                                                 |
| 文本语言      | lang      | false   | auto    | str   | auto为自动识别语言模式，也是默认模式。lang=mix时，文本应该用[ZH] 或 [JA] 包裹, |
| 语音长度/语速 | length    | false   | 1.0     | float | 调节语音长度，相当于调节语速，该数值越大语速越慢             |
| 噪声          | noise     | false   | 0.667   | float |                                                              |
| 噪声偏差      | noisew    | false   | 0.8     | float |                                                              |
| 分段阈值      | max       | false   | 50      | int   | 按标点符号分段，加起来大于max时为一段文本。max<=0表示不分段。 |
| 维度情感      | emotion   | false   | 0       | int   | 范围取决于npy情感参考文件，如[innnky](https://huggingface.co/spaces/innnky/nene-emotion/tree/main)的all_emotions.npy模型范围是0-5457 |

# 交流平台

现在只有 [Q群](https://qm.qq.com/cgi-bin/qm/qr?k=-1GknIe4uXrkmbDKBGKa1aAUteq40qs_&jump_from=webapi&authKey=x5YYt6Dggs1ZqWxvZqvj3fV8VUnxRyXm5S5Kzntc78+Nv3iXOIawplGip9LWuNR/)

# 鸣谢

- vits:https://github.com/jaywalnut310/vits
- MoeGoe:https://github.com/CjangCjengh/MoeGoe
- emotional-vits:https://github.com/innnky/emotional-vits
- vits-uma-genshin-honkai:https://huggingface.co/spaces/zomehwh/vits-uma-genshin-honkai
