prompts = [
   "Given the following task description, generate Python code that solves the problem efficiently. Ensure the code is well-documented with comments explaining each step and adheres to best practices in terms of readability and performance.",
   "Using the task description below, write a complete Python function that accomplishes the specified task. The code should include error handling, input validation, and comments to explain the logic clearly.",
   "Based on the provided task description, create a Python program that implements the required functionality.",
   "Generate a Python solution for the task described below. ",
   "Given the task description, write a complete and efficient implementation in Python.",
]

import argparse
import os
import json
from tqdm import tqdm
import copy
import openai
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from ast_left_name import check_function_completion


openai.api_key = 'API Key'

def preprocess_data(data):
    if f"```python" in data["completion"]:
        data["completion"] = data["completion"][data["completion"].find(f"```python")+len(f"```python"):]
        data["completion"] = data["completion"][:data["completion"].find("```")]
    elif f"```" in data["completion"]:
        data["completion"] = data["completion"][data["completion"].find(f"```")+len(f"```"):]
        data["completion"] = data["completion"][:data["completion"].find("```")]
    return data


def fetch_completion(data_entry, model,prompt):
    text = prompts[prompt]
    try:
        completions = openai.ChatCompletion.create(
            model=model,
            stream=False,
            messages=[
        {"role": "system", "content": "You are a code developer."},
        {"role": "user", "content":text+f"\n### Input:\n```python"+data_entry["prompt"]+f"\n```\n### Response:"},
            ],
            request_timeout=100,
        )
        data_entry["completion"] = completions.choices[0]["message"]["content"]
        data_entry = preprocess_data(data_entry)
        return data_entry
    except Exception as e:
        print(repr(e))
        data_entry["completion"] = ""
        return data_entry



if __name__ == "__main__":
    model_list = ["gpt-3.5-turbo"]
    for prompt in [0,1,2,3,4]:
        for model in model_list:
            with open(f"./dataset.json", "r") as f:
                dataset = json.load(f)
            dataset = [entry for entry in dataset]
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_to_entry = {executor.submit(fetch_completion, copy.deepcopy(entry), model,prompt): entry for entry in tqdm(dataset)}
                for future in tqdm(concurrent.futures.as_completed(future_to_entry)):
                    entry = future_to_entry[future]
                    try:
                        updated_entry = future.result()
                        idx = dataset.index(entry)
                        dataset[idx] = updated_entry
                    except Exception as e:
                        print(repr(e))
            with open(f"./json_save/{model}_{prompt}.json", "w") as f:
                json.dump(dataset, f, indent=4)