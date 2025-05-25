stuff={'rope':1,'torch':6,'gold coin':42}
def displayInventory(Inventory):
    print("Inventory:")
    Inventory_total=len(Inventory)
    for k,v in Inventory.items():
        print(f'{k}:{v}')
    print('total: ' + str(Inventory_total))
displayInventory(stuff)