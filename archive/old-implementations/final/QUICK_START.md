# Smart City Network - Quick Start Guide
**Fast Implementation | 23 Devices | Dual-Stack IPv4/IPv6**

## 📦 Step 1: Add All Devices (5 min)

Drag these devices onto the workspace:

```
ROUTERS:
□ 1x ISR4321 → "City-Gateway-Router"

SWITCHES:
□ 1x 3650 → "City-Core-Switch"
□ 3x 2960 → "Downtown-Switch", "Park-Switch", "Residential-Switch"

WIRELESS:
□ 2x WRT300N → "Public-WiFi-AP", "Residential-WiFi-AP"
□ 1x Cell Tower → "City-Cell-Tower"

SERVERS:
□ 5x Server-PT → "Central-Office-Server", "DNS-Server", "DHCP-Server", "Web-Server", "SMTP-Server"

END DEVICES:
□ 4x PC → "Admin-PC-1", "Admin-PC-2", "Public-Kiosk-PC", "Resident-Home-PC"
□ 1x Smartphone → "Citizen-Smartphone"
□ 2x IP Phone 7960 → "City-Hall-Phone", "Info-Line-Phone"

IOT:
□ 1x SBC-PT (Raspberry Pi) → "Park-IoT-Gateway"
□ 1x Motion Sensor → "Park-Motion-Sensor"
□ 1x Smart LED → "Smart-Streetlight"
```

---

## 🔌 Step 2: Cable Everything (10 min)

**Core Backbone:**
```
Router[Gig0/0/1] ─── [Gig0/1]Switch
```

**District Switches:**
```
Core-Switch[Gig0/2] ─── [Fa0/1]Downtown-Switch
Core-Switch[Gig0/3] ─── [Fa0/1]Park-Switch
Core-Switch[Gig0/4] ─── [Fa0/1]Residential-Switch
```

**Cellular:**
```
Cell-Tower[Coax] ═══ [Coax]Central-Office-Server[Eth] ─── [Fa0/3]Core-Switch
```

**Servers (all to Core-Switch):**
```
DNS-Server      → Fa0/4
DHCP-Server     → Fa0/5
Web-Server      → Fa0/6
SMTP-Server     → Fa0/7
```

**Admin Devices (all to Core-Switch):**
```
Admin-PC-1      → Fa0/8
Admin-PC-2      → Fa0/9
City-Hall-Phone → Fa0/10
```

**Downtown:**
```
Public-Kiosk-PC    → Downtown[Fa0/2]
Info-Line-Phone    → Downtown[Fa0/3]
Public-WiFi-AP     → Downtown[Fa0/4]
```

**Park IoT:**
```
Park-IoT-Gateway   → Park-Switch[Fa0/2]
Smart-Streetlight  → Park-Switch[Fa0/3] (network-connected LED)
Motion-Sensor      → Gateway[D0] (GPIO cable)
```

**Residential:**
```
Resident-Home-PC     → Residential[Fa0/2]
Residential-WiFi-AP  → Residential[Fa0/3]
```

**Wireless:** Smartphone will connect via WiFi/Cellular (no cable)

---

## ⚙️ Step 3: Configure Router (5 min)

Click router → CLI tab → Copy/paste:

```cisco
enable
configure terminal
hostname City-Gateway-Router
enable secret class

ipv6 unicast-routing

interface GigabitEthernet0/0/0
 ip address dhcp
 ip nat outside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown

interface GigabitEthernet0/0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 ipv6 address 2001:DB8:CITY:0::1/64
 no shutdown

ip nat inside source list 1 interface Gig0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255
ip route 0.0.0.0 0.0.0.0 Gig0/0/0
ipv6 route ::/0 Gig0/0/0

line console 0
 password cisco
 login
line vty 0 4
 password cisco
 login

end
write memory
```

---

## ⚙️ Step 4: Configure Core Switch (10 min)

Click switch → CLI tab → Copy/paste:

