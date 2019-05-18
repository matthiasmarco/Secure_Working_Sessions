#!/usr/bin/python
#!encoding=UTF-8
import subprocess, sys, time

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

def notification() :

	sequence = read_value('/home/Secure_Working_Sessions/ressources/files/sequence_value')
	duration = read_value('/home/Secure_Working_Sessions/ressources/files/duration_value')
	sequence = sequence[0]
	duration = duration[0]
	duration = int(duration)

	x=0
	i=0
	a=0
	b=0
	c=0
	d=0


        while i<duration:
                time.sleep(1)
                i=i+1
                x=i*100
                x=x/duration

                if x >= 25 and a == 0 :
                        a=1
                        subprocess.call(['zenity','--notification','--text="[WSP] : 25% of the sequence should now be completed"'])
                if x >= 50 and b == 0 :
                        b=1
                        subprocess.call(['zenity','--notification','--text="[WSP] : 50% of the sequence should now be completed"'])
                if x >= 75 and c == 0 :
                        c=1
                        subprocess.call(['zenity','--notification','--text="[WSP] : 75% of the sequence should now be completed"'])
                if x >= 100 and d == 0 :
                        d=1
                        subprocess.call(['zenity','--notification','--text="[WSP] : You reached the end of the sequence time"'])
   			subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/end_session.sh'])

notification()
