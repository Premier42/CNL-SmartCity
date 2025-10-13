# PART 2: CONFIGURATION
## 02 - ROUTER SETUP (OSPF, NAT, Sub-Interfaces)

**Complete step-by-step router configuration for all 14 routers**

---

## 📋 ROUTER CONFIGURATION ORDER

**Follow this sequence:**
1. ✅ City A Border Router (WAN + NAT)
2. ✅ City A Core Router (OSPF hub + inter-VLAN)
3. ✅ City A Zone Routers (OSPF + VLANs)
4. ✅ ISP Routers (backbone routing)
5. ✅ City B Routers (mirror of City A)

---

## ⚠️ IMPORTANT NOTES BEFORE STARTING

### **⚙️ Router Model Standard:**
- **ALL routers:** Cisco 2911 (standardized for this project)
- **Interface naming:** `GigabitEthernet0/0`, `GigabitEthernet0/1`, `Serial0/0/0`
- **If using 1941 instead:** Interface names are same (Gig0/0, Serial0/0/0)

**🔍 Always verify YOUR router's interfaces:**
```cisco
Router> enable
Router# show ip interface brief
```

**See `../COMPATIBILITY_GUIDE.md` for router substitutions if 2911 unavailable**

---

### **⚠️ Sub-Interface Parent MUST Be Up:**
When configuring sub-interfaces (e.g., `Gig0/0.10`):
1. **Parent interface** (e.g., `Gig0/0`) must have `no shutdown`
2. Parent does NOT need an IP address
3. Sub-interfaces configure their own IPs

**Example:**
```cisco
interface GigabitEthernet0/0
 no shutdown  ← CRITICAL!
 exit
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 exit
```

---

### **Serial Interface DCE/DTE:**
- **DCE side** (ISP) provides clock rate
- **DTE side** (City) receives clock
- Only configure `clock rate` on DCE side
- Cable direction matters in PT!

---

### **Configuration Tips:**
1. Copy-paste ONE command at a time
2. Wait for confirmation before next command
3. If error: Check interface names with `show ip int brief`
4. Save frequently: `write memory`
5. **Parent interfaces need `no shutdown` BEFORE configuring sub-interfaces**

---

## 🏙️ CITY A - ROUTER CONFIGURATIONS

---

## 🔧 **ROUTER 1: CityA-Border-R1** (Border + NAT)

### **Purpose:**
- Connects City A to ISP
- Performs NAT (private → public)
- OSPF Area 10 (City A)

---

### **Step 1: Basic Configuration**

```cisco
enable
configure terminal
hostname CityA-Border-R1

! Enable routing
ip routing
ipv6 unicast-routing

! Set console password (optional)
line console 0
 password cisco
 login
 exit

! Set enable password
enable secret class

! Save config reminder
service password-encryption
```

---

### **Step 2: Configure Interfaces**

#### **Interface to ISP (WAN - Serial)**

```cisco
interface Serial0/0/0
 description WAN Link to ISP-Border-R1
 ip address 203.0.113.1 255.255.255.252
 ipv6 address 2001:db8:a:ffff::1/127
 no shutdown
 exit
```

**Note:** If your router shows `Serial0/1/0` instead, use that

---

#### **Interface to Core Router (Internal)**

```cisco
interface GigabitEthernet0/0
 description Link to CityA-Core-R1
 ip address 10.0.0.2 255.255.255.252
 ipv6 address 2001:db8:a:ff01::2/127
 no shutdown
 exit
```

---

### **Step 3: Configure OSPF**

```cisco
router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.0.0.3 area 10
 network 203.0.113.0 0.0.0.3 area 0
 passive-interface Serial0/0/0
 exit
```

**Explanation:**
- `router-id 1.1.1.1` - Unique identifier
- Area 10 = City A internal
- Area 0 = ISP backbone
- Passive on Serial = Don't send OSPF to ISP

---

### **Step 4: Configure NAT**

```cisco
! Define inside/outside interfaces
interface GigabitEthernet0/0
 ip nat inside
 exit

interface Serial0/0/0
 ip nat outside
 exit

! Access list for NAT (allow all private IPs)
access-list 1 remark City-A-Private-Network
access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 10.0.0.0 0.0.255.255

! Enable NAT overload (PAT) using interface
ip nat inside source list 1 interface Serial0/0/0 overload
```

