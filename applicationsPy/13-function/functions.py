def myprint(oi):
    print('Hello World', oi)


def myprinttwo(msg='Ola'):
    print("hi ", msg)


def return_function(var):
    print('my value is ', var)
    return var


myprint('harry potter')
myprint('hermione')

myprinttwo()
myprinttwo('123')

return_function('oi')
