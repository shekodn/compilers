package stack

import(
  "fmt"
)

type Stack []int

func (s Stack) Push(x int) Stack {
    return append(s, x)
}

func (s Stack) IsEmpty() (bool) {
  return len(s) == 0
}

func (s Stack) Pop() (Stack, int) {
    l := len(s)

    if s.IsEmpty() {
      return s, 0
    }

    return s[:l-1], s[l-1]
}

func (s Stack) Top() int {
  l := len(s)

  if s.IsEmpty(){
    return 0
  } else {
    return s[l-1]
  }
}

///
func (s Stack) ChecksStack() {
  myStack := make(Stack,0)
  fmt.Println("Empty?: ", myStack.IsEmpty())
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
