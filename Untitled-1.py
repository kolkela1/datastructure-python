class stack :
    def __init__(self):
     self.l=[]
     self.le=0
     self.peak=None
    def is_empty(self):
        return self.le==0
    def push(self ,x):
        if self.is_empty():
            self.l=[0]
            self.l[0]=x
            self.peak=x
            self.le+=1
        else:
            self.l.append(x)
            self.peak=x
            self.le+=1
    def pop(self):
        if self.is_empty():
            print("sorry the stack is empty\n")
        else:
            self.l.remove(self.peak)
            self.le-=1
            m=self.peak
            if self.is_empty():
             self.peak=None
            else:
              self.peak=self.l[-1]
            return m
    def printall(self):
        print(f"the stack is {self.l} and the len is {self.le} and peak is {self.peak}")
    def clear(self):
        for i in range(self.le):
            self.pop()
        self.le=0
    def transfer(self,s,t):
        while s.le!=0:
            t.push(s.pop())
            

        
  
class queue :
    def __init__(self):
        self.l=[]
        self.head=None
        self.tail=None
        self.le=0
    def is_empty(self):
        return self.le==0
    def enqueue(self,x):
        if self.is_empty():
             self.head=x
             self.tail=x
             self.le+=1
             self.l.append(x)
        else:
            self.tail=x
            self.l.append(x)
            self.le+=1
    def dequeue(self):
        if self.is_empty():
            print("we have empty queue")
        else:
            self.l.remove(self.head)
            m=self.head
            self.le-=1
            if self.is_empty():
                self.head=None
                self.tail=None
            else:
              self.head=self.l[0]
            return m
    def printall(self):
        print(f"the queue is {self.l} and the len is {self.le} and head is {self.head} and tail {self.tail}")
class node:
    def __init__(self):
        self.value=None
        self.next=None
class linked_list:
     def __init__(self):
        self.head=None
     def is_empty(self):
         return self.head==None
     def insert_first(self,x):
         if self.is_empty():
             new_node=node()
             new_node.value=x
             new_node.next=None
             self.head=new_node
         else:
             new_node=node()
             new_node.value=x
             new_node.next=self.head
             self.head=new_node
     def display(self):
         if self.is_empty():
             print("the linked list is empty\n")
         else:
           temp=self.head
           while(temp!=None):
               print(temp.value)
               temp=temp.next

     def append(self,x):
         if self.is_empty():
             new_node=node()
             new_node.value=x
             self.head=new_node
             new_node.next=None
         else:
             new_node=node()
             new_node.value=x
             new_node.next=None 
             temp=self.head
             while(temp.next!=None):
                 temp=temp.next
             temp.next=new_node
     def insert(self ,i,x):
         if i==1:
             self.insert_first(x)
         else:
          c=1
          temp=self.head
          i-=1
          while(c<i):
             c+=1
             temp=temp.next
          new_node=node()
          new_node.value=x
          new_node.next=temp.next
          temp.next=new_node
     def remove(self,x):
         t1=self.head
         if t1.value==x:
             self.head=t1.next
             t1.next=None
             del t1
         else:    
          t2=self.head
          while(t2.value!=x):
             t2=t2.next
             if t2.value==x:
                 break
             else:
                 t1=t1.next
          t1.next=t2.next
          t2.next=None
          del t2
    
     def concat(self,l,m):
         if l.is_empty():
             l.head=m.head
         elif m.is_empty():
             m.head=l.head
         elif m.is_empty() and m.is_empty():
             return None
         else:
          temp=l.head
          while temp.next!=None:
             temp=temp.next
          temp.next=m.head
         
         return l

class curcile_linked_list:
    def __init__(self):
     self.head=None
    def is_empty(self):
        return self.head==None
    def append(self,x):
        if self.is_empty():
            new_node=node()
            new_node.value=x
            self.head=new_node
            new_node.next=self.head
        else:
            new_node=node()
            new_node.value=x
            temp=self.head
            while(temp.next!=self.head):
                  temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def desplay(self):
            if self.is_empty():
                return None
            else:
                temp=self.head
                while temp.next!=self.head:
                    print(temp.value)
                    temp=temp.next
                print(temp.value)
class node_tree:
    def __init__(self):
        self.value=None
        self.right=None
        self.left=None
class tree :
    def __init__(self):
        self.root=None
    def is_empty(self):
        return self.root==None

l1=linked_list()
l1.append(10)
l1.insert_first(70)
l1.append(20)
l1.insert_first(80)
l1.append(30)
l1.append(40)
l1.insert(3,60)
print("the l1")
l1.display()
l2=linked_list()

