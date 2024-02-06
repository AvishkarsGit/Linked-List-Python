class Node:
    def __init__(self):
        self.data = None
        self.next = None

def create_List(N):
    head = Node()
    x = int(input("Enter data:"))
    head.data = x
    head.next = None
    p = head
    for i in range(1,N,1):
        x = int(input("Enter data:"))
        p.next = Node()
        p = p.next
        p.data = x
        p.next = None
    return head


def display_list(p):
    while p is not None:
        print(p.data,end="->")
        p = p.next
    print("None")

def append_start(x,head):
    q = Node()
    q.data = x
    q.next = None
    if head is None:
        head = q
        return head
    else:
        q.next = head
        head = q
        return head


def append_middle(x,head):
    q = Node()
    q.data = x
    q.next = None

    p = head
    loc = int(input("At which position you want to insert your data:"))
    for i in range(1,loc-1,1):
        p = p.next
    
    q.next = p.next
    p.next = q
    return head
     
def append_end(x,head):
    q = Node()
    q.data = x
    q.next = None

    p = head
    while p.next is not None:
        p = p.next
    p.next = q
    return head

def remove_start(head):
    q = head
    if head is None:
        print("Linked list is empty")
    else:
        head = head.next
        del(q)
        return head

def search_node(x,head):
    p = head
    flag = 0
    while p is not None:
        if x is p.data:
            flag=1
            break
        else:
            p = p.next
    if flag == 1:
        return True
    else:
        return False

def remove_middle(x,head):
    p = head
    if head is None:
        print("linked list is empty")
    else:
        if search_node(x,head) == True:
            while p is not None:
                if p.next.data is x:
                    q = p.next
                    p.next = q.next
                    del(q)
                else:
                    p = p.next
        else:
            print("Node is not found!")
    return head


def remove_end(head):
    p = head
    while p.next.next is not None:
        p = p.next
    q = p.next
    p.next = None
    del(q)
    return head

def merge_list(head):
    n = int(input("How much nodes do you want to add in second linked list:"))
    head2 = create_List(n)
    p = head
    while p.next is not None:
        p = p.next
    p.next = head2
    return head

def sort(head):
    p = head
    while p.next is not None:
        q = p.next
        while q is not None:
            if p.data > q.data:
                temp = p.data
                p.data = q.data
                q.data = temp
            q = q.next
        p = p.next
    return head

choice = 0
head = Node()

while choice!=8:
    print("\n\n*** SLL MENUS ***")
    print("1.create List")
    print("2.Display List")
    print("3.Insertion At List")
    print("4.Deletion From List")
    print("5.Merge Two Lists")
    print("6.Sort List")
    print("7.Search Node")
    print("8.Exit")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        n = int(input("How much nodes do you wants to add:"))
        head = create_List(n)
    elif choice == 2:
        display_list(head)
    elif choice == 3:
        print("\n\n")
        print("*** INSERTION ***")
        print("1.At Start")
        print("2.At Middle")
        print("3.At End")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            x = int(input("Enter Data for insertion :"))
            head = append_start(x,head)
            display_list(head)
        elif ch == 2:
            x = int(input("Enter Data for insertion :"))
            head = append_middle(x,head)
            display_list(head)
        else:
            x = int(input("Enter Data for insertion :"))
            head = append_end(x,head)
            display_list(head)

    elif choice == 4:
        print("\n\n")
        print("*** DELETION ***")
        print("1.From Start")
        print("2.From Middle")
        print("3.From End")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            head = remove_start(head)
            display_list(head)
        elif ch == 2:
            x = int(input("Enter data:"))
            head = remove_middle(x,head)
            display_list(head)
        else:
            head = remove_end(head)
            display_list(head)
    elif choice == 5:
        head = merge_list(head)
        display_list(head)
    elif choice == 6:
        head = sort(head)
        display_list(head)
    elif choice == 7:
        x = int(input("Enter data for search:"))
        if search_node(x,head) == True:
            print(" Node is present ate linked list:")
            display_list(head)
        else:
            print("node is not found!")

    elif choice == 8:
        print("Thanks")

        # 10->20->30->11->22->33->none

