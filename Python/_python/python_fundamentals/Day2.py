# //Write an algorithm that takes in a string and checks to make sure the parentheses are valid.
# //all '(' should have a matching ')'
# //parentheses should also be in the correct order(i.e. ')(' would not be valid)

# //example: ()           -> true
# //example: (([(8+13)])) -> true
# //example: (()))()      -> false
# //example: (            -> false

# function parensValid(input){
#     //return true or false
# }

def parensValid(input):
    if len(input) % 2 != 0:
        return False
    #filter
    while '[]' in input or '{}' in input or '()' in input:
        input = input.replace('[]','')
        input = input.replace('{}','')
        input = input.replace('()','')
    return input == ''
print(parensValid("(())))"))#odd amount-false
print(parensValid("[[[]]]"))#true
print(parensValid("(([()]))"))#true
print(parensValid("(()))()"))#false
print(parensValid("("))#false






def parensValid(input):
#     //return true or false
    if len(input) % 2 != 0:
        return False
    counter=0
    for i in range(0,len(input)):
        if input[i]=='(' or input[i] == '[' or input[i] == '{':
            counter+=1
        elif input[i]==')'or input[i] == ']' or input[i] == '}':
            counter-=1
    if counter==0:
        return True
    else:
        return False
print(parensValid("(())))"))
print(parensValid((([(8+13)]))))
print(parensValid("((())))"))
