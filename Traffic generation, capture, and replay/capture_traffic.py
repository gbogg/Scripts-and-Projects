import subprocess
import argparse
import time
from datetime import datetime, timedelta
import os

def generate_filename(base_dir, prefix):
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
	filename = f"{prefix}_{timestamp}.pcap"
	return os.path.join(base_dir, filename)

def capture_segment(interface, duration, output_file):
	print(f"[+] Capturing for {duration} seconds on {interface} -> {output_file}")
	try:
    		subprocess.run([
        		"tshark",
        		"-i", interface,
        		"-a", f"duration:{duration}",
        		"-w", output_file
    		], check=True)
	except subprocess.CalledProcessError as e:
    		print(f"[!] Error during capture: {e}")

def main(interface, total_duration, base_dir, prefix):
	segment_duration = 300  # 5 minutes
	remaining = total_duration

	os.makedirs(base_dir, exist_ok=True)

	while remaining > 0:
    		current_segment = min(segment_duration, remaining)
    		filename = generate_filename(base_dir, prefix)
    		capture_segment(interface, current_segment, filename)
    		remaining -= current_segment

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Capture network traffic in 5-minute chunks.")
	parser.add_argument("-i", "--interface", required=True, help="Network interface to capture from (e.g., eth0)")
	parser.add_argument("-d", "--duration", type=int, required=True, help="Total capture duration in seconds")
	parser.add_argument("-o", "--output_dir", required=True, help="Directory to save .pcap files")
	parser.add_argument("-p", "--prefix", default="capture", help="Filename prefix for output files")

	args = parser.parse_args()

	main(args.interface, args.duration, args.output_dir, args.prefix)
