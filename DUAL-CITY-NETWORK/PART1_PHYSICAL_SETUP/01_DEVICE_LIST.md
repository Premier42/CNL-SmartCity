# PART 1: PHYSICAL SETUP
## 01 - COMPLETE DEVICE LIST

**Read this BEFORE opening Packet Tracer**

⚠️ **COMPATIBILITY NOTE:** See `../COMPATIBILITY_GUIDE.md` for Packet Tracer version requirements

---

## 📋 DEVICE SUMMARY

| Category | City A Qty | City B Qty | ISP/Internet | Total |
|----------|-----------|-----------|--------------|-------|
| Routers | 5 | 5 | 4 | **14** |
| Switches | 8 | 8 | 0 | **16** |
| Servers | 4 | 4 | 2 | **10** |
| Wireless Devices | 4 | 4 | 0 | **8** |
| IoT Devices | 15 | 15 | 0 | **30** |
| End Devices | 12 | 12 | 0 | **24** |
| **TOTAL** | **48** | **48** | **6** | **102** |

---

## 🏙️ CITY A - DEVICE LIST

### **ROUTERS (5 devices)**

| # | Device Name | Model | Purpose | Interfaces Needed |
|---|-------------|-------|---------|-------------------|
| 1 | `CityA-Border-R1` | **Cisco 2911** | Border router (connects to ISP, runs NAT) | 2× Gig, 1× Serial |
| 2 | `CityA-Core-R1` | **Cisco 2911** | Core city router (OSPF hub, inter-VLAN routing) | 3× Gig |
| 3 | `CityA-Gov-R1` | **Cisco 2911** | Government district router | 2× Gig |
| 4 | `CityA-Res-R1` | **Cisco 2911** | Residential zone router | 2× Gig |
| 5 | `CityA-Com-R1` | **Cisco 2911** | Commercial zone router | 2× Gig |

**Why these routers:**
- Border: Needs serial port for WAN
- Core: Needs multiple interfaces for OSPF areas
- Zone routers: Handle local VLANs and connect to core

**Interface naming:** Cisco 2911 uses `GigabitEthernet0/0`, `GigabitEthernet0/1`, etc. (NOT `0/0/0`)

---

### **SWITCHES (8 devices)**

| # | Device Name | Model | Purpose | Ports Needed |
|---|-------------|-------|---------|--------------|
| 1 | `CityA-Core-SW1` | **Cisco 2960-24TT** | Core distribution switch | 24 ports + 2 Gig uplinks |
| 2 | `CityA-Core-SW2` | **Cisco 2960-24TT** | Core distribution switch (redundancy) | 24 ports + 2 Gig uplinks |
| 3 | `CityA-Gov-SW1` | **Cisco 2960-24TT** | Government access switch | 24 ports |
| 4 | `CityA-Res-SW1` | **Cisco 2960-24TT** | Residential access switch | 24 ports |
| 5 | `CityA-Res-SW2` | **Cisco 2960-24TT** | Residential access switch 2 | 24 ports |
| 6 | `CityA-Com-SW1` | **Cisco 2960-24TT** | Commercial access switch | 24 ports |
| 7 | `CityA-Trans-SW1` | **Cisco 2960-24TT** | Transportation access switch | 24 ports |
| 8 | `CityA-Util-SW1` | **Cisco 2960-24TT** | Utilities access switch | 24 ports |

**Why multiple switches:**
- Core: Redundancy and high capacity
- Zone switches: Segmentation and broadcast control
- Access: Connect end devices in each zone

**Why 2960-24TT:** Universal availability in all PT versions, supports VLANs & trunking perfectly

---

### **SERVERS (4 devices)**

| # | Device Name | Model | Services Running | VLAN |
|---|-------------|-------|------------------|------|
| 1 | `CityA-DNS-Server` | **Server-PT** | DNS (city-a.local domain) | VLAN 99 |
| 2 | `CityA-DHCP-Server` | **Server-PT** | DHCP (8 pools for all VLANs) | VLAN 99 |
| 3 | `CityA-Web-Server` | **Server-PT** | HTTP/HTTPS (city website) | VLAN 99 |
| 4 | `CityA-Email-Server` | **Server-PT** | SMTP/POP3 (email@city-a.local) | VLAN 99 |

