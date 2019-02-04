# mass_archive
A basic Python tool for pushing a web page to multiple archiving services at once.

# Archivers:

mass_archive uses three different (mostly free) archiving services:

- The Wayback Machine
- Archive.is
- Perma.cc

Perma.cc will soon no longer offer free archives, so if you'd rather remove the option to upload to Perma, feel free to comment it out. If you do keep it in, before running mass_archive you'll also need to get a Perma.cc API key and paste it into "YOUR_PERMA_API_KEY_HERE" in the mass_archive script (instructions on finding your Perma.cc API key here: https://perma.cc/docs/developer). 

# Requirements and installation:

mass_archive requires several different modules to function. Those modules are:

- requests - handles HTTP requests
- json - for JSON metadata handling
- [archiveis] (https://github.com/pastpages/archiveis) - a wrapper for the archiveis service

You can typically install these, if necessary, through pip:

`pip3 install --user -U archiveis jsonpatch requests`

The required dependencies should be periodically upgraded by re-running the above command.

The tool works with Python 2.7 (pip) and Python 3 (pip3).

# Usage:

Example:

`python3 mass_archive.py [URL]`

To use the tool, download the mass_archive.py script, open a terminal in the directory you put the file, and type "python mass_archive.py example.com", with example.com being the webpage you want to archive. You can also input a file containing a list of URLs if you want to archive a load at once. Type "python mass_archive.py --list filename.txt".
