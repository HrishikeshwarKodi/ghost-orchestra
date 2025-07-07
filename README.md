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

			┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
			│ Piano MIDI │    │ Harmonium  │    │ Tabla Beat │    │ Vocal Pitch│
			└────┬───────┘    └────┬───────┘    └────┬───────┘    └────┬───────┘
			     ▼                 ▼                 ▼                 ▼
			 ┌─────────┐       ┌─────────┐       ┌─────────┐       ┌─────────┐
			 │RNN-Piano│       │RNN-Harm │       │RNN-Tbl  │       │RNN-Voice│
			 └────┬───▲┘       └────┬───▲┘       └────┬───▲┘       └────┬───▲┘
			      │   │             │   │             │   │             │   │
			      ▼   │             ▼   │             ▼   │             ▼   │
			      └───┴──────┬──────────┴─────────────┴───┴─────────────┴───┘
					 ▼
			       ┌────────────────────┐
			       │ Music Transformer  │
			       │  (orchestration)   │
			       └────────────────────┘
					 ▼
			       ┌────────────────────┐
			       │ Multi-track MIDI   │──▶ Synth or DAW
			       └────────────────────┘


    
[README W.I.P]

look but don't touch
