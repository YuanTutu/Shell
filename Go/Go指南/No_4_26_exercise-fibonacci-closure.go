package main
//实现一个 fibonacci 函数，它返回一个函数（闭包），
//该闭包返回一个斐波纳契数列 `(0, 1, 1, 2, 3, 5, ...)`。
import "fmt"

func fibonacci() func() int {
	//sum := 0
	//return func(x int) int {
	//	sum += sum
	//	return sum
	back1, back2:= 0, 1  // 预先设定好两个初始值

	return func() int {

		temp := back1 //记录（back1）的值
		back1,back2 = back2,(back1 + back2) // 重新赋值(这个就是核心代码)
		return temp //返回temp
	}
}
func main() {
	f:= fibonacci()
	for i:=0;i<10;i++{
		fmt.Println(f())
	}
}
