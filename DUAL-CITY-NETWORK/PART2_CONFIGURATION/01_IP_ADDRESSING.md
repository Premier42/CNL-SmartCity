# PART 2: CONFIGURATION
## 01 - IP ADDRESSING SCHEME (IPv4 & IPv6)

**Complete addressing plan for dual-city network**

---

## 📋 ADDRESSING OVERVIEW

### **Design Principles:**
1. **Hierarchical subnetting** - Easy to remember and scale
2. **Dual-stack** - Every device gets both IPv4 and IPv6
3. **VLAN-based allocation** - VLAN number matches third octet
4. **NAT boundaries** - Public IPs at ISP edge
5. **Reserved ranges** - Leave room for growth

---

## 🌐 PUBLIC IP ALLOCATION (Internet-facing)

| Network | Range | Purpose | NAT Pool |
|---------|-------|---------|----------|
| City A Public | `203.0.113.0/24` | City A border (WAN side) | 203.0.113.1 - .254 |
| City B Public | `203.0.114.0/24` | City B border (WAN side) | 203.0.114.1 - .254 |
| ISP Backbone | `198.51.100.0/24` | ISP internal routing | N/A |
| Internet Services | `8.8.8.0/24` | Simulated internet servers | N/A |

---

## 🏙️ CITY A - IPv4 ADDRESSING

### **Private Network: 192.168.0.0/16**

| VLAN | Name | Subnet | Range | Gateway | DHCP Pool | Static IPs |
|------|------|--------|-------|---------|-----------|------------|
| **10** | Government | `192.168.10.0/24` | .1 - .254 | .1 | .100 - .200 | .1-.99 |
| **20** | Residential | `192.168.20.0/24` | .1 - .254 | .1 | .100 - .220 | .1-.99 |
| **30** | Commercial | `192.168.30.0/24` | .1 - .254 | .1 | .100 - .220 | .1-.99 |
| **40** | Transportation | `192.168.40.0/24` | .1 - .254 | .1 | .100 - .150 | .1-.99 |
| **50** | Public WiFi | `192.168.50.0/24` | .1 - .254 | .1 | .100 - .220 | .1-.99 |
| **60** | Emergency | `192.168.60.0/24` | .1 - .254 | .1 | .100 - .150 | .1-.99 |
| **70** | Utilities | `192.168.70.0/24` | .1 - .254 | .1 | .100 - .150 | .1-.99 |
| **99** | Management | `192.168.99.0/24` | .1 - .254 | .1 | N/A (static) | All |

**Subnetting Logic:**
- `/24` mask = 254 usable hosts per VLAN
- Third octet = VLAN number (easy to remember)
- Gateway always `.1`
- DHCP starts at `.100`
- Static reservations: `.1-.99`

---

### **CITY A - DETAILED DEVICE IPs (IPv4)**

#### **VLAN 10: Government (192.168.10.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Gov-R1` (Gateway) | `192.168.10.1` | Static | Sub-interface on core |
| `CityA-Gov-PC-1` | `192.168.10.101` | DHCP | Auto-assigned |
| `CityA-Gov-PC-2` | `192.168.10.102` | DHCP | Auto-assigned |
| `CityA-WiFi-Gov-AP1` | `192.168.10.50` | Static | WiFi management IP |

#### **VLAN 20: Residential (192.168.20.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Res-R1` (Gateway) | `192.168.20.1` | Static | Sub-interface |
| `CityA-Home-PC-1` | `192.168.20.101` | DHCP | Auto-assigned |
| `CityA-Home-Laptop-1` | `192.168.20.102` | DHCP | Auto-assigned |
| `CityA-WiFi-Res-AP1` | `192.168.20.50` | Static | WiFi management |
| `CityA-CellTower-1` | `192.168.20.60` | Static | Cellular backhaul |
| `CityA-SmartHome-1` | `192.168.20.111` | DHCP | IoT device |
| `CityA-SmartHome-2` | `192.168.20.112` | DHCP | IoT device |
| `CityA-EnvMonitor-1` | `192.168.20.113` | DHCP | IoT device |
| `CityA-Home-Smartphone-1` | `192.168.20.115` | DHCP | Wireless |

