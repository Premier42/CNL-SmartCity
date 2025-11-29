# Smart City Network - Quick Reference Card

---

## 📁 THE FILE YOU NEED

```
connection_COMPLETED.pkt
```

**Location:** `/home/shinzuu/Documents/CNL-SmartCity/final/`

---

## ✅ What's Already Done (95%)

| Device | Status | Configuration |
|--------|--------|---------------|
| City-Gateway-Router | ✅ 100% | Full routing, NAT, IPv6 |
| City-Core-Switch | ✅ 100% | VLANs, trunks, ACLs, IPv6 |
| Downtown-Switch | ✅ 100% | VLANs, trunk |
| Park-Switch | ✅ 100% | VLANs, IoT ports |
| Residential-Switch | ✅ 100% | VLANs, ports |
| DNS-Server | ✅ 100% | IP: 10.10.10.10 |
| DHCP-Server | ✅ 100% | IP: 10.10.10.20 |
| Web-Server | ✅ 100% | IP: 10.10.10.30 |
| SMTP-Server | ✅ 100% | IP: 10.10.10.40 |

---

## 📝 What You Need to Do (5% - 37 minutes)

### Quick Checklist

- [ ] **DNS Records** (5 min) - Add 6 records on DNS-Server
- [ ] **DHCP Pools** (10 min) - Create 3 pools on DHCP-Server
- [ ] **Other IPs** (3 min) - Central Office + IoT Gateway
- [ ] **Client DHCP** (2 min) - Enable on all PCs/Phones
- [ ] **WiFi Setup** (5 min) - Configure 2 access points
- [ ] **Smartphone** (2 min) - Connect to WiFi
- [ ] **IoT Code** (5 min) - Blockly programming
- [ ] **Email Setup** (2 min) - Create SMTP users
- [ ] **Web Content** (3 min) - Update index.html

**Detailed Steps:** See `FINAL_MANUAL_STEPS.md`

---

## 🔑 Key Information

### Credentials

| Device | Password |
|--------|----------|
| All Routers/Switches | `cisco` (line password) |
| All Routers/Switches | `class` (enable secret) |
| SMTP Users | `cisco` |

### IP Addresses

| Device | IP | VLAN |
|--------|----|------|
| Router LAN | 10.0.0.1/30 | - |
| Core Switch (to Router) | 10.0.0.2/30 | - |
| VLAN 10 Gateway | 10.10.10.1 | Admin |
| VLAN 20 Gateway | 10.10.20.1 | Public |
| VLAN 30 Gateway | 10.10.30.1 | IoT |
| VLAN 99 Gateway | 10.10.99.1 | Management |
| DNS | 10.10.10.10 | 10 |
| DHCP | 10.10.10.20 | 10 |
| Web | 10.10.10.30 | 10 |
| SMTP | 10.10.10.40 | 10 |
| Central Office | 10.10.20.50 | 20 |
| IoT Gateway | 10.10.30.10 | 30 |
| Smart LED | 10.10.30.20 | 30 |

### DHCP Pools

| Pool | Network | Range | Gateway | DNS |
|------|---------|-------|---------|-----|
| AdminPool | 10.10.10.0/24 | .100-.150 | 10.10.10.1 | 10.10.10.10 |
| PublicPool | 10.10.20.0/24 | .100-.200 | 10.10.20.1 | 10.10.10.10 |
| IoTPool | 10.10.30.0/24 | .100-.150 | 10.10.30.1 | 10.10.10.10 |

### WiFi Credentials

| AP | SSID | Password |
|----|------|----------|
| Public-WiFi-AP | City-Public-WiFi | `publicaccess` |
| Residential-WiFi-AP | Residential-Network | `homeaccess` |

### DNS Records

| Name | IP |
|------|----|
| smartcity.local | 10.10.10.30 |
| dns.smartcity.local | 10.10.10.10 |
| dhcp.smartcity.local | 10.10.10.20 |
| web.smartcity.local | 10.10.10.30 |
| mail.smartcity.local | 10.10.10.40 |
| centraloffice.smartcity.local | 10.10.20.50 |

---

## 🧪 Quick Tests

### Test 1: Router Config
```
enable
show running-config
```
Should see: hostname, interfaces, NAT, routes

### Test 2: Core Switch VLANs
```
enable
show vlan brief
```
Should see: VLANs 10, 20, 30, 99

### Test 3: Connectivity
From any PC:
```
ipconfig           # Should show IP from DHCP
ping 10.10.10.1    # Gateway
ping 8.8.8.8       # Internet
nslookup smartcity.local
```

### Test 4: Web Access
Open browser → `http://smartcity.local`

### Test 5: Security
From Public-Kiosk-PC:
```
nslookup smartcity.local  # ✓ Should work
ping 10.10.10.10          # ✗ Should fail
```

### Test 6: IoT
Click motion sensor → LED lights up → waits 60s → LED off → email sent

---

## 📱 IoT Blockly Code (Copy-Paste)

```
WHEN Motion Sensor D0 IS ACTIVATED
  THEN IoT Device 10.10.30.20 SET brightness TO 1023
  WAIT 60 seconds
  THEN IoT Device 10.10.30.20 SET brightness TO 0
  AND SEND EMAIL
    TO: admin@smartcity.local
    FROM: iot@smartcity.local
    SUBJECT: Park Alert
    MESSAGE: Motion detected - Light activated
    SMTP: 10.10.10.40
```

---

## 🌐 Web Server HTML (Copy-Paste)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart City Dashboard</title>
</head>
<body style="font-family: Arial; background: #f0f0f0; padding: 20px;">
    <h1 style="color: #0066cc;">Smart City Network</h1>
    <hr>
    <h2>Services</h2>
    <ul>
        <li>DNS: 10.10.10.10</li>
        <li>DHCP: 10.10.10.20</li>
        <li>Web: 10.10.10.30</li>
        <li>Email: 10.10.10.40</li>
    </ul>
    <h2>VLANs</h2>
    <ul>
        <li><b>Admin:</b> 10.10.10.0/24</li>
        <li><b>Public:</b> 10.10.20.0/24</li>
        <li><b>IoT:</b> 10.10.30.0/24</li>
    </ul>
    <hr>
    <p><i>Smart City Simulation - Packet Tracer</i></p>
</body>
</html>
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| No DHCP | Check pools configured on DHCP-Server |
| No DNS | Check records added on DNS-Server |
| No internet | Check NAT on router (`show ip nat translations`) |
| ACL too strict | Verify DNS permit rules exist |
| IoT not working | Check IPs: Gateway=10.10.30.10, LED=10.10.30.20 |
| WiFi not connecting | Check SSID and password match |
| Trunk not working | Check VLAN allowed list on trunk ports |

---

## ⏱️ Time Breakdown

| Phase | Time |
|-------|------|
| Automation (Already Done) | 0 minutes ✅ |
| DNS Setup | 5 minutes |
| DHCP Setup | 10 minutes |
| Other Configs | 22 minutes |
| **TOTAL** | **37 minutes** |

---

## 📊 Success = All Green

- ✅ Router configured
- ✅ Core switch has VLANs
- ✅ Trunks operational
- ✅ Servers have IPs
- ✅ DHCP works
- ✅ DNS resolves
- ✅ Web accessible
- ✅ ACL blocks properly
- ✅ IoT automation works
- ✅ Email alerts sent
- ✅ WiFi connects
- ✅ VoIP calls work

---

**🚀 Ready? Open `connection_COMPLETED.pkt` and go!**
