dataset = ["codegen-2B-mono","codegen2-1B","gpt-3.5-turbo","gpt-neo-1.3B","incoder-1B","llama-bias-800cases-5trials","codet5p-770m-py","santacoder"]

import json
from tqdm import tqdm
bias_type = {"Age":0, "Region":0,"Gender":0, "Economic":0,"Education":0,"Race":0,"Ethnicity":0,"Religion":0,"Sexual":0,"Other Bias":0}

for data in dataset:
    path = data
    with open("./dataset/"+data+".json","r") as fp:
        data = json.load(fp)
    result = []
    for i in tqdm(range(len(data))):
        temp = data[i]["bif"][0]
        result.append(temp)
    print(result)
    with open("./dataset/bif/"+path+".json","w") as fp:
        json.dump(result,fp,indent=4)