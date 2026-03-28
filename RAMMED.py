
def main():
    #Try to import required libraries as some of these are not integrated
    try:
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
            # We really only want to know if the TCP connection timed out.
            # If anything else has happened the error should be raised.
            except socket.timeout:
                return False
            finally:
                sckt.close()
    except:
        print("Could not fetch required libraries! Please connect to the internet and download required libraries. Exiting...")
    else:
        #Intakes users filepath, ensures they copied the right one, and strips any "" if they copied it directly via file manager
        while True:
            filepath = input('Please paste your minecraft mod folder filepath from your modloader: ')
            if "minecraft" not in filepath:
                print('Minecraft was not detected in the filepath, check your path again!')
            else:
                filepath = filepath.replace('"', '')
                confirm = input(f"Is this the right filepath? Y/N: \n{filepath}\n")
                if confirm == 'Y' or confirm == 'y':
                    #for whatever reason, the python interpreter can only use filepaths when its formatted with a // rather than just /
                    filepath = filepath.replace("/","//")
                    break
                else:
                    pass

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
                    cachedHosts.close()
                    c = 1
        except:
            #If this is the first time the user has ran the script, or they deleted the cache, the above will error and move to here
            #creates cache file, manually finds the address 
            print("Creating cache...")
            cachedHosts = open("knownhosts.txt", "w")
            print("Opened cache...")
            for nmapLite in range(1, 255):
                nmapLite = str(nmapLite)
                localAddress = f"192.168.8.{nmapLite}"
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
                    with tempfile.TemporaryDirectory() as tmp:
                        #urllib is weird, you have to designate a new filename to save the files as rather than saving them to a
                        #directory/folder... which means the way this project functioned changed, now you just download all mods
                        #from someones mod folder directly rather than making it a big archive
                        tmpTMP = os.path.join(tmp, "mods.zip")
                        #downloads all files on the webserver, saves it as an archive
                        download(webserver, filename=tmpTMP)
                        #unpacks the mods downloaded into mod.zip and moves them to the mod folder
                        unpack(filename=tmpTMP, extract_dir=filepath)
                        os.remove(tmpTMP)
                        #lists all downloaded files in the temporary directory
                        print('Finished, please check mod loader and compare your mod list to your LAN mates!')
                    break

        else:
            #case for if unable to connect to the previous known hosts
            if c == 0:
                print("All known hosts offline! Moving to manual scan...")
                for nmapLite in range(1, 255):
                    nmapLite = str(nmapLite)
                    localAddress = f"192.168.8.{nmapLite}"
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
                        cachedHosts.write(f"{localAddress}\n")
                        print("Wrote to cache...")
                        cachedHosts.close()
                        #makes sure its a legit path, returns as a true directory for later use
                        #creates a secure temporary folder in the systems temp file directory
                        with tempfile.TemporaryDirectory() as tmp:
                            tmpTMP = os.path.join(tmp, "mods.zip")
                            #downloads all files on the webserver, saves it to temp directory
                            download(webserver, filename=tmpTMP)
                            unpack(filename=tmpTMP, extract_dir=filepath)
                            os.remove(tmpTMP)
                            #lists all downloaded files in the temporary directory
                            print('Finished, please check mod loader and compare your mod list to your LAN mates!')
                            break
            elif c == 1:
                #case if connected to previous known host
                with tempfile.TemporaryDirectory() as tmp:
                    #urllib is weird, you have to designate a new filename to save the files as rather than saving them to a
                    #directory/folder... which means the way this project functioned changed, now you just download all mods
                    #from someones mod folder directly rather than making it a big archive
                    tmpTMP = os.path.join(tmp, "mods.zip")
                    #downloads all files on the webserver, saves it to temp directory
                    download(webserver, filename=tmpTMP)
                    unpack(filename=tmpTMP, extract_dir=filepath)
                    os.remove(tmpTMP)
                    #lists all downloaded files in the temporary directory
                    print('Finished, please check mod loader and compare your mod list to your LAN mates!')

def lister():
    #imports listdir exclusively
    from os import listdir as list
    while True:
        #Intakes users filepath, ensures they copied the right one, and strips any "" if they copied it directly via file manager
        filepath = input('Please paste your minecraft mod folder filepath from your modloader: ')
        if "minecraft" not in filepath:
            print('Minecraft was not detected in the filepath, check your path again!')
        else:
            filepath = filepath.replace('"', '')
            confirm = input(f"Is this the right filepath? Y/N: \n{filepath}\n")
            if confirm == 'Y' or confirm == 'y':
                #python interpreter works with filepaths using // instead of /
                filepath = filepath.replace("/","//")
                modlist = list(filepath)
                print("Here are your installed mods: ")
                #only presents mod files, ignores readme's/other files (.disabled is the extension mod loaders use to disable mods)
                for l in modlist:
                    if ".zip" in l or ".disabled" in l or ".jar" in l:
                        print(l)
                    else:
                        pass
                break
            else:
                pass

def deleter():
    #imports select tools from OS lib
    from os import rmdir
    from os import listdir
    from os import remove
    from os.path import dirname
    from os.path import join
    while True:
        #Intakes users filepath, ensures they copied the right one, and strips any "" if they copied it directly via file manager
        filepath = input('Please paste your minecraft mod folder filepath from your modloader: ')
        if "minecraft" not in filepath:
            print('Minecraft was not detected in the filepath, check your path again!')
        else:
            filepath = filepath.replace('"', '')
            confirm = input(f"Is this the right filepath? Y/N: \n{filepath}\n")
            if confirm == 'Y' or confirm == 'y':
                #python interpreter works with filepaths using // rather than /
                filepath = filepath.replace("/","//")
                #makes a list of files in the directory for deletion
                list = listdir(filepath)
                #takes each file, appends it to the modfolder path, then passes that to os.remove for deletion
                for l in list:
                    delFile = str(l)
                    print(f"Deleting {delFile}...")
                    #delFile = (f"{filepath}//{delFile}")
                    delFile = join(filepath, delFile)
                    remove(delFile)
                break
            else:
                pass

def server():
    #import required functions from libs
    from shutil import make_archive as archive
    from os.path import join
    import tempfile
    while True:
        #Intakes users filepath, ensures they copied the right one, and strips any "" if they copied it directly via file manager
        filepath = input('Please paste your minecraft mod folder filepath from your modloader: ')
        if "minecraft" not in filepath:
            print('Minecraft was not detected in the filepath, check your path again!')
        else:
            filepath = filepath.replace('"', '')
            confirm = input(f"Is this the right filepath? Y/N: \n{filepath}\n")
            if confirm == 'Y' or confirm == 'y':
                #python interpreter uses // instead of / for formatting file paths
                filepath = filepath.replace("/","//")
                with tempfile.TemporaryDirectory() as tmp:
                    #makes it basically C:/users/user/appdata/local/temp/mods.file, then shutil modifies it to mods.zip, then
                    #python hosts it from that temporary folder
                    tmpTMP = join(tmp, "mods")
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
            else:
                pass
    
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
        
asciiArt()

#Note regarding security:
#Server can be exploited maliciously, since the minecraft folder is not found automatically,
#nor is it even checked if minecraft is installed. One could host a malicious server with
#malware posing as mods. Only run the installer if you trust all users on the network.

#Installer therefore has implicit security flaws, since there is no verification of discovered
#hosts. You're literally just blindly throwing yourself at a random host, and downloading whatever folder
#they're serving; again, only run the installer if you trust all users on the network.