**Traffic generation, capture, replay** -- 3 scripts built for use in the Linux CLI to generate generic traffic, capturing it using tshark, and replaying using TCPReplay
  
generate_traffic.py: 
  requires 1 input (duration)
How to run:
  sudo python3 generate_traffic.py -d [Duration in seconds]

capture_traffic.py:
  requires 3 inputs (interface, duration, output filepath and filename)
How to run:
  sudo python3 capture_traffic.py -i [Interface] -d [Duration in seconds] -o [Path/to/filename]

replay_pcaps.py:
  requires 2 inputs, *1 optional input* (filepath, interface, *delay*)
How to run:
  sudo python3 replay_pcaps.py [/path/to/files] [Interface] --delay [duration of delay, seconds]
