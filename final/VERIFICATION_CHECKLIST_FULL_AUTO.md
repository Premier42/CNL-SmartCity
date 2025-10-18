# Verification Checklist for connection_FULL_AUTO.pkt

---

## 📋 HOW TO USE THIS CHECKLIST

Open **`connection_FULL_AUTO.pkt`** in Packet Tracer, then go through each device below and verify the configurations.

Check off ✅ each item as you verify it. If something is ❌ missing, follow the fix instructions.

---

## 🔧 NETWORK DEVICES VERIFICATION

### 1. City-Gateway-Router

**Steps:**
1. Click **City-Gateway-Router**
2. Go to **CLI** tab
3. Type: `enable` (password: `class`)
4. Type: `show running-config`

**Verify these are present:**
- [ ] Hostname: `City-Gateway-Router`
- [ ] Enable secret configured
- [ ] Interface Gig0/0/0: `ip address dhcp`, `ip nat outside`
- [ ] Interface Gig0/0/1: `ip address 10.0.0.1 255.255.255.252`, `ip nat inside`
- [ ] NAT overload: `ip nat inside source list 1 interface Gig0/0/0 overload`
- [ ] Access-list 1: `permit 10.10.0.0 0.0.255.255`
- [ ] Default route: `ip route 0.0.0.0 0.0.0.0 Gig0/0/0`
- [ ] IPv6 routing enabled: `ipv6 unicast-routing`

**Quick test:**
```
show ip interface brief
```
- [ ] Gig0/0/0 shows up/up
- [ ] Gig0/0/1 shows up/up with IP 10.0.0.1

✅ **Status:** _______

---

### 2. City-Core-Switch

**Steps:**
1. Click **City-Core-Switch**
2. Go to **CLI** tab
3. Type: `enable` (password: `class`)
4. Type: `show running-config`

**Verify VLANs exist:**
```
show vlan brief
```
- [ ] VLAN 10 (Admin)
- [ ] VLAN 20 (Public)
- [ ] VLAN 30 (IoT)
- [ ] VLAN 99 (Management)

**Verify trunk ports:**
```
show interfaces trunk
```
- [ ] Gig1/0/2 (to Downtown-Switch) - VLANs 10,20,30,99
- [ ] Gig1/0/3 (to Park-Switch) - VLANs 10,20,30,99
- [ ] Gig1/0/4 (to Residential-Switch) - VLANs 10,20,30,99

**Verify SVIs (gateways):**
```
show ip interface brief
```
- [ ] Vlan10: 10.10.10.1
- [ ] Vlan20: 10.10.20.1
- [ ] Vlan30: 10.10.30.1
- [ ] Vlan99: 10.10.99.1
- [ ] Gig1/0/1: 10.0.0.2 (to router)

**Verify ACL:**
```
show access-lists
```
- [ ] Extended ACL "BLOCK-PUBLIC-TO-ADMIN"
- [ ] Permits DNS (UDP/TCP 53) to 10.10.10.10
- [ ] Denies Public (10.10.20.0/24) to Admin (10.10.10.0/24)
- [ ] Permits all other traffic

✅ **Status:** _______

---

### 3. Downtown-Switch

**Steps:**
1. Click **Downtown-Switch**
2. Go to **CLI** tab
3. Type: `enable`
4. Type: `show vlan brief`

**Verify:**
- [ ] Hostname: Downtown-Switch
- [ ] VLAN 20 (Public) exists
- [ ] VLAN 99 (Management) exists
- [ ] Fa0/1 is trunk port

✅ **Status:** _______

---

### 4. Park-Switch

**Steps:**
1. Click **Park-Switch**
2. Go to **CLI** tab
3. Type: `enable`
4. Type: `show vlan brief`

**Verify:**
- [ ] Hostname: Park-Switch
- [ ] VLAN 30 (IoT) exists
- [ ] VLAN 99 (Management) exists
- [ ] Fa0/1 is trunk port
- [ ] Fa0/2-3 are access ports (VLAN 30)

✅ **Status:** _______

---

### 5. Residential-Switch

**Steps:**
1. Click **Residential-Switch**
2. Go to **CLI** tab
3. Type: `enable`
4. Type: `show vlan brief`

**Verify:**
- [ ] Hostname: Residential-Switch
- [ ] VLAN 30 (IoT) exists
- [ ] VLAN 99 (Management) exists
- [ ] Fa0/1 is trunk port
- [ ] Fa0/2-3 are access ports (VLAN 30)

