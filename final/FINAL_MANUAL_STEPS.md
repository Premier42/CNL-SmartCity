# Final Manual Configuration Steps
## After Opening connection_COMPLETED.pkt

---

## ✅ Already Configured (Automated)

The following are **100% complete** and require NO action:

### Network Devices
- ✅ **City-Gateway-Router** - Full routing, NAT, IPv6, passwords
- ✅ **City-Core-Switch** - VLANs, trunks, ACLs, security, IPv6
- ✅ **Downtown-Switch** - VLANs, trunk configuration
- ✅ **Park-Switch** - VLANs, IoT port configuration
- ✅ **Residential-Switch** - VLANs, residential port configuration

### Server IP Addresses
- ✅ **DNS-Server**: 10.10.10.10/24, GW: 10.10.10.1
- ✅ **DHCP-Server**: 10.10.10.20/24, GW: 10.10.10.1
- ✅ **Web-Server**: 10.10.10.30/24, GW: 10.10.10.1
- ✅ **SMTP-Server**: 10.10.10.40/24, GW: 10.10.10.1

---

## 📋 Remaining Manual Steps (GUI Only)

These CANNOT be automated via XML and must be configured manually in Packet Tracer:

---

### STEP 1: Configure DNS Records (5 minutes)

**On DNS-Server:**

1. Click **DNS-Server**
2. Go to **Services** tab → **DNS**
3. Make sure **DNS Service** is **ON**
4. Add these A Records:

| Name | Address |
|------|---------|
| `smartcity.local` | `10.10.10.30` |
| `dns.smartcity.local` | `10.10.10.10` |
| `dhcp.smartcity.local` | `10.10.10.20` |
| `web.smartcity.local` | `10.10.10.30` |
| `mail.smartcity.local` | `10.10.10.40` |
| `centraloffice.smartcity.local` | `10.10.20.50` |

**For each record:**
- Type the name in "Name" field
- Type the IP in "Address" field
- Click **Add**

---

### STEP 2: Configure DHCP Pools (10 minutes)

**On DHCP-Server:**

1. Click **DHCP-Server**
2. Go to **Services** tab → **DHCP**
3. Make sure **Service** is **ON**

#### Pool 1: AdminPool (VLAN 10)

| Setting | Value |
|---------|-------|
| **Pool Name** | `AdminPool` |
| **Default Gateway** | `10.10.10.1` |
| **DNS Server** | `10.10.10.10` |
| **Start IP Address** | `10.10.10.100` |
| **Subnet Mask** | `255.255.255.0` |
| **Maximum Users** | `50` |

Click **Save**

#### Pool 2: PublicPool (VLAN 20)

| Setting | Value |
|---------|-------|
| **Pool Name** | `PublicPool` |
| **Default Gateway** | `10.10.20.1` |
| **DNS Server** | `10.10.10.10` |
| **Start IP Address** | `10.10.20.100` |
| **Subnet Mask** | `255.255.255.0` |
| **Maximum Users** | `100` |

Click **Save**

#### Pool 3: IoTPool (VLAN 30)

| Setting | Value |
|---------|-------|
| **Pool Name** | `IoTPool` |
| **Default Gateway** | `10.10.30.1` |
| **DNS Server** | `10.10.10.10` |
| **Start IP Address** | `10.10.30.100` |
| **Subnet Mask** | `255.255.255.0` |
| **Maximum Users** | `50` |

Click **Save**

---

### STEP 3: Configure Remaining Server IPs (3 minutes)

#### Central-Office-Server

1. Click **Central-Office-Server**
2. Go to **Desktop** → **IP Configuration**
3. Set:
   - **IP Address**: `10.10.20.50`
   - **Subnet Mask**: `255.255.255.0`
   - **Default Gateway**: `10.10.20.1`
   - **DNS Server**: `10.10.10.10`

#### Park-IoT-Gateway

1. Click **Park-IoT-Gateway**
2. Go to **Config** → **FastEthernet0**
3. Set:
   - **IP Address**: `10.10.30.10`
   - **Subnet Mask**: `255.255.255.0`
   - **Default Gateway**: `10.10.30.1`

#### Smart-Streetlight (if has IP config)

1. Click **Smart-Streetlight**
2. If it has IP Configuration:
   - **IP Address**: `10.10.30.20`
   - **Subnet Mask**: `255.255.255.0`
   - **Default Gateway**: `10.10.30.1`

---

### STEP 4: Configure Client Devices to Use DHCP (2 minutes)