**⚠️ IMPORTANT - Why Interface-Based NAT:**
- Pool-based NAT (`ip nat pool ...`) can be unreliable in Packet Tracer
- Interface-based NAT (`interface Serial0/0/0`) works consistently
- Uses the interface's public IP (203.0.113.1) for all translations
- `overload` = Multiple devices share one public IP (PAT)

**Explanation:**
- `ip nat inside` = Private network side
- `ip nat outside` = Public internet side
- ACL 1 = Defines which private IPs to translate
- Interface-based = More reliable in PT than pool-based

---

### **Step 5: Configure IPv6 OSPFv3 (Optional)**

**⚠️ SKIP THIS STEP IF:**
- Using Packet Tracer 8.0 or 8.1 (IPv6 support limited/buggy)
- Want to keep project simpler
- **Impact:** None - all technologies demonstrated with IPv4

**For PT 8.2+ only:**
```cisco
ipv6 router ospf 1
 router-id 1.1.1.1
 exit

interface GigabitEthernet0/0
 ipv6 ospf 1 area 10
 exit

interface Serial0/0/0
 ipv6 ospf 1 area 0
 exit
```

**Note:** If skipping IPv6, also skip all `ipv6 address` and `ipv6 route` commands

---

### **Step 6: Default Route to ISP**

```cisco
! IPv4 default route
ip route 0.0.0.0 0.0.0.0 203.0.113.2

! IPv6 default route
ipv6 route ::/0 2001:db8:a:ffff::2

! Advertise default route in OSPF
router ospf 1
 default-information originate
 exit
```

---

### **Step 7: Save Configuration**

```cisco
end
write memory
```

**Verification:**
```cisco
show ip interface brief
show ip ospf neighbor
show ip nat translations
```

---

## ✅ **CHECKPOINT:** Border Router Complete
Expected output:
- Serial0/0/0: Up/Up with IP 203.0.113.1
- Gig0/0: Up/Up with IP 10.0.0.2
- OSPF neighbor with Core-R1
- NAT configured

---

## 🔧 **ROUTER 2: CityA-Core-R1** (Core + Inter-VLAN)

### **Purpose:**
- Central routing hub
- Inter-VLAN routing (8 VLANs)
- OSPF hub for City A
- QoS policy

---

### **Step 1: Basic Configuration**

```cisco
enable
configure terminal
hostname CityA-Core-R1

ip routing
ipv6 unicast-routing

enable secret class
service password-encryption
```

---

### **Step 2: Physical Interfaces**

#### **Interface to Border Router**

```cisco
interface GigabitEthernet1/1
 description Link to CityA-Border-R1
 ip address 10.0.0.1 255.255.255.252
 ipv6 address 2001:db8:a:ff01::1/127
 no shutdown
 exit
```

---

#### **Interface to Government Router**

```cisco
interface GigabitEthernet0/2
 description Link to CityA-Gov-R1
 ip address 10.0.1.1 255.255.255.252
 ipv6 address 2001:db8:a:ff02::1/127
 no shutdown
 exit
```

---

#### **Interface to Residential Router**

```cisco
interface GigabitEthernet0/3
 description Link to CityA-Res-R1
 ip address 10.0.2.1 255.255.255.252
 ipv6 address 2001:db8:a:ff03::1/127
 no shutdown
 exit
```

---

#### **Interface to Commercial Router**

```cisco
interface GigabitEthernet1/0
 description Link to CityA-Com-R1
 ip address 10.0.3.1 255.255.255.252
 ipv6 address 2001:db8:a:ff04::1/127
 no shutdown
 exit
```

---

#### **Interface to Core Switches (Trunk)**

```cisco
interface GigabitEthernet0/0
 description Trunk to CityA-Core-SW1
 no ip address
 no shutdown
 exit

interface GigabitEthernet0/1
 description Trunk to CityA-Core-SW2
 no ip address
 no shutdown
 exit
```

**Note:** Main interfaces have NO IP because sub-interfaces will handle VLANs

---

### **Step 3: Sub-Interfaces for VLANs (Router-on-a-Stick)**

#### **VLAN 40: Transportation (on Gig0/0)**

```cisco
interface GigabitEthernet0/0.40
 description VLAN 40 - Transportation
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:a:40::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

**Explanation:**
- `encapsulation dot1Q 40` - Tag with VLAN 40
- `ip helper-address` - Forward DHCP to server

---

#### **VLAN 50: Public WiFi (on Gig0/0)**

```cisco
interface GigabitEthernet0/0.50
 description VLAN 50 - Public WiFi
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:a:50::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

