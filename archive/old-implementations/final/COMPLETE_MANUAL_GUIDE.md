# Complete Manual Configuration Guide
## Smart City Network - Step-by-Step

---

## ⚠️ IMPORTANT: Use This File

**Open:** `connection_COMPLETED.pkt` (the 95% version that actually works)

The enhanced version didn't apply server configurations properly. Follow this guide instead.

---

## 📋 COMPLETE CHECKLIST

### ✅ Already Done (Automated - 95%)
- [x] City-Gateway-Router configured
- [x] City-Core-Switch configured
- [x] Downtown-Switch configured
- [x] Park-Switch configured
- [x] Residential-Switch configured
- [x] DNS-Server IP: 10.10.10.10
- [x] DHCP-Server IP: 10.10.10.20
- [x] Web-Server IP: 10.10.10.30
- [x] SMTP-Server IP: 10.10.10.40

### 📝 You Need to Do Manually

---

## STEP 1: Configure Remaining Server IPs (3 minutes)

### 1.1 Central-Office-Server

1. Click **Central-Office-Server**
2. Go to **Desktop** tab
3. Click **IP Configuration**
4. Select **Static**
5. Enter:
   - **IPv4 Address:** `10.10.20.50`
   - **Subnet Mask:** `255.255.255.0`
   - **Default Gateway:** `10.10.20.1`
   - **DNS Server:** `10.10.10.10`
6. Close the window

### 1.2 Park-IoT-Gateway

1. Click **Park-IoT-Gateway**
2. Go to **Config** tab
3. Click **FastEthernet0** (in left menu)
4. Enter:
   - **IP Address:** `10.10.30.10`
   - **Subnet Mask:** `255.255.255.0`
5. Go to **Settings** → **Global Settings**
6. Enter:
   - **Default Gateway:** `10.10.30.1`
   - **DNS Server:** `10.10.10.10`
7. Close the window

### 1.3 Smart-Streetlight (if it has IP config)

1. Click **Smart-Streetlight**
2. If it has IP Configuration available:
   - **IP Address:** `10.10.30.20`
   - **Subnet Mask:** `255.255.255.0`
   - **Default Gateway:** `10.10.30.1`
3. If not, skip this (it may be IoT device without IP config)

---

## STEP 2: Configure DNS Server (5 minutes)

1. Click **DNS-Server**
2. Go to **Services** tab
3. Click **DNS** in left menu
4. Make sure **DNS Service** is **ON** (toggle to ON if OFF)
5. Add these A Records (one by one):

**Record 1:**
- Name: `smartcity.local`
- Address: `10.10.10.30`
- Click **Add**

**Record 2:**
- Name: `dns.smartcity.local`
- Address: `10.10.10.10`
- Click **Add**

**Record 3:**
- Name: `dhcp.smartcity.local`
- Address: `10.10.10.20`
- Click **Add**

**Record 4:**
- Name: `web.smartcity.local`
- Address: `10.10.10.30`
- Click **Add**

**Record 5:**
- Name: `mail.smartcity.local`
- Address: `10.10.10.40`
- Click **Add**

**Record 6:**
- Name: `centraloffice.smartcity.local`
- Address: `10.10.20.50`
- Click **Add**

6. Close the window

---

## STEP 3: Configure DHCP Server (10 minutes)

1. Click **DHCP-Server**
2. Go to **Services** tab
3. Click **DHCP** in left menu
4. Make sure **Service** is **ON** (toggle to ON if OFF)

### Pool 1: AdminPool (VLAN 10)