#### **VLAN 30: Commercial (192.168.30.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Com-R1` (Gateway) | `192.168.30.1` | Static | Sub-interface |
| `CityA-Com-PC-1` | `192.168.30.101` | DHCP | Office PC |
| `CityA-Com-Laptop-1` | `192.168.30.102` | DHCP | Office laptop |
| `CityA-Retail-POS-1` | `192.168.30.103` | DHCP | Point-of-sale |

#### **VLAN 40: Transportation (192.168.40.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Core-R1` (Gateway) | `192.168.40.1` | Static | Sub-interface |
| `CityA-TrafficLight-1` | `192.168.40.101` | DHCP | IoT controller |
| `CityA-TrafficLight-2` | `192.168.40.102` | DHCP | IoT controller |
| `CityA-ParkingSensor-1` | `192.168.40.103` | DHCP | IoT sensor |
| `CityA-ParkingSensor-2` | `192.168.40.104` | DHCP | IoT sensor |
| `CityA-BusTracker-1` | `192.168.40.105` | DHCP | IoT GPS |

#### **VLAN 50: Public WiFi (192.168.50.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Core-R1` (Gateway) | `192.168.50.1` | Static | Sub-interface |
| `CityA-WiFi-Pub-AP1` | `192.168.50.50` | Static | Public hotspot |
| `CityA-Public-Phone-1` | `192.168.50.101` | DHCP | Guest device |
| `CityA-Public-Tablet-1` | `192.168.50.102` | DHCP | Guest device |

#### **VLAN 60: Emergency Services (192.168.60.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Gov-R1` (Gateway) | `192.168.60.1` | Static | Sub-interface |
| `CityA-Police-PC-1` | `192.168.60.101` | DHCP | Police HQ |
| `CityA-Fire-PC-1` | `192.168.60.102` | DHCP | Fire station |
| `CityA-Gov-Camera-1` | `192.168.60.111` | DHCP | Security camera |
| `CityA-Gov-Camera-2` | `192.168.60.112` | DHCP | Security camera |
| `CityA-Fire-Sensor-1` | `192.168.60.113` | DHCP | Fire alarm |

#### **VLAN 70: Utilities (192.168.70.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Core-R1` (Gateway) | `192.168.70.1` | Static | Sub-interface |
| `CityA-SmartGrid-1` | `192.168.70.101` | DHCP | Power sensor |
| `CityA-SmartGrid-2` | `192.168.70.102` | DHCP | Power sensor |
| `CityA-WaterMonitor-1` | `192.168.70.103` | DHCP | Water quality |
| `CityA-WaterMonitor-2` | `192.168.70.104` | DHCP | Water quality |

#### **VLAN 99: Management/Servers (192.168.99.0/24)**

| Device | IPv4 Address | Assignment | Notes |
|--------|--------------|------------|-------|
| `CityA-Core-R1` (Gateway) | `192.168.99.1` | Static | Sub-interface |
| `CityA-DNS-Server` | `192.168.99.10` | Static | DNS primary |
| `CityA-DHCP-Server` | `192.168.99.20` | Static | DHCP service |
| `CityA-Web-Server` | `192.168.99.30` | Static | HTTP/HTTPS |
| `CityA-Email-Server` | `192.168.99.40` | Static | SMTP/POP3 |

---

### **CITY A - Router Point-to-Point Links (IPv4)**

