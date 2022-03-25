package main
//你也可以为非结构体类型声明方法
//在此例中，我们看到了一个带abs方法的数值类型MyFloat
//你只能为在同一包内定义的类型的接收者声明方法而不能为其他包内定义的类型（包括int之类的内建类型）的接收者声明方法
//就是接收者的类型定义和方发声明必须在同一包内，不能为内建类型声明方法
import (
	"fmt"
	"math"
)

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}
func main() {
	f:=MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())
}
