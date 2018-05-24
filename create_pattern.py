import numpy as np

data = np.load("int_to_note.npz")
keys = data['keys']
values = data['values']

int_to_note = dict(zip(keys, values))

def createPattern(input_sequence):
    prediction_output = []

    # generate notes
    for note_index in input_sequence:

        result = int_to_note[note_index]
        prediction_output.append(result)
    return prediction_output
