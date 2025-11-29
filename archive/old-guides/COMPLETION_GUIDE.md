# Smart City Network - Completion Configuration Guide

## Current Network Analysis

### IP Addressing Scheme (Detected):
- **VLAN 10 Network:** 10.10.10.0/24 (Servers/Admin)
- **VLAN 20 Network:** 10.10.20.0/24 (Public)
- **VLAN 30 Network:** 10.10.30.0/24 (IoT)

### Current Device IPs:
- **DNS Server:** 10.10.10.10
- **DHCP Server:** 10.10.10.20
- **Web Server:** 10.10.10.40
- **SMTP Server:** 10.10.10.30
- **PCs:** Using DHCP (10.10.10.100, 10.10.10.2, etc.)

---

## STEP-BY-STEP COMPLETION GUIDE

### STEP 1: Configure the Main Router (Critical - Do This First!)

**Device Name in Packet Tracer:** Look for the router device labeled "Router" in your network

#### How to Access the Router CLI:
1. In Packet Tracer workspace, **click on the Router device** (the icon that looks like a router)
2. A new window will pop up showing the device
3. At the top of the window, you'll see tabs: Physical, Config, CLI, etc.
4. **Click the "CLI" tab**
5. You'll see a black command-line screen - this is where you paste the commands

#### 1.1 Configure Router - Copy ALL commands below and paste into CLI:

```cisco
enable
configure terminal
hostname SmartCity-Router

! Enable IPv6 routing
ipv6 unicast-routing

! Interface to City-Core-Switch (Assuming GigabitEthernet0/0)
interface GigabitEthernet0/0
 description "Trunk to City-Core-Switch"
 no shutdown

! Subinterface for VLAN 10 (Servers/Admin)
interface GigabitEthernet0/0.10
 description "VLAN 10 - Servers and Admin"
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
 ipv6 address 2001:DB8:10::1/64
 ip helper-address 10.10.10.20
 no shutdown

! Subinterface for VLAN 20 (Public)
interface GigabitEthernet0/0.20
 description "VLAN 20 - Public Access"
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
 ipv6 address 2001:DB8:20::1/64
 ip helper-address 10.10.10.20
 no shutdown

! Subinterface for VLAN 30 (IoT)
interface GigabitEthernet0/0.30
 description "VLAN 30 - IoT Devices"
 encapsulation dot1Q 30
 ip address 10.10.30.1 255.255.255.0
 ipv6 address 2001:DB8:30::1/64
 ip helper-address 10.10.10.20
 no shutdown

exit
```

#### 1.2 Configure ACLs (Security)

```cisco
! IoT Security ACL - Allow IoT to servers/admin only
access-list 110 permit ip 10.10.30.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 110 deny ip 10.10.30.0 0.0.0.255 10.10.20.0 0.0.0.255 log
access-list 110 permit ip any any

! Public WiFi/Access Restrictions - Allow basic services only
access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 80
access-list 120 permit tcp 10.10.20.0 0.0.0.255 any eq 443
access-list 120 permit udp 10.10.20.0 0.0.0.255 10.10.10.10 0.0.0.0 eq 53
access-list 120 permit tcp 10.10.20.0 0.0.0.255 10.10.10.30 0.0.0.0 eq 25
access-list 120 deny ip 10.10.20.0 0.0.0.255 10.10.30.0 0.0.0.255 log
access-list 120 permit ip any any

! Apply ACLs to subinterfaces
interface GigabitEthernet0/0.30
 ip access-group 110 in

interface GigabitEthernet0/0.20
 ip access-group 120 in

exit
write memory
```

---

### STEP 2: Configure City-Core-Switch

**Device Name in Packet Tracer:** Look for the switch labeled "City-Core-Switch"

#### How to Access City-Core-Switch CLI:
1. In Packet Tracer workspace, **click on "City-Core-Switch"** device
2. A window pops up
3. **Click the "CLI" tab** at the top
4. Paste the commands below into the black CLI screen

#### 2.1 City-Core-Switch Configuration - Copy and Paste:

