import re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace jsSynthesizerReady checks in playSelectedTrack and exportAudio
content = content.replace(
    'if (!jsSynthesizerReady) {',
    'if (!toneReady) {'
)
content = content.replace(
    'await initFluidSynth();',
    'initAudio();'
)
content = content.replace(
    'jsSynthesizerReady = false;',
    ''
)
content = content.replace(
    'jsSynthesizerReady = true;',
    ''
)

# Replace the scanSoundfonts and checkLocalSf2 calls and definitions if any exist
content = re.sub(r'async function checkLocalSf2\(\) \{.*?return false;\s*\}', 'async function checkLocalSf2() { return false; }', content, flags=re.DOTALL)
content = re.sub(r'async function scanSoundfonts\(\) \{.*?return soundfonts;\s*\}', 'async function scanSoundfonts() { return ["ToneJS"]; }', content, flags=re.DOTALL)
content = re.sub(r'async function loadSoundfontIntoFluidSynth.*?(?=async function playDrumSoundFromSoundfont)', '', content, flags=re.DOTALL)

# In exportAudio, the Tone.js offline context is different.
# Let's just fix the alert and initialization for now so it doesn't crash on jsSynthesizerReady
content = content.replace(
    "alert('Rendering audio with SoundFont quality... This may take a moment.');",
    "alert('Rendering audio with Tone.js quality... This may take a moment.');"
)

# For the Tone.start() issue: 
# "The AudioContext is 'suspended'. Invoke Tone.start() from a user action to start the audio."
# We should wrap Tone.start() in a try-catch, but it's already only called in initAudio. 
# We can just change initAudio() to:
# function initAudio() { if (!toneReady && window.Tone) { try { Tone.start(); toneReady = true; } catch(e) {} } }
content = content.replace(
    'Tone.start();\n                toneReady = true;',
    'try { Tone.start(); toneReady = true; } catch(e) {}'
)

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed jsSynthesizerReady and .sf2 references")
