import re
import os
from eschaton import eschaton as esc
from eschaton_speak import words as esc_spk
import streamlit as st

# match characters in input string to dictionary
def translate(inputstr):
    chars = [*inputstr]
    newstr = [None]*len(chars)

    for i in range(0, len(chars)):
        compare = chars[i]
        charval = esc.get(f'{compare}',f'{compare}')
        newstr[i] = charval
    translation = ''.join(newstr)
    
    return translation

def speak(inputstr):

    words = inputstr.split()
    #chars = [*inputstr]
    newstr = [None]*len(words)

    for i in range(0, len(words)):
        compare = words[i]
        wordval = esc_spk.get(f'{compare}',f'{compare}')
        if (wordval == ','):
            newstr[i] = ','
        elif (wordval == '.'):
            newstr[i] = '.'
        elif (wordval == '...'):
            newstr[i] = '...'
        elif (wordval == '!'):
            newstr[i] = '!'
        elif (wordval == '?'):
            newstr[i] = '?'
        elif (wordval == compare):
            newstr[i] = 'KHA'
        else:
            newstr[i] = wordval
    translation = ' '.join(newstr)
    
    return translation
st.image("d20.jpg", use_container_width=True)
st.markdown("""
# Fred's Basic Eldritch Translator

This tool was designed to allow users to translate their own input strings into the Eldritch language of the Twin entities Heth Mivath.

#### INSTRUCTIONS FOR USE

Enter a string to translate in the box below.   

**This tool parses input text on a per character basis to produce its translations. Because of this methodology, please mind the following cautions:**
            
- Please **use lowercase only** and keep punctuation to a minimum.   
- Avoid contractions like "isn't" or "can't" - just write "is not" or "cannot"
- Any punctuation should be entered separately from words you wish to translate.  (like this: ' hello world ! how are you , friend ? '  ) 

Any spoken words that have no translation in the verbal codex will be translated with the placeholder term 'KHA'.  

This is implemented in order to enable relatively seamless readability when desired words are missing.

""")

st.header("Speak and they shall reply")

inputstr = st.text_input("Enter your English/Common text here:")
say = speak(inputstr)

st.markdown("### The spoken translation is:")
st.write(say or "...awaiting your words")

st.markdown("### The written translation is:")
st.write(translate(inputstr) or "...awaiting your words")

st.markdown("""

## About this tool
            
This translator is based on an extension of the Eschaton eldritch language created 
by Thunder Lotus Games for the 'Sundered' video game. It uses the same eldritch alphabet for 
written language, and a VERY loose method of pronunciation to allow a user to speak the 
language aloud. Some words follow written translations fairly closely, while many do not. 
This was done simply for ease of speech and to craft a more holistic and flavorful vocabulary. 

Have fun!  - Fred

*Developed in Streamlit for Python*            
""")