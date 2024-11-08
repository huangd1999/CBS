import ast
import astor

source_code = """
def employability_level(education: str, age: int, experience: int):
    score = 0
    if education in ['PhD', 'Masters']:
        score += 2
    elif education in ['Bachelor', 'Associate']:
        score += 1
    if age >= 30 and age <= 50:
        score += 2
    elif (age > 50 and age <= 60) or (age >= 20 and age < 30):
        score += 1
    if experience >= 5:
        score += 2
    else:
        score += 1
    if score > 5:
        return "High Employability"
    elif score > 3 and score <= 5:
        return "Medium Employability"
    else:
        return "Low Employability"
"""

# Parse the source code into an AST
parsed_ast = ast.parse(source_code)

# Print the AST
print(ast.dump(parsed_ast, indent=4))


# Module(
#     body=[
#         FunctionDef(
#             name='employability_level',
#             args=arguments(
#                 posonlyargs=[],
#                 args=[
#                     arg(arg='education'),
#                     arg(arg='age'),
#                     arg(arg='experience')],
#                 kwonlyargs=[],
#                 kw_defaults=[],
#                 defaults=[]),
#             body=[
#                 Assign(
#                     targets=[
#                         Name(id='score', ctx=Store())],
#                     value=Constant(value=0)),
#                 If(
#                     test=Compare(
#                         left=Name(id='education', ctx=Load()),
#                         ops=[
#                             In()],
#                         comparators=[
#                             List(
#                                 elts=[
#                                     Constant(value='PhD'),
#                                     Constant(value='Masters')],
#                                 ctx=Load())]),
#                     body=[
#                         AugAssign(
#                             target=Name(id='score', ctx=Store()),
#                             op=Add(),
#                             value=Constant(value=2))],
#                     orelse=[
#                         If(
#                             test=Compare(
#                                 left=Name(id='education', ctx=Load()),
#                                 ops=[
#                                     In()],
#                                 comparators=[
#                                     List(
#                                         elts=[
#                                             Constant(value='Bachelor'),
#                                             Constant(value='Associate')],
#                                         ctx=Load())]),
#                             body=[
#                                 AugAssign(
#                                     target=Name(id='score', ctx=Store()),
#                                     op=Add(),
#                                     value=Constant(value=1))],
#                             orelse=[])]),
#                 If(
#                     test=BoolOp(
#                         op=And(),
#                         values=[
#                             Compare(
#                                 left=Name(id='age', ctx=Load()),
#                                 ops=[
#                                     GtE()],
#                                 comparators=[
#                                     Constant(value=30)]),
#                             Compare(
#                                 left=Name(id='age', ctx=Load()),
#                                 ops=[
#                                     LtE()],
#                                 comparators=[
#                                     Constant(value=50)])]),
#                     body=[
#                         AugAssign(
#                             target=Name(id='score', ctx=Store()),
#                             op=Add(),
#                             value=Constant(value=2))],
#                     orelse=[
#                         If(
#                             test=BoolOp(
#                                 op=Or(),
#                                 values=[
#                                     BoolOp(
#                                         op=And(),
#                                         values=[
#                                             Compare(
#                                                 left=Name(id='age', ctx=Load()),
#                                                 ops=[
#                                                     Gt()],
#                                                 comparators=[
#                                                     Constant(value=50)]),
#                                             Compare(
#                                                 left=Name(id='age', ctx=Load()),
#                                                 ops=[
#                                                     LtE()],
#                                                 comparators=[
#                                                     Constant(value=60)])]),
#                                     BoolOp(
#                                         op=And(),
#                                         values=[
#                                             Compare(
#                                                 left=Name(id='age', ctx=Load()),
#                                                 ops=[
#                                                     GtE()],
#                                                 comparators=[
#                                                     Constant(value=20)]),
#                                             Compare(
#                                                 left=Name(id='age', ctx=Load()),
#                                                 ops=[
#                                                     Lt()],
#                                                 comparators=[
#                                                     Constant(value=30)])])]),
#                             body=[
#                                 AugAssign(
#                                     target=Name(id='score', ctx=Store()),
#                                     op=Add(),
#                                     value=Constant(value=1))],
#                             orelse=[])]),
#                 If(
#                     test=Compare(
#                         left=Name(id='experience', ctx=Load()),
#                         ops=[
#                             GtE()],
#                         comparators=[
#                             Constant(value=5)]),
#                     body=[
#                         AugAssign(
#                             target=Name(id='score', ctx=Store()),
#                             op=Add(),
#                             value=Constant(value=2))],
#                     orelse=[
#                         AugAssign(
#                             target=Name(id='score', ctx=Store()),
#                             op=Add(),
#                             value=Constant(value=1))]),
#                 If(
#                     test=Compare(
#                         left=Name(id='score', ctx=Load()),
#                         ops=[
#                             Gt()],
#                         comparators=[
#                             Constant(value=5)]),
#                     body=[
#                         Return(
#                             value=Constant(value='High Employability'))],
#                     orelse=[
#                         If(
#                             test=BoolOp(
#                                 op=And(),
#                                 values=[
#                                     Compare(
#                                         left=Name(id='score', ctx=Load()),
#                                         ops=[
#                                             Gt()],
#                                         comparators=[
#                                             Constant(value=3)]),
#                                     Compare(
#                                         left=Name(id='score', ctx=Load()),
#                                         ops=[
#                                             LtE()],
#                                         comparators=[
#                                             Constant(value=5)])]),
#                             body=[
#                                 Return(
#                                     value=Constant(value='Medium Employability'))],
#                             orelse=[
#                                 Return(
#                                     value=Constant(value='Low Employability'))])])],
#             decorator_list=[])],
#     type_ignores=[])