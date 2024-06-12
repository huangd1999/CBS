import json
from codebleu import calc_codebleu


model_list = ["palm-2-codechat-bison", "claude-instant-1","gpt-4-turbo-preview","gpt-3.5-turbo","gpt-4"]
for model in model_list:
    with open(f"../json_save/{model}.json", "r") as f:
        original_dataset = json.load(f)
    bleu_lists = []
    for prompt in ["zero_shot","one_shot","few_shot","CoT_1","CoT_2"]:
        with open(f"../new_dataset/bias_mitigation_{model}_{prompt}.json", "r") as f:
            dataset = json.load(f)
        
        total_bleu = 0
        total_cases = 0
        bias = {"age": 0, "region": 0, "gender": 0, "education": 0,"occupation":0,"race": 0}
        for i in range(len(original_dataset)):

            prediction = original_dataset[i]["completion"]
            reference = dataset[i]["completion"]
            analysis = False
            for key in bias.keys():
                if f"if {key}" in prediction:
                    analysis = True
            if not analysis:
                continue
            bleu = calc_codebleu([reference], [prediction], lang="python", tokenizer=None)["codebleu"]
            total_bleu+=bleu
            total_cases+=1

        bleu_lists.append(total_bleu/total_cases)


    print(f"{model}","&".join([str(round(bleu,2)) for bleu in bleu_lists]))