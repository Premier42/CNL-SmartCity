# PART 1: PHYSICAL SETUP
## 03 - NETWORK TOPOLOGY MAP

**Visual reference for the complete dual-city network**

---

## 🗺️ COMPLETE NETWORK TOPOLOGY

```
═══════════════════════════════════════════════════════════════════════════════════
                           DUAL-CITY SMART NETWORK
═══════════════════════════════════════════════════════════════════════════════════

┌──────────────────────────┐         ┌──────────────┐         ┌──────────────────────────┐
│       CITY A             │         │   ISP/       │         │       CITY B             │
│                          │         │  INTERNET    │         │                          │
│  ┌────────────────────┐  │         │              │         │  ┌────────────────────┐  │
│  │ Border Router      │  │ Serial  │ ┌──────────┐ │  Serial │  │ Border Router      │  │
│  │  CityA-Border-R1   │◄─┼─────────┼─┤ISP-Border│─┼─────────┼─►│  CityB-Border-R1   │  │
│  │                    │  │  WAN    │ │   -R1    │ │   WAN   │  │                    │  │
│  └─────────┬──────────┘  │         │ └────┬─────┘ │         │  └─────────┬──────────┘  │
│            │ NAT         │         │      │       │         │            │ NAT         │
│            │             │         │ ┌────▼─────┐ │         │            │             │
│  ┌─────────▼──────────┐  │         │ │ISP-Core  │ │         │  ┌─────────▼──────────┐  │
│  │   Core Router      │  │         │ │   -R1    │ │         │  │   Core Router      │  │
│  │   CityA-Core-R1    │  │         │ └────┬─────┘ │         │  │   CityB-Core-R1    │  │
│  │   (OSPF Hub)       │  │         │      │       │         │  │   (OSPF Hub)       │  │
│  └─┬───┬────┬─────┬───┘  │         │ ┌────▼─────┐ │         │  └─┬───┬────┬─────┬───┘  │
│    │   │    │     │      │         │ │ISP-Core  │ │         │    │   │    │     │      │
│    │   │    │     │      │         │ │   -R2    │ │         │    │   │    │     │      │
│┌───▼┐┌─▼──┐┌▼───┐┌▼────┐ │         │ └──┬────┬──┘ │         │┌───▼┐┌─▼──┐┌▼───┐┌▼────┐ │
││Gov ││Res ││Com ││Srv  │ │         │    │    │    │         ││Gov ││Res ││Com ││Srv  │ │
││-R1 ││-R1 ││-R1 ││Core │ │         │ ┌──▼──┐ ┌▼─┐ │         ││-R1 ││-R1 ││-R1 ││Core │ │
│└─┬──┘└┬───┘└┬───┘│ SW1 │ │         │ │DNS  │ │Web│ │         │└─┬──┘└┬───┘└┬───┘│ SW1 │ │
│  │    │     │    │     │ │         │ │Root │ │Srv│ │         │  │    │     │    │     │ │
│  │    │     │    └──┬──┘ │         │ └─────┘ └───┘ │         │  │    │     │    └──┬──┘ │
│  │    │     │       │    │         │                │         │  │    │     │       │    │
│  │    │     │  ┌────▼────┐         └────────────────┘         │  │    │     │  ┌────▼────┐
│  │    │     │  │Core-SW2 │                                    │  │    │     │  │Core-SW2 │
│  │    │     │  └─┬───┬───┘                                    │  │    │     │  └─┬───┬───┘
│  │    │     │    │   │                                        │  │    │     │    │   │
│  │    │     │  ┌─▼─┐┌▼──┐                                    │  │    │     │  ┌─▼─┐┌▼──┐
│  │    │     │  │Trn││Utl│                                    │  │    │     │  │Trn││Utl│
│  │    │     │  │SW1││SW1│                                    │  │    │     │  │SW1││SW1│
│  │    │     │  └───┘└───┘                                    │  │    │     │  └───┘└───┘
│  │    │     │                                                │  │    │     │
└──┼────┼─────┼────────────────────────────────────────────────┘  └──┼────┼─────┼─────────┘
   │    │     │                                                       │    │     │
   │    │     │                                                       │    │     │
   ▼    ▼     ▼                                                       ▼    ▼     ▼
 ZONES ZONES ZONES                                                 ZONES ZONES ZONES
```

---

## 🏗️ CITY A - DETAILED ZONE LAYOUT

### **GOVERNMENT DISTRICT**
```
                      CityA-Core-R1
                           │
                      CityA-Gov-R1
                           │
                      CityA-Gov-SW1
                           │
        ┌──────────┬────────┼────────┬──────────┬──────────┐
        │          │        │        │          │          │
     Gov-PC-1  Gov-PC-2  Police  Fire-PC  WiFi-AP  Camera-1
                         -PC-1                   Camera-2
                                                 Fire-Sensor

VLANs:
• VLAN 10: Government (Gov-PC-1, Gov-PC-2, WiFi-AP)
• VLAN 60: Emergency (Police-PC-1, Fire-PC-1, Cameras, Fire-Sensor)
```

---

