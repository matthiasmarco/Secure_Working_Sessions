#!/usr/bin/python
#!encoding=UTF-8
import subprocess, time, os, sys

#installation
if not os.path.isfile('/home/Secure_Working_Sessions/installation'):
	print("               +--------------+")
	print("               | Installation |")
	print("               +--------------+\n")
	subprocess.call(['sudo','apt-get','install','ccrypt','mplayer','zenity','git','tree','nemo','-y'])
	if not os.path.isdir('/home/Secure_Working_Sessions'):
		os.chdir('/home/')
		subprocess.call(['git','clone','https://github.com/matthiasmarco/Secure_Working_Sessions/'])
	        #installation = open('/home/Secure_Working_Sessions/installation','w')##same as above line
		#installation.write('WSP installed')##here this file is needed for a continious use of WSP program.
		#installation.close() no comment granteed
        print("            +---------------------+")
        print("            | Installation sucess |")
        print("            +---------------------+\n")

#definition des fonctions subalternes

braquet = "'"
double_braquet = '"'

def cool_print(string, speed):
        string = list(string)
        i=0
        while i < len(string):
                time.sleep(speed)
                sys.stdout.write((string[i]))
                sys.stdout.flush()
		i=i+1

def animation() :
	subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/declaration.sh'])
	print('\n')
	cool_print('                      .                               \n',0.02)
	cool_print('                   .  |  .                            \n',0.02)
	cool_print('                 .    |    .                          \n',0.02)
	cool_print('               .      0      .                        \n',0.02)
	cool_print('                 .    |    .                          \n',0.02)
	cool_print('                   . _|_ .                            \n',0.02)
	cool_print('                      .                               \n',0.02)
	cool_print('\n                 ShadowedWSP',0.1)
	print('\n')
	time.sleep(2)

def clear_screen() :
	subprocess.call(['clear'])

def choose_a_dir () :
	subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/choose_dir.sh'])
	file = open('/home/Secure_Working_Sessions/ressources/files/dir','r')
	directory = file.readlines()
	file.close()
	directory = directory[0]
	os.remove('/home/Secure_Working_Sessions/ressources/files/dir')
	return directory

def save_session(directory) :
	file = open('/home/Secure_Working_Sessions/ressources/files/sessions_list','a')
	file.write(directory+str('\n'))
	file.close()

def remove_n_liste(liste) :
	clear_list = []
	for i in range(len(liste)) :
		element=liste[i]
		element = list(element)
		element.pop(len(element)-1)
		clear_element = ''.join(str(i) for i in element)
		clear_element = str(clear_element)
		clear_list.append(clear_element)
	return clear_list

def remove_n_string(string):
	clear_string = ""
	caracter_list = list(string)
	caracter_list.pop(len(caracter_list)-1)
	clear_caracter_list = ''.join(str(i) for i in caracter_list)
	clear_string = str(clear_caracter_list)
	return clear_string

def read_dir_list() :
        file = open('/home/Secure_Working_Sessions/ressources/files/sessions_list','r')
        dir_list = file.readlines()
        file.close()
        return dir_list

#execution du proigramme
#submenus

def Main() :
	cool_print('                                                      \n',0)
        cool_print('                      .                               \n',0)
        cool_print('                   .  |  .                            \n',0)
        cool_print('                 .    |    .                          \n',0)
        cool_print('               .      0      .                        \n',0)
        cool_print('                 .    |    .                          \n',0)
        cool_print('                   . _|_ .                            \n',0)
        cool_print('                      .                               \n',0)

	print('[Main]')
	print('|')
	print('|-1 Start a new session')
	print('|')
	print('|-2 Open a previous working sequence')
	print('|')
	print('|-3 Start a rootkit scan')
	print('|')
	print('|-4 Settings')
	print('|')
	print('|-5 About')
	print('|')
	print('|-6 Contact')
	print('|')
	print('+---http://ftp.fau.de/cdn.media.ccc.de/')

animation()
clear_screen()
Main()

def About() :

	clear_screen()
	print("[About]")
	print("|")
	cool_print("| This tool is aimed at help you to keep the integrity\n",0.06)
	cool_print("| of your work, it considerabily reduce the risk of\n",0.06)
	cool_print("| beeing infected by a third party.\n",0.06)
	cool_print("|",0.06)
	cool_print("\n+---------------coded by ~ Morphovid-----------------+\n",0.06)
	time.sleep(4)

	clear_screen()
	Main()
	programm()

