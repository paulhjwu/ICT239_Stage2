'Ann'
"Ann"
'''Ann'''

greet = "Hello Bob"
x = 0
y = 6
print(greet[y - 2])
print(greet[0], greet[6])
print(greet[x], greet[y])
print(greet[-9], greet[-3])

# Slide 7

greet[0:3]
greet[0:3:1]

greet[3:0:-1]

greet[:5]
greet[0:5:1]

greet[5:]
greet[5:9:1]

greet[:]
greet[0:9:1]

greet[::-1]
greet[-1::-1]

# slide 8

"Hello" + "Bob"
greet[0] + greet[-1]
greet[0:2]*3

# slide 9

len("spam")
len(greet)

# slide 11

#firstName, lastName = input("Enter first name \
#     followed by last name:").split()

n1, n2 = [2, 3]
"Paul Wu".split()

#firstName, middleName, lastName = input("Enter first name, middle name, and \
#     followed by last name: ").split()

#hr:mn:sc

#hr, min, sec = input("Enter the hour, mins, and secs in hr:mn:sc format ").split(":")

#Slide 16

aList = ["Smith", "Mr.", 100]
a = f"{aList[1]} {aList[0]} won ${aList[2]}"

"Number, {0:8.3f}, 3 dec places".format(3.1416)

"left justification, min 5 characters: {0:<5s}".format("Hi!")

# slide 21

5 > 0

# Slide 24

import math
from math import sqrt

def main():

     a = float(input("Enter coefficient a: "))
     b = float(input("Enter coefficient b: "))
     c = float(input("Enter coefficient c: "))
     discrim = b * b - 4 * a * c

     if discrim < 0:
          print("No real roots")
     #if discrim >= 0:
     else:
          discRoot = sqrt(discrim)
          root1 = (-b + discRoot) / (2 * a)
          root2 = (-b - discRoot) / (2 * a)
          print(root1, root2)

#main()

def q9():

  #input
  hr, min, sec = input("Enter the current hr:mn:sc ").split(':')

  #These statements not necessary
  s = int(sec) % 60
  m = int(min) % 60
  h = int(hr) % 24
    
  #after 1 sec
  s_plus1 = (s + 1) % 60
  m_plus1 = (((s + 1)//60) + m) %60
  h_plus1 = (((((s + 1)//60) + m) // 60 ) + h) % 24

  s_plus1 = s + 1
  
  if s_plus1 == 60:
      s_plus1 = 0
      m_plus1 = m + 1
      if m_plus1 == 60:
          m_plus1 = 0
          h_plus1 = h + 1
          if h_plus1 == 24:
              h_plus1 = 0


  print("Clock time is ""{:02d}".format(h),":","{:02d}".format(m),":","{:02d}".format(s))
  print("After 1 seconds the time is ""{:02d}".format(h_plus1),":","{:02d}".format(m_plus1),":","{:02d}".format(s_plus1))

q9()
