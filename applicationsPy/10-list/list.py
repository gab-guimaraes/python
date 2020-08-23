

text = 'value'
myList = [1, 2, 3, 4, 'Text']
movies = ['fast and furious', 'halloween', 'john wick']
songs = ['always', 'not now']
print(myList[2])
print('movies 1', movies)
movies[2] = 'harry potter'
print('movies 2', movies)
print(movies[0:2])
print('\n\n\n\n')
print(movies + songs)
movies.insert(0, 'purge')
print('insert', movies)
movies.pop()
print(movies)
del(movies[0])
print(movies)
print('\n\n\n\n\n\n')
numbers = [1023, 1234, 356, 2]
print(max(numbers))
print(min(numbers))


for value in numbers:
    print(value)
    continue


