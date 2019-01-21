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

func main(){
    myStack := make(stack,0)
    myStack = myStack.Push(1)
    myStack = myStack.Push(2)
    myStack = myStack.Push(3)

    myStack, x := myStack.Pop()
    fmt.Println(x)

    myStack, x = myStack.Pop() /
    fmt.Println(x)

    myStack, x = myStack.Pop()
    fmt.Println(x)

    myStack, x = myStack.Pop() //0
    fmt.Println(x)

    myStack, x = myStack.Pop() //0
    fmt.Println(x)
}
