package main

import (
	"fmt"
	"math"
)

//方法
//Go 没有类，不过你可以为结构体类型定义方法
//方法就是一类带特殊的接收者参数的函数
//方法接收者在他自己带参数列表内，位于func关键字和方法名之间
//在此例中，Abs方法拥有一个名为V，类型为Vertex的接收者

type Vertex struct {
	X,Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X+v.Y*v.Y)
}
func main() {
	v:= Vertex{3,4}
	fmt.Println(v.Abs())
}
