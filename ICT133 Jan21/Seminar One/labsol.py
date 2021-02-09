# https://www.w3schools.com/python/ref_string_format.asp
# https://www.python-course.eu/python3_formatted_output.php

import math
from math import sqrt, pow

def q9():

    hrs = int(input("Enter current hr: "))
    mins =  int(input("Enter current min: "))
    secs =  int(input("Enter current sec: "))

    secs_new = (secs + 1) % 60
    mins_new = (((secs + 1) // 60) + mins) % 60
    hrs_new =  (((((secs + 1) // 60) + mins) // 60) + hrs ) % 24

    print(f"Clock time is {hrs:02d}:{mins:02d}:{secs:02d}")
    print(f"After 1 second, the time is {hrs_new:02d}:{mins_new:02d}:{secs_new:02d}")

q9()

def q8():

    loan = float(input("Enter the loan amount: "))
    duration = int(input("Enter the duration (in years): "))
    interest = float(input("Enter the interest rate: "))

    c = loan * pow(( 1 + interest/100), duration)

    print(f"The total compound interest to be paid is {c:10.2f}")

#q8()

def q7():

    #input
    s1 = float(input('Enter side a: '))
    s2 = float(input('Enter side b: '))
    s3 = float(input('Enter side c: '))

    s4 = 1/2 * (s1 + s2 + s3)

    area = math.sqrt(s4 * (s4 - s1) * (s4 - s2) * (s4 - s3) )
    area = sqrt(s4 * (s4 - s1) * (s4 - s2) * (s4 - s3) )

    print(f'The area is {area}')

#q7()

def q6():

    # input
    bill = float(input('Enter meal amount ($):'))

    cost = bill * 0.5
    service = cost * 0.1
    GST = (cost + service) * 0.07
    total = cost + service + GST

    print(f'Receipt')
    print(f'Cost of meal:   ${bill:6.2f}')
    print(f'50% discount:   ${cost:6.2f}')
    print(f'Service charge: ${service:6.2f}')
    print(f'GST:            ${GST:6.2f}')
    print(f'Total amount:   ${total:6.2f}')

#q6()

def q5():

    # input
    cents = int(input('Enter the number of cents: '))

    # process
    c50 = cents // 50
    c10 = (cents % 50 ) // 10
    c5 = (cents % 10) // 5
    c1 = cents % 5

    print(f'{cents} cents is equal to {c50} 50-cents, {c10} 10-cents, {c5} 5-cents, {c1} 1-cent')

#q5()

def q4():

    n1 = int(input('Enter the number of seconds: '))

    # hms

    h = n1 // 3600
    m = n1 // 60 % 60 
    s = n1 % 60

    print(f'{n1} seconds is equal to {h} hour(s), {m} minute(s), {s} seconds')

#q4()

def q3():

    n1 = int(input('Enter the 3-digits number : '))

    # hto

    h = n1 // 100
    t = n1 // 10 % 10
    o = n1 % 10

    sum1 = h + t + o
    prod1 = h * t * o

    print(f'The sum of the 3 digits is {sum1} and the product is {prod1}')

#q3()

def q2():

    n1 = float(input('Enter the first number : '))
    n2 = float(input('Enter the second number : '))
    n3 = float(input('Enter the third number : '))

    sum1 = n1 + n2 + n3
    ave1 = sum1/3

    print(f"The sum of the 3 numbers is {sum1}, and the average is {ave1}")

#q2()

def q1(): 

  # read the temperature in fahrenheit
  # calculate temp in c
  # output c

  f = float(input('Enter the temperature in Fahrenheit : '))

  c = 5/9 * (f - 32)

  print(f'The temperature in Celcius is {c}')
  print(f'The temperature in Celcius is {c:10.2f}')

#q1()