1. In the DHCP configuration area:
   - **Pool Name:** `AdminPool`
   - **Default Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`
   - **Start IP Address:** `10.10.10.100`
   - **Subnet Mask:** `255.255.255.0`
   - **Maximum Number of Users:** `50`
2. Click **Save**

### Pool 2: PublicPool (VLAN 20)

1. Click **Add** to create new pool
2. Enter:
   - **Pool Name:** `PublicPool`
   - **Default Gateway:** `10.10.20.1`
   - **DNS Server:** `10.10.10.10`
   - **Start IP Address:** `10.10.20.100`
   - **Subnet Mask:** `255.255.255.0`
   - **Maximum Number of Users:** `100`
3. Click **Save**

### Pool 3: IoTPool (VLAN 30)

1. Click **Add** to create new pool
2. Enter:
   - **Pool Name:** `IoTPool`
   - **Default Gateway:** `10.10.30.1`
   - **DNS Server:** `10.10.10.10`
   - **Start IP Address:** `10.10.30.100`
   - **Subnet Mask:** `255.255.255.0`
   - **Maximum Number of Users:** `50`
3. Click **Save**

4. Close the window

---

## STEP 4: Enable DHCP on Client Devices (2 minutes)

### 4.1 Admin-PC-1
1. Click **Admin-PC-1**
2. Go to **Desktop** tab
3. Click **IP Configuration**
4. Select **DHCP** (radio button)
5. Wait for IP to be assigned (should be 10.10.10.100-150)
6. Close the window

### 4.2 Admin-PC-2
1. Click **Admin-PC-2**
2. Go to **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Close the window

### 4.3 Public-Kiosk-PC
1. Click **Public-Kiosk-PC**
2. Go to **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Wait for IP (should be 10.10.20.100-200)
5. Close the window

### 4.4 Resident-Home-PC
1. Click **Resident-Home-PC**
2. Go to **Desktop** → **IP Configuration**
3. Select **DHCP**
4. Wait for IP (should be 10.10.30.100-150)
5. Close the window

---

## STEP 5: Configure WiFi Access Points (5 minutes)

### 5.1 Public-WiFi-AP

1. Click **Public-WiFi-AP**
2. Go to **Config** tab
3. Click **Wireless** in left menu (or **Port 0** if it's a wireless interface)
4. Enter:
   - **SSID:** `City-Public-WiFi`
   - **Authentication:** Select **WPA2-PSK** from dropdown
   - **PSK Pass Phrase:** `publicaccess`
   - **Encryption Type:** **AES** (if available)
   - **Channel:** Leave as **Auto** or select **6**
5. Click **Port 1** (the Internet/LAN port)
6. Set IP Configuration to **DHCP**
7. Close the window

### 5.2 Residential-WiFi-AP

1. Click **Residential-WiFi-AP**
2. Go to **Config** tab
3. Click **Wireless** in left menu
4. Enter:
   - **SSID:** `Residential-Network`
   - **Authentication:** Select **WPA2-PSK**
   - **PSK Pass Phrase:** `homeaccess`
   - **Encryption Type:** **AES** (if available)
   - **Channel:** Leave as **Auto** or select **11**
5. Click **Port 1**
6. Set IP Configuration to **DHCP**
7. Close the window

---

## STEP 6: Connect Smartphone to WiFi (2 minutes)

1. Click **Citizen-Smartphone**
2. Go to **Desktop** tab
3. Click **PC Wireless**
4. Click **Connect** tab
5. You should see **City-Public-WiFi** in the list
6. Click on **City-Public-WiFi**
7. Enter password: `publicaccess`
8. Click **Connect**
9. Wait for connection (you should see "Connected" status)
10. Close the window

---

## STEP 7: Configure SMTP Email Service (2 minutes)

1. Click **SMTP-Server**
2. Go to **Services** tab
3. Click **EMAIL** in left menu
4. Make sure **Service** is **ON**
5. Set **Domain Name:** `smartcity.local`
6. Add users:

**User 1:**
- Click in the **User** field (bottom section)
- Type: `admin`
- Click in **Password** field
- Type: `cisco`
- Click **+** button to add

**User 2:**
- **User:** `iot`
- **Password:** `cisco`
- Click **+** button to add

7. Close the window

---

## STEP 8: Configure Web Server (3 minutes)

1. Click **Web-Server**
2. Go to **Services** tab
3. Click **HTTP** in left menu
4. Make sure **HTTP** service is **ON**
5. You should see **index.html** in the file list
6. Click on **index.html** to select it
7. Click **Edit** (or double-click)
8. **DELETE ALL** existing content
9. **COPY AND PASTE** this HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart City Dashboard</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; margin: 0;">
    <div style="max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <h1 style="color: #0066cc; border-bottom: 3px solid #0066cc; padding-bottom: 10px;">Smart City Network Dashboard</h1>

        <h2 style="color: #333; margin-top: 30px;">Network Services</h2>
        <ul style="list-style-type: none; padding: 0;">
            <li style="padding: 8px; background: #e8f4f8; margin: 5px 0; border-left: 4px solid #0066cc;">
                <strong>DNS Server:</strong> 10.10.10.10
            </li>
            <li style="padding: 8px; background: #e8f4f8; margin: 5px 0; border-left: 4px solid #0066cc;">
                <strong>DHCP Server:</strong> 10.10.10.20
            </li>
            <li style="padding: 8px; background: #e8f4f8; margin: 5px 0; border-left: 4px solid #0066cc;">
                <strong>Web Server:</strong> 10.10.10.30
            </li>
            <li style="padding: 8px; background: #e8f4f8; margin: 5px 0; border-left: 4px solid #0066cc;">
                <strong>Email Server:</strong> 10.10.10.40
            </li>
        </ul>

        <h2 style="color: #333; margin-top: 30px;">VLAN Configuration</h2>
        <table style="width: 100%; border-collapse: collapse;">
            <tr style="background: #0066cc; color: white;">
                <th style="padding: 10px; text-align: left;">VLAN</th>
                <th style="padding: 10px; text-align: left;">Name</th>
                <th style="padding: 10px; text-align: left;">Network</th>
            </tr>
            <tr style="background: #f9f9f9;">
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">10</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">Admin</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">10.10.10.0/24</td>
            </tr>
            <tr style="background: #fff;">
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">20</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">Public</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">10.10.20.0/24</td>
            </tr>
            <tr style="background: #f9f9f9;">
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">30</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">IoT</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">10.10.30.0/24</td>
            </tr>
            <tr style="background: #fff;">
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">99</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">Management</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">10.10.99.0/24</td>
            </tr>
        </table>

        <h2 style="color: #333; margin-top: 30px;">IoT Devices</h2>
        <p style="color: #666;">Park Monitoring System: <span style="color: #00cc00; font-weight: bold;">Active</span></p>
        <p style="color: #666;">Smart Streetlight: <span style="color: #00cc00; font-weight: bold;">Online</span></p>

        <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
        <p style="text-align: center; color: #999; font-size: 14px;">
            <em>Smart City Network Simulation - Cisco Packet Tracer</em>
        </p>
    </div>
</body>
</html>
```