print("the l2")
l2.display()
l2.concat(l2,l1)
print("l2 when concat")
l2.display()
class Arr:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.kol = [None] * size

    def fill(self):
        n = int(input("How many elements do you want in the array?\n"))
        while n > self.size:
            print("Enter a number smaller than or equal to the size.")
            n = int(input())
        
        for i in range(n):
            self.kol[i] = int(input(f"Input item {i}: "))
            self.length += 1

    def display(self):
        print("Array elements:")
        for i in range(self.length):
            print(f"Item {i}: {self.kol[i]}")

    def append(self, m):
        if self.length < self.size:
            self.kol[self.length] = m
            self.length += 1
        else:
            print("Array is full. Cannot append.")

    def insert(self, index, value):
        if index < 0 or index > self.length or self.length == self.size:
            print("Invalid index or array is full.")
            return
        
        for i in range(self.length, index, -1):
            self.kol[i] = self.kol[i - 1]
        
        self.kol[index] = value
        self.length += 1

    def sort(self):
        self.kol[:self.length] = sorted(self.kol[:self.length])

    def merge(self, a1, a2):
        new_size = a1.length + a2.length
        if new_size > self.size:
            print("Not enough space to merge.")
            return
        
        self.kol[:a1.length] = a1.kol[:a1.length]
        self.kol[a1.length:new_size] = a2.kol[:a2.length]
        self.length = new_size

    def search(self, value):
        for i in range(self.length):
            if self.kol[i] == value:
                print(f"Element {value} found at index {i}")
                return
        print("Element not found in the array.")

    def delete(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index.")
            return
        
        for i in range(index, self.length - 1):
            self.kol[i] = self.kol[i + 1]
        
        self.kol[self.length - 1] = None
        self.length -= 1

    def enlarge(self, new_size):
        if new_size <= self.size:
            print("New size must be larger than the current size.")
            return
        
        new_kol = [None] * new_size
        for i in range(self.length):
            new_kol[i] = self.kol[i]
        
        self.kol = new_kol
        self.size = new_size

    def get_length(self):
        return self.length

    def get_size(self):
        return self.size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self):
        data = int(input("Enter the data for the first node: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def count(self):
        temp = self.head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        return c

    def search(self):
        d = int(input("Enter the number you want to search: "))
        temp = self.head
        count = 1
        while temp:
            if temp.data == d:
                print(f"We found the number at position: {count}")
                return
            count += 1
            temp = temp.next
        print("Number not found.")

    def append(self):
        data = int(input("Enter the data for the new node: "))
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self):
        index = int(input("Enter index to insert at: "))
        if index > self.count():
            print("Index out of range!")
            return
        data = int(input("Enter data: "))
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def delete(self):
        if self.is_empty():
            print("Cannot delete, the list is empty.")
            return
        index = int(input("Enter index to delete: "))
        if index > self.count():
            print("Index out of range!")
            return
        if index == 1:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 2):
                temp = temp.next
            to_delete = temp.next
            temp.next = to_delete.next
            del to_delete

def main():
    s = int(input("Enter size of array: "))
    a1 = Arr(s)
    a1.fill()
    
    m = int(input("Enter the new size: "))
    a1.enlarge(m)
    
    m = int(input("Enter number to search: "))
    a1.search(m)
    
    o = int(input("Enter size of second array: "))
    a2 = Arr(o)
    a2.fill()
    
    a3 = Arr(o + s)
    a3.merge(a1, a2)
    
    v = int(input("Enter a number to append: "))
    a1.append(v)
    
    # Insert and sort (if needed)
    # n, m = map(int, input("Enter index and number to insert: ").split())
    # a1.insert(n, m)
    # a1.sort()
    
    # Deletion
    m = int(input("Enter the index to delete: "))
    a1.delete(m)
    a1.display()
    
    # Uncomment when LinkedList is implemented
    # l1 = LinkedList()
    # if l1.is_empty():
    #     print("It's empty")
    # else:
    #     print("It's not empty")
    # l1.insert_first()
    # l1.insert_first()
    # l1.append()
    # l1.insert()
    # l1.search()
    # l1.count()
    # l1.delete()
    # l1.display()

if __name__ == "__main__":
    main()
class node:
    def __init__(self):
        self.value=0
        self.next=None
class circle_linked_list:
    def __init__(self):
      self.head=None
    def is_empty(self):
        return self.head==None
    def append(self,d):
        if self.is_empty():
            n=node()
            n.value=d
            self.head=n
            n.next= self.head
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            n=node()
            n.value=d
            temp.next=n
            n.next=self.head
    def display(self):
        if self.is_empty():
            print("the circle linked list is empty")
        else:
            temp=self.head
            while(temp.next!=self.head):
                print(temp.value)
                temp=temp.next
            print(temp.value)
c=circle_linked_list()
c.display()

c.append(3)
c.display()
