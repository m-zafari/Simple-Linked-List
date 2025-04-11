# Mohammad Zafari
# mhdzafari80@gmail.com

class Node:
    
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Slinkedlist:
    
    def __init__(self):
        self.head=None

    def append(self, new_data): 
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node 

    def get_n_th(self,n):
        nextnode = self.head
        for i in range(n):
            nextnode = nextnode.next
        return nextnode

"""
list1 = Slinkedlist()
list1.append(1)
list1.append(10)
list1.append(30)
list1.append(14)

n=2
print(list1.get_n_th(n).data)
"""
    