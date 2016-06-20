#!/bin/bash
# www.makerbrasiltv.com.br


clear
echo "Instalador RPi.GPIO";
sleep 1;
echo "MakerBrasilTv - www.makerrasiltv.com.br";
sleep 5;
clear

if [ "$(id -u)" != "0" ]; then
echo "This script must be run as root." 1>&2
   exit 1
else

  echo "Baixando RPi GPIO..."
  sleep 2;
  wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.6.tar.gz
  
  clear

  echo "Descompactando... =-)"
  sleep 2
  tar zxvf RPi.GPIO-0.5.6.tar.gz

  cd RPi.GPIO-0.5.6

  echo "Editando arquivo INSTALL para voce ver o que irei fazer"
  sleep 3
  cat INSTALL.txt

  sleep 5
  echo "Continuando... =-)" 

  sleep 2
  echo "Atualizando sistema!"
  sleep 2

  sudo apt-get update 
  clear
  echo "Upgrade no sistema..."
  sleep 2

  sudo apt-get dist-upgrade
  
  clear

  echo "Instalando python-rpi.gpio e python3-rpi.gpio" 
  sleep 3

  
  sudo apt-get install python-rpi.gpio python3-rpi.gpio -y

  clear
  
  echo "Mais instalacao..."
 
  sleep 3
  clear

  sudo apt-get install python-dev python3-dev -y

  sudo python3 setup.py install  

  clear
  echo "Instalacao completa."
  sleep 5
  clear

  echo "Divirta-se"

fi
