symbols = '£$%^@$'
codes = []
for symb in symbols:
    codes.append(ord(symb))
print(codes)


# List Comprehensions
coding = [ord(x) for x in symbols]

print(coding)


#List Comprehensions
z = 'ABC'
dummy = [ord(z) for z in z]

print(dummy)


#Listcomp and a map/filter composition.
sample = '%^@£@!'

# List Comprehensions
lstcomp = [ord(p) for p in sample if ord(p) > 40]
print(lstcomp)


#Filter/Mapping
filtlst = list(filter(lambda c: c > 40, map(ord,sample)))
print(filtlst)


#Tshirt Color and Sizes List Comperehension vs normal for loop

colors = ['navy','black','white']
sizes = ' S M L'.split()

# lst Comp
tshirts = [(color, size) for color in colors
                            for size in sizes]
print(tshirts)


#normal loop
lst = list()
for col in colors:
    for s in sizes:
        lst.append(col)
        lst.append(s)
print(lst)


