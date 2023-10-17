
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x / y
    


def modulo(x, y):
    if y <= 0:
        raise ValueError('This operation is not supported for given input parameters') 
    if x < y:
        raise ValueError('This operation is not supported for given input parameters')  
    return x % y

def secondPower(x):
    return x ** 2


def power(x, y):
    if x == 0 and y < 0:
        raise ValueError('This operation is not supported for given input parameters')
    if y == -1:
        raise ValueError('This operation is not supported for given input parameters')
    _sum = pow(x, y)
    return float(_sum)


def secondRadix(x):
    if x <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x ** 0.5



def magic(x, y, z, k):
    if z+y == 0:
        raise ValueError('This operation is not supported for given input parameters')
    l = x + k
    m = z + y
    n = (l/m) + 1 
    return n


def control(a, x, y, z, k):
    
    if a.upper() == 'ADDITION':
        return addition(x, y)
    
    elif a.upper() == 'SUBTRACTION':
        return subtraction(x, y)
    
    elif a.upper() == 'MULTIPLICATION':
        return multiplication(x, y)
    
    elif a.upper() == 'DIVISION':
        return division(x, y)
    
    elif a.upper() == 'MOD':
        return modulo(x, y)
    
    elif a.upper() == 'POWER':
        return power(x, y)
    
    elif a.upper() == 'SECONDRADIX':
        return secondRadix(x)
    
    elif a.upper() == 'MAGIC':
        return magic(x, y, z, k)
    
    else: 
        raise ValueError('This operation is not supported for given input parameters')


print(control('mod', 213, 7, 6, 1))

print(float(pow(-1, -1)))