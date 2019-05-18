#!/bin/bash
(
echo "0" ; sleep 0.5
echo "# Work in progress 0%"; sleep 0.5
echo "1" ; sleep 0.5
echo "# Work in progress 1%"; sleep 0.5
echo "3" ; sleep 0.5
echo "# Work in progress 3%"; sleep 0.5
echo "5" ; sleep 0.5
echo "# Work in progress 5%"; sleep 0.5
echo "6" ; sleep 0.5
echo "# Work in progress 6%"; sleep 0.5
echo "8" ; sleep 0.5
echo "# Work in progress 8%"; sleep 0.5
echo "10" ; sleep 0.5
echo "# Work in progress 10%"; sleep 0.5
echo "11" ; sleep 0.5
echo "# Work in progress 11%"; sleep 0.5
echo "13" ; sleep 0.5
echo "# Work in progress 13%"; sleep 0.5
echo "15" ; sleep 0.5
echo "# Work in progress 15%"; sleep 0.5
echo "16" ; sleep 0.5
echo "# Work in progress 16%"; sleep 0.5
echo "18" ; sleep 0.5
echo "# Work in progress 18%"; sleep 0.5
echo "20" ; sleep 0.5
echo "# Work in progress 20%"; sleep 0.5
echo "21" ; sleep 0.5
echo "# Work in progress 21%"; sleep 0.5
echo "23" ; sleep 0.5
echo "# Work in progress 23%"; sleep 0.5
echo "25" ; sleep 0.5
echo "# Work in progress 25%"; sleep 0.5
echo "26" ; sleep 0.5
echo "# Work in progress 26%"; sleep 0.5
echo "28" ; sleep 0.5
echo "# Work in progress 28%"; sleep 0.5
echo "30" ; sleep 0.5
echo "# Work in progress 30%"; sleep 0.5
echo "31" ; sleep 0.5
echo "# Work in progress 31%"; sleep 0.5
echo "33" ; sleep 0.5
echo "# Work in progress 33%"; sleep 0.5
echo "35" ; sleep 0.5
echo "# Work in progress 35%"; sleep 0.5
echo "36" ; sleep 0.5
echo "# Work in progress 36%"; sleep 0.5
echo "38" ; sleep 0.5
echo "# Work in progress 38%"; sleep 0.5
echo "40" ; sleep 0.5
echo "# Work in progress 40%"; sleep 0.5
echo "41" ; sleep 0.5
echo "# Work in progress 41%"; sleep 0.5
echo "43" ; sleep 0.5
echo "# Work in progress 43%"; sleep 0.5
echo "45" ; sleep 0.5
echo "# Work in progress 45%"; sleep 0.5
echo "46" ; sleep 0.5
echo "# Work in progress 46%"; sleep 0.5
echo "48" ; sleep 0.5
echo "# Work in progress 48%"; sleep 0.5
echo "50" ; sleep 0.5
echo "# Work in progress 50%"; sleep 0.5
echo "51" ; sleep 0.5
echo "# Work in progress 51%"; sleep 0.5
echo "53" ; sleep 0.5
echo "# Work in progress 53%"; sleep 0.5
echo "55" ; sleep 0.5
echo "# Work in progress 55%"; sleep 0.5
echo "56" ; sleep 0.5
echo "# Work in progress 56%"; sleep 0.5
echo "58" ; sleep 0.5
echo "# Work in progress 58%"; sleep 0.5
echo "60" ; sleep 0.5
echo "# Work in progress 60%"; sleep 0.5
echo "61" ; sleep 0.5
echo "# Work in progress 61%"; sleep 0.5
echo "63" ; sleep 0.5
echo "# Work in progress 63%"; sleep 0.5
echo "65" ; sleep 0.5
echo "# Work in progress 65%"; sleep 0.5
echo "66" ; sleep 0.5
echo "# Work in progress 66%"; sleep 0.5
echo "68" ; sleep 0.5
echo "# Work in progress 68%"; sleep 0.5
echo "70" ; sleep 0.5
echo "# Work in progress 70%"; sleep 0.5
echo "71" ; sleep 0.5
echo "# Work in progress 71%"; sleep 0.5
echo "73" ; sleep 0.5
echo "# Work in progress 73%"; sleep 0.5
echo "75" ; sleep 0.5
echo "# Work in progress 75%"; sleep 0.5
echo "76" ; sleep 0.5
echo "# Work in progress 76%"; sleep 0.5
echo "78" ; sleep 0.5
echo "# Work in progress 78%"; sleep 0.5
echo "80" ; sleep 0.5
echo "# Work in progress 80%"; sleep 0.5
echo "81" ; sleep 0.5
echo "# Work in progress 81%"; sleep 0.5
echo "83" ; sleep 0.5
echo "# Work in progress 83%"; sleep 0.5
echo "85" ; sleep 0.5
echo "# Work in progress 85%"; sleep 0.5
echo "86" ; sleep 0.5
echo "# Work in progress 86%"; sleep 0.5
echo "88" ; sleep 0.5
echo "# Work in progress 88%"; sleep 0.5
echo "90" ; sleep 0.5
echo "# Work in progress 90%"; sleep 0.5
echo "91" ; sleep 0.5
echo "# Work in progress 91%"; sleep 0.5
echo "93" ; sleep 0.5
echo "# Work in progress 93%"; sleep 0.5
echo "95" ; sleep 0.5
echo "# Work in progress 95%"; sleep 0.5
echo "96" ; sleep 0.5
echo "# Work in progress 96%"; sleep 0.5
echo "98" ; sleep 0.5
echo "# Work in progress 98%"; sleep 0.5
echo "100" ; sleep 0.5
echo "# Work should now be completed 100%"
) |
zenity --progress --no-cancel --time-remaining --title "Current sequence : [test"] --width=600 --height=20 | python /home/Secure_Working_Sessions/ressources/python/notification.py