---

#### **VLAN 70: Utilities (on Gig0/1)**

```cisco
interface GigabitEthernet0/1.70
 description VLAN 70 - Utilities
 encapsulation dot1Q 70
 ip address 192.168.70.1 255.255.255.0
 ipv6 address 2001:db8:a:70::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

---

#### **VLAN 99: Management/Servers (on Gig0/1)**

```cisco
interface GigabitEthernet0/1.99
 description VLAN 99 - Management
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0
 ipv6 address 2001:db8:a:99::1/64
 no shutdown
 exit
```

**Note:** VLAN 99 has NO ip helper (servers have static IPs)

---

### **Step 4: Configure OSPF**

```cisco
router ospf 1
 router-id 1.1.1.2
 network 10.0.0.0 0.0.0.3 area 10
 network 10.0.1.0 0.0.0.3 area 10
 network 10.0.2.0 0.0.0.3 area 10
 network 10.0.3.0 0.0.0.3 area 10
 network 192.168.40.0 0.0.0.255 area 10
 network 192.168.50.0 0.0.0.255 area 10
 network 192.168.70.0 0.0.0.255 area 10
 network 192.168.99.0 0.0.0.255 area 10
 passive-interface GigabitEthernet0/0.40
 passive-interface GigabitEthernet0/0.50
 passive-interface GigabitEthernet0/1.70
 passive-interface GigabitEthernet0/1.99
 exit
```

**Explanation:**
- All links in Area 10 (City A)
- Passive on VLAN interfaces (don't send OSPF to end devices)

---

### **Step 5: Configure ACLs for Security**

#### **ACL 110: Public WiFi Security**

```cisco
access-list 110 remark Public-WiFi-Security
access-list 110 permit tcp 192.168.50.0 0.0.0.255 any eq 80
access-list 110 permit tcp 192.168.50.0 0.0.0.255 any eq 443
access-list 110 permit udp 192.168.50.0 0.0.0.255 host 192.168.99.10 eq 53
access-list 110 deny ip 192.168.50.0 0.0.0.255 192.168.0.0 0.0.255.255 log
access-list 110 permit ip any any

! Apply to VLAN 50 interface
interface GigabitEthernet0/0.50
 ip access-group 110 in
 exit
```

**Explanation:**
- Allow: HTTP (80), HTTPS (443), DNS to server
- Deny: Access to all internal networks (192.168.x.x)
- Permit: Other traffic (internet access)

---

### **Step 6: Configure QoS**

```cisco
! Define traffic classes
class-map match-any EMERGENCY-TRAFFIC
 match access-group 120
 exit

class-map match-any IOT-TRAFFIC
 match access-group 121
 exit

! QoS Policy
policy-map CITYA-QOS
 class EMERGENCY-TRAFFIC
  priority percent 40
 class IOT-TRAFFIC
  bandwidth percent 30
 class class-default
  fair-queue
 exit

! Apply to outbound interface
interface GigabitEthernet1/1
 service-policy output CITYA-QOS
 exit

! Define emergency traffic (VLAN 60)
access-list 120 remark Emergency-Services
access-list 120 permit ip 192.168.60.0 0.0.0.255 any

! Define IoT traffic (VLANs 40, 70)
access-list 121 remark IoT-Devices
access-list 121 permit ip 192.168.40.0 0.0.0.255 any
access-list 121 permit ip 192.168.70.0 0.0.0.255 any
```

**Explanation:**
- Emergency (VLAN 60): 40% priority
- IoT (VLANs 40, 70): 30% bandwidth guarantee
- Others: Fair queuing

---

### **Step 7: Save Configuration**

```cisco
end
write memory
```

**Verification:**
```cisco
show ip interface brief
show ip ospf neighbor
show ip route ospf
show policy-map interface GigabitEthernet1/1
show access-lists
```

---

## ✅ **CHECKPOINT:** Core Router Complete
Expected:
- 8 interfaces UP (4 physical + 4 sub-interfaces)
- OSPF neighbors: Border-R1, Gov-R1, Res-R1, Com-R1
- QoS policy applied
- ACL 110 active on VLAN 50

---

## 🔧 **ROUTER 3: CityA-Gov-R1** (Government Zone)

### **Purpose:**
- Government district router
- VLANs 10 (Government) and 60 (Emergency)
- OSPF to core

---

### **Step 1: Basic Configuration**

```cisco
enable
configure terminal
hostname CityA-Gov-R1