10. Click **Save** or close the editor (it should auto-save)
11. Close the window

---

## STEP 9: Program IoT Automation (5 minutes)

1. Click **Park-IoT-Gateway**
2. Go to **Programming** tab
3. Click **Blockly** (visual programming interface)

### Build this automation using drag-and-drop blocks:

**Step-by-step block placement:**

1. **From "Conditions" section:**
   - Drag **"When [sensor] is [condition]"** block
   - Set sensor to: **D0** (motion sensor)
   - Set condition to: **Activated**

2. **From "Actions" section:**
   - Drag **"Set Device [IP] [attribute] to [value]"** block
   - Attach it under the "When" block
   - Set IP: `10.10.30.20`
   - Set attribute: **brightness**
   - Set value: `1023`

3. **From "Control" section:**
   - Drag **"Wait [time] seconds"** block
   - Attach it under the previous block
   - Set time: `60`

4. **From "Actions" section:**
   - Drag another **"Set Device"** block
   - Set IP: `10.10.30.20`
   - Set attribute: **brightness**
   - Set value: `0`

5. **From "Actions" section:**
   - Drag **"Send Email"** block
   - Attach it at the end
   - Fill in:
     - **To:** `admin@smartcity.local`
     - **From:** `iot@smartcity.local`
     - **Subject:** `Park Alert`
     - **Message:** `Motion detected in park - Light activated`
     - **SMTP Server:** `10.10.10.40`

6. Click **Save** or **Run** to activate the program
7. Close the window

---

## ✅ VERIFICATION TESTS

### Test 1: Router Configuration

1. Click **City-Gateway-Router**
2. Go to **CLI** tab
3. Type:
```
enable
show running-config
```
4. You should see hostname, NAT, routing configured
5. Type `exit` and close

### Test 2: Core Switch VLANs

1. Click **City-Core-Switch**
2. Go to **CLI** tab
3. Type:
```
enable
show vlan brief
```
4. You should see VLANs: 10, 20, 30, 99
5. Type:
```
show interfaces trunk
```
6. You should see trunk ports Gig1/0/2, Gig1/0/3, Gig1/0/4
7. Type `exit` and close

