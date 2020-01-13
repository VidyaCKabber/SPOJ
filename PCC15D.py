case_count = int(input("Total total cases : "))
total_amount = 0
total_GST = 0

for case in range(case_count):
    items_count = int(input("Number of items "))
    for item in range(items_count):
        name, contity, price, GST_type, = input("Enter food name, contity,price and GST type respectively : ").split(' ')
        
        contity  = int(contity)
        price    = float(price)
        GST_type = GST_type.upper();
        
        total_amount = total_amount + contity * price
        
        if GST_type == 'SR':
            total_GST = total_GST + contity * price * 0.06
        
        total_amount = total_amount + total_GST
    print(f'Case # {case+1}')
    print(f'Total amount including GST : {total_amount}')
    print(f'Total GST : { total_GST}')
