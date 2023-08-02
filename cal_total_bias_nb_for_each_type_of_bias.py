import json

bias = {"Age":[i for i in range(744)], "Region":[i for i in range(744)],"Gender":[i for i in range(744)], "Economic":[i for i in range(744)],"Education":[i for i in range(744)],"Race":[i for i in range(744)],"Ethnicity":[i for i in range(744)],"Religion":[i for i in range(744)],"Sexual":[i for i in range(744)],"OtherBias":[i for i in range(744)]}
dataset = ["codet5p-770m-py","codegen-2B-mono","codegen2-1B","llama-bias-800cases-5trials","gpt-neo-1.3B","santacoder","incoder-1B","gpt-3.5-turbo"]
for path in dataset:

    path = "./dataset/"+path+".json"
    with open(path,"r") as fp:
        data = json.load(fp)
    for i in range(len(data)):
        bias_dict = data[i]["bias"][0]
        bias_dict = str(bias_dict).lower().replace(" ","").replace("'","").replace("\"","")
        for key in bias.keys():
            # if key in bias_dict.keys() and bias_dict[key] == True and i in bias[key]:
            # print(str(bias_dict))
            # print(bias_dict)
            indicater = str(key).lower() + ":false"
            if indicater not in bias_dict and i in bias[key]:
                bias[key].remove(i)
for key in bias.keys():
    bias[key] = 744 - len(bias[key])
print(bias)
# print(bias)