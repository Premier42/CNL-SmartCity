# Smart City IoT Network - Implementation Guide

## Step-by-Step Cisco Packet Tracer Project

### Project Overview

Build a **complex engineering network** demonstrating IPv4/IPv6 dual-stack, VLANs, ACLs, DHCP, DNS, and IoT integration for a smart city infrastructure.

**Technologies Used**: IPv4/IPv6, DNS, ACL, DHCP, IoT devices, Smartphones, Laptops, Desktops, Servers, Wireless Routers, Routers, Switches

---

## Prerequisites

**Cisco Packet Tracer Version**: 8.2.1 or newer (recommended)

**Required Knowledge**: Basic networking, Cisco IOS commands, VLAN concepts

**Estimated Time**: 2-3 hours

---

## Step 1: Device Placement (15 minutes)

### Core Infrastructure

1. **Add Core Router**:
   - Device: **ISR4331** (preferred) or **2911** if ISR4331 unavailable
   - Position: Center of workspace
   - Label: `Core-Router`

2. **Add Distribution Switches** (2 devices):
   - Device: **Catalyst 3650-24PS** (preferred) or **2960-24TT**
   - Position: Below core router
   - Labels: `Dist-SW-A`, `Dist-SW-B`

3. **Add Access Switches** (5 devices):
   - Device: **Catalyst 2960** (24-port model)
   - Position: Below distribution switches
   - Labels: `Access-SW1`, `Access-SW2`, `Access-SW3`, `Access-SW4`, `Access-SW5`

4. **Add Servers** (3 devices):
   - Device: **Server-PT** (Generic Server)
   - Connect to: Access-SW1
   - Labels: `DNS-Server`, `DHCP-Server`, `Email-Server`

5. **Add Wireless Access Points** (2 devices):
   - Device: **AccessPoint-PT** or **Linksys WRT300N**
   - Connect to: Access-SW4 and Access-SW5
   - Labels: `WiFi-Zone1`, `WiFi-Zone2`

---

## Step 2: Physical Connections (10 minutes)

### Core to Distribution

- Core-Router `GigabitEthernet0/0/0` ↔ Dist-SW-A `GigabitEthernet1/0/1`
- Core-Router `GigabitEthernet0/0/1` ↔ Dist-SW-B `GigabitEthernet1/0/1`

### Distribution to Access

**Dist-SW-A connections:**

- `FastEthernet1/0/1` ↔ Access-SW1 `FastEthernet0/24` (Servers)
- `FastEthernet1/0/2` ↔ Access-SW2 `FastEthernet0/24` (IoT Sensors)
- `FastEthernet1/0/3` ↔ Access-SW3 `FastEthernet0/24` (Admin PCs)

**Dist-SW-B connections:**

- `FastEthernet1/0/1` ↔ Access-SW4 `FastEthernet0/24` (WiFi Zone 1)
- `FastEthernet1/0/2` ↔ Access-SW5 `FastEthernet0/24` (WiFi Zone 2 + Mobile Admin)

### End Device Connections

**Access-SW1 (Servers):**

- `FastEthernet0/1` → DNS Server
- `FastEthernet0/2` → DHCP Server
- `FastEthernet0/3` → Email Server

**Access-SW2 (IoT - 8 devices):**

- `FastEthernet0/1-3` → Traffic Sensors (3x IoT-PT devices)
- `FastEthernet0/4-5` → Environmental Monitors (2x IoT-PT devices)
- `FastEthernet0/6-7` → Smart Cameras (2x IoT-PT devices)
- `FastEthernet0/8` → Smart Lighting Controller (1x IoT-PT device)

**Access-SW3 (Admin - 4 devices):**

- `FastEthernet0/1-2` → Admin PCs (2x PC-PT)
- `FastEthernet0/3-4` → Admin Laptops (2x Laptop-PT)

**Access-SW4 (WiFi Zone 1):**

- `FastEthernet0/1` → WiFi-Zone1

**Access-SW5 (WiFi Zone 2 + Mobile Admin):**

- `FastEthernet0/1` → WiFi-Zone2
- `FastEthernet0/2-4` → Mobile Admin devices (3x Tablet-PT)

