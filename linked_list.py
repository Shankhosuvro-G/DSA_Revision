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
            print("Linked list is empty")
            return
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
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)  
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index < 0 or index >=self.length():
            raise Exception("Invaled Index")
        if index==0:
            self.head=self.head.next
            return
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
        itr.next=itr.next.next
    def insert_at(self,index,data):
        if index < 0 or index >=self.length():
            raise Exception("Invaled Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr=self.head
        for _ in range(index-1):
            itr=itr.next
        node=Node(data,itr.next)
        itr.next=node
    def insert_after_value(self,data_after,data_to_insert):
        if self.head.data is None:
            raise Exception("Linked list is empty")
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next
    def remove_by_value(self,data):
        if self.head.data is None:
            raise Exception("Linked list is empty")
        if self.head.data==data:
            self.head=self.head.next
        itr=self.head
        while itr:
            if itr.next.data==data:
                itr.next=itr.next.next    
                break
            itr=itr.next
    def reverse(self):
        list=[]
        itr=self.head
        while itr:
            list.append(itr.data)
            itr=itr.next
        list.reverse()
        for _ in list:
            print(_,"-->",end="")       
if __name__ =="__main__":

    ll=LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.remove_at(1)
    ll.insert_at(0,"figs")
    ll.insert_at(1,"jackfruit")
    ll.print()
    ll.reverse()
   