### **RESIDENTIAL ZONE**
```
                      CityA-Core-R1
                           │
                      CityA-Res-R1
                      ┌────┴────┐
               CityA-Res-SW1   CityA-Res-SW2
                      │              │
        ┌─────┬───────┼───────┬──────┤
        │     │       │       │      │
     Home-PC Home  WiFi-AP Smart  Linksys-WRT300N
           -Laptop-1      Home-1      │
                          Smart   (Wireless
                          Home-2   coverage)
                          Env-1

                      Smartphone-1
                      (connects wirelessly)

VLAN 20: Residential (all devices)
```

---

### **COMMERCIAL ZONE**
```
                      CityA-Core-R1
                           │
                      CityA-Com-R1
                           │
                      CityA-Com-SW1
                           │
        ┌──────────┬────────┼────────┬──────────┐
        │          │        │        │          │
     Com-PC-1  Com-Laptop Retail  WiFi-Pub
                           -POS-1   -AP1
                                      │
                                  (wireless)
                                      │
                            Public-Phone-1
                            Public-Tablet-1

VLANs:
• VLAN 30: Commercial (Com-PC-1, Laptop, POS)
• VLAN 50: Public WiFi (WiFi-Pub-AP1, wireless clients)
```

---

### **TRANSPORTATION ZONE**
```
                      CityA-Core-SW2
                           │
                      CityA-Trans-SW1
                           │
        ┌──────────┬────────┼────────┬──────────┐
        │          │        │        │          │
   TrafficLight TrafficLight Parking Parking  BusTracker
       -1           -2      Sensor-1 Sensor-2    -1

VLAN 40: Transportation (all IoT devices)
```

---

### **UTILITIES ZONE**
```
                      CityA-Core-SW2
                           │
                      CityA-Util-SW1
                           │
        ┌──────────┬────────┼────────┬──────────┐
        │          │        │        │          │
   SmartGrid  SmartGrid  Water    Water
      -1         -2      Monitor  Monitor
                          -1       -2

VLAN 70: Utilities (all monitoring devices)
```

---

### **SERVER ZONE**
```
                      CityA-Core-R1
                           │
                      CityA-Core-SW1
                           │
        ┌──────────┬────────┼────────┬──────────┐
        │          │        │        │          │
    DNS-Server DHCP-Server Web-Server Email-Server

VLAN 99: Management/Services (all infrastructure servers)
```

---

## 🌐 ISP/INTERNET BACKBONE

```
                    ┌─────────────────────────┐
                    │   INTERNET BACKBONE     │
                    │                         │
                    │    ┌──────────────┐     │
                    │    │ ISP-Core-R1  │     │
                    │    └──┬────────┬──┘     │
                    │       │        │        │
                    │  ┌────▼──┐  ┌──▼────┐   │
                    │  │ISP-   │  │ISP-   │   │
                    │  │Core   │  │Border │   │
                    │  │-R2    │  │-R1    │   │
                    │  └┬───┬──┘  └───┬───┘   │
                    │   │   │         │       │
                    │ ┌─▼┐ ┌▼─┐      ┌▼─────┐ │
                    │ │DNS│ │Web│    │ISP-  │ │
                    │ │Root │Srv│    │Border│ │
                    │ └───┘ └──┘    │-R2   │ │
                    │                └──────┘ │
                    └────────┬──────────┬─────┘
                          Serial    Serial
                         WAN Link  WAN Link
                             │         │
                    CityA-Border-R1  CityB-Border-R1
```

---

## 🔗 DATA FLOW EXAMPLES

### **Example 1: City A PC accesses City B Web Server**

```
1. CityA-Gov-PC-1 (192.168.10.10)
        │ "I want www.city-b.local"
        ▼
2. DNS query to CityA-DNS-Server
        │ Returns: 203.0.113.50
        ▼
3. Packet to CityA-Gov-R1 (default gateway)
        │ VLAN 10 → routes to Core
        ▼
4. CityA-Core-R1 (OSPF routing)
        │ Best path = via CityA-Border-R1
        ▼
5. CityA-Border-R1 (NAT)
        │ Translates: 192.168.10.10 → 203.0.113.1 (public IP)
        ▼
6. Serial WAN link to ISP-Border-R1
        │ WAN routing
        ▼
7. ISP-Core-R1 (OSPF)
        │ Routes to ISP-Border-R2
        ▼
8. ISP-Border-R2
        │ Routes to CityB-Border-R1
        ▼
9. CityB-Border-R1 (NAT reverse)
        │ Translates: 203.0.113.50 → 192.168.99.50 (CityB Web Server)
        ▼
10. CityB-Core-R1
        │ Routes to CityB-Core-SW1
        ▼
11. CityB-Web-Server (VLAN 99)
        │ Responds with web page
        ▼
12. Response follows reverse path back to CityA-Gov-PC-1

Total hops: ~12
Demonstrates: VLAN routing, OSPF, NAT, WAN, DNS
```

---

### **Example 2: IoT Sensor reports to local server**

