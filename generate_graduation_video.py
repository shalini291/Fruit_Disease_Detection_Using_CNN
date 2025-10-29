"""
Graduation Message Video Generator
Creates a beautiful video with text overlays and background music
"""

from moviepy.editor import (
    TextClip, CompositeVideoClip, ColorClip, 
    concatenate_videoclips, AudioFileClip
)
from moviepy.video.fx.all import fadein, fadeout
import textwrap

# The heartfelt graduation message
message_parts = [
    {
        "text": "Today marks the end of one beautiful chapter\nand the beginning of a new one. 🌸",
        "duration": 5
    },
    {
        "text": "To all my amazing friends from both A and B sections,\nI want to say thank you from the bottom of my heart\nfor showering me with your friendship, care,\nand all those unforgettable masalas of memories\nwe've shared together... 😊",
        "duration": 8
    },
    {
        "text": "From laughter to silly fights,\nfun, misunderstandings,\nand endless moments of togetherness...\nEach one of you has given me\nsomething to remember forever 💖",
        "duration": 7
    },
    {
        "text": "To all our teachers...\nto all sir's and ma'am,\nmy deepest gratitude to you all,\nespecially to all my dearest teachers\nwhom I love the most 🌺",
        "duration": 7
    },
    {
        "text": "Thank you for your constant support\nand encouragement throughout this MCA journey...\nYou all have been our source of guidance...\nWithout your care and motivation,\nreaching this milestone wouldn't have been possible 🙏",
        "duration": 8
    },
    {
        "text": "To all my dear friends,\nI sincerely wish each one of you\ngreat success, endless happiness,\nand the fulfillment of every dream\nyou've ever had... ❤️",
        "duration": 7
    },
    {
        "text": "May we all reach great heights,\nand may this bond we've built\nremain strong no matter\nwhere life takes us... 🌟",
        "duration": 6
    },
    {
        "text": "Congratulations to all of you\non your Graduation Day! 🎉\n\nEven though I'm not there to celebrate with you,\nI hope you all enjoy and have a wonderful time\nfilled with joy and beautiful memories... 💞",
        "duration": 8
    },
    {
        "text": "I know that I'm not someone special\nto be remembered,\nbut I've learned so many things\nfrom each and every one of you...\nlessons that I'll carry with me always 🌼",
        "duration": 7
    },
    {
        "text": "Let's promise to meet again in the future,\nwith the same smiles,\nthe same energy,\nand hearts full of memories... 💫",
        "duration": 6
    },
    {
        "text": "I know this message sounds a bit cliche 😅,\nbut it's written wholeheartedly\nwith pure love and gratitude... 💖\n\nHave a wonderful day, everyone! 😊",
        "duration": 7
    }
]

def create_text_clip(text, duration, size=(1920, 1080), fontsize=60, color='white', bg_color=(30, 60, 114)):
    """
    Create a text clip with background
    """
    # Create background
    background = ColorClip(size=size, color=bg_color, duration=duration)
    
    # Create text clip
    txt_clip = TextClip(
        text,
        fontsize=fontsize,
        color=color,
        font='Arial-Bold',
        method='caption',
        size=(size[0] - 200, None),
        align='center'
    ).set_duration(duration).set_position('center')
    
    # Apply fade in and fade out effects
    txt_clip = fadein(txt_clip, 0.5)
    txt_clip = fadeout(txt_clip, 0.5)
    
    # Composite text on background
    video = CompositeVideoClip([background, txt_clip])
    
    return video

def create_title_clip(duration=4, size=(1920, 1080)):
    """
    Create opening title clip
    """
    bg_color = (139, 0, 139)  # Purple
    background = ColorClip(size=size, color=bg_color, duration=duration)
    
    title_text = TextClip(
        "Graduation Day 2025\n🎓",
        fontsize=90,
        color='gold',
        font='Arial-Bold',
        method='caption',
        size=(size[0] - 200, None),
        align='center'
    ).set_duration(duration).set_position('center')
    
    title_text = fadein(title_text, 1)
    title_text = fadeout(title_text, 1)
    
    return CompositeVideoClip([background, title_text])

def create_ending_clip(duration=5, size=(1920, 1080)):
    """
    Create ending clip
    """
    bg_color = (139, 0, 139)  # Purple
    background = ColorClip(size=size, color=bg_color, duration=duration)
    
    ending_text = TextClip(
        "With Love & Best Wishes\n💖\n\nCongratulations Class of 2025!\n🎉🎓✨",
        fontsize=70,
        color='gold',
        font='Arial-Bold',
        method='caption',
        size=(size[0] - 200, None),
        align='center'
    ).set_duration(duration).set_position('center')
    
    ending_text = fadein(ending_text, 1)
    ending_text = fadeout(ending_text, 1)
    
    return CompositeVideoClip([background, ending_text])

def generate_video(output_filename='graduation_message.mp4'):
    """
    Generate the complete graduation video
    """
    print("🎬 Starting video generation...")
    
    # Create all clips
    clips = []
    
    # Add title
    print("Creating title clip...")
    clips.append(create_title_clip())
    
    # Add message parts with alternating background colors
    bg_colors = [
        (30, 60, 114),   # Dark blue
        (70, 130, 180),  # Steel blue
        (100, 149, 237), # Cornflower blue
        (65, 105, 225),  # Royal blue
    ]
    
    for i, part in enumerate(message_parts):
        print(f"Creating clip {i+1}/{len(message_parts)}...")
        bg_color = bg_colors[i % len(bg_colors)]
        clip = create_text_clip(
            part['text'], 
            part['duration'],
            bg_color=bg_color
        )
        clips.append(clip)
    
    # Add ending
    print("Creating ending clip...")
    clips.append(create_ending_clip())
    
    # Concatenate all clips
    print("Concatenating all clips...")
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Write the video file
    print(f"Writing video to {output_filename}...")
    final_video.write_videofile(
        output_filename,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True,
        preset='medium'
    )
    
    print(f"✅ Video successfully created: {output_filename}")
    print(f"📊 Total duration: {final_video.duration:.2f} seconds")
    
    return output_filename

if __name__ == "__main__":
    try:
        output_file = generate_video()
        print(f"\n🎉 Your graduation video is ready!")
        print(f"📁 Location: {output_file}")
        print(f"\nYou can now share this beautiful message with your friends! 💖")
    except Exception as e:
        print(f"❌ Error generating video: {str(e)}")
        print("\nMake sure you have moviepy installed:")
        print("pip install moviepy")
