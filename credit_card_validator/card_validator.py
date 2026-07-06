card_no = input('Enter your credit card number: ')
odd_sum = 0
even_sum = 0
double_list = []
number = list(card_no)

for (idx,val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        double_list.append(int(val)*2)

double_string = ""
for x in double_list:
    double_string+= str(x)
#converting string to list
double_list = list(double_string)
for x in double_list:
    even_sum+= int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('Valid card!')
else:
    print('Invalid card!')

