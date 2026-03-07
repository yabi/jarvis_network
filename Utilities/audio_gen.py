import math
import struct
import wave


def generate_beep(filename="input/sample.wav", duration=2.0):
    sample_rate = 44100
    frequency = 440.0
    n_samples = int(sample_rate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for i in range(n_samples):
            value = int(32767.0 * math.sin(2.0 * math.pi * frequency * i / sample_rate))
            data = struct.pack('<h', value)
            wav_file.writeframes(data)
    print(f"Generated sample audio: {filename}")


if __name__ == "__main__":
    generate_beep()
