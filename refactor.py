import re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace script loading
content = re.sub(
    r'<!-- js-synthesizer for proper drum support \(channel 9 percussion\) -->\s*<script.*?</script>\s*<script.*?</script>',
    r'<!-- Tone.js for high quality synthesis -->\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>',
    content,
    flags=re.DOTALL
)

# Overwrite functions using string replacement from a known start to known end
def replace_between(start_str, end_str, replacement):
    global content
    try:
        start_idx = content.index(start_str)
        end_idx = content.index(end_str, start_idx) + len(end_str)
        content = content[:start_idx] + replacement + content[end_idx:]
    except ValueError:
        print(f"Could not find section to replace: {start_str[:30]}...")

# 1. Variables
replace_between(
    'let jsSynthesizer = null;',
    'let jsSynthesizerReady = false;',
    'let toneReady = false;\n        let synths = {};'
)

# 2. initAudio
replace_between(
    'function initAudio() {',
    'audioContext = new (window.AudioContext || window.webkitAudioContext)();\n            }\n        }',
    '''function initAudio() {
            if (!toneReady && window.Tone) {
                Tone.start();
                toneReady = true;
            }
        }'''
)

# 3. initSoundfont
replace_between(
    'async function initSoundfont() {',
    'return true;\n        }',
    '''async function initSoundfont() {
            initAudio();
            try { await loadInstrument('piano'); } catch(e) {}
            return true;
        }'''
)

# 4. loadInstrument
replace_between(
    'async function loadInstrument(instrumentType) {',
    'return instrument;\n        }',
    '''async function loadInstrument(instrumentType) {
            initAudio();
            if (instrumentCache[instrumentType]) return instrumentCache[instrumentType];
            
            let synth;
            if (instrumentType.includes('synth') || instrumentType.includes('pad') || instrumentType.includes('lead')) {
                synth = new Tone.PolySynth(Tone.Synth, {
                    oscillator: { type: "sawtooth" },
                    envelope: { attack: 0.1, decay: 0.2, sustain: 0.5, release: 1.2 }
                }).toDestination();
            } else if (instrumentType.includes('bass')) {
                synth = new Tone.PolySynth(Tone.FMSynth).toDestination();
            } else if (instrumentType.includes('string') || instrumentType.includes('violin') || instrumentType.includes('cello')) {
                synth = new Tone.PolySynth(Tone.Synth, {
                    oscillator: { type: "triangle" },
                    envelope: { attack: 0.5, decay: 0.1, sustain: 0.8, release: 1.5 }
                }).toDestination();
            } else {
                synth = new Tone.PolySynth(Tone.Synth, {
                    oscillator: { type: "triangle8" },
                    envelope: { attack: 0.02, decay: 0.1, sustain: 0.3, release: 1 }
                }).toDestination();
            }
            
            synths[instrumentType] = synth;
            
            const instrument = {
                type: instrumentType,
                start: function(noteName, startTime, options = {}) {
                    const noteMatch = noteName.match(/([A-G])(#|b)?(\\d+)/);
                    if (!noteMatch) return;
                    const duration = options.duration || 0.5;
                    const velocity = options.gain || 0.8;
                    const t = Tone.now() + (startTime > 0 ? startTime : 0);
                    synth.triggerAttackRelease(noteName, duration, t, velocity);
                }
            };
            instrumentCache[instrumentType] = instrument;
            return instrument;
        }'''
)

# 5. loadDrumKit
replace_between(
    'async function loadDrumKit(soundfontName) {',
    'return null;\n            }\n        }',
    '''async function loadDrumKit(soundfontName) {
            initAudio();
            if (drumKitCache[soundfontName]) return drumKitCache[soundfontName];
            
            if (!synths.drum) {
                synths.drum = new Tone.MembraneSynth().toDestination();
                synths.hihat = new Tone.MetalSynth({
                    frequency: 200, envelope: { attack: 0.001, decay: 0.1, release: 0.01 },
                    harmonicity: 5.1, modulationIndex: 32, resonance: 4000, octaves: 1.5
                }).toDestination();
                synths.snare = new Tone.NoiseSynth({
                    noise: { type: 'white' }, envelope: { attack: 0.001, decay: 0.2, sustain: 0 }
                }).toDestination();
            }
            const drumKit = { loaded: true };
            drumKitCache[soundfontName] = drumKit;
            return drumKit;
        }'''
)

# 6. playDrumSoundFromSoundfont
replace_between(
    "async function playDrumSoundFromSoundfont(drumType, startTime = 0, soundfontName = 'FluidR3_GM') {",
    "console.error(`Error playing drum with js-synthesizer: ${error}`, error);\n            }\n        }",
    '''async function playDrumSoundFromSoundfont(drumType, startTime = 0, soundfontName = 'FluidR3_GM') {
            initAudio();
            if (!drumKitCache[soundfontName]) await loadDrumKit(soundfontName);
            
            const t = Tone.now() + (startTime > 0 ? startTime : 0);
            const velocity = 0.8;
            
            if (drumType === 'kick') synths.drum.triggerAttackRelease("C2", "8n", t, velocity);
            else if (drumType === 'snare') synths.snare.triggerAttackRelease("16n", t, velocity);
            else if (drumType === 'hihat') synths.hihat.triggerAttackRelease("32n", t, velocity, 0.5);
            else if (drumType === 'openhat') synths.hihat.triggerAttackRelease("8n", t, velocity, 0.8);
            else synths.drum.triggerAttackRelease("G2", "16n", t, velocity);
        }'''
)

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored src/index.html successfully!")
