import sys, time

def triangle_right() :
	a = ""
	b = "."

	i=0

	while i < 76 :

		a = a+b

		sys.stdout.write(a+b+"\n")
		time.sleep(0.05)
		sys.stdout.flush()

		i = i+1

j=0

while j<9000 :
	triangle_right()
	j=j+1
