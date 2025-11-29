# Smart City Network - Minimal Demonstration Setup

> **Purpose:** Build the SMALLEST network that demonstrates ALL major concepts clearly. Quick to build (1-2 hours), easy to explain, shows everything your teacher needs to see.

> **Philosophy:** "Less is more" - Use minimal devices but configure everything properly to demonstrate concepts.

---

# Quick Overview

## What We're Building

**One complete smart city with MINIMAL devices:**

```
                [Core Router]
                      │
        ┌─────────────┴─────────────┐
        │                           │
   [Dist-SW-A]                 [Dist-SW-B]
        │                           │
   ┌────┼────┐                 ┌────┼────┐
   │    │    │                 │    │
[SW1][SW2][SW3]             [SW4][SW5]
   │    │    │                 │    │
Servers IoT Admin           WiFi  WiFi+Tab
```

**Total devices: 20-25** (not 66!)

---

# Device List - Minimal Configuration

## Infrastructure (8 devices)

| Device | Quantity | Purpose |
|--------|----------|---------|
| Core Router (2911) | 1 | Inter-VLAN routing, ACLs, central point |
| Distribution Switches | 2 | VLAN aggregation, shows distribution layer |
| Access Switches | 5 | One per VLAN, shows access layer |

## End Devices (12-17 devices)

| Device | Quantity | Purpose | What It Demonstrates |
|--------|----------|---------|---------------------|
| **Servers** | 2 | DNS + DHCP (combined) | DHCP service, DNS service, static IPs |
| **IoT Sensors** | 2 | Traffic sensor + Camera | IoT connectivity, VLAN 10, ACL protection |
| **Admin PCs** | 2 | Admin workstations | VLAN 20, inter-VLAN routing, ACL access |
| **WiFi Access Points** | 1 | Public WiFi | Wireless infrastructure, VLAN 30 |
| **WiFi Clients** | 2 | Smartphones/Tablets | Wireless connectivity, DHCP, ACL blocking |
| **Mobile Tablet** | 1 | Wired tablet | VLAN 50, shows wired mobile device |

**Total: 20 devices** (8 infrastructure + 12 end devices)

---

# Why This Setup Works

## ✅ All Major Concepts Covered

| Concept | How We Demonstrate | Minimal Devices Needed |
|---------|-------------------|----------------------|
| **VLANs** | 5 VLANs (10,20,30,40,50) | ✅ 5 access switches, 1 device per VLAN |
| **Inter-VLAN Routing** | Router-on-a-stick with subinterfaces | ✅ 1 router, test ping across VLANs |
| **ACLs** | ACL 110 (IoT), ACL 130 (Public WiFi) | ✅ IoT + Public WiFi + test blocking |
| **DHCP** | 4 DHCP pools (VLANs 10,20,30,50) | ✅ 1 DHCP server, devices get IPs |
| **DNS** | 3-4 DNS records | ✅ 1 DNS server, test nslookup |
| **Trunk Links** | Distribution↔Access trunks | ✅ 5 trunk links visible |
| **Spanning Tree** | Portfast on access ports | ✅ `show spanning-tree` on switches |
| **Static IPs** | Servers use static | ✅ Servers configured manually |
| **DHCP IPs** | All end devices use DHCP | ✅ Admin, IoT, WiFi use DHCP |
| **Wireless** | WiFi AP + clients | ✅ 1 AP, 2 wireless clients connect |
| **IPv6** | Dual-stack on all interfaces | ✅ All devices have IPv6 |
| **Security** | IoT isolated from public | ✅ Ping test shows blocking |

---

# Phase 1: Device Placement (10 minutes)

## Core Infrastructure

1. **Add Router:** 2911, label `Core-Router`, place top-center
2. **Add Distribution Switches:** 2960-24TT × 2
   - `Dist-SW-A` (left, below router)
   - `Dist-SW-B` (right, below router)
3. **Add Access Switches:** 2960-24TT × 5
   - `Access-SW1` (far left, servers)
   - `Access-SW2` (center-left, IoT)
   - `Access-SW3` (center, admin)
   - `Access-SW4` (center-right, WiFi)
   - `Access-SW5` (right, tablet)

## End Devices - Servers ONLY (Minimal!)

