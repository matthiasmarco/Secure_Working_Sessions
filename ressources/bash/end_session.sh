#!/bin/bash

python /home/Secure_Working_Sessions/ressources/python/tree.py

if zenity --question --width=300 --height=10 --cancel-label "Yes, i have finished" --ok-label "No, i need more time" --title="Time has reached the end" --text="\nHave you finish your session ?"
then
	python /home/Secure_Working_Sessions/ressources/python/additional_time.py
else
	gnome-terminal --geometry 79x80+0+400 -- bash /home/Secure_Working_Sessions/ressources/bash/temp_tree.sh

	if zenity --question --width=500 --height=10 --cancel-label "Archive session" --ok-label "Remove session" --title="Time has reached the end" --text="[Archive session] :\nWSP will encrypt and store the session, you can still acess it after from main menu.\nWarning : Do not forget to save and close all your files in the shown directory.\n\n[Remove] :\nWSP will securely remove the session."	
	then
		python /home/Secure_Working_Sessions/ressources/python/remove_session.py
		pgrep --full temp_tree.sh | xargs kill
	else
		python /home/Secure_Working_Sessions/ressources/python/archive_session.py
		pgrep --full temp_tree.sh | xargs kill
	fi
fi
