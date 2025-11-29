# PART 1: PHYSICAL SETUP
## 02 - CABLE CONNECTIONS (Port-to-Port)

**Follow this guide AFTER placing all 102 devices from 01_DEVICE_LIST.md**

---

## ⚠️ CRITICAL: IoT DEVICE CONNECTIVITY

**IMPORTANT - Read Before Connecting IoT Devices:**

Many IoT devices in Packet Tracer 8.2+ are **WIRELESS-ONLY** and **CANNOT** be connected with Ethernet cables!

### ❌ **Devices You CANNOT Wire:**
- Webcam (Bluetooth/WiFi only)
- Motion Detector (wireless only)
- GPS (wireless only)
- Smoke Detector (wireless only)
- **Cell Tower** (if device exists, it's wireless-only)

### ✅ **Devices You CAN Wire:**
- **SBC-PT** (Single Board Computer) - FastEthernet0 port ← **USE FOR IoT!**
- **Home Gateway** - Ethernet0 port
- **MCU-PT** (Microcontroller) - FastEthernet0 port
- **PC-PT** - FastEthernet0 port (simplest option)
- **Linksys WRT300N** - Internet port ← **USE FOR CELL TOWER!**
- **AccessPoint-PT** - Ethernet1 port

### 📖 **For Complete Details:**
See `IOT_DEVICE_CONNECTIVITY_GUIDE.md` for comprehensive IoT device selection guide.

**This guide uses SBC-PT and Home Gateway devices for all IoT - they all have wired Ethernet ports!**

---

## 📌 CABLE TYPES REFERENCE

| Cable Type | Icon in PT | When to Use | In This Project |
|------------|-----------|-------------|-----------------|
| **Copper Straight-Through** | ▬▬▬ (solid) | Device ↔ Switch, Router ↔ Switch | 95% of connections |
| **Copper Cross-Over** | ╳╳╳ (X) | Switch ↔ Switch, Router ↔ Router (if no auto-MDI/X) | Redundant switch links |
| **Serial DCE/DTE** | ~~~~ (wavy) | WAN links (Router ↔ Router over distance) | ISP ↔ City connections |
| **Fiber Optic** | ))) | High-speed, long distance | Optional upgrades |

**For this project: Use Copper Straight-Through for 90% of connections**

---

## 🔌 CONNECTION STRATEGY

**Order of connections:**
1. ✅ Core infrastructure (routers, core switches)
2. ✅ Distribution layer (zone routers ↔ core)
3. ✅ Access layer (access switches ↔ distribution)
4. ✅ End devices (servers, PCs, IoT)
5. ✅ Wireless devices
6. ✅ Inter-city WAN links

---

## 🏙️ CITY A - CABLE CONNECTIONS

### **SECTION 1: CORE INFRASTRUCTURE (10 connections)**

#### Core Routers ↔ Core Switches

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 1 | `CityA-Core-R1` | `Gig0/0` | `CityA-Core-SW1` | `Gig1/0/1` | Straight-Through |
| 2 | `CityA-Core-R1` | `Gig0/1` | `CityA-Core-SW2` | `Gig1/0/1` | Straight-Through |
| 3 | `CityA-Core-SW1` | `Gig1/0/2` | `CityA-Core-SW2` | `Gig1/0/2` | Cross-Over (redundancy) |

**Why:**
- Core router needs connection to BOTH core switches (redundancy)
- Core switches link to each other (Spanning Tree will block one)

---

#### Core Switches ↔ Zone Routers

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 4 | `CityA-Core-SW1` | `Gig1/0/2` | `CityA-Gov-R1` | `Gig0/0` | Straight-Through |
| 5 | `CityA-Core-SW1` | `Gig1/0/3` | `CityA-Res-R1` | `Gig0/0` | Straight-Through |
| 6 | `CityA-Core-SW2` | `Gig1/0/3` | `CityA-Com-R1` | `Gig0/0` | Straight-Through |

**IMPORTANT:**
- Cisco 2911 routers have only 3 GigabitEthernet ports (Gig0/0, Gig0/1, Gig0/2)
- Zone routers connect to CORE SWITCHES, not directly to Core Router
- This follows proper hierarchical network design (more realistic!)

**Why:**
- Zone routers connect to distribution layer (core switches) for OSPF routing
- Core router handles inter-VLAN routing via trunk links to switches
- Each zone router serves VLANs for its area

---

#### Border Router Connection

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 7 | `CityA-Border-R1` | `Gig0/0` | `CityA-Core-R1` | `Gig0/2` | Straight-Through |
| 8 | `CityA-Border-R1` | `Serial0/0/0` | `ISP-Border-R1` | `Serial0/0/0` | Serial DCE |

**Why:**
- Border router connects to core router's Gig0/2 port
- Core router's Gig0/0 and Gig0/1 are used for switch trunks
- Serial link simulates WAN connection (fiber/leased line)

