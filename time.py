
def show_menu():
    print('1- Sum times')
    print('2- Submission time')
    print('3- Convert seconds to time') 
    print('4- Convert time to seconds')
    print('5- Exit')

def get_input():
    time_1 = input('Please enter first time (hh:mm:ss): ')
    time_1 = time_1.split(':')
    first_time = {'h' : int(time_1[0]), 'm' : int(time_1[1]), 's' : int(time_1[2])}
    
    time_2 = input('Please enter second time (hh:mm:ss): ')
    time_2 = time_2.split(':')
    second_time = {'h' : int(time_2[0]), 'm' : int(time_2[1]), 's' : int(time_2[2])}

    return first_time , second_time

def SUM(time1,time2):
    result = {}
    result['h'] = time1['h'] + time2['h']
    result['m'] = time1['m'] + time2['m']
    result['s'] = time1['s'] + time2['s']

    if result['s'] >=60 :
        result['m'] += (result['s'] // 60)
        result['s'] = result['s'] % 60
        
    if result['m'] >=60 :
        result['h'] += (result['m'] // 60)
        result['m'] = result['m'] % 60
        
    return result

def Submission(time1,time2):
    result = {}
    result['h'] = time1['h'] - time2['h']
    result['m'] = time1['m'] - time2['m']
    result['s'] = time1['s'] - time2['s']

    if result['s'] < 0:
        
        result['m'] -= 1
        result['s'] += 60
    
    if result['m'] < 0:
        
        result['h'] -= 1
        result['m'] += 60

    if result['h'] < 0:
        return 'Eroor'

    else:
        return result    

def convert_seconds_to_hours(a):
    result = {'h': 0, 'm': 0, 's': 0}
    while True:
        if a >= 3600:
            a -= 3600
            result['h'] = result['h']+1
        elif a >= 60:
            a -= 60
            result['m'] = result['m']+1
        else:
            result['s'] = a
            break
    print(result)



def convert_time_to_seconds():

    time = input('Pleas  Enter  Time (hh:mm:ss): ')
    time = time.split(':')
    my_time = {'h' : int(time[0]), 'm' : int(time[1]), 's' : int(time[2])}
    seconds = 0
    seconds += my_time['s']
    seconds += (my_time['m'] * 60)
    seconds += (my_time['h'] * 3600)

    return seconds

def show(time):
    print(f"{time['h']}:{time['m']}:{time['s']}")



while True:
    show_menu()
    choice = int(input('Please choose an option: '))

    if choice == 1:
        time1 , time2 = get_input()
        show(SUM(time1,time2))
    
    elif choice == 2:
        time1 , time2 = get_input()
        try:
            show(Submission(time1,time2))
        except:
            
            Submission(time1,time2)

    elif choice == 3:
        s1 = int(input('enter seconds :'))
        show(convert_seconds_to_hours(s1))

    elif choice == 4:
        print(convert_time_to_seconds())

    elif choice == 5:
        break  