```cisco
enable
configure terminal
hostname City-Core-Switch
enable secret class

ipv6 unicast-routing

vlan 10
 name Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management

interface GigabitEthernet0/1
 no switchport
 ip address 10.0.0.2 255.255.255.252
 ipv6 address 2001:DB8:CITY:0::2/64
 no shutdown

interface GigabitEthernet0/2
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

interface GigabitEthernet0/3
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

interface GigabitEthernet0/4
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

interface FastEthernet0/3
 switchport mode access
 switchport access vlan 20
 no shutdown

interface range FastEthernet0/4-10
 switchport mode access
 switchport access vlan 10
 no shutdown

interface Vlan10
 ip address 10.10.10.1 255.255.255.0
 ipv6 address 2001:DB8:CITY:10::1/64
 no shutdown

interface Vlan20
 ip address 10.10.20.1 255.255.255.0
 ipv6 address 2001:DB8:CITY:20::1/64
 no shutdown

interface Vlan30
 ip address 10.10.30.1 255.255.255.0
 ipv6 address 2001:DB8:CITY:30::1/64
 no shutdown

interface Vlan99
 ip address 10.10.99.1 255.255.255.0
 ipv6 address 2001:DB8:CITY:99::1/64
 no shutdown

ip route 0.0.0.0 0.0.0.0 10.0.0.1
ipv6 route ::/0 2001:DB8:CITY:0::1

ip access-list extended BLOCK-PUBLIC-TO-ADMIN
 permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
 permit ip any any

interface Vlan20
 ip access-group BLOCK-PUBLIC-TO-ADMIN in

ipv6 access-list BLOCK-PUBLIC-TO-ADMIN-V6
 permit udp 2001:DB8:CITY:20::/64 host 2001:DB8:CITY:10::10 eq 53
 permit tcp 2001:DB8:CITY:20::/64 host 2001:DB8:CITY:10::10 eq 53
 deny ipv6 2001:DB8:CITY:20::/64 2001:DB8:CITY:10::/64
 permit ipv6 any any

interface Vlan20
 ipv6 traffic-filter BLOCK-PUBLIC-TO-ADMIN-V6 in

end
write memory
```

---

## ⚙️ Step 5: Configure District Switches (3 min)

**Downtown-Switch:**
```cisco
enable
configure terminal
hostname Downtown-Switch
vlan 20,99
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-4
 switchport mode access
 switchport access vlan 20
end
write memory
```

**Park-Switch:**
```cisco
enable
configure terminal
hostname Park-Switch
vlan 30,99
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-3
 switchport mode access
 switchport access vlan 30
end
write memory
```

**Residential-Switch:**
```cisco
enable
configure terminal
hostname Residential-Switch
vlan 30,99
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-3
 switchport mode access
 switchport access vlan 30
end
write memory
```

---

## 🖥️ Step 6: Configure Servers (10 min)

Click each server → Desktop → IP Configuration

### **Central-Office-Server:**
```
IPv4: 10.10.20.50 / 255.255.255.0
Gateway: 10.10.20.1
DNS: 10.10.10.10
IPv6: 2001:DB8:CITY:20::50/64
Gateway: 2001:DB8:CITY:20::1
```

### **DNS-Server:**
```
IPv4: 10.10.10.10 / 255.255.255.0
Gateway: 10.10.10.1
DNS: 10.10.10.10
IPv6: 2001:DB8:CITY:10::10/64
Gateway: 2001:DB8:CITY:10::1
```

**Desktop → Services → DNS:**
- Turn ON
- Add A Records:
  - smartcity.local → 10.10.10.30
  - dns.smartcity.local → 10.10.10.10
  - dhcp.smartcity.local → 10.10.10.20
  - web.smartcity.local → 10.10.10.30
  - mail.smartcity.local → 10.10.10.40
  - centraloffice.smartcity.local → 10.10.20.50

- **If AAAA records available**, add IPv6 versions (same names, IPv6 IPs)

### **DHCP-Server:**
```
IPv4: 10.10.10.20 / 255.255.255.0
Gateway: 10.10.10.1
DNS: 10.10.10.10
IPv6: 2001:DB8:CITY:10::20/64
Gateway: 2001:DB8:CITY:10::1
```

**Desktop → Services → DHCP:**
- Pool: AdminPool
  - Default Gateway: 10.10.10.1
  - DNS Server: 10.10.10.10
  - Start IP: 10.10.10.100
  - Subnet Mask: 255.255.255.0
  - Max Users: 50

- Pool: PublicPool
  - Default Gateway: 10.10.20.1
  - DNS Server: 10.10.10.10
  - Start IP: 10.10.20.100
  - Subnet Mask: 255.255.255.0
  - Max Users: 100

- Pool: IoTPool
  - Default Gateway: 10.10.30.1
  - DNS Server: 10.10.10.10
  - Start IP: 10.10.30.100
  - Subnet Mask: 255.255.255.0
  - Max Users: 50

**Note:** If DHCPv6 option exists, configure similar pools for IPv6. If not, skip (use SLAAC).

### **Web-Server:**
```
IPv4: 10.10.10.30 / 255.255.255.0
Gateway: 10.10.10.1
DNS: 10.10.10.10
IPv6: 2001:DB8:CITY:10::30/64
Gateway: 2001:DB8:CITY:10::1
```

**Desktop → Services → HTTP:**
- Turn ON
- Edit index.html: "Smart City Dashboard"

### **SMTP-Server:**
```
IPv4: 10.10.10.40 / 255.255.255.0
Gateway: 10.10.10.1
DNS: 10.10.10.10
IPv6: 2001:DB8:CITY:10::40/64
Gateway: 2001:DB8:CITY:10::1
```

**Desktop → Services → EMAIL:**
- Domain: smartcity.local
- Create user: admin@smartcity.local (password: admin)

---

## 💻 Step 7: Configure PCs (5 min)

Click each PC → Desktop → IP Configuration → **DHCP**

