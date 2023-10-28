#

def add_inventory(widget_name, quantity, dictionary):
    if widget_name not in dictionary:
        dictionary[widget_name] = quantity
    else:
        initialQuantity = dictionary[widget_name]
        dictionary[widget_name] = initialQuantity + quantity

def remove_inventory_widget(widget_name, dictionary):

    if widget_name in dictionary:
        del dictionary[widget_name]
        return "Record deleted"
    else:
        return "Item not found"