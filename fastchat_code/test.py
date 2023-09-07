import json
import os

data={}

def read_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_json(path,data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

ques=read_json('yutao/fastchat/no_mem(1)(1).json')
for app in ques:
    data[app]={}
    for index in ques[app]:
        ques_list=[]
        for ask in ques[app][index]:
            save_json('yutao/fastchat/middle_ques.json',ask)
            os.system('python3 -m fastchat.serve.cli --model lmsys/vicuna-7b-v1.5')
            ques_list.append(read_json('yutao/fastchat/middle_res.json'))
        data[app][index]=ques_list
        save_json('yutao/fastchat/no_mem(1)(1)_res.json',data)

