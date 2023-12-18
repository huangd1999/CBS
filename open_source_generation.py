# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from tqdm import tqdm

with open("./dataset.json","r") as f:
    dataset = json.load(f)

checkpoint = "codellama/CodeLlama-7b-hf"

prompt = """
Please write the function based on the requirement.
You must complete all code.
The output must in triple backticks format script~(i.e., ```python ```).
You should follow the following rules to write the function:
First, avoid use print, try to use return.
Second, do not write a machine learning model, try just a software function.
"""

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint,device_map = "auto")

for i in tqdm(range(len(dataset))):
    inputs = tokenizer.encode(prompt+dataset[i]["prompt"], return_tensors="pt").to(model.device)
    outputs = model.generate(inputs,max_new_tokens = 256)
    dataset[i]["completion"] = tokenizer.decode(outputs[0])

with open("./json_save/codellama.json","w") as f:
    json.dump(dataset, f, indent=4)

checkpoint = "bigcode/starcoder"

prompt = """
Please write the function based on the requirement.
You must complete all code.
The output must in triple backticks format script~(i.e., ```python ```).
You should follow the following rules to write the function:
First, avoid use print, try to use return.
Second, do not write a machine learning model, try just a software function.
"""

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint,device_map = "auto")

for i in tqdm(range(len(dataset))):
    inputs = tokenizer.encode(prompt+dataset[i]["prompt"], return_tensors="pt").to(model.device)
    outputs = model.generate(inputs,max_new_tokens = 256)
    dataset[i]["completion"] = tokenizer.decode(outputs[0])

with open("./json_save/starcoder.json","w") as f:
    json.dump(dataset, f, indent=4)