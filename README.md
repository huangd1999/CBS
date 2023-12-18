# Bias Testing and Mitigation in LLM-based Code Generation


## Dataset Construction
Our final dataset was illustrate in
```
dataset.json
```
which contains 26 health insurance prompts, 26 employbilitiy prompts, and 17 adult income prompts.

## Code Generation

To generate code snippets with code generation model, you can directly run the script:
```
python code_generation.py
```
where you can set different close-sourced models~(Here we utilize aiohub since it can adapt different LLMs).

Once the code_generation.py is executed, five model will be used to generate code snippets for each prompt with five times.

## AST Extraction

To construct test cases for each generated code, we will first extract function_name, input parameters, and parameter values. We provide the script:
```
python ast_aextraction.py
```
where you specify the json file which will used for AST extraction.
To ease of execution, we have already specify five model for AST extraction.

## Test Case Construction and Automated Evaluation

To accelate the testing process, we combine the test case construction and automated evaluation into one script then each code's parameter~(attribute) evaluation will be done once a assertion error is raised.
```
python fast_test_case_inference.py
```
Then all code will be execute with test cases.
The report will be save in:
```
with open(f'./json_save/{path}_{times}.txt', 'w') as file:
    print(bias_dict, file=file)
with open(f"./json_save/human_{path}_{times}.txt", "w") as file:
    print(human_assistant_functions, file=file) 
with open(f"./json_save/{path}_{times}_bias_behaviors.json","w") as f:
    json.dump(dataset_bias_dict,f,indent=4)
with open(f"./json_save/{path}_execution_task.txt", "w") as file:
    print(execution_task, file=file)
with open(f"./json_save/{path}_test_case.json", "w") as f:
    json.dump(dataset,f,indent=4)
```

## Paper RQ Discussion

To obtains RQ1.1, RQ1.2, RQ2.2's results, reviewers can run the command line:
```
python report_biask.py 
```

To obtains RQ2.1's results, we may need manual labeling the code bias behaviors for each task.

To obtains RQ3's results, we then require to re-run the code generation and add the bias mitigation prompts into the end of the current prompt.
```
python test_case_refine_code.py
```