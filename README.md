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
TBD --model_name --execution_times
```
where you can set different close-sourced models~(Here we utilize aiohub since it can adapt different LLMs).

## AST Extraction

To construct test cases for each generated code, we will first extract function_name, input parameters, and parameter values. We provide the script:
```
TBD
```
where you specify the json file which will used for AST extraction.

## Test Case Construction and Automated Evaluation

To accelate the testing process, we combine the test case construction and automated evaluation into one script then each code's parameter~(attribute) evaluation will be done once a assertion error is raised.
```
TBD
```