---

#### Core Switches ↔ Servers

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 9 | `CityA-Core-SW1` | `Fa1/0/1` | `CityA-DNS-Server` | `Fa0` | Straight-Through |
| 10 | `CityA-Core-SW1` | `Fa1/0/2` | `CityA-DHCP-Server` | `Fa0` | Straight-Through |
| 11 | `CityA-Core-SW1` | `Fa1/0/3` | `CityA-Web-Server` | `Fa0` | Straight-Through |
| 12 | `CityA-Core-SW1` | `Fa1/0/4` | `CityA-Email-Server` | `Fa0` | Straight-Through |

**Why:**
- Servers in VLAN 99 (Management) connect to core switch
- Centralized for all zones to access

---

### **SECTION 2: GOVERNMENT ZONE (15 connections)**

#### Government Router ↔ Access Switch

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 13 | `CityA-Gov-R1` | `Gig0/1` | `CityA-Gov-SW1` | `Fa0/24` | Straight-Through |

**Why:**
- Trunk link carrying VLANs 10 (Gov), 60 (Emergency)

---

#### Government PCs and Devices

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 14 | `CityA-Gov-SW1` | `Fa0/1` | `CityA-Gov-PC-1` | `FastEthernet0` | Straight-Through |
| 15 | `CityA-Gov-SW1` | `Fa0/2` | `CityA-Gov-PC-2` | `FastEthernet0` | Straight-Through |
| 16 | `CityA-Gov-SW1` | `Fa0/3` | `CityA-Police-PC-1` | `FastEthernet0` | Straight-Through |
| 17 | `CityA-Gov-SW1` | `Fa0/4` | `CityA-Fire-PC-1` | `FastEthernet0` | Straight-Through |
| 18 | `CityA-Gov-SW1` | `Fa0/5` | `CityA-WiFi-Gov-AP1` | `Ethernet1` | Straight-Through |
| 19 | `CityA-Gov-SW1` | `Fa0/6` | `CityA-Gov-Camera-1` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 20 | `CityA-Gov-SW1` | `Fa0/7` | `CityA-Gov-Camera-2` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 21 | `CityA-Gov-SW1` | `Fa0/8` | `CityA-Fire-Sensor-1` (SBC-PT) | `FastEthernet0` | Straight-Through |

**VLANs:**
- Fa0/1-2: VLAN 10 (Government)
- Fa0/3-4: VLAN 60 (Emergency)
- Fa0/5: VLAN 10 (WiFi management)
- Fa0/6-8: VLAN 60 (Security IoT - SBC-PT devices)

**NOTE:** SBC-PT devices have FastEthernet0 port (wired connection)

---

### **SECTION 3: RESIDENTIAL ZONE (20 connections)**

#### Residential Router ↔ Access Switches

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 22 | `CityA-Res-R1` | `Gig0/1` | `CityA-Res-SW1` | `Fa0/24` | Straight-Through |
| 23 | `CityA-Res-R1` | `Gig1/0` | `CityA-Res-SW2` | `Fa0/24` | Straight-Through |

**Why:**
- Two access switches for residential area (more coverage)

---

#### Residential Devices ↔ Switch 1

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 24 | `CityA-Res-SW1` | `Fa0/1` | `CityA-Home-PC-1` | `FastEthernet0` | Straight-Through |
| 25 | `CityA-Res-SW1` | `Fa0/2` | `CityA-Home-Laptop-1` | `FastEthernet0` | Straight-Through |
| 26 | `CityA-Res-SW1` | `Fa0/3` | `CityA-WiFi-Res-AP1` | `Ethernet1` | Straight-Through |
| 27 | `CityA-Res-SW1` | `Fa0/4` | `CityA-SmartHome-1` (Home Gateway) | `Ethernet0` | Straight-Through |
| 28 | `CityA-Res-SW1` | `Fa0/5` | `CityA-SmartHome-2` (Home Gateway) | `Ethernet0` | Straight-Through |
| 29 | `CityA-Res-SW1` | `Fa0/6` | `CityA-EnvMonitor-1` (SBC-PT) | `FastEthernet0` | Straight-Through |

**VLANs:**
- All ports: VLAN 20 (Residential)

**NOTE:** Home Gateway uses Ethernet0, SBC-PT uses FastEthernet0

---

#### Cellular Tower ↔ Switch 2

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 30 | `CityA-Res-SW2` | `Fa0/1` | `CityA-CellTower-1` (Linksys WRT300N) | **Internet** port | Straight-Through |

**CRITICAL - Cell Tower Connection:**
- ⚠️ **Packet Tracer Cell Tower devices (if they exist) have NO Ethernet port**
- ✅ **MUST use Linksys WRT300N** for wired cellular simulation
- ✅ Connect to **"Internet"** port (WAN port) on WRT300N
- This port provides backhaul connection for cellular network

