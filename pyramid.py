#CO2 PRGRM3
#PYRAMID
def func_pyramid():
 rows = int(input("Enter the number of rows: "))    
 for i in range(1, rows):     
    for j in range(1, i + 1):     
        print(i*j, end='  ')    
    print()    
func_pyramid()