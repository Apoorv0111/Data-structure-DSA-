class Stack():
    def __init__(self, size=5):
        self.Max_size = size
        self.arr = size * [None]
        self.top = -1

    def push(self, value):
        if self.top < self.Max_size - 1:
            self.top += 1
            self.arr[self.top] = value

        else:
            print()
            print("\nStack Overflow!")

    def pop(self):
        if self.top == -1:
            print("\nStack Underflow!")
        else:
            value = self.arr[self.top]
            self.top -= 1
            print("Pop Sucessful!\n")
            return value

    def __str__(self):
        length = self.top
        s = ""
        for i in range(length, -1, -1):
            s = s + str(self.arr[i]) + "\n"
        return s

size = int(input("enter the size of stack: "))
list = Stack(size)
print("Enter the operation you want to perform:")
print("Enter 1 to push")
print("Enter 2 to pop")
print("Enter 3 to display")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.push(int(input("Enter the value you want to push:")))
        print("\n",list)

    elif option == 2:
        list.pop()
        print("\n",list)

    elif option == 3:
        print(list)

    else:
    	break