| Link | Router A | Interface | IP Address | Router B | Interface | IP Address | Subnet |
|------|----------|-----------|------------|----------|-----------|------------|--------|
| Core ↔ Border | `CityA-Core-R1` | `Gig1/1` | `10.0.0.1/30` | `CityA-Border-R1` | `Gig0/0` | `10.0.0.2/30` | `10.0.0.0/30` |
| Core ↔ Gov | `CityA-Core-R1` | `Gig0/2` | `10.0.1.1/30` | `CityA-Gov-R1` | `Gig0/0` | `10.0.1.2/30` | `10.0.1.0/30` |
| Core ↔ Res | `CityA-Core-R1` | `Gig0/3` | `10.0.2.1/30` | `CityA-Res-R1` | `Gig0/0` | `10.0.2.2/30` | `10.0.2.0/30` |
| Core ↔ Com | `CityA-Core-R1` | `Gig1/0` | `10.0.3.1/30` | `CityA-Com-R1` | `Gig0/0` | `10.0.3.2/30` | `10.0.3.0/30` |

**Why /30 subnets?** - Point-to-point links only need 2 usable IPs (efficient)

---

### **CITY A - WAN Connection (IPv4)**

| Link | Device | Interface | IP Address | Subnet | Notes |
|------|--------|-----------|------------|--------|-------|
| CityA → ISP | `CityA-Border-R1` | `Serial0/0/0` | `203.0.113.1/30` | `203.0.113.0/30` | Public IP (WAN) |
| ISP → CityA | `ISP-Border-R1` | `Serial0/0/0` | `203.0.113.2/30` | `203.0.113.0/30` | ISP side |

**NAT Configuration:** `CityA-Border-R1` will translate 192.168.0.0/16 → 203.0.113.1

---

## 🏙️ CITY A - IPv6 ADDRESSING

### **Prefix Allocation: 2001:db8:a::/48**

| VLAN | IPv6 Subnet | Gateway | Notes |
|------|-------------|---------|-------|
| **10** | `2001:db8:a:10::/64` | `::1` | Government |
| **20** | `2001:db8:a:20::/64` | `::1` | Residential |
| **30** | `2001:db8:a:30::/64` | `::1` | Commercial |
| **40** | `2001:db8:a:40::/64` | `::1` | Transportation |
| **50** | `2001:db8:a:50::/64` | `::1` | Public WiFi |
| **60** | `2001:db8:a:60::/64` | `::1` | Emergency |
| **70** | `2001:db8:a:70::/64` | `::1` | Utilities |
| **99** | `2001:db8:a:99::/64` | `::1` | Management |

**IPv6 Addressing Logic:**
- `2001:db8:a` = City A prefix (documentation range)
- Third hex = VLAN number (matches IPv4)
- `::1` = Gateway (router interface)
- `::10, ::20, ::30` = Servers (static)
- `::1001+` = DHCP range (SLAAC or DHCPv6)

---

### **CITY A - IPv6 Device Addresses (Examples)**

| Device | IPv6 Address | Assignment |
|--------|--------------|------------|
| `CityA-Core-R1` VLAN 10 GW | `2001:db8:a:10::1/64` | Static |
| `CityA-DNS-Server` | `2001:db8:a:99::10/64` | Static |
| `CityA-DHCP-Server` | `2001:db8:a:99::20/64` | Static |
| `CityA-Web-Server` | `2001:db8:a:99::30/64` | Static |
| `CityA-Email-Server` | `2001:db8:a:99::40/64` | Static |
| `CityA-Gov-PC-1` | `2001:db8:a:10::1001/64` | SLAAC |
| `CityA-TrafficLight-1` | `2001:db8:a:40::1001/64` | SLAAC |

**IPv6 Assignment Methods:**
- **Routers/Servers:** Manual static configuration
- **End devices/IoT:** SLAAC (Stateless Address Autoconfiguration)
- **Option:** Use DHCPv6 for more control

---

### **CITY A - IPv6 Router Links**

