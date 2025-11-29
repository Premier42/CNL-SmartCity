# Actual Network Topology - From Your PKT File

## Network Discovered from connection.pkt

### Physical Connections:

```
Router (ISR 4331)
└─ GigabitEthernet0/0/1 (IP: 10.0.0.1/30)
    │
    └─ Connected to City-Core-Switch
            │
            ├─ GigabitEthernet1/0/1 (IP: 10.0.0.2/30) → TO ROUTER
            ├─ GigabitEthernet1/0/2 → TO Downtown-Switch
            ├─ GigabitEthernet1/0/3 → TO Park-Switch
            ├─ GigabitEthernet1/0/4 → TO Residential-Switch
            ├─ GigabitEthernet1/0/5 → TO Wireless Router/Cell Tower
            └─ GigabitEthernet1/0/6-11 → TO Servers & End Devices

Downtown-Switch
└─ FastEthernet0/1 → FROM City-Core-Switch Gi1/0/2

Park-Switch
└─ FastEthernet0/1 → FROM City-Core-Switch Gi1/0/3

Residential-Switch
└─ FastEthernet0/1 → FROM City-Core-Switch Gi1/0/4
```

---

## Router Configuration

### Current Router Interfaces:
- **GigabitEthernet0/0/0** - NAT Outside (ISP connection)
- **GigabitEthernet0/0/1** - IP: 10.0.0.1/30 (connects to City-Core-Switch)

### Current Router Config:
```cisco
hostname Router
enable secret (encrypted)
line con 0 password: cisco
line vty 0 4 password: cisco

interface GigabitEthernet0/0/0
 no ip address
 ip nat outside
 ipv6 address autoconfig
 ipv6 enable

interface GigabitEthernet0/0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 ipv6 address autoconfig
 ipv6 enable
```

---

## City-Core-Switch Configuration

### Connected Interfaces:
- **GigabitEthernet1/0/1** - IP: 10.0.0.2/30 (connects to Router)
- **GigabitEthernet1/0/2** - Trunk to Downtown-Switch
- **GigabitEthernet1/0/3** - Trunk to Park-Switch
- **GigabitEthernet1/0/4** - Trunk to Residential-Switch
- **GigabitEthernet1/0/5** - To Wireless Router
- **GigabitEthernet1/0/6-11** - Server/PC connections

---

## Current IP Scheme:

### Management Link:
- Router Gi0/0/1: 10.0.0.1/30
- City-Core-Switch Gi1/0/1: 10.0.0.2/30

### VLANs (from servers):
- **VLAN 10**: 10.10.10.0/24 (Servers/Admin)
  - DNS: 10.10.10.10
  - DHCP: 10.10.10.20
  - Web: 10.10.10.40
  - SMTP: 10.10.10.30

- **VLAN 20**: 10.10.20.0/24 (Public Access)

- **VLAN 30**: 10.10.30.0/24 (IoT Devices)

---

## What's Missing:

### On Router:
❌ No subinterfaces configured for VLANs
❌ No inter-VLAN routing
❌ No DHCP helper addresses
❌ No ACLs

### On City-Core-Switch:
❌ Need to verify VLAN configuration
❌ Need to verify trunk configuration

### On Access Switches:
❌ Need to verify VLAN configuration
❌ Need to verify access port assignments

---

## CORRECTED Configuration Commands Coming Next...