**Or manually:**

**Admin-PC-1 & Admin-PC-2:**
```
DHCP (or manual: 10.10.10.100-101, gateway 10.10.10.1, DNS 10.10.10.10)
IPv6: Auto (SLAAC) or manual 2001:DB8:CITY:10::100/64
```

**Public-Kiosk-PC:**
```
DHCP (should get 10.10.20.x)
```

**Resident-Home-PC:**
```
DHCP (should get 10.10.30.x)
```

---

## 📱 Step 8: Configure Wireless (5 min)

### **Public-WiFi-AP:**
Click AP → GUI tab:
```
SSID: City-Public-WiFi
Security: WPA2-PSK
Passphrase: publicaccess
```
Setup → Network Setup → DHCP

### **Residential-WiFi-AP:**
```
SSID: Residential-Network
Security: WPA2-PSK
Passphrase: homeaccess
```
Setup → Network Setup → DHCP

### **Smartphone:**
- Desktop → PC Wireless → Connect to "City-Public-WiFi" (password: publicaccess)
- Should get IP via DHCP

---

## 🤖 Step 9: Configure IoT (5 min)

**Smart-Streetlight:**

Desktop → IP Configuration:
```
IPv4: Static 10.10.30.20 / 255.255.255.0
Gateway: 10.10.30.1
DNS: 10.10.10.10
```

**Park-IoT-Gateway:**

Desktop → IP Configuration:
```
IPv4: Static 10.10.30.10 / 255.255.255.0
Gateway: 10.10.30.1
DNS: 10.10.10.10
```

Desktop → Programming (Blockly):

```
WHEN Motion Sensor (D0) IS ACTIVATED
 THEN IoT Device (10.10.30.20) SET brightness TO 1023
 WAIT 60 seconds
 THEN IoT Device (10.10.30.20) SET brightness TO 0
 AND SEND EMAIL
   TO: admin@smartcity.local
   FROM: iot@smartcity.local
   SUBJECT: "Park Alert"
   MESSAGE: "Motion detected - Light activated"
   SMTP Server: 10.10.10.40
```

**Note:** Smart LED is network-connected, control it via IP (10.10.30.20) not GPIO.

---

## ✅ Step 10: Test Everything (10 min)

### **From Admin-PC-1 (Command Prompt):**

```cmd
ping 10.10.10.1
ping 10.10.20.1
ping 10.10.30.1
ping 8.8.8.8
ping 10.10.10.10
ping 2001:DB8:CITY:10::1
ping 2001:DB8:CITY:10::10
nslookup smartcity.local
```

### **From Public-Kiosk-PC:**
```cmd
ping 10.10.10.1    (should FAIL - ACL blocked)
ping 10.10.10.10   (should work - DNS allowed)
```

### **Web Browser Test:**
- Open browser on any PC
- Navigate to: http://smartcity.local
- Should see Smart City Dashboard

### **VoIP Test:**
- Click City-Hall-Phone
- Dial Info-Line-Phone number
- Should connect

### **ACL Security Test:**
From Public-Kiosk-PC:
```
nslookup smartcity.local  → Should WORK (DNS allowed)
ping 10.10.10.10          → Should FAIL (ICMP blocked)
ping 10.10.10.1           → Should FAIL (Admin VLAN blocked)
```

### **IoT Test:**
- Verify Smart-Streetlight has IP: 10.10.30.20 (ping from Admin-PC)
- Click Park-Motion-Sensor
- Activate it
- Watch Smart-Streetlight turn on (blue, full brightness 1023)
- Wait 60 seconds - should turn off (brightness 0)
- Check email on SMTP server for alert

---

## 🎯 Quick Troubleshooting

| Problem | Fix |
|---------|-----|
| Links stay orange | Wait 30 seconds, then check cables |
| No DHCP IP | Check DHCP server is ON, verify VLAN assignment |
| Can't ping gateway | Check VLAN interface is "no shutdown" |
| ACL not blocking | Verify ACL applied to Vlan20 interface |
| IPv6 not working | Check "ipv6 unicast-routing" enabled |
| IoT not emailing | Verify SMTP server IP, check IoT has DNS |
| DNS not resolving | Check DNS service is ON, records added |

---

## 📊 Time Breakdown

- Device placement: 5 min
- Cabling: 10 min
- Router config: 5 min
- Core switch: 10 min
- District switches: 3 min
- Servers: 10 min
- PCs: 5 min
- Wireless: 5 min
- IoT: 5 min
- Testing: 10 min

**Total: ~70 minutes (1-2 hours including troubleshooting)**

---

## ✨ You're Done!

Your smart city network is complete with:
- ✅ 23 devices
- ✅ 4 VLANs with segmentation
- ✅ Dual-stack IPv4/IPv6
- ✅ IoT automation
- ✅ Security ACLs
- ✅ Wireless & cellular
- ✅ All services operational

**Save your project and test all features!**