**Wireless Connections:**

- Connect 3x Smartphone-PT and 2x Tablet-PT to WiFi networks

---

## Step 3: Core Router Configuration (20 minutes)

```cisco
enable
configure terminal
hostname Core-Router

! Enable IPv6 routing
ip routing
ipv6 unicast-routing

! Interface to Distribution A
interface GigabitEthernet0/0/0
 description "Link to Dist-SW-A"
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1000:1::1/64
 no shutdown

! Interface to Distribution B
interface GigabitEthernet0/0/1
 description "Link to Dist-SW-B"
 ip address 192.168.2.1 255.255.255.0
 ipv6 address 2001:db8:1000:2::1/64
 no shutdown

! VLAN 10 - IoT Sensors
interface GigabitEthernet0/0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64

! VLAN 20 - Administrative
interface GigabitEthernet0/0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64

! VLAN 30 - Public WiFi
interface GigabitEthernet0/0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64

! VLAN 40 - Servers
interface GigabitEthernet0/0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64

! VLAN 50 - Mobile Admin
interface GigabitEthernet0/0/1.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64

! DHCP Helper addresses
interface GigabitEthernet0/0/0.10
 ip helper-address 192.168.40.20
interface GigabitEthernet0/0/0.20
 ip helper-address 192.168.40.20
interface GigabitEthernet0/0/1.30
 ip helper-address 192.168.40.20
interface GigabitEthernet0/0/1.50
 ip helper-address 192.168.40.20

write memory
```

---

## Step 4: Switch Configuration (15 minutes)

### Distribution Switch A

```cisco
enable
configure terminal
hostname Dist-SW-A

! Create VLANs
vlan 10
 name IoT-Sensors
vlan 20
 name Administrative
vlan 40
 name Servers

! Trunk to Core Router
interface GigabitEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,40

! Trunks to Access Switches
interface FastEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 40
interface FastEthernet1/0/2
 switchport mode trunk
 switchport trunk allowed vlan 10
interface FastEthernet1/0/3
 switchport mode trunk
 switchport trunk allowed vlan 20

write memory
```

### Distribution Switch B

```cisco
enable
configure terminal
hostname Dist-SW-B

! Create VLANs
vlan 30
 name Public-WiFi
vlan 50
 name Mobile-Admin

! Trunk to Core Router
interface GigabitEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 30,50

! Trunks to Access Switches
interface FastEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 30
interface FastEthernet1/0/2
 switchport mode trunk
 switchport trunk allowed vlan 30,50

write memory
```

### Access Switch Configuration Template

```cisco
! Example for Access-SW1 (Servers)
enable
configure terminal
hostname Access-SW1

vlan 40
 name Servers

interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 40

interface range FastEthernet0/1-3
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast

write memory
```

**Apply similar configuration to remaining switches:**

- Access-SW2: VLAN 10 (IoT) - ports 1-8
- Access-SW3: VLAN 20 (Admin) - ports 1-4
- Access-SW4: VLAN 30 (WiFi) - port 1
- Access-SW5: VLAN 30,50 (WiFi + Mobile) - ports 1-4

---

## Step 5: Server Configuration (15 minutes)

### DNS Server

```text
IP Configuration:
├── IPv4: 192.168.40.10/24
├── IPv6: 2001:db8:1000:40::10/64
├── Gateway: 192.168.40.1
└── DNS: 192.168.40.10

DNS Records (Services > DNS):
├── core-router.smart-city.local → 192.168.1.1
├── dhcp.smart-city.local → 192.168.40.20
├── email.smart-city.local → 192.168.40.30
└── iot-sensor1.smart-city.local → 192.168.10.101
```

### DHCP Server

