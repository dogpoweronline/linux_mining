#!/bin/bash

# Windows 10
#setx GPU_FORCE_64BIT_PTR 0
#setx GPU_MAX_HEAP_SIZE 100
#setx GPU_USE_SYNC_OBJECTS 1
#setx GPU_MAX_ALLOC_PERCENT 100
#setx GPU_SINGLE_ALLOC_PERCENT 100

/home/user/miner/claymore/ethdcrminer64 -epool us1.ethpool.org:3333 -ewal *ENTER_YOUR_ETH_WALLET_HERE* -epsw x -tt -85 -ttli 70 -tstop -83 -r 360

#-dpool stratum+tcp://dcr.suprnova.cc:3252 -dwal Redhex.my -dpsw x