ip routing
ipv6 unicast-routing

enable secret class
```

---

### **Step 2: Interface to Core**

```cisco
interface GigabitEthernet0/0
 description Link to CityA-Core-R1
 ip address 10.0.1.2 255.255.255.252
 ipv6 address 2001:db8:a:ff02::2/127
 no shutdown
 exit
```

---

### **Step 3: Interface to Government Switch (Trunk)**

```cisco
interface GigabitEthernet0/1
 description Trunk to CityA-Gov-SW1
 no ip address
 no shutdown
 exit
```

---

### **Step 4: Sub-Interfaces for VLANs**

#### **VLAN 10: Government**

```cisco
interface GigabitEthernet0/1.10
 description VLAN 10 - Government
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:a:10::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

---

#### **VLAN 60: Emergency Services**

```cisco
interface GigabitEthernet0/1.60
 description VLAN 60 - Emergency
 encapsulation dot1Q 60
 ip address 192.168.60.1 255.255.255.0
 ipv6 address 2001:db8:a:60::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

---

### **Step 5: Configure OSPF**

```cisco
router ospf 1
 router-id 1.1.1.3
 network 10.0.1.0 0.0.0.3 area 10
 network 192.168.10.0 0.0.0.255 area 10
 network 192.168.60.0 0.0.0.255 area 10
 passive-interface GigabitEthernet0/1.10
 passive-interface GigabitEthernet0/1.60
 exit
```

---

### **Step 6: Save**

```cisco
end
write memory
```

**Verification:**
```cisco
show ip interface brief
show ip ospf neighbor
```

---

## ✅ **CHECKPOINT:** Government Router Complete

---

## 🔧 **ROUTER 4: CityA-Res-R1** (Residential Zone)

### **Purpose:**
- Residential zone router
- VLAN 20 (Residential)
- Connects to 2 access switches

---

### **Step 1: Basic Configuration**

```cisco
enable
configure terminal
hostname CityA-Res-R1

ip routing
ipv6 unicast-routing

enable secret class
```

---

### **Step 2: Interface to Core**

```cisco
interface GigabitEthernet0/0
 description Link to CityA-Core-R1
 ip address 10.0.2.2 255.255.255.252
 ipv6 address 2001:db8:a:ff03::2/127
 no shutdown
 exit
```

---

### **Step 3: Interfaces to Residential Switches**

#### **To Res-SW1**

```cisco
interface GigabitEthernet0/1
 description Trunk to CityA-Res-SW1
 no ip address
 no shutdown
 exit

interface GigabitEthernet0/1.20
 description VLAN 20 - Residential
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:a:20::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

---

#### **To Res-SW2**

```cisco
interface GigabitEthernet1/0
 description Trunk to CityA-Res-SW2
 no ip address
 no shutdown
 exit

interface GigabitEthernet1/0.20
 description VLAN 20 - Residential (SW2)
 encapsulation dot1Q 20
 ip address 192.168.20.2 255.255.255.0
 ipv6 address 2001:db8:a:20::2/64
 ip helper-address 192.168.99.20
 no shutdown
 exit
```

**Note:** Different IP (.1 vs .2) because both in same VLAN 20

---

### **Step 4: Configure OSPF**

```cisco
router ospf 1
 router-id 1.1.1.4
 network 10.0.2.0 0.0.0.3 area 10
 network 192.168.20.0 0.0.0.255 area 10
 passive-interface GigabitEthernet0/1.20
 passive-interface GigabitEthernet1/0.20
 exit
```

---

### **Step 5: Save**

```cisco
end
write memory
```

---

## ✅ **CHECKPOINT:** Residential Router Complete

---

## 🔧 **ROUTER 5: CityA-Com-R1** (Commercial Zone)

### **Purpose:**
- Commercial zone router
- VLAN 30 (Commercial)

---

### **Quick Configuration (Similar Pattern)**

