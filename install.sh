#!/bin/bash

#
apt-get update

#ssh
apt-get install -y openssh-server
systemctl enable ssh

#
apt-get install -y mc tmux git x11vnc

#openvpn
apt-get install -y openvpn
systemctl enable openvpn

