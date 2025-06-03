import os
import subprocess
import time
import argparse

def get_sorted_pcaps(pcap_dir):
	pcaps = [f for f in os.listdir(pcap_dir) if f.endswith(".pcap") or f.endswith(".pcapng")]
	pcaps.sort(key=lambda f: os.path.getmtime(os.path.join(pcap_dir, f)))
	return pcaps

def replay_pcaps(pcap_dir, interface, delay=0):
	pcaps = get_sorted_pcaps(pcap_dir)
	if not pcaps:
    		print(f"No PCAP files found in directory: {pcap_dir}")
    		return

	print(f"Replaying {len(pcaps)} PCAP files in chronological order:\n")
	for pcap in pcaps:
    		pcap_path = os.path.join(pcap_dir, pcap)
    		print(f"▶ Replaying: {pcap_path}")
    		try:
        		subprocess.run(["tcpreplay", "-i", interface, pcap_path], check=True)
    		except subprocess.CalledProcessError as e:
        		print(f"❌ Error replaying {pcap}: {e}")
    		if delay > 0:
        		print(f"⏳ Waiting {delay} seconds before next file...")
        		time.sleep(delay)

def main():
	parser = argparse.ArgumentParser(description="Replay PCAP files in chronological order using tcpreplay.")
	parser.add_argument("pcap_dir", help="Path to the directory containing .pcap or .pcapng files")
	parser.add_argument("interface", help="Network interface to use for replay")
	parser.add_argument("--delay", type=int, default=0, help="Optional delay (in seconds) between file replays")

	args = parser.parse_args()

	if not os.path.isdir(args.pcap_dir):
    		print(f"❌ Error: The provided PCAP directory does not exist: {args.pcap_dir}")
    		return

	replay_pcaps(args.pcap_dir, args.interface, args.delay)

if __name__ == "__main__":
	main()