```cisco
enable
configure terminal
hostname CityA-Com-R1

ip routing
ipv6 unicast-routing

! Interface to Core
interface GigabitEthernet0/0
 description Link to CityA-Core-R1
 ip address 10.0.3.2 255.255.255.252
 ipv6 address 2001:db8:a:ff04::2/127
 no shutdown
 exit

! Interface to Commercial Switch
interface GigabitEthernet0/1
 no ip address
 no shutdown
 exit

interface GigabitEthernet0/1.30
 description VLAN 30 - Commercial
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:a:30::1/64
 ip helper-address 192.168.99.20
 no shutdown
 exit

! OSPF
router ospf 1
 router-id 1.1.1.5
 network 10.0.3.0 0.0.0.3 area 10
 network 192.168.30.0 0.0.0.255 area 10
 passive-interface GigabitEthernet0/1.30
 exit

end
write memory
```

---

## ✅ **CHECKPOINT:** All City A Routers Complete!

**Summary:**
- CityA-Border-R1: NAT, WAN connection ✅
- CityA-Core-R1: Inter-VLAN, OSPF hub, QoS, ACLs ✅
- CityA-Gov-R1: VLANs 10, 60 ✅
- CityA-Res-R1: VLAN 20 ✅
- CityA-Com-R1: VLAN 30 ✅

---

## 🌐 ISP ROUTERS CONFIGURATION

---

## 🔧 **ISP-Border-R1** (ISP Edge for City A)

```cisco
enable
configure terminal
hostname ISP-Border-R1

ip routing
ipv6 unicast-routing

! Serial to City A (DCE side - provides clock)
interface Serial0/0/0
 description WAN to CityA-Border-R1
 ip address 203.0.113.2 255.255.255.252
 ipv6 address 2001:db8:a:ffff::2/127
 clock rate 128000
 no shutdown
 exit

! Interface to ISP Core
interface GigabitEthernet0/1
 description Link to ISP-Core-R1
 ip address 198.51.100.1 255.255.255.252
 ipv6 address 2001:db8:ff:1::1/127
 no shutdown
 exit

! OSPF
router ospf 1
 router-id 2.2.2.1
 network 203.0.113.0 0.0.0.3 area 0
 network 198.51.100.0 0.0.0.3 area 0
 exit

end
write memory
```

---

## 🔧 **ISP-Border-R2** (ISP Edge for City B)

```cisco
enable
configure terminal
hostname ISP-Border-R2

ip routing
ipv6 unicast-routing

! Serial to City B (DCE side)
interface Serial0/0/0
 description WAN to CityB-Border-R1
 ip address 203.0.114.2 255.255.255.252
 ipv6 address 2001:db8:b:ffff::2/127
 clock rate 128000
 no shutdown
 exit

! Interface to ISP Core
interface GigabitEthernet0/1
 description Link to ISP-Core-R1
 ip address 198.51.100.5 255.255.255.252
 ipv6 address 2001:db8:ff:2::1/127
 no shutdown
 exit

! OSPF
router ospf 1
 router-id 2.2.2.2
 network 203.0.114.0 0.0.0.3 area 0
 network 198.51.100.4 0.0.0.3 area 0
 exit

end
write memory
```

---

## 🔧 **ISP-Core-R1** (ISP Backbone)

```cisco
enable
configure terminal
hostname ISP-Core-R1

ip routing
ipv6 unicast-routing

! Interface to ISP-Border-R1
interface GigabitEthernet0/0
 description Link to ISP-Border-R1
 ip address 198.51.100.2 255.255.255.252
 ipv6 address 2001:db8:ff:1::2/127
 no shutdown
 exit

! Interface to ISP-Border-R2
interface GigabitEthernet0/1
 description Link to ISP-Border-R2
 ip address 198.51.100.6 255.255.255.252
 ipv6 address 2001:db8:ff:2::2/127
 no shutdown
 exit

! Interface to ISP-Core-R2
interface GigabitEthernet0/2
 description Link to ISP-Core-R2
 ip address 198.51.100.9 255.255.255.252
 ipv6 address 2001:db8:ff:3::1/127
 no shutdown
 exit

! OSPF
router ospf 1
 router-id 2.2.2.3
 network 198.51.100.0 0.0.0.3 area 0
 network 198.51.100.4 0.0.0.3 area 0
 network 198.51.100.8 0.0.0.3 area 0
 exit

end
write memory
```

---

## 🔧 **ISP-Core-R2** (ISP Backbone Redundant)

