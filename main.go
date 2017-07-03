package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func main() {
	wg := &sync.WaitGroup{}

	for i := 0; i < 7; i++ {
		wg.Add(1)

		go func() {
			time.Sleep(500 * time.Millisecond)
			sayHi(rand.Intn(10) + 1)

			wg.Done()
		}()

	}
	wg.Wait()
}

func sayHi(i int) {
	fmt.Println("hello", "thing", i)
}
