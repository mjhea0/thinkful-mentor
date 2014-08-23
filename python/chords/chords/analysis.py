from __future__ import division

import math

import numpy
import librosa
import scipy.spatial.distance
import scipy.signal

CHORDS = numpy.array([
    [1,0,0,0,1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,1,0,0,0,0],
    [0,1,0,0,0,1,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,1,0,0,1,0,0],
    [0,0,1,0,0,1,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,1,0,0,1,0],
    [0,0,0,1,0,0,1,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,1,0,0,1],
    [0,0,0,0,1,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0],
    [1,0,0,0,0,1,0,0,1,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,1,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,1],
    [0,0,1,0,0,0,0,1,0,0,1,0],
    [1,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,0,1],
    [0,1,0,0,1,0,0,0,0,1,0,0],
    [1,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,1,0,0,0,0,1,0],
    [0,1,0,0,0,1,0,0,0,0,1,0],
    [0,0,0,1,0,0,1,0,0,0,0,1],
    [0,0,1,0,0,0,1,0,0,0,0,1]
])

CHORD_NAMES = numpy.array([#"A", "Am",
               #"A#", "A#m",
               #"B", "Bm",
               "C", "Cm",
               "C#", "C#m",
               "D", "Dm",
               "D#", "D#m",
               "E", "Em",
               "F", "Fm",
               "F#", "F#m",
               "G", "Gm",
               "G#", "G#m",
               "A", "Am",
               "A#", "A#m",
               "B", "Bm"])

def analyse(filename, resample_to=2756, bt_hop_length=128,
            chroma_hop_length=512, chroma_n_fft=1024):
    samples, sampleRate = librosa.load(filename)
    length = float(len(samples))/sampleRate
    if resample_to:
        samples = librosa.resample(samples, sampleRate, resample_to)
        sampleRate = resample_to
    newSampleRate = 2756
    samples = librosa.resample(samples, sampleRate, newSampleRate)
    sampleRate = newSampleRate
    tempo, beats = librosa.beat.beat_track(samples, sampleRate,
                                           hop_length=bt_hop_length)
    beat_times = librosa.frames_to_time(beats, sampleRate,
                                        hop_length=bt_hop_length)
    chromagram = librosa.feature.chromagram(samples, sampleRate,
                                            hop_length=chroma_hop_length,
                                            n_fft=chroma_n_fft)
    chromagram = numpy.transpose(chromagram)
    distances = scipy.spatial.distance.cdist(chromagram, CHORDS, "cosine")
    chords = distances.argmin(axis=1)
    chords = scipy.signal.medfilt(chords, 11)
    chord_frames = numpy.array(numpy.where(numpy.diff(chords) != 0))
    chords = chords[chord_frames][0].astype(int)
    chord_times = librosa.frames_to_time(chord_frames, sampleRate,
                                         hop_length=chroma_hop_length,
                                         n_fft=chroma_n_fft)[0]
    chord_names = CHORD_NAMES[chords]
    return {"beats": list(beat_times),
            "chords": [{"chord": chord_name, "time": chord_time} for chord_name, chord_time in zip(chord_names, chord_times)],
            "tempo": tempo}