```cisco
enable
configure terminal
hostname City-Core-Switch

! Create VLANs
vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management

! Configure trunk to router (adjust interface as needed)
interface GigabitEthernet0/1
 description "Trunk to SmartCity-Router"
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

! Configure trunks to other switches
! Adjust interface numbers based on your topology
interface GigabitEthernet0/2
 description "Trunk to Downtown-Switch"
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown

interface GigabitEthernet0/3
 description "Trunk to Park-Switch"
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30,99
 no shutdown

interface GigabitEthernet0/4
 description "Trunk to Residential-Switch"
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown

! Server connections (VLAN 10)
interface range FastEthernet0/1-4
 description "Servers - VLAN 10"
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown

exit
write memory
```

#### 2.2 Configure Downtown-Switch

**Device Name in Packet Tracer:** Look for "Downtown-Switch"

**How to access:** Click "Downtown-Switch" → Click "CLI" tab → Paste commands below:

```cisco
enable
configure terminal
hostname Downtown-Switch

vlan 20
 name Public
vlan 99
 name Management

! Trunk to core
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 20,99
 no shutdown

! Public access ports
interface range FastEthernet0/1-10
 description "Public Access - VLAN 20"
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown

exit
write memory
```

#### 2.3 Configure Park-Switch

**Device Name in Packet Tracer:** Look for "Park-Switch"

**How to access:** Click "Park-Switch" → Click "CLI" tab → Paste commands below:

```cisco
enable
configure terminal
hostname Park-Switch

vlan 30
 name IoT
vlan 99
 name Management

! Trunk to core
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 30,99
 no shutdown

! IoT device ports
interface range FastEthernet0/1-10
 description "IoT Devices - VLAN 30"
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown

exit
write memory
```

#### 2.4 Configure Residential-Switch

**Device Name in Packet Tracer:** Look for "Residential-Switch"

**How to access:** Click "Residential-Switch" → Click "CLI" tab → Paste commands below:

```cisco
enable
configure terminal
hostname Residential-Switch

vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 99
 name Management

! Trunk to core
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown

! Admin PCs (VLAN 10)
interface range FastEthernet0/1-5
 description "Admin PCs - VLAN 10"
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown

! Residential/Public (VLAN 20)
interface range FastEthernet0/6-10
 description "Residential - VLAN 20"
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown

exit
write memory
```

---

### STEP 3: Configure Servers

#### 3.1 Configure DNS-Server (IP: 10.10.10.10)

**Device Name in Packet Tracer:** Look for the server labeled "DNS-Server"

**How to configure:**
1. In Packet Tracer, **click on "DNS-Server"** device (server icon)
2. A window pops up with tabs at the top
3. **Click the "Desktop" tab**
4. Click **"IP Configuration"** from the menu

**Set IP Address:**
- **IP Address:** 10.10.10.10
- **Subnet Mask:** 255.255.255.0
- **Default Gateway:** 10.10.10.1
- **DNS Server:** 10.10.10.10

**Now configure DNS service:**
1. Still in DNS-Server window, **click "Services" tab** (at the top)
2. On the left menu, click **"DNS"**
- Turn DNS Service **ON**

Add DNS Records:
```
Name: smartcity-router.local      Type: A    Address: 10.10.10.1
Name: dns.smartcity.local          Type: A    Address: 10.10.10.10
Name: dhcp.smartcity.local         Type: A    Address: 10.10.10.20
Name: web.smartcity.local          Type: A    Address: 10.10.10.40
Name: mail.smartcity.local         Type: A    Address: 10.10.10.30
Name: admin1.smartcity.local       Type: A    Address: 10.10.10.100
Name: kiosk.smartcity.local        Type: A    Address: 10.10.20.100
```

#### 3.2 Configure DHCP-Server (IP: 10.10.10.20)

**Device Name in Packet Tracer:** Look for "DHCP-Server"

**How to configure:**
1. **Click on "DHCP-Server"** device
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**

**Set IP Address:**
- **IP Address:** 10.10.10.20
- **Subnet Mask:** 255.255.255.0
- **Default Gateway:** 10.10.10.1
- **DNS Server:** 10.10.10.10

