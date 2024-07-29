#Create a class "Queue" with methods: enqueue, dequeue, and display. Hint: Use a list as a member
class Queue:
    def __init__(self):
        self.list=[]
    def enqueue(self, element):
        self.list.append(element)
    def dequeue(self):
        return self.list.pop(0)
    def display(self):
        print(self.list)

def choice():
    print("\n\nMENU\n1. Enqueue\n2.Dequeue\n3.Display\n4.EXIT")
    ch=int(input("Enter choice:"))
    return ch

#MAIN
queue=Queue()
while True:
    ch=choice()
    if ch==1:
        elmnt=int(input("Enter element to be enqueued:"))
        queue.enqueue(elmnt)
    elif ch==2:
       print("element dequeued:", queue.dequeue())
    elif ch==3:
        queue.display()
    elif ch==4:
        break
    else:
        print("Enter valid choice!!!")