```text
IP Configuration:
├── IPv4: 192.168.40.20/24
├── IPv6: 2001:db8:1000:40::20/64
├── Gateway: 192.168.40.1
└── DNS: 192.168.40.10

DHCP Pools (Services > DHCP):
├── Pool Name: IoT_SENSORS
│   ├── Default Gateway: 192.168.10.1
│   ├── DNS Server: 192.168.40.10
│   ├── Start IP: 192.168.10.100
│   ├── Subnet Mask: 255.255.255.0
│   └── Max Users: 50
├── Pool Name: ADMIN_DEVICES
│   ├── Default Gateway: 192.168.20.1
│   ├── DNS Server: 192.168.40.10
│   ├── Start IP: 192.168.20.100
│   ├── Subnet Mask: 255.255.255.0
│   └── Max Users: 20
├── Pool Name: PUBLIC_WIFI
│   ├── Default Gateway: 192.168.30.1
│   ├── DNS Server: 192.168.40.10
│   ├── Start IP: 192.168.30.150
│   ├── Subnet Mask: 255.255.255.0
│   └── Max Users: 100
└── Pool Name: MOBILE_ADMIN
    ├── Default Gateway: 192.168.50.1
    ├── DNS Server: 192.168.40.10
    ├── Start IP: 192.168.50.100
    ├── Subnet Mask: 255.255.255.0
    └── Max Users: 20
```

### Email Server

```text
IP Configuration:
├── IPv4: 192.168.40.30/24
├── IPv6: 2001:db8:1000:40::30/64
├── Gateway: 192.168.40.1
└── DNS: 192.168.40.10

Email Service (Services > EMAIL):
├── Domain Name: smart-city.local
├── Users: admin@smart-city.local, operations@smart-city.local
└── Service: On (SMTP enabled)
```

---

## Step 6: Access Control Lists (ACLs) - (10 minutes)

Add to Core Router:

```cisco
! IoT Security ACL
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
access-list 110 permit ip any any

! Public WiFi Restrictions
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 80
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 443
access-list 130 permit udp 192.168.30.0 0.0.0.255 192.168.40.10 0.0.0.0 eq 53
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255 log
access-list 130 permit ip any any

! Apply ACLs
interface GigabitEthernet0/0/0.10
 ip access-group 110 in
interface GigabitEthernet0/0/1.30
 ip access-group 130 in
```

---

## Step 7: IoT Device Configuration (15 minutes)

### IoT Device Setup (8 devices)

Configure each IoT-PT device:

**Traffic Sensors (Ports 1-3 on Access-SW2):**

```text
Device: IoT-PT (Microcontroller Board)
Network Config: DHCP
Expected IP: 192.168.10.101-103
Programming: Python/Blockly
Function: Traffic monitoring simulation
```

**Environmental Monitors (Ports 4-5 on Access-SW2):**

```text
Device: IoT-PT (Environmental Monitor)
Network Config: DHCP
Expected IP: 192.168.10.104-105
Programming: Python/Blockly
Function: Temperature and air quality simulation
```

**Smart Cameras (Ports 6-7 on Access-SW2):**

```text
Device: IoT-PT (Security Camera)
Network Config: DHCP
Expected IP: 192.168.10.106-107
Programming: Python/Blockly
Function: Motion detection simulation
```

**Smart Lighting Controller (Port 8 on Access-SW2):**

```text
Device: IoT-PT (Smart Home Device)
Network Config: DHCP
Expected IP: 192.168.10.108
Programming: Python/Blockly
Function: Lighting control simulation
```

### IoT Programming Example

```python
# Example Python code for Traffic Sensor
import time
import random

def traffic_sensor():
    while True:
        vehicle_count = random.randint(10, 50)
        speed_avg = random.randint(25, 65)

        print(f"Vehicles: {vehicle_count}, Avg Speed: {speed_avg} mph")

        # Send data to server
        send_data(vehicle_count, speed_avg)
        time.sleep(30)

traffic_sensor()
```

---

## Step 8: Wireless Configuration (10 minutes)

### WiFi Access Point Setup

**WiFi-Zone1 Configuration:**

```text
Device: AccessPoint-PT or Linksys WRT300N
Network Tab:
├── Static IP: 192.168.30.50
├── Subnet Mask: 255.255.255.0
├── Default Gateway: 192.168.30.1
└── DNS Server: 192.168.40.10

Wireless Tab:
├── SSID: SmartCity_Zone1
├── Authentication: WPA2-PSK
├── PSK Pass Phrase: SmartCity2024
├── Channel: 6
└── SSID Broadcast: Enabled
```