def Start_a_new_session() :

        clear_screen()
        print("[Starting a new session]\n")

	sequence = raw_input('\nenter the name of the sequence :\ne.g : "Finish the html module" , "Learn about Li-Fi networks" , "Newspaper break" etc... \n> ')
	duration = raw_input('\nenter the time you plan for it to be achieved (unit: minutes)\n> ')
	duration = int(duration)*60

	sequence_value = open('/home/Secure_Working_Sessions/ressources/files/sequence_value','w')
	sequence_value.write(sequence)
	sequence_value.close()

	duration_value = open('/home/Secure_Working_Sessions/ressources/files/duration_value','w')
        duration_value.write(str(duration))
	duration_value.close()

	print('\nNow please choose a directory for your session ... ')
	time.sleep(3)
#
	directory = choose_a_dir()
	directory = remove_n_string(directory)
	directory = directory+str('/')+sequence+('/')
	current_session_dir = open('/home/Secure_Working_Sessions/ressources/files/current_session_dir','w')
	current_session_dir.write(directory)
	current_session_dir.close()
	os.mkdir(directory)
        save_session(directory)
	dir_list = read_dir_list()
	dir_list = remove_n_liste(dir_list)
#
	print(str('\nStarting sequence : ')+str(sequence)+str('...\n'))
	time.sleep(2)
	subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/new_session.sh'])
        clear_screen()
        Main()
	programm()

def Open_a_previous_working_sequence() :

	clear_screen()
	print('[previous working sessions]')
	print('|')

	k=0
	dir_list = read_dir_list()
	dir_list = remove_n_liste(dir_list)

	for i in range(len(dir_list)) :

                print(str('|-')+str(k)+str(' ')+str(dir_list[i]))
		k=k+1

	options = k
	print('|-')+str(options)+str(' OPTIONS')
	back = k+1
	print('|-')+str(back)+str(' RETURN')
	print('|')
	print('+---http://ftp.fau.de/cdn.media.ccc.de/')

	choice = input('Your choice :\n> ')

	if choice == back :
		clear_screen()
		Main()
		programm()

	if choice == options :
        	clear_screen()
        	print('[previous working sessions]/[OPTIONS]')
		print('|')
		print('|-1 Clear all Sessions')
		print('|-2 Select and remove ')
        	print('|-3 RETURN')
		print('|')
        	print('+---http://ftp.fau.de/cdn.media.ccc.de/')
		choice = input('Your choice :\n> ')

		if choice == 1 :
			print('Securely removing the sessions....')
			print('Curentrly under development ......')
		        time.sleep(2)
	        	clear_screen()
	        	Main()
        		programm()

		if choice == 2 :
			print('Zenity code here to get the selection list....')
                        print('Curentrly undr development .......')
                        time.sleep(2)
                        clear_screen()
                        Main()
                        programm()

		if choice == 3 :
                        time.sleep(2)
		        clear_screen()
                	Main()
                	programm()

	else :
		dir = dir_list[choice]
		dir = braquet+str(dir)+braquet
		process_content = str("nemo ")+dir+str(" >/dev/null 2>&1 </dev/null &")
		process = open('/home/Secure_Working_Sessions/ressources/bash/open_folder.sh','w')
		process.write(str("#!/bin/bash\n"))
		process.write(process_content)
		process.close()
		subprocess.call(['bash','/home/Secure_Working_Sessions/ressources/bash/open_folder.sh'])
		time.sleep(2)
		clear_screen()
		Main()
		programm()

def Start_a_rootkit_scan() :

	clear_screen()
	print("currently under development......")

	time.sleep(2)
	clear_screen()
	Main()
	programm()

def Settings() :

	clear_screen()
        print("currently under development......")
        time.sleep(2)

        clear_screen()
        Main()
        programm()

def Contact() :

	clear_screen()
        print("currently under development......")
        time.sleep(2)

        clear_screen()
        Main()
        programm()

def programm() :
	choice = input('\nYour choice :\n> ')
	if 0<choice<7 :
       		if choice == 1 :
                	Start_a_new_session()
        	if choice == 2 :
                	Open_a_previous_working_sequence()
        	if choice == 3 :
                	Start_a_rootkit_scan()
        	if choice == 4 :
                	Settings()
        	if choice == 5 :
                	About()
        	if choice == 6 :
                	Contact()
programm()

"""
NOTES :

-pour la reouverture d'ancienne session, demander a nautilus de s'ouvrir dans la
directory enregistree avec >/dev/null 2>&1 </dev/null &

-pour ouvrir un nouveau terminal |a chaque debut de tache| : xterm -hold -e command >/dev/null 2>&1 </dev/null &

"""
