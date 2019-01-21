package main

import(
  "fmt"
)

type stack []int

func (s stack) Push(x int) stack {
    return append(s, x)
}

func (s stack) isEmpty() (bool) {
  return len(s) == 0
}

func (s stack) Pop() (stack, int) {
    l := len(s)

    if s.isEmpty() {
      return s, 0
    }

    return s[:l-1], s[l-1]
}

func (s stack) Top() int {
  l := len(s)

  if s.isEmpty(){
    return 0
  } else {
    return s[l-1]
  }
}
/////////

type queue []int

func (q queue) PushBack(x int) queue {
    return append(q, x)
}

func (q queue) Size() int {
    return len(q)
}

func (q queue) isEmpty() (bool) {
  return len(q) == 0
}

func (q queue) PopFront() (queue) {
  l := len(q)
  if q.isEmpty() {
    return q
  }
  return q[1:l]
}

func (q queue) PopBack() (queue) {
  l := len(q)
  if q.isEmpty() {
    return q
  }
  return q[0:l-1]
}

func (q queue) Front() (int) {
  if q.isEmpty() {
    return 0
  }
  return q[0]
}

func (q queue) Back() (int) {
  l := len(q)
  if q.isEmpty() {
    return 0
  }
  return q[l-1]
}

func checksStack() {
  myStack := make(stack,0)
  fmt.Println("Empty?: ", myStack.isEmpty())
  myStack = myStack.Push(10)
  myStack = myStack.Push(12)
  myStack = myStack.Push(14)
  myStack = myStack.Push(16)

  fmt.Println("Stack: ", myStack)
  fmt.Println("Top:", myStack.Top())
  myStack = myStack.Push(1)
  fmt.Println("Push 1:", myStack)
  fmt.Println("Top:", myStack.Top())
  myStack, _ = myStack.Pop()
  fmt.Println("Pop 1, so new top is:", myStack.Top())
}

func checksQueue() {
  myQueue := make(queue,0)
  myQueue = myQueue.PushBack(10)
  myQueue = myQueue.PushBack(12)
  myQueue = myQueue.PushBack(14)
  myQueue = myQueue.PushBack(16)

  fmt.Println("Queue:", myQueue)
  fmt.Println("Size:", myQueue.Size())
  fmt.Println("isEmpty?:", myQueue.isEmpty())
  fmt.Println("Front:", myQueue.Front())
  fmt.Println("Back:", myQueue.Back())

  myQueue = myQueue.PushBack(18)
  fmt.Println("Push back 18:", myQueue)

  myQueue = myQueue.PopFront()
  fmt.Println("Pop front:", myQueue)

}

func main(){

    checksStack()
    fmt.Println("- - -")
    checksQueue()

}
