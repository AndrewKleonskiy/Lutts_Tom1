D = {'spam':2,'ham':1,'eggs':3}
print(list(D.items()))
print(list(D.values()))
print(D.get('spams',22))


table = {'1975':'Holy Grail',
         '1979':'Life of Brian',
         '1983':'The Meaning of Life'}
year = '1983'
movie = table[year]
print(movie)
for year in table:
    print(year + '\t' + table[year])


table = {
    'Holy Grail':'1975',
    'Life of Brian':'1979',
    'The Meaning of Life': '1983'
}
print('\n' + table['Holy Grail'])

print(list(table.items()))

print([title for (title,year) in table.items() if year == '1975'])


D = dict( a = 1, b = 2, c = 3)
K = D.keys()
print(list(K))
V = D.values()
print(list(V))
print(D.items())


for k in D.keys(): print(k)
