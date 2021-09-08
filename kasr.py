

a = {'s': 2, 'm': 3}
b = {'s': 5, 'm': 4}
print(a,b)


def sum(x,y):
    result = {}
    result ['s'] = x['s'] * y['m'] + x['m'] * y['s']
    result ['m'] = x['m'] * y['m']
    return result


def mul(x,y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
   
    return result

def sub(x,y):
    result = {}
    result ['s'] = x['s'] * y['m'] - x['m'] * y['s']
    result ['m'] = x['m'] * y['m']
    return result

def div(x,y):
    result = {}
    result['s'] = x ['s'] / y ['s']
    result['m'] = x ['m'] /y ['m'] 
    return result
def show(x,y):
    print(x['s'],'/',x['m'])
    print(y['s1'],'/',y['m1'])

def show(x):
    print(x['s'],'/',x['m'])
     


c = mul(a,b)
show(c)

d = sum(a,b)
show(d)

w = sub(a,b)
show(w)

q = div(a,b)
show(q)