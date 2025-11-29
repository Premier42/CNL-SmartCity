# START HERE - Simple Step-by-Step

## Your Mission: Complete the remaining 10% of your Smart City network

**Time needed:** 45-60 minutes
**What you'll do:** Configure router, switches, and servers to make everything work

---

## STEP-BY-STEP CHECKLIST

### ✓ Before You Start

1. Open **connection.pkt** in Packet Tracer
2. Open **QUICK_REFERENCE.md** in a text editor (to copy/paste from)
3. Keep this file open to track your progress

---

### □ STEP 1: Configure the Router (10 minutes)

**What device:** Click on "Router" in Packet Tracer

**What to do:**
1. Click "Router" device
2. Click "CLI" tab (you'll see a black screen)
3. Go to QUICK_REFERENCE.md → Section 1
4. Copy ALL the router commands
5. Right-click in CLI and Paste (or Ctrl+V)
6. Press Enter
7. Wait for commands to finish (you'll see "SmartCity-Router#")

**Why:** This enables inter-VLAN routing and security (ACLs)

---

### □ STEP 2: Configure City-Core-Switch (5 minutes)

**What device:** Click on "City-Core-Switch" in Packet Tracer

**What to do:**
1. Click "City-Core-Switch"
2. Click "CLI" tab
3. Go to QUICK_REFERENCE.md → Section 2
4. Copy all City-Core-Switch commands
5. Paste into CLI
6. Press Enter

**Why:** This creates VLANs and trunk connections

---

### □ STEP 3: Configure DNS-Server (10 minutes)

**What device:** Click on "DNS-Server" in Packet Tracer

**Part A - Set IP Address:**
1. Click "DNS-Server"
2. Click "Desktop" tab
3. Click "IP Configuration"
4. Enter:
   - IP: 10.10.10.10
   - Subnet: 255.255.255.0
   - Gateway: 10.10.10.1
   - DNS: 10.10.10.10

**Part B - Configure DNS Records:**
1. Still in DNS-Server window, click "Services" tab
2. Click "DNS" in left menu
3. Turn DNS Service **ON**
4. Add records from QUICK_REFERENCE.md → Section 4
   - Enter Name, select Type "A", enter Address
   - Click "Add" for each record
   - Repeat for all 5 records

**Why:** Allows devices to use names instead of IP addresses

---

### □ STEP 4: Configure DHCP-Server (10 minutes)

**What device:** Click on "DHCP-Server" in Packet Tracer

**Part A - Set IP Address:**
1. Click "DHCP-Server"
2. Click "Desktop" tab
3. Click "IP Configuration"
4. Enter:
   - IP: 10.10.10.20
   - Subnet: 255.255.255.0
   - Gateway: 10.10.10.1
   - DNS: 10.10.10.10

**Part B - Create DHCP Pools:**
1. Click "Services" tab
2. Click "DHCP" in left menu
3. Turn DHCP Service **ON**
4. Create Pool 1 - AdminPool:
   - Pool Name: AdminPool
   - Default Gateway: 10.10.10.1
   - DNS Server: 10.10.10.10
   - Start IP: 10.10.10.100
   - Subnet: 255.255.255.0
   - Max Users: 50
   - Click **Add**
5. Create Pool 2 - PublicPool:
   - Pool Name: PublicPool
   - Default Gateway: 10.10.20.1
   - DNS Server: 10.10.10.10
   - Start IP: 10.10.20.100
   - Subnet: 255.255.255.0
   - Max Users: 100
   - Click **Add**
6. Create Pool 3 - IoTPool:
   - Pool Name: IoTPool
   - Default Gateway: 10.10.30.1
   - DNS Server: 10.10.10.10
   - Start IP: 10.10.30.100
   - Subnet: 255.255.255.0
   - Max Users: 50
   - Click **Add**

**Why:** Automatically assigns IP addresses to devices

---

### □ STEP 5: Configure Web-Server (10 minutes)

**What device:** Click on "Web-Server" in Packet Tracer

**Part A - Set IP Address:**
1. Click "Web-Server"
2. Click "Desktop" tab
3. Click "IP Configuration"
4. Enter:
   - IP: 10.10.10.40
   - Subnet: 255.255.255.0
   - Gateway: 10.10.10.1
   - DNS: 10.10.10.10

**Part B - Configure Web Service:**
1. Click "Services" tab
2. Click "HTTP" in left menu
3. Turn HTTP Service **ON**
4. Turn HTTPS **ON** (if available)
5. Click "index.html" to edit it
6. Go to COMPLETION_GUIDE.md → Section 3.3
7. Copy the HTML code for index.html
8. Select all existing text in the editor and delete it
9. Paste the new HTML
10. Look for button to save/apply (usually at bottom)

**Why:** Provides web pages users can visit

---

### □ STEP 6: Configure SMTP-Server (5 minutes)

**What device:** Click on "SMTP-Server" in Packet Tracer

**Part A - Set IP Address:**
1. Click "SMTP-Server"
2. Click "Desktop" tab
3. Click "IP Configuration"
4. Enter:
   - IP: 10.10.10.30
   - Subnet: 255.255.255.0
   - Gateway: 10.10.10.1
   - DNS: 10.10.10.10

**Part B - Configure Email Service:**
1. Click "Services" tab
2. Click "EMAIL" in left menu
3. Turn Email Service **ON**
4. Set Domain Name: smartcity.local
5. Add users (see QUICK_REFERENCE.md Section 6):
   - Click "+ Add"
   - Username: admin, Password: admin123
   - Click "Add User"
   - Repeat for: operations/ops123, support/support123, public/public123

**Why:** Allows sending and receiving emails

---

### □ STEP 7: Configure Client PCs (5 minutes)

**Do this for ALL 4 PCs:**
- Admin-PC-1
- Admin-PC-2
- Public-Kiosk-PC
- Resident-Home-PC

**For each PC:**
1. Click the PC device
2. Click "Desktop" tab
3. Click "IP Configuration"
4. Select **DHCP** (click the DHCP radio button)
5. Wait a few seconds - you should see an IP address appear
6. Verify DNS Server shows: 10.10.10.10

**Why:** Gets IPs automatically from DHCP server

---

### □ STEP 8: TEST EVERYTHING (15-20 minutes)

#### Test 1: Basic Connectivity

**From Admin-PC-1:**
1. Click "Admin-PC-1"
2. Click "Desktop" → "Command Prompt"
3. Type: `ping 10.10.10.1` (should reply)
4. Type: `ping 10.10.10.10` (DNS - should reply)
5. Type: `ping 10.10.10.40` (Web - should reply)

✓ If all ping replies = SUCCESS!

---

#### Test 2: DNS Resolution

**From any PC:**
1. Desktop → Command Prompt
2. Type: `nslookup web.smartcity.local`
3. Should show: 10.10.10.40

✓ If IP appears = DNS WORKS!

---

#### Test 3: Web Access

**From any PC:**
1. Desktop → Web Browser
2. Type in address bar: `http://web.smartcity.local`
3. Press Go
4. Should see "Welcome to Smart City Network" page

✓ If page loads = WEB SERVER WORKS!

---

#### Test 4: Email

**From Admin-PC-1:**
1. Desktop → Email
2. Configure:
   - Your Name: Admin
   - Email: admin@smartcity.local
   - Incoming Mail: mail.smartcity.local
   - Outgoing Mail: mail.smartcity.local
   - Username: admin
   - Password: admin123
3. Click "Save"
4. Click "Compose"
5. To: operations@smartcity.local
6. Subject: Test
7. Message: Testing email
8. Click "Send"

**From Admin-PC-2:**
1. Desktop → Email
2. Configure for operations@smartcity.local (password: ops123)
3. Click "Receive"
4. Should see test email!

✓ If email received = EMAIL WORKS!

---

#### Test 5: ACL Security (Advanced)

**From Public-Kiosk-PC:**
1. Desktop → Command Prompt
2. Type: `ping 10.10.30.100` (IoT network)
3. Should FAIL (Request timed out)
4. This is CORRECT - ACL is blocking public from IoT

✓ If ping fails = SECURITY WORKS!

---

#### Test 6: Packet Simulation

**Visual test:**
1. Click the **Realtime/Simulation** toggle (bottom right) → choose "Simulation"
2. Click "Add Simple PDU" (envelope icon)
3. Click Admin-PC-1 (source)
4. Click Web-Server (destination)
5. Click "Auto Capture/Play" button (play icon)
6. Watch packet travel through network!
7. Should go: PC → Switch → Router → Core Switch → Server

✓ If packet reaches destination = ROUTING WORKS!

---

## SUCCESS! Network is 100% Complete ✓

### What you accomplished:
- ✓ Inter-VLAN routing (devices in different VLANs can talk)
- ✓ DHCP (automatic IP assignment)
- ✓ DNS (name resolution)
- ✓ Web server (hosted pages)
- ✓ Email service (send/receive)
- ✓ Security (ACLs blocking unauthorized traffic)
- ✓ Full network connectivity

### Files Created:
- **connection.pkt** - Your complete Smart City network
- **connection.xml** - XML export for analysis
- **COMPLETION_GUIDE.md** - Detailed guide with all configs
- **QUICK_REFERENCE.md** - Quick copy/paste commands
- **PROJECT_STATUS.md** - Network analysis
- **START_HERE.md** - This file!

---

## Troubleshooting

**DHCP not working?**
- Check router has `ip helper-address 10.10.10.20` on subinterfaces
- Verify DHCP server has service ON
- Make sure PC is set to DHCP mode

**Can't ping across VLANs?**
- Check router subinterfaces are configured
- Verify `no shutdown` on all router interfaces
- Check switches have correct VLAN trunks

**DNS not resolving?**
- Verify DNS service is ON
- Check DNS records are added
- Make sure PC has DNS = 10.10.10.10

**Web page not loading?**
- Check HTTP service is ON
- Try IP address first: http://10.10.10.40
- If IP works but DNS name doesn't, fix DNS

**Need more help?**
- Check COMPLETION_GUIDE.md for detailed instructions
- Review QUICK_REFERENCE.md for all settings
- Check PROJECT_STATUS.md for network overview

---

**CONGRATULATIONS! Your Smart City Network is Complete!**
