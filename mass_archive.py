from __future__ import print_function

import sys
import requests
import archiveis

PERMA_AIP_KEY = ""  # <-- remember to put your Perma.cc API key in here

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

    assert PERMA_AIP_KEY, "PERMA_AIP_KEY is not set."
    print("[*] Pushing to Perma.cc...")

    response = requests.post("https://api.perma.cc/v1/archives/?api_key=" +
                             PERMA_AIP_KEY, data={'url': target})
    if response.status_code == 201:

        page_id = response.json()['guid']
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
perma_result = perma(target) if PERMA_AIP_KEY else "Skipping Perma: No API key"
print(perma_result)
