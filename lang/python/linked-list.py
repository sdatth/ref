class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(None)

def add(new_data):
    temp = head
    while (temp.next):
        temp = temp.next
    new_node = Node(new_data)
    new_node.next = None
    temp.next = new_node

def traverse():
        temp = head.next
        while (temp):
            print (temp.data)
            temp = temp.next

def delete():
    temp = head
    while (temp.next):
        prev = temp
        temp = temp.next
    prev.next = None              

def reverse():
    prev = None
    current = head.next
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head.next = prev            


while True:
    print("\n--------------------------------------------")
    print("\n1-> Add new element")
    print("2-> Print the list")
    print("3-> Reverse") 
    print("4-> Delete")
    print("5-> Exit")
    
    x = int(input("Enter your choice: "))

    if x == 1:
        element = int(input("Enter your element: "))
        add(element)
        print("Successfully added your element:",element)

    elif x == 2:
        print("\nLinked list :")
        traverse()

    elif x == 3:
        reverse()
        print("Successfully reversed linked list")
        print("New linked list :")
        traverse()

    elif x == 4:
        delete()
        print("Successfully deleted the last element")

    elif x == 5:
        break    


print("exited!")