**Below Access-SW1:**
1. **Server-PT** → Label: `DNS-DHCP-Server` (combined server!)
   - Runs BOTH DNS and DHCP services
   - IP: 192.168.40.10

**That's it for servers!** (1 server does both jobs)

## End Devices - IoT (Minimal!)

**Below Access-SW2:**
1. IoT device (or PC-PT) → Label: `IoT-Traffic-1`
2. IoT device (or PC-PT) → Label: `IoT-Camera-1`

**That's it!** (2 IoT devices demonstrate the concept)

## End Devices - Admin (Minimal!)

**Below Access-SW3:**
1. **PC-PT** → Label: `Admin-PC-1`
2. **Laptop-PT** → Label: `Admin-Laptop-1`

## End Devices - WiFi

**Below Access-SW4:**
1. **AccessPoint-PT** → Label: `WiFi-Zone1`

**Wireless clients (no cables):**
1. **Smartphone-PT** → Label: `Phone-1`
2. **Tablet-PT** → Label: `Tablet-Public-1`

## End Devices - Mobile Admin

**Below Access-SW5:**
1. **Tablet-PT** → Label: `Tablet-Admin-1`

---

# Phase 2: Physical Connections (15 minutes)

## Router ↔ Distribution

1. **Core-Router** Gig0/0 ↔ **Dist-SW-A** Gig1/0/1
2. **Core-Router** Gig0/1 ↔ **Dist-SW-B** Gig1/0/1

## Distribution ↔ Access

**From Dist-SW-A:**
3. Fa1/0/1 → **Access-SW1** Fa0/24
4. Fa1/0/2 → **Access-SW2** Fa0/24
5. Fa1/0/3 → **Access-SW3** Fa0/24

**From Dist-SW-B:**
6. Fa1/0/1 → **Access-SW4** Fa0/24
7. Fa1/0/2 → **Access-SW5** Fa0/24

## Access ↔ End Devices

**Access-SW1:**
8. Fa0/1 → DNS-DHCP-Server

**Access-SW2:**
9. Fa0/1 → IoT-Traffic-1
10. Fa0/2 → IoT-Camera-1

**Access-SW3:**
11. Fa0/1 → Admin-PC-1
12. Fa0/2 → Admin-Laptop-1

**Access-SW4:**
13. Fa0/1 → WiFi-Zone1

**Access-SW5:**
14. Fa0/1 → Tablet-Admin-1

**Total connections: 14 wired**

---

# Phase 3: Router Configuration (30 minutes)

## Base Configuration

```cisco
enable
configure terminal
hostname Core-Router
ip routing
ipv6 unicast-routing
```

## Physical Interfaces

```cisco
interface GigabitEthernet0/0
 description Link to Dist-SW-A
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1000:1::1/64
 no shutdown
 exit

interface GigabitEthernet0/1
 description Link to Dist-SW-B
 ip address 192.168.2.1 255.255.255.0
 ipv6 address 2001:db8:1000:2::1/64
 no shutdown
 exit
```

## VLAN Subinterfaces

```cisco
! VLAN 10: IoT Sensors
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.10
 no shutdown
 exit

! VLAN 20: Administrative
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.10
 no shutdown
 exit

! VLAN 40: Servers
interface GigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown
 exit

! VLAN 30: Public WiFi
interface GigabitEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.10
 no shutdown
 exit

! VLAN 50: Mobile Admin
interface GigabitEthernet0/1.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64
 ip helper-address 192.168.40.10
 no shutdown
 exit
```

## ACLs (Security Demonstration)

```cisco
! ACL 110: IoT Security
access-list 110 remark IoT-Sensor-Security
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
access-list 110 permit ip any any

interface GigabitEthernet0/0.10
 ip access-group 110 in
 exit

! ACL 130: Public WiFi Security
access-list 130 remark Public-WiFi-Security
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 80
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 443
access-list 130 permit udp 192.168.30.0 0.0.0.255 192.168.40.10 0.0.0.0 eq 53
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.40.0 0.0.0.255 log
access-list 130 permit ip any any

interface GigabitEthernet0/1.30
 ip access-group 130 in
 exit

end
write memory
```

