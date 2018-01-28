inventory = {
    'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12
}

drgonLoot = [
    'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'
]


def displayInventory(stuff):
    print('Inventory:')
    total = 0
    for key, value in stuff.items():
        print(str(value) + ' ' + key)
        total += value
    print('Totol count of items: ' + str(total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory.setdefault(item, 1)


print('Befor I kill the drgon=========================>')
displayInventory(inventory)
addToInventory(inventory, drgonLoot)
print('After I kill the drgon=========================>')
displayInventory(inventory)
