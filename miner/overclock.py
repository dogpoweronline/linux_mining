#!/usr/bin/python3

# import sys
import os
from subprocess import call


# settings
# fan=x%
#
# gpu_min=-200MHz
# gpu_max=1200Mhz
#
# gtx1050ti
# nvidia-settings -c :0 -q [gpu:0]/GPUGraphicsClockOffset[3]
# mem_min=-200MHz
# mem_max=1200MHz
#
# gtx1060
# nvidia-settings -c :0 -q [gpu:0]/GPUGraphicsClockOffset[3]
# mem_min=-2000MHz
# mem_max=2000MHz

# see: /etc/passwd
user_uid = 10000  # user
user_uid = 29999  # oem

gpu_list = [
    # gtx1060ti
    {'pl': '99', 'fan': '70', 'gpu': '-200', 'mem': '1900'},  # gpu 0

    # gtx1050ti
    # {'pl': '75', 'fan': '75', 'gpu': '-200', 'mem': '1500'},  # gpu 0
    # {'pl': '75', 'fan': '75', 'gpu': '-200', 'mem': '1500'},  # gpu 1
    # {'pl': '75', 'fan': '75', 'gpu': '-200', 'mem': '1500'},  # gpu 2
    # {'pl': '75', 'fan': '75', 'gpu': '-200', 'mem': '1500'},  # gpu 3
    # {'pl': '75', 'fan': '75', 'gpu': '-200', 'mem': '1500'},  # gpu 4

    # gtx1080ti
    # {'pl': '200', 'fan': '75', 'gpu': '0', 'mem': '700'},  # gpu 0

    # gtx1660ti_super
    # {'pl': '70', 'fan': '55', 'gpu': '0', 'mem': '800'},  # gpu 1
    # {'pl': '70', 'fan': '50', 'gpu': '0', 'mem': '9000'},  # gpu 2
]


number_of_gpu = len(gpu_list)

# nvidia-smi lower power-limits in XXXW
c = 0
for i in gpu_list:
    call(['nvidia-smi', '-i', '{}'.format(c), '-pl', i['pl']])
    c += 1


# nvidia-settings overclocking
os.environ['DISPLAY'] = ':0'
os.setreuid(user_uid, user_uid)

print('Display env: {}, uid: {}'.format(dict(os.environ)['DISPLAY'], os.getuid()))  # noqa

# call(['su', '-', 'user', '-c', 'DISPLAY=:0',])
# call(['export', '"DISPLAY=:0"',])
# nvidia-settings --query all
# nvidia-settings -c :0 -q [gpu:0]/GPUGraphicsClockOffset[3]


def nvidia_settings(arg):
    control_set = [
        'nvidia-settings',
        '-c',
        ':0',
        '-a',
        arg,
    ]
    print(' '.join(control_set))  # noqa
    call(control_set)


c = 0
for i in gpu_list:
    # '[gpu:0]/GPUOverclockingState=1',
    # '[gpu:0]/GPU2DClockFreqs=350,550',
    # '[gpu:0]/GPU3DClockFreqs=500,800',
    # FAN CONTROL
    # 'GPUFanControlState=1',
    # 'GPUTargetFanSpeed=90',
    # GPU
    # -200MHz 1200Mhz
    # 'GPUGraphicsClockOffset[3]=-200',
    # -2000MHz 2000Mhz
    # 'GPUMemoryTransferRateOffset[3]=1950',
    # nvidia-settings -c :0 -q [gpu:0]/GPUGraphicsClockOffset[2]
    if 'fan' in i:
        nvidia_settings('[gpu:%s]/GPUFanControlState=1' % (c))
        nvidia_settings('[fan:%s]/GPUTargetFanSpeed=%s' % (c, i['fan']))
    #
    if 'gpu' in i:
        nvidia_settings('[gpu:%s]/GPUGraphicsClockOffset[1]=%s' % (c, i['gpu']))
        nvidia_settings('[gpu:%s]/GPUGraphicsClockOffset[2]=%s' % (c, i['gpu']))
        nvidia_settings('[gpu:%s]/GPUGraphicsClockOffset[3]=%s' % (c, i['gpu']))
    #
    if 'mem' in i:
        nvidia_settings('[gpu:%s]/GPUMemoryTransferRateOffset[1]=%s' % (c, i['mem']))
        nvidia_settings('[gpu:%s]/GPUMemoryTransferRateOffset[2]=%s' % (c, i['mem']))
        nvidia_settings('[gpu:%s]/GPUMemoryTransferRateOffset[3]=%s' % (c, i['mem']))
    #
    c += 1

"""
nvidia-settings -c :0 -a [gpu:0]/GPUFanControlState=1
nvidia-settings -c :0 -a [fan:0]/GPUTargetFanSpeed=75
nvidia-settings -c :0 -a [gpu:0]/GPUGraphicsClockOffset[1]=-100
nvidia-settings -c :0 -a [gpu:0]/GPUGraphicsClockOffset[2]=-100
nvidia-settings -c :0 -a [gpu:0]/GPUGraphicsClockOffset[3]=-100
nvidia-settings -c :0 -a [gpu:0]/GPUMemoryTransferRateOffset[1]=700
nvidia-settings -c :0 -a [gpu:0]/GPUMemoryTransferRateOffset[2]=700
nvidia-settings -c :0 -a [gpu:0]/GPUMemoryTransferRateOffset[3]=700

nvidia-settings -c :0 -a [gpu:1]/GPUFanControlState=1
nvidia-settings -c :0 -a [fan:1]/GPUTargetFanSpeed=75
nvidia-settings -c :0 -a [gpu:1]/GPUGraphicsClockOffset[1]=-200
nvidia-settings -c :0 -a [gpu:1]/GPUGraphicsClockOffset[2]=-200
nvidia-settings -c :0 -a [gpu:1]/GPUGraphicsClockOffset[3]=-200
nvidia-settings -c :0 -a [gpu:1]/GPUMemoryTransferRateOffset[1]=300
nvidia-settings -c :0 -a [gpu:1]/GPUMemoryTransferRateOffset[2]=300
nvidia-settings -c :0 -a [gpu:1]/GPUMemoryTransferRateOffset[3]=300

nvidia-settings -c :0 -a [gpu:2]/GPUFanControlState=1
nvidia-settings -c :0 -a [fan:2]/GPUTargetFanSpeed=75
nvidia-settings -c :0 -a [gpu:2]/GPUGraphicsClockOffset[1]=-200
nvidia-settings -c :0 -a [gpu:2]/GPUGraphicsClockOffset[2]=-200
nvidia-settings -c :0 -a [gpu:2]/GPUGraphicsClockOffset[3]=-200
nvidia-settings -c :0 -a [gpu:2]/GPUMemoryTransferRateOffset[1]=300
nvidia-settings -c :0 -a [gpu:2]/GPUMemoryTransferRateOffset[2]=300
nvidia-settings -c :0 -a [gpu:2]/GPUMemoryTransferRateOffset[3]=300

nvidia-settings -c :0 -q [gpu:1]/GPUGraphicsClockOffset[3]
nvidia-settings -c :0 -q [gpu:1]/GPUMemoryTransferRateOffset[3]
"""
