# Quick Reference - Copy/Paste Commands

## How to Use This Guide

**For each section below:**
1. Find the device name in Packet Tracer (e.g., "Router", "City-Core-Switch")
2. Click on that device
3. Click the **CLI tab** at the top of the window
4. Copy ALL the commands in the code block
5. Paste into the CLI (right-click and paste, or Ctrl+V)
6. Press Enter

---

## 1. Router Configuration

**Device to click in Packet Tracer:** "Router"
**Where to paste:** Click Router → Click "CLI" tab → Paste below commands

```cisco
enable
configure terminal
hostname SmartCity-Router
ipv6 unicast-routing

interface GigabitEthernet0/0
 description "Trunk to City-Core-Switch"
 no shutdown
exit

interface GigabitEthernet0/0.10
 description "VLAN 10 - Servers and Admin"
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
 ipv6 address 2001:DB8:10::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

interface GigabitEthernet0/0.20
 description "VLAN 20 - Public Access"
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
 ipv6 address 2001:DB8:20::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

interface GigabitEthernet0/0.30
 description "VLAN 30 - IoT Devices"
 encapsulation dot1Q 30
 ip address 10.10.30.1 255.255.255.0
 ipv6 address 2001:DB8:30::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

access-list 110 permit ip 10.10.30.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 110 deny ip 10.10.30.0 0.0.0.255 10.10.20.0 0.0.0.255 log
access-list 110 permit ip any any

access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 80
access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 443
access-list 120 permit udp 10.10.20.0 0.0.0.255 10.10.10.10 0.0.0.0 eq 53
access-list 120 permit tcp 10.10.20.0 0.0.0.255 10.10.10.30 0.0.0.0 eq 25
access-list 120 deny ip 10.10.20.0 0.0.0.255 10.10.30.0 0.0.0.255 log
access-list 120 permit ip any any

interface GigabitEthernet0/0.30
 ip access-group 110 in
exit

interface GigabitEthernet0/0.20
 ip access-group 120 in
exit

write memory
```

## 2. City-Core-Switch Configuration

**Device to click in Packet Tracer:** "City-Core-Switch"
**Where to paste:** Click City-Core-Switch → Click "CLI" tab → Paste below commands

```cisco
enable
configure terminal
hostname City-Core-Switch

vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management
exit

interface GigabitEthernet0/1
 description "Trunk to SmartCity-Router"
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
exit

interface range FastEthernet0/1-4
 description "Servers - VLAN 10"
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## 3. Server IP Addresses

**How to configure servers:**
- Click server device (e.g., "DNS-Server")
- Click **"Desktop" tab**
- Click **"IP Configuration"**
- Enter the values from table below

| Server | IP | Gateway | DNS |
|--------|------------|------------|-----------|
| DNS    | 10.10.10.10 | 10.10.10.1 | 10.10.10.10 |
| DHCP   | 10.10.10.20 | 10.10.10.1 | 10.10.10.10 |
| Web    | 10.10.10.40 | 10.10.10.1 | 10.10.10.10 |
| SMTP   | 10.10.10.30 | 10.10.10.1 | 10.10.10.10 |

---

## 4. DNS Records to Add

**Where to add:**
- Click "DNS-Server" → Click "Services" tab → Click "DNS"
- Turn DNS Service ON
- Add these records one by one:

```
smartcity-router.local  → 10.10.10.1
dns.smartcity.local     → 10.10.10.10
dhcp.smartcity.local    → 10.10.10.20
web.smartcity.local     → 10.10.10.40
mail.smartcity.local    → 10.10.10.30
```

---

## 5. DHCP Pools to Create

**Where to add:**
- Click "DHCP-Server" → Click "Services" tab → Click "DHCP"
- Turn DHCP Service ON
- Create these 3 pools (click "Add" after each):

**Pool 1 - AdminPool:**
- Gateway: 10.10.10.1
- DNS: 10.10.10.10
- Start IP: 10.10.10.100
- Subnet: 255.255.255.0
- Max Users: 50

**Pool 2 - PublicPool:**
- Gateway: 10.10.20.1
- DNS: 10.10.10.10
- Start IP: 10.10.20.100
- Subnet: 255.255.255.0
- Max Users: 100

**Pool 3 - IoTPool:**
- Gateway: 10.10.30.1
- DNS: 10.10.10.10
- Start IP: 10.10.30.100
- Subnet: 255.255.255.0
- Max Users: 50

---

## 6. Email Users to Create

**Where to add:**
- Click "SMTP-Server" → Click "Services" tab → Click "EMAIL"
- Turn Email Service ON
- Set Domain: smartcity.local
- Add these users:

```
admin       / admin123
operations  / ops123
support     / support123
public      / public123
```

---

## 7. Testing Commands

**Where to run these:**
- Click any PC device (e.g., "Admin-PC-1")
- Click "Desktop" tab
- Click "Command Prompt"
- Type these commands:

**Ping tests:**
```
ping 10.10.10.1
ping 10.10.10.10
ping web.smartcity.local
```

**DNS lookup:**
```
nslookup web.smartcity.local
nslookup mail.smartcity.local
```

**DHCP:**
```
ipconfig /all
ipconfig /release
ipconfig /renew
```