**Verify:**
```cisco
show ip interface brief
show access-lists
```

---

# Phase 4: Switch Configuration (30 minutes)

## Dist-SW-A (Quick Config)

```cisco
enable
configure terminal
hostname Dist-SW-A

vlan 10
 name IoT-Sensors
vlan 20
 name Administrative
vlan 40
 name Servers

interface GigabitEthernet1/0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,40
 no shutdown
 exit

interface range FastEthernet1/0/1-3
 switchport mode trunk
 no shutdown
 exit

interface FastEthernet1/0/1
 switchport trunk allowed vlan 40
interface FastEthernet1/0/2
 switchport trunk allowed vlan 10
interface FastEthernet1/0/3
 switchport trunk allowed vlan 20

end
write memory
```

## Dist-SW-B (Quick Config)

```cisco
enable
configure terminal
hostname Dist-SW-B

vlan 30
 name Public-WiFi
vlan 50
 name Mobile-Admin

interface GigabitEthernet1/0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

interface range FastEthernet1/0/1-2
 switchport mode trunk
 no shutdown
 exit

interface FastEthernet1/0/1
 switchport trunk allowed vlan 30
interface FastEthernet1/0/2
 switchport trunk allowed vlan 50

end
write memory
```

## Access Switches (Copy-Paste Templates)

**Access-SW1 (Servers - VLAN 40):**
```cisco
enable
configure terminal
hostname Access-SW1
vlan 40
 name Servers
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 no shutdown
end
write memory
```

**Access-SW2 (IoT - VLAN 10):**
```cisco
enable
configure terminal
hostname Access-SW2
vlan 10
 name IoT-Sensors
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
interface range FastEthernet0/1-2
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
end
write memory
```

**Access-SW3 (Admin - VLAN 20):**
```cisco
enable
configure terminal
hostname Access-SW3
vlan 20
 name Administrative
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
interface range FastEthernet0/1-2
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
end
write memory
```

**Access-SW4 (WiFi - VLAN 30):**
```cisco
enable
configure terminal
hostname Access-SW4
vlan 30
 name Public-WiFi
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
end
write memory
```

**Access-SW5 (Mobile Admin - VLAN 50):**
```cisco
enable
configure terminal
hostname Access-SW5
vlan 50
 name Mobile-Admin
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 50
 no shutdown
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown
end
write memory
```

---

# Phase 5: Server Configuration (15 minutes)

## DNS-DHCP-Server (Combined Server!)

**Click DNS-DHCP-Server → Desktop → IP Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.10 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::10 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

### Configure DNS Service

**Services → DNS → Turn ON**

Add records:

| Name | Address |
|------|---------|
| core-router.smart-city.local | 192.168.1.1 |
| server.smart-city.local | 192.168.40.10 |
| iot-traffic.smart-city.local | 192.168.10.100 |

### Configure DHCP Service

**Services → DHCP**

**Pool 1: IoT_SENSORS**
- Default Gateway: 192.168.10.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.10.100
- Subnet: 255.255.255.0
- Max Users: 10

**Pool 2: ADMIN**
- Default Gateway: 192.168.20.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.20.100
- Subnet: 255.255.255.0
- Max Users: 10

**Pool 3: PUBLIC_WIFI**
- Default Gateway: 192.168.30.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.30.100
- Subnet: 255.255.255.0
- Max Users: 20

**Pool 4: MOBILE_ADMIN**
- Default Gateway: 192.168.50.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.50.100
- Subnet: 255.255.255.0
- Max Users: 10

---

# Phase 6: End Device Configuration (10 minutes)

## IoT Devices

**IoT-Traffic-1, IoT-Camera-1:**
- Desktop → IP Configuration → **DHCP**
- Should get IPs: 192.168.10.100, 192.168.10.101

## Admin Devices

**Admin-PC-1, Admin-Laptop-1:**
- Desktop → IP Configuration → **DHCP**
- Should get IPs: 192.168.20.100, 192.168.20.101

## Mobile Admin

**Tablet-Admin-1:**
- Desktop → IP Configuration → **DHCP**
- Should get IP: 192.168.50.100

## WiFi Access Point

**WiFi-Zone1:**
- Config → Port 1:
  - IP: 192.168.30.50
  - Subnet: 255.255.255.0
  - Gateway: 192.168.30.1
