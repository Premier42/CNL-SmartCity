# 🔧 COMPLETE MANUAL SETUP - FROM SCRATCH
## Use with connection.pkt (Your Original File)

**Time: ~45 minutes | Complete Step-by-Step**

---

## 📋 SECTION 1: ROUTER CONFIGURATION (8 minutes)

### Step 1.1: Access Router CLI

1. Click **City-Gateway-Router**
2. Click **CLI** tab
3. Wait for "Would you like to enter the initial configuration dialog?"
4. Type: `no` and press Enter

### Step 1.2: Enter Configuration Mode

```
enable
configure terminal
```

### Step 1.3: Basic Configuration

Copy and paste these commands ONE BY ONE:

```
hostname City-Gateway-Router
enable secret class
```

### Step 1.4: Enable IPv6 Routing

```
ipv6 unicast-routing
```

### Step 1.5: Configure WAN Interface (Gig0/0/0)

```
interface GigabitEthernet0/0/0
ip address dhcp
ip nat outside
ipv6 address autoconfig
ipv6 enable
no shutdown
exit
```

### Step 1.6: Configure LAN Interface (Gig0/0/1)

```
interface GigabitEthernet0/0/1
ip address 10.0.0.1 255.255.255.252
ip nat inside
ipv6 address autoconfig
ipv6 enable
no shutdown
exit
```

### Step 1.7: Configure NAT

```
ip nat inside source list 1 interface GigabitEthernet0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255
```

### Step 1.8: Configure Default Route

```
ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0/0
```

### Step 1.9: Configure Passwords

```
line console 0
password cisco
login
exit
line vty 0 4
password cisco
login
exit
```

### Step 1.10: Save Configuration

```
end
write memory
```

**Verification:**
```
show ip interface brief
```

**Expected output:**
```
GigabitEthernet0/0/0    unassigned      YES DHCP   up   up
GigabitEthernet0/0/1    10.0.0.1        YES manual up   up
```

✅ **Router Done!**

---

## 📋 SECTION 2: CORE SWITCH CONFIGURATION (10 minutes)

### Step 2.1: Access Core Switch CLI

1. Click **City-Core-Switch**
2. Click **CLI** tab
3. Type `no` if asked about initial config dialog

### Step 2.2: Enter Configuration Mode

```
enable
configure terminal
```

### Step 2.3: Basic Configuration

```
hostname City-Core-Switch
enable secret class
ipv6 unicast-routing
```

### Step 2.4: Create VLANs

```
vlan 10
name Admin
exit
vlan 20
name Public
exit
vlan 30
name IoT
exit
vlan 99
name Management
exit
```

### Step 2.5: Configure Router Link (Gig1/0/1)

```
interface GigabitEthernet1/0/1
no switchport
ip address 10.0.0.2 255.255.255.252
ipv6 enable
no shutdown
exit
```

### Step 2.6: Configure Trunk to Downtown-Switch (Gig1/0/2)

```
interface GigabitEthernet1/0/2
description Trunk to Downtown-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit
```

### Step 2.7: Configure Trunk to Park-Switch (Gig1/0/3)

```
interface GigabitEthernet1/0/3
description Trunk to Park-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit
```

### Step 2.8: Configure Trunk to Residential-Switch (Gig1/0/4)

```
interface GigabitEthernet1/0/4
description Trunk to Residential-Switch
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,30,99
no shutdown
exit
```

### Step 2.9: Configure Central Office Server Port (Gig1/0/5)

```
interface GigabitEthernet1/0/5
description Central Office Server - Cellular Backhaul
switchport mode access
switchport access vlan 20
no shutdown
exit
```

### Step 2.10: Configure Server Ports (Gig1/0/6-9)

```
interface range GigabitEthernet1/0/6-9
description Servers (DNS, DHCP, Web, SMTP)
switchport mode access
switchport access vlan 10
no shutdown
exit
```

