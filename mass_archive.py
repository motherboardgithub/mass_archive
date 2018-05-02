from __future__ import print_function

import sys
import requests
import archiveis
import json

URL = "https://api.perma.cc/v1/archives/?api_key=YOUR_PERMA_API_KEY_HERE"

target = str(sys.argv[1])

print("[*] Archiving %s..." % target)


#
# function for pushing to The Internet Archive/Wayback Machine
#
def internet_archive(target):

    print("[*] Pushing to the Wayback Machine...")

    save_url = "https://web.archive.org/save/%s" % target

    # send off request to wayback machine
    response = requests.get(save_url)

    if response.status_code == 200:

        # grab the part of the URL dealing with the archive page
        result = response.headers['Content-Location']

        # build archive URL
        internet_archive_url = "https://web.archive.org%s" % result

        return internet_archive_url
    else:
        print("[!] Connection error")


#
# function for pushing to Perma.cc
#
def perma(target):

    print("[*] Pushing to Perma.cc...")

    perma_json = {}
    perma_json['url'] = '%s' % target

    # remember to put your Perma.cc API key in here
    response = requests.post(URL, data=perma_json)
    if response.status_code == 201:

        result = json.loads(response.content)
        page_id = result['guid']
        perma_url = "https://perma.cc/%s" % page_id

        return perma_url
    else:
        print("[*] Connection error")


# push to The Internet Archive
internet_archive_result = internet_archive(target)
print(internet_archive_result)

# push to archive.is
print("[*] Pushing to archive.is...")
archiveis_result = archiveis.capture(target)
print(archiveis_result)

# push to perma.cc
perma_result = perma(target)
print(perma_result)
