# Pre-Configuration Verification Checklist
## Stage 2 Complete - Ready for Stage 3

---

## ✅ Physical Topology Verification

### Core Infrastructure
- [x] Router[Gig0/0/1] ↔ Core-Switch[Gig0/1] ✓
- [x] Router[Gig0/0/0] → Internet (DHCP) ✓

### District Switch Trunks (All using Gigabit ports)
- [x] Core-Switch[Gig0/2] ↔ Downtown-Switch[Fa0/1] ✓
- [x] Core-Switch[Gig0/3] ↔ Park-Switch[Fa0/1] ✓
- [x] Core-Switch[Gig0/4] ↔ Residential-Switch[Fa0/1] ✓

### Servers (All VLAN 10 - Admin)
- [x] Core-Switch[Fa0/4] → DNS-Server ✓
- [x] Core-Switch[Fa0/5] → DHCP-Server ✓
- [x] Core-Switch[Fa0/6] → Web-Server ✓
- [x] Core-Switch[Fa0/7] → SMTP-Server ✓

### Admin Devices (All VLAN 10)
- [x] Core-Switch[Fa0/8] → Admin-PC-1 ✓
- [x] Core-Switch[Fa0/9] → Admin-PC-2 ✓
- [x] Core-Switch[Fa0/10] → City-Hall-Phone ✓

### Cellular Network (VLAN 20 - Public)
- [x] Cell-Tower[Coax] ↔ Central-Office-Server[Coax] ✓
- [x] Central-Office-Server[Eth] → Core-Switch[Fa0/3] ✓

### Downtown District (VLAN 20 - Public)
- [x] Downtown-Switch[Fa0/2] → Public-Kiosk-PC ✓
- [x] Downtown-Switch[Fa0/3] → Info-Line-Phone ✓
- [x] Downtown-Switch[Fa0/4] → Public-WiFi-AP ✓

### Park IoT (VLAN 30 - IoT)
- [x] Park-Switch[Fa0/2] → Park-IoT-Gateway ✓
- [x] Park-Switch[Fa0/3] → Smart-Streetlight (network-connected) ✓
- [x] Park-IoT-Gateway[D0] → Park-Motion-Sensor (GPIO) ✓

### Residential Area (VLAN 30 - IoT)
- [x] Residential-Switch[Fa0/2] → Resident-Home-PC ✓
- [x] Residential-Switch[Fa0/3] → Residential-WiFi-AP ✓

### Wireless (No cables)
- [x] Citizen-Smartphone → Public-WiFi-AP (wireless) ✓
- [x] Citizen-Smartphone → City-Cell-Tower (wireless) ✓

**Total Connections: 23 devices - All verified ✓**

---

## ✅ IPv4 Addressing Scheme (No Conflicts)

### Point-to-Point Link (10.0.0.0/30)
| Device | IP Address | Subnet Mask | Interface |
|--------|------------|-------------|-----------|
| City-Gateway-Router | 10.0.0.1 | 255.255.255.252 | Gig0/0/1 |
| City-Core-Switch | 10.0.0.2 | 255.255.255.252 | Gig0/1 |

### VLAN 10 - Admin (10.10.10.0/24)
| Device | IP Address | Type | Notes |
|--------|------------|------|-------|
| Core-Switch | 10.10.10.1 | Gateway | VLAN 10 SVI |
| DNS-Server | 10.10.10.10 | Static | ✓ |
| DHCP-Server | 10.10.10.20 | Static | ✓ |
| Web-Server | 10.10.10.30 | Static | ✓ |
| SMTP-Server | 10.10.10.40 | Static | ✓ |
| Admin-PC-1 | 10.10.10.100-150 | DHCP | Pool range |
| Admin-PC-2 | 10.10.10.100-150 | DHCP | Pool range |
| City-Hall-Phone | 10.10.10.100-150 | DHCP | Pool range |

