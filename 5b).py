inv={ 'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
def displayinventory(inv):
    tott=0
    for k,v in inv.items():
        print(f"{v}{k}")
        tott +=v
    print("Total no of items are",tott)
displayinventory(inv)
inv1={'rope':1,'gold coin':42}  
additems=['gold coin','dagger','gold coin','gold coin','ruby']
def addtoinv(inv1,additems):
    for k in additems:
        inv1[k]=inv1.get(k,0)+1
addtoinv(inv1,additems)
displayinventory(inv1)

