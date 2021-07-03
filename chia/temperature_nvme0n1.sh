#!/bin/bash

# apt install -t smartmontools

smartctl -a /dev/nvme0n1 | grep Temperature

read -n 1 -s -r -p "Press any key to continue"