**Why Linksys WRT300N:**
- Cell tower provides 4G/5G coverage for mobile devices via WiFi
- Internet port connects to wired network for backhaul
- Simulates real cellular tower with fiber/ethernet backhaul connection

**Configuration (after connection):**
1. Click Linksys WRT300N
2. Config tab → Wireless
3. SSID: `CityA-4G-LTE`
4. Security: WPA2-PSK, Password: `Cellular2024`
5. Config tab → DHCP → **Disable** DHCP Server
6. Config tab → Internet (WAN) → Static IP: 192.168.20.60
7. Gateway: 192.168.20.1

---

#### Wireless Devices (NO CABLES - Configure Later)

**These devices connect wirelessly after configuration:**
- `CityA-Home-Smartphone-1` → Connects to `CityA-WiFi-Res-AP1` OR `CityA-CellTower-1`

---

### **SECTION 4: COMMERCIAL ZONE (12 connections)**

#### Commercial Router ↔ Access Switch

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 31 | `CityA-Com-R1` | `Gig0/1` | `CityA-Com-SW1` | `Fa0/24` | Straight-Through |

---

#### Commercial Devices

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 32 | `CityA-Com-SW1` | `Fa0/1` | `CityA-Com-PC-1` | `FastEthernet0` | Straight-Through |
| 33 | `CityA-Com-SW1` | `Fa0/2` | `CityA-Com-Laptop-1` | `FastEthernet0` | Straight-Through |
| 34 | `CityA-Com-SW1` | `Fa0/3` | `CityA-Retail-POS-1` | `FastEthernet0` | Straight-Through |
| 35 | `CityA-Com-SW1` | `Fa0/4` | `CityA-WiFi-Pub-AP1` | `Ethernet1` | Straight-Through |

**VLANs:**
- Fa0/1-3: VLAN 30 (Commercial)
- Fa0/4: VLAN 50 (Public WiFi management)

---

#### Public WiFi Wireless Devices (NO CABLES)

**Connect wirelessly after configuration:**
- `CityA-Public-Phone-1` → `CityA-WiFi-Pub-AP1`
- `CityA-Public-Tablet-1` → `CityA-WiFi-Pub-AP1`

---

### **SECTION 5: TRANSPORTATION ZONE (10 connections)**

#### Transportation Switch Connection

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 36 | `CityA-Core-SW2` | `Fa1/0/5` | `CityA-Trans-SW1` | `Fa0/24` | Straight-Through |

**Note:** Transportation connects directly to Core-SW2 (no dedicated router for simplicity)

---

#### Transportation IoT Devices

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 37 | `CityA-Trans-SW1` | `Fa0/1` | `CityA-TrafficLight-1` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 38 | `CityA-Trans-SW1` | `Fa0/2` | `CityA-TrafficLight-2` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 39 | `CityA-Trans-SW1` | `Fa0/3` | `CityA-ParkingSensor-1` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 40 | `CityA-Trans-SW1` | `Fa0/4` | `CityA-ParkingSensor-2` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 41 | `CityA-Trans-SW1` | `Fa0/5` | `CityA-BusTracker-1` (SBC-PT) | `FastEthernet0` | Straight-Through |

**VLANs:**
- All ports: VLAN 40 (Transportation)

**NOTE:** All IoT devices use SBC-PT with FastEthernet0 port

---

### **SECTION 6: UTILITIES ZONE (8 connections)**

#### Utilities Switch Connection

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 42 | `CityA-Core-SW2` | `Fa1/0/6` | `CityA-Util-SW1` | `Fa0/24` | Straight-Through |

---

#### Utilities IoT Devices

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 43 | `CityA-Util-SW1` | `Fa0/1` | `CityA-SmartGrid-1` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 44 | `CityA-Util-SW1` | `Fa0/2` | `CityA-SmartGrid-2` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 45 | `CityA-Util-SW1` | `Fa0/3` | `CityA-WaterMonitor-1` (SBC-PT) | `FastEthernet0` | Straight-Through |
| 46 | `CityA-Util-SW1` | `Fa0/4` | `CityA-WaterMonitor-2` (SBC-PT) | `FastEthernet0` | Straight-Through |

**VLANs:**
- All ports: VLAN 70 (Utilities)

**NOTE:** All IoT devices use SBC-PT with FastEthernet0 port

---

## 🏙️ CITY B - CABLE CONNECTIONS

**EXACT COPY OF CITY A CONNECTIONS**

Replace all device names:
- `CityA-XXX` → `CityB-XXX`

**Example:**
- Connection 1: `CityB-Core-R1` Gig0/0 ↔ `CityB-Core-SW1` Gig1/0/1
- Connection 7: `CityB-Border-R1` Gig0/0 ↔ `CityB-Core-R1` Gig1/1
- Connection 8: `CityB-Border-R1` Serial0/0/0 ↔ `ISP-Border-R2` Serial0/0/0
- etc.

