package main
//可以去掉分号，因为C的while在go里面叫做for
import (
	"fmt"
)

func main() {
	sum := 1
	for sum < 1000{
		sum += sum
	}
	fmt.Println(sum)
}
