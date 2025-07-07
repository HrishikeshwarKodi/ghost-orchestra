# ***Ghost Orchestra***
A semi-personal project that uses AI* to dynamically generate supporting and background instrumentals

              [MIDI Input from instrument]
                          ↓
                    [Trained AI]
                          ↓
          [Generated Accompaniment from AI]
                          ↓
    [Accompaniment is played along with the actual]

AI is going to be run locally*


Current plan:

    ┌────────────┐      ┌────────────────┐
    │  MIDI IN   │────▶│ Input Listener  │
    └────────────┘      └────────────────┘
                             │
                  ┌──────────┴────────────┐
                  ▼                       ▼
       ┌────────────────┐      ┌────────────────────┐
       │ Performance RNN│      │ Music Transformer  │
       └────────────────┘      └────────────────────┘
                  │                       │
                  └──────────┬────────────┘
                             ▼
                      ┌────────────┐
                      │ MIDI OUT   │───▶ Fluidsynth / DAW
                      └────────────┘

    
[README W.I.P]

look but don't touch
