# SIMPLE WORKING CONFIGURATION - Easiest Path to Success

## Strategy: Use City-Core-Switch for Inter-VLAN Routing

Your City-Core-Switch is a **Layer 3 multilayer switch** - it can route between VLANs!
This is EASIER than configuring router subinterfaces.

---

## STEP 1: Configure City-Core-Switch (DO THIS FIRST!)

### Access the switch:
1. Click **"City-Core-Switch"**
2. Click **"CLI" tab**
3. Password: `cisco` (if asked)

### Copy and paste ALL these commands:

```cisco
enable
configure terminal

! Enable IP routing on the switch
ip routing

! Create VLANs
vlan 10
 name Servers-Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management
exit

! Create VLAN interfaces (SVIs) - These are the gateways!
interface Vlan10
 description Servers-Admin Gateway
 ip address 10.10.10.1 255.255.255.0
 ip helper-address 10.10.10.20
 no shutdown
exit

interface Vlan20
 description Public Gateway
 ip address 10.10.20.1 255.255.255.0
 ip helper-address 10.10.10.20
 no shutdown
exit

interface Vlan30
 description IoT Gateway
 ip address 10.10.30.1 255.255.255.0
 ip helper-address 10.10.10.20
 no shutdown
exit

interface Vlan99
 description Management
 ip address 10.10.99.1 255.255.255.0
 no shutdown
exit

! Configure trunks to other switches
interface GigabitEthernet1/0/2
 description Trunk to Downtown-Switch
 switchport trunk native vlan 99
 switchport trunk allowed vlan 20,99
 switchport mode trunk
 no shutdown
exit

interface GigabitEthernet1/0/3
 description Trunk to Park-Switch
 switchport trunk native vlan 99
 switchport trunk allowed vlan 30,99
 switchport mode trunk
 no shutdown
exit

interface GigabitEthernet1/0/4
 description Trunk to Residential-Switch
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,99
 switchport mode trunk
 no shutdown
exit

! Server/PC access ports - VLAN 10
interface range GigabitEthernet1/0/6-11
 description Servers and Admin PCs
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 2: Configure Downtown-Switch

```cisco
enable
configure terminal
hostname Downtown-Switch

vlan 20
 name Public
vlan 99
 name Management
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description Trunk to City-Core
 switchport mode trunk
 switchport trunk allowed vlan 20,99
 no shutdown
exit

! Public access ports
interface range FastEthernet0/2-10
 description Public Access
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 3: Configure Park-Switch

```cisco
enable
configure terminal
hostname Park-Switch

vlan 30
 name IoT
vlan 99
 name Management
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description Trunk to City-Core
 switchport mode trunk
 switchport trunk allowed vlan 30,99
 no shutdown
exit

! IoT device ports
interface range FastEthernet0/2-10
 description IoT Devices
 switchport access vlan 30
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 4: Configure Residential-Switch

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
exit

! Trunk to City-Core-Switch
interface FastEthernet0/1
 description Trunk to City-Core
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! Admin devices
interface range FastEthernet0/2-5
 description Admin Devices
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

! Residential/Public devices
interface range FastEthernet0/6-10
 description Residential Access
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

write memory
```

---

## STEP 5: Configure Servers (GUI - No CLI needed!)

### DNS-Server (10.10.10.10)

1. Click **"DNS-Server"** → **Desktop** → **IP Configuration**
   - IP: `10.10.10.10`
   - Subnet: `255.255.255.0`
   - Gateway: `10.10.10.1`
   - DNS: `10.10.10.10`

2. Click **Services** → **DNS** → Turn **ON**
   - Add records:
     ```
     dns.smartcity.local     → 10.10.10.10
     dhcp.smartcity.local    → 10.10.10.20
     web.smartcity.local     → 10.10.10.40
     mail.smartcity.local    → 10.10.10.30
     ```

---

### DHCP-Server (10.10.10.20)

1. Click **"DHCP-Server"** → **Desktop** → **IP Configuration**
   - IP: `10.10.10.20`
   - Subnet: `255.255.255.0`
   - Gateway: `10.10.10.1`
   - DNS: `10.10.10.10`

2. Click **Services** → **DHCP** → Turn **ON**

   **Pool 1 - AdminPool:**
   - Pool Name: `AdminPool`
   - Default Gateway: `10.10.10.1`
   - DNS Server: `10.10.10.10`
   - Start IP: `10.10.10.100`
   - Subnet Mask: `255.255.255.0`
   - Max Users: `50`
   - Click **Add**

   **Pool 2 - PublicPool:**
   - Pool Name: `PublicPool`
   - Default Gateway: `10.10.20.1`
   - DNS Server: `10.10.10.10`
   - Start IP: `10.10.20.100`
   - Subnet Mask: `255.255.255.0`
   - Max Users: `100`
   - Click **Add**

   **Pool 3 - IoTPool:**
   - Pool Name: `IoTPool`
   - Default Gateway: `10.10.30.1`
   - DNS Server: `10.10.10.10`
   - Start IP: `10.10.30.100`
   - Subnet Mask: `255.255.255.0`
   - Max Users: `50`
   - Click **Add**

