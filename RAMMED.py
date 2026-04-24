def fp():
    import os.path
    import os
    global filepath
    global path
    if os.name == 'nt':
        pospaths = []
        cache = open("ntpaths.txt", "r")
        ntpaths = list(cache)
        for i in ntpaths:
            i = i.strip()
            i = os.path.expanduser(i)
            if os.path.isdir(i) == False:
                pass
            elif os.path.isdir(i) == True:
                pospaths.append(i)        
        if len(pospaths) < 2:
            for i in pospaths:
                path = i
                break
        elif len(pospaths) > 1:
            print("Multiple modloaders found, which one would you like to select? ")
            a = 0
            for i in pospaths:
                a += 1
                if "curse" in i:
                    i = "Curseforge"
                elif "gd" in i:
                    i = "GD_Launcher"
                elif "lunar" in i:
                    i = "Lunar Client"
                elif "prism" in i:
                    i = "Prism Launcher"
                elif "Modrinth" in i:
                    i = "Modrinth"
                print(f"{a}. {i}")
            a = 0
            multsel = int(input())
            for i in pospaths:
                a += 1
                if a == multsel:
                    path = i
                else:
                    pass
        if len(pospaths) == 0:
            print("Could not detect a mod loader! Exiting... ")
            import sys
            sys.exit(0)
    elif os.name == "posix":
        pospaths = []
        cache = open("posixpaths.txt", "r")
        ntpaths = list(cache)
        for i in ntpaths:
            i = i.strip()
            i = os.path.expanduser(i)
            if os.path.isdir(i) == False:
                pass
            elif os.path.isdir(i) == True:
                pospaths.append(i)        
        if len(pospaths) < 2:
            for i in pospaths:
                path = i
                break
        elif len(pospaths) > 1:
            print("Multiple modloaders found, which one would you like to select? ")
            a = 0
            for i in pospaths:
                a += 1
                if "curse" in i:
                    i = "Curseforge"
                elif "gd" in i:
                    i = "GD_Launcher"
                elif "lunar" in i:
                    i = "Lunar Client"
                elif "prism" in i:
                    i = "Prism Launcher"
                elif "Modrinth" in i:
                    i = "Modrinth"
                print(f"{a}. {i}")
            a = 0
            multsel = int(input())
            for i in pospaths:
                a += 1
                if a == multsel:
                    path = i
                else:
                    pass
        if len(pospaths) == 0:
            print("Could not detect a mod loader! Exiting... ")
            import sys
            sys.exit(0)
    listedpath = list(os.listdir(path))
    if len(listedpath) < 2:
        for i in listedpath:
            path = f"{path}\{i}\mods"
            filepath = path
    else:
        c = 0
        modfolder = ""
        for i in listedpath:
            c += 1
            modfolder += i
            print(f"{c}. {i}")
        if c > 1:
            sel = int(input("Which instance would you like to select? "))
            c = 0
            for i in listedpath:
                c += 1
                if sel != c:
                    pass
                else:
                    path = f"{path}\{i}\mods"
                    filepath = path
def asciiArt():
    print("\n    Welcome to the Rudimentary Assisted Minecraft Modpack Extractor and Downloader (or RAMMED)! ")
    #r ignores some escape characters to make asciiArt less hellish to implement, ''' lets text exist beyond a single line
    while True:
        print(r'''
                                                                                    
                                        ____            ____                          
    ,-.----.      ,---,               ,'  , `.        ,'  , `.    ,---,.    ,---,     
    \    /  \    '  .' \           ,-+-,.' _ |     ,-+-,.' _ |  ,'  .' |  .'  .' `\   
    ;   :    \  /  ;    '.      ,-+-. ;   , ||  ,-+-. ;   , ||,---.'   |,---.'     \  
    |   | .\ : :  :       \    ,--.'|'   |  ;| ,--.'|'   |  ;||   |   .'|   |  .`\  | 
    .   : |: | :  |   /\   \  |   |  ,', |  ':|   |  ,', |  '::   :  |-,:   : |  '  | 
    |   |  \ : |  :  ' ;.   : |   | /  | |  |||   | /  | |  ||:   |  ;/||   ' '  ;  : 
    |   : .  / |  |  ;/  \   \|   | :  | :  |,'   | :  | :  |,|   :   .''   | ;  .  | 
    ;   | |  \ '  :  | \  \ ,';   . |  ; |--' ;   . |  ; |--' |   |  |-,|   | :  |  ' 
    |   | ;\  \|  |  '  '--'  |   : |  | ,    |   : |  | ,    '   :  ;/|'   : | /  ;  
    :   ' | \.'|  :  :        |   : '  |/     |   : '  |/     |   |    \|   | '` ,/   
    :   : :-'  |  | ,'        ;   | |`-'      ;   | |`-'      |   :   .';   :  .'     
    |   |.'    `--''          |   ;/          |   ;/          |   | ,'  |   ,.'       
    `---'                     '---'           '---'           `----'    '---'         

        
        
                                                                                            ''')
        launcher = input("What would you like to do? (ctrl + c to quit at any time) \n1. Install mods\n2. List all mods\n3. Remove all mods\n4. Share your mods\n")
        if launcher == "1":
            main()
        elif launcher == "2":
            lister()
        elif launcher == "3":
            deleter()
        elif launcher == "4":
            server()
        else:
            print("Exiting...")
            break
