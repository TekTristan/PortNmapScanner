import nmap
import sys
import time

nm = nmap.PortScanner()

print('\nRunning...\n')

nmScanner = nm.scan(sys.argv[1], '80', arguments='-O')

  

hostOnline = "The host is: "+nmScanner['scan'][sys.argv[1]]['status']['state']+".\n"

portOpen="The port 80 is: "+nmScanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"

methodScan = "The method of scanning is: "+nmScanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"

guessedOS = "There is a %s percent chance that the host is running %s"%(nmScanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'], nmScanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"

  

with open("%s.txt"%sys.argv[1], 'w') as f:
    f.write(hostOnline+portOpen+methodScan+guessedOS)

    f.write("\nReport Generated "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))



print("\nFinished...")