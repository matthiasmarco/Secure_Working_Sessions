import sys, time

def triangle_left() :
	a = ""
	b = "."
	c = " "
	xterm_width = 79

	i=2

	while i < 79 :

		a = a+b

		sys.stdout.write(((xterm_width-i*1)*c)+b+a+'\n')
		time.sleep(0.05)
		sys.stdout.flush()

		i = i+1
j=0

while j<9000 :
	triangle_left()
	j=j+1
