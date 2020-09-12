

#3.1

def right_justify(str):
    s = len(str)
    #return s
    print(" "*70, str)
 

#right_justify('monty')

#3.2

def do2(f, arg):
    f(arg)
    f(arg)


def print_spam():
    print('spam')



def do4(f, arg):
    do2(f, arg)
    do2(f, arg)


#do4(print, "Hi Claire")

#for i in range(70):
    #do4(print, "Hello Claire Ann Hansen")

#3.3
    
print('+ - - - - + - - - - +')
do4(print,"|         |        |")
print('+ - - - - + - - - - +')
do4(print,"|         |        |")
print('+ - - - - + - - - - +')

print('+ - - - - + - - - - + - - - - + - - - - +')
do4(print,"|         |         |         |         |")
print('+ - - - - + - - - - + - - - - + - - - - +')
do4(print,"|         |         |         |         |")
print('+ - - - - + - - - - + - - - - + - - - - +')
do4(print,"|         |         |         |         |")
print('+ - - - - + - - - - + - - - - + - - - - +')
do4(print,"|         |         |         |         |")
print('+ - - - - + - - - - + - - - - + - - - - +')



