# PART 2: Smart City IoT Network - Complete Implementation Guide

> **Purpose:** Step-by-step instructions to build the complete Smart City IoT Network in Cisco Packet Tracer from start to finish. Following this guide will result in a fully functional network meeting all project requirements.

> **Prerequisites:** Cisco Packet Tracer 8.2.x or newer, PART 1 read for understanding WHY each step is done.

> **Estimated Time:** 3-4 hours for complete implementation

---

# Table of Contents

1. [Pre-Implementation Checklist](#1-pre-implementation-checklist)
2. [Phase 1: Device Placement](#2-phase-1-device-placement)
3. [Phase 2: Physical Connections](#3-phase-2-physical-connections)
4. [Phase 3: Core Router Configuration](#4-phase-3-core-router-configuration)
5. [Phase 4: Distribution Switch Configuration](#5-phase-4-distribution-switch-configuration)
6. [Phase 5: Access Switch Configuration](#6-phase-5-access-switch-configuration)
7. [Phase 6: Server Configuration](#7-phase-6-server-configuration)
8. [Phase 7: WiFi Access Point Configuration](#8-phase-7-wifi-access-point-configuration)
9. [Phase 8: End Device Configuration](#9-phase-8-end-device-configuration)
10. [Phase 9: QoS Configuration](#10-phase-9-qos-configuration)
11. [Phase 10: Testing and Validation](#11-phase-10-testing-and-validation)
12. [Phase 11: Documentation and Screenshots](#12-phase-11-documentation-and-screenshots)
13. [Troubleshooting Guide](#13-troubleshooting-guide)

---

# 1. Pre-Implementation Checklist

## 1.1 Software Requirements

✅ **Cisco Packet Tracer Version Check:**
1. Open Packet Tracer
2. Click **Help** → **About**
3. Verify version: 8.2.0 or newer
4. **Critical:** Versions before 8.2 may not have IoT devices

✅ **Computer Requirements:**
- RAM: Minimum 4GB (8GB recommended)
- Storage: 2GB free space
- OS: Windows 10/11, macOS 10.14+, or Ubuntu 18.04+

## 1.2 Knowledge Prerequisites

✅ **Before Starting, You Should Know:**
- Basic Cisco IOS commands (enable, configure terminal, interface, exit)
- How to use Packet Tracer interface (add devices, connect cables)
- Basic networking (IP addresses, subnet masks, default gateways)

✅ **If You're New to Packet Tracer:**
- Complete Packet Tracer tutorial: **Getting Started** → **Tutorials** → **Interface Overview** (15 minutes)

## 1.3 Reference Materials

✅ **Keep These Open While Working:**
1. **PART 1** (PROJECT_KNOWLEDGE.md) - for understanding WHY
2. This guide (PART 2) - for HOW
3. Notepad - for recording IP addresses and test results

## 1.4 Network Design Summary

**Quick Reference - What We're Building:**

```
                          ┌──────────────┐
                          │ Core-Router  │
                          │ (ISR4331 or  │
                          │  Cisco 2911) │
                          └──────┬───────┘
                    ┌────────────┴────────────┐
                    │                         │
            ┌───────▼──────┐          ┌──────▼───────┐
            │  Dist-SW-A   │          │  Dist-SW-B   │
            │(Catalyst 3650│          │(Catalyst 3650│
            │   or 2960)   │          │   or 2960)   │
            └──────┬───────┘          └──────┬───────┘
         ┌─────────┼─────────┐         ┌─────┼────────┐
         │         │         │         │     │        │
    ┌────▼──┐ ┌───▼───┐┌───▼───┐┌────▼──┐ ┌▼─────┐  │
    │Access │ │Access ││Access ││Access │ │Access│  │
    │ SW1   │ │  SW2  ││  SW3  ││  SW4  │ │ SW5  │  │
    │(VLAN  │ │(VLAN  ││(VLAN  ││(VLAN  │ │(VLAN │  │
    │  40)  │ │  10)  ││  20)  ││  30)  │ │ 30,50│  │
    └───┬───┘ └───┬───┘└───┬───┘└───┬───┘ └──┬───┘  │
        │         │        │        │         │      │
    Servers    8 IoT    Admin    WiFi      WiFi +   │
    (DNS,    Sensors   PCs/     Zone1     Mobile    │
    DHCP,              Laptops            Admin     │
    Email)
```

**Device Count:**
- 1 Core Router
- 2 Distribution Switches
- 5 Access Switches
- 3 Servers
- 8 IoT Devices
- 4 Admin PCs/Laptops
- 2 WiFi Access Points
- 5+ WiFi clients (smartphones, tablets)
- 3 Mobile Admin tablets

**Total: 33+ devices**

---

# 2. Phase 1: Device Placement (20 minutes)

## 2.1 Open Packet Tracer and Create New Project

1. Launch Cisco Packet Tracer
2. Click **File** → **New** (or press Ctrl+N)
3. Click **File** → **Save As**
4. Save as: `SmartCity_IoT_Network.pkt` in your Documents folder

## 2.2 Add Core Router

**Step 1:** Click the **Network Devices** icon (bottom left)
- Icon looks like: 🔲 (device rack)

**Step 2:** Click **Routers** category

**Step 3:** Select router model:
- **Preferred:** 2911 (most compatible with Packet Tracer)
- **Alternative:** ISR4331 (if available; newer model)
- **NOT recommended:** 1841, 2621XM (too old; limited interfaces)

**Step 4:** Drag router to **center of workspace**

**Step 5:** Label the router:
- Click router
- In left panel, click **Config** tab
- Under **GLOBAL Settings**, find **Display Name** field
- Enter: `Core-Router`
- Close device window

**Verification:**
✅ Router should display "Core-Router" label on workspace

---

## 2.3 Add Distribution Switches (2 devices)

**For Dist-SW-A:**

**Step 1:** Click **Network Devices** → **Switches**

**Step 2:** Select switch model:
- **Preferred:** 2960-24TT (24 Fast Ethernet ports + 2 Gig uplinks)
- **Alternative:** 3560-24PS (if available; supports more features)
- **NOT recommended:** 2950-24 (EOL model; limited features)

**Step 3:** Drag switch to **left side, below router**

**Step 4:** Label as `Dist-SW-A`

**For Dist-SW-B:**

**Step 5:** Add another switch (same model)

**Step 6:** Drag to **right side, below router**

**Step 7:** Label as `Dist-SW-B`

**Workspace Layout Check:**
```
        [Core-Router]
           /      \
          /        \
  [Dist-SW-A]    [Dist-SW-B]
```

---

## 2.4 Add Access Switches (5 devices)

**Repeat this process 5 times:**

1. Click **Network Devices** → **Switches**
2. Select **2960-24TT** (same as distribution switches for consistency)
3. Drag to workspace below distribution switches
4. Label switches:
   - `Access-SW1` (below Dist-SW-A, left position)
   - `Access-SW2` (below Dist-SW-A, middle position)
   - `Access-SW3` (below Dist-SW-A, right position)
   - `Access-SW4` (below Dist-SW-B, left position)
   - `Access-SW5` (below Dist-SW-B, right position)

**Workspace Layout Check:**
```
              [Core-Router]
                 /      \
                /        \
        [Dist-SW-A]    [Dist-SW-B]
          /  |  \        /       \
         /   |   \      /         \
  [Access] [Access] [Access] [Access] [Access]
   -SW1     -SW2     -SW3     -SW4     -SW5
```

---

## 2.5 Add Servers (3 devices)

**Step 1:** Click **End Devices** icon (bottom left)
- Icon looks like: 🖥️ (computer)

**Step 2:** Click **Server** category

**Step 3:** Drag **Server-PT** (generic server) to workspace
- Place below Access-SW1

**Step 4:** Label as `DNS-Server`

**Step 5:** Add second server, label as `DHCP-Server`

**Step 6:** Add third server, label as `Email-Server`

**Arrangement:**
```
[Access-SW1]
  |  |  |
 DNS DHCP Email
```

---

## 2.6 Add IoT Devices (8 devices)

**Step 1:** Click **End Devices** → **IoT Devices** (if available)
- If no IoT category: Use **Single Board Computer (SBC)** or **Laptop-PT** as substitutes

**Option A: If IoT Devices Available**

**Traffic Sensors (3 devices):**
1. Drag **Motion Detector** or **Environmental Monitor** to workspace
2. Place below Access-SW2
3. Label: `IoT-Traffic-1`, `IoT-Traffic-2`, `IoT-Traffic-3`

**Environmental Monitors (2 devices):**
4. Drag **Environmental Monitor**
5. Label: `IoT-Env-1`, `IoT-Env-2`

**Smart Cameras (2 devices):**
6. Drag **Webcam** or **Security Camera**
7. Label: `IoT-Camera-1`, `IoT-Camera-2`

**Smart Lighting (1 device):**
8. Drag **Smart Home Device** or **Light**
9. Label: `IoT-Light-1`

**Option B: If No IoT Devices (Substitute with PCs)**
- Use **PC-PT** devices
- Configure as "simulated IoT" (we'll configure later)
- Label as above

**Arrangement:**
```
[Access-SW2]
  |  |  |  |  |  |  |  |
 T1 T2 T3 E1 E2 C1 C2 L1
 (Traffic) (Env) (Cam)(Light)
```

---

## 2.7 Add Admin Devices (4 devices)

**Step 1:** Click **End Devices**

**Admin PCs (2 devices):**
1. Drag **PC-PT** below Access-SW3
2. Label: `Admin-PC-1`, `Admin-PC-2`

**Admin Laptops (2 devices):**
3. Drag **Laptop-PT** below Access-SW3
4. Label: `Admin-Laptop-1`, `Admin-Laptop-2`

**Arrangement:**
```
[Access-SW3]
  |  |  |  |
 PC1 PC2 L1 L2
```

---

## 2.8 Add WiFi Access Points (2 devices)

**Step 1:** Click **Network Devices** → **Wireless Devices**

**Step 2:** Select **AccessPoint-PT** (generic AP)
- Alternative: **Linksys WRT300N** (wireless router in AP mode)

**WiFi-Zone1:**
3. Drag to workspace below Access-SW4
4. Label: `WiFi-Zone1`

**WiFi-Zone2:**
5. Drag to workspace below Access-SW5
6. Label: `WiFi-Zone2`

**Arrangement:**
```
[Access-SW4]    [Access-SW5]
      |              |
  [WiFi-Z1]      [WiFi-Z2]
```

---

## 2.9 Add Mobile Devices (8+ devices)

**Mobile Admin Tablets (3 wired devices on Access-SW5):**
1. Click **End Devices** → **Tablet-PT**
2. Drag 3 tablets below Access-SW5
3. Label: `Tablet-Admin-1`, `Tablet-Admin-2`, `Tablet-Admin-3`

**WiFi Clients (5+ wireless devices):**

**Smartphones (3 devices):**
4. Drag **Smartphone-PT** to workspace (near WiFi-Zone1 and WiFi-Zone2)
5. Label: `Phone-1`, `Phone-2`, `Phone-3`

**Tablets (2 devices):**
6. Drag **Tablet-PT** to workspace (near WiFi access points)
7. Label: `Tablet-Public-1`, `Tablet-Public-2`

**Note:** Wireless devices don't need to be "near" APs visually; WiFi will work anywhere

**Final Device Count Verification:**

| Type | Quantity | Labels |
|------|----------|--------|
| Routers | 1 | Core-Router |
| Distribution Switches | 2 | Dist-SW-A, Dist-SW-B |
| Access Switches | 5 | Access-SW1 through Access-SW5 |
| Servers | 3 | DNS-Server, DHCP-Server, Email-Server |
| IoT Devices | 8 | IoT-Traffic-1, IoT-Traffic-2, IoT-Traffic-3, IoT-Env-1, IoT-Env-2, IoT-Camera-1, IoT-Camera-2, IoT-Light-1 |
| Admin PCs/Laptops | 4 | Admin-PC-1, Admin-PC-2, Admin-Laptop-1, Admin-Laptop-2 |
| WiFi Access Points | 2 | WiFi-Zone1, WiFi-Zone2 |
| Mobile Admin Tablets | 3 | Tablet-Admin-1, Tablet-Admin-2, Tablet-Admin-3 |
| Wireless Clients | 5 | Phone-1, Phone-2, Phone-3, Tablet-Public-1, Tablet-Public-2 |
| **TOTAL** | **33** | |

✅ **Checkpoint:** Save project (Ctrl+S)

---

# 3. Phase 2: Physical Connections (30 minutes)

## 3.1 Cable Types Reference

**Before Connecting, Understand Cable Types:**

| Cable Type | Icon | Use Case | In This Project |
|------------|------|----------|-----------------|
| **Copper Straight-Through** | —— (solid line) | Device to switch | PC to switch, Router to switch |
| **Copper Cross-Over** | ╳ (X line) | Switch to switch, Router to router | ONLY if auto-MDI/MDIX disabled |
| **Fiber Optic** | ))) | Long distance, high speed | Not used (optional enhancement) |
| **Console** | ~~~ (wavy) | Management access | Not needed in simulation |

**Packet Tracer Auto-MDI/MDIX:**
- Modern switches automatically detect cable type
- **Recommendation:** Use **Copper Straight-Through** for ALL connections
- Packet Tracer will auto-correct if wrong cable used

---

## 3.2 Connect Core Router to Distribution Switches

**Connection 1: Core-Router to Dist-SW-A**

**Step 1:** Click **Connections** icon (bottom left, lightning bolt symbol)

**Step 2:** Select **Copper Straight-Through** (solid black line)

**Step 3:** Click **Core-Router**
- A window appears showing available interfaces

**Step 4:** Select router interface:
- **If using 2911:** Select `GigabitEthernet0/0`
- **If using ISR4331:** Select `GigabitEthernet0/0/0`

**Step 5:** Click **Dist-SW-A**

**Step 6:** Select switch interface: `GigabitEthernet1/0/1`
- Why Gig1/0/1? Uplink port (faster than Fast Ethernet)

**Verification:**
- Green line appears connecting devices
- Initially shows orange dots (ports are down)
- Wait 30 seconds → dots turn green (ports come up)

**Connection 2: Core-Router to Dist-SW-B**

**Step 7:** Repeat process:
- **Router interface:**
  - 2911: `GigabitEthernet0/1`
  - ISR4331: `GigabitEthernet0/0/1`
- **Switch interface:** `GigabitEthernet1/0/1` on Dist-SW-B

**Checkpoint:**
```
      [Core-Router]
       Gig0/0│ │Gig0/1
              │ │
   Gig1/0/1   │ │  Gig1/0/1
    [Dist-SW-A] [Dist-SW-B]
```

✅ **Verify:** 2 green lines from router to switches

---

## 3.3 Connect Distribution Switches to Access Switches

**Dist-SW-A Connections:**

**Connection 3: Dist-SW-A to Access-SW1 (Servers VLAN 40)**

1. Select **Copper Straight-Through** cable
2. Click **Dist-SW-A** → Select `FastEthernet1/0/1`
3. Click **Access-SW1** → Select `FastEthernet0/24` (uplink port)

**Connection 4: Dist-SW-A to Access-SW2 (IoT VLAN 10)**

4. **Dist-SW-A** `FastEthernet1/0/2` ↔ **Access-SW2** `FastEthernet0/24`

**Connection 5: Dist-SW-A to Access-SW3 (Admin VLAN 20)**

5. **Dist-SW-A** `FastEthernet1/0/3` ↔ **Access-SW3** `FastEthernet0/24`

**Dist-SW-B Connections:**

**Connection 6: Dist-SW-B to Access-SW4 (WiFi VLAN 30)**

6. **Dist-SW-B** `FastEthernet1/0/1` ↔ **Access-SW4** `FastEthernet0/24`

**Connection 7: Dist-SW-B to Access-SW5 (WiFi + Mobile Admin VLANs 30,50)**

7. **Dist-SW-B** `FastEthernet1/0/2` ↔ **Access-SW5** `FastEthernet0/24`

**Checkpoint Diagram:**
```
       [Core-Router]
          /      \
   [Dist-SW-A]  [Dist-SW-B]
      /  |  \      /    \
    SW1 SW2 SW3  SW4   SW5
```

✅ **Verify:** 5 green lines from distribution to access layer

---

## 3.4 Connect End Devices to Access Switches

### Access-SW1: Servers (VLAN 40)

**Connection 8-10: Servers**

1. **DNS-Server** → **Access-SW1** port `FastEthernet0/1`
2. **DHCP-Server** → **Access-SW1** port `FastEthernet0/2`
3. **Email-Server** → **Access-SW1** port `FastEthernet0/3`

**Cable:** Copper Straight-Through
**Server Interface:** FastEthernet0 (default on Server-PT)

---

### Access-SW2: IoT Devices (VLAN 10)

**Connection 11-18: IoT Sensors**

| Device | Switch Port |
|--------|-------------|
| IoT-Traffic-1 | FastEthernet0/1 |
| IoT-Traffic-2 | FastEthernet0/2 |
| IoT-Traffic-3 | FastEthernet0/3 |
| IoT-Env-1 | FastEthernet0/4 |
| IoT-Env-2 | FastEthernet0/5 |
| IoT-Camera-1 | FastEthernet0/6 |
| IoT-Camera-2 | FastEthernet0/7 |
| IoT-Light-1 | FastEthernet0/8 |

**Cable:** Copper Straight-Through
**IoT Interface:** FastEthernet0 (or Ethernet0 if IoT device)

---

### Access-SW3: Admin Devices (VLAN 20)

**Connection 19-22: Admin PCs and Laptops**

| Device | Switch Port |
|--------|-------------|
| Admin-PC-1 | FastEthernet0/1 |
| Admin-PC-2 | FastEthernet0/2 |
| Admin-Laptop-1 | FastEthernet0/3 |
| Admin-Laptop-2 | FastEthernet0/4 |

**Cable:** Copper Straight-Through
**PC/Laptop Interface:** FastEthernet0

---

### Access-SW4: WiFi Access Point (VLAN 30)

**Connection 23: WiFi-Zone1**

1. **WiFi-Zone1** → **Access-SW4** port `FastEthernet0/1`

**Cable:** Copper Straight-Through
**AP Interface:** Port 1 (Ethernet)

---

### Access-SW5: WiFi + Mobile Admin (VLANs 30, 50)

**Connection 24: WiFi-Zone2**

1. **WiFi-Zone2** → **Access-SW5** port `FastEthernet0/1`

**Connection 25-27: Mobile Admin Tablets (Wired)**

| Device | Switch Port |
|--------|-------------|
| Tablet-Admin-1 | FastEthernet0/2 |
| Tablet-Admin-2 | FastEthernet0/3 |
| Tablet-Admin-3 | FastEthernet0/4 |

**Cable:** Copper Straight-Through
**Tablet Interface:** FastEthernet0 or Wireless0 (choose wired)

---

## 3.5 Wireless Connections (Configured Later)

**Do NOT connect cables to:**
- Phone-1, Phone-2, Phone-3
- Tablet-Public-1, Tablet-Public-2

These will connect wirelessly after WiFi configuration (Phase 8).

---

## 3.6 Physical Topology Verification

**Final Connection Count:**

| Layer | Connections | Status |
|-------|-------------|--------|
| Core → Distribution | 2 | ✅ |
| Distribution → Access | 5 | ✅ |
| Access → End Devices | 20 | ✅ |
| **Total Wired** | **27** | ✅ |
| Wireless (pending) | 5 | ⏳ Phase 8 |

**Visual Check:**
1. Click **Logical** workspace view (bottom toolbar)
2. All wired connections should show **green triangles** on both ends
3. If orange triangles: Wait 30-60 seconds (ports coming up)
4. If red X: Check cable type and interface selection

✅ **Checkpoint:** Save project (Ctrl+S)

---

# 4. Phase 3: Core Router Configuration (45 minutes)

## 4.1 Important: Interface Naming

**CRITICAL: Verify your router model's interface names BEFORE starting**

**Step 1:** Click **Core-Router** device

**Step 2:** Click **CLI** tab

**Step 3:** Press Enter, type:
```
enable
show ip interface brief
```

**Expected Output (Example for 2911):**
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up
GigabitEthernet0/1     unassigned      YES unset  up                    up
GigabitEthernet0/2     unassigned      YES unset  down                  down
```

**Expected Output (Example for ISR4331):**
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   unassigned      YES unset  up                    up
GigabitEthernet0/0/1   unassigned      YES unset  up                    up
```

**Determine Your Interface Format:**
- See `GigabitEthernet0/0` → Use format: `Gig0/0`, `Gig0/1`
- See `GigabitEthernet0/0/0` → Use format: `Gig0/0/0`, `Gig0/0/1`

**For This Guide:**
- **Commands below use 2911 format** (`Gig0/0`)
- **If you have ISR4331:** Change `Gig0/0` → `Gig0/0/0` and `Gig0/1` → `Gig0/0/1`

---

## 4.2 Base Router Configuration

**Step 1:** Enter privileged mode and global configuration:

```cisco
enable
configure terminal
```

**Step 2:** Set hostname:

```cisco
hostname Core-Router
```

**Verification:** Prompt changes to `Core-Router(config)#` ✅

**Step 3:** Enable routing:

```cisco
ip routing
ipv6 unicast-routing
```

**Purpose:**
- `ip routing`: Enable IPv4 routing (default ON, but explicit is good practice)
- `ipv6 unicast-routing`: Enable IPv6 routing (required for IPv6)

---

## 4.3 Configure Physical Interfaces

### Interface to Distribution Switch A

**Step 1:** Enter interface configuration mode:

```cisco
interface GigabitEthernet0/0
```

*(If ISR4331, use `interface GigabitEthernet0/0/0`)*

**Step 2:** Configure interface:

```cisco
 description Link to Dist-SW-A
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1000:1::1/64
 no shutdown
 exit
```

**Explanation:**
- `description`: Documentation (shows in `show interfaces`)
- `ip address`: IPv4 address (default gateway for VLAN traffic)
- `ipv6 address`: IPv6 address (dual-stack)
- `no shutdown`: Enable interface (interfaces are shutdown by default)

**Verification:**

```cisco
show ip interface brief | include GigabitEthernet0/0
```

**Expected Output:**
```
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
```

✅ Status = up, Protocol = up

---

### Interface to Distribution Switch B

**Step 3:** Configure second physical interface:

```cisco
interface GigabitEthernet0/1
```

*(If ISR4331, use `interface GigabitEthernet0/0/1`)*

```cisco
 description Link to Dist-SW-B
 ip address 192.168.2.1 255.255.255.0
 ipv6 address 2001:db8:1000:2::1/64
 no shutdown
 exit
```

**Verification:**

```cisco
show ip interface brief | include GigabitEthernet0/1
```

**Expected Output:**
```
GigabitEthernet0/1     192.168.2.1     YES manual up                    up
```

✅ Both physical interfaces UP

---

## 4.4 Configure VLAN Subinterfaces (Router-on-a-Stick)

**Concept:** VLANs need separate IP subnets; create subinterfaces on router for inter-VLAN routing.

### VLAN 10: IoT Sensors (on Gig0/0)

**Step 1:** Create subinterface:

```cisco
interface GigabitEthernet0/0.10
```

*(If ISR4331, use `interface GigabitEthernet0/0/0.10`)*

**Step 2:** Configure subinterface:

```cisco
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

**Explanation:**
- `encapsulation dot1Q 10`: Tag traffic with VLAN 10 (802.1Q standard)
- `ip address 192.168.10.1`: Default gateway for IoT devices
- `ip helper-address 192.168.40.20`: Forward DHCP broadcasts to DHCP server
- `no shutdown`: Enable subinterface (inherit from physical interface, but explicit is safe)

---

### VLAN 20: Administrative (on Gig0/0)

**Step 3:** Create Admin VLAN subinterface:

```cisco
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

---

### VLAN 40: Servers (on Gig0/0)

**Step 4:** Create Server VLAN subinterface:

```cisco
interface GigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown
 exit
```

**Note:** No `ip helper-address` on VLAN 40 (servers have static IPs; no DHCP needed)

---

### VLAN 30: Public WiFi (on Gig0/1)

**Step 5:** Create Public WiFi subinterface:

```cisco
interface GigabitEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

---

### VLAN 50: Mobile Admin (on Gig0/1)

**Step 6:** Create Mobile Admin subinterface:

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

## 4.5 Verify Subinterfaces

**Step 7:** Check all interfaces:

```cisco
show ip interface brief
```

**Expected Output:**
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/0.10  192.168.10.1    YES manual up                    up
GigabitEthernet0/0.20  192.168.20.1    YES manual up                    up
GigabitEthernet0/0.40  192.168.40.1    YES manual up                    up
GigabitEthernet0/1     192.168.2.1     YES manual up                    up
GigabitEthernet0/1.30  192.168.30.1    YES manual up                    up
GigabitEthernet0/1.50  192.168.50.1    YES manual up                    up
```

✅ **Verify:**
- 2 physical interfaces (Gig0/0, Gig0/1)
- 5 subinterfaces (.10, .20, .30, .40, .50)
- All Status = up, Protocol = up

**Step 8:** Check IPv6:

```cisco
show ipv6 interface brief
```

**Expected Output:**
```
GigabitEthernet0/0         [up/up]
    FE80::...
    2001:DB8:1000:1::1
GigabitEthernet0/0.10      [up/up]
    FE80::...
    2001:DB8:1000:10::1
...
```

✅ Each interface should show link-local (FE80::) + global IPv6 address

---

## 4.6 Configure Access Control Lists (ACLs)

### ACL 110: IoT Sensor Security

**Purpose:** Allow IoT to servers/admin, block IoT to public WiFi

**Step 1:** Create ACL:

```cisco
access-list 110 remark IoT-Sensor-Security-Policy
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
access-list 110 permit ip any any
```

**Explanation:**
- Line 1: Remark (comment for documentation)
- Line 2: Permit IoT (192.168.10.0/24) to Servers (192.168.40.0/24)
- Line 3: Permit IoT to Admin (192.168.20.0/24)
- Line 4: Deny IoT to Public WiFi (192.168.30.0/24), log attempts
- Line 5: Permit all other traffic (e.g., IoT to internet)

---

### ACL 130: Public WiFi Security

**Purpose:** Allow public web browsing, block access to internal networks

**Step 2:** Create ACL:

```cisco
access-list 130 remark Public-WiFi-Security-Policy
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 80
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 443
access-list 130 permit udp 192.168.30.0 0.0.0.255 192.168.40.10 0.0.0.0 eq 53
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.40.0 0.0.0.255 log
access-list 130 permit ip any any
```

**Explanation:**
- Line 2: Permit HTTP (port 80) to anywhere
- Line 3: Permit HTTPS (port 443) to anywhere
- Line 4: Permit DNS (port 53 UDP) to DNS server (192.168.40.10) ONLY
- Line 5: Deny public to IoT, log attempts
- Line 6: Deny public to Admin, log attempts
- Line 7: Deny public to Servers (except DNS already allowed), log attempts
- Line 8: Permit all other (internet access)

---

## 4.7 Apply ACLs to Interfaces

**Step 3:** Apply ACL 110 to IoT VLAN:

```cisco
interface GigabitEthernet0/0.10
 ip access-group 110 in
 exit
```

**Explanation:**
- `ip access-group 110 in`: Apply ACL 110 to inbound traffic (traffic FROM IoT devices)

**Step 4:** Apply ACL 130 to Public WiFi VLAN:

```cisco
interface GigabitEthernet0/1.30
 ip access-group 130 in
 exit
```

---

## 4.8 Verify ACL Configuration

**Step 5:** Check ACLs:

```cisco
show access-lists
```

**Expected Output:**
```
Extended IP access list 110
    10 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
    20 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
    30 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
    40 permit ip any any (XX matches)

Extended IP access list 130
    10 permit tcp 192.168.30.0 0.0.0.255 any eq www
    20 permit tcp 192.168.30.0 0.0.0.255 any eq 443
    30 permit udp 192.168.30.0 0.0.0.255 host 192.168.40.10 eq domain
    40 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log
    50 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255 log
    60 deny ip 192.168.30.0 0.0.0.255 192.168.40.0 0.0.0.255 log
    70 permit ip any any
```

✅ **Verify:** ACL lines match configuration

**Step 6:** Check ACL application:

```cisco
show ip interface GigabitEthernet0/0.10 | include access list
```

**Expected Output:**
```
  Inbound  access list is 110
  Outbound access list is not set
```

✅ ACL 110 applied inbound to VLAN 10

---

## 4.9 Save Router Configuration

**Step 7:** Exit configuration mode:

```cisco
end
```

**Step 8:** Save configuration:

```cisco
write memory
```

OR

```cisco
copy running-config startup-config
```

**Expected Output:**
```
Building configuration...
[OK]
```

✅ Configuration saved (survives router reload)

---

## 4.10 Core Router Configuration Summary

**Interfaces Configured:**
- ✅ Gig0/0 (to Dist-SW-A): 192.168.1.1
- ✅ Gig0/1 (to Dist-SW-B): 192.168.2.1
- ✅ Gig0/0.10 (VLAN 10 IoT): 192.168.10.1
- ✅ Gig0/0.20 (VLAN 20 Admin): 192.168.20.1
- ✅ Gig0/0.40 (VLAN 40 Servers): 192.168.40.1
- ✅ Gig0/1.30 (VLAN 30 Public WiFi): 192.168.30.1
- ✅ Gig0/1.50 (VLAN 50 Mobile Admin): 192.168.50.1

**ACLs Configured:**
- ✅ ACL 110 (IoT security) - applied to Gig0/0.10
- ✅ ACL 130 (Public WiFi security) - applied to Gig0/1.30

**Helper Addresses:**
- ✅ VLANs 10, 20, 30, 50 forward DHCP to 192.168.40.20

**IPv6:**
- ✅ Routing enabled
- ✅ All interfaces have IPv6 addresses

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 5. Phase 4: Distribution Switch Configuration (30 minutes)

## 5.1 Distribution Switch A Configuration

**Purpose:** Carries VLANs 10 (IoT), 20 (Admin), 40 (Servers) between access layer and core router

**Step 1:** Click **Dist-SW-A** → **CLI** tab

**Step 2:** Enter configuration mode:

```cisco
enable
configure terminal
hostname Dist-SW-A
```

---

### Create VLANs

**Step 3:** Create required VLANs:

```cisco
vlan 10
 name IoT-Sensors
 exit

vlan 20
 name Administrative
 exit

vlan 40
 name Servers
 exit
```

**Explanation:**
- `vlan 10`: Create VLAN 10
- `name IoT-Sensors`: Label for documentation (shows in `show vlan`)

**Verification:**

```cisco
show vlan brief
```

**Expected Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa1/0/4, Fa1/0/5, ...
10   IoT-Sensors                      active
20   Administrative                   active
40   Servers                          active
```

✅ VLANs 10, 20, 40 exist (no ports assigned yet)

---

### Configure Trunk to Core Router

**Step 4:** Configure uplink to Core-Router:

```cisco
interface GigabitEthernet1/0/1
 description Trunk to Core-Router
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,40
 no shutdown
 exit
```

**Explanation:**
- `switchport trunk encapsulation dot1q`: Use 802.1Q tagging
  - **Note:** Some switch models (2960) don't need this command (only support dot1Q)
  - If error: "Invalid input", skip this line (2960 series)
- `switchport mode trunk`: Set port as trunk (carries multiple VLANs)
- `switchport trunk allowed vlan 10,20,40`: Only allow specific VLANs (security)
- `no shutdown`: Enable interface

**Verification:**

```cisco
show interfaces trunk
```

**Expected Output:**
```
Port        Mode         Encapsulation  Status        Native vlan
Gig1/0/1    on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gig1/0/1    10,20,40

Port        Vlans allowed and active in management domain
Gig1/0/1    10,20,40
```

✅ Trunk operational, carrying VLANs 10,20,40

---

### Configure Trunks to Access Switches

**Step 5:** Configure trunk to Access-SW1 (Servers):

```cisco
interface FastEthernet1/0/1
 description Trunk to Access-SW1 (Servers)
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit
```

**Step 6:** Configure trunk to Access-SW2 (IoT):

```cisco
interface FastEthernet1/0/2
 description Trunk to Access-SW2 (IoT)
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit
```

**Step 7:** Configure trunk to Access-SW3 (Admin):

```cisco
interface FastEthernet1/0/3
 description Trunk to Access-SW3 (Admin)
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit
```

**Verification:**

```cisco
show interfaces trunk
```

**Expected Output:**
```
Port        Mode         Encapsulation  Status        Native vlan
Fa1/0/1     on           802.1q         trunking      1
Fa1/0/2     on           802.1q         trunking      1
Fa1/0/3     on           802.1q         trunking      1
Gig1/0/1    on           802.1q         trunking      1
```

✅ 4 trunk ports operational

---

### Save Configuration

**Step 8:** Exit and save:

```cisco
end
write memory
```

**Expected Output:**
```
Building configuration...
[OK]
```

✅ **Dist-SW-A configured**

---

## 5.2 Distribution Switch B Configuration

**Purpose:** Carries VLANs 30 (Public WiFi), 50 (Mobile Admin)

**Step 1:** Click **Dist-SW-B** → **CLI** tab

**Step 2:** Enter configuration mode:

```cisco
enable
configure terminal
hostname Dist-SW-B
```

---

### Create VLANs

**Step 3:** Create VLANs:

```cisco
vlan 30
 name Public-WiFi
 exit

vlan 50
 name Mobile-Admin
 exit
```

**Verification:**

```cisco
show vlan brief
```

**Expected Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    ...
30   Public-WiFi                      active
50   Mobile-Admin                     active
```

✅ VLANs 30, 50 created

---

### Configure Trunk to Core Router

**Step 4:** Configure uplink:

```cisco
interface GigabitEthernet1/0/1
 description Trunk to Core-Router
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit
```

**Note:** Skip `switchport trunk encapsulation dot1q` if you get an error (2960 switches)

---

### Configure Trunks to Access Switches

**Step 5:** Configure trunk to Access-SW4 (WiFi Zone 1):

```cisco
interface FastEthernet1/0/1
 description Trunk to Access-SW4 (WiFi-Zone1)
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit
```

**Step 6:** Configure trunk to Access-SW5 (WiFi Zone 2 + Mobile Admin):

```cisco
interface FastEthernet1/0/2
 description Trunk to Access-SW5 (WiFi-Zone2 and Mobile-Admin)
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit
```

**Verification:**

```cisco
show interfaces trunk
```

**Expected Output:**
```
Port        Mode         Encapsulation  Status        Native vlan
Fa1/0/1     on           802.1q         trunking      1
Fa1/0/2     on           802.1q         trunking      1
Gig1/0/1    on           802.1q         trunking      1

Port        Vlans allowed on trunk
Fa1/0/1     30
Fa1/0/2     30,50
Gig1/0/1    30,50
```

✅ Trunks operational

---

### Save Configuration

**Step 7:** Exit and save:

```cisco
end
write memory
```

✅ **Dist-SW-B configured**

---

## 5.3 Distribution Layer Summary

**Dist-SW-A:**
- ✅ VLANs: 10, 20, 40
- ✅ Trunk to Core-Router (Gig1/0/1)
- ✅ Trunk to Access-SW1 (Fa1/0/1, VLAN 40)
- ✅ Trunk to Access-SW2 (Fa1/0/2, VLAN 10)
- ✅ Trunk to Access-SW3 (Fa1/0/3, VLAN 20)

**Dist-SW-B:**
- ✅ VLANs: 30, 50
- ✅ Trunk to Core-Router (Gig1/0/1)
- ✅ Trunk to Access-SW4 (Fa1/0/1, VLAN 30)
- ✅ Trunk to Access-SW5 (Fa1/0/2, VLANs 30,50)

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 6. Phase 5: Access Switch Configuration (45 minutes)

*(Continuing from previous sections...)*

## 6.1 Access-SW1: Servers (VLAN 40)

**Step 1:** Click **Access-SW1** → **CLI** tab

**Step 2:** Enter configuration:

```cisco
enable
configure terminal
hostname Access-SW1

vlan 40
 name Servers
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-A
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

**Verification:**

```cisco
show vlan brief
```

**Expected Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/4, Fa0/5, ...
40   Servers                          active    Fa0/1, Fa0/2, Fa0/3
```

✅ Ports Fa0/1-3 in VLAN 40

---

## 6.2 Access-SW2: IoT Sensors (VLAN 10)

**Step 1:** Click **Access-SW2** → **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW2

vlan 10
 name IoT-Sensors
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-A
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit

interface range FastEthernet0/1-8
 description IoT Device Ports
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Verification:**

```cisco
show vlan brief
```

**Expected Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/9, Fa0/10, ...
10   IoT-Sensors                      active    Fa0/1, Fa0/2, ..., Fa0/8
```

✅ Ports Fa0/1-8 in VLAN 10

---

## 6.3 Access-SW3: Administrative (VLAN 20)

```cisco
enable
configure terminal
hostname Access-SW3

vlan 20
 name Administrative
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-A
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

interface range FastEthernet0/1-4
 description Admin Device Ports
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

✅ Ports Fa0/1-4 in VLAN 20

---

## 6.4 Access-SW4: WiFi Zone 1 (VLAN 30)

```cisco
enable
configure terminal
hostname Access-SW4

vlan 30
 name Public-WiFi
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-B
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit

interface FastEthernet0/1
 description WiFi-Zone1 Access Point
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

✅ Port Fa0/1 in VLAN 30

---

## 6.5 Access-SW5: WiFi Zone 2 + Mobile Admin (VLANs 30, 50)

```cisco
enable
configure terminal
hostname Access-SW5

vlan 30
 name Public-WiFi
 exit

vlan 50
 name Mobile-Admin
 exit

interface FastEthernet0/24
 description Trunk to Dist-SW-B
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

interface FastEthernet0/1
 description WiFi-Zone2 Access Point
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

interface range FastEthernet0/2-4
 description Mobile Admin Tablets
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

**Verification:**

```cisco
show vlan brief
```

**Expected Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/5, Fa0/6, ...
30   Public-WiFi                      active    Fa0/1
50   Mobile-Admin                     active    Fa0/2, Fa0/3, Fa0/4
```

✅ VLAN 30 on Fa0/1, VLAN 50 on Fa0/2-4

---

## 6.6 Access Layer Summary

| Switch | VLANs | Access Ports | Trunk Port |
|--------|-------|--------------|------------|
| Access-SW1 | 40 | Fa0/1-3 (Servers) | Fa0/24 (to Dist-SW-A) |
| Access-SW2 | 10 | Fa0/1-8 (IoT) | Fa0/24 (to Dist-SW-A) |
| Access-SW3 | 20 | Fa0/1-4 (Admin) | Fa0/24 (to Dist-SW-A) |
| Access-SW4 | 30 | Fa0/1 (WiFi AP) | Fa0/24 (to Dist-SW-B) |
| Access-SW5 | 30, 50 | Fa0/1 (WiFi AP), Fa0/2-4 (Mobile Admin) | Fa0/24 (to Dist-SW-B) |

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 7. Phase 6: Server Configuration (30 minutes)

## 7.1 DNS Server Configuration

**Step 1:** Click **DNS-Server** device

**Step 2:** Click **Desktop** tab → **IP Configuration**

**Step 3:** Configure static IP:

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.10 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::10 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

**Step 4:** Click **Services** tab → **DNS**

**Step 5:** Turn DNS Service **ON**

**Step 6:** Add DNS records:

| Name | Address | Type |
|------|---------|------|
| core-router.smart-city.local | 192.168.1.1 | A |
| dhcp.smart-city.local | 192.168.40.20 | A |
| email.smart-city.local | 192.168.40.30 | A |
| dns.smart-city.local | 192.168.40.10 | A |

**For each record:**
1. Enter **Name** field
2. Enter **Address** field
3. Click **Add**

**Verification:** Entries appear in DNS table

✅ DNS Server configured

---

## 7.2 DHCP Server Configuration

**Step 1:** Click **DHCP-Server** device

**Step 2:** Click **Desktop** → **IP Configuration**

**Step 3:** Configure static IP:

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.20 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::20 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

**Step 4:** Click **Services** tab → **DHCP**

---

### DHCP Pool 1: IoT Sensors (VLAN 10)

**Step 5:** Configure IoT pool:

| Field | Value |
|-------|-------|
| Pool Name | IoT_SENSORS |
| Default Gateway | 192.168.10.1 |
| DNS Server | 192.168.40.10 |
| Start IP Address | 192.168.10.100 |
| Subnet Mask | 255.255.255.0 |
| Maximum Number of Users | 50 |

**Click "Add"**

---

### DHCP Pool 2: Administrative (VLAN 20)

**Step 6:** Configure Admin pool:

| Field | Value |
|-------|-------|
| Pool Name | ADMIN_DEVICES |
| Default Gateway | 192.168.20.1 |
| DNS Server | 192.168.40.10 |
| Start IP Address | 192.168.20.100 |
| Subnet Mask | 255.255.255.0 |
| Maximum Number of Users | 20 |

**Click "Add"**

---

### DHCP Pool 3: Public WiFi (VLAN 30)

**Step 7:** Configure Public WiFi pool:

| Field | Value |
|-------|-------|
| Pool Name | PUBLIC_WIFI |
| Default Gateway | 192.168.30.1 |
| DNS Server | 192.168.40.10 |
| Start IP Address | 192.168.30.100 |
| Subnet Mask | 255.255.255.0 |
| Maximum Number of Users | 100 |

**Click "Add"**

---

### DHCP Pool 4: Mobile Admin (VLAN 50)

**Step 8:** Configure Mobile Admin pool:

| Field | Value |
|-------|-------|
| Pool Name | MOBILE_ADMIN |
| Default Gateway | 192.168.50.1 |
| DNS Server | 192.168.40.10 |
| Start IP Address | 192.168.50.100 |
| Subnet Mask | 255.255.255.0 |
| Maximum Number of Users | 20 |

**Click "Add"**

**Verification:** 4 pools appear in DHCP service list

✅ DHCP Server configured with 4 pools

---

## 7.3 Email Server Configuration

**Step 1:** Click **Email-Server** device

**Step 2:** Click **Desktop** → **IP Configuration**

**Step 3:** Configure static IP:

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.40.30 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.40.1 |
| DNS Server | 192.168.40.10 |
| IPv6 Address | 2001:db8:1000:40::30 |
| IPv6 Gateway | 2001:db8:1000:40::1 |

**Step 4:** Click **Services** tab → **EMAIL**

**Step 5:** Configure email service:

| Field | Value |
|-------|-------|
| Domain Name | smart-city.local |

**Step 6:** Add users:

**User 1:**
- User: `admin`
- Password: `admin123`
- Click **+** button

**User 2:**
- User: `operations`
- Password: `ops123`
- Click **+** button

**Verification:** Users appear in user list

✅ Email Server configured

---

## 7.4 Server Configuration Summary

| Server | IP Address | Services | Status |
|--------|------------|----------|--------|
| DNS-Server | 192.168.40.10 | DNS (4 records) | ✅ |
| DHCP-Server | 192.168.40.20 | DHCP (4 pools) | ✅ |
| Email-Server | 192.168.40.30 | SMTP (2 users) | ✅ |

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 8. Phase 7: WiFi Access Point Configuration (20 minutes)

## 8.1 WiFi-Zone1 Configuration

**Step 1:** Click **WiFi-Zone1** access point

**Step 2:** Click **Config** tab

**Step 3:** Configure network settings:

- Click **Port 1** (or **Interface** if different model)

| Field | Value |
|-------|-------|
| IP Configuration | Static |
| IP Address | 192.168.30.50 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.30.1 |
| DNS Server | 192.168.40.10 |

**Step 4:** Configure wireless settings:

- Click **Wireless** or **Port 1** → **Wireless** section

| Field | Value |
|-------|-------|
| SSID | SmartCity_Zone1 |
| Authentication | WPA2-PSK |
| PSK Pass Phrase | SmartCity2024 |
| Channel | 6 |
| SSID Broadcast | Enabled |

**Verification:**
- Wireless indicator on AP should be green
- SSID should be visible in wireless device scans

✅ WiFi-Zone1 configured

---

## 8.2 WiFi-Zone2 Configuration

**Step 1:** Click **WiFi-Zone2** access point

**Step 2:** Click **Config** tab

**Step 3:** Configure network settings:

| Field | Value |
|-------|-------|
| IP Configuration | Static |
| IP Address | 192.168.30.51 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.30.1 |
| DNS Server | 192.168.40.10 |

**Step 4:** Configure wireless settings:

| Field | Value |
|-------|-------|
| SSID | SmartCity_Zone2 |
| Authentication | WPA2-PSK |
| PSK Pass Phrase | SmartCity2024 |
| Channel | 11 |
| SSID Broadcast | Enabled |

**Note:** Different channel (11 vs 6) to avoid interference

✅ WiFi-Zone2 configured

---

## 8.3 WiFi Configuration Summary

| Access Point | IP Address | SSID | Password | Channel |
|--------------|------------|------|----------|---------|
| WiFi-Zone1 | 192.168.30.50 | SmartCity_Zone1 | SmartCity2024 | 6 |
| WiFi-Zone2 | 192.168.30.51 | SmartCity_Zone2 | SmartCity2024 | 11 |

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 9. Phase 8: End Device Configuration (30 minutes)

## 9.1 Admin Devices (VLAN 20) - DHCP

**For each admin device (Admin-PC-1, Admin-PC-2, Admin-Laptop-1, Admin-Laptop-2):**

**Step 1:** Click device → **Desktop** tab → **IP Configuration**

**Step 2:** Select **DHCP** radio button

**Step 3:** Wait 5-10 seconds

**Expected Result:**

| Field | Expected Value (example) |
|-------|--------------------------|
| IPv4 Address | 192.168.20.100 - 192.168.20.103 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.20.1 |
| DNS Server | 192.168.40.10 |

**Verification:**
- Click **Desktop** → **Command Prompt**
- Type: `ipconfig`
- Verify IP address in 192.168.20.100-119 range

✅ If successful: Device has IP, can ping 192.168.20.1

❌ If fails (169.254.x.x): Check DHCP server, router helper-address, VLAN configuration

---

## 9.2 IoT Devices (VLAN 10) - DHCP

**For each IoT device (IoT-Traffic-1 through IoT-Light-1):**

**Step 1:** Click device → **Config** tab (or **Desktop** if PC-PT substitute)

**Step 2:** Click **FastEthernet0** (or similar interface)

**Step 3:** Select **DHCP**

**Expected Result:**
- IPv4 Address: 192.168.10.100 - 192.168.10.107
- Gateway: 192.168.10.1

**Verification:**
- Click **Desktop** → **Command Prompt**
- Type: `ipconfig`
- Type: `ping 192.168.10.1` (test gateway)

✅ 8 IoT devices with IPs in 192.168.10.100-107 range

---

## 9.3 Mobile Admin Tablets (VLAN 50) - DHCP

**For wired tablets (Tablet-Admin-1, 2, 3):**

**Step 1:** Click device → **Desktop** → **IP Configuration**

**Step 2:** Select **DHCP**

**Expected Result:**
- IPv4 Address: 192.168.50.100 - 192.168.50.102
- Gateway: 192.168.50.1

✅ 3 tablets with IPs in VLAN 50 range

---

## 9.4 Wireless Clients (Smartphones and Tablets)

### Connect Phone-1 to WiFi

**Step 1:** Click **Phone-1** device

**Step 2:** Click **Desktop** tab → **PC Wireless**

**Step 3:** Click **Connect** tab

**Step 4:** Scan for networks:
- List should show: `SmartCity_Zone1` and `SmartCity_Zone2`

**Step 5:** Select **SmartCity_Zone1**

**Step 6:** Click **Connect**

**Step 7:** Enter password: `SmartCity2024`

**Step 8:** Click **OK**

**Expected Result:**
- Connection status: **Connected**
- Signal strength: Green bars

**Step 9:** Verify IP assignment:
- Click **Desktop** → **IP Configuration**
- Should show DHCP-assigned IP: 192.168.30.100 - 192.168.30.199

✅ Phone-1 connected to WiFi

---

### Connect Remaining Wireless Devices

**Repeat above process for:**
- Phone-2 → Connect to `SmartCity_Zone1` or `SmartCity_Zone2`
- Phone-3 → Connect to `SmartCity_Zone1` or `SmartCity_Zone2`
- Tablet-Public-1 → Connect to `SmartCity_Zone1`
- Tablet-Public-2 → Connect to `SmartCity_Zone2`

**Tip:** Distribute devices across both APs for load balancing

✅ All 5 wireless clients connected

---

## 9.5 End Device Summary

| VLAN | Device Type | Quantity | IP Range | Config Method |
|------|-------------|----------|----------|---------------|
| 10 | IoT Sensors | 8 | 192.168.10.100-107 | DHCP |
| 20 | Admin PCs/Laptops | 4 | 192.168.20.100-103 | DHCP |
| 30 | WiFi Clients | 5 | 192.168.30.100-104 | DHCP (wireless) |
| 40 | Servers | 3 | 192.168.40.10, .20, .30 | Static |
| 50 | Mobile Admin | 3 | 192.168.50.100-102 | DHCP |

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 10. Phase 9: QoS Configuration (20 minutes)

**Purpose:** Prioritize emergency and IoT traffic over public WiFi

**Step 1:** Click **Core-Router** → **CLI** tab

**Step 2:** Enter configuration mode:

```cisco
enable
configure terminal
```

---

## 10.1 Define Traffic Classes

**Step 3:** Create class maps:

```cisco
class-map match-any EMERGENCY
 match access-group 140
 exit

class-map match-any IOT-CRITICAL
 match access-group 141
 exit

class-map match-any ADMIN
 match access-group 142
 exit
```

---

## 10.2 Define Access Lists for QoS

**Step 4:** Create ACLs to identify traffic:

```cisco
access-list 140 remark EMERGENCY-SERVICES
access-list 140 permit ip host 192.168.10.101 any

access-list 141 remark IOT-CRITICAL-SENSORS
access-list 141 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255

access-list 142 remark ADMIN-TRAFFIC
access-list 142 permit ip 192.168.20.0 0.0.0.255 any
```

**Explanation:**
- ACL 140: Emergency traffic (from first IoT sensor as example)
- ACL 141: All IoT sensor traffic to servers
- ACL 142: All administrative traffic

---

## 10.3 Create QoS Policy

**Step 5:** Define policy map:

```cisco
policy-map SMART-CITY-QOS
 class EMERGENCY
  priority percent 30
 class IOT-CRITICAL
  bandwidth percent 40
 class ADMIN
  bandwidth percent 20
 class class-default
  fair-queue
 exit
```

**Explanation:**
- EMERGENCY: 30% priority (strict priority - always first)
- IOT-CRITICAL: 40% guaranteed bandwidth
- ADMIN: 20% guaranteed bandwidth
- class-default: 10% remaining (public WiFi gets this)

---

## 10.4 Apply QoS Policy

**Step 6:** Apply to router interfaces:

```cisco
interface GigabitEthernet0/0
 service-policy output SMART-CITY-QOS
 exit

interface GigabitEthernet0/1
 service-policy output SMART-CITY-QOS
 exit
```

---

## 10.5 Verify QoS Configuration

**Step 7:** Check QoS policy:

```cisco
show policy-map
```

**Expected Output:**
```
Policy Map SMART-CITY-QOS
 Class EMERGENCY
  priority percent 30
 Class IOT-CRITICAL
  bandwidth percent 40
 Class ADMIN
  bandwidth percent 20
 Class class-default
  fair-queue
```

**Step 8:** Check policy application:

```cisco
show policy-map interface GigabitEthernet0/0
```

**Expected Output:**
```
GigabitEthernet0/0

  Service-policy output: SMART-CITY-QOS

    Class-map: EMERGENCY (match-any)
      0 packets, 0 bytes
      ...
```

✅ QoS configured and applied

**Step 9:** Save configuration:

```cisco
end
write memory
```

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 11. Phase 10: Testing and Validation (45 minutes)

## 11.1 Basic Connectivity Tests

### Test 1: Verify Router Interfaces

**Step 1:** On **Core-Router**, run:

```cisco
show ip interface brief
```

**Expected Result:**
- All interfaces: Status = up, Protocol = up
- 2 physical + 5 subinterfaces = 7 total UP

✅ Pass / ❌ Fail

---

### Test 2: Verify VLAN Configuration

**Step 1:** On **Access-SW2**, run:

```cisco
show vlan brief
```

**Expected Result:**
- VLAN 10 exists
- Ports Fa0/1-8 in VLAN 10

✅ Pass / ❌ Fail

---

### Test 3: Verify Trunk Links

**Step 1:** On **Dist-SW-A**, run:

```cisco
show interfaces trunk
```

**Expected Result:**
- 4 trunk ports (Gig1/0/1, Fa1/0/1-3)
- VLANs 10,20,40 allowed

✅ Pass / ❌ Fail

---

## 11.2 DHCP Tests

### Test 4: DHCP Assignment - Admin PC

**Step 1:** Click **Admin-PC-1** → **Desktop** → **Command Prompt**

**Step 2:** Type:

```
ipconfig
```

**Expected Result:**
```
IP Address...........192.168.20.100 (or 192.168.20.101-103)
Subnet Mask..........255.255.255.0
Default Gateway......192.168.20.1
DNS Server...........192.168.40.10
```

✅ Pass / ❌ Fail

---

### Test 5: DHCP Assignment - IoT Device

**Step 1:** Click **IoT-Traffic-1** → **Desktop** → **Command Prompt**

**Step 2:** Type:

```
ipconfig
```

**Expected Result:**
```
IP Address...........192.168.10.100 (or similar in range)
Default Gateway......192.168.10.1
DNS Server...........192.168.40.10
```

✅ Pass / ❌ Fail

---

## 11.3 Connectivity Tests (Ping)

### Test 6: Admin PC to DNS Server

**Step 1:** From **Admin-PC-1** command prompt:

```
ping 192.168.40.10
```

**Expected Result:**
```
Reply from 192.168.40.10: bytes=32 time<1ms TTL=127
...
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

✅ Pass / ❌ Fail

---

### Test 7: IoT Sensor to DHCP Server

**Step 1:** From **IoT-Traffic-1** command prompt:

```
ping 192.168.40.20
```

**Expected Result:**
- Replies received (0% packet loss)

✅ Pass / ❌ Fail

---

### Test 8: Admin PC to IoT Sensor (Should Work)

**Step 1:** From **Admin-PC-1**:

```
ping 192.168.10.100
```

**Expected Result:**
- Replies received (ACL 110 permits Admin → IoT)

✅ Pass / ❌ Fail

---

## 11.4 ACL Security Tests

### Test 9: Public WiFi to IoT Sensor (Should FAIL)

**Step 1:** Click **Phone-1** → **Desktop** → **Command Prompt**

**Step 2:** Type:

```
ping 192.168.10.100
```

**Expected Result:**
```
Request timed out.
...
Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
```

✅ Pass (blocked as expected) / ❌ Fail (shouldn't work!)

**Verification:** Check router ACL hits:

```cisco
Core-Router# show access-lists 130
Extended IP access list 130
    ...
    40 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log (4 matches)
```

✅ Matches should increment each ping attempt

---

### Test 10: Public WiFi to DNS Server (Should WORK for DNS only)

**Step 1:** From **Phone-1** command prompt:

**Test DNS (UDP port 53):**

```
nslookup dns.smart-city.local
```

**Expected Result:**
```
Name: dns.smart-city.local
Address: 192.168.40.10
```

✅ Pass / ❌ Fail

**Test ping (ICMP - should FAIL):**

```
ping 192.168.40.10
```

**Expected Result:**
- Request timed out (ACL 130 line 60 blocks all to 192.168.40.0 except DNS)

✅ Pass (blocked) / ❌ Fail

---

### Test 11: IoT Sensor to Public WiFi (Should FAIL)

**Step 1:** From **IoT-Traffic-1** command prompt:

```
ping 192.168.30.100
```

**Expected Result:**
- Request timed out (ACL 110 line 30 blocks IoT → Public WiFi)

✅ Pass (blocked) / ❌ Fail

---

## 11.5 DNS Resolution Tests

### Test 12: DNS Lookup from Admin PC

**Step 1:** From **Admin-PC-1** command prompt:

```
nslookup dhcp.smart-city.local
```

**Expected Result:**
```
Name: dhcp.smart-city.local
Address: 192.168.40.20
```

✅ Pass / ❌ Fail

---

### Test 13: DNS Lookup Multiple Records

**Step 1:** From **Admin-PC-1**:

```
nslookup email.smart-city.local
nslookup core-router.smart-city.local
```

**Expected Result:**
- email.smart-city.local → 192.168.40.30
- core-router.smart-city.local → 192.168.1.1

✅ Pass / ❌ Fail

---

## 11.6 IPv6 Tests (Optional)

### Test 14: IPv6 Connectivity

**Step 1:** From **Admin-PC-1** command prompt:

```
ping6 2001:db8:1000:40::10
```

**Expected Result:**
- Replies received from DNS server via IPv6

✅ Pass / ❌ Fail

---

## 11.7 Test Results Documentation

**Create a test results table:**

| Test # | Test Description | Expected Result | Actual Result | Status |
|--------|------------------|-----------------|---------------|--------|
| 1 | Router interfaces UP | 7 interfaces up | | ✅ / ❌ |
| 2 | VLAN configuration | VLAN 10 on Fa0/1-8 | | ✅ / ❌ |
| 3 | Trunk links | 4 trunks operational | | ✅ / ❌ |
| 4 | Admin DHCP | 192.168.20.100-103 | | ✅ / ❌ |
| 5 | IoT DHCP | 192.168.10.100-107 | | ✅ / ❌ |
| 6 | Admin → DNS | Ping successful | | ✅ / ❌ |
| 7 | IoT → DHCP | Ping successful | | ✅ / ❌ |
| 8 | Admin → IoT | Ping successful | | ✅ / ❌ |
| 9 | Public → IoT | **Ping BLOCKED** | | ✅ / ❌ |
| 10 | Public DNS lookup | nslookup works | | ✅ / ❌ |
| 11 | IoT → Public | **Ping BLOCKED** | | ✅ / ❌ |
| 12 | DNS resolution | Resolves to 192.168.40.20 | | ✅ / ❌ |

**Target:** 12/12 tests pass

✅ **Checkpoint:** Save Packet Tracer project (Ctrl+S)

---

# 12. Phase 11: Documentation and Screenshots (30 minutes)

## 12.1 Configuration Backups

### Export Router Configuration

**Step 1:** On **Core-Router** CLI:

```cisco
show running-config
```

**Step 2:** Copy output to text file:
- Save as: `Core-Router_config.txt`

**Repeat for all switches:**
- `Dist-SW-A_config.txt`
- `Dist-SW-B_config.txt`
- `Access-SW1_config.txt`
- ... (all 5 access switches)

---

## 12.2 Screenshot Checklist

**Required screenshots for report:**

1. ✅ **Network topology** (full workspace view in Logical mode)
2. ✅ **Core router: `show ip interface brief`**
3. ✅ **Core router: `show ipv6 interface brief`**
4. ✅ **Core router: `show access-lists`**
5. ✅ **Dist-SW-A: `show vlan brief`**
6. ✅ **Dist-SW-A: `show interfaces trunk`**
7. ✅ **Access-SW2: `show vlan brief`** (IoT ports)
8. ✅ **Admin-PC-1: `ipconfig`** (DHCP assignment)
9. ✅ **Admin-PC-1: `ping 192.168.40.10`** (connectivity test)
10. ✅ **Phone-1: `ping 192.168.10.100`** (blocked - ACL test)
11. ✅ **DNS Server: Services → DNS** (showing records)
12. ✅ **DHCP Server: Services → DHCP** (showing pools)
13. ✅ **WiFi-Zone1: Config → Wireless** (SSID settings)
14. ✅ **Phone-1: Desktop → PC Wireless → Connect** (connected status)
15. ✅ **Core-Router: `show policy-map`** (QoS configuration)

---

## 12.3 Network Diagram Export

**Step 1:** In Packet Tracer, click **File** → **Export** → **Export as PDF**

**Step 2:** Save as: `Smart_City_Network_Diagram.pdf`

**Alternative:** Take screenshot of full workspace

---

## 12.4 Final Project Files

**Organize files:**

```
CNL-SmartCity/
├── main/
│   └── app_v00.pkt (Packet Tracer file)
├── configs/
│   ├── Core-Router_config.txt
│   ├── Dist-SW-A_config.txt
│   ├── Dist-SW-B_config.txt
│   ├── Access-SW1_config.txt
│   ├── Access-SW2_config.txt
│   ├── Access-SW3_config.txt
│   ├── Access-SW4_config.txt
│   └── Access-SW5_config.txt
├── screenshots/
│   ├── 01_topology.png
│   ├── 02_router_interfaces.png
│   ├── 03_router_ipv6.png
│   ├── 04_acl_config.png
│   ├── ... (15 screenshots total)
├── PART1_PROJECT_KNOWLEDGE.md
├── PART2_IMPLEMENTATION_GUIDE.md
└── README.md
```

✅ **Final Checkpoint:** Save everything!

---

# 13. Troubleshooting Guide

## 13.1 Common Issues and Solutions

### Issue 1: DHCP Not Working (Device gets 169.254.x.x)

**Symptoms:**
- Device shows IP address 169.254.x.x (APIPA)
- `ipconfig` shows no default gateway

**Diagnosis:**

**Step 1:** Check DHCP server is ON:
- Click DHCP-Server → Services → DHCP
- Verify service is ON

**Step 2:** Check DHCP pool exists for VLAN:
- Verify pool name matches (e.g., "IoT_SENSORS" for VLAN 10)
- Check "Start IP Address" is correct subnet

**Step 3:** Check router helper-address:

```cisco
Core-Router# show running-config interface GigabitEthernet0/0.10 | include helper
 ip helper-address 192.168.40.20
```

**Step 4:** Check VLAN configuration:

```cisco
Access-SW2# show vlan brief | include 10
10   IoT-Sensors                  active    Fa0/1, Fa0/2, ..., Fa0/8
```

**Step 5:** Check trunk link:

```cisco
Dist-SW-A# show interfaces trunk
```

Verify VLAN 10 in "Vlans allowed and active" list

**Solution:**
- Add missing DHCP pool, OR
- Add `ip helper-address 192.168.40.20` to router subinterface, OR
- Fix VLAN configuration on switches

---

### Issue 2: Cannot Ping Across VLANs

**Symptoms:**
- Admin PC cannot ping IoT sensor (different VLANs)
- Ping within same VLAN works

**Diagnosis:**

**Step 1:** Check router subinterface UP:

```cisco
Core-Router# show ip interface brief | include 0.10
GigabitEthernet0/0.10  192.168.10.1    YES manual up                    up
```

Status and Protocol must BOTH be "up"

**Step 2:** Check encapsulation configured:

```cisco
Core-Router# show running-config interface GigabitEthernet0/0.10 | include encap
 encapsulation dot1Q 10
```

**Step 3:** Check device default gateway:

From IoT device:
```
ipconfig
```

Gateway should be 192.168.10.1 (router subinterface IP)

**Step 4:** Check ACLs not blocking:

```cisco
Core-Router# show access-lists 110
```

Verify ACL permits desired traffic

**Solution:**
- Add `encapsulation dot1Q <vlan-id>` to subinterface, OR
- Configure correct default gateway on end devices, OR
- Modify ACL to permit traffic

---

### Issue 3: WiFi Clients Cannot Connect

**Symptoms:**
- WiFi SSID not visible
- Connection fails with "Authentication failed"

**Diagnosis:**

**Step 1:** Check AP powered on:
- Click access point → Check if wireless indicator is green

**Step 2:** Verify AP has IP address:
- Click WiFi-Zone1 → Config → Port 1
- IP should be 192.168.30.50

**Step 3:** Check SSID broadcast enabled:
- Config → Wireless
- SSID Broadcast: **Enabled**

**Step 4:** Verify password:
- PSK Pass Phrase: `SmartCity2024` (case-sensitive!)

**Step 5:** Check VLAN 30 configured:

```cisco
Access-SW4# show vlan brief | include 30
30   Public-WiFi                  active    Fa0/1
```

Port connected to AP must be in VLAN 30

**Solution:**
- Enable SSID broadcast, OR
- Correct WiFi password (case-sensitive), OR
- Add port to VLAN 30 on access switch

---

### Issue 4: ACL Not Blocking Traffic

**Symptoms:**
- Public WiFi user CAN ping IoT sensor (should be blocked)

**Diagnosis:**

**Step 1:** Check ACL exists:

```cisco
Core-Router# show access-lists 130
```

**Step 2:** Check ACL applied to interface:

```cisco
Core-Router# show ip interface GigabitEthernet0/1.30 | include access list
  Inbound  access list is 130
```

**Step 3:** Check ACL direction (inbound vs outbound):
- Should be **inbound** (traffic FROM public WiFi)
- If outbound → ACL won't filter traffic leaving VLAN

**Step 4:** Check ACL line order:
- `permit ip any any` at END, not beginning
- Specific deny rules BEFORE general permits

**Solution:**
- Apply ACL with `ip access-group 130 in`, OR
- Reorder ACL lines (most specific first), OR
- Add missing deny statements

---

### Issue 5: Invalid Interface Error on Router

**Symptoms:**
- Error: "% Invalid input detected at '^' marker."
- When configuring `interface GigabitEthernet0/0.10`

**Diagnosis:**

**Step 1:** Check router interface names:

```cisco
show ip interface brief
```

**Step 2:** Identify correct format:
- See `GigabitEthernet0/0` → Use `Gig0/0.10`
- See `GigabitEthernet0/0/0` → Use `Gig0/0/0.10`

**Solution:**
- Use correct interface naming for your router model
- If 2911: `interface GigabitEthernet0/0.10`
- If ISR4331: `interface GigabitEthernet0/0/0.10`

---

### Issue 6: Trunk Link Not Passing VLANs

**Symptoms:**
- VLAN configured on switch
- Trunk shows "trunking"
- But traffic doesn't cross trunk

**Diagnosis:**

**Step 1:** Check allowed VLANs:

```cisco
Dist-SW-A# show interfaces trunk
Port        Vlans allowed on trunk
Fa1/0/2     10
```

**Step 2:** Check VLAN active:

```cisco
Dist-SW-A# show interfaces trunk
Port        Vlans allowed and active in management domain
Fa1/0/2     10
```

If VLAN missing from "active" → VLAN doesn't exist on both sides

**Step 3:** Create VLAN on BOTH switches:

```cisco
! On both Dist-SW-A and Access-SW2:
vlan 10
 name IoT-Sensors
 exit
```

**Solution:**
- Add VLAN to trunk allowed list: `switchport trunk allowed vlan add 10`, OR
- Create VLAN on both ends of trunk

---

## 13.2 Verification Command Quick Reference

**Router:**
```cisco
show ip interface brief
show ipv6 interface brief
show running-config
show access-lists
show policy-map interface <interface>
```

**Switches:**
```cisco
show vlan brief
show interfaces trunk
show spanning-tree brief
show running-config
```

**End Devices:**
```
ipconfig
ipconfig /all
ping <ip-address>
ping6 <ipv6-address>
tracert <ip-address>
nslookup <hostname>
```

---

# Implementation Complete! 🎉

## Final Checklist

✅ **33 devices configured:**
- 1 Core Router (with 5 VLAN subinterfaces, ACLs, QoS)
- 2 Distribution Switches (VLANs, trunks)
- 5 Access Switches (access ports, trunks)
- 3 Servers (DNS, DHCP, Email)
- 8 IoT Devices (DHCP, VLAN 10)
- 4 Admin Devices (DHCP, VLAN 20)
- 2 WiFi Access Points (SSIDs configured)
- 3 Mobile Admin Tablets (VLAN 50)
- 5 WiFi Clients (connected wirelessly)

✅ **5 VLANs operational:**
- VLAN 10: IoT Sensors
- VLAN 20: Administrative
- VLAN 30: Public WiFi
- VLAN 40: Servers
- VLAN 50: Mobile Admin

✅ **Security configured:**
- ACL 110: IoT protection
- ACL 130: Public WiFi isolation
- VLAN segmentation

✅ **Services operational:**
- DHCP (4 pools, auto-assignment)
- DNS (4 records, name resolution)
- Email (SMTP with 2 users)
- QoS (traffic prioritization)

✅ **Testing completed:**
- 12+ connectivity tests
- ACL security validation
- DNS resolution verified

✅ **Documentation saved:**
- Packet Tracer project file
- Configuration backups (8 devices)
- 15 screenshots
- Test results table

---

## What You've Built

This network demonstrates:

1. **Depth of Knowledge:** IPv6, VLANs, ACLs, QoS, DNS, DHCP
2. **Conflicting Requirements:** Security vs performance (ACL placement), public access vs security (ACL 130)
3. **Depth of Analysis:** See PART 1 for bandwidth calculations, failure analysis
4. **Familiarity:** Based on Singapore/Barcelona smart city case studies
5. **Stakeholder Involvement:** 5 stakeholder groups with different needs
6. **Conflicting Requirements:** IoT ops vs security, public vs admin, budget vs redundancy
7. **Interdependence:** DHCP chain, DNS resolution, ACL security all interconnected

---

## Next Steps for Your Report

1. **Read PART 1** for all theoretical knowledge and justifications
2. **Copy relevant sections** from PART 1 into your report chapters
3. **Insert screenshots** from Phase 11 into appropriate report sections
4. **Add test results** from Phase 10 to validation chapter
5. **Write conclusion** summarizing what was achieved

**Report Structure Guide in PART 1, Section 11**

---

## Need Help?

**Common questions:**
- Interface naming issues → Section 13.1, Issue 5
- DHCP not working → Section 13.1, Issue 1
- ACL not blocking → Section 13.1, Issue 4
- WiFi connection problems → Section 13.1, Issue 3

**For report writing:**
- See PART 1, Section 11 (Report Writing Guide)
- Use sample paragraphs in PART 1, Section 6 (Conflicts)

---

**Project Complete!**

Your Smart City IoT Network is fully functional and ready for demonstration and report writing. 🚀
