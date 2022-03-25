package main
//方法即函数
//方法只是个带接收者参数的函数
//现在这个abc的写法就是个正常的函数，功能没什么变化
import (
	"fmt"
	"math"
)

type Vertex struct {
	X,Y float64
}

func (v Vertex) Abs() float64  {
	return math.Sqrt(v.X*v.X+v.Y*v.Y)
}
func main() {
	v:=Vertex{3,4}
	fmt.Println(v.Abs())
}
