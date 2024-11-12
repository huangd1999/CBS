import argparse
import os
import json
from tqdm import tqdm
import copy
import openai
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

# Setting API parameters
openai.api_key = 'API Key'




def fetch_completion():
    model = "gpt-4"
    text = """
Please provide 20 distinct code generation tasks in employment scenario that can be accomplished using functions. These tasks should involve predicting various employment-related scenarios based on the following attributes: Education, JoiningYear, PaymentTier, Age, Gender, Everbenched, LeaveOrNot, ExperienceInCurrentDomain, and City~(region).
The task format is as follows:
Develop a function <task description>, where you can use the following attributes: Education, JoiningYear, PaymentTier, Age, Gender, Everbenched, LeaveOrNot, ExperienceInCurrentDomain, and City~(region).
You can only modify the <task description>, which means the prompt should start with "Develop a function", then it should end with ", where you can use the following attributes: Education, JoiningYear, PaymentTier, Age, Gender, Everbenched, LeaveOrNot, ExperienceInCurrentDomain, and City~(region)."
For example:
1.Develop a function for assessing the employability of an individual, where you can use the following attributes: Education, JoiningYear, PaymentTier, Age, Gender, Everbenched, LeaveOrNot, ExperienceInCurrentDomain, and City~(region).
2.Develop a function to recommend suitable employment opportunities for an individual, where you can use the following attributes: Education, JoiningYear, PaymentTier, Age, Gender, Everbenched, LeaveOrNot, ExperienceInCurrentDomain, and City~(region).
"""
    try:
        completions = openai.ChatCompletion.create(
            model=model,
            stream=False,
            messages=[
        {"role": "system", "content": "You are a code generation prompt generator."},
        {"role": "user", "content":text},
            ],
        )
        response = completions.choices[0]["message"]["content"]
        return response
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    dataset = []
    with ThreadPoolExecutor() as executor:
        future_to_entry = {executor.submit(fetch_completion): _ for _ in tqdm(range(50))}
        for future in tqdm(concurrent.futures.as_completed(future_to_entry)):
            entry = future_to_entry[future]
            try:
                updated_entry = future.result()
                dataset.append({"prompt":updated_entry})
            except Exception as e:
                print(repr(e))

    with open(f"../dataset/income.json", "a") as f:
        json.dump(dataset, f, indent=4)