**VLAN 99 = Management/Services VLAN**

---

### **WIRELESS DEVICES (4 devices)**

| # | Device Name | Model | Purpose | Location | Wired Port |
|---|-------------|-------|---------|----------|------------|
| 1 | `CityA-CellTower-1` | **Linksys WRT300N** | 4G/LTE cellular coverage (simulated) | Residential zone | Internet port |
| 2 | `CityA-WiFi-Gov-AP1` | **AccessPoint-PT** | Government building WiFi | Government zone | Ethernet1 |
| 3 | `CityA-WiFi-Pub-AP1` | **AccessPoint-PT** | Public WiFi hotspot | Commercial zone | Ethernet1 |
| 4 | `CityA-WiFi-Res-AP1` | **AccessPoint-PT** | Residential WiFi | Residential zone | Ethernet1 |

**CRITICAL - Cellular Tower Reality:**
- ⚠️ **Packet Tracer has NO dedicated "Cell Tower" device with Ethernet in ANY version**
- ⚠️ If "Cell Tower" exists in PT 8.2.2+, it's wireless-only (no Ethernet port)
- ✅ **SOLUTION: Use Linksys WRT300N** configured as cellular access point
- ✅ **WRT300N has "Internet" port** for wired backhaul connection
- Configure SSID as `CityA-4G-LTE` to simulate cellular network
- Disable DHCP server on WRT300N (router will provide DHCP)

**How to Setup Linksys WRT300N as Cell Tower:**
1. Place Linksys WRT300N from Network Devices → Wireless Devices
2. Connect **Internet port** to switch via Ethernet cable
3. Label as "CityA-CellTower-1"
4. Configure wireless SSID: "CityA-4G-LTE"
5. Disable DHCP server (use network DHCP instead)

**Why Linksys WRT300N:**
- ✅ Has physical Ethernet port (Internet/WAN port)
- ✅ Supports wireless clients (smartphones, tablets)
- ✅ Available in all PT versions
- ✅ Can be configured to simulate cellular backhaul

---

### **IoT DEVICES (15 devices)**

**🔌 CRITICAL - CONNECTIVITY ALERT:**
- ⚠️ **Many IoT devices are WIRELESS-ONLY** (Webcam, Motion Detector, GPS, etc.)
- ⚠️ **Wireless devices cannot be connected via Ethernet cable**
- ✅ **Solution: Use SBC-PT (Single Board Computer) for wired IoT**
- ✅ **Alternative: Use PC-PT** (works in all versions, has Ethernet)
- 📖 **See:** `IOT_DEVICE_CONNECTIVITY_GUIDE.md` for complete details

**🎯 RECOMMENDED DEVICE MODELS (All have Ethernet ports):**

#### Government Zone (3 devices) - **Use SBC-PT**
| # | Device Name | Model | Purpose | VLAN | Connection |
|---|-------------|-------|---------|------|-----------|
| 1 | `CityA-Gov-Camera-1` | **SBC-PT** | Security camera | VLAN 60 | FastEthernet0 |
| 2 | `CityA-Gov-Camera-2` | **SBC-PT** | Security camera | VLAN 60 | FastEthernet0 |
| 3 | `CityA-Fire-Sensor-1` | **SBC-PT** | Fire alarm sensor | VLAN 60 | FastEthernet0 |

**Location in PT:** End Devices → IoT Devices → SBC

#### Transportation Zone (5 devices) - **Use SBC-PT**
| # | Device Name | Model | Purpose | VLAN | Connection |
|---|-------------|-------|---------|------|-----------|
| 4 | `CityA-TrafficLight-1` | **SBC-PT** | Traffic light controller | VLAN 40 | FastEthernet0 |
| 5 | `CityA-TrafficLight-2` | **SBC-PT** | Traffic light controller | VLAN 40 | FastEthernet0 |
| 6 | `CityA-ParkingSensor-1` | **SBC-PT** | Smart parking sensor | VLAN 40 | FastEthernet0 |
| 7 | `CityA-ParkingSensor-2` | **SBC-PT** | Smart parking sensor | VLAN 40 | FastEthernet0 |
| 8 | `CityA-BusTracker-1` | **SBC-PT** | Bus location tracker | VLAN 40 | FastEthernet0 |

