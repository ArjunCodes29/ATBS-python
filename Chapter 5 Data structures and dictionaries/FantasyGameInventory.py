inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print( 'Inventory: ')
    totalInventory = 0
    for key in inventory.keys():
        print(key + ' ' + str(inventory[key]))
        totalInventory += inventory[key]
    print('Total items: ' + str(totalInventory))


def addToInventory(inventory, addedItems):
    for i,item in enumerate(addedItems):
        newItem = True
        for items in inventory:
            if(item== items):
                inventory[items] += 1
                del(i)
                newItem = False
        if newItem:
            inventory[item] = 1

    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)