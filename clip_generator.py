import os
import subprocess


# clip_length: Length of each clip in seconds.
def generate_clips(input_dir, output_dir, clip_length=90):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through files
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)

        # Skip if not a file
        if not os.path.isfile(input_path):
            continue

        # Checks extensions (add more if needed)
        valid_exts = (".mp4", ".mkv", ".mov", ".avi", ".mp3", ".wav", ".flac", ".m4a")
        if not file_name.lower().endswith(valid_exts):
            continue

        base_name, ext = os.path.splitext(file_name)
        output_path = os.path.join(output_dir, f"{base_name}_clip{ext}")

        # creates segment
        cmd = [
            "ffmpeg", "-y",  # overwrite
            "-i", input_path,
            "-t", str(clip_length),
            "-c", "copy",  # copy codec (fast, no re-encoding)
            output_path
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Created clip: {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {file_name}: {e.stderr.decode()}")

if __name__ == "__main__":
    input_dir = input("Enter path to A/V directory: ").strip()
    
    # create a new directory for the clips directory
    output_dir = input("Enter path to clips directory: ").strip()
    generate_clips(input_dir, output_dir)