#### Utilities Zone (4 devices) - **Use SBC-PT**
| # | Device Name | Model | Purpose | VLAN | Connection |
|---|-------------|-------|---------|------|-----------|
| 9 | `CityA-SmartGrid-1` | **SBC-PT** | Power grid sensor | VLAN 70 | FastEthernet0 |
| 10 | `CityA-SmartGrid-2` | **SBC-PT** | Power grid sensor | VLAN 70 | FastEthernet0 |
| 11 | `CityA-WaterMonitor-1` | **SBC-PT** | Water quality monitor | VLAN 70 | FastEthernet0 |
| 12 | `CityA-WaterMonitor-2` | **SBC-PT** | Water quality monitor | VLAN 70 | FastEthernet0 |

#### Residential Zone (3 devices) - **Use Home Gateway + SBC-PT**
| # | Device Name | Model | Purpose | VLAN | Connection |
|---|-------------|-------|---------|------|-----------|
| 13 | `CityA-SmartHome-1` | **Home Gateway** | Smart home hub | VLAN 20 | Ethernet0 |
| 14 | `CityA-SmartHome-2` | **Home Gateway** | Smart home hub | VLAN 20 | Ethernet0 |
| 15 | `CityA-EnvMonitor-1` | **SBC-PT** | Air quality sensor | VLAN 20 | FastEthernet0 |

**Location in PT:** End Devices → IoT Devices → Home Gateway

---

### **✅ DEVICE SELECTION RULES:**

1. **ALL IoT devices MUST have Ethernet ports** for wired connection
2. **Recommended Models:**
   - **SBC-PT** (Single Board Computer) - Best for sensors/controllers
   - **Home Gateway** - Best for smart home hubs
   - **PC-PT** - Universal fallback (works in all PT versions)
3. **AVOID These (Wireless-Only):**
   - ❌ Webcam
   - ❌ Motion Detector
   - ❌ GPS
   - ❌ Smoke Detector
   - ❌ Any device without visible Ethernet port

---

### **📱 ALTERNATIVE: Simple PC-PT Approach**

**If you want maximum simplicity:**
- Use **PC-PT** for ALL 15 IoT devices
- Label each PC with IoT name (e.g., "IoT-Camera-1", "IoT-Traffic-1")
- Configure DHCP or Static IP
- Works perfectly for networking demonstration

**Why this works:**
- ✅ PC-PT always has FastEthernet0 port
- ✅ Available in all PT versions (8.0+)
- ✅ Easy to configure and troubleshoot
- ✅ Demonstrates same networking concepts
- ✅ Professor evaluates networking, not IoT hardware realism

---

### **END DEVICES (12 devices)**

#### Government Zone (4 devices)
| # | Device Name | Model | Purpose | VLAN |
|---|-------------|-------|---------|------|
| 1 | `CityA-Gov-PC-1` | **PC-PT** | City Hall workstation | VLAN 10 |
| 2 | `CityA-Gov-PC-2` | **PC-PT** | City Hall workstation | VLAN 10 |
| 3 | `CityA-Police-PC-1` | **PC-PT** | Police HQ workstation | VLAN 60 |
| 4 | `CityA-Fire-PC-1` | **PC-PT** | Fire station dispatch | VLAN 60 |

#### Commercial Zone (3 devices)
| # | Device Name | Model | Purpose | VLAN |
|---|-------------|-------|---------|------|
| 5 | `CityA-Com-PC-1` | **PC-PT** | Office workstation | VLAN 30 |
| 6 | `CityA-Com-Laptop-1` | **Laptop-PT** | Office laptop | VLAN 30 |
| 7 | `CityA-Retail-POS-1` | **PC-PT** | Retail point-of-sale | VLAN 30 |

#### Residential Zone (3 devices)
| # | Device Name | Model | Purpose | VLAN |
|---|-------------|-------|---------|------|
| 8 | `CityA-Home-PC-1` | **PC-PT** | Resident home PC | VLAN 20 |
| 9 | `CityA-Home-Laptop-1` | **Laptop-PT** | Resident laptop | VLAN 20 |
| 10 | `CityA-Home-Smartphone-1` | **Smartphone-PT** | Resident mobile (WiFi) | VLAN 20 or 50 |

