package queue

import (
  "fmt"
)

type Queue []int

func (q Queue) PushBack(x int) Queue {
    return append(q, x)
}

func (q Queue) Size() int {
    return len(q)
}

func (q Queue) IsEmpty() (bool) {
  return len(q) == 0
}

func (q Queue) PopFront() (Queue) {
  l := len(q)
  if q.IsEmpty() {
    return q
  }
  return q[1:l]
}

func (q Queue) PopBack() (Queue) {
  l := len(q)
  if q.IsEmpty() {
    return q
  }
  return q[0:l-1]
}

func (q Queue) Front() (int) {
  if q.IsEmpty() {
    return 0
  }
  return q[0]
}

func (q Queue) Back() (int) {
  l := len(q)
  if q.IsEmpty() {
    return 0
  }
  return q[l-1]
}

func (q Queue) ChecksQueue() {
  myQueue := make(Queue,0)
  myQueue = myQueue.PushBack(10)
  myQueue = myQueue.PushBack(12)
  myQueue = myQueue.PushBack(14)
  myQueue = myQueue.PushBack(16)

  fmt.Println("Queue:", myQueue)
  fmt.Println("Size:", myQueue.Size())
  fmt.Println("IsEmpty?:", myQueue.IsEmpty())
  fmt.Println("Front:", myQueue.Front())
  fmt.Println("Back:", myQueue.Back())

  myQueue = myQueue.PushBack(18)
  fmt.Println("Push back 18:", myQueue)

  myQueue = myQueue.PopFront()
  fmt.Println("Pop front:", myQueue)

}
