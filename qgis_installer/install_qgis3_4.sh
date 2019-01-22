#!/bin/bash

#Site com tutorial 
#https://qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu

Usage() {
#----------------------USAGE:---------------------------------------------------------

#./install_qgis.sh  
	echo "-------USAGE------ "
	echo "# use no parameters to run this script: "
	echo "# this Script only works for Ubuntu versions"
	echo "#./install_qgis3_4.sh"
	echo " "

#----------------------------------------------------------------------------------
}

if [ $# -gt 0 ]
then
	Usage
	exit 1
fi

#nome do repositorio 
repository="https://qgis.org/debian"

QGIS_version="3.4 Madeira"

qgis_path=$(command -v qgis)

#checa se qgis ja esta instalado e pergunta se quer instalar em cima dessa versao atual

if [ -n "$qgis_path"  ]
then
	echo "------------------------------------------------"
	echo "QGIS is already installed,do you want to install QGIS ${QGIS_version} over it?"
	read -p "[y/n]: " answer

	while [ "${answer,,}" != "y" ]&&[ "${answer,,}" != "n" ]; 
	do
		echo "Answer either 'y' for yes and 'n' for no"
		read -p "[y/n]: " answer
	done
	
	if [ "${answer,,}" == 'n' ]
	then
		echo "QGIS ${QGIS_version} will not be installed"
		exit 0
	elif [ "${answer,,}" == 'y' ]
	then
		echo "------------------------------------"
		echo "Purging old version of QGIS     ...   "
		echo "-----------------------------------"
		sudo apt purge qgis* python-qgis* --auto-remove 
	fi
fi

#obtem versao e codename do ubuntu
codename=$(lsb_release --codename | grep "Codename")
codename=${codename:9}

if [ $codename = "bionic" ] 
then
	version="Ubuntu 18.04"
elif [ $codename = "xenial" ]
then
	version="Ubuntu 16.04"	
elif [ $codename = "artful" ]
then
	version="Ubuntu 17.10"
elif [ $codename = "trusty" ]
then
	version="Ubuntu 14.04"
else
	Usage
	exit 1
fi

echo "----------------------------------------"
echo "Version and codename of OS:"
echo $version
echo $codename
echo "----------------------------------------"

line1="deb $repository $codename main"
line2="deb-src $repository $codename main"

#checa se ja nao existem essas linhas 
if ! grep -Fxq "$line1" /etc/apt/sources.list 
then
	echo "$line1" | sudo tee -a /etc/apt/sources.list
fi

if ! grep -Fxq "$line2" /etc/apt/sources.list 
then
	echo "$line2" | sudo tee -a /etc/apt/sources.list
fi

#download de chaves
wget -O - https://qgis.org/downloads/qgis-2017.gpg.key | gpg --import
gpg --fingerprint CAEB3DC3BDF7FB45
gpg --export --armor CAEB3DC3BDF7FB45 | sudo apt-key add -

#agora eh possivel instalar com sucesso
sudo apt-get update
sudo apt-get install qgis python-qgis qgis-plugin-grass