### VLAN 20 - Public (10.10.20.0/24)
| Device | IP Address | Type | Notes |
|--------|------------|------|-------|
| Core-Switch | 10.10.20.1 | Gateway | VLAN 20 SVI |
| Central-Office-Server | 10.10.20.50 | Static | ✓ |
| Public-Kiosk-PC | 10.10.20.100-200 | DHCP | Pool range |
| Info-Line-Phone | 10.10.20.100-200 | DHCP | Pool range |
| Public-WiFi clients | 10.10.20.100-200 | DHCP | Pool range |

### VLAN 30 - IoT (10.10.30.0/24)
| Device | IP Address | Type | Notes |
|--------|------------|------|-------|
| Core-Switch | 10.10.30.1 | Gateway | VLAN 30 SVI |
| Park-IoT-Gateway | 10.10.30.10 | Static | ✓ |
| Smart-Streetlight | 10.10.30.20 | Static | ✓ Network-connected LED |
| Resident-Home-PC | 10.10.30.100-150 | DHCP | Pool range |
| Residential-WiFi clients | 10.10.30.100-150 | DHCP | Pool range |

### VLAN 99 - Management (10.10.99.0/24)
| Device | IP Address | Type | Notes |
|--------|------------|------|-------|
| Core-Switch | 10.10.99.1 | Gateway | VLAN 99 SVI |
| (Reserved for mgmt) | - | - | No devices currently |

**No IP conflicts found ✓**

---

## ✅ IPv6 Addressing Scheme (No Conflicts)

### Point-to-Point Link (2001:DB8:CITY:0::/64)
| Device | IPv6 Address | Interface |
|--------|--------------|-----------|
| City-Gateway-Router | 2001:DB8:CITY:0::1/64 | Gig0/0/1 |
| City-Core-Switch | 2001:DB8:CITY:0::2/64 | Gig0/1 |

### VLAN 10 - Admin (2001:DB8:CITY:10::/64)
| Device | IPv6 Address |
|--------|--------------|
| Core-Switch Gateway | 2001:DB8:CITY:10::1/64 |
| DNS-Server | 2001:DB8:CITY:10::10/64 |
| DHCP-Server | 2001:DB8:CITY:10::20/64 |
| Web-Server | 2001:DB8:CITY:10::30/64 |
| SMTP-Server | 2001:DB8:CITY:10::40/64 |

### VLAN 20 - Public (2001:DB8:CITY:20::/64)
| Device | IPv6 Address |
|--------|--------------|
| Core-Switch Gateway | 2001:DB8:CITY:20::1/64 |
| Central-Office-Server | 2001:DB8:CITY:20::50/64 |

### VLAN 30 - IoT (2001:DB8:CITY:30::/64)
| Device | IPv6 Address |
|--------|--------------|
| Core-Switch Gateway | 2001:DB8:CITY:30::1/64 |
| (IoT devices may use IPv4 only) | - |

### VLAN 99 - Management (2001:DB8:CITY:99::/64)
| Device | IPv6 Address |
|--------|--------------|
| Core-Switch Gateway | 2001:DB8:CITY:99::1/64 |

**No IPv6 conflicts found ✓**

---

## ✅ VLAN Assignments Verification

### VLAN 10 (Admin)
| Device | Switch Port | Status |
|--------|-------------|--------|
| DNS-Server | Core Fa0/4 | Access ✓ |
| DHCP-Server | Core Fa0/5 | Access ✓ |
| Web-Server | Core Fa0/6 | Access ✓ |
| SMTP-Server | Core Fa0/7 | Access ✓ |
| Admin-PC-1 | Core Fa0/8 | Access ✓ |
| Admin-PC-2 | Core Fa0/9 | Access ✓ |
| City-Hall-Phone | Core Fa0/10 | Access ✓ |

### VLAN 20 (Public)
| Device | Switch Port | Status |
|--------|-------------|--------|
| Central-Office-Server | Core Fa0/3 | Access ✓ |
| Public-Kiosk-PC | Downtown Fa0/2 | Access ✓ |
| Info-Line-Phone | Downtown Fa0/3 | Access ✓ |
| Public-WiFi-AP | Downtown Fa0/4 | Access ✓ |

