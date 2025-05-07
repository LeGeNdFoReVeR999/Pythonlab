allguests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}

def t(allguests,items):
    value=0
    for k,v in allguests.items():
        value=v.get(items,0)+value
    return value

print("Number of items being brought:")
items=['apples','cups','cakes','ham sandwiches','apple pies']

for k in items:
    print("-",k,t(allguests,k))