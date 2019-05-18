#!/usr/bin/python
#!encoding=UTF-8
import subprocess, sys, time

x=0
i=0
a=0
b=0
c=0
d=0

def remove_n(liste) :

        clear_list = []

        for i in range(len(liste)) :
                element=liste[i]
                element = list(element)
                element.pop(len(element)-1)
                clear_element = ''.join(str(i) for i in element)
                clear_element=str(clear_element)
                clear_list.append(clear_element)

        return clear_list

def read_value(file) :

        file = open(file,'r')
        value = file.readlines()
        file.close()

        return value

sequence = read_value('/home/Secure_Working_Sessions/ressources/files/sequence_value')
duration = read_value('/home/Secure_Working_Sessions/ressources/files/duration_value')
sequence = sequence[0]
duration = duration[0]
duration = int(duration)



def progress_bar() :
	i=0
	x=0
	double_braquet = '"'
	progress_bar = open('/home/Secure_Working_Sessions/ressources/bash/progress_bar.sh','w')

	progress_bar.write(str('#!/bin/bash\n('))

	while i<duration:
		line1 = str('\necho ')+double_braquet+str(x)+double_braquet+str(' ; sleep 0.5')
		line2 = str('\necho ')+double_braquet+str('# Work in progress ')+str(x)+str('%')+double_braquet
		progress_bar.write(line1)
		progress_bar.write(line2+str(';')+str(' sleep 0.5'))
		i=i+1
		x=i*100
		x=x/duration

	progress_bar.write(str('\necho ')+double_braquet+str('100')+double_braquet+str(' ; sleep 0.5'))
        progress_bar.write(str('\necho ')+double_braquet+str('# Work should now be completed ')+str('100')+str('%')+double_braquet)
	command = str('zenity')+str(' --progress --no-cancel --time-remaining --title ')+double_braquet+str('Current sequence : [')+str(sequence)+double_braquet+str('] --width=600 --height=20')
	progress_bar.write('\n) |\n')
	progress_bar.write(command)
	progress_bar.write(' | python /home/Secure_Working_Sessions/ressources/python/notification.py')
	progress_bar.close()
	subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/progress_bar.sh'])

progress_bar()
