#!/bin/bash

# apt install -t smartmontools

smartctl -a /dev/nvme0n1 | grep Temperature
