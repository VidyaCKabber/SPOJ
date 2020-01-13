count = int(input("Enter the count : "))
for item in range(count):
    a,b = input("Enter two numbers : ").split(' ')
    try:
        a = int(a)
        try:
            b = int(b)
            print(int(a)+int(b))
        except:
            b = float(b) 
            print(int(a)+float(b))
    except :
        try:
            b = int(b)
            print(float(a)+int(b))
        except :
            print(float(a)+float(b))
