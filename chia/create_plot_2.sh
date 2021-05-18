#!/bin/bash

tmux new-session -s create_plot_2 '/bin/bash chia plots create -k 32 -n 3 -t /home/chia/xch_hot -2 /home/chia/xch_hot -d /home/chia/xch_cold_1'
