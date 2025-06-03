import subprocess
import time
import random
import argparse

# Simulated traffic actions
def simulate_ping():
	targets = ["8.8.8.8", "1.1.1.1", "www.google.com"]
	target = random.choice(targets)
	subprocess.run(["ping", "-c", "3", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def simulate_http_request():
	urls = ["http://example.com", "http://neverssl.com", "http://httpbin.org/get"]
	url = random.choice(urls)
	subprocess.run(["curl", "-s", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def simulate_dns_query():
	domains = ["google.com", "openai.com", "wikipedia.org"]
	domain = random.choice(domains)
	subprocess.run(["dig", domain], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#def simulate_ntp():
#	subprocess.run(["ntpdate", "-q", "pool.ntp.org"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def simulate_package_update():
	subprocess.run(["apt-get", "update"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Main traffic generator
def run_traffic(duration_seconds):
	actions = [simulate_ping, simulate_http_request, simulate_dns_query, simulate_package_update] #,simulate_ntp]
	start_time = time.time()

	print(f"Generating traffic for {duration_seconds} seconds...")
	while time.time() - start_time < duration_seconds:
    		action = random.choice(actions)
    		action()
    		delay = random.uniform(300, 1200)
    		time.sleep(delay)
	print("Traffic generation complete.")

# Command-line interface
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Simulate normal Linux network traffic.")
	parser.add_argument("-d", "--duration", type=int, required=True, help="Duration to run traffic generator (in seconds)")
	args = parser.parse_args()

	run_traffic(args.duration)
