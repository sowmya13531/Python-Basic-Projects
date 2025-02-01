#Python credit card validator program

#1.Remove any '-' and ' '
#2.Add all digits in the odd places from right to left
#3.Double every second digit from right to left
#       (If result is a 2-digit number,
#          add the 2-digit number together to get a single digit.)
#4.Sum the totals of steps 2&3
#5.If sum is divisible by 10, the credit card # is valid

sum_odd_num = 0
sum_even_num = 0

#step1
card_num = input("Enter credit card num:")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]

#step2
for x in card_num[::2]:
    sum_odd_num += int(x)

#step3
for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_num += (1 + (x % 10))
    else:
        sum_even_num += x

#step4

total = sum_odd_num + sum_even_num

#step5
if total % 10 == 0:
    print("VALID")
else:
    print("Invalid")