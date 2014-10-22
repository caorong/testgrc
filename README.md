 
cvlc udp://@0.0.0.0:5005

gqrx 

verify the data 

nc -l -u 7355

nc -l -u 7355 | aplay -r 48k -f S16_LE -t raw -c 1

vlc --demux=rawaud --rawaud-channels=1 --rawaud-samplerate=48000 udp://@:7355