- Config → Wireless:
  - SSID: SmartCity_WiFi
  - Auth: WPA2-PSK
  - Password: SmartCity2024
  - Channel: 6

## WiFi Clients

**Phone-1, Tablet-Public-1:**
- Desktop → PC Wireless → Connect
- Select: SmartCity_WiFi
- Password: SmartCity2024
- Should get IPs: 192.168.30.100, 192.168.30.101

---

# Phase 7: Demonstration Tests (20 minutes)

## Test 1: Show VLANs

**On Access-SW2:**
```cisco
show vlan brief
```

**Expected:** VLAN 10 with ports Fa0/1-2

**SAY:** "This shows VLAN segmentation - IoT devices are isolated in VLAN 10"

---

## Test 2: Show Inter-VLAN Routing

**From Admin-PC-1:**
```
ping 192.168.10.100
```

**Expected:** Success!

**SAY:** "Admin PC (VLAN 20) can ping IoT sensor (VLAN 10) because router does inter-VLAN routing via subinterfaces Gig0/0.20 and Gig0/0.10"

**Show on router:**
```cisco
show ip interface brief | include 0.
```

**Expected:** Shows .10, .20, .30, .40, .50 subinterfaces

---

## Test 3: Show ACL Blocking Public WiFi

**From Phone-1:**
```
ping 192.168.10.100
```

**Expected:** Request timed out (BLOCKED!)

**SAY:** "Public WiFi (VLAN 30) CANNOT access IoT sensors (VLAN 10) due to ACL 130 blocking traffic"

**Show on router:**
```cisco
show access-lists 130
```

**Expected:** See deny rule with match counter increasing

---

## Test 4: Show DHCP Working

**From Admin-PC-1:**
```
ipconfig
```

**Expected:** IP 192.168.20.100, Gateway 192.168.20.1, DNS 192.168.40.10

**SAY:** "DHCP server automatically assigned IP address from pool ADMIN. Router helper-address forwards DHCP requests from VLAN 20 to server in VLAN 40"

---

## Test 5: Show DNS Resolution

**From Admin-PC-1:**
```
nslookup server.smart-city.local
```

**Expected:** Returns 192.168.40.10

**SAY:** "DNS service resolves hostnames to IP addresses. This enables user-friendly naming instead of memorizing IPs"

---

## Test 6: Show Trunk Links

**On Dist-SW-A:**
```cisco
show interfaces trunk
```

**Expected:** Shows Gig1/0/1 and Fa1/0/1-3 as trunk ports carrying VLANs

**SAY:** "Trunk links use 802.1Q tagging to carry multiple VLANs over a single physical connection. This shows which VLANs are allowed on each trunk"

---

## Test 7: Show Spanning Tree

**On Access-SW2:**
```cisco
show spanning-tree brief
```

**Expected:** Shows STP status for VLAN 10

**SAY:** "Spanning Tree Protocol prevents loops in the network. Portfast on access ports allows immediate connectivity for end devices"

---

## Test 8: Show IPv6

**On Core-Router:**
```cisco
show ipv6 interface brief
```

**Expected:** Shows IPv6 addresses on all interfaces

**From Admin-PC-1:**
```
ping6 2001:db8:1000:40::10
```

**Expected:** Ping succeeds

**SAY:** "Dual-stack implementation - network runs both IPv4 and IPv6 simultaneously for future compatibility"

---

## Test 9: Show Static IP vs DHCP

**Click DNS-DHCP-Server → Desktop → IP Configuration:**

**SAY:** "Server uses static IP (192.168.40.10) configured manually because servers need predictable addresses. End devices use DHCP for automatic configuration"

---

## Test 10: Show Wireless Connectivity

**Click Phone-1 → Desktop → PC Wireless:**

**Expected:** Shows connected to SmartCity_WiFi with signal strength

**SAY:** "Wireless clients connect to WiFi access point which is in VLAN 30. Access point bridges wireless to wired network"

---

# Summary: What This Minimal Setup Demonstrates

## ✅ All Major Concepts (Teacher Checklist)