**Now configure DHCP service:**
1. Still in DHCP-Server window, **click "Services" tab**
2. On the left menu, click **"DHCP"**
- Turn DHCP Service **ON**

**Pool 1: Admin/Server VLAN**
- **Pool Name:** AdminPool
- **Default Gateway:** 10.10.10.1
- **DNS Server:** 10.10.10.10
- **Start IP Address:** 10.10.10.100
- **Subnet Mask:** 255.255.255.0
- **Maximum Users:** 50
- Click **Add**

**Pool 2: Public VLAN**
- **Pool Name:** PublicPool
- **Default Gateway:** 10.10.20.1
- **DNS Server:** 10.10.10.10
- **Start IP Address:** 10.10.20.100
- **Subnet Mask:** 255.255.255.0
- **Maximum Users:** 100
- Click **Add**

**Pool 3: IoT VLAN**
- **Pool Name:** IoTPool
- **Default Gateway:** 10.10.30.1
- **DNS Server:** 10.10.10.10
- **Start IP Address:** 10.10.30.100
- **Subnet Mask:** 255.255.255.0
- **Maximum Users:** 50
- Click **Add**

#### 3.3 Configure Web-Server (IP: 10.10.10.40)

**Device Name in Packet Tracer:** Look for "Web-Server"

**How to configure:**
1. **Click on "Web-Server"** device
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**

**Set IP Address:**
- **IP Address:** 10.10.10.40
- **Subnet Mask:** 255.255.255.0
- **Default Gateway:** 10.10.10.1
- **DNS Server:** 10.10.10.10

**Now configure Web service:**
1. Still in Web-Server window, **click "Services" tab**
2. On the left menu, click **"HTTP"**
- Turn HTTP Service **ON**
- Turn HTTPS Service **ON** (if available)

