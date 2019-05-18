#!/usr/bin/python
#encoding=UTF-8

import os, subprocess

def read_dir_value() :
        file = open('/home/Secure_Working_Sessions/ressources/files/current_session_dir','r')
        dir_value = file.readlines()
        file.close()
	dir_value = dir_value[0]
	print(dir_value)
        return dir_value

dir_value = read_dir_value()

tree = open('/home/Secure_Working_Sessions/ressources/bash/temp_tree.sh','w')
tree.write('#!/bin/bash\n#encoding=UTF-8\n')
tree.write('echo "[ Your current session dir ] :"\n')
tree.write('tree '+dir_value)
tree.write('\nsleep 9000')
tree.close()
