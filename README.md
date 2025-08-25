# A/V Clip Generator

This Python script generates **90-second clips** (or custom length) from all audio and video files in a given directory.  
It uses [FFmpeg](https://ffmpeg.org/) to quickly trim media files **without re-encoding**, preserving original quality.  

## Features
- Works with both **audio** and **video** formats  
- Supports common file types: `.mp4`, `.mkv`, `.mov`, `.avi`, `.mp3`, `.wav`, `.flac`, `.m4a`  
- Creates a new output directory for clips  
- Fast operation using `-c copy` (no re-encoding)  

## Requirements
- Python 3.7+  
- [FFmpeg](https://ffmpeg.org/download.html) installed and available in your system’s PATH  

### Install FFmpeg
- **Windows:** Download binaries from [FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/) and add the `bin` folder to your PATH  
- **macOS (Homebrew):**
  ```bash
  brew install ffmpeg
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install ffmpeg


### Usage

1. Save the script as clip_generator.py

2. Run it in a terminal:
`python clip_generator.py`
3. Enter:

`The path to the input directory containing your audio/video files
The path to the output directory where clips will be saved`




### Custom Clip Length

By default, each clip is 90 seconds long.
To change this, edit the function call in the script: `generate_clips(input_dir, output_dir, clip_length=120)  # 120 seconds`



### Notes

Files shorter than the requested clip length will simply be copied in full
Unsupported file extensions will be skipped silently
Errors (e.g., corrupted files) will be printed in the console
