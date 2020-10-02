#!/bin/bash

# Non-SSL connection: asia1 eu1 us1 us2
# /home/user/miner/ethminer/bin/ethminer -P stratum1+tcp://0xE8068577d46A1028f5f0D289f9df4fbcC7A06ff7.walter@us1.ethermine.org:4444

# SSL connection: asia1 eu1 us1 us2
/home/user/miner/ethminer/bin/ethminer \
-P stratum1+ssl://0xE8068577d46A1028f5f0D289f9df4fbcC7A06ff7.walter@asia1.ethermine.org:5555 \
--HWMON 1 \
--tstart 65 --tstop 85 \
--display-interval 2 \
