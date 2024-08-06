class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("Linked List is empty.")
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)  
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def create_new_linked(self,data_list):
        itr=self.head
        while itr:
            prev=itr
            itr=itr.next
            del prev
        self.head=None
        self.insert_values(data_list)
    def length(self):
        count=0
        itr=self.head
        while itr is not None:
            count+=1
            itr=itr.next
        #print(f"The length of linked list is {count}")
        return count    
    def remove_at(self,index):
        if self.head is None:
            print("Nothing to remove") 
        if index  < 0 or index >= self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head=self.head.next
            return
        itr=self.head
        for _ in range (index-1):
            itr=itr.next
        itr.next=itr.next.next
    def remove_by_value(self,data):
        if self.head is None:
            print("Nothing to remove")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr:
            if itr.data==data:
                itr=itr.next
                return
    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise Exception()
        if index==0:
            self.insert_at_beginning(data)
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
            node=Node(data,itr.next)
        itr.next=node 
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
            itr=itr.next
    def multiply_by_2(self):
        itr=self.head
        while itr:
            itr.data=itr.data*2
            itr=itr.next
    def find_middle(self):
        i=0
        itr=self.head
        while i < self.length()//2:
            itr=itr.next
            i+=1
        print(itr.data)
    def delete_middle(self):
        length=self.length()//2
        itr=self.head
        for _ in range(length-1):
            itr=itr.next
        itr.next=itr.next.next
ll=LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(6)
ll.insert_at_beginning(7)
ll.insert_at_end(4)
ll.insert_values([3,2,1])
ll.length()
ll.print()
ll.remove_at(2)
ll.print()
ll.remove_by_value(7)
ll.print()
ll.remove_by_value(6)
ll.print()
ll.insert_at(2,5)
ll.print()
ll.insert_after_value(1,0)
ll.print()
ll.multiply_by_2()
ll.print()
ll.find_middle()
ll.delete_middle()
ll.print()
              
    
            

