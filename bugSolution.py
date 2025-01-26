def function(a, b):
    return str(a) + str(b)

result = function(5, '10')
print(result)

#Alternative solution using type checking
def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Error: Incompatible types"

result = function(5, 10) #This will work
print(result)
result = function(5, '10') #This will return an error message
print(result)