**WiFi-Zone2 Configuration:**

```text
Device: AccessPoint-PT or Linksys WRT300N
Network Tab:
├── Static IP: 192.168.30.51
├── Subnet Mask: 255.255.255.0
├── Default Gateway: 192.168.30.1
└── DNS Server: 192.168.40.10

Wireless Tab:
├── SSID: SmartCity_Zone2
├── Authentication: WPA2-PSK
├── PSK Pass Phrase: SmartCity2024
├── Channel: 11
└── SSID Broadcast: Enabled
```

### Connect Mobile Devices

- 3x Smartphone-PT → Connect to WiFi networks
- 2x Tablet-PT → Connect to WiFi networks
- Password: SmartCity2024

---

## Step 9: Testing & Validation (10 minutes)

### Connectivity Tests

1. **IPv4 Ping Tests:**

   ```bash
   # From Admin PC
   ping 192.168.10.101    # IoT sensor
   ping 192.168.40.10     # DNS server

   # From IoT device (if CLI available)
   ping 192.168.40.10     # DNS server

   # From WiFi device
   ping 192.168.40.10     # Should work (DNS only)
   ping 192.168.10.101    # Should fail (blocked by ACL)
   ```

2. **DHCP Verification:**

   ```bash
   # Check device IP assignments
   ipconfig         # Windows devices
   ip addr show     # Linux devices

   # Verify DNS server assignment
   nslookup dhcp.smart-city.local
   nslookup email.smart-city.local
   ```

3. **ACL Security Tests:**

   ```bash
   # These should FAIL (blocked by ACL)
   # From WiFi device to IoT network
   ping 192.168.10.101

   # These should PASS (allowed)
   # From IoT to Servers
   ping 192.168.40.10

   # From Admin to anywhere
   ping 192.168.10.101
   ping 192.168.30.150
   ```

4. **Service Tests:**

   ```bash
   # DNS Resolution
   nslookup core-router.smart-city.local
   nslookup dhcp.smart-city.local

   # Email connectivity (telnet test)
   telnet 192.168.40.30 25
   ```

---

## Troubleshooting Common Issues

### Connection Problems

1. **No DHCP Address:**
   - Check DHCP server is running
   - Verify helper-address on router
   - Ensure VLAN configuration is correct

2. **Cannot Ping Across VLANs:**
   - Check router subinterface configuration
   - Verify trunk links carry required VLANs
   - Check ACL configuration

3. **WiFi Connection Issues:**
   - Verify SSID broadcast is enabled
   - Check password and authentication type
   - Ensure access point has correct IP

### Configuration Verification Commands

```cisco
# On Router
show ip interface brief
show ipv6 interface brief
show vlan brief
show access-lists

# On Switches
show vlan brief
show interfaces trunk
show spanning-tree brief
```

---

## Final Network Summary

### Device Count: 33 total devices

- **Infrastructure**: 8 (1 router + 7 switches)
- **Servers**: 3 (DNS, DHCP, Email)
- **WiFi**: 2 (Access Points)
- **IoT Devices**: 8 (Sensors, cameras, lighting)
- **End Devices**: 12 (PCs, laptops, phones, tablets)

### VLANs Implemented

- **VLAN 10**: IoT Sensors (8 devices)
- **VLAN 20**: Administrative (4 devices)
- **VLAN 30**: Public WiFi (5 devices)
- **VLAN 40**: Servers (3 devices)
- **VLAN 50**: Mobile Admin (3 devices)

### Complex Engineering Features

✅ **IPv4/IPv6 Dual Stack**: Complete addressing scheme
✅ **VLAN Segmentation**: 5 isolated network segments
✅ **ACL Security**: Traffic filtering and access control
✅ **DHCP Services**: Automated IP assignment
✅ **DNS Services**: Local name resolution
✅ **IoT Integration**: 8 smart city devices
✅ **Wireless Infrastructure**: Public WiFi with security
✅ **Multiple Stakeholders**: Different user groups with varying access needs

**Total Implementation Time**: 2-3 hours

This implementation demonstrates complex engineering problem-solving with multiple conflicting requirements, stakeholder needs, and technical interdependencies suitable for academic evaluation.