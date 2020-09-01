# usuario vai criar um login e senha
# menor que 18 não pode criar usuario
# se idade_int > 18
#

usauario = input("digite o seu usuario")
senha = input("digite sua senha")
email = input("digite seu email")
idade = input("digite a sua idade")

idade_int = int(idade)
print(usauario)
print(email)

if idade_int > 18:
    print("usuario criado")
else:
    print("usuario negado, você é menor de idade")