---

### Web-Server (10.10.10.40)

1. Click device **"Web-Server"** in workspace
2. Click **Desktop** tab (at top of window)
3. Click **IP Configuration** from the menu

   **Fill in these fields:**
   - **IPv4 Address:** `10.10.10.40`
   - **Subnet Mask:** `255.255.255.0`
   - **Default Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

4. Click **Services** tab (at top of window)
5. Click **HTTP** from the left menu
6. Find the toggle/checkbox for **HTTP Service**
7. Turn it **ON** (click to enable)
8. If there's an **HTTPS** option, turn it **ON** too

---

### SMTP-Server (10.10.10.30)

1. Click device **"SMTP-Server"** in workspace
2. Click **Desktop** tab (at top of window)
3. Click **IP Configuration** from the menu

   **Fill in these fields:**
   - **IPv4 Address:** `10.10.10.30`
   - **Subnet Mask:** `255.255.255.0`
   - **Default Gateway:** `10.10.10.1`
   - **DNS Server:** `10.10.10.10`

4. Click **Services** tab (at top of window)
5. Click **EMAIL** from the left menu
6. Find **Service** and turn it **ON** (enable checkbox/toggle)
7. Find **Domain Name** field
8. Enter: `smartcity.local`

   **Add Email Users (one at a time):**

   **User 1:**
   - In the **User** field, type: `admin`
   - In the **Password** field, type: `admin123`
   - Click **+** or **Add** button

   **User 2:**
   - In the **User** field, type: `operations`
   - In the **Password** field, type: `ops123`
   - Click **+** or **Add** button

   **User 3:**
   - In the **User** field, type: `support`
   - In the **Password** field, type: `support123`
   - Click **+** or **Add** button

   **User 4:**
   - In the **User** field, type: `public`
   - In the **Password** field, type: `public123`
   - Click **+** or **Add** button

---

## STEP 6: Configure PCs (Set to DHCP)

For **ALL 4 PCs** (Admin-PC-1, Admin-PC-2, Public-Kiosk-PC, Resident-Home-PC):

1. Click PC → **Desktop** → **IP Configuration**
2. Select **DHCP** (radio button)
3. Wait - IP should appear automatically!
4. Verify DNS = `10.10.10.10`

---

## STEP 7: TEST! (This Will Work Now!)

### Test 1: Ping from Admin-PC-1

Click Admin-PC-1 → Desktop → Command Prompt:
```
ping 10.10.10.1        ← Gateway (should work!)
ping 10.10.10.10       ← DNS (should work!)
ping 10.10.10.40       ← Web (should work!)
ping 10.10.20.1        ← Other VLAN gateway (should work!)
```

### Test 2: DNS Resolution

From any PC:
```
nslookup web.smartcity.local
```
Should return: `10.10.10.40` ✅

### Test 3: Browse Web

From any PC → Desktop → Web Browser:
- Enter: `http://10.10.10.40`
- Or: `http://web.smartcity.local`
- Should load web page! ✅

### Test 4: Packet Simulation

1. Click **Simulation Mode** (bottom right)
2. Click **Add Simple PDU**
3. Click source PC
4. Click destination server
5. Click **Auto Capture/Play**
6. Watch packet travel successfully! ✅

---

## Why This Works:

```
Before (Router-on-a-stick - Complex):
Router with subinterfaces → Complex ACLs → Hard to configure

Now (Layer 3 Switch - Simple):
City-Core-Switch does ALL routing → Simple, clean, WORKS!
```

### Network Flow:
```
PC in VLAN 20 → City-Core-Switch Gi1/0/2 → VLAN 20 SVI (10.10.20.1)
                                                 ↓
                                    Routes to VLAN 10 SVI (10.10.10.1)
                                                 ↓
                                    Server in VLAN 10 receives packet ✅
```

---

## What About the Router?

**You don't need to configure it!** Just leave it as-is. The City-Core-Switch handles everything.

---

## Verification Commands:

### On City-Core-Switch:
```cisco
show ip interface brief       ← See all VLAN IPs
show ip route                 ← See routing table
show vlan brief              ← See VLANs
show interfaces trunk        ← See trunk ports
```

---

## Time Required: 20-30 minutes

**This WILL work - it's the simplest, most reliable configuration!** 🎯

No complex subinterfaces, no router headaches - just clean Layer 3 switching! ✅