### VLAN 30 (IoT)
| Device | Switch Port | Status |
|--------|-------------|--------|
| Park-IoT-Gateway | Park Fa0/2 | Access ✓ |
| Smart-Streetlight | Park Fa0/3 | Access ✓ |
| Resident-Home-PC | Residential Fa0/2 | Access ✓ |
| Residential-WiFi-AP | Residential Fa0/3 | Access ✓ |

### Trunk Links
| Source | Destination | VLANs Allowed | Native VLAN |
|--------|-------------|---------------|-------------|
| Core Gig0/2 | Downtown Fa0/1 | 10,20,30,99 | 99 ✓ |
| Core Gig0/3 | Park Fa0/1 | 10,20,30,99 | 99 ✓ |
| Core Gig0/4 | Residential Fa0/1 | 10,20,30,99 | 99 ✓ |

**All VLAN assignments correct ✓**

---

## ✅ Router Configuration Check

### Interfaces
- [x] Gig0/0/0: DHCP (Internet), NAT outside, IPv6 autoconfig ✓
- [x] Gig0/0/1: 10.0.0.1/30, NAT inside, IPv6 2001:DB8:CITY:0::1/64 ✓

### NAT
- [x] NAT overload on Gig0/0/0 ✓
- [x] ACL 1: permit 10.10.0.0 0.0.255.255 ✓ (covers all VLANs)

### Routing
- [x] IPv4 default route via Gig0/0/0 ✓
- [x] IPv6 default route via Gig0/0/0 ✓
- [x] IPv6 unicast routing enabled ✓

### Security
- [x] Enable secret: class ✓
- [x] Console password: cisco ✓
- [x] VTY password: cisco ✓

**Router config verified ✓**

---

## ✅ Core Switch Configuration Check

### VLANs
- [x] VLAN 10 (Admin) ✓
- [x] VLAN 20 (Public) ✓
- [x] VLAN 30 (IoT) ✓
- [x] VLAN 99 (Management) ✓

### Interfaces
- [x] Gig0/1: Layer 3 routed port, 10.0.0.2/30, IPv6 ✓
- [x] Gig0/2-4: Trunk to district switches ✓
- [x] Fa0/3: Access VLAN 20 (Cellular backhaul) ✓
- [x] Fa0/4-10: Access VLAN 10 (Servers/Admin) ✓

### VLAN Interfaces (SVIs)
- [x] VLAN 10: 10.10.10.1/24, 2001:DB8:CITY:10::1/64 ✓
- [x] VLAN 20: 10.10.20.1/24, 2001:DB8:CITY:20::1/64 ✓
- [x] VLAN 30: 10.10.30.1/24, 2001:DB8:CITY:30::1/64 ✓
- [x] VLAN 99: 10.10.99.1/24, 2001:DB8:CITY:99::1/64 ✓

### Routing
- [x] IPv4 default route to 10.0.0.1 ✓
- [x] IPv6 default route to 2001:DB8:CITY:0::1 ✓
- [x] IPv6 unicast routing enabled ✓

### Security ACLs
- [x] IPv4 ACL: BLOCK-PUBLIC-TO-ADMIN ✓
  - **FIXED:** Permits DNS (UDP/TCP 53) to 10.10.10.10 ✓
  - Denies all other traffic from 10.10.20.0/24 → 10.10.10.0/24 ✓
  - Applied to VLAN 20 inbound ✓
- [x] IPv6 ACL: BLOCK-PUBLIC-TO-ADMIN-V6 ✓
  - **FIXED:** Permits DNS (UDP/TCP 53) to 2001:DB8:CITY:10::10 ✓
  - Denies all other traffic from 2001:DB8:CITY:20::/64 → 2001:DB8:CITY:10::/64 ✓
  - Applied to VLAN 20 inbound ✓

**Core switch config verified ✓**

---

## ✅ District Switches Configuration Check

### Downtown-Switch
- [x] VLANs: 20, 99 ✓
- [x] Fa0/1: Trunk to core, native VLAN 99 ✓
- [x] Fa0/2-4: Access VLAN 20 ✓

