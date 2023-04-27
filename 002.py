# TASK
# There is an array of objects that have "id" and "parent" fields through which they can be linked into a tree and some arbitrary fields.

# You need to write a class that takes an array of these objects in the constructor and implements 4 methods:
# - getAll() Should return the original array of elements.
# - getItem(id) Takes the "id" of the element and returns the element object itself;
# - getChildren(id) Takes the "id" of an element and returns an array of elements that are children of the element whose "id"
# is given in the argument. If the element has no children, then an empty array should be returned;
# - getAllParents(id) Takes the "id" of an element and returns an array of a chain of parent elements,
# starting from the element itself whose "id" was passed in the argument, up to the root element,
# i.e. should get the path of the element to the top of the tree through the chain of parents to the root of the tree.
# The order of the elements matters!

# Requirements: maximum performance, therefore, the minimum number of array traversals during operations.


# Initial data:
class Store:

    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

s_list= Store.items



# Solution:
class TreeFunc:
    def func(self):
        List_first = []
        List_second = [{},{}]
        k = 1
        
        for i in s_list:
            exp_id = {'id': 0}
            exp_pa = {'parent': 0}
        
            if exp_id.keys() == self.keys() and self.items() <= i.items(): 
                List_first.append(i)
                
            elif exp_pa.keys() == self.keys() and self.items() <= i.items(): 
                List_first.append(i)

            elif list(self.values())[0] > list(i.values())[0] and list((List_second[k]).values())[-2:] != list(i.values())[-2:]:
                List_second.append(i)
                k += 1
                
        return List_first, List_second

    
    def getAll():
        print(s_list)
    
    def getItem(self):
        temp = {"id": self}
        result = TreeFunc.func(temp)
        print(str(result[0])[1:-1])

    def getChildren(self):
        temp = {"parent": self}
        result = TreeFunc.func(temp)
        print(result[0])

    def getAllParents(self):
        temp = {"id": self}
        result = TreeFunc.func(temp)
        print(list(reversed(result[1][2:])))

        
if __name__ == "__main__":
    TreeFunc.getAll()
    TreeFunc.getItem(7)
    TreeFunc.getChildren(4)
    TreeFunc.getChildren(5)
    TreeFunc.getAllParents(7)
    
