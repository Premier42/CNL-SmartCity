# 🚀 MANUAL SETUP PROGRESS TRACKER

**Date:** 2025-10-18
**File:** connection.pkt (original with physical connections only)

---

## ✅ COMPLETED SECTIONS

### ✅ SECTION 1: ROUTER CONFIGURATION (DONE)

**Device:** City-Gateway-Router

**Commands Executed:**
```
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
exit

interface GigabitEthernet0/0/1
ip address 10.0.0.1 255.255.255.252
ip nat inside
ipv6 address autoconfig
ipv6 enable
no shutdown
exit

ip nat inside source list 1 interface GigabitEthernet0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255
ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0/0

line console 0
password cisco
login
exit

line vty 0 4
password cisco
login
exit

end
write memory
```

**Verification:**
```
Router#show ip interface brief
GigabitEthernet0/0/0   unassigned      YES DHCP   up   down  ✅
GigabitEthernet0/0/1   10.0.0.1        YES manual up   up    ✅
```

**Status:** ✅ COMPLETE

---

### ✅ SECTION 2: CORE SWITCH CONFIGURATION (IN PROGRESS)

**Device:** City-Core-Switch

**Commands Executed So Far:**
```
enable
configure terminal
hostname City-Core-Switch
enable secret class
ipv6 unicast-routing

vlan 10
name Admin
exit
vlan 20
name Public
exit
vlan 30
name IoT
exit
vlan 99
name Management
exit

interface GigabitEthernet1/0/1
no switchport
ip address 10.0.0.2 255.255.255.252
ipv6 enable
no shutdown
exit

interface GigabitEthernet1/0/2
description Trunk to Downtown-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit

interface GigabitEthernet1/0/3
description Trunk to Park-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit

interface GigabitEthernet1/0/4
description Trunk to Residential-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit

interface GigabitEthernet1/0/5
description Central Office Server - Cellular Backhaul
switchport mode access
switchport access vlan 20
no shutdown
exit

interface range GigabitEthernet1/0/6-9
description Servers (DNS, DHCP, Web, SMTP)
switchport mode access
switchport access vlan 10
no shutdown
exit

interface range GigabitEthernet1/0/10-12
description Admin Devices (PCs and Phone)
switchport mode access
switchport access vlan 10
no shutdown
exit
```

**Verification Done:**
```
City-Core-Switch#show vlan brief
VLAN 10 (Admin)   ✅
VLAN 20 (Public)  ✅
VLAN 30 (IoT)     ✅
VLAN 99 (Management) ✅

City-Core-Switch#show interfaces trunk
Gig1/0/2: trunking, native 99, VLANs 10,20,30,99 ✅
Gig1/0/3: trunking, native 99, VLANs 10,20,30,99 ✅
Gig1/0/4: trunking, native 99, VLANs 10,20,30,99 ✅

City-Core-Switch#show ip interface brief
Gig1/0/1: 10.0.0.2 up/up ✅
```

**Status:** 🔄 IN PROGRESS

---

## 🔄 NEXT STEPS

### SECTION 2: CORE SWITCH - REMAINING TASKS

**Step 11: Configure VLAN Interfaces (SVIs) - NEXT**
```
interface Vlan10
description Admin VLAN Gateway
ip address 10.10.10.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan20
description Public VLAN Gateway
ip address 10.10.20.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan30
description IoT VLAN Gateway
ip address 10.10.30.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan99
description Management VLAN Gateway
ip address 10.10.99.1 255.255.255.0
ipv6 enable
no shutdown
exit
```

**Step 12: Configure Default Route**
```
ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

**Step 13: Configure Security ACL**
```
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
permit ip any any
exit
```

**Step 14: Apply ACL**
```
interface Vlan20
ip access-group BLOCK-PUBLIC-TO-ADMIN in
exit
```

**Step 15: Save Configuration**
```
end
write memory
```

---

### SECTION 3: DOWNTOWN-SWITCH

**Device:** Downtown-Switch

**Commands to Execute:**
```
enable
configure terminal
hostname Downtown-Switch

vlan 20
name Public
exit
vlan 99
name Management
exit

interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit

interface range FastEthernet0/2-4
description Public VLAN Access Ports
switchport mode access
switchport access vlan 20
no shutdown
exit

end
write memory
```

---

### SECTION 4: PARK-SWITCH

**Device:** Park-Switch

**Commands to Execute:**
```
enable
configure terminal
hostname Park-Switch

vlan 30
name IoT
exit
vlan 99
name Management
exit

interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit

interface range FastEthernet0/2-3
description IoT VLAN Access Ports
switchport mode access
switchport access vlan 30
no shutdown
exit