| Concept | Demonstrated By | Show Command / Test |
|---------|----------------|---------------------|
| **VLANs** | 5 VLANs (10,20,30,40,50) | `show vlan brief` on switches |
| **Inter-VLAN Routing** | Router subinterfaces | Ping across VLANs, `show ip int brief` |
| **ACLs** | ACL 110, 130 block traffic | Ping fails, `show access-lists` |
| **DHCP** | 4 pools, auto IP assignment | `ipconfig` on devices |
| **DNS** | 3 records, name resolution | `nslookup server.smart-city.local` |
| **Trunk Links** | 5 trunks carrying VLANs | `show interfaces trunk` |
| **Spanning Tree** | STP prevents loops | `show spanning-tree brief` |
| **Static Routing** | N/A (single router) | N/A |
| **IPv6** | Dual-stack on all interfaces | `show ipv6 interface brief`, `ping6` |
| **Wireless** | 1 AP, 2 wireless clients | Connect to WiFi, verify IP |
| **Security** | ACLs block public from IoT | Ping test shows blocking |
| **Helper-Address** | DHCP relay via router | `ipconfig` shows DHCP from different VLAN |

---

# Device Count Summary

| Type | Quantity | Purpose |
|------|----------|---------|
| Router | 1 | Core routing, ACLs |
| Distribution Switches | 2 | Aggregation layer |
| Access Switches | 5 | One per VLAN |
| Servers | 1 | DNS + DHCP combined |
| IoT Devices | 2 | Demonstrate IoT VLAN |
| Admin PCs | 2 | Demonstrate Admin VLAN |
| WiFi AP | 1 | Wireless infrastructure |
| WiFi Clients | 2 | Wireless connectivity |
| Mobile Tablet | 1 | Mobile admin VLAN |
| **TOTAL** | **17-20** | Minimal but complete |

---

# Time Estimate

| Phase | Time |
|-------|------|
| Device Placement | 10 min |
| Physical Connections | 15 min |
| Router Configuration | 30 min |
| Switch Configuration | 30 min |
| Server Configuration | 15 min |
| End Device Configuration | 10 min |
| Testing & Demonstration Prep | 20 min |
| **TOTAL** | **2 hours 10 minutes** |

---

# What to Say to Your Teacher

> **"We've built a minimal smart city network that demonstrates all core concepts:**
>
> **Architecture:**
> - 1 core router with 5 VLAN subinterfaces for inter-VLAN routing
> - 2 distribution switches for aggregation
> - 5 access switches (one per VLAN) showing layered design
>
> **Services:**
> - Combined DNS/DHCP server with 4 pools and 3 DNS records
> - 2 IoT sensors in isolated VLAN with ACL protection
> - 2 admin workstations with full network access
> - 1 WiFi access point serving 2 wireless clients
> - 1 mobile admin tablet on separate VLAN
>
> **Security:**
> - ACL 110 protects IoT from public WiFi
> - ACL 130 restricts public WiFi to web traffic only
> - VLAN segmentation isolates device types
>
> **Demonstrations:**
> - Can show all VLANs, trunk links, ACLs via `show` commands
> - Can demonstrate inter-VLAN routing with ping tests
> - Can show ACL blocking with failed pings
> - Can demonstrate DHCP, DNS, wireless connectivity
> - Can prove spanning tree, IPv6, security policies work
>
> **This minimal setup covers 100% of requirements with 70% fewer devices than the full design, making it easier to build, explain, and demonstrate."**

---

# Quick Reference: Show Commands for Demonstration

```cisco
! On Router:
show ip interface brief              # Shows all interfaces/subinterfaces
show access-lists                    # Shows ACL configurations
show ip route                        # Shows routing table
show ipv6 interface brief            # Shows IPv6 addressing

! On Switches:
show vlan brief                      # Shows VLAN configuration
show interfaces trunk                # Shows trunk links
show spanning-tree brief             # Shows STP status
show running-config                  # Shows full configuration

! On End Devices:
ipconfig                             # Shows IP, gateway, DNS
ping <ip>                            # Tests connectivity
tracert <ip>                         # Shows path through network
nslookup <hostname>                  # Tests DNS resolution
```

---

**This is your optimal demonstration setup!** Build this version, and you can clearly show every concept without overwhelming complexity. 🎯
