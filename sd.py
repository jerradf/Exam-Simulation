# sd.py
# Jerrad Flores

# This is the file that detects the Sound
# Rather than identifying words, we are identifying sound waves
# Assuming the test-taker is in a quite room, if there is detection of a sound, trigger a warning

import pyaudio
import struct
import math


# The following are standard measurements utilized by sound engineers and many standard global requirements for audio recordings.
# These are the standards we are going to use for the microphone.
VOICE_THRESHOLD = 0.28
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 1
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)


def get_rms(block):
    # RMS amplitude is defined as the square root of the 
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into 
    # a string of 16-bit samples...

    # we will get one short out for each 
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)



class SoundDetector(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()


    def stop(self):
        self.stream.close()


    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index
        if device_index == None:
            print( "No preferred input found; using default input device." )
        return device_index


    def open_mic_stream(self):
        device_index = self.find_input_device()
        print(device_index)
        stream = self.pa.open(  format = FORMAT,
                                channels = CHANNELS,
                                rate = RATE,
                                input = True,
                                input_device_index = device_index,
                                frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream


    def detector(self):
        block = self.stream.read(INPUT_FRAMES_PER_BLOCK, exception_on_overflow = False)
        amplitude = get_rms(block)
        if amplitude > VOICE_THRESHOLD:
            return True
        else:
            return False