✅ **Status:** _______

---

## 🖥️ SERVER IP VERIFICATION

### 6. DNS-Server

**Steps:**
1. Click **DNS-Server**
2. Go to **Config** tab
3. Click **FastEthernet0**

**Verify IP Configuration:**
- [ ] IP Address: `10.10.10.10`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.10.1`
- [ ] DNS Server: `10.10.10.10`

**Check DNS Service:**
1. Go to **Services** tab
2. Click **DNS**

**Verify:**
- [ ] DNS Service is ON
- [ ] Check if DNS records exist (you may need to add them)

**If DNS records are missing, add these:**
- [ ] `smartcity.local` → `10.10.10.30`
- [ ] `dns.smartcity.local` → `10.10.10.10`
- [ ] `dhcp.smartcity.local` → `10.10.10.20`
- [ ] `web.smartcity.local` → `10.10.10.30`
- [ ] `mail.smartcity.local` → `10.10.10.40`
- [ ] `centraloffice.smartcity.local` → `10.10.20.50`

✅ **Status:** _______

---

### 7. DHCP-Server

**Steps:**
1. Click **DHCP-Server**
2. Go to **Config** tab
3. Click **FastEthernet0**

**Verify IP Configuration:**
- [ ] IP Address: `10.10.10.20`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.10.1`
- [ ] DNS Server: `10.10.10.10`

**Check DHCP Service:**
1. Go to **Services** tab
2. Click **DHCP**

**Verify:**
- [ ] DHCP Service is ON
- [ ] Check if DHCP pools exist

**Expected pools (check if they exist):**
- [ ] **AdminPool:** 10.10.10.100-150, Gateway: 10.10.10.1, DNS: 10.10.10.10
- [ ] **PublicPool:** 10.10.20.100-200, Gateway: 10.10.20.1, DNS: 10.10.10.10
- [ ] **IoTPool:** 10.10.30.100-150, Gateway: 10.10.30.1, DNS: 10.10.10.10

**If pools are missing or wrong, you need to create them manually:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 3

✅ **Status:** _______

---

### 8. Web-Server

**Steps:**
1. Click **Web-Server**
2. Go to **Config** tab
3. Click **FastEthernet0**

**Verify IP Configuration:**
- [ ] IP Address: `10.10.10.30`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.10.1`
- [ ] DNS Server: `10.10.10.10`

**Check HTTP Service:**
1. Go to **Services** tab
2. Click **HTTP**

**Verify:**
- [ ] HTTP Service is ON
- [ ] Check if `index.html` exists
- [ ] Check if content is custom or default

**If web content needs updating:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 8

✅ **Status:** _______

---

### 9. SMTP-Server

**Steps:**
1. Click **SMTP-Server**
2. Go to **Config** tab
3. Click **FastEthernet0**

**Verify IP Configuration:**
- [ ] IP Address: `10.10.10.40`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.10.1`
- [ ] DNS Server: `10.10.10.10`

**Check EMAIL Service:**
1. Go to **Services** tab
2. Click **EMAIL**

**Verify:**
- [ ] EMAIL Service is ON
- [ ] Domain Name: `smartcity.local` (you may need to set this)
- [ ] Check if users exist

**Expected users:**
- [ ] `admin` (password: `cisco`)
- [ ] `iot` (password: `cisco`)

**If users are missing:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 7

✅ **Status:** _______

---

### 10. Central-Office-Server

**Steps:**
1. Click **Central-Office-Server**
2. Go to **Config** tab
3. Click **FastEthernet0** (or Desktop → IP Configuration)

