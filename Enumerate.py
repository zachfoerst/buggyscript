import subprocess
import requests
import os

def check_domain(domain):
    try:
        # Check DNS records using nslookup
        nslookup_output = subprocess.check_output(['nslookup', domain], universal_newlines=True)
        if 'Non-existent domain' in nslookup_output:
            print(f"{domain}: DNS records not found")
        else:
            print(f"{domain}: DNS records found")

            # Check HTTP response
            try:
                response = requests.get(f"http://{domain}", timeout=5)
                if response.status_code == 200:
                    print(f"{domain}: Website is active")
                else:
                    print(f"{domain}: Website returned status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"{domain}: Error checking website - {e}")

    except subprocess.CalledProcessError:
        print(f"{domain}: Error checking DNS records")

print("\033[92m" + "="*50 + "\033[0m")
print("\033[91m" + "Enum deez".center(50) + "\033[0m")
print("\033[91m" + "By: Dark Mattr".center(50) + "\033[0m")
print("\033[92m" + "="*50 + "\033[0m")
print()
print()

domain = input("Which domain would you like to look at today? ")

subsSaved = domain + "_subs.txt"

def get_subs():
    try:
        subprocess.run(["subfinder", "-d", domain, "-o", subsSaved], check=True)
        print(f"Subdomains saved to {subsSaved}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Subfinder: {e}")

get_subs()

subs_list = open(subsSaved).readlines()
print("Subdomains found:")
for sub in subs_list:
    check_domain(sub.strip())