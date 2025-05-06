# Convert English text to speech
# DOCS: https://pypi.org/project/coqui-tts/
# pip install coqui-tts

from TTS.api import TTS

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# This is the model used to add voice to the text. 
# print(tts.speakers) # print for available models
model = 'Royston Min'

# This is Deepseek's response and poetic improvement to this prompt:
# For if we remove God from our lives, we remove all hope for objectivity. And if truth is subject to our own will, then it changes with it. 
# How do we then have truth, which is by definition unchanging? This is the madness of the modern man who has glorified his ego!
text  = """
Behold—the modern Babel!
Where we topple the altar of the Absolute,
and in its place erect a thousand mirrors,
each reflecting a different face of Truth,
each whispering: 'I am God now.'

What is truth, when it kneels to our passing whims?
What is reason, when it dances on the strings of desire?
We have sold the compass for the thrill of the storm,
and call our drowning 'enlightenment.'

O wretched architects of ruin!
We smash the scales of the Divine,
then wonder why justice is a shifting fog.
We silence the Voice that said 'I AM',
and now hear only echoes of our own hunger.
"""

# Export wav file: a little slow on CPU
tts.tts_to_file(
    text=text,
    speaker=model,
    language="en",
    file_path=f"{model}.wav"
)
