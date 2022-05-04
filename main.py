# pip install requests
import requests
# pip install colorama
from colorama import init
from colorama import Fore as c 
from colorama import Style as s

import json

init()

class LoAd :
    def __init__(self, url):
        self.session = requests.Session()
        try:
            if  self.session.get("https://"+url).status_code != 200:
                raise 
        except :
                raise Exception("Invalid URL")
        self.url = url
        self.words = []
        self.possible  = {}
        self.include_wordlist()
        try : 
            self.checker()
            print(c.GREEN + "Done" + c.RESET)
        except KeyboardInterrupt:
            print(c.RED + "\n Exiting..." + c.RESET)
            print(c.GREEN + "Possible Admin Panels :" + c.RESET)
            for u,s in self.possible.items():
                print(f"{c.GREEN}{u} {c.YELLOW}>>>  {c.BLUE}{s} ")
            if input(f"{c.RED}Do You Want To Save The Results [y/N] ?  {c.RESET}").upper() == "Y":
                with open(f"{self.url}.results.json", 'w') as f:
                    json.dump(self.possible, f)
                    print(f"{c.GREEN}Results Saved To {self.url}.results.json")
            exit()
        
    def checker(self):
        for ind , word in enumerate(self.words):
            url = f"https://{self.url}/{word}"
            r =  self.session.get(url).status_code
            if r != 404:
                print(f"{c.GREEN }Possible Admin Panel : {c.RED}{url}{c.RESET}")
                self.possible[url] = r
            else:
                print(f"{c.BLUE}Try : {c.YELLOW} {ind+1} {c.RED}FAILED{c.RESET}")

    def include_wordlist(self):
        try :
            with open("wordlist.txt", 'r') as f:
                [ self.words.append(line.strip()) for line in f ]
        except:
            raise Exception("Wordlist not found")
        print(c.GREEN + "Wordlist loaded" + c.RESET)
        print(c.GREEN + "Total words: " + str(len(self.words)) + c.RESET)
if __name__ == "__main__":
    url = input("Enter the url: ")
    main = LoAd(url)