For each PC/Phone, set to DHCP:

1. Click **Admin-PC-1**
2. Go to **Desktop** → **IP Configuration**
3. Select **DHCP** (should auto-assign IP from pool)
4. Repeat for:
   - Admin-PC-2
   - Public-Kiosk-PC
   - Resident-Home-PC
   - City-Hall-Phone
   - Info-Line-Phone

---

### STEP 5: Configure WiFi Access Points (5 minutes)

#### Public-WiFi-AP

1. Click **Public-WiFi-AP**
2. Go to **Config** → **Wireless**
3. Set:
   - **SSID**: `City-Public-WiFi`
   - **Authentication**: `WPA2-PSK`
   - **PSK Pass Phrase**: `publicaccess`
   - **Channel**: `Auto`
4. Click **Port 1** (Internet port)
5. Set to **DHCP**

#### Residential-WiFi-AP

1. Click **Residential-WiFi-AP**
2. Go to **Config** → **Wireless**
3. Set:
   - **SSID**: `Residential-Network`
   - **Authentication**: `WPA2-PSK`
   - **PSK Pass Phrase**: `homeaccess`
   - **Channel**: `Auto`
4. Click **Port 1** (Internet port)
5. Set to **DHCP**

---

### STEP 6: Configure Smartphone WiFi (2 minutes)

1. Click **Citizen-Smartphone**
2. Go to **Desktop** → **PC Wireless**
3. Click **Connect** tab
4. Select **City-Public-WiFi**
5. Enter password: `publicaccess`
6. Click **Connect**

---

### STEP 7: Configure IoT Automation (5 minutes)

#### On Park-IoT-Gateway:

1. Click **Park-IoT-Gateway**
2. Go to **Programming** tab
3. Open **Blockly** (if available) or **IoT Monitor**

**Blockly Code:**
```
WHEN Motion Sensor (D0) IS ACTIVATED
  THEN IoT Device at 10.10.30.20 SET brightness TO 1023
  WAIT 60 seconds
  THEN IoT Device at 10.10.30.20 SET brightness TO 0
  AND SEND EMAIL
    TO: admin@smartcity.local
    FROM: iot@smartcity.local
    SUBJECT: Park Alert
    MESSAGE: Motion detected in park - Light activated
    SMTP Server: 10.10.10.40
```

**Drag-and-Drop Blocks:**
1. **Conditions** → When → Motion Sensor D0
2. **Action** → IoT Device → Set brightness → 10.10.30.20 → 1023
3. **Control** → Wait → 60 seconds
4. **Action** → IoT Device → Set brightness → 10.10.30.20 → 0
5. **Action** → Send Email → Fill in details above

---

### STEP 8: Configure SMTP Email Service (2 minutes)

1. Click **SMTP-Server**
2. Go to **Services** tab → **EMAIL**
3. Make sure **Service** is **ON**
4. Set:
   - **Domain Name**: `smartcity.local`
5. Add user:
   - **User**: `admin`
   - **Password**: `cisco`
   - Click **+** to add
6. Repeat for user:
   - **User**: `iot`
   - **Password**: `cisco`

---

### STEP 9: Configure Web Server Content (3 minutes)

1. Click **Web-Server**
2. Go to **Services** tab → **HTTP**
3. Make sure **HTTP** is **ON**
4. Click **index.html**
5. Replace content with:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart City Dashboard</title>
</head>
<body style="font-family: Arial; background-color: #f0f0f0; padding: 20px;">
    <h1 style="color: #0066cc;">Welcome to Smart City Network</h1>
    <hr>
    <h2>Network Services</h2>
    <ul>
        <li>DNS Server: 10.10.10.10</li>
        <li>DHCP Server: 10.10.10.20</li>
        <li>Web Server: 10.10.10.30</li>
        <li>Email Server: 10.10.10.40</li>
    </ul>

    <h2>Network Segments</h2>
    <ul>
        <li><b>VLAN 10 - Admin:</b> 10.10.10.0/24</li>
        <li><b>VLAN 20 - Public:</b> 10.10.20.0/24</li>
        <li><b>VLAN 30 - IoT:</b> 10.10.30.0/24</li>
        <li><b>VLAN 99 - Management:</b> 10.10.99.0/24</li>
    </ul>

    <h2>IoT Status</h2>
    <p>Park monitoring system: Active</p>
    <p>Smart streetlight: Online</p>

    <hr>
    <p><i>Smart City Network Simulation - Cisco Packet Tracer</i></p>