**Total City B connections: 46 (same as City A)**

---

## 🌐 ISP/INTERNET BACKBONE CONNECTIONS (8 connections)

### **ISP Core Infrastructure**

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 1 | `ISP-Border-R1` | `Gig0/1` | `ISP-Core-R1` | `Gig0/0` | Straight-Through |
| 2 | `ISP-Border-R2` | `Gig0/1` | `ISP-Core-R1` | `Gig0/1` | Straight-Through |
| 3 | `ISP-Core-R1` | `Gig0/2` | `ISP-Core-R2` | `Gig0/0` | Straight-Through |
| 4 | `ISP-Core-R2` | `Gig0/1` | `Internet-DNS-Root` | `Fa0` | Straight-Through |
| 5 | `ISP-Core-R2` | `Gig0/2` | `Internet-Web-Server` | `Fa0` | Straight-Through |

**Why:**
- ISP has redundant core routers
- Internet servers accessible from both cities

---

### **WAN Links (City ↔ ISP)**

| # | From Device | From Port | To Device | To Port | Cable Type |
|---|-------------|-----------|-----------|---------|------------|
| 6 | `CityA-Border-R1` | `Serial0/0/0` | `ISP-Border-R1` | `Serial0/0/0` | Serial DCE |
| 7 | `CityB-Border-R1` | `Serial0/0/0` | `ISP-Border-R2` | `Serial0/0/0` | Serial DCE |

**CRITICAL:**
- Set **DCE side** on ONE router (usually ISP side)
- DCE provides clock rate (set to 64000 or 128000)

---

## 📊 CONNECTION SUMMARY

### **City A:**
- Core infrastructure: 12 connections
- Government zone: 8 connections
- Residential zone: 7 connections (wired)
- Commercial zone: 4 connections (wired)
- Transportation zone: 5 connections
- Utilities zone: 4 connections
- **Subtotal: ~40 wired connections**

### **City B:**
- ~40 wired connections (mirror of City A)

### **ISP/Internet:**
- 5 backbone connections
- 2 WAN links to cities
- **Subtotal: 7 connections**

### **Grand Total: ~87 wired connections + ~15 wireless associations**

---

## 🔍 CONNECTION VERIFICATION CHECKLIST

After connecting all cables, verify:

**Visual Checks:**
- [ ] All links show **green triangles** at both ends
- [ ] No **red X** marks (indicates wrong cable or port)
- [ ] Orange triangles = interface administratively down (normal, will fix in config)

**Serial Link Checks:**
- [ ] Serial connections show as connected
- [ ] DCE side configured (will set clock rate later)

**Wireless Checks:**
- [ ] Wireless devices show wireless icon enabled
- [ ] Do NOT connect cables to smartphones/tablets (wireless only)

---

## 🚨 COMMON CONNECTION MISTAKES

### **Mistake 1: Wrong Cable Type**
❌ Using cross-over for device-to-switch
✅ Use straight-through for device-to-switch

### **Mistake 2: Serial DCE/DTE Confusion**
❌ Both routers set as DCE or both as DTE
✅ One DCE (ISP side), one DTE (City side)

### **Mistake 3: Connecting Wireless Devices with Cables**
❌ Smartphone with Ethernet cable
✅ Smartphones/tablets connect wirelessly only

### **Mistake 4: Wrong Port Numbers**
❌ Using Fa0/25 on 24-port switch
✅ Check switch model for available ports

### **Mistake 5: Forgetting Redundancy Links**
❌ Single link between core switches
✅ Dual links (Spanning Tree will manage)

---

## ⏱️ ESTIMATED TIME

- **City A connections:** 1.5 hours
- **City B connections:** 1 hour (faster, same pattern)
- **ISP connections:** 15 minutes
- **Total:** ~2.5-3 hours

---

## 📝 NEXT STEP

✅ **All 102 devices connected**

➡️ **Next:** Read `03_TOPOLOGY_MAP.md` for visual reference, then proceed to **PART2_CONFIGURATION**

---

## 💾 SAVE YOUR WORK!

**Before moving to configuration:**

```
File → Save As → "DualCity_Physical_Complete.pkt"
```

**Create backup:**
```
Copy file to: DualCity_Physical_Complete_BACKUP.pkt
```

---

## 🎨 OPTIONAL: Color Coding Connections

For easier visual debugging:
- **Core links:** Blue cables
- **Zone links:** Green cables
- **Server links:** Orange cables
- **IoT links:** Purple cables
- **WAN links:** Red cables

*(Right-click cable → Change color)*

---

Ready to configure? Proceed to **PART2_CONFIGURATION/01_IP_ADDRESSING.md**! 🚀
