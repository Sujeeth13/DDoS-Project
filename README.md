# DDoS-Project
# Modern methods of Detecting DDoS attacks in SDN
This repository consists of all the files related to the final project of the course CS3543: Computer Networks 2
## Contents
```
1. Introduction
2. Pre-requisite Installations
3. More about file structure
4. Project and Implementation
5. Developers / Team Members
```

## Introduction

In this project, we attempt to develop a prototype framework that efficiently detects DDoS intrusions in real time networks based on modern Deep Learning based methods. We also try to go one step further and explore certain existing implementations for preventing/mitigating certain kinds of DDoS attacks. Finally we also present a new idea (to the best of our knowledge) for converting resource-targeting DDoS attacks to bandwidth-targeting DDoS attacks, so that the prevention/mitigation procedures applied for bandwidth-targeting DDoS attacks can be applied to resource-targeting DDoS attacks as well.

## Pre-requisite Installations
Follow  the below commands on a terminal to install the required pre-requisites for the working of the code
```
sudo -s
apt remove python2
apt autoremove --purge
pip3 install ryu 
pip3 install eventlet==0.30.2
pip3 install tensorflow
pip3 install cicflowmeter

# To install Tshark follow the below set of commands
wget https://www.wireshark.org/download/src/wireshark-3.0.0.tar.xz -O /tmp/wireshark-3.0.0.tar.xz
tar -xvf /tmp/wireshark-3.0.0.tar.xz
cd /tmp/wireshark-3.0.0
sudo apt update && sudo apt dist-upgrade
sudo apt install cmake libglib2.0-dev libgcrypt20-dev flex yacc bison byacc \
  libpcap-dev qtbase5-dev libssh-dev libsystemd-dev qtmultimedia5-dev \
  libqt5svg5-dev qttools5-dev
cmake .
make
sudo make install

# To Install Hyenae, refer to their github repository
https://github.com/r-richter/hyenae

```
Refer to the below image for the steps of installation:
![Untitled presentation](https://user-images.githubusercontent.com/74396985/166516485-1e070697-763e-4b82-bd54-39be19bb8000.png)


## More about file structure
All the relevant code files can be found in the Code folder
All the latex files used to make report can be found in Latex_files folder

## Project and Implementation


Refer to the Project report regarding the implementation and results

## Developers / Team Members

1. <a href = "https://github.com/Sujeeth13"> <b>Bhavanam Sujeeth Kumar Reddy | ES19BTECH11022</b> </a> <br>
2. <a href = "https://github.com/G-Sidhardha"> <b>Grandhi Sai Sidhardha | CS19BTECH11050</b> </a> <br>
3. <a href = "https://github.com/KrishnKher"> <b>Krishn Vishwas Kher | ES19BTECH11015</b> </a> <br>
4. <a href = "https://github.com/chandra3000"> <b>Mukkavalli Bharat Chandra | ES19BTECH11016</b> </a> <br>
5. <a href = "https://github.com/Akhil06042002"> <b>Mylavarapu Sri Akhil | ES19BTECH11014</b> </a> <br>
