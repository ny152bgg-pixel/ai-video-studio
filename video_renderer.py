from moviepy.editor import *
from ai_image import generate_image

def render_video(script):
    clips = []

    for i, line in enumerate(script):
        img_path = generate_image(line, i)
        clip = (
            ImageClip(img_path)
            .set_duration(3)
            .fadein(0.3)
            .fadeout(0.3)
        )
        clips.append(clip)

    final = concatenate_videoclips(clips)
    path = "output/final.mp4"

    final.write_videofile(path, fps=24, audio=False)
    return path
