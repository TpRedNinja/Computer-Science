# This program will create a basic linked list object

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"This node's value is {self.data} and points to {self.next}"

    def set_next(self,new_next):
        self.next = new_next

def add_node(HEAD,value):
    new_node = Node(value)
    # transverse though our list
    if HEAD == None:
        return new_node
    else:
        current = HEAD
        while current.next != None:
            current = current.next
        current.next = new_node
        return HEAD

def display(HEAD):
    current = HEAD
    while current.next != None:
        print(current.data)
        current = current.next

def search(HEAD,num_to_find):
    current = HEAD
    while current.next != None:
        if current.data == num_to_find:
            return True
        current = current.next
    return False
def delete_node(HEAD,num_to_remove):
    current = HEAD
    previous = None
    while current.next != None:
        if current.data == num_to_remove:
            if previous == None:
                return HEAD.next
            else:
                previous.set_next(current.next)
                
        previous = current
        current = current.next
    return HEAD
        
def main():
    HEAD = None

    for i in range(10,60,10):
        HEAD = add_node(HEAD,i)
    display(HEAD)
    print()
    HEAD = delete_node(HEAD,20)
    display(HEAD)


# call main
main()