def main():
    #Try to import required libraries as some of these are not integrated
    try:
        import socket
        import os
        import tempfile
        from urllib.request import urlretrieve as download
        from shutil import unpack_archive as unpack
        # This is code from the netutils library, not my own. I have only manually added the ping function
        # and changed the timeout value to accept float data types instead of integers for the purposes
        # of this script. Full credit goes to it's original creators!
        def ping(ip: str, port: int, timeout: float = 1.0) -> bool:
            import socket
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.settimeout(float(timeout))
            try:
                sckt.connect((ip, int(port)))  
                sckt.shutdown(socket.SHUT_RDWR)
                return True
            except socket.timeout:
                return False
            finally:
                sckt.close()
        def instUnpck():
            global filepath, path
            with tempfile.TemporaryDirectory() as tmp:
                #urllib is weird, you have to designate a new filename to save the files as rather than saving them to a
                #directory/folder...
                tmpTMP = os.path.join(tmp, "mods.zip")
                #downloads all files on the webserver, saves it as an archive
                download(webserver, filename=tmpTMP)
                #unpacks the mods downloaded into mod.zip and moves them to the mod folder
                fp()
                unpack(filename=tmpTMP, extract_dir=filepath)
                os.remove(tmpTMP)
                #lists all downloaded files in the temporary directory
                print('Finished, please check mod loader and compare your mod list to your LAN mates!')
    except:
        print("Could not fetch required libraries! Please connect to the internet and download required libraries. Exiting...")

    else:
        try:
            #c acts as a state check for what has happened, 0 means all hosts are dead, 1 means it successfully connected to one
            #please please please never use this script on public wifi its so insecure lmao
            c = 0
            #attempts to read a cache of hosts, attempts to connect to each one
            print("Attempting to read cache...")
            cachedHosts = open("knownhosts.txt", "r")
            print('Read cache...')
            for hosts in cachedHosts:
                hosts = hosts.replace("\n", "")
                hosts = hosts.replace(" ", "")
                print(f"Attempting to connect to previous known host {hosts}...")
                concheck = ping(hosts, 8259, timeout=1.0)
                if concheck == False:
                    print(f"Could not connect to {hosts}, trying next...")
                    pass
                elif concheck == True:
                    localAddress = hosts
                    webserver = f"http://{localAddress}:8259/mods.zip"
                    print(f"Found webserver on {webserver}! Attempting download...")
                    c = 1
        except:
            #If this is the first time the user has ran the script, or they deleted the cache, the above will error and move to here
            #creates cache file, manually finds the address
            #the idea to use socket to get the local ip was done by AI, though it was manually implemented by us
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            local_ip = local_ip.split(".")
            print("Creating cache...")
            cachedHosts = open("knownhosts.txt", "w")
            print("Opened cache...")
            for nmapLite in range(1, 255):
                nmapLite = str(nmapLite)
                local_ip[-1] = nmapLite
                localAddress = '.'.join(local_ip)
                print(f"Trying {localAddress}...")
                #pings the address on port 8259, gives 200ms for a response (average latency is < 15ms)
                concheck = ping(localAddress, 8259, timeout=0.2)
                if concheck == False:
                    pass
                else:
                    #turns the correct IP into a http formatted address, setup to download everything under / on the webserver
                    webserver = f"http://{localAddress}:8259/mods.zip"
                    print(f"Found webserver on {webserver}! Attempting download...")
                    #writes the address as the raw ip to cache
                    print("Writing to cache...")
                    cachedHosts.write(f"{localAddress}\n")
                    print("Wrote to cache...")
                    cachedHosts.close()
                #creates a secure temporary folder in the systems temp file directory
                    instUnpck()
                    break

        else:
            #case for if unable to connect to the previous known hosts
            if c == 0:
                #the idea to use socket to get the local ip was done by AI, though it was manually implemented by us
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)
                local_ip = local_ip.split(".")
                print("All known hosts offline! Moving to manual scan...")
                for nmapLite in range(1, 255):
                    nmapLite = str(nmapLite)
                    local_ip[-1] = nmapLite
                    localAddress = '.'.join(local_ip)
                    print(f"Trying {localAddress}...")
                    #pings the address on port 8259, gives 200ms for a response (average latency is < 15ms)
                    concheck = ping(localAddress, 8259, timeout=0.2)
                    if concheck == False:
                        pass
                    else:
                        #turns the correct IP into a http formatted address, setup to download everything under / on the webserver
                        webserver = f"http://{localAddress}:8259/mods.zip"
                        print(f"Found webserver on {webserver}! Attempting download...")
                        #closes it as read, opens it again as write, writes the address, closes
                        cachedHosts.close()
                        print("Opening cache for writing...")
                        cachedHosts = open("knownhosts.txt", "a")
                        print("Writing to cache... ")
                        cachedHosts.write(f"\n{localAddress}")
                        print("Wrote to cache... ")
                        cachedHosts.close()
                        #makes sure its a legit path, returns as a true directory for later use
                        #creates a secure temporary folder in the systems temp file directory
                        instUnpck()
                        break
            elif c == 1:
                #case if connected to previous known host
                instUnpck()
