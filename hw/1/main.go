package main

import(
  "fmt"
  "errors"
)

type stack []int

func (s stack) Push(x int) stack {
    return append(s, x)
}

func (s stack) Pop() (stack, int, error) {

    _, err := s.isEmpty()
    l := len(s)

    if err != nil {
      fmt.Println(err)
      return s, 0, err
    }

    return s[:l-1], s[l-1], nil
}

func (s stack) isEmpty() (bool, error) {
  l := len(s)

  if l > 0 {
    return false, nil
  }

  return true, errors.New("Error: Stack is empty")
}

func (s stack) isEmpty2() (bool) {
  return len(s) == 0
}



func (s stack) Pop2() (stack, int) {
    l := len(s)

    if s.isEmpty2() {
      return s, 0
    }

    return s[:l-1], s[l-1]
}




func main(){
    myStack := make(stack,0)
    myStack = myStack.Push(1)
    myStack = myStack.Push(2)
    myStack = myStack.Push(3)

    myStack, x, _ := myStack.Pop()
    fmt.Println(x)

    myStack, x, _ = myStack.Pop()
    fmt.Println(x)

    myStack, x, _ = myStack.Pop()
    fmt.Println(x)

    myStack, x, _ = myStack.Pop()
    fmt.Println(x)

}
