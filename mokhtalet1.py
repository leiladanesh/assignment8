def show_menu():
    print('1- multiplication' ) 
    print('2- addition ' )
    print('3- subtraction')

def multiplication(x,y):
    result = {}
    result_i = {}
    result=(x['a']*y['c'])-(x['bi']*y['di'])
    result_i=(x['bi']*y['c'])+(x['a']*y['di'])
    print(result,'+',result_i,'i') 
    return result , result_i
    

def addition(x,y):
    result = {}
    result_i = {}
    result=(x['a']+y['c'])
    result_i=(x['bi']+y['di'])
    print(result,'+',result_i,'i') 
    return result,result_i 
  

def subtraction(x,y):
    result = {}
    result_i = {}
    result=(x['a']-y['c'])
    result_i=(x['bi']-y['di'])
    print(result,'+',result_i,'i') 
    return result,result_i


while True:

    a = int(input('enter first real number:'))
    bi = int(input('enter mohumi:'))
    c = int(input('enter second real number:'))
    di = int(input('enter mohumi:'))

    complex_1 = {'a':a , 'bi':bi}
    complex_2 = {'c':c , 'di':di}

    show_menu()

    choice = int(input('choose one of the options:'))

    if choice==1:
        multiplication(complex_1, complex_2)
    if choice==2:
        addition(complex_1, complex_2)
    if choice==3:
        subtraction(complex_1,complex_2)