#### Public WiFi (2 devices)
| # | Device Name | Model | Purpose | VLAN |
|---|-------------|-------|---------|------|
| 11 | `CityA-Public-Phone-1` | **Smartphone-PT** | Public WiFi user | VLAN 50 |
| 12 | `CityA-Public-Tablet-1` | **Tablet-PT** | Public WiFi user | VLAN 50 |

---

## 🏙️ CITY B - DEVICE LIST

**EXACT COPY OF CITY A** - Replace all "CityA" with "CityB"

**Example:**
- `CityA-Border-R1` → `CityB-Border-R1`
- `CityA-Core-SW1` → `CityB-Core-SW1`
- `CityA-DNS-Server` → `CityB-DNS-Server`
- etc.

**Total City B devices: 48 (identical to City A)**

---

## 🌐 INTERNET BACKBONE / ISP (6 devices)

### **ISP ROUTERS (4 devices)**

| # | Device Name | Model | Purpose | Interfaces |
|---|-------------|-------|---------|-----------|
| 1 | `ISP-Border-R1` | **Cisco 2911** | ISP edge (connects City A) | 2× Gig, 1× Serial |
| 2 | `ISP-Border-R2` | **Cisco 2911** | ISP edge (connects City B) | 2× Gig, 1× Serial |
| 3 | `ISP-Core-R1` | **Cisco 2911** | ISP backbone router | 3× Gig |
| 4 | `ISP-Core-R2` | **Cisco 2911** | ISP backbone router (redundancy) | 3× Gig |

### **INTERNET SERVERS (2 devices)**

| # | Device Name | Model | Purpose |
|---|-------------|-------|---------|
| 1 | `Internet-DNS-Root` | **Server-PT** | Root DNS server (simulates 8.8.8.8) |
| 2 | `Internet-Web-Server` | **Server-PT** | Public website (simulates www.example.com) |

---

## 📊 DEVICE SUMMARY BY TECHNOLOGY

### **IPv4/IPv6 Dual-Stack:**
- ✅ ALL routers, switches (management), servers, end devices

### **VLANs (8 per city):**
- ✅ Configured on: All switches
- ✅ Inter-VLAN routing: Core routers

### **OSPF:**
- ✅ Enabled on: All City A routers, All City B routers, All ISP routers
- ✅ Areas: Area 0 (backbone), Area 10 (City A), Area 20 (City B)

### **NAT:**
- ✅ Configured on: `CityA-Border-R1`, `CityB-Border-R1`

### **DHCP:**
- ✅ Server: `CityA-DHCP-Server` (8 pools), `CityB-DHCP-Server` (8 pools)
- ✅ Helper addresses: Configured on all router sub-interfaces

### **DNS:**
- ✅ Primary: `CityA-DNS-Server` (city-a.local)
- ✅ Secondary: `CityB-DNS-Server` (city-b.local)
- ✅ Root: `Internet-DNS-Root`

### **ACLs:**
- ✅ Applied on: Border routers (NAT), Core routers (inter-VLAN)

### **QoS:**
- ✅ Applied on: Core routers (priority for VLAN 60 emergency)

### **Wireless:**
- ✅ WiFi: 3 APs per city
- ✅ Cellular: 1 tower per city

---

## 🔧 DEVICE MODEL STANDARDS & SUBSTITUTIONS

### **STANDARDIZED MODELS (Use These):**

**Routers:**
- **Standard:** Cisco 2911 (ALL routers in project)
- **Why:** Universal availability, consistent interface naming (`Gig0/0`, not `Gig0/0/0`)
- **If unavailable:** Cisco 1941 (check interface names with `show ip interface brief`)

**Switches:**
- **Standard:** Cisco 2960-24TT (ALL switches in project)
- **Why:** Available in all PT versions, perfect VLAN/trunk support
- **If unavailable:** 2950-24 (older but functional)

**Servers:**
- **Only option:** Server-PT (generic server device)
- No alternatives - this is the only server type in Packet Tracer

**Wireless:**
- **WiFi Access Points:** AccessPoint-PT (preferred) or Linksys WRT300N
- **Cellular Simulation:** Linksys WRT300N configured as AP (NO "Cell Tower" device exists!)
- **SSID for cellular:** `CityA-4G-LTE` or `CityB-4G-LTE`

