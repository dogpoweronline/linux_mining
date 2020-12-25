#!/bin/bash

# Non-SSL connection: asia1 eu1 us1 us2
# /home/user/miner/ethminer/bin/ethminer -P stratum1+tcp://0x892070E6B885F1B32b0405C91ba68309e769F6Ea.1060@us1.ethermine.org:4444

# SSL connection: asia1 eu1 us1 us2
/home/user/miner/ethminer/bin/ethminer \
-P stratum1+ssl://0x892070E6B885F1B32b0405C91ba68309e769F6Ea.1060@asia1.ethermine.org:5555 \
--HWMON 1 \
--tstart 65 --tstop 85 \
--display-interval 2 \
