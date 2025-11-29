# Complete Device-by-Device Verification Checklist
## Smart City Network - connection_FULL_AUTO.pkt

---

## 📋 HOW TO USE THIS CHECKLIST

For EACH device:
1. Click the device in Packet Tracer
2. Check Physical tab, Config tab, CLI tab (if applicable)
3. Verify ALL items listed below
4. Check off ✅ when verified
5. Note ❌ if missing or incorrect

---

## 🔧 NETWORK DEVICES

---

### DEVICE 1: City-Gateway-Router (ISR4321)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Location:** Verified on topology
- [ ] **Connections:**
  - [ ] Gig0/0/0 → (Check what's connected - may be Intercity or unconnected)
  - [ ] Gig0/0/1 → City-Core-Switch Gig1/0/1 (cable connected, green)

**Note:** Check your topology to see what Gig0/0/0 is actually connected to. It might be:
- Not connected (WAN interface for simulation purposes)
- Connected to "Intercity" device
- Or another external network device

#### Modules/Hardware
1. Click device → **Physical** tab
   - [ ] Router is ON (toggle switch)
   - [ ] Gig0/0/0 module present
   - [ ] Gig0/0/1 module present
   - [ ] No red indicators

#### IP Configuration
1. Go to **CLI** tab
2. Type: `enable` (password: `class`)
3. Type: `show ip interface brief`

**Verify:**
- [ ] Gig0/0/0: Status UP/UP (IP from DHCP or static)
- [ ] Gig0/0/1: IP 10.0.0.1, Status UP/UP

#### IPv6 Configuration
```
show ipv6 interface brief
```
- [ ] Gig0/0/0: Has IPv6 address (link-local + autoconfigured)
- [ ] Gig0/0/1: Has IPv6 address (link-local + autoconfigured)
- [ ] IPv6 unicast routing enabled

#### NAT Configuration
```
show running-config | section nat
```
- [ ] `ip nat inside source list 1 interface Gig0/0/0 overload`
- [ ] Gig0/0/0 has `ip nat outside`
- [ ] Gig0/0/1 has `ip nat inside`

```
show access-lists
```
- [ ] Access-list 1: `permit 10.10.0.0 0.0.255.255`

#### Routing
```
show ip route
```
- [ ] Default route: `0.0.0.0/0` via Gig0/0/0

#### Security
```
show running-config | section line
```
- [ ] Console password: `cisco`
- [ ] VTY password: `cisco`
- [ ] Enable secret: configured

#### Full Config Check
```
show running-config
```
- [ ] Hostname: `City-Gateway-Router`
- [ ] All configurations present

✅ **Device 1 Status:** _______

---

### DEVICE 2: City-Core-Switch (Catalyst 3650)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Location:** Verified on topology
- [ ] **Connections:**
  - [ ] Gig1/0/1 → Router Gig0/0/1 (green)
  - [ ] Gig1/0/2 → Downtown-Switch Fa0/1 (green)
  - [ ] Gig1/0/3 → Park-Switch Fa0/1 (green)
  - [ ] Gig1/0/4 → Residential-Switch Fa0/1 (green)
  - [ ] Gig1/0/5 → Central-Office-Server (green)
  - [ ] Gig1/0/6 → SMTP-Server (green)
  - [ ] Gig1/0/7 → Web-Server (green)
  - [ ] Gig1/0/8 → DHCP-Server (green)
  - [ ] Gig1/0/9 → DNS-Server (green)
  - [ ] Gig1/0/10 → Admin-PC-1 (green)
  - [ ] Gig1/0/11 → Admin-PC-2 (green)
  - [ ] Gig1/0/12 → City-Hall-Phone (green)

#### Modules/Hardware
1. Go to **Physical** tab
   - [ ] Switch is ON
   - [ ] All GigabitEthernet modules present
   - [ ] All ports show green when connected

#### VLANs
```
enable
show vlan brief
```
- [ ] VLAN 10 - Name: Admin
- [ ] VLAN 20 - Name: Public
- [ ] VLAN 30 - Name: IoT
- [ ] VLAN 99 - Name: Management

**Port Assignments:**
- [ ] Gig1/0/5: VLAN 20 (Central Office)
- [ ] Gig1/0/6-9: VLAN 10 (Servers)
- [ ] Gig1/0/10-12: VLAN 10 (Admin devices)

#### Trunk Ports
```
show interfaces trunk
```
- [ ] Gig1/0/2: Mode trunk, Native VLAN 99, Allowed VLANs: 10,20,30,99
- [ ] Gig1/0/3: Mode trunk, Native VLAN 99, Allowed VLANs: 10,20,30,99
- [ ] Gig1/0/4: Mode trunk, Native VLAN 99, Allowed VLANs: 10,20,30,99

#### Layer 3 Configuration
```
show ip interface brief
```
- [ ] Gig1/0/1: 10.0.0.2 (routed port to router)
- [ ] Vlan10: 10.10.10.1
- [ ] Vlan20: 10.10.20.1
- [ ] Vlan30: 10.10.30.1
- [ ] Vlan99: 10.10.99.1

#### IPv6
```
show ipv6 interface brief
```
- [ ] IPv6 enabled on Gig1/0/1
- [ ] IPv6 enabled on all VLANs
- [ ] IPv6 unicast routing enabled

#### Routing
```
show ip route
```
- [ ] Connected routes for all VLANs
- [ ] Default route: `0.0.0.0/0` via 10.0.0.1

#### Security ACL
```
show access-lists
```
- [ ] Extended ACL: `BLOCK-PUBLIC-TO-ADMIN`
- [ ] Rule 1: `permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq domain`
- [ ] Rule 2: `permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq domain`
- [ ] Rule 3: `deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255`
- [ ] Rule 4: `permit ip any any`

```
show running-config interface vlan20
```
- [ ] ACL applied inbound: `ip access-group BLOCK-PUBLIC-TO-ADMIN in`

#### Full Config
```
show running-config
```
- [ ] Hostname: `City-Core-Switch`
- [ ] Enable secret configured

✅ **Device 2 Status:** _______

---

### DEVICE 3: Downtown-Switch (Catalyst 2960)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Connections:**
  - [ ] Fa0/1 → Core-Switch Gig1/0/2 (green trunk)
  - [ ] Fa0/2 → Public-Kiosk-PC (green)
  - [ ] Fa0/3 → Public-WiFi-AP (green)
  - [ ] Fa0/4 → Info-Line-Phone (green)

#### Modules/Hardware
1. **Physical** tab
   - [ ] Switch is ON
   - [ ] All FastEthernet ports present

#### VLANs
```
enable
show vlan brief
```
- [ ] VLAN 20 - Name: Public
- [ ] VLAN 99 - Name: Management
- [ ] Fa0/2-4: VLAN 20

#### Trunk Port
```
show interfaces trunk
```
- [ ] Fa0/1: Mode trunk, Native VLAN 99

#### Configuration
```
show running-config
```
- [ ] Hostname: `Downtown-Switch`

✅ **Device 3 Status:** _______

---

### DEVICE 4: Park-Switch (Catalyst 2960)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Connections:**
  - [ ] Fa0/1 → Core-Switch Gig1/0/3 (green trunk)
  - [ ] Fa0/2 → Park-IoT-Gateway (green)
  - [ ] Fa0/3 → Smart-Streetlight (green)

#### Modules/Hardware
1. **Physical** tab
   - [ ] Switch is ON
   - [ ] All FastEthernet ports present

#### VLANs
```
enable
show vlan brief
```
- [ ] VLAN 30 - Name: IoT
- [ ] VLAN 99 - Name: Management
- [ ] Fa0/2-3: VLAN 30

#### Trunk Port
```
show interfaces trunk
```
- [ ] Fa0/1: Mode trunk, Native VLAN 99

#### Configuration
```
show running-config
```
- [ ] Hostname: `Park-Switch`

✅ **Device 4 Status:** _______

---

### DEVICE 5: Residential-Switch (Catalyst 2960)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Connections:**
  - [ ] Fa0/1 → Core-Switch Gig1/0/4 (green trunk)
  - [ ] Fa0/2 → Resident-Home-PC (green)
  - [ ] Fa0/3 → Residential-WiFi-AP (green)

#### Modules/Hardware
1. **Physical** tab
   - [ ] Switch is ON
   - [ ] All FastEthernet ports present

#### VLANs
```
enable
show vlan brief
```
- [ ] VLAN 30 - Name: IoT
- [ ] VLAN 99 - Name: Management
- [ ] Fa0/2-3: VLAN 30

#### Trunk Port
```
show interfaces trunk
```
- [ ] Fa0/1: Mode trunk, Native VLAN 99

#### Configuration
```
show running-config
```
- [ ] Hostname: `Residential-Switch`

✅ **Device 5 Status:** _______

---

## 🖥️ SERVERS

---

### DEVICE 6: DNS-Server (Server-PT)

#### Physical Status
- [ ] **Power:** ON (green light on chassis)
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/9 (green)

#### Hardware/Modules
1. Go to **Physical** tab
   - [ ] Server is ON (power button)
   - [ ] PT-HOST-NM-1CFE module installed
   - [ ] FastEthernet0 port visible

#### Network Configuration
1. Go to **Config** tab
2. Click **FastEthernet0**

**Verify:**
- [ ] **Port Status:** On
- [ ] **Bandwidth:** 100 Mbps
- [ ] **Duplex:** Auto
- [ ] **IP Configuration:** Static (not DHCP)
- [ ] **IP Address:** `10.10.10.10`
- [ ] **Subnet Mask:** `255.255.255.0`
- [ ] **IPv6 Configuration:** (check if available)

#### Global Settings
1. Click **Settings** → **Global**

**Verify:**
- [ ] **Gateway:** `10.10.10.1`
- [ ] **DNS Server:** `10.10.10.10`

#### DNS Service
1. Go to **Services** tab
2. Click **DNS**

**Verify:**
- [ ] **DNS Service:** ON (toggle enabled)

**Check DNS Records:**
- [ ] `smartcity.local` → `10.10.10.30`
- [ ] `dns.smartcity.local` → `10.10.10.10`
- [ ] `dhcp.smartcity.local` → `10.10.10.20`
- [ ] `web.smartcity.local` → `10.10.10.30`
- [ ] `mail.smartcity.local` → `10.10.10.40`
- [ ] `centraloffice.smartcity.local` → `10.10.20.50`

**If records missing:** Add them manually (Name → Address → Add button)

#### Desktop Test
1. Go to **Desktop** tab
2. Click **Command Prompt**
3. Type: `ipconfig`

**Verify:**
- [ ] IP Address: 10.10.10.10
- [ ] Subnet Mask: 255.255.255.0
- [ ] Default Gateway: 10.10.10.1

✅ **Device 6 Status:** _______

---

### DEVICE 7: DHCP-Server (Server-PT)

#### Physical Status
- [ ] **Power:** ON (green light)
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/8 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Server is ON
   - [ ] PT-HOST-NM-1CFE module installed
   - [ ] FastEthernet0 port visible

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **Port Status:** On
- [ ] **IP Configuration:** Static
- [ ] **IP Address:** `10.10.10.20`
- [ ] **Subnet Mask:** `255.255.255.0`

#### Global Settings
1. **Settings** → **Global**

**Verify:**
- [ ] **Gateway:** `10.10.10.1`
- [ ] **DNS Server:** `10.10.10.10`

#### DHCP Service
1. **Services** tab → **DHCP**

**Verify:**
- [ ] **DHCP Service:** ON (toggle enabled)

**Check DHCP Pools:**

**Pool 1: AdminPool**
- [ ] Pool Name: `AdminPool`
- [ ] Default Gateway: `10.10.10.1`
- [ ] DNS Server: `10.10.10.10`
- [ ] Start IP: `10.10.10.100`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Maximum Users: `50`

**Pool 2: PublicPool**
- [ ] Pool Name: `PublicPool`
- [ ] Default Gateway: `10.10.20.1`
- [ ] DNS Server: `10.10.10.10`
- [ ] Start IP: `10.10.20.100`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Maximum Users: `100`

**Pool 3: IoTPool**
- [ ] Pool Name: `IoTPool`
- [ ] Default Gateway: `10.10.30.1`
- [ ] DNS Server: `10.10.10.10`
- [ ] Start IP: `10.10.30.100`
- [ ] Subnet Mask: `255.255.255.0`
- [ ] Maximum Users: `50`

**If pools missing:** Create them manually (enter details → Save for each pool)

#### Desktop Test
1. **Desktop** → **Command Prompt**
2. `ipconfig`

**Verify:**
- [ ] IP: 10.10.10.20
- [ ] Gateway: 10.10.10.1

✅ **Device 7 Status:** _______

---

### DEVICE 8: Web-Server (Server-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/7 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Server is ON
   - [ ] PT-HOST-NM-1CFE module installed

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **Port Status:** On
- [ ] **IP Configuration:** Static
- [ ] **IP Address:** `10.10.10.30`
- [ ] **Subnet Mask:** `255.255.255.0`

#### Global Settings
1. **Settings** → **Global**

**Verify:**
- [ ] **Gateway:** `10.10.10.1`
- [ ] **DNS Server:** `10.10.10.10`

#### HTTP Service
1. **Services** tab → **HTTP**

**Verify:**
- [ ] **HTTP Service:** ON (toggle enabled)
- [ ] **HTTPS:** Can be ON or OFF (optional)

**Check Web Content:**
- [ ] File `index.html` exists in file list
- [ ] Click on `index.html` to view/edit
- [ ] Content is custom (not default "Cisco Packet Tracer Server")

**If content needs updating:** Edit index.html with provided HTML

#### Desktop Test
1. **Desktop** → **Command Prompt**
2. `ipconfig`

**Verify:**
- [ ] IP: 10.10.10.30

✅ **Device 8 Status:** _______

---

### DEVICE 9: SMTP-Server (Server-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/6 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Server is ON
   - [ ] PT-HOST-NM-1CFE module installed

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **Port Status:** On
- [ ] **IP Configuration:** Static
- [ ] **IP Address:** `10.10.10.40`
- [ ] **Subnet Mask:** `255.255.255.0`

#### Global Settings
1. **Settings** → **Global**

**Verify:**
- [ ] **Gateway:** `10.10.10.1`
- [ ] **DNS Server:** `10.10.10.10`

#### EMAIL Service
1. **Services** tab → **EMAIL**

**Verify:**
- [ ] **Service:** ON (toggle enabled)
- [ ] **Domain Name:** `smartcity.local`

**Check Users:**
- [ ] User: `admin`, Password: `cisco`
- [ ] User: `iot`, Password: `cisco`

**If users missing:** Add them (User field → Password field → + button)

#### Desktop Test
1. **Desktop** → **Command Prompt**
2. `ipconfig`

**Verify:**
- [ ] IP: 10.10.10.40

✅ **Device 9 Status:** _______

---

### DEVICE 10: Central-Office-Server (Server-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/5 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Server is ON
   - [ ] Network module installed

#### Network Configuration
1. **Config** tab → **FastEthernet0** OR
2. **Desktop** tab → **IP Configuration**

**Verify:**
- [ ] **Port Status:** On
- [ ] **IP Configuration:** Static (not DHCP)
- [ ] **IP Address:** `10.10.20.50`
- [ ] **Subnet Mask:** `255.255.255.0`
- [ ] **Default Gateway:** `10.10.20.1`
- [ ] **DNS Server:** `10.10.10.10`

**If NOT configured:**
- Desktop → IP Configuration → Static
- Enter: IP, Subnet, Gateway, DNS

#### Desktop Test
1. **Desktop** → **Command Prompt**
2. `ipconfig`

**Verify:**
- [ ] IP: 10.10.20.50
- [ ] Gateway: 10.10.20.1

✅ **Device 10 Status:** _______

---

### DEVICE 11: Park-IoT-Gateway (SBC - Single Board Computer)

#### Physical Status
- [ ] **Power:** ON (check power indicator)
- [ ] **Connections:**
  - [ ] FastEthernet0 → Park-Switch Fa0/2 (green)
  - [ ] D0 → Park-Motion-Sensor (connected)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Device is ON
   - [ ] FastEthernet module present
   - [ ] GPIO pins available (for sensor/actuator)
   - [ ] D0 pin has motion sensor connected

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **Port Status:** On
- [ ] **IP Address:** `10.10.30.10`
- [ ] **Subnet Mask:** `255.255.255.0`

#### Global Settings
1. **Settings** → **Global Settings**

**Verify:**
- [ ] **Default Gateway:** `10.10.30.1`
- [ ] **DNS Server:** `10.10.10.10`

#### IoT Programming
1. **Programming** tab
2. Click **Blockly** (visual programming)

**Verify automation exists:**
- [ ] **Trigger:** When Motion Sensor (D0) is ACTIVATED
- [ ] **Action 1:** Set Device 10.10.30.20 brightness to 1023
- [ ] **Action 2:** Wait 60 seconds
- [ ] **Action 3:** Set Device 10.10.30.20 brightness to 0
- [ ] **Action 4:** Send Email
  - [ ] To: admin@smartcity.local
  - [ ] From: iot@smartcity.local
  - [ ] Subject: Park Alert
  - [ ] Message: Motion detected - Light activated
  - [ ] SMTP Server: 10.10.10.40

**If NOT programmed:** Create blocks in Blockly editor

#### Desktop Test (if available)
1. **Desktop** → **Command Prompt** (if available)
2. `ipconfig`

**Verify:**
- [ ] IP: 10.10.30.10

✅ **Device 11 Status:** _______

---

## 💻 CLIENT DEVICES (PCs)

---

### DEVICE 12: Admin-PC-1 (PC-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/10 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] PC is ON
   - [ ] FastEthernet module installed

#### Network Configuration
1. **Desktop** tab → **IP Configuration**

**Verify:**
- [ ] **Configuration:** DHCP (radio button selected)
- [ ] **IP Address:** 10.10.10.100-150 range (from AdminPool)
- [ ] **Subnet Mask:** 255.255.255.0
- [ ] **Default Gateway:** 10.10.10.1
- [ ] **DNS Server:** 10.10.10.10

**If shows 0.0.0.0:**
- DHCP not working
- Check DHCP-Server pools configured
- Try: Static → then back to DHCP to refresh

#### Connectivity Test
1. **Desktop** → **Command Prompt**

**Test commands:**
```
ipconfig
```
- [ ] Shows IP 10.10.10.x

```
ping 10.10.10.1
```
- [ ] Replies received

```
ping 10.10.10.10
```
- [ ] Replies received

✅ **Device 12 Status:** _______

---

### DEVICE 13: Admin-PC-2 (PC-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Core-Switch Gig1/0/11 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] PC is ON
   - [ ] FastEthernet module installed

#### Network Configuration
1. **Desktop** → **IP Configuration**

**Verify:**
- [ ] **Configuration:** DHCP
- [ ] **IP Address:** 10.10.10.100-150 (different from PC-1)
- [ ] **Subnet Mask:** 255.255.255.0
- [ ] **Default Gateway:** 10.10.10.1
- [ ] **DNS Server:** 10.10.10.10

**If NOT configured:** Select DHCP radio button

✅ **Device 13 Status:** _______

---

### DEVICE 14: Public-Kiosk-PC (PC-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Downtown-Switch Fa0/2 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] PC is ON
   - [ ] FastEthernet module installed

#### Network Configuration
1. **Desktop** → **IP Configuration**

**Verify:**
- [ ] **Configuration:** DHCP
- [ ] **IP Address:** 10.10.20.100-200 (from PublicPool)
- [ ] **Subnet Mask:** 255.255.255.0
- [ ] **Default Gateway:** 10.10.20.1
- [ ] **DNS Server:** 10.10.10.10

**Security Test (IMPORTANT):**
1. **Command Prompt**
```
ping 10.10.10.10
```
- [ ] Should FAIL (timeout) - This is CORRECT! ACL blocking.

```
nslookup smartcity.local
```
- [ ] Should WORK - Returns 10.10.10.30

✅ **Device 14 Status:** _______

---

### DEVICE 15: Resident-Home-PC (PC-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] FastEthernet0 → Residential-Switch Fa0/2 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] PC is ON
   - [ ] FastEthernet module installed

#### Network Configuration
1. **Desktop** → **IP Configuration**

**Verify:**
- [ ] **Configuration:** DHCP
- [ ] **IP Address:** 10.10.30.100-150 (from IoTPool)
- [ ] **Subnet Mask:** 255.255.255.0
- [ ] **Default Gateway:** 10.10.30.1
- [ ] **DNS Server:** 10.10.10.10

✅ **Device 15 Status:** _______

---

## 📡 WIRELESS DEVICES

---

### DEVICE 16: Public-WiFi-AP (Access Point-PT)

#### Physical Status
- [ ] **Power:** ON (green LED)
- [ ] **Connections:**
  - [ ] Port 0 (Wireless) - Broadcasting
  - [ ] Port 1 (Ethernet) → Downtown-Switch Fa0/3 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Access Point is ON
   - [ ] Wireless antenna visible
   - [ ] Ethernet port connected

#### Wireless Configuration
1. **Config** tab → **Wireless** (or **Port 0**)

**Verify:**
- [ ] **SSID:** `City-Public-WiFi`
- [ ] **Authentication:** WPA2-PSK
- [ ] **PSK Pass Phrase:** `publicaccess`
- [ ] **Encryption Type:** AES (if available)
- [ ] **Channel:** Auto or 6
- [ ] **SSID Broadcast:** Enabled

#### Internet Port Configuration
1. **Config** tab → **Port 1** (Ethernet/Internet port)

**Verify:**
- [ ] **IP Configuration:** DHCP
- [ ] **IP Address:** 10.10.20.x (from PublicPool)
- [ ] **Gateway:** 10.10.20.1

**If NOT configured:** Set to DHCP

#### Test
1. Check if **Citizen-Smartphone** can see this network
2. Signal indicator should be visible

✅ **Device 16 Status:** _______

---

### DEVICE 17: Residential-WiFi-AP (Access Point-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connections:**
  - [ ] Port 0 (Wireless) - Broadcasting
  - [ ] Port 1 (Ethernet) → Residential-Switch Fa0/3 (green)

#### Hardware/Modules
1. **Physical** tab
   - [ ] Access Point is ON
   - [ ] Wireless antenna visible

#### Wireless Configuration
1. **Config** tab → **Wireless**

**Verify:**
- [ ] **SSID:** `Residential-Network`
- [ ] **Authentication:** WPA2-PSK
- [ ] **PSK Pass Phrase:** `homeaccess`
- [ ] **Encryption Type:** AES (if available)
- [ ] **Channel:** Auto or 11
- [ ] **SSID Broadcast:** Enabled

#### Internet Port Configuration
1. **Config** tab → **Port 1**

**Verify:**
- [ ] **IP Configuration:** DHCP
- [ ] **IP Address:** 10.10.30.x (from IoTPool)
- [ ] **Gateway:** 10.10.30.1

✅ **Device 17 Status:** _______

---

### DEVICE 18: Citizen-Smartphone (Smartphone-PT)

#### Physical Status
- [ ] **Power:** ON (screen visible)
- [ ] **Wireless Adapter:** Enabled

#### Hardware/Modules
1. **Physical** tab
   - [ ] Smartphone is ON
   - [ ] Wireless adapter present

#### Wireless Connection
1. **Desktop** tab → **PC Wireless**
2. **Connect** tab

**Verify:**
- [ ] **Available Networks:** City-Public-WiFi visible
- [ ] **Connection Status:** Connected (to City-Public-WiFi)
- [ ] **Signal Strength:** Good/Excellent

**Connection Details:**
1. **Link Information** tab (if available)

**Verify:**
- [ ] **SSID:** City-Public-WiFi
- [ ] **IP Address:** 10.10.20.x (from PublicPool via WiFi)
- [ ] **Gateway:** 10.10.20.1
- [ ] **DNS:** 10.10.10.10

**If NOT connected:**
1. Click **Connect** tab
2. Select **City-Public-WiFi**
3. Enter password: `publicaccess`
4. Click **Connect**
5. Wait for connection

#### Test
1. **Desktop** → **Web Browser**
2. Try accessing: `http://smartcity.local`
- [ ] Website loads successfully

✅ **Device 18 Status:** _______

---

## 📱 VoIP PHONES

---

### DEVICE 19: City-Hall-Phone (IP Phone-PT)

#### Physical Status
- [ ] **Power:** ON (screen lit)
- [ ] **Connection:**
  - [ ] Ethernet → Core-Switch Gig1/0/12 (green)

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **IP Configuration:** DHCP (should get from AdminPool)
- [ ] **IP Address:** 10.10.10.x
- [ ] **Default Gateway:** 10.10.10.1

#### Phone Configuration
1. Check phone number is assigned (if applicable)
2. Phone should be registered to network

**Test:**
- [ ] Can dial other phones
- [ ] Receives calls

✅ **Device 19 Status:** _______

---

### DEVICE 20: Info-Line-Phone (IP Phone-PT)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] Ethernet → Downtown-Switch Fa0/4 (green)

#### Network Configuration
1. **Config** tab → **FastEthernet0**

**Verify:**
- [ ] **IP Configuration:** DHCP (from PublicPool)
- [ ] **IP Address:** 10.10.20.x
- [ ] **Default Gateway:** 10.10.20.1

#### Test
- [ ] Can receive calls from City-Hall-Phone

✅ **Device 20 Status:** _______

---

## 🔌 IoT DEVICES

---

### DEVICE 21: Park-Motion-Sensor (Motion Detector)

#### Physical Status
- [ ] **Power:** ON (if applicable)
- [ ] **Connection:**
  - [ ] Connected to Park-IoT-Gateway D0 pin

#### Configuration
1. Click device
2. Check connection status

**Verify:**
- [ ] Properly connected to IoT Gateway
- [ ] Responds when clicked (triggers event)

#### Test
- [ ] Click sensor to activate
- [ ] Should trigger IoT Gateway automation

✅ **Device 21 Status:** _______

---

### DEVICE 22: Smart-Streetlight (Smart LED)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] Ethernet → Park-Switch Fa0/3 (green)

#### Network Configuration (if configurable)
1. **Config** tab (if available)

**Verify:**
- [ ] **IP Address:** `10.10.30.20` (if static IP supported)
- [ ] **Subnet Mask:** `255.255.255.0`
- [ ] **Default Gateway:** `10.10.30.1`

**Note:** Some IoT devices auto-configure or don't have IP config GUI

#### Test
- [ ] Responds to Park-IoT-Gateway commands
- [ ] Turns ON when motion detected
- [ ] Turns OFF after 60 seconds

✅ **Device 22 Status:** _______

---

### DEVICE 23: Cell Tower (if present)

#### Physical Status
- [ ] **Power:** ON
- [ ] **Connection:**
  - [ ] To Central-Office-Server
  - [ ] Wireless connection visible

#### Configuration
- [ ] Operational
- [ ] Provides cellular connectivity

✅ **Device 23 Status:** _______

---

## 🧪 COMPREHENSIVE FUNCTIONAL TESTS

---

### TEST 1: Basic Layer 1-2 Connectivity

**Check ALL cable connections are GREEN:**
- [ ] Router ↔ Core Switch
- [ ] Core ↔ Downtown Switch
- [ ] Core ↔ Park Switch
- [ ] Core ↔ Residential Switch
- [ ] All server connections
- [ ] All PC connections
- [ ] All phone connections
- [ ] All IoT connections

**If any RED:**
- Cable not connected properly
- Port shutdown
- Wrong cable type

---

### TEST 2: Layer 3 Routing

**From Admin-PC-1 Command Prompt:**

```
tracert 10.10.20.1
```
- [ ] Hop 1: 10.10.10.1 (VLAN 10 gateway)
- [ ] Hop 2: 10.10.20.1 (destination)

```
tracert 8.8.8.8
```
- [ ] Should reach Internet through NAT

---

### TEST 3: DHCP Functionality

**Test all DHCP clients:**
1. Release/Renew on each PC:
   - Admin-PC-1: Desktop → Command Prompt → `ipconfig /renew`
   - Admin-PC-2: `ipconfig /renew`
   - Public-Kiosk-PC: `ipconfig /renew`
   - Resident-Home-PC: `ipconfig /renew`

**Verify:**
- [ ] All get new IPs from correct pools
- [ ] All have correct gateways
- [ ] All have DNS: 10.10.10.10

---

### TEST 4: DNS Resolution

**From any PC:**
```
nslookup smartcity.local
```
- [ ] Returns: 10.10.10.30

```
nslookup dns.smartcity.local
```
- [ ] Returns: 10.10.10.10

```
nslookup mail.smartcity.local
```
- [ ] Returns: 10.10.10.40

---

### TEST 5: Web Services

**From Admin-PC-1:**
1. Desktop → Web Browser
2. Test these URLs:
   - `http://smartcity.local`
     - [ ] Loads Smart City Dashboard
   - `http://10.10.10.30`
     - [ ] Loads same page
   - `http://web.smartcity.local`
     - [ ] Loads same page

---

### TEST 6: Security ACL

**From Public-Kiosk-PC (VLAN 20):**

**Should WORK:**
```
nslookup smartcity.local
```
- [ ] ✅ Returns 10.10.10.30 (DNS allowed)

```
ping 10.10.20.1
```
- [ ] ✅ Replies received (same VLAN)

**Should FAIL:**
```
ping 10.10.10.10
```
- [ ] ❌ Request timed out (ACL blocks ICMP to Admin VLAN)

```
ping 10.10.10.1
```
- [ ] ❌ Request timed out (ACL blocks to Admin VLAN)

```
telnet 10.10.10.30 80
```
- [ ] ❌ Connection failed (ACL blocks HTTP to Admin VLAN servers)

**This proves ACL is working correctly!**

---

### TEST 7: Inter-VLAN Routing

**Ping from Admin-PC-1 to other VLANs:**
```
ping 10.10.20.1
```
- [ ] ✅ Works (can reach Public VLAN gateway)

```
ping 10.10.30.1
```
- [ ] ✅ Works (can reach IoT VLAN gateway)

**Admin can reach all VLANs (no restrictions on Admin VLAN)**

---

### TEST 8: NAT/Internet Access

**From Admin-PC-1:**
```
ping 8.8.8.8
```
- [ ] ✅ Replies received (NAT working)

**On Router CLI:**
```
show ip nat translations
```
- [ ] ✅ Shows translations (inside local → inside global)

---

### TEST 9: IoT Automation Complete Test

**Full workflow:**
1. Click **Park-Motion-Sensor**
2. **Observe Smart-Streetlight:**
   - [ ] Turns ON immediately (full brightness/blue)
   - [ ] Stays ON for exactly 60 seconds
   - [ ] Turns OFF automatically
3. **Check Email:**
   - Click **SMTP-Server** → Services → EMAIL
   - Check admin@smartcity.local inbox
   - [ ] Email from iot@smartcity.local present
   - [ ] Subject: "Park Alert"
   - [ ] Message: "Motion detected - Light activated"

**If fails at any step:**
- Check Park-IoT-Gateway IP: 10.10.30.10
- Check Smart-Streetlight IP: 10.10.30.20 (if applicable)
- Check Blockly code programmed correctly
- Check SMTP users exist
- Check all devices in VLAN 30 have connectivity

---

### TEST 10: WiFi Connectivity

**Test 1: Smartphone Connection**
1. **Citizen-Smartphone** → Desktop → PC Wireless
   - [ ] Connected to City-Public-WiFi
   - [ ] Has IP from PublicPool (10.10.20.x)
   - [ ] Can browse web

**Test 2: WiFi AP Reachability**
- From Public-Kiosk-PC:
```
ping [Public-WiFi-AP IP]
```
- [ ] Replies received (both in VLAN 20)

---

### TEST 11: VoIP Functionality

**Make a call:**
1. Click **City-Hall-Phone**
2. Pick up handset
3. Dial **Info-Line-Phone** number
4. **Verify:**
   - [ ] Call rings on Info-Line-Phone
   - [ ] Can answer call
   - [ ] Audio connection established
   - [ ] Can hang up cleanly

---

### TEST 12: IPv6 Functionality

**On Router CLI:**
```
show ipv6 interface brief
```
- [ ] All interfaces have IPv6 addresses (link-local minimum)
- [ ] Gig0/0/0 has autoconfigured global address
- [ ] Gig0/0/1 has autoconfigured global address

**On Core Switch CLI:**
```
show ipv6 interface brief
```
- [ ] All VLANs have IPv6 enabled
- [ ] Link-local addresses present

**Note:** Full IPv6 connectivity may be limited in PT simulation

---

## 📊 FINAL VERIFICATION SUMMARY

### Network Devices (5)
- [ ] City-Gateway-Router - All checks ✅
- [ ] City-Core-Switch - All checks ✅
- [ ] Downtown-Switch - All checks ✅
- [ ] Park-Switch - All checks ✅
- [ ] Residential-Switch - All checks ✅

### Servers (6)
- [ ] DNS-Server - All checks ✅
- [ ] DHCP-Server - All checks ✅
- [ ] Web-Server - All checks ✅
- [ ] SMTP-Server - All checks ✅
- [ ] Central-Office-Server - All checks ✅
- [ ] Park-IoT-Gateway - All checks ✅

### Client Devices (4)
- [ ] Admin-PC-1 - All checks ✅
- [ ] Admin-PC-2 - All checks ✅
- [ ] Public-Kiosk-PC - All checks ✅
- [ ] Resident-Home-PC - All checks ✅

### Wireless Devices (3)
- [ ] Public-WiFi-AP - All checks ✅
- [ ] Residential-WiFi-AP - All checks ✅
- [ ] Citizen-Smartphone - All checks ✅

### VoIP Devices (2)
- [ ] City-Hall-Phone - All checks ✅
- [ ] Info-Line-Phone - All checks ✅

### IoT Devices (2-3)
- [ ] Park-Motion-Sensor - All checks ✅
- [ ] Smart-Streetlight - All checks ✅
- [ ] Cell Tower (if present) - All checks ✅

### Functional Tests (12)
- [ ] Test 1: Physical connectivity ✅
- [ ] Test 2: Layer 3 routing ✅
- [ ] Test 3: DHCP ✅
- [ ] Test 4: DNS ✅
- [ ] Test 5: Web services ✅
- [ ] Test 6: Security ACL ✅
- [ ] Test 7: Inter-VLAN routing ✅
- [ ] Test 8: NAT/Internet ✅
- [ ] Test 9: IoT automation ✅
- [ ] Test 10: WiFi ✅
- [ ] Test 11: VoIP ✅
- [ ] Test 12: IPv6 ✅

---

## 🎯 PROJECT COMPLETION CRITERIA

**YOUR PROJECT IS 100% COMPLETE WHEN:**

1. [ ] **All 23 devices** verified and operational
2. [ ] **All network configurations** in place
3. [ ] **All server services** running
4. [ ] **All 12 functional tests** PASS
5. [ ] **No red cables** on topology
6. [ ] **All ports green/up**
7. [ ] **IoT automation** works end-to-end
8. [ ] **Security ACL** blocks correctly
9. [ ] **DHCP** assigns IPs correctly
10. [ ] **DNS** resolves all names

---

## 📝 ISSUES LOG

**Document any problems found:**

| Device | Issue | Status | Fix Applied |
|--------|-------|--------|-------------|
| | | | |
| | | | |
| | | | |
| | | | |

---

**Total Checks in This Document:** 300+

**Use this comprehensive checklist to verify EVERY aspect of your network!**

**For any missing configurations, refer to `COMPLETE_MANUAL_GUIDE.md` for detailed fix instructions.**