**IoT Devices:**
- **PT 8.2+:** IoT-PT devices (Motion Detector, Environmental Monitor, etc.)
- **PT 8.0/8.1:** PC-PT labeled as IoT simulators
- **Works identically for demonstration purposes**

### **COMPATIBILITY MATRIX:**

| Device Type | PT 8.0 | PT 8.1 | PT 8.2+ | Workaround |
|-------------|--------|--------|---------|------------|
| Cisco 2911 | ✅ | ✅ | ✅ | Use 1941 if missing |
| Cisco 2960-24TT | ✅ | ✅ | ✅ | Use 2950-24 if missing |
| Linksys WRT300N | ✅ | ✅ | ✅ | None needed |
| AccessPoint-PT | ✅ | ✅ | ✅ | Use WRT300N |
| IoT-PT devices | ❌ | ⚠️ | ✅ | Use PC-PT |
| Server-PT | ✅ | ✅ | ✅ | None needed |

**See `../COMPATIBILITY_GUIDE.md` for detailed version-specific workarounds**

---

## ✅ DEVICE PLACEMENT CHECKLIST

Before moving to cable connections, verify you have placed:

**City A:**
- [ ] 5 routers
- [ ] 8 switches
- [ ] 4 servers
- [ ] 4 wireless devices
- [ ] 15 IoT devices
- [ ] 12 end devices
- **Total: 48 devices**

**City B:**
- [ ] 48 devices (exact copy of City A with "CityB" naming)

**ISP/Internet:**
- [ ] 4 ISP routers
- [ ] 2 internet servers
- **Total: 6 devices**

**GRAND TOTAL: 102 devices** ✅

---

## 🎨 RECOMMENDED LAYOUT IN PACKET TRACER

**Workspace Division:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│  CITY A (LEFT SIDE)            ISP (CENTER)    CITY B (RIGHT)│
│                                                               │
│  ┌─────────────┐           ┌──────────┐       ┌──────────┐  │
│  │ Government  │           │ISP Core  │       │Government│  │
│  │   Zone      │           │  + DNS   │       │   Zone   │  │
│  └─────────────┘           └──────────┘       └──────────┘  │
│                                  │                           │
│  ┌─────────────┐                 │            ┌──────────┐  │
│  │ Commercial  │────────Border───┴───Border───│Commercial│  │
│  │   Zone      │        R1              R1    │   Zone   │  │
│  └─────────────┘                               └──────────┘  │
│                                                               │
│  ┌─────────────┐                              ┌──────────┐  │
│  │Residential  │                              │Residential│  │
│  │   Zone      │                              │   Zone   │  │
│  └─────────────┘                              └──────────┘  │
│                                                               │
│  ┌─────────────┐                              ┌──────────┐  │
│  │Transportation│                             │Transport │  │
│  │& Utilities   │                             │& Util    │  │
│  └─────────────┘                              └──────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 NEXT STEP

✅ **You've read the device list**

➡️ **Next:** Open `02_CABLE_CONNECTIONS.md` to see how to connect all 102 devices

---

**IMPORTANT REMINDERS:**

1. **Use consistent naming:** CityA-ZoneName-DeviceType-Number
2. **Label every device** immediately after placing it
3. **Save your work** after placing City A, City B, and ISP separately
4. **Color code devices** (optional but helpful):
   - Routers: Blue
   - Switches: Green
   - Servers: Orange
   - Wireless: Yellow
   - IoT: Purple

**⚠️ PROJECT TOO LARGE?**
- This guide describes the **Full Implementation** (102 devices)
- If your computer struggles, see `00_SCALING_OPTIONS.md` for:
  - **Option B (Medium):** 53 devices - all technologies, less hardware stress
  - **Option C (Minimal):** 30 devices - quick build, core technologies only

**Estimated time to place all devices: 1.5-2 hours**

---

Ready to connect? Open **02_CABLE_CONNECTIONS.md** next! 🚀

**BEFORE YOU START:**
- ✅ Read `../COMPATIBILITY_GUIDE.md` if using PT 8.0 or 8.1
- ✅ Read `00_SCALING_OPTIONS.md` if concerned about device count
- ✅ Verify you have Cisco 2911 routers available
