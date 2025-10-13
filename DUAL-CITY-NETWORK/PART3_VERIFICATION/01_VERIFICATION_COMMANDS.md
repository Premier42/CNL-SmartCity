# PART 3: VERIFICATION
## 01 - VERIFICATION COMMANDS & TESTS

**Quick checks to verify all technologies are working**

---

## ⚠️ IMPORTANT PACKET TRACER LIMITATIONS

### **What Works Perfectly:**
- ✅ OSPF routing and neighbor relationships
- ✅ VLAN creation and trunking
- ✅ NAT translations (with interface-based NAT)
- ✅ DHCP IP assignment
- ✅ DNS name resolution
- ✅ HTTP/HTTPS web services
- ✅ Wireless connectivity
- ✅ Inter-city communication

### **What Has Limitations:**
- ⚠️ **QoS:** Commands accepted, no actual packet prioritization visible
- ⚠️ **Some show commands:** May display zeros or no statistics
  - `show ip nat statistics` - may show zero counts
  - `show policy-map interface` - may show no stats
  - `show processes cpu` - always shows 0%
- ⚠️ **Cellular:** Simulated via Linksys WRT300N, works identically to WiFi

### **Working Show Commands:**
- ✅ `show ip ospf neighbor`
- ✅ `show ip nat translations`
- ✅ `show ip route`
- ✅ `show vlan brief`
- ✅ `show interfaces trunk`
- ✅ `show spanning-tree`
- ✅ `show ip interface brief`

**See `../COMPATIBILITY_GUIDE.md` for detailed PT version differences**

---

## 📋 VERIFICATION CHECKLIST

### **Physical Layer:**
- [ ] All devices powered on (green power indicators)
- [ ] All cables connected (green link lights)
- [ ] No red X marks on connections

### **Network Layer:**
- [ ] Router OSPF neighbors formed
- [ ] All interfaces UP/UP
- [ ] Routing tables populated

### **Data Link Layer:**
- [ ] VLANs created on all switches
- [ ] Trunk links operational
- [ ] STP converged

### **Application Layer:**
- [ ] DHCP assigning IPs
- [ ] DNS resolving names
- [ ] Web servers accessible
- [ ] Email working

### **Wireless:**
- [ ] SSIDs broadcasting
- [ ] Devices connected
- [ ] Wireless clients have IPs

### **Inter-City:**
- [ ] City A can ping City B
- [ ] NAT translating
- [ ] Data crossing ISP

---

## 🔧 ROUTER VERIFICATION

### **On CityA-Core-R1:**

```cisco
! Check interfaces
show ip interface brief
show ipv6 interface brief

! Check OSPF neighbors
show ip ospf neighbor

! Expected: 4 neighbors
! - CityA-Border-R1 (1.1.1.1)
! - CityA-Gov-R1 (1.1.1.3)
! - CityA-Res-R1 (1.1.1.4)
! - CityA-Com-R1 (1.1.1.5)

! Check routing table
show ip route
show ip route ospf

! Should see routes to:
! - 192.168.10.0/24 (via Gov-R1)
! - 192.168.20.0/24 (via Res-R1)
! - 192.168.30.0/24 (via Com-R1)
! - Default route (via Border-R1)

! Check sub-interfaces
show ip interface brief | include \\.

! Expected: Gig0/0.40, Gig0/0.50, Gig0/1.70, Gig0/1.99 UP

! Check ACLs
show access-lists
show ip access-lists 110

! Should show hit counts on ACL 110

! Check QoS
show policy-map
show policy-map interface GigabitEthernet1/1

! Check NAT (on Border-R1)
```

---

### **On CityA-Border-R1:**

```cisco
! Check WAN interface
show ip interface brief | include Serial

! Expected: Serial0/0/0 UP with IP 203.0.113.1

! Check NAT
show ip nat translations
show ip nat statistics

! After traffic flows, should see translations:
! Inside: 192.168.x.x → Outside: 203.0.113.x

! Check default route
show ip route static

! Expected: 0.0.0.0/0 via 203.0.113.2

! Test internet connectivity
ping 8.8.8.8
```

---

### **On ISP-Core-R1:**

