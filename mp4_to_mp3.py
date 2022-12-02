from moviepy.editor import *

def mp4_to_mp3(mp4, mp3):     
    mp4_without_frames = AudioFileClip(mp4)     
    mp4_without_frames.write_audiofile(mp3)     
    mp4_without_frames.close()
    
mp4_to_mp3("Lewis Capaldi - Forget Me (Official Lyric Video).mp4", "Forget me.mp3")