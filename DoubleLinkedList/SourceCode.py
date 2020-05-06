class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class DoubleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    #inserting element at the begginig of the list
    def insert_at_beg(self,data):
        newnode = Node(data)
        if self.start == None:
            self.start = newnode
            self.end = newnode
        else:
            newnode.right = self.start
            self.start.left = newnode
            self.start = newnode  
        self.count = self.count + 1
    
    #inserting element at the end of list
    def insert_at_end(self,data):
        newnode = Node(data)
        if self.start == None:
            self.start = newnode
            self.end = newnode
        else:
            self.end.right = newnode
            newnode.left = self.end
            self.end = newnode
        self.count = self.count + 1
    
    #inserting element at the required position
    def insert_at_pos(self,data,pos):
        newnode = Node(data)
        if(pos<1 or pos>self.count):
            print("print a valide position")
            print("note : node count starts from 1 and total element are {}".format(self.count))
        elif(pos ==1 ):
            print("Please choose \"Insert at biggining\"")
        else:
            temp = self.start
            while(pos > 2):
                temp = temp.right
                pos = pos -1
            newnode.right  = temp.right
            newnode.left = temp
            temp.right.left = newnode
            temp.right = newnode
            self.count += 1
                
    #deleting element at beggining
    def del_at_beg(self):
        if self.start == None:
            print("Cannot pop from empty list")
        elif self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.right
            self.start.left = None
            self.count = self.count -1
        
    # del element at the end
    def del_at_end(self):
        if self.start == None:
            print("Cannot pop from empty list")
        elif self.start == self.end:
            self.start = None
            self.end = None
            self.count -= 1
        else:
            temp = self.start
            while(temp.right != self.end):
                temp = temp.right
            temp.right = None
            self.end = temp
            self.count -=1
    
    #del element at required position
    def del_at_pos(self,pos):
        if(pos<1 or pos > self.count):
            print("Please enter a valid position ")
            print("The count of elements in the list are : {}".format(self.count))
        elif(pos==1):
            print("Please choose del from biggining operation")
        else:
            temp = self.start
            while(pos>2):
                temp = temp.right
                pos -=1
            temp.right = temp.right.right
            temp.right.left = temp
    
    def Traverse(self):
        if(self.start == None):
            print("List do not contain any elements")
        else:
            temp = self.start
            print("****************************** SUMMMARY *****************************")
            print("")
            print("Total Number of elements in list are : ",self.count)
            print("The elements are : ",end=" ")
            while(temp):
                print(temp.data,end="")
                temp = temp.right
                if(temp):
                    print(" -> ",end="")
            print("")

    def ReveredList(self):
        if(self.start == None):
            print("List is empty")
        elif(self.start == self.end):
            print(self.start.data)
        else:
            temp = self.end
            while(temp.left != self.start):
                print(temp.data,end="->")
                temp = temp.left
            temp = temp.left
            print(temp.data)

def Menu():
    print("")
    print("*******************SINGLE LINKED LIST *************************")
    print("0> Insert bulk elements")
    print("1> Insert at biggining")
    print("2> Insert at end")
    print("3> Insert at position")
    print("4> Delete at biggining")
    print("5> Delete at end")
    print("6> Delete at required position")
    print("7> Traverse the list")
    print("8> Reversed list")
    print("9> Quit")
    print("")
    while(True):
        choice = int(input("Enter your choice : "))
        if(choice>=0 and choice<=8):
            return choice
            
    
if __name__ =="__main__":
    dll = DoubleLinkedList()
    while(True):
        choice = Menu()
        if choice == 0:
            elements = list(map(int,input("enter List of elements :").split()))
            for ele in elements:
                dll.insert_at_end(ele)
        elif(choice == 1):
            ele = int(input("enter element : "))
            dll.insert_at_beg(ele)
        elif(choice == 2):
            ele = int(input("enter element :"))
            dll.insert_at_end(ele)
        elif(choice == 3):
            ele = int(input("enter element :"))
            pos = int(input("enter position :"))
            dll.insert_at_pos(ele,pos)
        elif(choice == 4):
            dll.del_at_beg()
        elif(choice == 5):
            dll.del_at_end()
        elif(choice == 6):
            pos = int(input("enter position to delete : "))
            dll.del_at_pos(pos)
        elif(choice == 7):
            dll.Traverse()
        elif(choice == 8):
            dll.ReveredList()
        else:
            quit()
    
            



        


        