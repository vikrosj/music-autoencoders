# music-autoencoders

This page contains two small autoencoders for MIDI files. 
They are made as an example of how one can train neural network to autoencode MIDI files.

This is a part of a larger project, where the goal is to produce a variational autoencoder to generate new MIDI music.

The MIDI files can be read and written with the [music 21](http://web.mit.edu/music21/) library.
There is still a lot of work left regarding keeping information from the MIDI file 
and training the NN on more detailed representations.


The code for parsing the MIDI files came from [this guy](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5),
and I have changed the code a little to suit my needs. 

For instance, I do not need a one-hot-vector for classifying correct class in a autoencoder. So I've reduced his code.

I will continue working on representing the duration and velocity of the notes and chords.