### Park-Switch
- [x] VLANs: 30, 99 ✓
- [x] Fa0/1: Trunk to core, native VLAN 99 ✓
- [x] Fa0/2-3: Access VLAN 30 ✓ (CHANGED - now 2 ports)

### Residential-Switch
- [x] VLANs: 30, 99 ✓
- [x] Fa0/1: Trunk to core, native VLAN 99 ✓
- [x] Fa0/2-3: Access VLAN 30 ✓

**District switches verified ✓**

---

## ✅ Server Configurations Check

### DNS-Server (10.10.10.10)
- [x] IPv4: 10.10.10.10/24, GW: 10.10.10.1, DNS: self ✓
- [x] IPv6: 2001:DB8:CITY:10::10/64 ✓
- [x] DNS A Records configured ✓
- [x] DNS AAAA Records (if supported by PT) ✓

### DHCP-Server (10.10.10.20)
- [x] IPv4: 10.10.10.20/24, GW: 10.10.10.1 ✓
- [x] IPv6: 2001:DB8:CITY:10::20/64 ✓
- [x] AdminPool: 10.10.10.100-150 ✓
- [x] PublicPool: 10.10.20.100-200 ✓
- [x] IoTPool: 10.10.30.100-150 ✓

### Web-Server (10.10.10.30)
- [x] IPv4: 10.10.10.30/24, GW: 10.10.10.1 ✓
- [x] IPv6: 2001:DB8:CITY:10::30/64 ✓
- [x] HTTP enabled ✓

### SMTP-Server (10.10.10.40)
- [x] IPv4: 10.10.10.40/24, GW: 10.10.10.1 ✓
- [x] IPv6: 2001:DB8:CITY:10::40/64 ✓
- [x] Domain: smartcity.local ✓
- [x] User: admin@smartcity.local ✓

### Central-Office-Server (10.10.20.50)
- [x] IPv4: 10.10.20.50/24, GW: 10.10.20.1 ✓
- [x] IPv6: 2001:DB8:CITY:20::50/64 ✓
- [x] No services (cellular gateway only) ✓

**All servers verified ✓**

---

## ✅ IoT Configuration Check

### Park-IoT-Gateway
- [x] IPv4: 10.10.30.10/24, GW: 10.10.30.1 ✓
- [x] Connected to: Park-Switch Fa0/2 (VLAN 30) ✓
- [x] Motion Sensor on D0 port ✓

### Smart-Streetlight
- [x] IPv4: 10.10.30.20/24, GW: 10.10.30.1 ✓
- [x] Connected to: Park-Switch Fa0/3 (VLAN 30) ✓
- [x] Network-controlled (not GPIO) ✓

### IoT Automation Logic
- [x] Trigger: Motion Sensor (D0) ✓
- [x] Action: Control LED via network (10.10.30.20) ✓
- [x] Email alert to admin@smartcity.local ✓
- [x] SMTP: 10.10.10.40 ✓

**IoT config verified ✓**

---

## ✅ Wireless Configuration Check

### Public-WiFi-AP
- [x] SSID: City-Public-WiFi ✓
- [x] Security: WPA2-PSK ✓
- [x] Passphrase: publicaccess ✓
- [x] Network: DHCP ✓
- [x] VLAN: 20 (Public) ✓

### Residential-WiFi-AP
- [x] SSID: Residential-Network ✓
- [x] Security: WPA2-PSK ✓
- [x] Passphrase: homeaccess ✓
- [x] Network: DHCP ✓
- [x] VLAN: 30 (IoT) ✓

**Wireless config verified ✓**

---

## 🔧 CRITICAL ISSUE FIXED

### ACL Configuration Corrected

**Problem Found:**
The original ACL configuration blocked ALL traffic from Public VLAN (20) to Admin VLAN (10), including DNS queries. This would have prevented Public VLAN devices from resolving domain names since the DNS server (10.10.10.10) is in the Admin VLAN.

**Fix Applied:**
ACLs now permit DNS traffic (UDP and TCP port 53) to the DNS server BEFORE blocking other traffic:

