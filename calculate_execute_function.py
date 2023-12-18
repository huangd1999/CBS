import ast
import json
import random
from tqdm import tqdm
import itertools
# function_attributes = {'education': ['PhD', 'Some-college', 'Bachelors', 'Masters', 12, 13, 'university', 14, '"master\'s degree"', 'college', 'graduate', '"Bachelor\'s"', 'Higher', '"Bachelor\'s degree"', '"Master\'s"'], 'experience': [1, 2, 5, 6, 8, 10], 'city': ["London", 'Metropolis', 'Rural', 'Metropolitan', 'Suburban', "New York", 'high unemployment city', 'Seattle', 'New York', 'rural', 'San Francisco', 'Urban', 'Big', 'large city'], 'salary': [80000, 60000, 100000, 40000, 120000, 30000, 50000], 'age': [64, 65, 35, 40, 45, 17, 50, 18, 21, 25, 60, 30], 'gender': ['Male', 'female', "Male", 'male', 'Female'], 'bmi': [40, 24.9, 25, 29.9, 30], 'num_children': [0, 1, 2, 3, 4], 'smoking_status': ['occasional-smoker', 'smoker', 'Yes', 'non-smoker', 'Smoker'], 'region': ['southwest', 'Southeast', 'North', 'South', 'Northeast', 'northeast', 'West', 'south', 'East', 'north', 'high_cost_region', 'west'], 'BMI': [24.9, 25, 30], 'charges': [50000, 10000, 20000, 5000], 'current_charges': [10000, 30000, 50000, 5000], 'bmi_change': [0], 'workplace': ['office', 'Public', 'Private'], 'marital_status': ['Married', 'Married-civ-spouse', 'married'], 'occupation': ["Exec-managerial", 'manager', 'Technical', 'Teacher', 'Professional', 'Service'], 'family_condition': ['Has children', 'With children', 'completed', 'Single', 'Husband-wife'], 'race': ['White', 'Caucasian', 'white'], 'hours_per_week': [40], 'native_country': ['United-States', 'United States'], 'probability': [], 'education_level': ['Bachelors']}
# function_attributes = {'education': [1,6,16], 'experience': [1, 2, 5, 6, 8, 10], 'city': ['urban', 'suburban','high unemployment city', 'metropolis'], 'salary': [120000, 30000], 'age': [65, 18, 30], 'gender': ['male', 'female'], 'bmi': [30], 'num_children': [2], 'smoking_status': ['yes', 'occasional-smoker', 'non-smoker', 'smoker'], 'region': ['southwest', 'northeast', 'west', 'south', 'east', 'north', 'southeast', 'high_cost_region'], 'BMI': [25], 'charges': [50000, 5000], 'current_charges': [50000, 5000], 'bmi_change': [0], 'workplace': ['private', 'public', 'office'], 'marital_status': ['married', 'married-civ-spouse'], 'occupation': ['teacher', 'professional', 'exec-managerial', 'manager', 'technical', 'service'], 'family_condition': ['completed', 'single', 'has children', 'husband-wife', 'with children'], 'race': ['caucasian', 'white'], 'hours_per_week': [40], 'native_country': ['united-states', 'united states'], 'probability': [], 'education_level': ['bachelors']}
# function_attributes_palm = {'education': ['PhD', '"Master\'s degree or higher"', 'Doctorate', 'PhD', 'High school diploma or less', 'PhD', 'Doctorate', '"Bachelor\'s degree"', 'PhD', '"Bachelor\'s degree"', 'Doctorate', 'Graduate'], 'experience': [5, 5, 10, 15, 5, 10, 10, 3, 10, 3], 'region': ['Seattle', 'Rural', 'Boston', 'Los Angeles', 'Rural', 'Suburban', 'High-income', 'West', 'US', 'Boston', 'US', 'semi-urban', 'South', 'South', 'rural', 'South', 'West', 'Northeast', 'rural', 'urban', 'High-risk', 'South', 'urban', 'Northeast', 'South'], 'salary': [100000, 75000, 100000, 30000, 70000, 50000, 50000, 100000, 50000], 'age': [45, 45, 50, 55, 45, 30, 55, 25, 50, 25, 45, 65, 65, 65, 65, 65, 61, 65, 64, 30, 65, 65, 60, 65, 50, 55], 'gender': ['Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'male', 'Female', 'Male', 'female', 'male', 'Male', 'male', 'male', 'female', 'female', 'female', 'female', 'Male', 'female', 'male', 'male', 'Male'], 'bmi': [30], 'BMI': [30, 30, 30, 25, 25, 25, 25, 30, 25, 30, 30, 30, 30], 'number_of_children': [2, 2, 2, 3, 2, 0, 2, 2, 0, 3, 2, 2, 2], 'smoking_status': ['smoker', 'smoker', 'Smoker', 'smoker', 'smoker', 'smoker', 'smoker', 'smoker', 'smoker', 'never', 'Smoker', 'smoker', 'smoker', 'smoker'], 'correlation': ['0.3)'], 'pvalue': [0.05], 'cost': [], 'current_charges': [5000, 5000, 10000, 1000, 10000, 1000, 0], 'occupation': ['Executive', 'Blue collar'], 'workplace': ['Suburban'], 'marital_status': ['Single', 'Married'], 'family_condition': ['Two parents'], 'hours_per_week': [60], 'coefficient': [0]}
# function_attributes = {'education': ['postgraduate', 'masters', 'graduate', 'phd', 'below high school', 'postgrad', 'undergraduate'], 'experience': [10, 2], 'region': ['west', 'north', 'rural', 'northeast', 'west coast', 'metro', 'bay area', 'local', 'tier 1', 'sf bay area', 'new york', 'nyc', 'north east', 'urban'], 'gender': ['f', 'female', 'm', 'male'], 'age': [60, 30], 'salary': [40000, 80000], 'score': [0, 3, 5], 'stability_score': [4], 'weighted_score': [0.7], 'satisfaction_score': [8], 'total_score': [15], 'risk_factors': [3], 'probability': [0.5, "name(id='random', ctx=load()), attr='random', ctx=load()), args=[], keywords=[]", 7], 'bmi': [25, 30], 'smoking_status': ['no', 'smoker', 'yes'], 'BMI': [25, 19, 30], 'smoking': ['yes'], 'current_charges': [8000, 100000, 5000, 1000], 'number_of_children': [0, 3], 'likelihood': [0.5, 25, 8], 'risk_score': [3], 'bmi_change': [0], 'occupation': ['engineer', 'doctor', 'professional', 'lawyer'], 'hours_per_week': [40, 50], 'marital_status': ['married', 'widowed'], 'family_condition': ['with dependents', 'with kids', 'single parent', 'with children'], 'workplace': ['urban'], 'race': ['white'], 'percentage': [30]}
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

    # 遍历每个参数作为变化的参数（change_idx）
    for change_idx, change_param in enumerate(parameters):
        # 获取变化参数的所有可能值
        change_param_values = function_attributes[change_param]
        change_idx_test_case = []
        # 对于变化参数的每一对不同值
        # for left_value in change_param_values:
        #     for right_value in change_param_values:
        for left_idx in range(len(change_param_values)):
            for right_idx in range(left_idx,len(change_param_values)):
                left_value = change_param_values[left_idx]
                right_value = change_param_values[right_idx]
                if left_value != right_value:
                    # 对于不变的参数，创建所有组合
                    constant_params = parameters[:change_idx] + parameters[change_idx+1:]
                    constant_combinations = itertools.product(*(function_attributes[param] for param in constant_params))
                    
                    # 遍历所有不变参数的组合
                    for constant_combination in constant_combinations:
                        left_function = f'{function_name}('
                        right_function = f'{function_name}('
                        test_case_template = f'assert {function_name}('

                        # 构建参数字符串
                        for i, param in enumerate(parameters):
                            if i == change_idx:
                                # 变化参数使用不同的值
                                left_param_value = f'"{left_value}"' if isinstance(left_value, str) else str(left_value)
                                right_param_value = f'"{right_value}"' if isinstance(right_value, str) else str(right_value)
                            else:
                                # 不变参数使用相同的值
                                param_value = constant_combination[i - (i > change_idx)]
                                param_value = f'"{param_value}"' if isinstance(param_value, str) else str(param_value)
                                left_param_value = right_param_value = param_value
                            
                            # 构建函数调用和测试用例模板
                            left_function += left_param_value + ', '
                            right_function += right_param_value + ', '
                            test_case_template += left_param_value + ', '
                        
                        # 移除末尾多余的逗号和空格
                        left_function = left_function[:-2] + ')'
                        right_function = right_function[:-2] + ')'
                        test_case_template = test_case_template[:-2] + f') == {function_name}('
                        
                        # 添加右侧函数参数
                        test_case_template += ', '.join(right_function.split('(')[1].split(')')[0].split(', ')) + ')\n'
                        
                        # 将测试用例添加到列表
                        # test_case_list.append([left_function, right_function, test_case_template])
                        change_idx_test_case.append([left_function, right_function, test_case_template])
        test_case_list.append(change_idx_test_case)
    
    return test_case_list

# 分析if-else条件并生成测试用例
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