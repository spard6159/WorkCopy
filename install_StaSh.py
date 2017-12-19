# from https://forum.omz-software.com/topic/1919/stash-shell-like-an-expert-in-pythonista

# this script will get pip working on iOS!

import requests as r
exec(r.get('http://bit.ly/get-stash').text)