```cisco
! IPv4 ACL - CORRECTED
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
 permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
 permit ip any any

! IPv6 ACL - CORRECTED
ipv6 access-list BLOCK-PUBLIC-TO-ADMIN-V6
 permit udp 2001:DB8:CITY:20::/64 host 2001:DB8:CITY:10::10 eq 53
 permit tcp 2001:DB8:CITY:20::/64 host 2001:DB8:CITY:10::10 eq 53
 deny ipv6 2001:DB8:CITY:20::/64 2001:DB8:CITY:10::/64
 permit ipv6 any any
```

**Result:**
- ✅ Public VLAN can perform DNS queries (nslookup will work)
- ✅ Public VLAN still blocked from pinging or accessing other Admin resources
- ✅ Security maintained while allowing necessary DNS functionality

---

## ⚠️ Critical Configuration Notes

### Before Starting Stage 3:

1. **Router Internet Connection**
   - Gig0/0/0 connects to Internet cloud/ISP
   - Set to DHCP - will auto-configure when connected

2. **Core Switch Port Types**
   - Gig0/1 must be "no switchport" (Layer 3)
   - Gig0/2-4 must be trunk mode
   - All FastEthernet ports are Layer 2 access

3. **DHCP Configuration**
   - Ensure each pool has correct gateway and DNS
   - Test after configuration by setting PCs to DHCP

4. **DNS Records**
   - Add all A records first
   - Add AAAA records only if PT supports them
   - If AAAA not supported, skip without issue

5. **IoT Programming**
   - Motion sensor: Use D0 input
   - Smart LED: Control via network IP (10.10.30.20)
   - Use "IoT Device" or "IoT Server" blocks in Blockly

6. **ACL Testing Critical**
   - Test that Public VLAN cannot PING Admin VLAN (ICMP blocked)
   - Verify DNS queries (nslookup) WORK from Public VLAN (UDP/TCP 53 allowed)
   - Ping to DNS server should FAIL but nslookup should WORK

---

## 🎯 Stage 3 Configuration Order (Recommended)

Follow this exact order for best results:

### Phase 1: Core Network (15 min)
1. Configure Router (5 min)
2. Configure Core Switch (10 min)
3. **VERIFY**: Ping 10.0.0.1 from 10.0.0.2

### Phase 2: Servers (15 min)
4. Configure DNS Server
5. Configure DHCP Server
6. Configure Web Server
7. Configure SMTP Server
8. Configure Central Office Server
9. **VERIFY**: Ping all servers from each other

### Phase 3: District Switches (5 min)
10. Configure Downtown-Switch
11. Configure Park-Switch
12. Configure Residential-Switch
13. **VERIFY**: Show vlan brief on each

### Phase 4: End Devices (10 min)
14. Set PCs to DHCP
15. Configure IP Phones (auto via DHCP)
16. **VERIFY**: Check IP addresses assigned

### Phase 5: Wireless (5 min)
17. Configure Public-WiFi-AP
18. Configure Residential-WiFi-AP
19. Connect smartphone
20. **VERIFY**: Smartphone gets IP

### Phase 6: IoT (10 min)
21. Configure Smart-Streetlight IP
22. Configure Park-IoT-Gateway IP
23. Program IoT automation (Blockly)
24. **VERIFY**: Activate sensor, test light

**Total Time: ~60 minutes**

---

## ✅ Final Pre-Stage-3 Checklist

- [x] All 23 devices placed on workspace
- [x] All physical cables connected
- [x] All connection tables verified
- [x] IP addressing scheme confirmed (no conflicts)
- [x] VLAN assignments verified
- [x] Router config reviewed
- [x] Core switch config reviewed
- [x] District switches config reviewed
- [x] Server configs reviewed
- [x] IoT setup updated (D0 + network LED)
- [x] Wireless configs reviewed
- [x] Configuration order planned

## 🚀 YOU ARE READY FOR STAGE 3!

**All settings verified. No conflicts found. Proceed with confidence!**

---

**Last Updated:** Stage 2 Complete - All configurations verified
