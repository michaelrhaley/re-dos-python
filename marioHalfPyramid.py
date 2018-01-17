#Mario half pyramid in python
import sys
import cs50
#x = 0
ht = int(input("Height of Mario's pyramid: "))
while True:
    (ht <= 0 and ht >= 24)

    for i in range(1, ht+1):
        print(" " * (ht - i) + "#" * i + " " + ("#" * i))
    
    print("\n")
    break

#for x in range(ht):
#        print("#")
#        for h in range(x+1):
#            print("#", end = "")