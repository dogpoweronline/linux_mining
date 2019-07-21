#!/usr/bin/python3

# import sys
import os
from subprocess import call


# settings
# fan=x%
# gpu_min=-200MHz
# gpu_max=1200Mhz
# mem_min=-2000MHz
# mem_max=2000MHz


gpu_list = [
    # gtx1060
    {'fan': '70', 'gpu': '-200', 'mem': '1900'},  # gpu 0
    # gtx1050ti
    # {'fan': '67', 'gpu': '-200', 'mem': '1950'},  # gpu 0
    # {'fan': '67', 'gpu': '-200', 'mem': '1950'},  # gpu 1
    # {'fan': '67', 'gpu': '-200', 'mem': '1950'},  # gpu 2
    # {'fan': '67', 'gpu': '-200', 'mem': '1950'},  # gpu 3
    # {'fan': '67', 'gpu': '-200', 'mem': '1950'},  # gpu 4
]


number_of_gpu = len(gpu_list)

# nvidia-smi lower power-limits in 100W
c = 0
for n in gpu_list:
    call(['nvidia-smi', '-i', '%s' % (c), '-pl', '99'])
    c += 1


# nvidia-settings overclocking
os.environ['DISPLAY'] = ':0'
os.setreuid(1000, 1000)

print('Display env: %s, uid: %s' % (dict(os.environ)['DISPLAY'], os.getuid()))

# call(['su', '-', 'user', '-c', 'DISPLAY=:0',])
# call(['export', '"DISPLAY=:0"',])
# nvidia-settings --query all


def nvidia_settings(arg):
    control_set = [
        'nvidia-settings',
        '-c',
        ':0',
        '-a',
        arg,
    ]
    print(' '.join(control_set))
    call(control_set)


c = 0
for i in gpu_list:
    # '[gpu:0]/GPUOverclockingState=1',
    # '[gpu:0]/GPU2DClockFreqs=350,550',
    # '[gpu:0]/GPU3DClockFreqs=500,800',
    # fan control
    # 'GPUFanControlState=1',
    # 'GPUTargetFanSpeed=90',
    # -200MHz 1200Mhz
    # 'GPUGraphicsClockOffset[3]=-200',
    # -2000MHz 2000Mhz
    # 'GPUMemoryTransferRateOffset[3]=1950',
    #
    if 'fan' in i:
        nvidia_settings('[gpu:%s]/GPUFanControlState=1' % (c))
        nvidia_settings('[fan:%s]/GPUTargetFanSpeed=%s' % (c, i['fan']))
    #
    if 'gpu' in i:
        nvidia_settings('[gpu:%s]/GPUGraphicsClockOffset[3]=%s' % (c, i['gpu']))
    #
    if 'mem' in i:
        nvidia_settings('[gpu:%s]/GPUMemoryTransferRateOffset[3]=%s' % (c, i['mem']))
    #
    c += 1