**Verify IP Configuration:**
- [ ] IP Address: `10.10.20.50`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.20.1`
- [ ] DNS Server: `10.10.10.10`

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 1.1

✅ **Status:** _______

---

### 11. Park-IoT-Gateway

**Steps:**
1. Click **Park-IoT-Gateway**
2. Go to **Config** tab
3. Click **FastEthernet0**

**Verify IP Configuration:**
- [ ] IP Address: `10.10.30.10`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Default Gateway: `10.10.30.1` (in Settings → Global)
- [ ] DNS Server: `10.10.10.10`

**Check IoT Programming:**
1. Go to **Programming** tab
2. Click **Blockly**

**Verify automation exists:**
- [ ] Motion sensor (D0) trigger exists
- [ ] Sets device 10.10.30.20 brightness to 1023
- [ ] Waits 60 seconds
- [ ] Sets device 10.10.30.20 brightness to 0
- [ ] Sends email to admin@smartcity.local

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Steps 1.2 and 9

✅ **Status:** _______

---

## 💻 CLIENT DEVICE VERIFICATION

### 12. Admin-PC-1

**Steps:**
1. Click **Admin-PC-1**
2. Go to **Desktop** tab
3. Click **IP Configuration**

**Verify:**
- [ ] DHCP is selected (not Static)
- [ ] IP Address shows: 10.10.10.100-150 range
- [ ] Subnet Mask: 255.255.255.0
- [ ] Default Gateway: 10.10.10.1
- [ ] DNS Server: 10.10.10.10

**If shows 0.0.0.0 or wrong IP:**
- DHCP pools may not be configured
- See **COMPLETE_MANUAL_GUIDE.md** Step 3 (DHCP pools)
- Then see Step 4.1 (enable DHCP on PC)

✅ **Status:** _______

---

### 13. Admin-PC-2

**Steps:**
1. Click **Admin-PC-2**
2. Go to **Desktop** → **IP Configuration**

**Verify:**
- [ ] DHCP is selected
- [ ] IP Address: 10.10.10.100-150 range
- [ ] Gateway: 10.10.10.1
- [ ] DNS: 10.10.10.10

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 4.2

✅ **Status:** _______

---

### 14. Public-Kiosk-PC

**Steps:**
1. Click **Public-Kiosk-PC**
2. Go to **Desktop** → **IP Configuration**

**Verify:**
- [ ] DHCP is selected
- [ ] IP Address: 10.10.20.100-200 range
- [ ] Gateway: 10.10.20.1
- [ ] DNS: 10.10.10.10

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 4.3

✅ **Status:** _______

---

### 15. Resident-Home-PC

**Steps:**
1. Click **Resident-Home-PC**
2. Go to **Desktop** → **IP Configuration**

**Verify:**
- [ ] DHCP is selected
- [ ] IP Address: 10.10.30.100-150 range
- [ ] Gateway: 10.10.30.1
- [ ] DNS: 10.10.10.10

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 4.4

✅ **Status:** _______

---

## 📡 WiFi DEVICE VERIFICATION

### 16. Public-WiFi-AP

**Steps:**
1. Click **Public-WiFi-AP**
2. Go to **Config** tab
3. Click **Wireless** (or Port 0)

**Verify:**
- [ ] SSID: `City-Public-WiFi`
- [ ] Authentication: WPA2-PSK
- [ ] Password: `publicaccess`

**Check Internet Port:**
1. Click **Port 1**

**Verify:**
- [ ] IP Configuration set to DHCP
- [ ] Has received IP from PublicPool (10.10.20.x)

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 5.1

✅ **Status:** _______

---

### 17. Residential-WiFi-AP

**Steps:**
1. Click **Residential-WiFi-AP**
2. Go to **Config** tab
3. Click **Wireless**

**Verify:**
- [ ] SSID: `Residential-Network`
- [ ] Authentication: WPA2-PSK
- [ ] Password: `homeaccess`

**Check Internet Port:**
1. Click **Port 1**

**Verify:**
- [ ] IP Configuration set to DHCP
- [ ] Has received IP from IoTPool (10.10.30.x)

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 5.2

✅ **Status:** _______

---

### 18. Citizen-Smartphone

**Steps:**
1. Click **Citizen-Smartphone**
2. Go to **Desktop** tab
3. Click **PC Wireless**
4. Check **Connect** tab

**Verify:**
- [ ] Connected to: `City-Public-WiFi`
- [ ] Status shows: Connected
- [ ] Has IP address from PublicPool (10.10.20.x)

**If NOT configured:**
- See **COMPLETE_MANUAL_GUIDE.md** Step 6

✅ **Status:** _______

---

## 🧪 FUNCTIONAL TESTS

### Test 1: Basic Connectivity

**From Admin-PC-1:**
1. Desktop → Command Prompt
2. Run these commands:

```
ipconfig
```
- [ ] Shows IP 10.10.10.x

```
ping 10.10.10.1
```
- [ ] Replies received (gateway works)

```
ping 10.10.10.10
```
- [ ] Replies received (DNS server reachable)

```
ping 8.8.8.8
```
- [ ] Replies received (Internet/NAT works)

✅ **Test 1 Status:** _______

---

### Test 2: DNS Resolution

**From Admin-PC-1 Command Prompt:**

```
nslookup smartcity.local
```
- [ ] Returns: 10.10.10.30

```
nslookup dns.smartcity.local
```
- [ ] Returns: 10.10.10.10

**If fails:**
- DNS records not configured
- See **COMPLETE_MANUAL_GUIDE.md** Step 2

✅ **Test 2 Status:** _______

---

### Test 3: Web Server Access

**From Admin-PC-1:**
1. Desktop → Web Browser
2. URL: `http://smartcity.local`