```cisco
! Check OSPF neighbors
show ip ospf neighbor

! Expected: 3 neighbors
! - ISP-Border-R1 (2.2.2.1)
! - ISP-Border-R2 (2.2.2.2)
! - ISP-Core-R2 (2.2.2.4)

! Check routes to cities
show ip route | include 203.0.113
show ip route | include 203.0.114

! Should see routes to both cities
```

---

## 📡 SWITCH VERIFICATION

### **On CityA-Core-SW1:**

```cisco
! Check VLANs
show vlan brief

! Expected: VLANs 1, 10, 20, 30, 40, 50, 60, 70, 99

! Check trunks
show interfaces trunk

! Expected: Gig1/0/1, Gig1/0/2 trunking

! Check STP
show spanning-tree summary

! Expected: Root bridge for all VLANs

! Check port security
show port-security
show port-security interface FastEthernet1/0/1

! Check interface status
show ip interface brief
```

---

### **On Access Switches (e.g., CityA-Gov-SW1):**

```cisco
! Check VLANs
show vlan brief

! Expected: VLANs specific to that switch

! Check trunk
show interfaces trunk

! Expected: Port 24 trunking

! Check access ports
show interfaces status

! All access ports should show "connected"
```

---

## 🖥️ SERVER VERIFICATION

### **DNS Server Test:**

**From CityA-Gov-PC-1:**

```
! Open Command Prompt
nslookup www.city-a.local

! Expected output:
! Name: www.city-a.local
! Address: 192.168.99.30

! Test external DNS
nslookup www.city-b.local

! Should resolve to 203.0.114.1 (City B public IP)

! Test internet DNS
nslookup www.example.com

! Should resolve to 8.8.8.10
```

---

### **DHCP Server Test:**

**From any end device:**

1. Set IP configuration to **DHCP**
2. Wait 5-10 seconds
3. Check IP:

```
ipconfig

! Expected:
! IP Address: 192.168.[VLAN].100-220
! Subnet Mask: 255.255.255.0
! Default Gateway: 192.168.[VLAN].1
! DNS Server: 192.168.99.10
```

**On DHCP Server:**
- Check **Services → DHCP**
- View pool utilization
- Should show leases assigned

---

### **Web Server Test:**

**From any PC:**

1. Open **Desktop → Web Browser**
2. Enter URL: `http://www.city-a.local` OR `http://192.168.99.30`
3. Expected: City A welcome page loads

**Test from City B to City A:**
1. From CityB-Gov-PC-1
2. Navigate to: `http://www.city-a.local`
3. Should load (tests inter-city connectivity)

---

### **Email Server Test:**

**From CityA-Gov-PC-1:**

1. **Desktop → Email**
2. Configure:
   - Name: `Administrator`
   - Email: `admin@city-a.local`
   - Mail Server: `192.168.99.40`
   - User: `admin`
   - Password: `admin123`
3. **Compose** email to `gov.admin@city-a.local`
4. Send
5. Log in as `gov.admin` to receive
6. Expected: Email received

---

## 📶 WIRELESS VERIFICATION

### **WiFi Connection Test:**

**From CityA-Home-Smartphone-1:**

1. **Desktop → PC Wireless → Connect**
2. Scan should show:
   - `CityA-Gov-WiFi`
   - `CityA-Residential`
   - `CityA-Public`
3. Connect to `CityA-Residential`
4. Enter password: `ResidentSecure2024`
5. Connection status: **Connected**
6. Check IP: Should be in 192.168.20.100-220 range

---

### **Cellular Connection Test:**

**From smartphone with cellular:**

1. **Config → Wireless → Cellular**
2. Should auto-connect to `CityA-4G`
3. Check IP: 192.168.20.xxx
4. Test connectivity: `ping 192.168.99.1`

---

## 🌐 INTER-CITY CONNECTIVITY TESTS

### **Test 1: Ping from City A to City B**

**From CityA-Gov-PC-1:**

```
ping 192.168.10.101

! This pings internal City A device - should work

ping 192.168.99.30

! This pings City A web server - should work

ping 203.0.114.1

! This pings City B border router public IP - should work
```

**Expected:** All pings successful

---

### **Test 2: Traceroute Inter-City**

**From CityA-Gov-PC-1:**