### Test 3: DHCP Working

1. Click **Admin-PC-1**
2. Go to **Desktop** → **Command Prompt**
3. Type:
```
ipconfig
```
4. You should see:
   - IP Address: 10.10.10.100-150
   - Subnet Mask: 255.255.255.0
   - Default Gateway: 10.10.10.1
   - DNS Server: 10.10.10.10
5. Type `exit` and close

### Test 4: DNS Resolution

1. From **Admin-PC-1** Command Prompt:
2. Type:
```
nslookup smartcity.local
```
3. Should return: **10.10.10.30**
4. Type `exit` and close

### Test 5: Internet Connectivity (NAT)

1. From **Admin-PC-1** Command Prompt:
2. Type:
```
ping 8.8.8.8
```
3. You should get replies (this tests NAT is working)
4. Type `exit` and close

### Test 6: Web Server Access

1. Click **Admin-PC-1**
2. Go to **Desktop** → **Web Browser**
3. In the URL bar, type: `http://smartcity.local`
4. Press Enter
5. You should see the Smart City Dashboard webpage
6. Close browser and device

### Test 7: Security ACL (Public → Admin blocked)

1. Click **Public-Kiosk-PC**
2. Go to **Desktop** → **Command Prompt**
3. Type:
```
nslookup smartcity.local
```
4. Should WORK (return 10.10.10.30) ✅
5. Type:
```
ping 10.10.10.10
```
6. Should FAIL (Request timed out) ✅ This is correct! ACL is blocking.
7. Type `exit` and close

### Test 8: IoT Automation

1. Click **Park-Motion-Sensor** (the motion sensor device)
2. Click on it to activate/trigger it
3. Watch **Smart-Streetlight** - it should:
   - Turn ON (full brightness/blue color)
   - Stay ON for 60 seconds
   - Turn OFF automatically
4. Check email was sent:
   - Click **SMTP-Server**
   - Go to **Services** → **EMAIL**
   - Check if email appears in admin's mailbox
5. Close

---

## 🎉 YOU'RE DONE WHEN:

- [ ] All 9 configuration steps completed
- [ ] All 8 verification tests passed
- [ ] No red X's on network connections
- [ ] All devices show green/up status
- [ ] IoT automation works (motion → light → email)

---

## 📊 FINAL CHECKLIST

**Configured:**
- [x] 5 network devices (router + switches)
- [x] 4 main servers (DNS, DHCP, Web, SMTP)
- [ ] 2 additional servers (Central Office, IoT Gateway)
- [ ] 6 DNS records
- [ ] 3 DHCP pools
- [ ] 4 PCs set to DHCP
- [ ] 2 WiFi access points
- [ ] 1 smartphone connected
- [ ] 2 email users
- [ ] 1 web page
- [ ] 1 IoT automation

---

## 🔑 CREDENTIALS REFERENCE

| Item | Username/SSID | Password |
|------|---------------|----------|
| Router/Switch Console | - | `cisco` |
| Router/Switch Enable | - | `class` |
| Public WiFi | `City-Public-WiFi` | `publicaccess` |
| Residential WiFi | `Residential-Network` | `homeaccess` |
| Email: Admin | `admin` | `cisco` |
| Email: IoT | `iot` | `cisco` |

---

## 💡 TROUBLESHOOTING

**Problem:** DHCP not giving IPs
- **Solution:** Check DHCP pools are created and saved on DHCP-Server

**Problem:** DNS not resolving
- **Solution:** Verify all 6 DNS records are added on DNS-Server

**Problem:** Can't access website
- **Solution:**
  1. Ping 10.10.10.30 (should work)
  2. Run `nslookup smartcity.local` (should return 10.10.10.30)
  3. Check HTTP service is ON on Web-Server

**Problem:** IoT light doesn't turn on
- **Solution:**
  1. Verify Park-IoT-Gateway IP: 10.10.30.10
  2. Verify Smart-Streetlight IP: 10.10.30.20 (if configurable)
  3. Check Blockly code is saved
  4. Click motion sensor to trigger

**Problem:** WiFi not connecting
- **Solution:** Check SSID and password match exactly

---

**Total Time:** ~40 minutes for all manual steps

**Good luck! Follow each step carefully and you'll have a perfect Smart City Network!** 🚀
