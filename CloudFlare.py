## CFBypass 
# Coded on 16/04/2020
# Inspired by CloudSearch.cf
# Author = ghosthub
# Imports
import os
import socket
# END Imports
os.system('clear')
class c:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
        white='\033[0m'

print c.red +"""
    __  _____  ____   __ __  ____   ____  _____ _____
   /  ]|     ||    \ |  |  ||    \ /    |/ ___// ___/
  /  / |   __||  o  )|  |  ||  o  )  o  (   \_(   \_
 /  /  |  |_  |     ||  ~  ||   _/|     |\__  |\__  |
/   \_ |   _] |  O  ||___, ||  |  |  _  |/  \ |/  \ |
\     ||  |   |     ||     ||  |  |  |  |\    |\    |
 \____||__|   |_____||____/ |__|  |__|__| \___| \___|

               CFBypass - CloudFlare Bypass
                 Author - ghosthub (b@b@y)
"""
i = raw_input(c.orange + "Website Name> " + c.white)
websitename = "i"
ip = socket.gethostbyname('ssh.'+i)
print c.pink + "IP Behind Cloudflare - "+ip
    
