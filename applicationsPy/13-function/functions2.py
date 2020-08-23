def func(brand, model, hp, country='none'):
    print(brand, model, hp, country)


def func_args(*args, **kwargs):
    args = list(args)
    print(args[0])
    print(args)
    print('kwargs ', kwargs)


func('Mitsubishi', 'Lancer Evo', '340', 'Japan')

func_args(1, 2, 43, 56, 6, name="mitsubishi")
