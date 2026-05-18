class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def find(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def pop_front(self):
        if not self.head: 
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data
    
    def pop_back(self):
        if not self.head:
            return None

        # если один элемент
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        
        cur = self.head
        while cur.next.next:
            cur = cur.next
        removed_data = cur.next.data
        cur.next = None
        return removed_data
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next

        print("None")
#E5. Сложение полиномов
class PolyNode:
    def __init__(self, coeff, exp, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next
def add_polynomials(p1, p2):
    dummy = PolyNode(0, 0)
    cur = dummy

    while p1 and p2:

        if p1.exp > p2.exp:
            cur.next = PolyNode(p1.coeff, p1.exp)
            p1 = p1.next

        elif p2.exp > p1.exp:
            cur.next = PolyNode(p2.coeff, p2.exp)
            p2 = p2.next

        else:
            # одинаковые степени складываем
            new_coeff = p1.coeff + p2.coeff

            if new_coeff != 0:
                cur.next = PolyNode(new_coeff, p1.exp)

            p1 = p1.next
            p2 = p2.next

        if cur.next:
            cur = cur.next

    # остатки
    while p1:
        cur.next = PolyNode(p1.coeff, p1.exp)
        cur = cur.next
        p1 = p1.next

    while p2:
        cur.next = PolyNode(p2.coeff, p2.exp)
        cur = cur.next
        p2 = p2.next

    return dummy.next
def print_poly(head) -> None:
    cur = head
    parts = []

    while cur:
        parts.append(f"{cur.coeff}x^{cur.exp}")
        cur = cur.next

    print(" + ".join(parts))



def create_ll(size):
    ll = LinkedList()
    for i in range(size):
        ll.push_front(int(input()))
    return ll
def create_ll_auto(size):
    ll = LinkedList()
    for i in range(size):
        ll.push_front(size - i)
    return ll


#A5. Перенос последнего элемента в начало
def move_last_to_front(ll):
    last = ll.pop_back()
    ll.push_front(last)
    
#B5. Второй по величине элемент
def second_max(ll):
    first = None
    second = None
    cur = ll.head
    while cur:
        x = cur.data
        if first is None or x > first:
            if x != first:
                second = first
                first = x
        elif x != first and (second is None or x > second):
            second = x
        cur = cur.next
    return second

#C5. Поменять местами попарно
def swap_pairs(ll):
    cur = ll.head
    while cur and cur.next:
        cur.data, cur.next.data = cur.next.data, cur.data
        cur = cur.next.next
    return ll
#D5. Середина списка за один проход
def middle_node(ll):
    slow = ll.head
    fast = ll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data



ll = create_ll_auto(5)
ll.print_list()

move_last_to_front(ll)
ll.print_list()

ll = create_ll_auto(5)
swap_pairs(ll)
ll.print_list()

ll = create_ll_auto(5)
ll.print_list()
print(second_max(ll))
print(middle_node(ll))

p1 = PolyNode(3,4, PolyNode(2,2, PolyNode(1,0)))
p2 = PolyNode(5,3, PolyNode(2,2, PolyNode(4,1)))
result = add_polynomials(p1, p2)
print_poly(result)

        

    