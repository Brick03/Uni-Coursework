#!/bin/bash

read -p "---Please enter a username: " username

#cheacks if $user exits, if it does user is promted to enter another name 
while grep -q "$username" /etc/passwd 1>&2 ; do
  read -p "---That user already exits, please enter another name: " username
 # echo "-----$username------"
done

read -p "---Please enter the primary group of the user: " group
#cheacks if the group entered exists if not the user is asked if they want to make the group
#echo "--------- ${group} -------------"


if cat /etc/group | grep -q $group 1>&2 ; then
	#echo "---------TRUE---------"
	echo "---Group exists, adding to group ${group}"

else 
	echo "This group doesn't exists would you like to create one [Y/N]"
	read yn 
	
	case $yn in 
	
		y*) echo  "adding group ${group}"
			groupadd ${group}
			;;
		n*) read -p "---Please enter a group that exists " group
			;;	
	
	esac

fi


sudo useradd $username -g $group -m -e 2022-12-31 -s /bin/bash

echo "---Created user: $username, in the group: $group"

passwd $username







#sudo tail -n 1 /etc/passwd
#sudo tail -n 1 /etc/group
