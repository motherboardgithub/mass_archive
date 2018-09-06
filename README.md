# mass_archive
A basic python 2.7 tool for pushing a web page to multiple archiving services at once.

# Archivers:

mass_archive uses three different (mostly free) archiving services:

- The Wayback Machine
- Archive.is
- Perma.cc

To use Perma.cc, you'll need to sign up for an account on their website, where you'll get 10 free archives per month. Before running mass_archive, you'll also need to get a Perma.cc API key and paste it into "YOUR_PERMA_API_KEY_HERE" in the mass_archive script (instructions on finding your Perma.cc API key here: https://perma.cc/docs/developer). If you'd rather remove the option to upload to Perma, feel free to comment it out.

# Requirements:

mass_archive requires several different modules to function. Those modules are:

- requests
- json
- archiveis (a wrapper for the archiveis service, install here: https://github.com/pastpages/archiveis)

You can typically install these, if necessary, through pip (details on pip here: https://pip.pypa.io/en/stable/installing/)

# Usage:

To use the tool, download the mass_archive.py script, open a terminal in the directory you put the file, and type "python mass_archive.py example.com", with example.com being the webpage you want to archive. You can also input a file containing a list of URLs if you want to archive a load at once. Type "python mass_archive.py --list filename.txt".
