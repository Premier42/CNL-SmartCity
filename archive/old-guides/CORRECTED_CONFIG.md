# CORRECTED Configuration - Based on YOUR Actual Network

## ✅ VERIFIED Network Information

**Router Name:** City-Gateway-Router (ISR4321)
**Router Password:** cisco
**Current Connection:** GigabitEthernet0/0/1 → City-Core-Switch Gi1/0/1

---

## STEP 1: Configure City-Gateway-Router (CORRECTED)

### How to Access:
1. Click on **"City-Gateway-Router"** (or device labeled "Router")
2. Click **"CLI" tab**
3. Password: `cisco`
4. Type: `enable`
5. Password: `cisco` (or just press Enter)

### Complete Router Configuration (Copy ALL):

```cisco
enable
configure terminal

! Change hostname
hostname SmartCity-Router

! Enable IPv6
ipv6 unicast-routing

! IMPORTANT: Your router's main interface is Gi0/0/1 (connects to switch)
! We'll create subinterfaces on this for VLANs

interface GigabitEthernet0/0/1
 description "Trunk to City-Core-Switch"
 no ip address
 no shutdown
exit

! Subinterface for VLAN 10 (Servers/Admin)
interface GigabitEthernet0/0/1.10
 description "VLAN 10 - Servers and Admin"
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
 ipv6 address 2001:DB8:10::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

! Subinterface for VLAN 20 (Public)
interface GigabitEthernet0/0/1.20
 description "VLAN 20 - Public Access"
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
 ipv6 address 2001:DB8:20::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

! Subinterface for VLAN 30 (IoT)
interface GigabitEthernet0/0/1.30
 description "VLAN 30 - IoT Devices"
 encapsulation dot1Q 30
 ip address 10.10.30.1 255.255.255.0
 ipv6 address 2001:DB8:30::1/64
 ip helper-address 10.10.10.20
 no shutdown
exit

! Configure ACLs for Security
! Note: "log" keyword removed - not supported in Packet Tracer
access-list 110 permit ip 10.10.30.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 110 deny ip 10.10.30.0 0.0.0.255 10.10.20.0 0.0.0.255
access-list 110 permit ip any any

access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 80
access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 443
access-list 120 permit udp 10.10.20.0 0.0.0.255 10.10.10.10 0.0.0.0 eq 53
access-list 120 permit tcp 10.10.20.0 0.0.0.255 10.10.10.30 0.0.0.0 eq 25
access-list 120 deny ip 10.10.20.0 0.0.0.255 10.10.30.0 0.0.0.255
access-list 120 permit ip any any

! Apply ACLs
interface GigabitEthernet0/0/1.30
 ip access-group 110 in
exit

interface GigabitEthernet0/0/1.20
 ip access-group 120 in
exit

write memory
```

---

## STEP 2: Configure City-Core-Switch (CORRECTED)

### How to Access:
1. Click on **"City-Core-Switch"**
2. Click **"CLI" tab**
3. Password: cisco (if asked)

### Complete Switch Configuration:

```cisco
enable
configure terminal
hostname City-Core-Switch

! Create VLANs
vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management
exit

! Trunk to Router (YOUR actual connection!)
! Note: 3650 switch doesn't need "switchport trunk encapsulation" - only supports 802.1Q
interface GigabitEthernet1/0/1
 description "Trunk to City-Gateway-Router"
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
exit

! Trunk to Downtown-Switch
interface GigabitEthernet1/0/2
 description "Trunk to Downtown-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 20,99
 no shutdown
exit

! Trunk to Park-Switch
interface GigabitEthernet1/0/3
 description "Trunk to Park-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 30,99
 no shutdown
exit

! Trunk to Residential-Switch
interface GigabitEthernet1/0/4
 description "Trunk to Residential-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! Server/PC connections - VLAN 10
! (Check which Gi ports have servers connected - likely Gi1/0/6-11)
interface range GigabitEthernet1/0/6-11
 description "Server and PC connections - VLAN 10"
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 3: Configure Downtown-Switch

### How to Access:
1. Click on **"Downtown-Switch"**
2. Click **"CLI" tab**

### Configuration:

```cisco
enable
configure terminal
hostname Downtown-Switch

! Create VLANs
vlan 20
 name Public
vlan 99
 name Management
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description "Trunk to City-Core-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 20,99
 no shutdown
exit

! Public Access Ports
interface range FastEthernet0/2-10
 description "Public Access - VLAN 20"
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 4: Configure Park-Switch

### How to Access:
1. Click on **"Park-Switch"**
2. Click **"CLI" tab**

### Configuration:

```cisco
enable
configure terminal
hostname Park-Switch

! Create VLANs
vlan 30
 name IoT
vlan 99
 name Management
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description "Trunk to City-Core-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 30,99
 no shutdown
exit

! IoT Device Ports
interface range FastEthernet0/2-10
 description "IoT Devices - VLAN 30"
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 5: Configure Residential-Switch

### How to Access:
1. Click on **"Residential-Switch"**
2. Click **"CLI" tab**

### Configuration:

```cisco
enable
configure terminal
hostname Residential-Switch

! Create VLANs
vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 99
 name Management
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description "Trunk to City-Core-Switch"
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! Admin Devices - VLAN 10
interface range FastEthernet0/2-5
 description "Admin Devices - VLAN 10"
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
exit

! Residential/Public - VLAN 20
interface range FastEthernet0/6-10
 description "Residential - VLAN 20"
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## Verification Commands

### On Router:
```cisco
show ip interface brief
show ip route
show access-lists
show running-config
```

### On Switches:
```cisco
show vlan brief
show interfaces trunk
show running-config
```

---

## Key Differences from Original Guide:

| Original (WRONG) | Corrected (RIGHT) |
|-----------------|-------------------|
| Router name: "Router" | **"City-Gateway-Router"** |
| Interface: Gi0/0 | **GigabitEthernet0/0/1** |
| Subinterfaces: Gi0/0.10 | **GigabitEthernet0/0/1.10** |
| Switch trunk: Gi0/1 | **GigabitEthernet1/0/1** |

---

**Your network will work after this configuration!** 🎯