```
tracert 203.0.114.1

! Expected path:
! 1. 192.168.10.1 (Gov-R1)
! 2. 10.0.1.1 (Core-R1)
! 3. 10.0.0.1 (Core-R1 to Border)
! 4. 203.0.113.2 (ISP-Border-R1)
! 5. 198.51.100.2 (ISP-Core-R1)
! 6. 198.51.100.6 (ISP-Core-R1 to Border-R2)
! 7. 203.0.114.1 (CityB-Border-R1)
```

---

### **Test 3: Access City B Website from City A**

**From CityA-Gov-PC-1:**

1. **Web Browser**
2. URL: `http://www.city-b.local`
3. Expected: City B welcome page loads

**This tests:**
- ✅ DNS resolution (city-b.local)
- ✅ Routing (OSPF)
- ✅ NAT (public IP translation)
- ✅ WAN link (serial connection)
- ✅ HTTP service

---

## 🔒 SECURITY & ACL TESTS

### **Test 1: Public WiFi Isolation**

**From CityA-Public-Phone-1 (VLAN 50):**

```
! Try to access internal network
ping 192.168.10.101

! Expected: Request timed out (ACL blocks)

! Try to access servers
ping 192.168.99.10

! Expected: Request timed out (ACL blocks DNS server)

! Try DNS query (should work)
nslookup www.example.com

! Expected: Resolves (ACL allows DNS to 192.168.99.10:53)

! Try internet access
ping 8.8.8.8

! Expected: Success (ACL allows internet)

! Try web browsing
! Open browser → http://www.city-a.local
! Expected: Loads (ACL allows HTTP/HTTPS)
```

**Demonstrates ACL working correctly!**

---

### **Test 2: Check ACL Hit Counters**

**On CityA-Core-R1:**

```cisco
show access-lists 110

! Expected output shows matches:
! Extended IP access list 110
!   10 permit tcp 192.168.50.0 0.0.0.255 any eq 80 (XX matches)
!   20 permit tcp 192.168.50.0 0.0.0.255 any eq 443 (XX matches)
!   30 permit udp 192.168.50.0 0.0.0.255 host 192.168.99.10 eq 53 (XX matches)
!   40 deny ip 192.168.50.0 0.0.0.255 192.168.0.0 0.0.255.255 log (XX matches)
!   50 permit ip any any (XX matches)
```

---

## 🎯 QoS VERIFICATION

### **Check QoS Policy:**

**On CityA-Core-R1:**

```cisco
show policy-map interface GigabitEthernet1/1

! Expected: Shows class traffic statistics
! - EMERGENCY-TRAFFIC: Priority 40%
! - IOT-TRAFFIC: Bandwidth 30%
! - class-default: Fair queue
```

---

### **Test QoS Priority:**

**Simulate emergency traffic:**

1. From **CityA-Police-PC-1** (VLAN 60 - Emergency)
2. Generate traffic (ping flood or large file transfer)
3. Simultaneously generate IoT traffic (VLAN 40)
4. Emergency traffic should have lower latency

**Note:** QoS effects are subtle in Packet Tracer simulation mode

---

## 🔍 COMPREHENSIVE END-TO-END TEST

### **Test Scenario: City A Resident accesses City B City Hall Website**

**From CityA-Home-PC-1 (VLAN 20):**

**Step 1:** Check connectivity
```
ipconfig

! Verify IP: 192.168.20.101 (DHCP)
! Verify Gateway: 192.168.20.1
! Verify DNS: 192.168.99.10
```

**Step 2:** Test DNS
```
nslookup www.city-b.local

! Should resolve to 203.0.114.1 (City B public IP)
```

**Step 3:** Test routing
```
tracert 203.0.114.1

! Should show path through City A → ISP → City B
```

**Step 4:** Access website
1. Open **Web Browser**
2. Navigate to: `http://www.city-b.local`
3. Expected: City B website loads

**THIS TESTS EVERYTHING:**
- ✅ DHCP (IP assignment)
- ✅ DNS (name resolution)
- ✅ VLAN (residential network)
- ✅ Inter-VLAN routing (VLAN 20 → Core)
- ✅ OSPF (routing to border)
- ✅ NAT (private → public IP)
- ✅ WAN (serial link to ISP)
- ✅ ISP routing (backbone)
- ✅ City B NAT (reverse translation)
- ✅ HTTP (web service)

