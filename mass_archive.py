#!/usr/bin/env python3

import os
import sys
import json
import argparse
import requests
import archiveis

# Modify this to add a default Perma.cc API key.
perma_key = ""

def internet_archive(url):
    """
    Function for pushing to The Internet Archive/Wayback Machine
    """
    print("[*] Pushing to the Wayback Machine...")
    
    save_url = "https://web.archive.org/save/{}".format(url)
    response = requests.get(save_url)
    
    if response.status_code == 200:
        result = response.headers["Content-Location"]
        internet_archive_url = "https://web.archive.org{}".format(result)

        print(internet_archive_url)
    else:
        print("[!] Connection error")

def perma(url):
    """
    Function for pushing to perma.cc
    """
    if not perma_key:
        return

    print("[*] Pushing to Perma.cc...")

    perma_url = "https://api.perma.cc/v1/archives/?api_key={}".format(perma_key)
    perma_json = {"url": url}
    response = requests.post(perma_url, data=perma_json)
    if response.status_code == 201:
        result = json.loads(response.content)
        page_id = result["guid"]
        archived_url = "https://perma.cc/{}".format(page_id)

        print(archived_url)
    else:
        print("[!] Connection error: did you provide a valid API key?")

def archive_is(url):
    """
    Function for pushing to archive.is
    """
    print("[*] Pushing to archive.is...")
    archiveis_result = archiveis.capture(url).replace("http://", "https://")
    print(archiveis_result)

def main():
    parser = argparse.ArgumentParser(description="Archive a webpage on multiple online web archives")
    parser.add_argument("--perma-key", action="store", required=False,
                        help="Specify API key required to submit URL to Perma.cc")
    parser.add_argument("--list", action="store_true", default=False, required=False,
                        help="Enable this flag if the target is not a URL, but a file with list of URLs")
    parser.add_argument("target", action="store",
                        help="The URL you want to archive or the path to a list of URLs")
    args = parser.parse_args()

    if args.perma_key:
        perma_key = args.perma_key

    urls = []

    if args.list:
        if not os.path.exists(args.target):
            print("[!] ERROR: the file you specified does not exist")
            sys.exit(-1)

        with open(args.target, "r") as handle:
            for line in handle:
                line = line.strip()
                if line == "":
                    continue
                urls.append(line)
    else:
        urls.append(args.target)

    for url in urls:
        print("[+] Archiving {}...".format(url))

        for func in [internet_archive, perma, archive_is]:
            try:
                func(url)
            except Exception as e:
                print("[!] ERROR: {}".format(e))

if __name__ == "__main__":
    main()
