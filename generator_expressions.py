# pycharm


#genexps
symbols = '$^£$£$'
print(tuple(ord(symbol) for symbol in symbols))

import array

print(array.array('I', (ord(x) for x in symbols)))


#Tuples used as records
lax_coordinates = (33.9423,-118.4084343)
city, year, pop, chg, area = ('BANGKOK', 2017, 323132,0.132, 8924)
travel_id = [('GB','1231454'), ('ESP', '23423432'), ('USA','34242456')]

for passport in sorted(travel_id):
    print('%s/%s' % passport)


for country, _ in travel_id:
    print(country)

    