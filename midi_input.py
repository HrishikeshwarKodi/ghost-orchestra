import mido
import time
from note_seq import NoteSequence

# ========== MIDI LISTENER FUNCTION ==========
def midi_input_to_note_sequence(port_name=None):
    """
    Continuously listens to MIDI input and builds a NoteSequence.
    Stops on KeyboardInterrupt.

    Args:
        port_name (str): Optional MIDI input port name. If None, uses default input.

    Returns:
        note_seq.NoteSequence with captured notes.
    """
    if port_name is None:
        inport = mido.open_input()
    else:
        inport = mido.open_input(port_name)

    sequence = NoteSequence()
    sequence.ticks_per_quarter = 220
    note_on_times = {}

    start_time = time.time()
    print(f"[Listener] Listening for MIDI input on port '{inport.name}' until stopped...")

    try:
        while True:
            for msg in inport.iter_pending():
                print(f"[Listener] Raw message: {msg}")

                current_time = time.time() - start_time

                if msg.type == 'note_on' and msg.velocity > 0:
                    note_on_times[msg.note] = current_time
                    print(f"[Listener] Note ON: {msg.note}, velocity: {msg.velocity}, time: {current_time:.2f}s")

                elif msg.type in ['note_off', 'note_on'] and msg.velocity == 0:
                    if msg.note in note_on_times:
                        start_note_time = note_on_times.pop(msg.note)
                        end_note_time = current_time

                        note = sequence.notes.add()
                        note.pitch = msg.note
                        note.velocity = msg.velocity if msg.velocity > 0 else 64
                        note.start_time = start_note_time
                        note.end_time = end_note_time
                        sequence.total_time = max(sequence.total_time, end_note_time)

                        print(f"[Listener] Note OFF: {msg.note}, time: {end_note_time:.2f}s")

            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n[Main] KeyboardInterrupt received, stopping...")
        inport.close()
        return sequence


# ========== VIRTUAL MIDI PLAYER (DEBUG TOOL) ==========
# def virtual_midi_chord_player(interval=1.0, chord_notes=[60, 64, 67], repeat=10):
#     """
#     Sends a triad chord to a virtual MIDI port repeatedly.
#     Only for debugging/testing the listener.
#     """
#     outport = mido.open_output('Virtual Output', virtual=True)
#     print("[Player] Virtual MIDI output port 'Virtual Output' created.")

#     try:
#         for i in range(repeat):
#             # Send chord on
#             for note in chord_notes:
#                 msg = mido.Message('note_on', note=note, velocity=64)
#                 outport.send(msg)
#             print("[Player] Sent chord ON")
#             time.sleep(0.5)

#             # Send chord off
#             for note in chord_notes:
#                 msg = mido.Message('note_off', note=note, velocity=0)
#                 outport.send(msg)
#             print("[Player] Sent chord OFF")
#             time.sleep(interval)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         outport.close()
#         print("[Player] Virtual MIDI output port closed.")


# ========== MAIN ==========
if __name__ == '__main__':
    # Uncomment to test sending fake chords to your listener
    # import threading
    # threading.Thread(target=virtual_midi_chord_player, daemon=True).start()

    sequence = midi_input_to_note_sequence()
    print(f"[Main] Final NoteSequence has {len(sequence.notes)} notes.")
