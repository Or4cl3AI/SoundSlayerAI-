import ffmpeg

def vocals(song_path):
    """
    This function removes vocals from a song using ffmpeg.
    """
    output_path = song_path.replace(".mp3", "_no_vocals.mp3")

    try:
        # Use ffmpeg to remove vocals
        ffmpeg.input(song_path).output(output_path, acodec='pcm_s16le', ac=1, vn=True).run()
    except Exception as e:
        print(f"Error removing vocals: {e}")
        return None

    return output_path
