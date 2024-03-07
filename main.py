num = input('Enter a number (decimal only): ')
# type your code here
num = num.strip()
index = num.find('.')
rem_val = num[index+1:]
dp = len(rem_val)


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