def lister():
    #imports listdir exclusively
    from os import listdir as list
    from time import sleep
    global filepath, path
    fp()
    while True:
        #python interpreter works with filepaths using // instead of /
        filepath = filepath.replace("/","//")
        modlist = list(filepath)
        print("Here are your installed mods: ")
        #only presents mod files, ignores readme's/other files (.disabled is the extension mod loaders use to disable mods)
        for l in modlist:
            if ".zip" in l or ".disabled" in l or ".jar" in l:
                print(l)
                sleep(0.005)
            else:
                pass
        break
def deleter():
    #imports select tools from OS lib
    from os import listdir
    from os import remove
    from os.path import join
    from time import sleep
    while True:
        global filepath, path
        fp()
        confirm = input(f"Is this the right filepath? Y/N: \n{filepath}\n")
        if confirm == 'Y' or confirm == 'y':
            #python interpreter works with filepaths using // rather than /
            #makes a list of files in the directory for deletion
            list = listdir(filepath)
            #takes each file, appends it to the modfolder path, then passes that to os.remove for deletion
            for l in list:
                delFile = str(l)
                print(f"Deleting {delFile}...")
                delFile = join(filepath, delFile)
                #prevents oopsie daisies (total system anihilation)
                if ".zip" in delFile or ".jar" in delFile or ".disabled" in delFile:
                    remove(delFile)
                    sleep(0.005)
                else:
                    pass
            break
        else:
            break
def server():
    #import required functions from libs
    from shutil import make_archive as archive
    from os.path import join
    import tempfile
    while True:
        with tempfile.TemporaryDirectory() as tmp:
            #makes it basically C:/users/user/appdata/local/temp/mods.file, then shutil modifies it to mods.zip, then
            #python hosts it from that temporary folder
            tmpTMP = join(tmp, "mods")
            global filepath, path
            fp()
            archive(base_name=tmpTMP, format="zip", root_dir=filepath)
            import http.server
            import socketserver
            import functools
            PORT = 8259
            DIRECTORY = tmp
            #standard handler for http, default for most browsers
            Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
            #serves all files in a tcp server, keeps it open forever till the user interupts
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f"Serving at port {PORT}, your friends should be able to see and download your mods now!")
                httpd.serve_forever()
            break

asciiArt()

# Things to add:
#      clamd anti-virus on share/install functions (if it's light enough)
#      UI Cleanup
#      option to delete entire instance folder
#      Massively overhauled webserver address locator
