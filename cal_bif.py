import json

dataset = ["codet5p-770m-py","codegen-2B-mono","codegen2-1B","gpt-neo-1.3B","santacoder","incoder-1B","gpt-3.5-turbo","gpt4"]


for path in dataset:
    with open("./dataset/zero-shot-bf/"+path+".json","r") as fp:
        data = json.load(fp)
    bias_with_functionality = 0
    bias = 0
    for i in range(len(data)):
        if isinstance(data[i],list):
            data[i] = data[i][0]
        # print(data[i])
        if i not in filter_data and "bias" in data[i].keys() and "bias with functionality" in data[i].keys() and data[i]["bias"] == True and data[i]["bias with functionality"] == True:
            bias_with_functionality += 1
        if i not in filter_data and "bias" in data[i].keys() and data[i]["bias"] == True:
            bias += 1
    print("&"+str(round(bias/(744)*100,2))+"&"+str(round(bias_with_functionality/(744)*100,2))+"&"+str(round(bias_with_functionality/bias*100,2)))
    
