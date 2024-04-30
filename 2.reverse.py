def reverseString(x) :
    # 투포인터 문제로도 볼 수 있음
    rever = [ i for i in x[::-1]]
    print(rever)


reverseString(["H", "e", "l", "l", "o"])