| Link | Router A | IPv6 Address | Router B | IPv6 Address |
|------|----------|--------------|----------|--------------|
| Core ↔ Border | `CityA-Core-R1` | `2001:db8:a:ff01::1/127` | `CityA-Border-R1` | `2001:db8:a:ff01::2/127` |
| Core ↔ Gov | `CityA-Core-R1` | `2001:db8:a:ff02::1/127` | `CityA-Gov-R1` | `2001:db8:a:ff02::2/127` |
| Core ↔ Res | `CityA-Core-R1` | `2001:db8:a:ff03::1/127` | `CityA-Res-R1` | `2001:db8:a:ff03::2/127` |
| Core ↔ Com | `CityA-Core-R1` | `2001:db8:a:ff04::1/127` | `CityA-Com-R1` | `2001:db8:a:ff04::2/127` |

**Why /127?** - RFC 6164 recommends /127 for point-to-point IPv6 links (2 addresses, no waste)

---

## 🏙️ CITY B - ADDRESSING (Mirror of City A)

### **IPv4: 192.168.0.0/16** (SAME private range as City A)

**How is this possible?**
- NAT at each city's border router isolates private networks
- Public-facing: City A = `203.0.113.0/24`, City B = `203.0.114.0/24`

| VLAN | City B Subnet | Gateway | Notes |
|------|---------------|---------|-------|
| **10** | `192.168.10.0/24` | `.1` | Government (same as CityA internally) |
| **20** | `192.168.20.0/24` | `.1` | Residential |
| **30** | `192.168.30.0/24` | `.1` | Commercial |
| **40** | `192.168.40.0/24` | `.1` | Transportation |
| **50** | `192.168.50.0/24` | `.1` | Public WiFi |
| **60** | `192.168.60.0/24` | `.1` | Emergency |
| **70** | `192.168.70.0/24` | `.1` | Utilities |
| **99** | `192.168.99.0/24` | `.1` | Management |

**Device IPs:** Same pattern as City A (e.g., `CityB-DNS-Server` = `192.168.99.10`)

---

### **IPv6: 2001:db8:b::/48** (Different prefix)

| VLAN | City B IPv6 Subnet | Gateway |
|------|-------------------|---------|
| **10** | `2001:db8:b:10::/64` | `::1` |
| **20** | `2001:db8:b:20::/64` | `::1` |
| **30** | `2001:db8:b:30::/64` | `::1` |
| **40** | `2001:db8:b:40::/64` | `::1` |
| **50** | `2001:db8:b:50::/64` | `::1` |
| **60** | `2001:db8:b:60::/64` | `::1` |
| **70** | `2001:db8:b:70::/64` | `::1` |
| **99** | `2001:db8:b:99::/64` | `::1` |

**Note:** `2001:db8:b` prefix differentiates City B from City A

---

### **CITY B - WAN Connection**

| Link | Device | Interface | IP Address | Subnet |
|------|--------|-----------|------------|--------|
| CityB → ISP | `CityB-Border-R1` | `Serial0/0/0` | `203.0.114.1/30` | `203.0.114.0/30` |
| ISP → CityB | `ISP-Border-R2` | `Serial0/0/0` | `203.0.114.2/30` | `203.0.114.0/30` |

---

## 🌐 ISP / INTERNET BACKBONE ADDRESSING

### **ISP Backbone (IPv4)**

| Device | Interface | IPv4 Address | Subnet | Notes |
|--------|-----------|--------------|--------|-------|
| `ISP-Border-R1` | `Gig0/1` | `198.51.100.1/30` | `198.51.100.0/30` | Link to ISP-Core-R1 |
| `ISP-Core-R1` | `Gig0/0` | `198.51.100.2/30` | `198.51.100.0/30` | Receives from Border-R1 |
| `ISP-Border-R2` | `Gig0/1` | `198.51.100.5/30` | `198.51.100.4/30` | Link to ISP-Core-R1 |
| `ISP-Core-R1` | `Gig0/1` | `198.51.100.6/30` | `198.51.100.4/30` | Receives from Border-R2 |
| `ISP-Core-R1` | `Gig0/2` | `198.51.100.9/30` | `198.51.100.8/30` | Link to ISP-Core-R2 |
| `ISP-Core-R2` | `Gig0/0` | `198.51.100.10/30` | `198.51.100.8/30` | Redundant core |

