
#백준 _10845 풀이
import sys

class Queue :
    def __init__(self):
        self.queue = [];
        self.front = 0;
        self.back = 0;
        self.size = 0;

    def isEmpty(self):
        if self.queue:
            return 0;
        else :
            return 1;

    def push(self, data):
        self.queue.append(data);
        self.back += 1;                     #back조정
        self.size += 1;

    def pop(self):
        if self.isEmpty():
            return -1;
        else :
            dequeued = self.queue[0];
            self.front += 1;                 #front 조정
            self.size  -= 1;                 #size 조정

            self.queue = self.queue[self.front:]
            self.front = 0;                   #front의 index조정
            return dequeued;

    def getFront(self):
        if self.isEmpty():
            return -1;
        else :
            return self.queue[0];           #첫번쨰 원소 출력

    def getBack(self):
        if self.isEmpty():
            return -1;
        else:
            return self.queue[-1];          #마지막 원소 출력


myQueue = Queue();


T = int(sys.stdin.readline().rstrip());

for i in range (0,T):
    word = (sys.stdin.readline().rstrip().split());
    if(word[0] == "push"):                  #push 구현
        myQueue.push((word[1]));
    elif (word[0] == "front"):             
        print(myQueue.getFront());
    elif (word[0] == "back"):
        print(myQueue.getBack());
    elif (word[0] == "pop"):
         print(myQueue.pop());
    elif (word[0] == "empty"):             #is empty 구현
        print(myQueue.isEmpty());
    elif (word[0] == "size") :               #word 구현
        print(myQueue.size);

    
