# mfcc.py
# Compute MFCCs of a given WAV file
# Author: Adam Mitchell
# Email:  adamstuartmitchell@gmail.com

import numpy
from scipy.io.wavfile import read


def open_file(f):
    '''
    return sampling frequency (fs) and time series data (data) of .wav file (f)
    '''
    fs, data = read(f)

    return fs, data


def frame_data(data, fs, length=0.025, shift=0.010):
    '''
    return array of arrays where each array is a framed segment of data (data)
    length of frames is given as sampling frequency (fs) * length (in ms)
    shift between frames is given as sampling frequency (fs) * shift (in ms)
    '''
    length = int(round(fs * length))
    shift = int(round(fs * shift))
    frames = list()

    for i in range(0, len(data), shift):
        frame = data[i:i+length]

        if len(frame) != length:
            frame = numpy.append(frame, [0] * (length-len(frame)))

        frames.append(frame)

    return length, numpy.array(frames)


def window_frame(frames, length):
    '''
    return array of arrays where each array is a frame within frames (frames) with
    a hamming window function applied
    length of hamming window is equivalent to the frame lengths (should be uniform)
    '''
    window = numpy.hamming(length)
    windowed_frames = list()

    for frame in frames:
        windowed_frame = list()

        for idx, sample in enumerate(frame):
            windowed_frame.append(sample * window[idx])

        windowed_frames.append(windowed_frame)

    return numpy.array(windowed_frames)










if __name__ == '__main__':
    fs, data = open_file('wavs/one-adam-1.wav')
    framelength, frames = frame_data(data, fs)
    window_frame(frames, framelength)
