package main

import(
  "fmt"
  "github.com/shekodn/compilers/hw/1/stack"
  "github.com/shekodn/compilers/hw/1/queue"
  "github.com/shekodn/compilers/hw/1/hash"
)


func main(){

    myStack := make(stack.Stack,0)
    // TODO - Use Testing package to automate and make real tests
    myStack.ChecksStack()

    fmt.Println("- - -")

    myQueue := make(queue.Queue,0)
    // TODO - Use Testing package to automate and make real tests
    myQueue.ChecksQueue()

    fmt.Println("- - -")

    // Go’s map is a hashmap
    myHash := make(hash.Hash)
    myHash["mexico"] = 2
    myHash["usa"] = 1

    i, ok := myHash["mexico"]

    if ok {
      fmt.Println(i, " is in hash")
    } else {
      fmt.Println(i, " is not in hash")
    }

    for key, value := range myHash {
      fmt.Println("key: ", key, " value: ", value)
    }
}
