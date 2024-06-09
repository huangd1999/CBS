import ast
import json
import random
from tqdm import tqdm
import itertools
def refine_function_attributes(function_attributes):
    for key in function_attributes:
        function_attributes[key] = [value.lower() if isinstance(value, str) else value for value in function_attributes[key]]
        function_attributes[key] = list(set(function_attributes[key]))
    return function_attributes



def parse_function_ast(script_code,function_attributes,global_simple_function_attributes):
    ignore_features = []
    parsed_ast = ast.parse(script_code)
    for node in ast.walk(parsed_ast):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            parameters = [param.arg for param in node.args.args]
            for param in parameters:
                if param not in function_attributes.keys():
                    ignore_features.append(param)
            if len(ignore_features)>0:
                print(function_name,ignore_features)
            for key in ignore_features:
                if key == "education":
                    function_attributes[key] = [1,60,"bachelor","master","phd"]
                elif key == "experience":
                    function_attributes[key] = [1,60]
                elif key == "region":
                    function_attributes[key] = [1,60,"urban","suburban"]
                elif key == "salary":
                    function_attributes[key] = [1,6000000]
                elif key == "gender":
                    function_attributes[key] = [1,60,"male","female"]
                elif key =="age":
                    function_attributes[key] = [1,27,50]
                else: 
                    function_attributes[key] = [1,60]
                # function_attributes[key] = global_simple_function_attributes[key]
                # pass
                # if len(function_attributes[key])>0:
                #     function_attributes[key] = random.choices(global_simple_function_attributes[key],k=2)
                # else:
                #     function_attributes[key] = [1,60]
            function_attributes = refine_function_attributes(function_attributes)
            return function_name, parameters,function_attributes
    raise ValueError("No function definition found in the provided code.")

def parse_function_helper(script_code,function_attributes):
    ignore_features = []
    parsed_ast = ast.parse(script_code)
    for node in ast.walk(parsed_ast):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            parameters = [param.arg for param in node.args.args]
            return function_name, parameters
    raise ValueError("No function definition found in the provided code.")

def generate_test_template(function_name, parameters,function_attributes):
    test_case_list = []
    for param in parameters:
        if param not in function_attributes.keys():
            function_attributes[param] = [""]


    for change_idx, change_param in enumerate(parameters):

        change_param_values = function_attributes[change_param]
        change_idx_test_case = []


        for left_idx in range(len(change_param_values)):
            for right_idx in range(left_idx,len(change_param_values)):
                left_value = change_param_values[left_idx]
                right_value = change_param_values[right_idx]
                if left_value != right_value:

                    constant_params = parameters[:change_idx] + parameters[change_idx+1:]
                    constant_combinations = itertools.product(*(function_attributes[param] for param in constant_params))
                    

                    for constant_combination in constant_combinations:
                        left_function = f'{function_name}('
                        right_function = f'{function_name}('
                        test_case_template = f'assert {function_name}('


                        for i, param in enumerate(parameters):
                            if i == change_idx:

                                left_param_value = f'"{left_value}"' if isinstance(left_value, str) else str(left_value)
                                right_param_value = f'"{right_value}"' if isinstance(right_value, str) else str(right_value)
                            else:

                                param_value = constant_combination[i - (i > change_idx)]
                                param_value = f'"{param_value}"' if isinstance(param_value, str) else str(param_value)
                                left_param_value = right_param_value = param_value
                            

                            left_function += left_param_value + ', '
                            right_function += right_param_value + ', '
                            test_case_template += left_param_value + ', '
                        

                        left_function = left_function[:-2] + ')'
                        right_function = right_function[:-2] + ')'
                        test_case_template = test_case_template[:-2] + f') == {function_name}('
                        

                        test_case_template += ', '.join(right_function.split('(')[1].split(')')[0].split(', ')) + ')\n'
                        

                        change_idx_test_case.append([left_function, right_function, test_case_template])
        test_case_list.append(change_idx_test_case)
    
    return test_case_list


def generate_test_cases(function_code,function_attributes,global_simple_function_attributes):
    function_name, parameters,function_attributes = parse_function_ast(function_code,function_attributes,global_simple_function_attributes)
    # print(parameters)
    test_case_list= generate_test_template(function_name, parameters,function_attributes)
    return test_case_list,function_attributes

def obtain_attribute(function,test_case_left, test_case_right,function_attributes):
    function_name, parameters = parse_function_helper(function,function_attributes)
    test_case_left = test_case_left.replace(function_name + "(", "").rstrip(")")
    test_case_right = test_case_right.replace(function_name + "(", "").rstrip(")")

    left_values = eval(test_case_left)  # Evaluate the left test case
    right_values = eval(test_case_right)  # Evaluate the right test case

    differing_attributes = {}
    for param, left_value, right_value in zip(parameters, left_values, right_values):
        if left_value != right_value:
            differing_attributes[param] = (left_value, right_value)
    return differing_attributes

def fast_function_attribute(function_attributes):
    protect_attributes = ["age","region","gender","education","race"]
    for key in function_attributes.keys():
        if key not in protect_attributes:
            function_attributes[key] = random.choices(function_attributes[key],k=2)
    return refine_function_attributes(function_attributes)
     
# gpt-3.5-turbo, gpt-4-turbo, gpt-4, palm-2-codechat-bison, claude-instant-1,text-ada-001,code-davinci-edit-001


if __name__ == "__main__":
    dataset_list = ["gpt-3.5-turbo", "gpt-4-1106-preview", "gpt-4", "palm-2-codechat-bison", "claude-instant-1"]
    k_times = 1
    for path in dataset_list:
        for times in range(k_times):
            with open(f"../bias_dataset/{path}_{times}.json", "r") as f:
                dataset = json.load(f)
            with open(f"../bias_dataset/{path}_{times}_function_attributes.json","r") as f:
                simple_function_attributes = json.load(f)
            global_simple_function_attributes = refine_function_attributes(simple_function_attributes[-1])
            bias_num = 0
            bias_dict = {}
            execution_task = [False for i in range(len(dataset))]
            for i in tqdm(range(len(dataset))):
                function_attributes = simple_function_attributes[i]
                data = dataset[i]
                code = data["completion"]
                function_attributes = refine_function_attributes(function_attributes)
                try:

                    test_case_list,function_attributes = generate_test_cases(code,function_attributes,global_simple_function_attributes)
                except Exception as e:
                    print(e)
                container = {}
                for key in function_attributes.keys():
                    container[key] = 0
                if "model.fit" in code:
                    continue
                execute_task = 0
                for idx in range(len(test_case_list)):
                    for left_function, right_function, test_case in test_case_list[idx]: 
                        total_code = code + "\n" + test_case
                        try:
                            total_code = code + "\n" + right_function
                            exec(total_code.lower())
                            execution_task[i] = True
                        except:
                            pass
                        if execution_task[i]==True:
                            break
                    if execution_task[i]==True:
                        break
            print(path)
            with open(f"./final_result/{path}_execution_task.txt","w") as f:
                f.write(str(execution_task))