from itertools import product
import string

min = int(input("min:"))
max = int(input("max:"))

cntr = 0

# car = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
# l = "s"+"S"+"h"+"H"+"m"+"M"+"u"+"U"+"l"+"L"+"I"+"i"+"a"

# car = string.digits
car = "1234567890"

f_o = open("pass.txt", 'w')

for i in range(min, max + 1):
	for j in product(car, repeat=i):
		word = "".join(j)
		f_o.write("9"+word+"03")
		f_o.write("\n")
		cntr += 1

print("{} passowrd".format(cntr))