**If this works, EVERYTHING works!** 🎉

---

## 📊 VERIFICATION SUMMARY TABLE

| Technology | Test Command/Action | Expected Result |
|------------|---------------------|-----------------|
| **OSPF** | `show ip ospf neighbor` | All neighbors UP |
| **NAT** | `show ip nat translations` | Translations visible |
| **VLANs** | `show vlan brief` | All VLANs present |
| **Trunking** | `show interfaces trunk` | Trunk ports operational |
| **STP** | `show spanning-tree` | Root bridge elected, converged |
| **DHCP** | `ipconfig` on client | IP in correct range |
| **DNS** | `nslookup www.city-a.local` | Resolves correctly |
| **HTTP** | Web browser → city website | Page loads |
| **WiFi** | Connect smartphone | Associated, IP assigned |
| **ACLs** | Ping from public to internal | Blocked |
| **QoS** | `show policy-map interface` | Policy active |
| **IPv6** | `show ipv6 interface brief` | All interfaces have IPv6 |
| **Inter-City** | Ping/Web to other city | Communication successful |

---

## ⏱️ ESTIMATED TIME

- Router checks: 15 minutes
- Switch checks: 15 minutes
- Server tests: 15 minutes
- Wireless tests: 10 minutes
- Inter-city tests: 10 minutes
- Security tests: 10 minutes
- **Total: ~1.5 hours**

---

## 🎓 DEMONSTRATING TO PROFESSOR

### **Quick Demo Script (10 minutes):**

**1. Show Physical Topology (1 min)**
- Open Packet Tracer file
- Zoom out to show both cities + ISP
- Point out zones, VLANs, wireless

**2. Show Router OSPF (2 min)**
- CLI on CityA-Core-R1
- `show ip ospf neighbor` (4 neighbors)
- `show ip route ospf` (routes learned)

**3. Show NAT (1 min)**
- CLI on CityA-Border-R1
- `show ip nat translations`

**4. Show VLANs (1 min)**
- CLI on CityA-Core-SW1
- `show vlan brief` (8 VLANs)
- `show interfaces trunk`

**5. Demonstrate DHCP (1 min)**
- On CityA-Gov-PC-1
- `ipconfig` (show DHCP-assigned IP)

**6. Demonstrate DNS (1 min)**
- On same PC
- `nslookup www.city-b.local`

**7. Demonstrate Inter-City Web (2 min)**
- On CityA-Gov-PC-1
- Web Browser → `http://www.city-b.local`
- Show page loading

**8. Demonstrate ACL Security (1 min)**
- On CityA-Public-Phone-1
- Try ping 192.168.10.101 (blocked)
- Try web browsing (works)

**Professor sees:**
- ✅ Two realistic cities
- ✅ All technologies working
- ✅ Professional configuration
- ✅ Security implemented
- ✅ Inter-city connectivity

---

## ✅ FINAL CHECKLIST

**Before submission:**

- [ ] All 102 devices placed
- [ ] All ~90 cables connected
- [ ] All 14 routers configured (OSPF, NAT, sub-interfaces)
- [ ] All 16 switches configured (VLANs, trunks, STP)
- [ ] All 10 servers configured (DHCP, DNS, HTTP, Email)
- [ ] All 8 wireless devices configured
- [ ] All wireless clients connected
- [ ] OSPF neighbors formed
- [ ] NAT working
- [ ] DHCP assigning IPs
- [ ] DNS resolving names
- [ ] Websites accessible
- [ ] ACLs blocking public access
- [ ] Inter-city communication working
- [ ] File saved with proper name
- [ ] Backup copy created

---

## 🎉 PROJECT COMPLETE!

**You've built:**
- 2 complete smart cities
- 102 devices
- 8 VLANs per city
- OSPF routing (14 routers)
- NAT implementation
- DHCP automation
- DNS services
- Wireless infrastructure
- Security policies (ACLs)
- QoS prioritization
- Inter-city WAN

**ALL networking technologies demonstrated!**

**Ready for submission!** 🚀
