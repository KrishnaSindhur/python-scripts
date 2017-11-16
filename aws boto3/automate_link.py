''' This will open all link in your browser present in file link.txt'''

import webbrowser
with open('/home/krish/link.txt') as f:
    for line in f:
        webbrowser.open(line)
