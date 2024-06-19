import subprocess
import requests

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

if __name__ == "__main__":
    file_path = input("Enter the path to the text file containing the list of domains: ")

    try:
        with open(file_path, 'r') as file:
            domain_list = [line.strip() for line in file.readlines()]

        for domain in domain_list:
            check_domain(domain)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")