**Verify:**
- [ ] Page loads
- [ ] Shows "Smart City Network Dashboard"
- [ ] Shows network services list
- [ ] Shows VLAN table

**If fails:**
- Check DNS resolves smartcity.local
- Check Web-Server HTTP service is ON
- See **COMPLETE_MANUAL_GUIDE.md** Step 8

✅ **Test 3 Status:** _______

---

### Test 4: Security ACL (Public → Admin blocked)

**From Public-Kiosk-PC Command Prompt:**

```
nslookup smartcity.local
```
- [ ] Should WORK (returns 10.10.10.30) ✅

```
ping 10.10.10.10
```
- [ ] Should FAIL (Request timed out) ✅ This is CORRECT!

```
ping 10.10.10.1
```
- [ ] Should FAIL (Request timed out) ✅ This is CORRECT!

**If ping works (it shouldn't):**
- ACL not applied properly
- Check City-Core-Switch ACL configuration

✅ **Test 4 Status:** _______

---

### Test 5: IoT Automation

**Steps:**
1. Click **Park-Motion-Sensor**
2. Click to activate it
3. Watch **Smart-Streetlight**

**Verify:**
- [ ] Light turns ON (full brightness)
- [ ] Light stays ON for ~60 seconds
- [ ] Light turns OFF automatically

**Check email sent:**
1. Click **SMTP-Server**
2. Services → EMAIL
3. Check mailbox for admin@smartcity.local

**Verify:**
- [ ] Email from iot@smartcity.local received
- [ ] Subject: "Park Alert"
- [ ] Message mentions motion detected

**If fails:**
- Check Park-IoT-Gateway IP: 10.10.30.10
- Check Blockly code programmed
- Check SMTP users created
- See **COMPLETE_MANUAL_GUIDE.md** Steps 7 and 9

✅ **Test 5 Status:** _______

---

### Test 6: VoIP (Optional)

**Steps:**
1. Click **City-Hall-Phone**
2. Pick up handset
3. Dial **Info-Line-Phone** number

**Verify:**
- [ ] Call connects
- [ ] Can see call status
- [ ] Phones ring

✅ **Test 6 Status:** _______

---

## 📊 FINAL SUMMARY CHECKLIST

### Network Infrastructure
- [ ] All 5 network devices configured (Router + 4 Switches)
- [ ] All VLANs created (10, 20, 30, 99)
- [ ] All trunk ports operational
- [ ] All SVIs/gateways configured
- [ ] ACL configured and working

### Server Configuration
- [ ] All 6 server IPs configured
- [ ] DNS service configured with records
- [ ] DHCP service configured with pools
- [ ] Web server configured with content
- [ ] SMTP service configured with users
- [ ] IoT Gateway programmed

### Client Devices
- [ ] All 4 PCs configured for DHCP
- [ ] All PCs receiving IP addresses
- [ ] 2 WiFi APs configured
- [ ] Smartphone connected to WiFi

### Functional Tests
- [ ] Connectivity tests pass
- [ ] DNS resolution works
- [ ] Web access works
- [ ] Security ACL blocks correctly
- [ ] IoT automation works
- [ ] Emails send successfully

---

## 🎯 COMPLETION STATUS

**Total Items:** 100+

**Completed:** ___ / 100+

**Percentage:** ____%

---

## ✅ PROJECT IS 100% COMPLETE WHEN:

- [ ] All network devices verified ✅
- [ ] All servers verified ✅
- [ ] All clients verified ✅
- [ ] All WiFi devices verified ✅
- [ ] All 6 functional tests PASS ✅
- [ ] No red X on connections ✅
- [ ] All ports show green ✅

---

## 📝 NOTES / ISSUES FOUND

Write down any issues you find:

1. _________________________________________________

2. _________________________________________________

3. _________________________________________________

4. _________________________________________________

5. _________________________________________________

---

**Use this checklist to verify everything in `connection_FULL_AUTO.pkt`!**

**For any missing configurations, refer to `COMPLETE_MANUAL_GUIDE.md` for fix instructions.**