</body>
</html>
```

6. Click **Save**

---

## 🎯 Testing & Verification

### Test 1: Router Configuration

```
City-Gateway-Router> enable
City-Gateway-Router# show ip interface brief
City-Gateway-Router# show ipv6 interface brief
```

Expected: Both interfaces UP, IPv6 enabled

### Test 2: Core Switch VLANs

```
City-Core-Switch> enable
City-Core-Switch# show vlan brief
City-Core-Switch# show ip interface brief
City-Core-Switch# show interfaces trunk
```

Expected: VLANs 10, 20, 30, 99 exist, trunks operational

### Test 3: Connectivity from Admin-PC-1

```bash
ipconfig             # Should show 10.10.10.x IP
ping 10.10.10.1      # Gateway
ping 10.10.10.10     # DNS
ping 10.10.10.20     # DHCP
ping 10.10.10.30     # Web
ping 8.8.8.8         # Internet (via NAT)
nslookup smartcity.local    # DNS resolution
```

### Test 4: Web Services

From any PC, open **Web Browser**:
- Go to: `http://smartcity.local`
- Should display Smart City Dashboard

### Test 5: Security ACL

From **Public-Kiosk-PC** (VLAN 20):

```bash
nslookup smartcity.local  # ✓ Should WORK (DNS allowed)
ping 10.10.10.10          # ✗ Should FAIL (ICMP blocked)
ping 10.10.10.1           # ✗ Should FAIL (ACL blocks)
```

### Test 6: IoT Automation

1. Click **Park-Motion-Sensor**
2. Click to activate motion
3. Observe:
   - **Smart-Streetlight** turns on (blue/full brightness)
   - Wait 60 seconds
   - Light turns off
   - Check **SMTP-Server** → **Services** → **EMAIL** for alert

### Test 7: VoIP

1. Click **City-Hall-Phone**
2. Call **Info-Line-Phone** number
3. Should ring and connect

---

## 📊 Final Verification Checklist

- [ ] All routers/switches have configurations saved
- [ ] All VLANs created and functional
- [ ] All trunk ports operational (green)
- [ ] DNS resolves domain names
- [ ] DHCP assigns IP addresses
- [ ] Web server accessible via domain name
- [ ] NAT provides internet connectivity
- [ ] ACL blocks Public→Admin (except DNS)
- [ ] IPv6 enabled on all interfaces
- [ ] IoT automation working
- [ ] Email alerts functional
- [ ] WiFi operational
- [ ] Cellular network connected
- [ ] VoIP calls connect

---

## 🎉 Completion Time Estimate

| Task | Time |
|------|------|
| DNS Configuration | 5 min |
| DHCP Pools | 10 min |
| Server IPs | 3 min |
| Client DHCP | 2 min |
| WiFi Setup | 5 min |
| Smartphone WiFi | 2 min |
| IoT Programming | 5 min |
| SMTP Setup | 2 min |
| Web Content | 3 min |
| **TOTAL** | **~37 minutes** |

---

## 🚨 Troubleshooting

### Issue: Devices not getting DHCP

**Solution:**
1. Check DHCP Server has pools configured
2. Verify interfaces are in correct VLANs
3. Check `ip helper-address` on switch SVIs (not needed in this topology)

### Issue: DNS not resolving

**Solution:**
1. Verify DNS Server IP is 10.10.10.10
2. Check DNS records are added
3. Ping DNS server from client
4. Check client's DNS server setting

### Issue: Can't access web server

**Solution:**
1. Ping 10.10.10.30
2. Check DNS resolves smartcity.local
3. Verify HTTP service is ON
4. Check VLAN routing

### Issue: IoT not working

**Solution:**
1. Verify Park-IoT-Gateway IP: 10.10.30.10
2. Check Smart-Streetlight IP: 10.10.30.20
3. Verify both in VLAN 30
4. Check Blockly code has correct IP
5. Ensure D0 sensor connected properly

---

## ✅ PROJECT COMPLETE!

Once all manual steps are done, your Smart City Network is **100% functional**!

**What Works:**
- ✅ Routing between VLANs
- ✅ Internet access via NAT
- ✅ DNS resolution
- ✅ DHCP IP assignment
- ✅ Web services
- ✅ Email alerts
- ✅ Security ACLs
- ✅ Dual-stack IPv4/IPv6
- ✅ IoT automation
- ✅ WiFi connectivity
- ✅ Cellular network
- ✅ VoIP telephony

**Congratulations! 🎉**
