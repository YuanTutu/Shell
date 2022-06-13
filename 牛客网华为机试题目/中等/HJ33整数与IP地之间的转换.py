

# a=1010000000000000001111000001
# print(type(a))
# b=str(a)
# print(int(b,2))

# ipaddres=input().split('.')
def IPtoNum(ipaddres):
    bin_ip=[]
    for i in ipaddres:
        bin_ip.append(bin(int(i))[2:].rjust(8,'0'))
    erjinzhi=''
    for i in bin_ip:
        erjinzhi+=i
    shijinzhi=int(erjinzhi,2)
    print(shijinzhi)

def NumtoIP(num):
    erjinzhi=bin(num)[2:].rjust(32,'0')
    fenge=[]
    IPADDR=[]
    for i in range(0,32,8):
        fenge.append(erjinzhi[i:i+8])
    for i in fenge:
        j=int(i,2)
        IPADDR.append(j)
        IPADDR.append('.')
    for i in IPADDR[:-1]:
        print(i,end='')


if __name__ == "__main__":
    ipaddres = input().split('.')
    num = int(input())
    IPtoNum(ipaddres)
    NumtoIP(num)