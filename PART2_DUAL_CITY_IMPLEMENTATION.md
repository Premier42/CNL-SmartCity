# PART 2: Dual Smart City IoT Network - Complete Implementation Guide

> **Purpose:** Build TWO complete identical smart cities connected via a central core router. Each city has its own complete infrastructure: routers, switches, servers, IoT devices, WiFi, and admin networks.

> **Architecture:** Metropolitan area network connecting City A and City B, demonstrating inter-city connectivity and redundancy.

> **Estimated Time:** 5-6 hours for complete dual-city implementation

---

# Table of Contents

1. [Dual-City Architecture Overview](#1-dual-city-architecture-overview)
2. [Phase 1: Device Placement](#2-phase-1-device-placement)
3. [Phase 2: Physical Connections](#3-phase-2-physical-connections)
4. [Phase 3: City A Configuration](#4-phase-3-city-a-configuration)
5. [Phase 4: City B Configuration](#5-phase-4-city-b-configuration)
6. [Phase 5: Inter-City Routing](#6-phase-5-inter-city-routing)
7. [Phase 6: Testing](#7-phase-6-testing)

---

# 1. Dual-City Architecture Overview

## 1.1 Network Design

**What We're Building:**

```
┌────────────────────────────────────────────────────────────┐
│              METROPOLITAN SMART CITY NETWORK               │
│                                                            │
│  ┌──────────────────────┐      ┌──────────────────────┐  │
│  │      CITY A          │      │      CITY B          │  │
│  │  (Left Side)         │      │  (Right Side)        │  │
│  │                      │      │                      │  │
│  │ • 1 City Router      │      │ • 1 City Router      │  │
│  │ • 2 Dist Switches    │◄────►│ • 2 Dist Switches    │  │
│  │ • 5 Access Switches  │      │ • 5 Access Switches  │  │
│  │ • 3 Servers          │      │ • 3 Servers          │  │
│  │ • 8 IoT Devices      │      │ • 8 IoT Devices      │  │
│  │ • 4 Admin Devices    │      │ • 4 Admin Devices    │  │
│  │ • 2 WiFi APs         │      │ • 2 WiFi APs         │  │
│  │ • 3 Mobile Tablets   │      │ • 3 Mobile Tablets   │  │
│  │ • 5 Wireless Clients │      │ • 5 Wireless Clients │  │
│  └──────────────────────┘      └──────────────────────┘  │
│                                                            │
│  Total Devices: 66 (33 per city)                          │
└────────────────────────────────────────────────────────────┘
```

---

## 1.2 Why Two Cities?

**Demonstrates:**
1. ✅ **Scalability** - Shows how infrastructure expands across regions
2. ✅ **Redundancy** - If City A fails, City B continues operating
3. ✅ **Inter-city connectivity** - Cities can share data (traffic sensors, emergency services)
4. ✅ **Load balancing** - Distribute services across two locations
5. ✅ **Real-world design** - Matches how Singapore/Barcelona connect multiple districts

**Example Use Cases:**
- City A traffic sensor detects congestion → alerts City B traffic management
- City A DHCP server fails → City B DHCP server provides backup
- Emergency services in City A can access City B camera feeds

---

## 1.3 Addressing Scheme

### City A IP Ranges

| VLAN | Purpose | IPv4 Subnet | IPv6 Subnet | Gateway |
|------|---------|-------------|-------------|---------|
| 10 | IoT Sensors (City A) | 192.168.10.0/24 | 2001:db8:1000:10::/64 | .1 |
| 20 | Admin (City A) | 192.168.20.0/24 | 2001:db8:1000:20::/64 | .1 |
| 30 | Public WiFi (City A) | 192.168.30.0/24 | 2001:db8:1000:30::/64 | .1 |
| 40 | Servers (City A) | 192.168.40.0/24 | 2001:db8:1000:40::/64 | .1 |
| 50 | Mobile Admin (City A) | 192.168.50.0/24 | 2001:db8:1000:50::/64 | .1 |

### City B IP Ranges

| VLAN | Purpose | IPv4 Subnet | IPv6 Subnet | Gateway |
|------|---------|-------------|-------------|---------|
| 110 | IoT Sensors (City B) | 192.168.110.0/24 | 2001:db8:2000:10::/64 | .1 |
| 120 | Admin (City B) | 192.168.120.0/24 | 2001:db8:2000:20::/64 | .1 |
| 130 | Public WiFi (City B) | 192.168.130.0/24 | 2001:db8:2000:30::/64 | .1 |
| 140 | Servers (City B) | 192.168.140.0/24 | 2001:db8:2000:40::/64 | .1 |
| 150 | Mobile Admin (City B) | 192.168.150.0/24 | 2001:db8:2000:50::/64 | .1 |

### Inter-City Link

| Link | Purpose | IPv4 Subnet | IPv6 Subnet |
|------|---------|-------------|-------------|
| City A ↔ City B | Router interconnect | 10.0.0.0/30 | 2001:db8:ffff::/64 |

---

## 1.4 Device Naming Convention

### City A Devices

```
City-A-Router (Core router for City A)
├── Dist-SW-A1 (Distribution switch 1)
├── Dist-SW-A2 (Distribution switch 2)
├── Access-SW-A1 (Servers)
├── Access-SW-A2 (IoT)
├── Access-SW-A3 (Admin)
├── Access-SW-A4 (WiFi Zone 1)
├── Access-SW-A5 (WiFi Zone 2 + Mobile Admin)
├── DNS-Server-A (192.168.40.10)
├── DHCP-Server-A (192.168.40.20)
├── Email-Server-A (192.168.40.30)
├── IoT-A-Traffic-1 through IoT-A-Light-1 (8 devices)
├── Admin-A-PC-1 through Admin-A-Laptop-2 (4 devices)
├── WiFi-Zone-A1, WiFi-Zone-A2 (2 access points)
├── Tablet-Admin-A1 through A3 (3 wired tablets)
└── Phone-A1, Phone-A2, Phone-A3, Tablet-Public-A1, A2 (5 wireless)
```

### City B Devices

```
City-B-Router (Core router for City B)
├── Dist-SW-B1 (Distribution switch 1)
├── Dist-SW-B2 (Distribution switch 2)
├── Access-SW-B1 (Servers)
├── Access-SW-B2 (IoT)
├── Access-SW-B3 (Admin)
├── Access-SW-B4 (WiFi Zone 1)
├── Access-SW-B5 (WiFi Zone 2 + Mobile Admin)
├── DNS-Server-B (192.168.140.10)
├── DHCP-Server-B (192.168.140.20)
├── Email-Server-B (192.168.140.30)
├── IoT-B-Traffic-1 through IoT-B-Light-1 (8 devices)
├── Admin-B-PC-1 through Admin-B-Laptop-2 (4 devices)
├── WiFi-Zone-B1, WiFi-Zone-B2 (2 access points)
├── Tablet-Admin-B1 through B3 (3 wired tablets)
└── Phone-B1, Phone-B2, Phone-B3, Tablet-Public-B1, B2 (5 wireless)
```

---

# 2. Phase 1: Device Placement (40 minutes)

## 2.1 Workspace Layout Strategy

**Organize your workspace:**

```
┌─────────────────────────────────────────────────────────────┐
│                    Packet Tracer Workspace                  │
│                                                             │
│  LEFT HALF (City A)              RIGHT HALF (City B)       │
│  ┌──────────────────┐           ┌──────────────────┐      │
│  │  City-A-Router   │◄─────────►│  City-B-Router   │      │
│  └────────┬─────────┘           └────────┬─────────┘      │
│           │                               │                 │
│      ┌────┴────┐                    ┌────┴────┐           │
│  Dist-SW-A1  Dist-SW-A2         Dist-SW-B1  Dist-SW-B2   │
│      │          │                    │          │          │
│  (5 Access    (Identical        (5 Access    (Identical   │
│   Switches)    layout)           Switches)    layout)     │
│      │                               │                     │
│  (Devices)                        (Devices)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Visual Guide:**
- **City A:** Left 50% of workspace
- **City B:** Right 50% of workspace
- **Mirror layout:** City B is a mirror image of City A

---

## 2.2 Add City A Infrastructure

### Step 1: Add City A Router

1. Click **Network Devices** → **Routers** → **2911**
2. Drag to **upper-left quadrant**
3. Label: `City-A-Router`

### Step 2: Add City A Distribution Switches (2)

1. **Network Devices** → **Switches** → **2960-24TT**
2. Drag **below City-A-Router, slightly left**
3. Label: `Dist-SW-A1`

4. Add second switch **below City-A-Router, slightly right**
5. Label: `Dist-SW-A2`

### Step 3: Add City A Access Switches (5)

Add 5 switches in a row below distribution layer:

| Switch | Label | Position | Connects To |
|--------|-------|----------|-------------|
| 1 | Access-SW-A1 | Far left | Servers |
| 2 | Access-SW-A2 | Center-left | IoT devices |
| 3 | Access-SW-A3 | Center | Admin devices |
| 4 | Access-SW-A4 | Center-right | WiFi Zone 1 |
| 5 | Access-SW-A5 | Right | WiFi Zone 2 + Tablets |

---

## 2.3 Add City B Infrastructure (Mirror City A)

### Step 4: Add City B Router

1. **Network Devices** → **Routers** → **2911**
2. Drag to **upper-right quadrant** (mirror position to City-A-Router)
3. Label: `City-B-Router`

### Step 5: Add City B Distribution Switches (2)

1. Add switch **below City-B-Router, slightly left**
2. Label: `Dist-SW-B1`

3. Add switch **below City-B-Router, slightly right**
4. Label: `Dist-SW-B2`

### Step 6: Add City B Access Switches (5)

Add 5 switches below Dist-SW-B1/B2:

| Switch | Label | Position |
|--------|-------|----------|
| 1 | Access-SW-B1 | Far left (mirrors Access-SW-A1) |
| 2 | Access-SW-B2 | Center-left |
| 3 | Access-SW-B3 | Center |
| 4 | Access-SW-B4 | Center-right |
| 5 | Access-SW-B5 | Right |

**Checkpoint:** You should now have **2 routers + 4 distribution switches + 10 access switches = 16 switches**

---

## 2.4 Add City A End Devices

### Servers (City A)

**Below Access-SW-A1:**

1. **End Devices** → **Server-PT**
2. Add 3 servers vertically
3. Labels:
   - `DNS-Server-A`
   - `DHCP-Server-A`
   - `Email-Server-A`

### IoT Devices (City A)

**Below Access-SW-A2:**

Add 8 IoT devices:

| Device Type | Quantity | Labels |
|-------------|----------|--------|
| Motion Detector / Environmental Monitor | 3 | IoT-A-Traffic-1, IoT-A-Traffic-2, IoT-A-Traffic-3 |
| Environmental Monitor | 2 | IoT-A-Env-1, IoT-A-Env-2 |
| Webcam | 2 | IoT-A-Camera-1, IoT-A-Camera-2 |
| Smart Device / Light | 1 | IoT-A-Light-1 |

**If IoT devices not available:** Use **PC-PT** or **Laptop-PT** as substitutes

### Admin Devices (City A)

**Below Access-SW-A3:**

1. Add 2 **PC-PT**: `Admin-A-PC-1`, `Admin-A-PC-2`
2. Add 2 **Laptop-PT**: `Admin-A-Laptop-1`, `Admin-A-Laptop-2`

### WiFi Infrastructure (City A)

**Below Access-SW-A4:**
1. **Network Devices** → **Wireless Devices** → **AccessPoint-PT**
2. Label: `WiFi-Zone-A1`

**Below Access-SW-A5:**
3. Add second access point: `WiFi-Zone-A2`
4. Add 3 **Tablet-PT** (wired): `Tablet-Admin-A1`, `Tablet-Admin-A2`, `Tablet-Admin-A3`

### Wireless Clients (City A)

**Place anywhere in City A workspace (no cables):**

1. Add 3 **Smartphone-PT**: `Phone-A1`, `Phone-A2`, `Phone-A3`
2. Add 2 **Tablet-PT**: `Tablet-Public-A1`, `Tablet-Public-A2`

---

## 2.5 Add City B End Devices (Identical to City A)

**Repeat Section 2.4 for City B** with these label changes:

### Servers (City B)

**Below Access-SW-B1:**
- `DNS-Server-B`
- `DHCP-Server-B`
- `Email-Server-B`

### IoT Devices (City B)

**Below Access-SW-B2:**
- 8 devices labeled: `IoT-B-Traffic-1` through `IoT-B-Light-1`

### Admin Devices (City B)

**Below Access-SW-B3:**
- `Admin-B-PC-1`, `Admin-B-PC-2`
- `Admin-B-Laptop-1`, `Admin-B-Laptop-2`

### WiFi Infrastructure (City B)

**Below Access-SW-B4:**
- `WiFi-Zone-B1`

**Below Access-SW-B5:**
- `WiFi-Zone-B2`
- `Tablet-Admin-B1`, `Tablet-Admin-B2`, `Tablet-Admin-B3` (wired)

### Wireless Clients (City B)

**Anywhere in City B workspace:**
- `Phone-B1`, `Phone-B2`, `Phone-B3`
- `Tablet-Public-B1`, `Tablet-Public-B2`

---

## 2.6 Device Count Verification

**After placement, verify counts:**

| Category | City A | City B | Total |
|----------|--------|--------|-------|
| Routers | 1 | 1 | **2** |
| Distribution Switches | 2 | 2 | **4** |
| Access Switches | 5 | 5 | **10** |
| Servers | 3 | 3 | **6** |
| IoT Devices | 8 | 8 | **16** |
| Admin PCs/Laptops | 4 | 4 | **8** |
| WiFi Access Points | 2 | 2 | **4** |
| Mobile Admin Tablets | 3 | 3 | **6** |
| Wireless Clients | 5 | 5 | **10** |
| **TOTAL** | **33** | **33** | **66** |

✅ **Checkpoint:** Save project (Ctrl+S)

---

# 3. Phase 2: Physical Connections (60 minutes)

## 3.1 Inter-City Link (Most Important!)

**Connect the two city routers together:**

**Step 1:** Click **Connections** → **Copper Straight-Through**

**Step 2:** Connect routers:
- **City-A-Router** interface `GigabitEthernet0/2` (or `Gig0/0/2` if ISR4331)
- ↔
- **City-B-Router** interface `GigabitEthernet0/2` (or `Gig0/0/2`)

**This is the critical link that connects the two cities!**

✅ Verify: Orange line between the two routers

---

## 3.2 City A Internal Connections

### City A Router to Distribution

**Connection 1:** City-A-Router to Dist-SW-A1
- Router: `GigabitEthernet0/0` (or `Gig0/0/0`)
- Switch: `GigabitEthernet1/0/1`

**Connection 2:** City-A-Router to Dist-SW-A2
- Router: `GigabitEthernet0/1` (or `Gig0/0/1`)
- Switch: `GigabitEthernet1/0/1`

### City A Distribution to Access

**From Dist-SW-A1:**
- `Fa1/0/1` → **Access-SW-A1** `Fa0/24` (Servers)
- `Fa1/0/2` → **Access-SW-A2** `Fa0/24` (IoT)
- `Fa1/0/3` → **Access-SW-A3** `Fa0/24` (Admin)

**From Dist-SW-A2:**
- `Fa1/0/1` → **Access-SW-A4** `Fa0/24` (WiFi Zone 1)
- `Fa1/0/2` → **Access-SW-A5** `Fa0/24` (WiFi Zone 2 + Tablets)

### City A Access to End Devices

**Access-SW-A1 to Servers:**
- `Fa0/1` → DNS-Server-A
- `Fa0/2` → DHCP-Server-A
- `Fa0/3` → Email-Server-A

**Access-SW-A2 to IoT (8 devices):**
- `Fa0/1` → IoT-A-Traffic-1
- `Fa0/2` → IoT-A-Traffic-2
- `Fa0/3` → IoT-A-Traffic-3
- `Fa0/4` → IoT-A-Env-1
- `Fa0/5` → IoT-A-Env-2
- `Fa0/6` → IoT-A-Camera-1
- `Fa0/7` → IoT-A-Camera-2
- `Fa0/8` → IoT-A-Light-1

**Access-SW-A3 to Admin (4 devices):**
- `Fa0/1` → Admin-A-PC-1
- `Fa0/2` → Admin-A-PC-2
- `Fa0/3` → Admin-A-Laptop-1
- `Fa0/4` → Admin-A-Laptop-2

**Access-SW-A4 to WiFi:**
- `Fa0/1` → WiFi-Zone-A1

**Access-SW-A5 to WiFi + Tablets:**
- `Fa0/1` → WiFi-Zone-A2
- `Fa0/2` → Tablet-Admin-A1
- `Fa0/3` → Tablet-Admin-A2
- `Fa0/4` → Tablet-Admin-A3

**Wireless clients:** NO CABLES (will connect via WiFi later)

---

## 3.3 City B Internal Connections (Identical Pattern)

**Repeat Section 3.2 for City B** using City B devices:

### City B Router to Distribution

- **City-B-Router** `Gig0/0` → **Dist-SW-B1** `Gig1/0/1`
- **City-B-Router** `Gig0/1` → **Dist-SW-B2** `Gig1/0/1`

### City B Distribution to Access

**From Dist-SW-B1:**
- `Fa1/0/1` → Access-SW-B1
- `Fa1/0/2` → Access-SW-B2
- `Fa1/0/3` → Access-SW-B3

**From Dist-SW-B2:**
- `Fa1/0/1` → Access-SW-B4
- `Fa1/0/2` → Access-SW-B5

### City B Access to End Devices

**Access-SW-B1:** 3 servers (DNS-Server-B, DHCP-Server-B, Email-Server-B)

**Access-SW-B2:** 8 IoT devices (IoT-B-Traffic-1 through IoT-B-Light-1)

**Access-SW-B3:** 4 admin devices (Admin-B-PC-1, Admin-B-PC-2, Admin-B-Laptop-1, Admin-B-Laptop-2)

**Access-SW-B4:** WiFi-Zone-B1

**Access-SW-B5:** WiFi-Zone-B2 + 3 tablets (Tablet-Admin-B1, B2, B3)

---

## 3.4 Connection Summary

**Total Connections:**

| Connection Type | City A | City B | Inter-City | Total |
|-----------------|--------|--------|------------|-------|
| Router ↔ Distribution | 2 | 2 | 1 | 5 |
| Distribution ↔ Access | 5 | 5 | 0 | 10 |
| Access ↔ End Devices | 20 | 20 | 0 | 40 |
| **TOTAL WIRED** | **27** | **27** | **1** | **55** |

✅ **Checkpoint:** All green triangles on connections? Save project!

---

# 4. Phase 3: City A Configuration (90 minutes)

## 4.1 City A Router Configuration

**Click City-A-Router → CLI tab**

### Verify Interface Names

```cisco
enable
show ip interface brief
```

**Determine format:** `Gig0/0` (2911) or `Gig0/0/0` (ISR4331)

**For this guide:** Using 2911 format (`Gig0/0`). If you have ISR4331, change to `Gig0/0/0`.

---

### Base Configuration

```cisco
enable
configure terminal
hostname City-A-Router

ip routing
ipv6 unicast-routing
```

---

### Configure Physical Interfaces

**Interface to Dist-SW-A1:**

```cisco
interface GigabitEthernet0/0
 description Link to Dist-SW-A1
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1000:1::1/64
 no shutdown
 exit
```

**Interface to Dist-SW-A2:**

```cisco
interface GigabitEthernet0/1
 description Link to Dist-SW-A2
 ip address 192.168.2.1 255.255.255.0
 ipv6 address 2001:db8:1000:2::1/64
 no shutdown
 exit
```

**Interface to City-B-Router (Inter-City Link):**

```cisco
interface GigabitEthernet0/2
 description Inter-City Link to City-B-Router
 ip address 10.0.0.1 255.255.255.252
 ipv6 address 2001:db8:ffff::1/64
 no shutdown
 exit
```

---

### Configure VLAN Subinterfaces (City A)

**VLAN 10: IoT Sensors**

```cisco
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

**VLAN 20: Administrative**

```cisco
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

**VLAN 40: Servers**

```cisco
interface GigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown
 exit
```

**VLAN 30: Public WiFi**

```cisco
interface GigabitEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

**VLAN 50: Mobile Admin**

```cisco
interface GigabitEthernet0/1.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

---

### Configure ACLs (City A)

**ACL 110: IoT Security**

```cisco
access-list 110 remark IoT-Security-City-A
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.110.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
access-list 110 permit ip any any

interface GigabitEthernet0/0.10
 ip access-group 110 in
 exit
```

**ACL 130: Public WiFi Security**

```cisco
access-list 130 remark Public-WiFi-Security-City-A
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
```

---

### Configure Inter-City Routing (City A)

**Static routes to City B networks:**

```cisco
ip route 192.168.110.0 255.255.255.0 10.0.0.2
ip route 192.168.120.0 255.255.255.0 10.0.0.2
ip route 192.168.130.0 255.255.255.0 10.0.0.2
ip route 192.168.140.0 255.255.255.0 10.0.0.2
ip route 192.168.150.0 255.255.255.0 10.0.0.2

ipv6 route 2001:db8:2000::/48 2001:db8:ffff::2
```

**Explanation:**
- `10.0.0.2` = City-B-Router interface on inter-city link
- Routes point to City B's networks (192.168.110-150)

---

### Save Configuration

```cisco
end
write memory
```

✅ **Verify:**

```cisco
show ip interface brief
show ip route
```

Expected: 8 interfaces UP (3 physical + 5 subinterfaces), routes to City B networks

---

## 4.2 City A Switch Configuration

### Dist-SW-A1 Configuration

```cisco
enable
configure terminal
hostname Dist-SW-A1

vlan 10
 name IoT-Sensors-City-A
 exit
vlan 20
 name Administrative-City-A
 exit
vlan 40
 name Servers-City-A
 exit

interface GigabitEthernet1/0/1
 description Trunk to City-A-Router
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,40
 no shutdown
 exit

interface FastEthernet1/0/1
 description Trunk to Access-SW-A1
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

interface FastEthernet1/0/2
 description Trunk to Access-SW-A2
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit

interface FastEthernet1/0/3
 description Trunk to Access-SW-A3
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

end
write memory
```

---

### Dist-SW-A2 Configuration

```cisco
enable
configure terminal
hostname Dist-SW-A2

vlan 30
 name Public-WiFi-City-A
 exit
vlan 50
 name Mobile-Admin-City-A
 exit

interface GigabitEthernet1/0/1
 description Trunk to City-A-Router
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

interface FastEthernet1/0/1
 description Trunk to Access-SW-A4
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit

interface FastEthernet1/0/2
 description Trunk to Access-SW-A5
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

end
write memory
```

---

### Access Switch Configurations (City A)

**Access-SW-A1 (Servers):**

```cisco
enable
configure terminal
hostname Access-SW-A1

vlan 40
 name Servers-City-A
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-A1
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

interface range FastEthernet0/1-3
 description Server Ports
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Access-SW-A2 (IoT):**

```cisco
enable
configure terminal
hostname Access-SW-A2

vlan 10
 name IoT-Sensors-City-A
 exit

interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit

interface range FastEthernet0/1-8
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Access-SW-A3 (Admin):**

```cisco
enable
configure terminal
hostname Access-SW-A3

vlan 20
 name Administrative-City-A
 exit

interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

interface range FastEthernet0/1-4
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Access-SW-A4 (WiFi Zone 1):**

```cisco
enable
configure terminal
hostname Access-SW-A4

vlan 30
 name Public-WiFi-City-A
 exit

interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit

interface FastEthernet0/1
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Access-SW-A5 (WiFi Zone 2 + Mobile Admin):**

```cisco
enable
configure terminal
hostname Access-SW-A5

vlan 30
 name Public-WiFi-City-A
 exit
vlan 50
 name Mobile-Admin-City-A
 exit

interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

interface FastEthernet0/1
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

interface range FastEthernet0/2-4
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## 4.3 City A Server Configuration

### DNS-Server-A

**Click DNS-Server-A → Desktop → IP Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.10 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::10 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

**Click Services → DNS → Turn ON**

**Add DNS Records:**

| Name | Address |
|------|---------|
| city-a-router.smart-city.local | 192.168.1.1 |
| dhcp-a.smart-city.local | 192.168.40.20 |
| email-a.smart-city.local | 192.168.40.30 |
| dns-a.smart-city.local | 192.168.40.10 |
| city-b-router.smart-city.local | 10.0.0.2 |
| dns-b.smart-city.local | 192.168.140.10 |

---

### DHCP-Server-A

**IP Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.20 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::20 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

**Services → DHCP:**

**Pool 1: IoT_SENSORS_A**
- Default Gateway: 192.168.10.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.10.100
- Subnet Mask: 255.255.255.0
- Max Users: 50

**Pool 2: ADMIN_A**
- Default Gateway: 192.168.20.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.20.100
- Subnet Mask: 255.255.255.0
- Max Users: 20

**Pool 3: PUBLIC_WIFI_A**
- Default Gateway: 192.168.30.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.30.100
- Subnet Mask: 255.255.255.0
- Max Users: 100

**Pool 4: MOBILE_ADMIN_A**
- Default Gateway: 192.168.50.1
- DNS Server: 192.168.40.10
- Start IP: 192.168.50.100
- Subnet Mask: 255.255.255.0
- Max Users: 20

---

### Email-Server-A

**IP Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.30 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |

**Services → EMAIL:**
- Domain: smart-city-a.local
- Add Users: admin, operations

---

## 4.4 City A WiFi Configuration

### WiFi-Zone-A1

**Config → Port 1:**

| Field | Value |
|-------|-------|
| IP Address | 192.168.30.50 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.30.1 |

**Wireless:**
- SSID: SmartCity_A_Zone1
- Authentication: WPA2-PSK
- Password: SmartCityA2024
- Channel: 6

### WiFi-Zone-A2

**Config → Port 1:**

| Field | Value |
|-------|-------|
| IP Address | 192.168.30.51 |

**Wireless:**
- SSID: SmartCity_A_Zone2
- Password: SmartCityA2024
- Channel: 11

---

## 4.5 City A End Device Configuration

**Admin devices:** Desktop → IP Configuration → **DHCP**

**IoT devices:** Config → Interface → **DHCP**

**Mobile tablets:** Desktop → IP Configuration → **DHCP**

**Wireless clients:** Desktop → PC Wireless → Connect to SmartCity_A_Zone1 or SmartCity_A_Zone2

✅ **City A configuration complete!**

---

# 5. Phase 4: City B Configuration (90 minutes)

## 5.1 City B Router Configuration

**Click City-B-Router → CLI**

**IDENTICAL to City A router config, with these changes:**

### Key Differences for City B

**Hostname:**
```cisco
hostname City-B-Router
```

**Physical Interfaces:**

```cisco
interface GigabitEthernet0/0
 description Link to Dist-SW-B1
 ip address 192.168.101.1 255.255.255.0
 ipv6 address 2001:db8:2000:1::1/64
 no shutdown
 exit

interface GigabitEthernet0/1
 description Link to Dist-SW-B2
 ip address 192.168.102.1 255.255.255.0
 ipv6 address 2001:db8:2000:2::1/64
 no shutdown
 exit

interface GigabitEthernet0/2
 description Inter-City Link to City-A-Router
 ip address 10.0.0.2 255.255.255.252
 ipv6 address 2001:db8:ffff::2/64
 no shutdown
 exit
```

**VLAN Subinterfaces (City B uses VLANs 110, 120, 130, 140, 150):**

```cisco
interface GigabitEthernet0/0.110
 encapsulation dot1Q 110
 ip address 192.168.110.1 255.255.255.0
 ipv6 address 2001:db8:2000:10::1/64
 ip helper-address 192.168.140.20
 no shutdown
 exit

interface GigabitEthernet0/0.120
 encapsulation dot1Q 120
 ip address 192.168.120.1 255.255.255.0
 ipv6 address 2001:db8:2000:20::1/64
 ip helper-address 192.168.140.20
 no shutdown
 exit

interface GigabitEthernet0/0.140
 encapsulation dot1Q 140
 ip address 192.168.140.1 255.255.255.0
 ipv6 address 2001:db8:2000:40::1/64
 no shutdown
 exit

interface GigabitEthernet0/1.130
 encapsulation dot1Q 130
 ip address 192.168.130.1 255.255.255.0
 ipv6 address 2001:db8:2000:30::1/64
 ip helper-address 192.168.140.20
 no shutdown
 exit

interface GigabitEthernet0/1.150
 encapsulation dot1Q 150
 ip address 192.168.150.1 255.255.255.0
 ipv6 address 2001:db8:2000:50::1/64
 ip helper-address 192.168.140.20
 no shutdown
 exit
```

**ACLs (adjust for City B subnets):**

```cisco
access-list 210 remark IoT-Security-City-B
access-list 210 permit ip 192.168.110.0 0.0.0.255 192.168.140.0 0.0.0.255
access-list 210 permit ip 192.168.110.0 0.0.0.255 192.168.120.0 0.0.0.255
access-list 210 permit ip 192.168.110.0 0.0.0.255 192.168.10.0 0.0.0.255
access-list 210 deny ip 192.168.110.0 0.0.0.255 192.168.130.0 0.0.0.255 log
access-list 210 permit ip any any

interface GigabitEthernet0/0.110
 ip access-group 210 in
 exit

access-list 230 remark Public-WiFi-Security-City-B
access-list 230 permit tcp 192.168.130.0 0.0.0.255 any eq 80
access-list 230 permit tcp 192.168.130.0 0.0.0.255 any eq 443
access-list 230 permit udp 192.168.130.0 0.0.0.255 192.168.140.10 0.0.0.0 eq 53
access-list 230 deny ip 192.168.130.0 0.0.0.255 192.168.110.0 0.0.0.255 log
access-list 230 deny ip 192.168.130.0 0.0.0.255 192.168.120.0 0.0.0.255 log
access-list 230 deny ip 192.168.130.0 0.0.0.255 192.168.140.0 0.0.0.255 log
access-list 230 permit ip any any

interface GigabitEthernet0/1.130
 ip access-group 230 in
 exit
```

**Static Routes to City A:**

```cisco
ip route 192.168.10.0 255.255.255.0 10.0.0.1
ip route 192.168.20.0 255.255.255.0 10.0.0.1
ip route 192.168.30.0 255.255.255.0 10.0.0.1
ip route 192.168.40.0 255.255.255.0 10.0.0.1
ip route 192.168.50.0 255.255.255.0 10.0.0.1

ipv6 route 2001:db8:1000::/48 2001:db8:ffff::1

end
write memory
```

---

## 5.2 City B Switch Configuration

**Repeat City A switch configs with these name changes:**

### Dist-SW-B1

- Hostname: `Dist-SW-B1`
- VLANs: 110, 120, 140
- VLAN names: IoT-Sensors-City-B, Administrative-City-B, Servers-City-B

### Dist-SW-B2

- Hostname: `Dist-SW-B2`
- VLANs: 130, 150
- VLAN names: Public-WiFi-City-B, Mobile-Admin-City-B

### Access-SW-B1 through Access-SW-B5

- Use VLANs 110, 120, 130, 140, 150
- Update hostnames (Access-SW-B1, etc.)
- VLAN names include "City-B"

---

## 5.3 City B Server Configuration

**Identical to City A servers, with IP changes:**

### DNS-Server-B
- IP: 192.168.140.10
- Gateway: 192.168.140.1
- Add DNS records for City B services + City A cross-references

### DHCP-Server-B
- IP: 192.168.140.20
- Gateway: 192.168.140.1
- Pools: Use 192.168.110.x, 192.168.120.x, 192.168.130.x, 192.168.150.x ranges

### Email-Server-B
- IP: 192.168.140.30
- Domain: smart-city-b.local

---

## 5.4 City B WiFi & End Devices

**WiFi-Zone-B1, WiFi-Zone-B2:**
- IP: 192.168.130.50, 192.168.130.51
- SSID: SmartCity_B_Zone1, SmartCity_B_Zone2
- Password: SmartCityB2024

**End devices:** All use DHCP (admin, IoT, tablets, wireless clients)

✅ **City B configuration complete!**

---

# 6. Phase 5: Inter-City Routing (15 minutes)

## 6.1 Verify Inter-City Connectivity

**From City-A-Router:**

```cisco
ping 10.0.0.2
```

**Expected:** Replies from City-B-Router

**From City-B-Router:**

```cisco
ping 10.0.0.1
```

**Expected:** Replies from City-A-Router

---

## 6.2 Verify Routing Tables

**On City-A-Router:**

```cisco
show ip route
```

**Expected output includes:**

```
S    192.168.110.0/24 [1/0] via 10.0.0.2
S    192.168.120.0/24 [1/0] via 10.0.0.2
S    192.168.130.0/24 [1/0] via 10.0.0.2
S    192.168.140.0/24 [1/0] via 10.0.0.2
S    192.168.150.0/24 [1/0] via 10.0.0.2
C    10.0.0.0/30 is directly connected, GigabitEthernet0/2
```

**On City-B-Router:**

```
S    192.168.10.0/24 [1/0] via 10.0.0.1
S    192.168.20.0/24 [1/0] via 10.0.0.1
...
```

✅ Static routes present for opposite city's networks

---

# 7. Phase 6: Testing (45 minutes)

## 7.1 Intra-City Tests (Within Each City)

### Test 1: City A Internal Connectivity

**From Admin-A-PC-1:**

```
ipconfig
```

**Expected:** IP in 192.168.20.100-119 range

```
ping 192.168.40.10
```

**Expected:** Replies from DNS-Server-A

---

### Test 2: City B Internal Connectivity

**From Admin-B-PC-1:**

```
ipconfig
```

**Expected:** IP in 192.168.120.100-119 range

```
ping 192.168.140.10
```

**Expected:** Replies from DNS-Server-B

---

## 7.2 Inter-City Tests (Between Cities)

### Test 3: City A Admin to City B Server

**From Admin-A-PC-1:**

```
ping 192.168.140.10
```

**Expected:** Replies from DNS-Server-B (in City B)

**Explanation:** Traffic goes:
- Admin-A-PC-1 (192.168.20.100)
- → Access-SW-A3
- → Dist-SW-A1
- → City-A-Router
- → Inter-city link (10.0.0.0/30)
- → City-B-Router
- → Dist-SW-B1
- → Access-SW-B1
- → DNS-Server-B (192.168.140.10)

---

### Test 4: City B IoT to City A Server

**From IoT-B-Traffic-1:**

```
ping 192.168.40.20
```

**Expected:** Replies from DHCP-Server-A (in City A)

---

### Test 5: Cross-City DNS Resolution

**From Admin-A-PC-1:**

```
nslookup dns-b.smart-city.local
```

**Expected:** Returns 192.168.140.10 (City B DNS server)

---

## 7.3 Security Tests

### Test 6: City A Public WiFi Cannot Access City A IoT

**From Phone-A1 (connected to SmartCity_A_Zone1):**

```
ping 192.168.10.100
```

**Expected:** Request timed out (blocked by ACL 130)

---

### Test 7: City B Public WiFi Cannot Access City B Admin

**From Phone-B1:**

```
ping 192.168.120.100
```

**Expected:** Request timed out (blocked by ACL 230)

---

### Test 8: Cross-City IoT Communication

**From IoT-A-Traffic-1:**

```
ping 192.168.110.100
```

**Expected:** Success! (IoT devices in City A can communicate with City B IoT - ACL permits)

---

## 7.4 Redundancy Test (Optional)

### Test 9: City A DHCP Failover

**Scenario:** City A DHCP server fails; use City B DHCP

**Step 1:** Turn off DHCP service on DHCP-Server-A

**Step 2:** On City-A-Router, modify helper-address:

```cisco
configure terminal
interface GigabitEthernet0/0.10
 no ip helper-address 192.168.40.20
 ip helper-address 192.168.140.20
 exit
end
```

**Step 3:** Release/renew DHCP on City A IoT device

**Expected:** Device gets IP from City B DHCP server (192.168.140.20)

✅ **Demonstrates cross-city service redundancy!**

---

## 7.5 Test Results Summary

**Create test report:**

| Test # | Description | Expected Result | Actual Result | Status |
|--------|-------------|-----------------|---------------|--------|
| 1 | City A internal connectivity | Admin PC pings DNS | | ✅/❌ |
| 2 | City B internal connectivity | Admin PC pings DNS | | ✅/❌ |
| 3 | Inter-city: City A → City B | Ping City B DNS | | ✅/❌ |
| 4 | Inter-city: City B → City A | Ping City A DHCP | | ✅/❌ |
| 5 | Cross-city DNS resolution | nslookup works | | ✅/❌ |
| 6 | City A ACL security | Public WiFi blocked | | ✅/❌ |
| 7 | City B ACL security | Public WiFi blocked | | ✅/❌ |
| 8 | Cross-city IoT communication | IoT A ↔ IoT B | | ✅/❌ |
| 9 | DHCP redundancy (optional) | City B provides DHCP to City A | | ✅/❌ |

**Target:** 8/8 core tests pass (9/9 with optional redundancy test)

---

# Final Checklist

## ✅ Device Count Verification

| Category | City A | City B | Total | Status |
|----------|--------|--------|-------|--------|
| Routers | 1 | 1 | **2** | |
| Distribution Switches | 2 | 2 | **4** | |
| Access Switches | 5 | 5 | **10** | |
| Servers | 3 | 3 | **6** | |
| IoT Devices | 8 | 8 | **16** | |
| Admin PCs/Laptops | 4 | 4 | **8** | |
| WiFi Access Points | 2 | 2 | **4** | |
| Mobile Admin Tablets | 3 | 3 | **6** | |
| Wireless Clients | 5 | 5 | **10** | |
| **TOTAL** | **33** | **33** | **66** | |

---

## ✅ Configuration Verification

**City A:**
- [ ] Router: 8 interfaces UP (3 physical + 5 subinterfaces)
- [ ] Router: ACLs 110, 130 configured and applied
- [ ] Router: Static routes to City B networks
- [ ] Switches: VLANs 10, 20, 30, 40, 50 created
- [ ] Switches: Trunk links operational
- [ ] Servers: DNS, DHCP, Email configured
- [ ] WiFi: 2 APs broadcasting SmartCity_A_Zone1/2
- [ ] End devices: All have DHCP IPs or static IPs

**City B:**
- [ ] Router: 8 interfaces UP
- [ ] Router: ACLs 210, 230 configured
- [ ] Router: Static routes to City A networks
- [ ] Switches: VLANs 110, 120, 130, 140, 150 created
- [ ] Switches: Trunk links operational
- [ ] Servers: DNS, DHCP, Email configured
- [ ] WiFi: 2 APs broadcasting SmartCity_B_Zone1/2
- [ ] End devices: All have DHCP IPs or static IPs

**Inter-City:**
- [ ] Inter-city link UP (10.0.0.0/30)
- [ ] Ping between City-A-Router and City-B-Router works
- [ ] Static routes functional
- [ ] Cross-city communication verified

---

## 📊 What You've Accomplished

**Network Complexity:**
- ✅ 66 devices configured
- ✅ 55 wired connections
- ✅ 10 VLANs (5 per city)
- ✅ 4 ACLs (2 per city)
- ✅ 8 DHCP pools (4 per city)
- ✅ 12 DNS records (6 per city)
- ✅ Inter-city routing with static routes

**Demonstrates:**
1. ✅ **Depth of Knowledge** - Dual-stack IPv4/IPv6, VLANs, ACLs, inter-router routing
2. ✅ **Conflicting Requirements** - Same conflicts × 2 cities
3. ✅ **Depth of Analysis** - Capacity planning for 2 cities, redundancy analysis
4. ✅ **Familiarity** - Metropolitan area network design (real-world)
5. ✅ **Stakeholder Involvement** - Same 5 stakeholders × 2 cities
6. ✅ **Conflicting Requirements** - Cross-city resource sharing conflicts
7. ✅ **Interdependence** - Cross-city service dependencies

**Report Enhancement:**
- Can discuss inter-city failover scenarios
- Can analyze cross-city traffic patterns
- Can demonstrate metropolitan-scale design
- Can show how cities share resources (DHCP, DNS)

---

## 🎯 For Your Report

**Add these sections:**

### Chapter X: Metropolitan Network Design

> "This project extends the smart city infrastructure across two metropolitan areas (City A and City B), demonstrating scalability and inter-city connectivity. Each city operates autonomously with complete infrastructure (routers, switches, servers, IoT devices) while maintaining connectivity for resource sharing and redundancy."

### Inter-City Routing Analysis

> "Static routing was chosen over dynamic routing protocols (OSPF, EIGRP) for the inter-city link due to the simple topology (point-to-point connection). With only 2 cities, static routes provide deterministic paths without the overhead of routing protocol updates. Future expansion to 5+ cities would justify migrating to OSPF for automatic route convergence."

### Redundancy and Failover

> "The dual-city design provides service redundancy: if City A's DHCP server fails, City B's DHCP server can provide backup service by modifying helper-addresses on City A router. This demonstrates metropolitan-scale resilience, where critical services span geographic locations."

---

**Project Complete! You now have a comprehensive dual-city smart infrastructure network ready for demonstration and academic evaluation.** 🎉
