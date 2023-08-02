
total_bias_number = {'Age': 228, 'Region': 118, 'Gender': 219, 'Economic': 142, 'Education': 96, 'Race': 148, 'Ethnicity': 129, 'Religion': 106, 'Sexual': 80, 'Other Bias': 44}



import json


model_list = ["modified-codet5p-770m-py","modified-codegen-2B-mono","modified-codegen2-1B","modified-llama-bias-800cases-5trials","modified-gpt-neo-1.3B","modified-santacoder","modified-incoder-1B","modified-gpt-3.5-turbo","modified-gpt4"]

for i in range(len(model_list)):
    total_BI = 0
    total_BD = 0
    total_BE = 0
    path = "./dataset/biask/"+model_list[i]+".json"
    import json
    from tqdm import tqdm
    bias_type = {"Age":0, "Region":0,"Gender":0, "Economic":0,"Education":0,"Race":0,"Ethnicity":0,"Religion":0,"Sexual":0,"Other Bias":0}
    with open(path,"r") as fp:
        data = json.load(fp)
    total = 0
    for i in tqdm(range(len(data))):
        if i not in filter_data:
            bias_dict = data[i][0]
            if isinstance(bias_dict,dict):
                for key in bias_type.keys():
                    if key in bias_dict.keys() and bias_dict[key] == True:
                        bias_type[key] += 1

            total+=1
    total = total/(744)
    str1 = ""
    for key in bias_type.keys():
        str1 = str1 + "&" + str(round(bias_type[key]/total_bias_number[key]*100,2))
    print(str1)
    print("#####################")

