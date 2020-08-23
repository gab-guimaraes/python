var = 'ferrari'

def func():
    print(var)


def func2():
    global var
    var = 'outro valor'
    print(var)


func()
func2()
print(var)