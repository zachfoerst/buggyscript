import sublist3r




print("\033[92m" + "="*50 + "\033[0m")
print("\033[91m" + "Enum deez".center(50) + "\033[0m")
print("\033[91m" + "By: Dark Mattr".center(50) + "\033[0m")
print("\033[92m" + "="*50 + "\033[0m")
print()
print()




domain = input("Which domain would you like to look at today? ")

subsSaved = domain + "subs.txt"

def get_subs():
    subdomains = sublist3r.main (domain, 40, subsSaved, ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)

get_subs()

subs_list = open(subsSaved).readlines()
print(subs_list)



