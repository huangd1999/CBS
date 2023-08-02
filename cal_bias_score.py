from datasets import load_dataset
from tqdm import tqdm
import json
# dataset = load_dataset("json", data_files="./dataset/few-shot-gpt-3.5-turbo-0301.json")
with open("./dataset/one-shot-codet5p-770m-py.json","r") as fp:
    dataset = json.load(fp)

data = []
bias_type = {"Age": 0, "Region": 0, "Gender": 0, "Lookism": 0, "Economic": 0, "Education": 0, "Other Bias": 0, "Ethics": 0, "Unfairness or Discrimination": 0, "Crimes or Illegal Activities": 0, "Physical Harm": 0, "Mental Health": 0, "Privacy or Property": 0, "Ethics or Morality": 0, "Other Unsafety": 0}
for i in tqdm(range(len(dataset))):
    data.append(dataset[i]["bias"])


with open("./dataset/biask/one-shot-codet5p-770m-py.json","w") as fp:
    json.dump(data,fp,indent=4)



# import json
# from tqdm import tqdm
# bias_type = {"Age":0, "Region":0,"Gender":0, "Economic":0,"Education":0,"Race":0,"Ethnicity":0,"Religion":0,"Sexual":0,"Other Bias":0}
# model_list = ["modified-codet5p-770m-py","modified-codegen-2B-mono","modified-codegen2-1B","modified-llama-bias-800cases-5trials","modified-gpt-neo-1.3B","modified-santacoder","modified-incoder-1B","modified-gpt-3.5-turbo"]

# with open("./dataset/modified-calculate_bias_type_samples.json","r") as fp:
#     data = json.load(fp)

# for i in tqdm(range(len(data))):
#     bias_dict = data[i]
#     print(bias_dict)
#     for key in bias_type.keys():
#         if key in bias_dict.keys() and bias_dict[key] == True:
#             bias_type[key] += 1
# print(bias_type)
# print(len(data))


# dataset = ["modified-codegen-2B-mono","modified-codegen2-1B","modified-gpt-3.5-turbo-0301","modified-gpt-neo-1.3B","modified-incoder-1B","modified-llama7b-codealapaca-120k-bias-841cases","modified-codet5p-6b","modified-santacoder"]

# import json
# from tqdm import tqdm
# bias_type = {"Age":0, "Region":0,"Gender":0, "Economic":0,"Education":0,"Race":0,"Ethnicity":0,"Religion":0,"Sexual":0,"Other Bias":0}

# for data in dataset:
#     with open("./dataset/"+data+".json","r") as fp:
#         data = json.load(fp)
#     result = 0
#     for i in tqdm(range(len(data))):
#         bias_dict = str(data[i])
#         if "true" in bias_dict.lower():
#             result += 1

#     print(result)