```
1. CityA-TrafficLight-1 (DHCP: 192.168.40.101)
        │ Sends traffic data
        ▼
2. CityA-Trans-SW1 (VLAN 40)
        │ Trunks to Core-SW2
        ▼
3. CityA-Core-SW2
        │ Routes to Core-R1 (inter-VLAN)
        ▼
4. CityA-Core-R1
        │ Routes VLAN 40 → VLAN 99
        ▼
5. CityA-Core-SW1 (VLAN 99)
        │ Delivers to server
        ▼
6. CityA-Web-Server
        │ Logs data, responds

Total hops: 6
Demonstrates: VLANs, Trunking, Inter-VLAN routing
```

---

### **Example 3: Emergency coordination between cities**

```
1. CityA-Police-PC-1 (VLAN 60, QoS priority)
        │ Emergency call to CityB Police
        ▼
2. CityA-Gov-SW1 → CityA-Gov-R1
        │ QoS marks traffic as HIGH PRIORITY
        ▼
3. CityA-Core-R1 (OSPF)
        │ QoS ensures priority queuing
        ▼
4. CityA-Border-R1 → WAN → ISP → CityB-Border-R1
        │ Traffic prioritized across WAN
        ▼
5. CityB-Core-R1 → CityB-Gov-R1
        │ QoS maintained
        ▼
6. CityB-Police-PC-1 (VLAN 60)
        │ Receives call with <50ms latency

Demonstrates: QoS, VLAN priority, OSPF routing, WAN
```

---

## 📊 TECHNOLOGY MAPPING

### **Where Each Technology is Used:**

| Technology | Location | Devices |
|------------|----------|---------|
| **IPv4 Addressing** | Everywhere | All devices (192.168.x.x, 203.0.113.x) |
| **IPv6 Addressing** | Everywhere | All devices (2001:db8:xxxx::) |
| **VLANs** | All switches | 8 VLANs per city |
| **Trunking (802.1Q)** | Switch uplinks | 24+ trunk links |
| **OSPF** | All routers | 14 routers (3 areas) |
| **NAT** | Border routers | 2 routers (CityA/B-Border-R1) |
| **DHCP** | Servers | 2 servers (16 pools total) |
| **DNS** | Servers | 3 servers (CityA, CityB, Internet) |
| **ACLs** | Routers | Border + Core routers |
| **QoS** | Core routers | Priority for VLAN 60 |
| **Wireless** | APs + Cellular | 6 APs + 2 Linksys WRT300N (cellular sim) |
| **STP** | Core switches | CityA/B-Core-SW1/SW2 |
| **Port Security** | Access switches | All access ports |

---

## 🎯 PROFESSOR'S VIEW - QUICK GLANCE

**What professor will immediately see:**

1. ✅ **Two separate cities** (left and right sides)
2. ✅ **ISP connection in middle** (realistic internet simulation)
3. ✅ **Multiple zones per city** (Government, Residential, Commercial, Transportation, Utilities)
4. ✅ **Hierarchical design** (Border → Core → Distribution → Access layers)
5. ✅ **Wireless infrastructure** (WiFi APs + Cellular towers)
6. ✅ **IoT sensors everywhere** (traffic, utilities, smart homes)
7. ✅ **Redundancy** (dual core switches, dual ISP routers)
8. ✅ **Professional naming** (CityA-ZoneName-DeviceType-Number)

---

## 📐 ADDRESSING HIERARCHY PREVIEW

**CITY A:**
- Border WAN: 203.0.113.1 (public)
- Internal: 192.168.0.0/16
  - VLAN 10: 192.168.10.0/24 (Government)
  - VLAN 20: 192.168.20.0/24 (Residential)
  - VLAN 30: 192.168.30.0/24 (Commercial)
  - VLAN 40: 192.168.40.0/24 (Transportation)
  - VLAN 50: 192.168.50.0/24 (Public WiFi)
  - VLAN 60: 192.168.60.0/24 (Emergency)
  - VLAN 70: 192.168.70.0/24 (Utilities)
  - VLAN 99: 192.168.99.0/24 (Management)

**CITY B:**
- Border WAN: 203.0.114.1 (public)
- Internal: 192.168.0.0/16 (same private range, NAT isolates)

**ISP:**
- 203.0.113.0/24 (CityA public range)
- 203.0.114.0/24 (CityB public range)
- 8.8.8.8 (Internet DNS simulation)

*(Full details in PART2_CONFIGURATION/01_IP_ADDRESSING.md)*

---

## 📝 NEXT STEP

✅ **Physical topology understood**

➡️ **Next:** Proceed to **PART2_CONFIGURATION/01_IP_ADDRESSING.md** to start configuring!

---

## 💡 TIPS FOR PACKET TRACER LAYOUT

1. **Zoom level:** 75-100% to see everything
2. **Workspace size:** Use maximum workspace area
3. **Device spacing:** Leave 2-3 device widths between zones
4. **Labels:** Show device names (View → Show Device Names)
5. **Color groups:** Use notes/labels to mark zones

**Save diagram view:**
```
File → Export → Export Image → "DualCity_Topology.png"
```

---

Ready to configure IP addresses? Open **PART2_CONFIGURATION/01_IP_ADDRESSING.md**! 🚀