### **Internet Servers (IPv4)**

| Server | IPv4 Address | Subnet | DNS Name |
|--------|--------------|--------|----------|
| `Internet-DNS-Root` | `8.8.8.8/24` | `8.8.8.0/24` | dns.google (simulation) |
| `Internet-Web-Server` | `8.8.8.10/24` | `8.8.8.0/24` | www.example.com |

---

### **ISP Backbone (IPv6)**

| Device | Interface | IPv6 Address | Subnet |
|--------|-----------|--------------|--------|
| `ISP-Border-R1` | `Gig0/1` | `2001:db8:ff:1::1/127` | Link to Core-R1 |
| `ISP-Core-R1` | `Gig0/0` | `2001:db8:ff:1::2/127` | Link to Border-R1 |
| `ISP-Border-R2` | `Gig0/1` | `2001:db8:ff:2::1/127` | Link to Core-R1 |
| `ISP-Core-R1` | `Gig0/1` | `2001:db8:ff:2::2/127` | Link to Border-R2 |
| `ISP-Core-R1` | `Gig0/2` | `2001:db8:ff:3::1/127` | Link to Core-R2 |
| `ISP-Core-R2` | `Gig0/0` | `2001:db8:ff:3::2/127` | Link to Core-R1 |

---

## 📊 ADDRESSING SUMMARY TABLE

### **Complete Network Ranges**

| Network | IPv4 Range | IPv6 Range | Devices | Purpose |
|---------|------------|------------|---------|---------|
| **City A Internal** | `192.168.0.0/16` | `2001:db8:a::/48` | 48 | Private network |
| **City A Public** | `203.0.113.0/24` | `2001:470:a::/48` | 254 | NAT pool |
| **City B Internal** | `192.168.0.0/16` | `2001:db8:b::/48` | 48 | Private network |
| **City B Public** | `203.0.114.0/24` | `2001:470:b::/48` | 254 | NAT pool |
| **ISP Backbone** | `198.51.100.0/24` | `2001:db8:ff::/48` | 6 | ISP routing |
| **Internet** | `8.8.8.0/24` | `2001:4860::/32` | 2 | Public internet |

---

## 🔢 SUBNETTING CALCULATIONS

### **VLAN 10 Example (Government):**

**IPv4:**
```
Network:    192.168.10.0
Mask:       255.255.255.0 (/24)
Wildcard:   0.0.0.255
First IP:   192.168.10.1 (Gateway)
Last IP:    192.168.10.254
Broadcast:  192.168.10.255
Usable:     253 hosts (excluding gateway)
DHCP Pool:  192.168.10.100 - .200 (101 addresses)
Static:     192.168.10.1 - .99 (99 addresses)
```

**IPv6:**
```
Network:    2001:db8:a:10::/64
Prefix:     64 bits
Host bits:  64 bits = 18,446,744,073,709,551,616 addresses
Gateway:    2001:db8:a:10::1
SLAAC:      Devices auto-configure using prefix
```

---

## 📝 NEXT STEPS

✅ **IP addressing scheme designed**

➡️ **Next:** Open `02_ROUTER_SETUP.md` to configure all routers with these IPs!

---

## 🎓 TECHNOLOGIES DEMONSTRATED

| Technology | Where Used | Count |
|------------|------------|-------|
| **IPv4 Subnetting** | All VLANs (/24), P2P links (/30) | 20+ subnets |
| **IPv6 Addressing** | All VLANs (/64), P2P links (/127) | 20+ subnets |
| **NAT (IPv4)** | Border routers | 2 routers |
| **VLSM** | Different mask sizes (/16, /24, /30) | Throughout |
| **Public/Private** | RFC1918 private, public internet ranges | Both |
| **Hierarchical** | Easy-to-remember structure | All addresses |

---

**Ready to apply these IPs? Open PART2_CONFIGURATION/02_ROUTER_SETUP.md!** 🚀
