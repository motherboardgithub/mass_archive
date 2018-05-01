import sys
import requests
import archiveis
import json

target     = sys.argv[1]
input      = str(target)

print "[*] Archiving %s..." % input

#
# function for pushing to The Internet Archive/Wayback Machine
#
def internet_archive(input):
    
    print "[*] Pushing to the Wayback Machine..."
    
    save_url = "https://web.archive.org/save/%s" % input
    
    # send off request to wayback machine
    response = requests.get(save_url)
    
    if response.status_code == 200:
        
        # grab the part of the URL dealing with the archive page
        result               = response.headers['Content-Location']
        
        # build archive URL 
        internet_archive_url = "https://web.archive.org%s" % result
        
        return internet_archive_url
    else:
        print "[!] Connection error"

#
# function for pushing to Perma.cc
#   
def perma(input):
    
    print "[*] Pushing to Perma.cc..."
    
    perma_json = {}
    perma_json['url'] = '%s' % input
    
    # remember to put your Perma.cc API key in here
    response = requests.post("https://api.perma.cc/v1/archives/?api_key=YOUR_PERMA_API_KEY_HERE", data=perma_json)
    if response.status_code == 201:
         
        result = json.loads(response.content)
        page_id = result['guid']
        perma_url = "https://perma.cc/%s" % page_id

        return perma_url
    else:
        print "[*] Connection error"
    
# push to The Internet Archive
internet_archive_result = internet_archive(input)
print internet_archive_result

# push to archive.is
print "[*] Pushing to archive.is..."
archiveis_result = archiveis.capture(input)
print archiveis_result

# push to perma.cc
perma_result = perma(input)
print perma_result
