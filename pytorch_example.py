import ast
import torch
import inspect

class PyTorchIfConditionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.conditions = []

    def visit_Compare(self, node):
        left_name = ast.dump(node.left)
        comparators = [ast.dump(comparator) for comparator in node.comparators]
        condition = {'left_name': left_name, 'comparators': comparators}
        self.conditions.append(condition)
        self.generic_visit(node)

def analyze_pytorch_module(module):
    # Get the source code of the module
    module_code = inspect.getsource(module)

    # Parse the AST of the module
    parsed_ast = ast.parse(module_code)

    # Create and apply the visitor
    visitor = PyTorchIfConditionVisitor()
    visitor.visit(parsed_ast)

    protect_attributes = ["age", "region","gender", "education", "race"]
    # Process the results as needed
    for condition in visitor.conditions:
        for key in protect_attributes:
            if key in condition['left_name']:
                print(f"Left Name: {condition['left_name']}")
                print(f"Comparators: {condition['comparators']}")

# Example usage:
analyze_pytorch_module(torch)
