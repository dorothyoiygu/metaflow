import pyaudio
import wave
import os

class MetaFlow:
    def __init__(self, filename="output.wav"):
        self.filename = filename
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.rate = 44100  # Record at 44100 samples per second
        self.p = pyaudio.PyAudio()

    def record(self, duration=5):
        print("Recording...")
        stream = self.p.open(format=self.format,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.chunk)

        frames = []

        for i in range(0, int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    def play(self):
        wf = wave.open(self.filename, 'rb')

        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                             channels=wf.getnchannels(),
                             rate=wf.getframerate(),
                             output=True)

        data = wf.readframes(self.chunk)

        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)

        stream.stop_stream()
        stream.close()

    def edit(self, new_filename):
        print(f"Renaming file to {new_filename}")
        os.rename(self.filename, new_filename)
        self.filename = new_filename
        
    def save(self, path="."):
        if not os.path.exists(path):
            os.makedirs(path)
        new_path = os.path.join(path, self.filename)
        os.rename(self.filename, new_path)
        print(f"File saved to {new_path}")

    def close(self):
        self.p.terminate()

if __name__ == "__main__":
    metaflow = MetaFlow()
    metaflow.record(duration=5)  # Record for 5 seconds
    metaflow.play()              # Playback the recording
    metaflow.edit("edited_output.wav")  # Rename the file
    metaflow.save("saved_files") # Save to a directory
    metaflow.close()