```cisco
enable
configure terminal
hostname ISP-Core-R2

ip routing
ipv6 unicast-routing

! Interface to ISP-Core-R1
interface GigabitEthernet0/0
 description Link to ISP-Core-R1
 ip address 198.51.100.10 255.255.255.252
 ipv6 address 2001:db8:ff:3::2/127
 no shutdown
 exit

! Interface to Internet DNS
interface GigabitEthernet0/1
 description Link to Internet-DNS-Root
 ip address 8.8.8.1 255.255.255.0
 no shutdown
 exit

! OSPF
router ospf 1
 router-id 2.2.2.4
 network 198.51.100.8 0.0.0.3 area 0
 network 8.8.8.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/1
 exit

end
write memory
```

---

## 🏙️ CITY B - ROUTER CONFIGURATIONS

**EXACT COPY of City A routers with these changes:**
- Hostname: `CityA-XXX` → `CityB-XXX`
- Router IDs: `1.1.1.X` → `1.1.2.X`
- OSPF Area: Keep `area 10` (or use `area 20` if professor wants separate areas)
- IPv4: Same IPs (192.168.x.x) - NAT isolates
- IPv6: `2001:db8:a` → `2001:db8:b`
- WAN: 203.0.114.0/30 (different public range)

---

### **Example: CityB-Border-R1 (abbreviated)**

```cisco
hostname CityB-Border-R1

interface Serial0/0/0
 ip address 203.0.114.1 255.255.255.252
 ipv6 address 2001:db8:b:ffff::1/127
 exit

interface GigabitEthernet0/0
 ip address 10.0.0.2 255.255.255.252
 ipv6 address 2001:db8:b:ff01::2/127
 exit

router ospf 1
 router-id 1.1.2.1
 network 10.0.0.0 0.0.0.3 area 10
 network 203.0.114.0 0.0.0.3 area 0
 exit

! NAT (interface-based, more reliable than pool)
interface GigabitEthernet0/0
 ip nat inside
 exit
interface Serial0/0/0
 ip nat outside
 exit
access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 10.0.0.0 0.0.255.255
ip nat inside source list 1 interface Serial0/0/0 overload

! Default route
ip route 0.0.0.0 0.0.0.0 203.0.114.2

end
write memory
```

**Repeat for all 5 City B routers following City A pattern**

---

## ✅ COMPLETE ROUTER CONFIGURATION CHECKLIST

### **City A:**
- [ ] CityA-Border-R1 (NAT, OSPF, default route)
- [ ] CityA-Core-R1 (OSPF hub, VLANs 40/50/70/99, ACLs, QoS)
- [ ] CityA-Gov-R1 (VLANs 10/60)
- [ ] CityA-Res-R1 (VLAN 20)
- [ ] CityA-Com-R1 (VLAN 30)

### **ISP:**
- [ ] ISP-Border-R1 (DCE, clock rate)
- [ ] ISP-Border-R2 (DCE, clock rate)
- [ ] ISP-Core-R1 (OSPF backbone)
- [ ] ISP-Core-R2 (OSPF backbone, internet servers)

### **City B:**
- [ ] All 5 routers (mirror City A)

**Total: 14 routers configured** ✅

---

## 🔍 VERIFICATION COMMANDS

Run on EACH router:

```cisco
! Check interfaces
show ip interface brief
show ipv6 interface brief

! Check OSPF
show ip ospf neighbor
show ip route ospf

! Check NAT (border routers only)
show ip nat translations
show ip nat statistics

! Check ACLs (core routers)
show access-lists
show ip access-lists

! Check QoS (core routers)
show policy-map interface GigabitEthernet1/1
```

---

## 🎯 EXPECTED RESULTS

### **CityA-Core-R1:**
- 4 OSPF neighbors: Border, Gov, Res, Com
- Routes to all 192.168.x.0/24 networks
- QoS policy active
- ACL 110 applied to VLAN 50

### **CityA-Border-R1:**
- 1 OSPF neighbor: Core-R1
- Default route to 203.0.113.2
- NAT translations active (after traffic flows)

### **ISP-Core-R1:**
- 3 OSPF neighbors: Border-R1, Border-R2, Core-R2
- Routes to 203.0.113.0/30 and 203.0.114.0/30

---

## 📝 NEXT STEPS

✅ **All routers configured**

➡️ **Next:** Open `03_SWITCH_SETUP.md` to configure VLANs and trunks!

---

## ⏱️ ESTIMATED TIME

- City A routers: 1.5 hours
- ISP routers: 30 minutes
- City B routers: 1 hour (copying pattern)
- **Total: ~3 hours**

---

**Router configuration complete! Ready for switches!** 🚀