### Step 2.11: Configure Admin Device Ports (Gig1/0/10-12)

```
interface range GigabitEthernet1/0/10-12
description Admin Devices (PCs and Phone)
switchport mode access
switchport access vlan 10
no shutdown
exit
```

### Step 2.12: Configure VLAN Interfaces (SVIs)

```
interface Vlan10
description Admin VLAN Gateway
ip address 10.10.10.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan20
description Public VLAN Gateway
ip address 10.10.20.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan30
description IoT VLAN Gateway
ip address 10.10.30.1 255.255.255.0
ipv6 enable
no shutdown
exit

interface Vlan99
description Management VLAN Gateway
ip address 10.10.99.1 255.255.255.0
ipv6 enable
no shutdown
exit
```

### Step 2.13: Configure Default Route

```
ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

### Step 2.14: Configure Security ACL

```
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
permit ip any any
exit
```

### Step 2.15: Apply ACL to VLAN 20

```
interface Vlan20
ip access-group BLOCK-PUBLIC-TO-ADMIN in
exit
```

### Step 2.16: Save Configuration

```
end
write memory
```

**Verification:**
```
show vlan brief
show ip interface brief
```

✅ **Core Switch Done!**

---

## 📋 SECTION 3: DOWNTOWN-SWITCH CONFIGURATION (3 minutes)

### Step 3.1: Access Downtown-Switch CLI

1. Click **Downtown-Switch**
2. Click **CLI** tab
3. Type `no` if asked

### Step 3.2: Configure

```
enable
configure terminal
hostname Downtown-Switch
```

### Step 3.3: Create VLANs

```
vlan 20
name Public
exit
vlan 99
name Management
exit
```

### Step 3.4: Configure Trunk Port (Fa0/1)

```
interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit
```

### Step 3.5: Configure Access Ports (Fa0/2-4)

```
interface range FastEthernet0/2-4
description Public VLAN Access Ports
switchport mode access
switchport access vlan 20
no shutdown
exit
```

### Step 3.6: Save

```
end
write memory
```

✅ **Downtown-Switch Done!**

---

## 📋 SECTION 4: PARK-SWITCH CONFIGURATION (3 minutes)

### Step 4.1: Access Park-Switch CLI

1. Click **Park-Switch**
2. Click **CLI** tab
3. Type `no` if asked

### Step 4.2: Configure

```
enable
configure terminal
hostname Park-Switch
```

### Step 4.3: Create VLANs

```
vlan 30
name IoT
exit
vlan 99
name Management
exit
```

### Step 4.4: Configure Trunk Port (Fa0/1)

```
interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit
```

### Step 4.5: Configure Access Ports (Fa0/2-3)

```
interface range FastEthernet0/2-3
description IoT VLAN Access Ports
switchport mode access
switchport access vlan 30
no shutdown
exit
```

### Step 4.6: Save

```
end
write memory
```

✅ **Park-Switch Done!**

---

## 📋 SECTION 5: RESIDENTIAL-SWITCH CONFIGURATION (3 minutes)

### Step 5.1: Access Residential-Switch CLI

1. Click **Residential-Switch**
2. Click **CLI** tab
3. Type `no` if asked

### Step 5.2: Configure

```
enable
configure terminal
hostname Residential-Switch
```

### Step 5.3: Create VLANs

```
vlan 30
name IoT
exit
vlan 99
name Management
exit
```

### Step 5.4: Configure Trunk Port (Fa0/1)

```
interface FastEthernet0/1
description Trunk to City-Core-Switch
switchport mode trunk
switchport trunk native vlan 99
no shutdown
exit
```

### Step 5.5: Configure Access Ports (Fa0/2-3)

```
interface range FastEthernet0/2-3
description IoT VLAN Access Ports
switchport mode access
switchport access vlan 30
no shutdown
exit
```

### Step 5.6: Save

```
end
write memory
```

✅ **Residential-Switch Done!**

---

## 📋 SECTION 6: SERVER IP CONFIGURATION (5 minutes)

### DNS-Server

1. Click **DNS-Server**
2. Click **Config** tab
3. Click **FastEthernet0**
4. Set:
   - **IP Address:** `10.10.10.10`
   - **Subnet Mask:** `255.255.255.0`
5. Scroll down to **Settings** section (same page)
6. Set:
   - **Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

### DHCP-Server

1. Click **DHCP-Server**
2. Click **Config** tab
3. Click **FastEthernet0**
4. Set:
   - **IP Address:** `10.10.10.20`
   - **Subnet Mask:** `255.255.255.0`
5. Scroll down to **Settings**
6. Set:
   - **Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

### Web-Server

1. Click **Web-Server**
2. Click **Config** tab
3. Click **FastEthernet0**
4. Set:
   - **IP Address:** `10.10.10.30`
   - **Subnet Mask:** `255.255.255.0`
5. Scroll down to **Settings**
6. Set:
   - **Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

### SMTP-Server

1. Click **SMTP-Server**
2. Click **Config** tab
3. Click **FastEthernet0**
4. Set:
   - **IP Address:** `10.10.10.40`
   - **Subnet Mask:** `255.255.255.0`
5. Scroll down to **Settings**
6. Set:
   - **Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

✅ **Servers Done!**

---

## 📋 SECTION 7: DHCP POOLS CONFIGURATION (5 minutes)

### Step 7.1: Enable DHCP Service

1. Click **DHCP-Server**
2. Click **Services** tab
3. Click **DHCP**
4. Click **On** radio button (to enable service)

### Step 7.2: Create AdminPool

**Fill in the form fields:**
- **Pool Name:** `AdminPool`
- **Default Gateway:** `10.10.10.1`
- **DNS Server:** `10.10.10.10`
- **Start IP Address:** `10.10.10.100`
- **Subnet Mask:** `255.255.255.0`
- **Maximum Number of Users:** `50`

**Click the [Add] or [Save] button!** (Very important!)

### Step 7.3: Create PublicPool

**Clear the form and enter:**
- **Pool Name:** `PublicPool`
- **Default Gateway:** `10.10.20.1`
- **DNS Server:** `10.10.10.10`
- **Start IP Address:** `10.10.20.100`
- **Subnet Mask:** `255.255.255.0`
- **Maximum Number of Users:** `100`

**Click [Add] or [Save]!**

### Step 7.4: Create IoTPool

**Clear the form and enter:**
- **Pool Name:** `IoTPool`
- **Default Gateway:** `10.10.30.1`
- **DNS Server:** `10.10.10.10`
- **Start IP Address:** `10.10.30.100`
- **Subnet Mask:** `255.255.255.0`
- **Maximum Number of Users:** `50`

**Click [Add] or [Save]!**

### Step 7.5: Verify Pools Created

**Scroll down** - you should see all 3 pools listed:
- AdminPool
- PublicPool
- IoTPool

✅ **DHCP Pools Done!**

---

## 📋 SECTION 8: DNS RECORDS CONFIGURATION (4 minutes)

### Step 8.1: Enable DNS Service

1. Click **DNS-Server**
2. Click **Services** tab
3. Click **DNS**
4. Click **On** radio button

### Step 8.2: Add DNS Records

**For each record below:**
1. Enter the **Name**
2. Enter the **IP Address**
3. Click **[Add]**

**Record 1:**
- Name: `smartcity.local`
- Address: `10.10.10.30`
- Click [Add]

**Record 2:**
- Name: `dns.smartcity.local`
- Address: `10.10.10.10`
- Click [Add]

**Record 3:**
- Name: `mail.smartcity.local`
- Address: `10.10.10.40`
- Click [Add]

**Record 4:**
- Name: `dhcp.smartcity.local`
- Address: `10.10.10.20`
- Click [Add]

**Record 5:**
- Name: `www.smartcity.local`
- Address: `10.10.10.30`
- Click [Add]

✅ **DNS Records Done!**

---

## 📋 SECTION 9: CLIENT PC CONFIGURATION (3 minutes)

### Admin-PC-1

1. Click **Admin-PC-1**
2. Click **Desktop** tab
3. Click **IP Configuration**
4. Select **DHCP** radio button
5. Wait 5 seconds
6. **Should get IP:** `10.10.10.100` or similar

**If you get 169.254.x.x (APIPA):**
- Click **Static**, wait 2 seconds
- Click **DHCP** again
- Wait 5 seconds

### Admin-PC-2

1. Click **Admin-PC-2**
2. Click **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Should get: `10.10.10.101` or similar

### Public-Kiosk-PC

1. Click **Public-Kiosk-PC**
2. Click **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Should get: `10.10.20.100` or similar

### Resident-Home-PC

1. Click **Resident-Home-PC**
2. Click **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Should get: `10.10.30.100` or similar

✅ **Client PCs Done!**

---

## 📋 SECTION 10: ADDITIONAL DEVICE CONFIGURATION (5 minutes)

### Central-Office-Server

1. Click **Central-Office-Server**
2. Click **Desktop** → **IP Configuration**
3. Select **Static**
4. Set:
   - **IP Address:** `10.10.20.50`
   - **Subnet Mask:** `255.255.255.0`
   - **Default Gateway:** `10.10.20.1`
   - **DNS Server:** `10.10.10.10`

### Park-IoT-Gateway

1. Click **Park-IoT-Gateway**
2. Click **Config** tab
3. Click **Ethernet0** (or FastEthernet0)
4. Set:
   - **IP Address:** `10.10.30.10`
   - **Subnet Mask:** `255.255.255.0`
5. Scroll to **Settings**
6. Set:
   - **Gateway:** `10.10.30.1`
   - **DNS Server:** `10.10.10.10`

✅ **Additional Devices Done!**

---

## 🧪 VERIFICATION TESTS (2 minutes)

### Test 1: Ping Gateway from Admin-PC-1

1. **Admin-PC-1** → **Desktop** → **Command Prompt**
2. Type: `ping 10.10.10.1`
3. **Expected:** Replies

### Test 2: Ping DNS Server

```
ping 10.10.10.10
```
**Expected:** Replies

### Test 3: DNS Resolution

```
nslookup smartcity.local
```
**Expected:** Returns `10.10.10.30`

### Test 4: ACL Security Test

1. **Public-Kiosk-PC** → **Desktop** → **Command Prompt**
2. Type: `ping 10.10.10.10`
3. **Expected:** Should FAIL (timeout) - this proves ACL is blocking Public → Admin

But test DNS still works:
```
nslookup smartcity.local
```
**Expected:** Should work (DNS queries allowed by ACL)

### Test 5: Inter-VLAN Routing

From **Admin-PC-1**:
```
ping 10.10.20.50
```
**Expected:** Replies from Central-Office-Server

---

## ✅ ALL DONE!

**If all 5 tests pass, your network is 100% functional!** 🚀

**Save your file:**
- File → Save As → `my_completed_network.pkt`

---

## 📋 COMPLETION CHECKLIST

- [ ] Router configured and saved
- [ ] Core Switch configured and saved
- [ ] Downtown-Switch configured and saved
- [ ] Park-Switch configured and saved
- [ ] Residential-Switch configured and saved
- [ ] All 4 servers have IPs
- [ ] DHCP service enabled
- [ ] 3 DHCP pools created
- [ ] DNS service enabled
- [ ] 5 DNS records added
- [ ] All 4 PCs have DHCP IPs
- [ ] Central Office Server has static IP
- [ ] Park IoT Gateway has static IP
- [ ] All 5 verification tests pass

**Time Estimate:** 45-50 minutes total

Good luck! Tell me when you're ready to start and I'll guide you through each section!
