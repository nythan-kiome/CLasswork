from symtable import Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def deleteFromBeginning(self):
        if self.head is None:
            return "The Linked List is Empty"
        self.head = self.head.next


    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtTheBeginning("fox")
    llist.insertAtTheBeginning("brown")
    llist.insertAtTheBeginning("quick")
    llist.insertAtTheBeginning("The")
    llist.printLinkedList()






