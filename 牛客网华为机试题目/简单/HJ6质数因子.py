def find_factors(number):
    is_prime = True
    for i in range(2, int(number ** 0.5 + 2)):
        if number % i == 0:
            is_prime = False
            print(str(i), end=" ")
            find_factors(int(number / i))
            break

    if is_prime:
        print(str(number), end=" ")

    return


try:
    number = int(input())
    if number <= 0:
        raise Exception
    find_factors(number)
except Exception as e:
    exit()


# 会超时
# N = int(input())
# i= 2
# while i<=N:
#     while N % i == 0:
#         N /= i
#         print(str(i),end=" ")
#     i += 1