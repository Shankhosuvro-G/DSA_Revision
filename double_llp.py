class Node:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        node=Node(data,None,self.head)
        if self.head is not None:
            self.head.prev=node
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
        itr=self.head    
        while itr.next is not None:
            itr=itr.next
        itr.next=Node(data,itr.prev,None)        
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
        itr=self.head    
        llstr=""
        while itr:
            llstr+=str(itr.data)+"<--->"
            itr=itr.next
        print(llstr)
    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
        itr=self.head
        while itr.next is not None:
            itr = itr.next
        llstr=""
        while itr:
            llstr+=str(itr.data)+"<--->"
            itr=itr.prev
        print(llstr)
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def create_new_linkedlist(self,data_list):
        itr=self.head
        while itr is not None:
            prev=itr
            itr=itr.next
            del prev
        self.insert_values(data_list)    
        print("The linked list has been deleted")
    def length(self):
        itr=self.head
        count=0
        while itr is not None:
            count+=1
            itr=itr.next
        print(f"The length of the linked list is {count}")
        return count
    def remove_at(self,index):
        if self.head is None:
            raise Exception("Linked list is empty")
        if index < 0  or index > self.length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
        itr.next=itr.next.next
    def remove_by_value(self,data):
        if self.head is None:
            raise Exception("Linked list is empty")
        itr=self.head
        while itr:
            if itr.data==data:
                if itr.next is not None:
                    itr.next.prev=itr.prev
                if itr.prev is not None:   
                    itr.prev.next=itr.next
                if itr.next is None:
                    itr=itr.prev    
                return
            itr=itr.next
    def insert_at(self,data,index):
        if index < 0 or index > self.length():
            raise Exception()
        if index==0:
            self.insert_at_beginning(data)
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
        itr.next=Node(data,itr.prev,itr.next)
    def insert_after_value(self,data_after,data_to_insert):
        itr=self.head
        while itr is not None:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.prev,itr.next)
                return
            itr=itr.next
if __name__=="__main__":            
    ll=LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.print_forward() 
    ll.print_backward()
    ll.insert_at_end(4)
    ll.print_forward()  
    ll.insert_values([5,6,7])
    ll.print_forward()
    #ll.remove_at(2)
    #ll.print_forward()
    #ll.remove_by_value(7)
    #ll.print_forward()
    ll.insert_at(8,7)
    ll.print_forward()
    ll.insert_after_value(8,9)
    ll.print_forward()


