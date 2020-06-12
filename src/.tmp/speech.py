from gtts import gTTS
from io import BytesIO as bio
import os
import audio

txt = "Global warming is the long-term rise in the average temperature of the Earth’s climate system"
language = 'en'

mach = bio()
ob = gTTS(txt, 'en')
ob.wr