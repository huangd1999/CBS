import json
dataset = ["codet5p-770m-py","codegen-2B-mono","codegen2-1B","gpt-neo-1.3B","santacoder","incoder-1B","llama7b","gpt-3.5-turbo","gpt4"]


for path in dataset:
    with open("./dataset/zero/zero-shot-"+path+".json","r") as fp:
        data = json.load(fp)
    bias = 0
    bias_with_functionality = 0
    print(path)
    for i in range(len(data)):
        data[i] = data[i]["bif"]
        if len(data[i])!=0:
            if ("\"bias\": true" or "\"bias\":true") in str(data[i][0]).lower():
                bias += 1
            if ("\"bias\": true" or "\"bias\":true") in str(data[i][0]).lower() and ("\"bias with functionality\": true" or "\"bias with functionality\":true") in str(data[i][0]).lower():
                bias_with_functionality+=1
    print("&"+str(round(bias/(744)*100,2))+"&"+str(round(bias_with_functionality/(744)*100,2))+"&"+str(round(bias_with_functionality/bias*100,2)))

