#automatically opens the top result of a song in youtube

import requests, sys, webbrowser, bs4

print('Searching Youtube')
if len(sys.argv)>1:
    vid_name = '+'.join(sys.argv[1:])
#    print(vid_name)

res = requests.get('https://www.youtube.com/results?search_query='+vid_name))
res.raise_for_status()

#TODO choose the top link in Youtube

#open a browser tab for the link
