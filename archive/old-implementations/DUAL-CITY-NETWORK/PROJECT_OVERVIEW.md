# DUAL-CITY SMART NETWORK PROJECT
## Complete Implementation Guide with All Technologies

---

## 🎯 PROJECT SCOPE

**Two realistic smart cities (City A and City B) connected via Internet, demonstrating ALL networking technologies**

### Technologies Demonstrated:
✅ **IPv4 & IPv6** - Dual-stack addressing throughout
✅ **VLANs** - Multiple VLANs per city (Government, Residential, Commercial, Transportation)
✅ **NAT** - Network Address Translation at ISP border
✅ **Subnetting** - Hierarchical IP address design
✅ **OSPF** - Dynamic routing protocol (Open Shortest Path First)
✅ **DHCP** - Dynamic Host Configuration Protocol (8 pools)
✅ **DNS** - Domain Name System (city-a.local, city-b.local)
✅ **ACLs** - Access Control Lists for security
✅ **QoS** - Quality of Service prioritization
✅ **Wireless** - WiFi Access Points + Cellular Towers
✅ **Trunking** - 802.1Q VLAN trunks
✅ **STP** - Spanning Tree Protocol
✅ **Port Security** - MAC address filtering
✅ **Inter-VLAN Routing** - Router-on-a-stick

---

## 📊 NETWORK STATISTICS

**Total Devices:** ~120 devices
- **City A:** 55 devices
- **City B:** 55 devices (mirror of City A)
- **Internet Backbone:** 10 devices

**Device Breakdown per City:**
- 5 Routers (Core, Border, Distribution zones)
- 8 Switches (Distribution + Access layers)
- 4 Servers (DNS, DHCP, Web, Email)
- 1 Cellular Tower
- 3 WiFi Access Points
- 15 IoT Sensors (traffic, environment, utilities)
- 8 End devices (PCs, laptops, smartphones)
- 6 Specialized devices (traffic lights, security cameras)

**VLANs per City:** 8 VLANs
- VLAN 10: Government Services
- VLAN 20: Residential Zone
- VLAN 30: Commercial Zone
- VLAN 40: Transportation Infrastructure
- VLAN 50: Public WiFi
- VLAN 60: Emergency Services
- VLAN 70: Utilities Management
- VLAN 99: Network Management

---

## 🗺️ CITY ZONES (Each City Has)

### **Zone 1: GOVERNMENT DISTRICT**
- City Hall network (admin workstations)
- Police headquarters (emergency network)
- Fire station (dispatch system)
- **Technologies:** Static IPs, ACLs, QoS priority

### **Zone 2: RESIDENTIAL AREA**
- Apartment buildings (home routers)
- Smart homes (IoT devices)
- Cellular tower (mobile coverage)
- **Technologies:** DHCP, NAT, Wireless, IPv6

### **Zone 3: COMMERCIAL DISTRICT**
- Office buildings (enterprise WiFi)
- Retail stores (POS systems)
- Public WiFi hotspots
- **Technologies:** VLANs, Trunking, Port Security

### **Zone 4: TRANSPORTATION HUB**
- Traffic light controllers (IoT)
- Smart parking sensors
- Bus tracking system
- **Technologies:** IoT VLANs, QoS, ACLs

### **Zone 5: UTILITIES & SERVICES**
- Water monitoring sensors
- Smart grid sensors
- Waste management IoT
- **Technologies:** Dedicated VLAN, low-latency routing

---

## 🌐 INTER-CITY CONNECTION

**City A ↔ ISP Cloud ↔ City B**

- **WAN Technology:** Serial links (simulating fiber/leased lines)
- **Routing:** OSPF Area 0 (backbone)
- **NAT:** Configured at each city's border router
- **Redundancy:** Dual ISP connections per city
- **Bandwidth:** Simulated 1 Gbps links

**Data Flows to Demonstrate:**
1. City A Resident → City B Web Server (HTTP)
2. City A Traffic Sensor → City B Control Center (IoT data)
3. City A Police → City B Police (Emergency coordination)
4. DNS resolution across cities
5. Email between cities

---

## 📁 DOCUMENTATION STRUCTURE

