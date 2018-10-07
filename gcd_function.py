def gcd_func(m,n):
    
    while m%n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m%old_n
        
    print(n)
   

a = input("Enter two numbers(separated by a(one) space): ")
first_num, sec_num = a.split(' ')
gcd_func(int(first_num),int(sec_num))