**Edit index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart City Portal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f0f8ff;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .info-box {
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .services {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .service {
            background-color: #3498db;
            color: white;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            min-width: 150px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Welcome to Smart City Network</h1>

    <div class="info-box">
        <h2>Network Information</h2>
        <p><strong>Web Server:</strong> 10.10.10.40</p>
        <p><strong>DNS Server:</strong> 10.10.10.10</p>
        <p><strong>Mail Server:</strong> 10.10.10.30</p>
        <p><strong>Status:</strong> All Systems Operational</p>
    </div>

    <div class="info-box">
        <h2>Available Services</h2>
        <div class="services">
            <div class="service">DNS Resolution</div>
            <div class="service">DHCP Assignment</div>
            <div class="service">Email Services</div>
            <div class="service">Web Hosting</div>
            <div class="service">IoT Management</div>
        </div>
    </div>

    <div class="info-box">
        <h2>Network Zones</h2>
        <p><strong>VLAN 10:</strong> Admin & Servers (10.10.10.0/24)</p>
        <p><strong>VLAN 20:</strong> Public Access (10.10.20.0/24)</p>
        <p><strong>VLAN 30:</strong> IoT Devices (10.10.30.0/24)</p>
    </div>

    <div class="info-box" style="text-align: center; background-color: #2ecc71; color: white;">
        <h3>Smart City Network - Fully Operational</h3>
        <p>Powered by Cisco Packet Tracer</p>
    </div>
</body>
</html>
```

**Create additional page - services.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart City Services</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #ecf0f1;
        }
        h1 {
            color: #16a085;
            text-align: center;
        }
        .service-list {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .service-item {
            border-left: 4px solid #16a085;
            padding: 10px;
            margin: 10px 0;
            background-color: #f8f9fa;
        }
    </style>
</head>
<body>
    <h1>Smart City Services Directory</h1>

    <div class="service-list">
        <div class="service-item">
            <h3>DNS Service</h3>
            <p>Server: 10.10.10.10 | Domain: smartcity.local</p>
        </div>

        <div class="service-item">
            <h3>DHCP Service</h3>
            <p>Server: 10.10.10.20 | Auto IP Assignment</p>
        </div>

        <div class="service-item">
            <h3>Email Service</h3>
            <p>Server: 10.10.10.30 | SMTP Available</p>
        </div>

        <div class="service-item">
            <h3>Web Portal</h3>
            <p>Server: 10.10.10.40 | HTTP/HTTPS Enabled</p>
        </div>
    </div>

    <div style="text-align: center; margin-top: 30px;">
        <a href="index.html">Back to Home</a>
    </div>
</body>
</html>
```

#### 3.4 Configure SMTP-Server (Email Server - IP: 10.10.10.30)

**Device Name in Packet Tracer:** Look for "SMTP-Server"

**How to configure:**
1. **Click on "SMTP-Server"** device
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**

**Set IP Address:**
- **IP Address:** 10.10.10.30
- **Subnet Mask:** 255.255.255.0
- **Default Gateway:** 10.10.10.1
- **DNS Server:** 10.10.10.10

**Now configure Email service:**
1. Still in SMTP-Server window, **click "Services" tab**
2. On the left menu, click **"EMAIL"**
- Turn Email Service **ON**
- **Domain Name:** smartcity.local

**Add Users:**
```
Username: admin          Password: admin123
Username: operations     Password: ops123
Username: support        Password: support123
Username: public         Password: public123
```

---

### STEP 4: Configure Client PCs

#### 4.1 Configure Admin-PC-1 and Admin-PC-2

**Device Names in Packet Tracer:** "Admin-PC-1" and "Admin-PC-2"

**How to configure (do for BOTH Admin PCs):**
1. **Click on "Admin-PC-1"** device (PC icon)
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**
- Select **DHCP**
- Verify they receive IPs in range 10.10.10.100+
- Set DNS to 10.10.10.10

#### 4.2 Configure Public-Kiosk-PC

**Device Name in Packet Tracer:** "Public-Kiosk-PC"

**How to configure:**
1. **Click on "Public-Kiosk-PC"** device
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**
- Select **DHCP**
- Verify receives IP in range 10.10.20.100+
- Set DNS to 10.10.10.10

#### 4.3 Configure Resident-Home-PC

**Device Name in Packet Tracer:** "Resident-Home-PC"

**How to configure:**
1. **Click on "Resident-Home-PC"** device
2. **Click "Desktop" tab**
3. Click **"IP Configuration"**
- Select **DHCP**
- Verify receives IP in range 10.10.20.100+
- Set DNS to 10.10.10.10

---

### STEP 5: Testing & Verification

#### Test 1: Connectivity Tests

**From Admin-PC-1:**
```
ping 10.10.10.1          (Router - should work)
ping 10.10.10.10         (DNS - should work)
ping 10.10.10.20         (DHCP - should work)
ping 10.10.10.40         (Web - should work)
ping 10.10.10.30         (SMTP - should work)
ping 10.10.20.1          (VLAN 20 gateway - should work)
ping 10.10.30.1          (VLAN 30 gateway - should work)
```

**From Public-Kiosk-PC:**
```
ping 10.10.20.1          (Gateway - should work)
ping 10.10.10.40         (Web Server - should work)
ping 10.10.10.30         (SMTP - should work via ACL)
ping 10.10.10.10         (DNS - should work via ACL)
ping 10.10.30.100        (IoT device - should FAIL - ACL blocks)
```

#### Test 2: DNS Resolution

**From any PC:**
- Desktop → Command Prompt
```
nslookup web.smartcity.local
nslookup mail.smartcity.local
nslookup dns.smartcity.local
```

Should resolve to correct IPs.

#### Test 3: Web Access

**From any PC:**
- Desktop → Web Browser
- Enter: `http://10.10.10.40` or `http://web.smartcity.local`
- Should display Smart City Portal webpage
- Test navigation to services.html

#### Test 4: Email Test

**From Admin-PC-1:**
- Desktop → Email
- Configure Email Client:
  - Email: admin@smartcity.local
  - Incoming/Outgoing Mail Server: 10.10.10.30 or mail.smartcity.local
  - Username: admin
  - Password: admin123

**Send Test Email:**
- To: operations@smartcity.local
- Subject: Test Email
- Message: Testing email functionality

**From Admin-PC-2:**
- Configure email for operations@smartcity.local
- Check inbox for test email
- Reply to confirm two-way communication

#### Test 5: DHCP Verification

**From any PC with DHCP:**
- Desktop → Command Prompt
```
ipconfig /all
```

Verify:
- IP address in correct range
- Correct gateway
- DNS server = 10.10.10.10

**Release and renew:**
```
ipconfig /release
ipconfig /renew
```

Verify new IP is assigned.

#### Test 6: ACL Security Test

**From Public-Kiosk-PC (VLAN 20):**
```
ping 10.10.30.100        (Should FAIL - ACL blocks Public to IoT)
```

**From IoT device (if configured in VLAN 30):**
```
ping 10.10.20.100        (Should FAIL - ACL blocks IoT to Public)
ping 10.10.10.10         (Should WORK - IoT can access servers)
```

---

### STEP 6: Packet Simulation Test

#### PDU Test (Simple PDU)

1. Click **Add Simple PDU** (envelope icon)
2. Click source device (e.g., Admin-PC-1)
3. Click destination device (e.g., Web-Server)
4. Click **Simulation Mode** (stopwatch icon)
5. Click **Play** to watch packet traverse network
6. Verify packet successfully reaches destination

#### Complex PDU Test (Specific Protocols)

1. Click **Add Complex PDU**
2. **HTTP Test:**
   - Source: Public-Kiosk-PC
   - Destination: Web-Server (10.10.10.40)
   - Service: HTTP
   - Click Create PDU
   - Run simulation

3. **DNS Test:**
   - Source: Any PC
   - Destination: DNS-Server (10.10.10.10)
   - Service: DNS
   - Click Create PDU
   - Run simulation

4. **Email Test:**
   - Source: Admin-PC-1
   - Destination: SMTP-Server (10.10.10.30)
   - Service: SMTP
   - Click Create PDU
   - Run simulation

---

## Summary Checklist

### Router ✓
- [ ] IPv6 enabled
- [ ] Subinterfaces for VLANs 10, 20, 30 configured
- [ ] IP helper-addresses configured
- [ ] ACL 110 (IoT security) created and applied
- [ ] ACL 120 (Public restrictions) created and applied

### Switches ✓
- [ ] VLANs 10, 20, 30, 99 created on all switches
- [ ] Trunk ports configured
- [ ] Access ports assigned to correct VLANs
- [ ] Spanning-tree portfast enabled on access ports

### Servers ✓
- [ ] DNS server configured with records
- [ ] DHCP server configured with 3 pools
- [ ] Web server with HTML pages
- [ ] SMTP server with user accounts

### Testing ✓
- [ ] Inter-VLAN routing works
- [ ] DHCP assigns IPs correctly
- [ ] DNS resolves names
- [ ] Web pages accessible
- [ ] Email send/receive works
- [ ] ACLs block traffic correctly
- [ ] PDU simulations successful

---

## Troubleshooting Tips

**No DHCP Assignment:**
- Check `ip helper-address` on router subinterfaces
- Verify DHCP pools on server match VLANs
- Check client is set to DHCP mode

**Can't access other VLANs:**
- Verify router subinterfaces are `no shutdown`
- Check trunk ports allow all VLANs
- Verify IP addresses are correct

**DNS not resolving:**
- Check DNS service is ON
- Verify DNS server IP in client configuration
- Confirm DNS records are added

**Webpage not loading:**
- Check HTTP service is ON
- Verify web server IP
- Test with IP address first, then DNS name

**Email not working:**
- Verify SMTP service is ON
- Check user accounts exist
- Confirm email client settings match server

**ACLs too restrictive:**
- Review ACL rules with `show access-lists`
- Remember: ACLs have implicit deny at end
- Check ACL is applied to correct interface/direction

---

**Completion Time Estimate:** 45-60 minutes

Good luck! Your Smart City network will be fully operational after these steps.
