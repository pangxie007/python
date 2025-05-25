stuff={'rope':1,'torch':6,'gold coin':42}
dragonLoot=['gold coin','rope','ruby','ruby']
def addtoInventory(Inventory,add):
    for k in add:
        if k in Inventory:
            Inventory[k]+=1
        elif k not in Inventory:
            Inventory[k]=1
    print('Inventory:')
    for k,v in Inventory.items():
        
        print(k,v)
    print(f'Inventory total:',end=' ')
    print(sum(Inventory.values()))
addtoInventory(stuff,dragonLoot)