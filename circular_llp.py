class Node:
    def __init__(self,data,next):
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
            print("The linked list is empty.")
        itr=self.head
        llstr=""
        while itr!=self.head:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
        node=Node(data,self.head)
        itr=self.head
        while itr.next!=self.head:
            itr=itr.next
        itr.next=node
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def length(self):
        if self.head is None:
            print("The linked list is empty")
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(f"The length of the Linked List is {count}.")
    def remove_at(self,index):
        if index<0 and index>self.length():
            raise Exception("Invalid Index")
        if index==self.length-1:
            itr=self.head
            while itr.next!=self.head:
                itr=itr.next
            itr.next=self.head    

        if index==0:
            self.head=self.head.next
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
        itr.next=itr.next.next
                        

                    