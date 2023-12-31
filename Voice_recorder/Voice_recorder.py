import pyaudio
import wave

def record_audio(output_file, duration=5, sample_rate=44100, channels=2, chunk=1024):
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk
    )

    print("Recording...")

    frames = []

    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    duration = 5  # Set the duration of the recording (in seconds)
    record_audio(output_file, duration)
    print(f"Audio recorded and saved to {output_file}")