end
write memory
```

---

### SECTION 5: RESIDENTIAL-SWITCH

**Device:** Residential-Switch

**Commands to Execute:**
```
enable
configure terminal
hostname Residential-Switch

vlan 30
name IoT
exit
vlan 99
name Management
exit

interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit

interface range FastEthernet0/2-3
description IoT VLAN Access Ports
switchport mode access
switchport access vlan 30
no shutdown
exit

end
write memory
```

---

### SECTION 6: SERVER IP CONFIGURATION (GUI)

**DNS-Server:**
- Config → FastEthernet0
- IP: 10.10.10.10
- Subnet: 255.255.255.0
- Gateway: 10.10.10.1
- DNS: 10.10.10.10

**DHCP-Server:**
- Config → FastEthernet0
- IP: 10.10.10.20
- Subnet: 255.255.255.0
- Gateway: 10.10.10.1
- DNS: 10.10.10.10

**Web-Server:**
- Config → FastEthernet0
- IP: 10.10.10.30
- Subnet: 255.255.255.0
- Gateway: 10.10.10.1
- DNS: 10.10.10.10

**SMTP-Server:**
- Config → FastEthernet0
- IP: 10.10.10.40
- Subnet: 255.255.255.0
- Gateway: 10.10.10.1
- DNS: 10.10.10.10

---

### SECTION 7: DHCP POOLS CONFIGURATION (GUI)

**DHCP-Server → Services → DHCP**

**Enable Service:** ON

**Pool 1: AdminPool**
- Pool Name: AdminPool
- Default Gateway: 10.10.10.1
- DNS Server: 10.10.10.10
- Start IP: 10.10.10.100
- Subnet Mask: 255.255.255.0
- Max Users: 50
- Click [Add]

**Pool 2: PublicPool**
- Pool Name: PublicPool
- Default Gateway: 10.10.20.1
- DNS Server: 10.10.10.10
- Start IP: 10.10.20.100
- Subnet Mask: 255.255.255.0
- Max Users: 100
- Click [Add]

**Pool 3: IoTPool**
- Pool Name: IoTPool
- Default Gateway: 10.10.30.1
- DNS Server: 10.10.10.10
- Start IP: 10.10.30.100
- Subnet Mask: 255.255.255.0
- Max Users: 50
- Click [Add]

---

### SECTION 8: DNS RECORDS CONFIGURATION (GUI)

**DNS-Server → Services → DNS**

**Enable Service:** ON

**Add Records:**
1. smartcity.local → 10.10.10.30
2. dns.smartcity.local → 10.10.10.10
3. mail.smartcity.local → 10.10.10.40
4. dhcp.smartcity.local → 10.10.10.20
5. www.smartcity.local → 10.10.10.30

---

### SECTION 9: CLIENT PC CONFIGURATION (GUI)

**Admin-PC-1:** Desktop → IP Configuration → DHCP
**Admin-PC-2:** Desktop → IP Configuration → DHCP
**Public-Kiosk-PC:** Desktop → IP Configuration → DHCP
**Resident-Home-PC:** Desktop → IP Configuration → DHCP

---

### SECTION 10: ADDITIONAL DEVICES (GUI)

**Central-Office-Server:**
- Desktop → IP Configuration → Static
- IP: 10.10.20.50
- Subnet: 255.255.255.0
- Gateway: 10.10.20.1
- DNS: 10.10.10.10

**Park-IoT-Gateway:**
- Config → Ethernet0
- IP: 10.10.30.10
- Subnet: 255.255.255.0
- Gateway: 10.10.30.1
- DNS: 10.10.10.10

---

## 📊 OVERALL PROGRESS

- [x] Section 1: Router ✅
- [ ] Section 2: Core Switch (70% done)
  - [x] Basic config ✅
  - [x] VLANs ✅
  - [x] Router link ✅
  - [x] Trunk ports ✅
  - [x] Access ports ✅
  - [ ] VLAN interfaces (SVIs) - NEXT
  - [ ] Routing - NEXT
  - [ ] ACLs - NEXT
- [ ] Section 3: Downtown-Switch
- [ ] Section 4: Park-Switch
- [ ] Section 5: Residential-Switch
- [ ] Section 6: Server IPs
- [ ] Section 7: DHCP Pools
- [ ] Section 8: DNS Records
- [ ] Section 9: Client PCs
- [ ] Section 10: Additional Devices

**Estimated Time Remaining:** ~35 minutes

---

## 🎯 CURRENT STATUS

**Currently working on:** Core Switch VLAN Interfaces (SVIs)
**Next command to execute:** Configure Vlan10 interface
**Ready to continue:** YES

---

**Last Updated:** 2025-10-18
