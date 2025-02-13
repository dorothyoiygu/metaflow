# MetaFlow

MetaFlow is a simple Python tool that allows users to record, edit, and save audio directly on Windows. This program leverages the `pyaudio` library for audio processing and provides basic functionalities for handling audio files.

## Features

- **Record Audio**: Capture audio from your microphone for a specified duration.
- **Play Audio**: Playback the recorded audio.
- **Edit Audio**: Rename the recorded audio file.
- **Save Audio**: Save the audio file to a specified directory.

## Requirements

- Python 3.x
- `pyaudio` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/metaflow.git
    cd metaflow
    ```

2. Install the required dependencies:

    ```bash
    pip install pyaudio
    ```

## Usage

1. Run the `metaflow.py` script:

    ```bash
    python metaflow.py
    ```

2. The script will record audio for 5 seconds, play it back, rename the file to `edited_output.wav`, and then save it in the `saved_files` directory.

## Notes

- Ensure your microphone is connected and working properly.
- You can modify the recording duration and file names by editing the parameters in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Developed using the [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) library.