class Item:
    '''An item'''
    def __init__(self,price,item_number,description,catagory):
        self.price=price
        self.item_number=item_number
        self.description=description
        self.catagory=catagory


    def __str__(self):
        return "This item costs ${0}".format(self.price)

    
class Inventory_system:
    '''inventory system'''
    def __init__(self):
        self.items=[]

    def add(self,item):
        self.items.append(item)
        print("{0} is added".format(item.description))

    def find_item(self,item):
        for t in self.items:
            if(t.description==item):
                return t
            
        return None

    def compare(self,item1,item2):
        i1 = self.find_item(item1)
        i2 = self.find_item(item2)
        if(i1==None):
            print("Item1 not found")
        elif(i2==None):
            print("Item2 not found")
        else:
            if(i1.price<=i2.price):
                print("{0} is cheaper".format(i1.description))
            else:
                print("{0} is cheaper".format(i2.description))
        
    
#test
if __name__ == "__main__":
    inv = Inventory_system();
    apple=Item(1,1,"apple","food")

    inv.add(apple)

    inv.compare("apple","pen")

    pen=Item(0.5,2,"pen","tool")

    inv.add(pen)

    inv.compare("apple","pen")