### **PART 1: PHYSICAL SETUP** (What to Place & Connect)
- `01_DEVICE_LIST.md` - Every device with model numbers
- `02_CABLE_CONNECTIONS.md` - Every cable, port-to-port
- `03_TOPOLOGY_MAP.md` - Visual ASCII layout

### **PART 2: CONFIGURATION** (How to Configure Everything)
- `01_IP_ADDRESSING.md` - Complete IPv4/IPv6 scheme
- `02_ROUTER_SETUP.md` - All router configs (OSPF, NAT, sub-interfaces)
- `03_SWITCH_SETUP.md` - All switch configs (VLANs, trunks, STP)
- `04_SERVER_SETUP.md` - DHCP, DNS, Web, Email
- `05_WIRELESS_SETUP.md` - WiFi APs + Cellular towers
- `06_SECURITY_SETUP.md` - ACLs, Port Security, QoS
- `07_INTER_CITY_WAN.md` - WAN links and routing

### **PART 3: VERIFICATION** (Quick Checks)
- `01_VERIFICATION_COMMANDS.md` - Commands to verify each technology

---

## 🎓 PROFESSOR WILL SEE

**At a glance, your network demonstrates:**

1. **Realistic City Layout** ✅
   - Government, Residential, Commercial, Transportation zones
   - Emergency services, utilities, public WiFi
   - Cellular coverage, IoT sensors everywhere

2. **All Major Technologies** ✅
   - IPv4/IPv6 dual-stack
   - VLANs with proper segmentation
   - OSPF dynamic routing (not just static)
   - NAT at ISP boundaries
   - DHCP with multiple pools
   - DNS with two city domains
   - ACLs for inter-zone security
   - QoS for emergency traffic priority

3. **Inter-City Connectivity** ✅
   - Two separate cities
   - Connected via ISP cloud
   - Data flows between cities
   - Realistic WAN simulation

4. **Wireless Infrastructure** ✅
   - WiFi access points
   - Cellular towers
   - Mobile device support

5. **Scalability** ✅
   - Can copy City A → City B
   - Modular design
   - Easy to expand

---

## ⏱️ ESTIMATED IMPLEMENTATION TIME

- **PART 1 (Physical Setup):** 2 hours
  - Place 120 devices
  - Connect all cables (~150 connections)

- **PART 2 (Configuration):** 4-5 hours
  - Routers: 1.5 hours
  - Switches: 1.5 hours
  - Servers: 1 hour
  - Wireless: 30 min
  - Security: 30 min

- **PART 3 (Verification):** 30 minutes
  - Test connectivity
  - Verify all technologies

**TOTAL: 6-8 hours** (can be split over multiple days)

---

## 🚀 NEXT STEPS

1. ✅ Read PROJECT_OVERVIEW.md (you are here)
2. 📖 Read PART1_PHYSICAL_SETUP/01_DEVICE_LIST.md
3. 🔌 Follow PART1_PHYSICAL_SETUP/02_CABLE_CONNECTIONS.md
4. ⚙️ Configure using PART2_CONFIGURATION guides (in order)
5. ✔️ Verify with PART3_VERIFICATION commands

---

## 📌 IMPORTANT NOTES

- **Professional Naming Convention:**
  - City A: `CityA-Core-R1`, `CityA-Gov-SW1`, `CityA-DNS-Server`
  - City B: `CityB-Core-R1`, `CityB-Gov-SW1`, `CityB-DNS-Server`
  - ISP: `ISP-Cloud-R1`, `ISP-Border-R2`

- **Color Coding Recommendation:**
  - Routers: Blue
  - Switches: Green
  - Servers: Orange
  - Wireless: Yellow
  - IoT: Purple

- **Save Frequently:**
  - Save after each major section
  - Keep backups (CityA-complete.pkt, CityB-complete.pkt)

---

## 🎯 LEARNING OUTCOMES

After completing this project, you will understand:
- How real cities design their network infrastructure
- Why VLANs are essential for large networks
- How OSPF dynamically adjusts routing
- How NAT enables private networks to access the internet
- How DHCP scales to thousands of devices
- How DNS makes the internet usable
- How ACLs protect sensitive infrastructure
- How QoS ensures emergency services work during congestion
- How wireless technologies integrate with wired networks

---

**PROJECT STATUS: Ready for Implementation**

Proceed to **PART1_PHYSICAL_SETUP/01_DEVICE_LIST.md** to begin! 🚀
