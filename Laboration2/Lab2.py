#from arrayQFile import ArrayQ
from linkedQFile import LinkedQ
import sys


def card_trick():
    #print("Vilken ordning ligger korten i?")
    #numbers = input().split()
    numbers = sys.stdin.readline()
    #numbers = "3 1 4 2 5"
    numbers = numbers.split()
    #print(numbers)
    #q = ArrayQ()
    #card_r = ArrayQ()
    q = LinkedQ()
    card_r = LinkedQ()
    for x in numbers:
        q.enqueue((x))
    #q.get_items()
    #print(q.get_size())

    while q.get_size() > 0: 
        front_num = q.dequeue()
        #print(front_num)
        q.enqueue(front_num)
        second_num = q.dequeue()
        #print(second_num)
        card_r.enqueue(second_num)
        #q.print_queue()
    
    card_r.get_items()

def main():
    card_trick()

main()