try:
    print(a)
except NameError as erro:
    print('Error :', erro)
except Exception as erro:
    print('Exception error :', erro)
finally:
    print('Finally')