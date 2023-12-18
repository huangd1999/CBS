import ast
import json
import black
import os


feature_value_dict = []
# 遍历AST以查找if-else条件语句和它们的特征值
bias_type = ["age","region","gender","education","race"]
bias_type_dict = {"age":0,"region":0,"gender":0,"education":0,"race":0}
def find_if_else_features_and_values(node,i,j):
    global feature_value_dict,bias_type_dict,bias_type_dict
    if isinstance(node, ast.If):
        if isinstance(node.test, ast.Compare) and isinstance(node.test.left, ast.Name):
            feature_name = node.test.left.id
            feature_value = ast.dump(node.test.comparators[0])
            print(f"Feature: {feature_name}, Value: {feature_value}")
            if str(i)+"_"+str(j) not in feature_value_dict:
                # print(f"Feature: {feature_name}, Value: {feature_value}")
                feature_value_dict.append({str(i)+"_"+str(j):[{feature_name:feature_value}]})
                if feature_name.lower() in bias_type:
                    bias_type_dict[feature_name.lower()]+=1
            else:
                feature_value_dict.append({str(i)+"_"+str(j):[{feature_name:feature_value}]})
                if feature_name.lower() in bias_type:
                    bias_type_dict[feature_name.lower()]+=1
    for child in ast.iter_child_nodes(node):
        find_if_else_features_and_values(child,i,j)
features = {}
def find_all_if_features(node):
    if isinstance(node, ast.If):
        if isinstance(node.test, ast.Compare) and isinstance(node.test.left, ast.Name):
            feature_name = node.test.left.id
            feature_value = ast.dump(node.test.comparators[0])
            features[feature_name] = feature_value

    # 递归遍历子节点
    for child in ast.iter_child_nodes(node):
        find_all_if_features(child)

# dataset_list = ["codet5p-770m-py","gpt-neo-1.3B", "incoder-1B","codegen2-1B","CodeLlama-7b-Python-hf","starcoder"]
# dataset_list = ["codegen2-1B"] gpt-3.5-turbo, gpt-4-1106-preview, gpt-4, palm-2-codechat-bison, claude-instant-1,text-ada-001,code-davinci-edit-001
# dataset_list = ["gpt-3.5-turbo","gpt-4-turbo","gpt-4","palm-2-codechat-bison","claude-instant-1","text-ada-001","code-davinci-edit-001"]
dataset_list = ["gpt-4-1106-preview","gpt-4"]
for path in dataset_list:
    with open(f"../bias_dataset/{path}.json","r") as f:
        dataset = json.load(f)
    analyze = 0
    # os.mkdir(path)
    error_idx=0
    # for data in dataset:
    for i in range(len(dataset)):
        data = dataset[i]

        # for code in data["output"]:
        # for j in range(len(data["output"])):
        code = data["output"][0]
        j=0
        try:
            parsed_ast = ast.parse(code)
            find_if_else_features_and_values(parsed_ast,i,j)
            # find_all_if_features(parsed_ast)
            analyze += 1
        except Exception as e:
            # pass
            print(e)
            # with open(f"./{path}/error_{error_idx}.py","w") as f:
            #     f.write(code)
            # error_idx+=1
    print(analyze)
    # print(feature_value_dict)
    with open(f"./{path}_if_else_features.json","w") as f:
        json.dump(features,f,indent=4)
    print(bias_type_dict)
