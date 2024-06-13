## Nmap Active Info Script
This Python script uses the nmap library to perform a port scan and OS detection on a specified target. The script scans port 80 and attempts to identify the operating system running on the target. The results are saved to a text file.

## Requirements
- Python 3.x
- 'python-nmap' library
- Nmap installed on your system

## Installing python-nmap
```
pip install python-nmap
```

## Usage
1.) Save script to file, for example port.py

2.) Run the script with the target ip as the first argument
```
python port.py <target ip address>
```
