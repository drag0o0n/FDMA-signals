import matplotlib.pyplot as plt
import numpy as np
import random
import scipy
import wave
import struct
import pylab
import pdb
from scipy.io import wavfile
WaveFile = 'C:\Users\DRAGON\Desktop\DBZU\21-22-2nd\communication\FDMAMixedAudio1.wav'

rate, data = WaveData.read(WaveFile)
# reading the info from the wavwfile (.wav) save it to WaveData
if len(data.shape) > 1:
    data = data[:, 0]
print(data)
