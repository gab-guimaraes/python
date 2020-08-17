user = input("Create your user ")
password = input("Create your password")


qtd = len(user)

print(user, qtd)

if len(password) < 5:
    print("Short Password")
else:
    print("ok")
