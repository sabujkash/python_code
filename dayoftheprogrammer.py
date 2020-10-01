import math

constant = 243  #sum of days till august 
n = int(input())

elif n % 4 == 0 and n < 1918:
    constant += 1
    constant = 256 - constant
elif n % 400 or (n % 4 == 0 and n % 100 != 0):
    constant += 1                                      
    constant=256-constant                             
else:
    constant= 256-constant

print('{0}.{1}.{2}'.format(constant,'09',n)) 