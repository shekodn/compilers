package stack

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
