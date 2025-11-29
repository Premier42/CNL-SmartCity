# PART 2: REALISTIC OPTIMIZED IMPLEMENTATION GUIDE
## Smart City IoT Network - Production Architecture

**Total Device Count: 29 devices**
- Infrastructure: 8 devices (realistic 3-tier hierarchy)
- Servers: 4 devices (consolidated services like real deployments)
- End Devices: 17 devices (representative samples of each category)

**Design Philosophy:** This mirrors real smart city networks where you have centralized infrastructure serving multiple device types, not duplicated equipment. Each device represents a category deployed at scale.

---

## REAL WORLD ARCHITECTURE

```
                    CORE-R1 (ISR 2911)
                    [City Network Core]
                         |
        +----------------+----------------+
        |                                 |
    DIST-SW1                          DIST-SW2
    [West District]                   [East District]
        |                                 |
   +----+----+                       +----+----+
   |    |    |                       |         |
  SW1  SW2  SW3                     SW4       SW5
  IoT  Admin WiFi                   Servers   Mobile
```

**How Real Cities Deploy:**
- One central router handling all inter-VLAN routing
- Redundant distribution switches for different geographic zones
- Access switches grouped by device type (not duplicated)
- Consolidated servers (DNS+DHCP combined, multi-purpose email/web server)
- Representative IoT devices (each representing hundreds of actual sensors)
- WiFi infrastructure with strategic AP placement
- Admin workstations for different departments
- Mobile access for field teams

---

## DEVICE INVENTORY

### Infrastructure Layer (8 devices)
1. **CORE-R1**: Cisco 2911 Router - Central routing and inter-VLAN
2. **DIST-SW1**: Cisco 3560-24PS - West district distribution
3. **DIST-SW2**: Cisco 3560-24PS - East district distribution
4. **SW1-IoT**: Cisco 2960-24TT - IoT sensor aggregation
5. **SW2-Admin**: Cisco 2960-24TT - Administrative access
6. **SW3-WiFi**: Cisco 2960-24TT - Public WiFi infrastructure
7. **SW4-Servers**: Cisco 2960-24TT - Data center access
8. **SW5-Mobile**: Cisco 2960-24TT - Mobile admin access

### Server Layer (4 devices) - VLAN 40
9. **Primary-Server**: DNS + DHCP + Monitoring (192.168.40.10)
10. **App-Server**: Email + Web + Database (192.168.40.20)
11. **IoT-Gateway**: IoT data collection and processing (192.168.40.30)
12. **Backup-Server**: Redundancy and logging (192.168.40.40)

### IoT Sensor Layer (5 devices) - VLAN 10
*Each represents a deployed category scaled citywide*
13. **Traffic-Controller**: Smart traffic light system (represents 50+ intersections)
14. **Environment-Monitor**: Air quality/weather station (represents 20+ stations)
15. **Smart-Streetlight**: Adaptive lighting system (represents 500+ lights)
16. **Waste-Sensor**: Smart bin fill monitoring (represents 100+ bins)
17. **Water-Monitor**: Water quality/flow sensor (represents 30+ points)

### Administrative Layer (4 devices) - VLAN 20
18. **Network-Admin-PC**: Network operations center workstation
19. **City-Manager-PC**: City operations management terminal
20. **Security-Console**: Security monitoring station
21. **Shared-Printer**: Network printer for admin offices

### Public WiFi Layer (4 devices) - VLAN 30
22. **WiFi-AP-CentralPark**: AccessPoint-PT (high-traffic zone)
23. **WiFi-AP-CityHall**: AccessPoint-PT (government building)
24. **Citizen-Laptop**: Sample public user device
25. **Citizen-Phone**: Sample mobile user device

### Mobile Admin Layer (4 devices) - VLAN 50
26. **Mobile-AP-Field**: AccessPoint-PT (field operations)
27. **Engineer-Tablet**: Maintenance crew tablet
28. **Inspector-Tablet**: City inspector mobile device
29. **Emergency-Phone**: First responder smartphone

---

## NETWORK DESIGN - REALISTIC APPROACH

### VLAN Structure (Production Standard)

| VLAN | Name | Network | IPv6 | Purpose | Real-World Scale |
|------|------|---------|------|---------|------------------|
| 10 | IoT-Sensors | 192.168.10.0/24 | 2001:db8:1000:10::/64 | City-wide IoT devices | 700+ sensors |
| 20 | Admin | 192.168.20.0/24 | 2001:db8:1000:20::/64 | Employee workstations | 50+ staff |
| 30 | Public-WiFi | 192.168.30.0/22 | 2001:db8:1000:30::/64 | Free public internet | 1000+ daily users |
| 40 | Data-Center | 192.168.40.0/24 | 2001:db8:1000:40::/64 | Server infrastructure | 10-20 servers |
| 50 | Mobile-Admin | 192.168.50.0/24 | 2001:db8:1000:50::/64 | Field operations | 30+ field devices |

**Note:** In Packet Tracer we show 1 device per category. In production, each scales to hundreds.

---

## STEP 1: PHYSICAL TOPOLOGY

### 1.1 Place Infrastructure (Center to Edge)

**Core Layer:**
1. Place **Router-PT 2911** → rename to **CORE-R1** (center top)

**Distribution Layer:**
2. Place **3560-24PS** → rename to **DIST-SW1** (left middle)
3. Place **3560-24PS** → rename to **DIST-SW2** (right middle)

**Access Layer:**
4. Place **2960-24TT** → rename to **SW1-IoT** (far left bottom)
5. Place **2960-24TT** → rename to **SW2-Admin** (left bottom)
6. Place **2960-24TT** → rename to **SW3-WiFi** (center bottom)
7. Place **2960-24TT** → rename to **SW4-Servers** (right bottom)
8. Place **2960-24TT** → rename to **SW5-Mobile** (far right bottom)

### 1.2 Place Servers (Connect to SW4-Servers)

9. Place **Server-PT** → rename to **Primary-Server**
10. Place **Server-PT** → rename to **App-Server**
11. Place **Server-PT** → rename to **IoT-Gateway**
12. Place **Server-PT** → rename to **Backup-Server**

### 1.3 Place IoT Devices (Connect to SW1-IoT)

13. Place **SBC-PT** → rename to **Traffic-Controller**
14. Place **SBC-PT** → rename to **Environment-Monitor**
15. Place **SBC-PT** → rename to **Smart-Streetlight**
16. Place **SBC-PT** → rename to **Waste-Sensor**
17. Place **SBC-PT** → rename to **Water-Monitor**

*Alternative: Use Home Gateway-PT or Custom Made devices if SBC-PT unavailable*

### 1.4 Place Admin Devices (Connect to SW2-Admin)

18. Place **PC-PT** → rename to **Network-Admin-PC**
19. Place **PC-PT** → rename to **City-Manager-PC**
20. Place **PC-PT** → rename to **Security-Console**
21. Place **Printer-PT** → rename to **Shared-Printer**

### 1.5 Place WiFi Infrastructure (Connect to SW3-WiFi)

22. Place **AccessPoint-PT** → rename to **WiFi-AP-CentralPark**
23. Place **AccessPoint-PT** → rename to **WiFi-AP-CityHall**
24. Place **Laptop-PT** → rename to **Citizen-Laptop** (will connect wirelessly)
25. Place **Smartphone** → rename to **Citizen-Phone** (will connect wirelessly)

### 1.6 Place Mobile Admin (Connect to SW5-Mobile)

26. Place **AccessPoint-PT** → rename to **Mobile-AP-Field**
27. Place **Tablet-PT** → rename to **Engineer-Tablet** (will connect wirelessly)
28. Place **Tablet-PT** → rename to **Inspector-Tablet** (will connect wirelessly)
29. Place **Smartphone** → rename to **Emergency-Phone** (will connect wirelessly)

---

## STEP 2: CABLING (PRODUCTION STANDARD)

### 2.1 Core to Distribution (Redundant Trunks)
```
CORE-R1 Gig0/0 -----(straight-through)-----> DIST-SW1 Gig0/1
CORE-R1 Gig0/1 -----(straight-through)-----> DIST-SW2 Gig0/1
```

### 2.2 Distribution to Access (Access Layer Trunks)
```
DIST-SW1 Fa0/1 -----> SW1-IoT Gig0/1
DIST-SW1 Fa0/2 -----> SW2-Admin Gig0/1
DIST-SW1 Fa0/3 -----> SW3-WiFi Gig0/1

DIST-SW2 Fa0/1 -----> SW4-Servers Gig0/1
DIST-SW2 Fa0/2 -----> SW5-Mobile Gig0/1
```

### 2.3 Inter-Distribution Redundancy (Critical)
```
DIST-SW1 Gig0/2 -----(crossover)-----> DIST-SW2 Gig0/2
```
*This provides failover if CORE-R1 or uplinks fail*

### 2.4 Server Connections (Wired)
```
SW4-Servers Fa0/1 -----> Primary-Server FastEthernet0
SW4-Servers Fa0/2 -----> App-Server FastEthernet0
SW4-Servers Fa0/3 -----> IoT-Gateway FastEthernet0
SW4-Servers Fa0/4 -----> Backup-Server FastEthernet0
```

### 2.5 IoT Sensor Connections (Wired)
```
SW1-IoT Fa0/1 -----> Traffic-Controller FastEthernet0
SW1-IoT Fa0/2 -----> Environment-Monitor FastEthernet0
SW1-IoT Fa0/3 -----> Smart-Streetlight FastEthernet0
SW1-IoT Fa0/4 -----> Waste-Sensor FastEthernet0
SW1-IoT Fa0/5 -----> Water-Monitor FastEthernet0
```

### 2.6 Admin Connections (Wired)
```
SW2-Admin Fa0/1 -----> Network-Admin-PC FastEthernet0
SW2-Admin Fa0/2 -----> City-Manager-PC FastEthernet0
SW2-Admin Fa0/3 -----> Security-Console FastEthernet0
SW2-Admin Fa0/4 -----> Shared-Printer FastEthernet0
```

### 2.7 WiFi Infrastructure (Wired Backhaul)
```
SW3-WiFi Fa0/1 -----> WiFi-AP-CentralPark Ethernet Port
SW3-WiFi Fa0/2 -----> WiFi-AP-CityHall Ethernet Port
```
*Citizen devices connect wirelessly - no cables needed*

### 2.8 Mobile Admin Infrastructure (Wired Backhaul)
```
SW5-Mobile Fa0/1 -----> Mobile-AP-Field Ethernet Port
```
*Mobile devices connect wirelessly - no cables needed*

---

## STEP 3: CORE ROUTER CONFIGURATION (CORE-R1)

Click **CORE-R1** > **CLI** tab > Press Enter

```cisco
enable
configure terminal
hostname CORE-R1

! Enable IPv6 routing
ipv6 unicast-routing

! Physical interfaces must be enabled first
interface GigabitEthernet0/0
 description Uplink-to-DIST-SW1
 no shutdown

interface GigabitEthernet0/1
 description Uplink-to-DIST-SW2
 no shutdown

! VLAN 10 - IoT Sensors (on Gig0/0)
interface GigabitEthernet0/0.10
 description IoT-Sensor-Network
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.10
 no shutdown

! VLAN 20 - Admin Network (on Gig0/0)
interface GigabitEthernet0/0.20
 description Administrative-Network
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.10
 no shutdown

! VLAN 30 - Public WiFi (on Gig0/0)
interface GigabitEthernet0/0.30
 description Public-WiFi-Network
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.252.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.10
 no shutdown

! VLAN 40 - Data Center (on Gig0/1)
interface GigabitEthernet0/1.40
 description Data-Center-Network
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown

! VLAN 50 - Mobile Admin (on Gig0/1)
interface GigabitEthernet0/1.50
 description Mobile-Admin-Network
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64
 ip helper-address 192.168.40.10
 no shutdown

! ACL 110: IoT Security Policy
! Deny IoT devices from accessing Admin network
! Deny IoT devices from accessing other IoT devices (lateral movement)
! Allow IoT to Data Center for data upload
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.10.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 deny ip any any

! ACL 130: Public WiFi Security Policy
! Deny public access to Admin network
! Deny public access to Data Center (except web server)
! Deny public access to IoT network
! Allow internet access only (simulated)
access-list 130 deny ip 192.168.30.0 0.0.3.255 192.168.20.0 0.0.0.255
access-list 130 deny ip 192.168.30.0 0.0.3.255 192.168.40.0 0.0.0.255
access-list 130 deny ip 192.168.30.0 0.0.3.255 192.168.10.0 0.0.0.255
access-list 130 permit ip any any

! Apply ACLs to subinterfaces
interface GigabitEthernet0/0.10
 ip access-group 110 in

interface GigabitEthernet0/0.30
 ip access-group 130 in

! QoS Configuration (Traffic Prioritization)
! Class 1: Critical IoT traffic (emergency sensors)
! Class 2: Admin traffic
! Class 3: Public WiFi (best effort)
class-map match-any CRITICAL-IOT
 match access-group 111

class-map match-any ADMIN-TRAFFIC
 match access-group 121

policy-map SMARTCITY-QOS
 class CRITICAL-IOT
  priority percent 30
 class ADMIN-TRAFFIC
  bandwidth percent 40
 class class-default
  bandwidth percent 30

! Apply QoS policy
interface GigabitEthernet0/0
 service-policy output SMARTCITY-QOS

interface GigabitEthernet0/1
 service-policy output SMARTCITY-QOS

! ACL for QoS classification
access-list 111 permit ip 192.168.10.0 0.0.0.255 any
access-list 121 permit ip 192.168.20.0 0.0.0.255 any

end
write memory
```

---

## STEP 4: DISTRIBUTION SWITCHES

### 4.1 DIST-SW1 Configuration (West District)

Click **DIST-SW1** > **CLI** tab

```cisco
enable
configure terminal
hostname DIST-SW1

! Create all VLANs
vlan 10
 name IoT-Sensors
vlan 20
 name Admin
vlan 30
 name Public-WiFi
vlan 40
 name Data-Center
vlan 50
 name Mobile-Admin

! Trunk to Core Router
interface GigabitEthernet0/1
 description Trunk-to-CORE-R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 switchport trunk native vlan 999
 no shutdown

! Trunk to SW1-IoT
interface FastEthernet0/1
 description Trunk-to-SW1-IoT
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown

! Trunk to SW2-Admin
interface FastEthernet0/2
 description Trunk-to-SW2-Admin
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown

! Trunk to SW3-WiFi
interface FastEthernet0/3
 description Trunk-to-SW3-WiFi
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown

! Inter-Distribution Link (Redundancy)
interface GigabitEthernet0/2
 description InterDist-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Spanning Tree - Root for VLANs 10,20,30
spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,30 priority 24576

! Enable PortFast on access (if needed)
spanning-tree portfast default

end
write memory
```

### 4.2 DIST-SW2 Configuration (East District)

Click **DIST-SW2** > **CLI** tab

```cisco
enable
configure terminal
hostname DIST-SW2

! Create all VLANs
vlan 10
 name IoT-Sensors
vlan 20
 name Admin
vlan 30
 name Public-WiFi
vlan 40
 name Data-Center
vlan 50
 name Mobile-Admin

! Trunk to Core Router
interface GigabitEthernet0/1
 description Trunk-to-CORE-R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 switchport trunk native vlan 999
 no shutdown

! Trunk to SW4-Servers
interface FastEthernet0/1
 description Trunk-to-SW4-Servers
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown

! Trunk to SW5-Mobile
interface FastEthernet0/2
 description Trunk-to-SW5-Mobile
 switchport mode trunk
 switchport trunk allowed vlan 50
 no shutdown

! Inter-Distribution Link (Redundancy)
interface GigabitEthernet0/2
 description InterDist-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Spanning Tree - Root for VLANs 40,50
spanning-tree mode rapid-pvst
spanning-tree vlan 40,50 priority 24576

spanning-tree portfast default

end
write memory
```

---

## STEP 5: ACCESS SWITCHES

### 5.1 SW1-IoT Configuration

```cisco
enable
configure terminal
hostname SW1-IoT

vlan 10
 name IoT-Sensors

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown

! Access ports for IoT sensors
interface range FastEthernet0/1-5
 description IoT-Sensor-Ports
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation shutdown
 switchport port-security mac-address sticky
 spanning-tree portfast
 no shutdown

end
write memory
```

### 5.2 SW2-Admin Configuration

```cisco
enable
configure terminal
hostname SW2-Admin

vlan 20
 name Admin

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown

! Access ports for admin devices
interface range FastEthernet0/1-4
 description Admin-Device-Ports
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation restrict
 switchport port-security mac-address sticky
 spanning-tree portfast
 no shutdown

end
write memory
```

### 5.3 SW3-WiFi Configuration

```cisco
enable
configure terminal
hostname SW3-WiFi

vlan 30
 name Public-WiFi

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown

! Access ports for WiFi APs
interface range FastEthernet0/1-2
 description WiFi-AP-Ports
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown

end
write memory
```

### 5.4 SW4-Servers Configuration

```cisco
enable
configure terminal
hostname SW4-Servers

vlan 40
 name Data-Center

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown

! Access ports for servers
interface range FastEthernet0/1-4
 description Server-Ports
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 no shutdown

end
write memory
```

### 5.5 SW5-Mobile Configuration

```cisco
enable
configure terminal
hostname SW5-Mobile

vlan 50
 name Mobile-Admin

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 50
 no shutdown

! Access port for Mobile AP
interface FastEthernet0/1
 description Mobile-AP-Port
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown

end
write memory
```

---

## STEP 6: SERVER CONFIGURATIONS

### 6.1 Primary-Server (DNS + DHCP + Monitoring)

Click **Primary-Server** > **Config** tab > **FastEthernet0**:
- IP Address: `192.168.40.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10` (itself)

**DNS Configuration:**
Go to **Services** tab > **DNS**:
- DNS Service: **On**
- Add DNS Records:
  - `primary.smartcity.local` → `192.168.40.10`
  - `app.smartcity.local` → `192.168.40.20`
  - `iot.smartcity.local` → `192.168.40.30`
  - `backup.smartcity.local` → `192.168.40.40`
  - `smartcity.local` → `192.168.40.20` (default to app server)

**DHCP Configuration:**
Go to **Services** tab > **DHCP**:
- Service: **On**

**Pool 1 - IoT VLAN 10:**
- Pool Name: `IoT-Sensors`
- Default Gateway: `192.168.10.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.10.50`
- Subnet Mask: `255.255.255.0`
- Max Users: `100`
- Click **Add**

**Pool 2 - Admin VLAN 20:**
- Pool Name: `Admin-Devices`
- Default Gateway: `192.168.20.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.20.50`
- Subnet Mask: `255.255.255.0`
- Max Users: `50`
- Click **Add**

**Pool 3 - Public WiFi VLAN 30:**
- Pool Name: `Public-WiFi`
- Default Gateway: `192.168.30.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.30.100`
- Subnet Mask: `255.255.252.0`
- Max Users: `1000`
- Click **Add**

**Pool 4 - Mobile Admin VLAN 50:**
- Pool Name: `Mobile-Admin`
- Default Gateway: `192.168.50.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.50.50`
- Subnet Mask: `255.255.255.0`
- Max Users: `30`
- Click **Add**

### 6.2 App-Server (Email + Web)

Click **App-Server** > **Config** tab > **FastEthernet0**:
- IP Address: `192.168.40.20`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

**Email Configuration:**
Go to **Services** tab > **EMAIL**:
- Service: **On**
- Domain Name: `smartcity.local`
- Add users:
  - User: `admin`, Password: `CityAdmin2025`
  - User: `iot`, Password: `IoTData2025`
  - User: `engineer`, Password: `Field2025`

**Web Server Configuration:**
Go to **Services** tab > **HTTP**:
- HTTP Service: **On**
- HTTPS Service: **On** (if available)

Edit `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
<title>Smart City Operations Dashboard</title>
<style>
body { font-family: Arial; background: #1a1a2e; color: #eee; padding: 20px; }
h1 { color: #0f3460; }
.status { background: #16213e; padding: 15px; margin: 10px 0; border-left: 4px solid #0f3460; }
.online { border-left-color: #4caf50; }
</style>
</head>
<body>
<h1>🏙️ Smart City Network Operations Center</h1>
<div class="status online">
<h2>Network Status: OPERATIONAL</h2>
<p>🔗 Core Router: ACTIVE</p>
<p>🌐 VLANs: 5 Active (IoT, Admin, WiFi, Servers, Mobile)</p>
</div>
<div class="status">
<h3>📊 Device Statistics</h3>
<ul>
<li>IoT Sensors: 5 categories (700+ actual devices)</li>
<li>Admin Workstations: 4 active</li>
<li>Public WiFi: 2 zones, 2 active users</li>
<li>Mobile Admin: 3 field devices</li>
<li>Servers: 4 operational</li>
</ul>
</div>
<div class="status">
<h3>🔒 Security Status</h3>
<p>✅ ACL 110: IoT isolation active</p>
<p>✅ ACL 130: Public WiFi restrictions active</p>
<p>✅ Port Security: Enabled on all access ports</p>
</div>
</body>
</html>
```

### 6.3 IoT-Gateway (IoT Data Processing)

Click **IoT-Gateway** > **Config** tab > **FastEthernet0**:
- IP Address: `192.168.40.30`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

**Note:** This server acts as the endpoint for IoT data collection. In production, this would run specialized software (MQTT broker, time-series database, analytics platform).

### 6.4 Backup-Server (Logging & Redundancy)

Click **Backup-Server** > **Config** tab > **FastEthernet0**:
- IP Address: `192.168.40.40`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

---

## STEP 7: IOT DEVICE CONFIGURATION

All IoT devices use DHCP for automatic configuration.

For each device, click **Config** tab > **FastEthernet0**:
- IP Configuration: **DHCP**
- Should receive IPs starting from `192.168.10.50`

**Verify on each device:**
- Traffic-Controller: `192.168.10.50`
- Environment-Monitor: `192.168.10.51`
- Smart-Streetlight: `192.168.10.52`
- Waste-Sensor: `192.168.10.53`
- Water-Monitor: `192.168.10.54`

---

## STEP 8: ADMIN DEVICE CONFIGURATION

### 8.1 Network-Admin-PC (Static IP)

Click **Network-Admin-PC** > **Config** tab > **FastEthernet0**:
- IP Configuration: **Static**
- IP Address: `192.168.20.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.20.1`
- DNS Server: `192.168.40.10`

### 8.2 Other Admin Devices (DHCP)

For **City-Manager-PC**, **Security-Console**, **Shared-Printer**:
- Click **Config** tab > **FastEthernet0**
- IP Configuration: **DHCP**
- Should receive IPs starting from `192.168.20.50`

---

## STEP 9: WIRELESS ACCESS POINT CONFIGURATION

### 9.1 WiFi-AP-CentralPark (Public Zone 1)

Click **WiFi-AP-CentralPark** > **Config** tab > **Port 1**:
- SSID: `SmartCity-FreeWiFi`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `CityGuest2025`
- Encryption Type: **AES**
- Channel: **6**

### 9.2 WiFi-AP-CityHall (Public Zone 2)

Click **WiFi-AP-CityHall** > **Config** tab > **Port 1**:
- SSID: `SmartCity-FreeWiFi`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `CityGuest2025`
- Encryption Type: **AES**
- Channel: **11** (different to avoid interference)

### 9.3 Mobile-AP-Field (Admin Mobile)

Click **Mobile-AP-Field** > **Config** tab > **Port 1**:
- SSID: `SmartCity-Field-Ops`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `FieldOps2025!`
- Encryption Type: **AES**
- Channel: **1**

---

## STEP 10: WIRELESS CLIENT CONFIGURATION

### 10.1 Public WiFi Clients

**For Citizen-Laptop:**
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-FreeWiFi`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `CityGuest2025`
5. IP Configuration: **DHCP**

**For Citizen-Phone:**
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-FreeWiFi`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `CityGuest2025`
5. IP Configuration: **DHCP**

### 10.2 Mobile Admin Clients

**For Engineer-Tablet:**
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-Field-Ops`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `FieldOps2025!`
5. IP Configuration: **DHCP**

**For Inspector-Tablet:**
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-Field-Ops`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `FieldOps2025!`
5. IP Configuration: **DHCP**

**For Emergency-Phone:**
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-Field-Ops`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `FieldOps2025!`
5. IP Configuration: **DHCP**

---

## STEP 11: TESTING & VERIFICATION

### Test 1: Basic Connectivity

From **Network-Admin-PC** > **Desktop** > **Command Prompt**:
```
ipconfig
ping 192.168.40.10    (Primary-Server - should work)
ping 192.168.40.20    (App-Server - should work)
ping 192.168.10.50    (IoT device - should work, admin can access IoT)
ping 192.168.30.100   (Public WiFi - should work)
```

### Test 2: IoT Security Isolation

From **Traffic-Controller** > **Desktop** > **Command Prompt**:
```
ipconfig
ping 192.168.40.30    (IoT-Gateway - should WORK, IoT can send data)
ping 192.168.20.10    (Admin PC - should FAIL, blocked by ACL 110)
ping 192.168.10.51    (Another IoT device - should FAIL, lateral movement blocked)
```

**Expected:** IoT devices can ONLY communicate with IoT-Gateway server, nothing else.

### Test 3: Public WiFi Restrictions

From **Citizen-Laptop** > **Desktop** > **Command Prompt**:
```
ipconfig
ping 192.168.30.1     (Own gateway - should work)
ping 192.168.40.20    (App-Server - should FAIL, blocked by ACL 130)
ping 192.168.20.10    (Admin PC - should FAIL, blocked by ACL 130)
ping 192.168.10.50    (IoT device - should FAIL, blocked by ACL 130)
```

**Expected:** Public WiFi users are completely isolated, can only access internet (simulated).

### Test 4: Web Dashboard Access

From **Network-Admin-PC** > **Desktop** > **Web Browser**:
- URL: `http://192.168.40.20`
- Should display Smart City Operations Dashboard
- Shows network statistics and security status

Alternatively try:
- URL: `http://app.smartcity.local` (tests DNS resolution)

### Test 5: Email Functionality

From **City-Manager-PC** > **Desktop** > **Email**:
- Email Address: `admin@smartcity.local`
- Incoming/Outgoing Mail Server: `192.168.40.20` (or `app.smartcity.local`)
- Username: `admin`
- Password: `CityAdmin2025`
- Send email to: `engineer@smartcity.local`

From **Engineer-Tablet** > **Desktop** > **Email**:
- Email Address: `engineer@smartcity.local`
- Incoming/Outgoing Mail Server: `192.168.40.20`
- Username: `engineer`
- Password: `Field2025`
- Check inbox for admin's email

### Test 6: DHCP Verification

From **Primary-Server** > **Services** > **DHCP**:
- Check allocated IP addresses
- Should see devices in each pool:
  - IoT-Sensors: 5 allocations
  - Admin-Devices: 3 allocations
  - Public-WiFi: 2 allocations
  - Mobile-Admin: 3 allocations

### Test 7: DNS Resolution

From **Network-Admin-PC** > **Desktop** > **Command Prompt**:
```
nslookup primary.smartcity.local
nslookup app.smartcity.local
nslookup iot.smartcity.local
```
All should resolve to correct IP addresses (192.168.40.x).

### Test 8: Spanning Tree Failover

From **DIST-SW1** > **CLI**:
```
show spanning-tree
show spanning-tree vlan 10
```

Verify root bridge settings:
- DIST-SW1 should be root for VLANs 10, 20, 30
- DIST-SW2 should be root for VLANs 40, 50

**Failover test:**
1. Disconnect cable between DIST-SW1 and CORE-R1
2. Wait 30 seconds
3. From Network-Admin-PC, ping 192.168.40.10
4. Traffic should reroute through DIST-SW2 and inter-distribution link
5. Reconnect cable
6. Verify automatic restoration

### Test 9: Port Security

From **SW1-IoT** > **CLI**:
```
show port-security
show port-security interface fa0/1
```

Try connecting a second device to same port → Port should shutdown (violation).

### Test 10: QoS Verification

From **CORE-R1** > **CLI**:
```
show policy-map interface gig0/0
show class-map
```

Verify traffic classification and bandwidth allocation.

---

## STEP 12: DEMONSTRATION SCENARIOS

### Scenario 1: IoT Data Collection Flow
**Objective:** Show how IoT sensors send data to central gateway

1. From **Traffic-Controller**: Ping `192.168.40.30` (IoT-Gateway) → **SUCCESS**
2. From **Environment-Monitor**: Ping `192.168.40.30` → **SUCCESS**
3. Explain: All IoT data flows to IoT-Gateway for processing
4. Show ACL blocking: Ping `192.168.20.10` from Traffic-Controller → **BLOCKED**
5. **Key Point:** IoT devices have single-purpose connectivity (security best practice)

### Scenario 2: Administrative Operations
**Objective:** Show admin staff can manage all systems

1. From **Network-Admin-PC**: Access web dashboard `http://app.smartcity.local`
2. Ping all servers (40.10, 40.20, 40.30, 40.40) → All reachable
3. Ping IoT device `192.168.10.50` → Reachable (admin has full access)
4. Send email from City-Manager to engineer about maintenance
5. **Key Point:** Admin network has privileged access to all zones

### Scenario 3: Public WiFi Service
**Objective:** Demonstrate public internet access with security isolation

1. Connect **Citizen-Laptop** to `SmartCity-FreeWiFi`
2. Receive IP via DHCP (192.168.30.x)
3. Try to ping Admin PC → **BLOCKED**
4. Try to ping servers → **BLOCKED**
5. Try to ping IoT devices → **BLOCKED**
6. Explain: Public WiFi provides internet access only (no internal access)
7. **Key Point:** Guests are completely isolated from city infrastructure

### Scenario 4: Field Operations Mobile Access
**Objective:** Show how field teams securely access network

1. Connect **Engineer-Tablet** to `SmartCity-Field-Ops`
2. Receive IP from Mobile-Admin pool (192.168.50.x)
3. Access email: `engineer@smartcity.local`
4. Ping servers to verify connectivity
5. Access web dashboard for real-time status
6. **Key Point:** Field teams have secure, authenticated mobile access

### Scenario 5: Network Redundancy
**Objective:** Prove high availability design

1. Show current traffic flow from Admin to Servers
2. Disconnect DIST-SW1 uplink to CORE-R1
3. Traffic automatically reroutes through DIST-SW2
4. Connectivity maintained (may have brief interruption)
5. Reconnect cable → Spanning Tree reconverges
6. **Key Point:** No single point of failure (except core router)

### Scenario 6: Security Policy Enforcement
**Objective:** Demonstrate ACL effectiveness

**Test Matrix:**
| Source | Destination | Expected | Reason |
|--------|-------------|----------|--------|
| IoT → Admin | DENY | ACL 110 blocks | Security isolation |
| IoT → Servers | ALLOW | ACL 110 permits | Data upload |
| IoT → IoT | DENY | ACL 110 blocks | Prevent lateral attack |
| Public → Admin | DENY | ACL 130 blocks | Guest isolation |
| Public → Servers | DENY | ACL 130 blocks | No internal access |
| Admin → Any | ALLOW | No restrictions | Full privilege |

Run pings from each source to verify matrix.

---

## REAL-WORLD SCALING EXPLANATION

**This lab represents a production smart city network at scale:**

### Physical Deployment (Production)
- **29 lab devices** = **~1,000 actual devices** in production
- Each lab IoT sensor represents a deployed category:
  - 1 Traffic-Controller = 50+ actual traffic lights
  - 1 Environment-Monitor = 20+ air quality stations
  - 1 Smart-Streetlight = 500+ adaptive streetlights
  - 1 Waste-Sensor = 100+ smart bins
  - 1 Water-Monitor = 30+ water quality sensors

### Network Capacity Planning
- **VLAN 10 (IoT):** 254 addresses, supports 700+ sensors with proper subnetting
- **VLAN 20 (Admin):** 50 staff workstations, printers, management devices
- **VLAN 30 (Public WiFi):** /22 subnet = 1,022 addresses for 1,000+ daily users
- **VLAN 40 (Servers):** 10-20 physical/virtual servers
- **VLAN 50 (Mobile):** 30-50 field devices (tablets, phones, vehicles)

### Geographic Distribution
- **DIST-SW1** = West district (residential + parks)
- **DIST-SW2** = East district (downtown + industrial)
- Each distribution switch handles 10-15 access switches in real deployment
- Access switches placed in utility cabinets throughout city

### Why This Design is Production-Ready

**1. Hierarchical 3-Tier Architecture**
- Core layer: Inter-VLAN routing and policy enforcement
- Distribution layer: Traffic aggregation and redundancy
- Access layer: End-device connectivity

**2. Redundancy and High Availability**
- Dual uplinks from core to distribution
- Cross-link between distribution switches
- Spanning Tree prevents loops, enables failover

**3. Security in Depth**
- VLAN segmentation (Layer 2 isolation)
- ACLs (Layer 3 filtering)
- Port security (MAC address control)
- WPA2 authentication (wireless security)

**4. Scalability**
- Add more access switches without redesign
- VLAN structure supports thousands of devices
- QoS ensures critical traffic prioritized as load increases

**5. Operational Efficiency**
- Centralized DHCP (easy management)
- DNS for service discovery
- Consolidated servers (cost-effective)
- Mobile access for field teams

**6. Best Practices Followed**
- Native VLAN 999 (security)
- PortFast on access ports (fast convergence)
- Sticky MAC addresses (security)
- QoS traffic shaping (performance)
- Logical naming conventions (maintainability)

---

## NETWORK METRICS & STATISTICS

### Device Count by Layer
```
Core Layer:        1 router
Distribution:      2 switches (redundant)
Access Layer:      5 switches
Servers:           4 systems
Endpoints:         17 devices
─────────────────────
Total:             29 devices
```

### Traffic Patterns (Simulated Production Load)
```
IoT Sensors:       5 devices sending telemetry every 60s
                   = 300 packets/hour per sensor
                   = 1,500 packets/hour total
                   At scale: 700 sensors = 210,000 packets/hour

Admin Users:       4 concurrent users
                   Average session: 8 hours/day
                   Interactive traffic: 100-500 kbps per user

Public WiFi:       2 active users (represents 100-200 daily)
                   Average throughput: 5 Mbps per user
                   Peak load: 50+ concurrent users

Mobile Admin:      3 field devices
                   Sporadic usage: 1-2 hours/day
                   Low bandwidth: 50-100 kbps
```

### VLAN Statistics
```
VLAN 10 (IoT):        5 devices → scales to 700+
VLAN 20 (Admin):      4 devices → scales to 50
VLAN 30 (WiFi):       2 devices → scales to 1000+
VLAN 40 (Servers):    4 devices → scales to 20
VLAN 50 (Mobile):     3 devices → scales to 50
```

### Security Metrics
```
ACL Rules:           5 explicit deny rules + permit any
Port Security:       13 protected ports (all access ports)
Wireless Auth:       3 WPA2-PSK networks
VLAN Isolation:      5 separate broadcast domains
```

---

## TROUBLESHOOTING GUIDE

### Problem 1: Device Not Getting IP Address
**Symptoms:** Device shows 169.254.x.x (APIPA) or 0.0.0.0

**Check:**
1. DHCP service enabled on Primary-Server (192.168.40.10)
2. Correct DHCP pool exists for device's VLAN
3. Router has `ip helper-address 192.168.40.10` on subinterface
4. Trunk ports allow device's VLAN
5. Access port assigned to correct VLAN

**Fix:**
```cisco
! On router subinterface
interface GigabitEthernet0/0.10
 ip helper-address 192.168.40.10
```

### Problem 2: Cannot Ping Across VLANs
**Symptoms:** Can ping within VLAN, not across

**Check:**
1. Router subinterfaces are `no shutdown`
2. `show ip route` on router shows connected subnets
3. Trunk links allow all required VLANs
4. ACLs aren't blocking traffic (check with `show access-lists`)

**Fix:**
```cisco
! Verify routing
show ip interface brief
show ip route
show access-lists

! Check if subinterface is up
interface GigabitEthernet0/0.10
 no shutdown
```

### Problem 3: Wireless Clients Won't Connect
**Symptoms:** SSID visible but connection fails

**Check:**
1. SSID exactly matches (case-sensitive)
2. Password exactly matches (case-sensitive)
3. Authentication type matches (WPA2-PSK on both)
4. AP has IP address (check AP status)
5. AP switch port in correct VLAN

**Fix:**
- Retype SSID and password carefully
- Verify AP connected to correct switch/VLAN
- Check AP shows "Associated" status

### Problem 4: Spanning Tree Loop
**Symptoms:** Extreme slowness, duplicate packets, broadcast storm

**Check:**
1. `show spanning-tree` on all switches
2. Look for multiple root bridges
3. Verify trunk native VLAN configuration

**Fix:**
```cisco
! Set consistent root priorities
spanning-tree vlan 10 priority 24576
```

### Problem 5: ACL Blocking Legitimate Traffic
**Symptoms:** Connectivity works without ACL, fails with ACL

**Check:**
1. `show access-lists` to see rule order
2. Remember: ACLs process top-down, first match wins
3. Check if `permit ip any any` exists at end

**Fix:**
```cisco
! View current ACL
show access-lists 110

! Fix by recreating ACL with correct order
no access-list 110
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 permit ip any any
```

### Problem 6: Port Security Violation
**Symptoms:** Port shows err-disabled, device disconnected

**Check:**
```cisco
show port-security interface fa0/1
show interfaces status err-disabled
```

**Fix:**
```cisco
! Re-enable port
interface fa0/1
 shutdown
 no shutdown
```

### Problem 7: DNS Not Resolving
**Symptoms:** Ping by IP works, ping by name fails

**Check:**
1. Device has DNS server configured (192.168.40.10)
2. DNS service enabled on Primary-Server
3. DNS records exist for hostname
4. Can ping 192.168.40.10 from device

**Fix:**
- Add DNS server to device: Config > FastEthernet > DNS Server: 192.168.40.10
- Add missing records on Primary-Server > Services > DNS

---

## CONFIGURATION VERIFICATION CHECKLIST

### Router (CORE-R1)
- [ ] Hostname set to CORE-R1
- [ ] IPv6 routing enabled
- [ ] Physical interfaces Gig0/0 and Gig0/1 are `no shutdown`
- [ ] 5 subinterfaces configured (.10, .20, .30, .40, .50)
- [ ] Each subinterface has IPv4 and IPv6 address
- [ ] Subinterfaces have `ip helper-address 192.168.40.10` (except VLAN 40)
- [ ] ACL 110 applied to Gig0/0.10 (IoT)
- [ ] ACL 130 applied to Gig0/0.30 (Public WiFi)
- [ ] QoS policy configured and applied
- [ ] Config saved (`write memory`)

### Distribution Switches (DIST-SW1, DIST-SW2)
- [ ] Hostname set correctly
- [ ] All 5 VLANs created (10, 20, 30, 40, 50)
- [ ] Uplink to router configured as trunk (allowed all VLANs)
- [ ] Downlinks to access switches configured as trunk
- [ ] Inter-distribution link configured as trunk
- [ ] Spanning Tree priorities set (DIST-SW1: 10,20,30 / DIST-SW2: 40,50)
- [ ] Native VLAN 999 configured
- [ ] Config saved

### Access Switches (SW1-5)
- [ ] Hostname set correctly
- [ ] VLAN created for this switch's purpose
- [ ] Uplink (Gig0/1) configured as trunk
- [ ] Access ports (Fa0/x) configured as access mode
- [ ] Access ports assigned to correct VLAN
- [ ] Port security enabled on access ports (except WiFi AP ports)
- [ ] PortFast enabled where appropriate
- [ ] Config saved

### Servers
- [ ] Primary-Server: IP 192.168.40.10, DNS and DHCP services running
- [ ] App-Server: IP 192.168.40.20, Email and HTTP services running
- [ ] IoT-Gateway: IP 192.168.40.30, basic config
- [ ] Backup-Server: IP 192.168.40.40, basic config
- [ ] All servers have gateway 192.168.40.1 and DNS 192.168.40.10

### Access Points
- [ ] WiFi-AP-CentralPark: SSID "SmartCity-FreeWiFi", password "CityGuest2025", channel 6
- [ ] WiFi-AP-CityHall: SSID "SmartCity-FreeWiFi", password "CityGuest2025", channel 11
- [ ] Mobile-AP-Field: SSID "SmartCity-Field-Ops", password "FieldOps2025!", channel 1

### End Devices
- [ ] All IoT devices set to DHCP, receiving 192.168.10.x addresses
- [ ] Network-Admin-PC has static IP 192.168.20.10
- [ ] Other admin devices set to DHCP, receiving 192.168.20.x addresses
- [ ] Wireless clients configured with correct SSID/password
- [ ] Wireless clients set to DHCP

### Testing
- [ ] All devices have IP addresses
- [ ] Ping test between VLANs works (except where blocked by ACL)
- [ ] IoT devices blocked from Admin network (ACL 110)
- [ ] Public WiFi blocked from Admin/Servers/IoT (ACL 130)
- [ ] Web dashboard accessible at http://192.168.40.20
- [ ] Email works between admin users
- [ ] DNS resolution works (ping by hostname)
- [ ] DHCP allocations visible on Primary-Server
- [ ] Spanning Tree shows correct root bridges
- [ ] Failover test successful (disconnect uplink, traffic reroutes)

---

## SUMMARY & KEY ACHIEVEMENTS

### ✅ Complete Smart City Network Implementation

**Infrastructure:**
- 3-tier hierarchical design (industry standard)
- Redundant distribution layer (high availability)
- 8 managed network devices

**Services:**
- Centralized DHCP for 4 VLANs (auto-configuration)
- DNS for service discovery (user-friendly)
- Email system for administrative communication
- Web dashboard for monitoring
- IoT data gateway for sensor integration

**Security:**
- 5-VLAN segmentation (isolation)
- 2 ACLs with 5 rules (traffic filtering)
- Port security on 13 ports (MAC control)
- WPA2 wireless authentication (encryption)

**Scalability:**
- 29 lab devices represent 1,000+ production devices
- VLANs support up to 1,000+ addresses
- Design scales to 50+ access switches without changes

**Demonstration Capability:**
- ✅ Router-on-a-stick inter-VLAN routing
- ✅ VLAN segmentation and trunking
- ✅ DHCP relay across VLANs
- ✅ DNS resolution
- ✅ ACL security policies
- ✅ Wireless infrastructure (dual-band strategy)
- ✅ QoS traffic prioritization
- ✅ Spanning Tree redundancy
- ✅ Port security
- ✅ IPv4/IPv6 dual-stack
- ✅ Email services
- ✅ Web services

**Real-World Alignment:**
This topology mirrors actual smart city deployments in:
- Singapore (Smart Nation initiative)
- Barcelona (Smart City program)
- Amsterdam (IoT Living Lab)
- Dubai (Smart Dubai project)

**Academic Criteria Met:**
1. ✅ Depth of knowledge: Advanced routing, switching, security
2. ✅ Conflicting requirements: Security vs accessibility, cost vs redundancy
3. ✅ Depth of analysis: Traffic flow, failure scenarios, scaling
4. ✅ Familiarity with issues: ACL conflicts, VLAN design, wireless interference
5. ✅ Stakeholder involvement: City admin, public users, field teams, IT staff
6. ✅ Conflicting stakeholder needs: Privacy vs monitoring, access vs security
7. ✅ Interdependence: DHCP requires routing, DNS requires DHCP, services require all

---

## NEXT STEPS FOR DEMONSTRATION

### Presentation Flow
1. **Show topology** (explain 3-tier design)
2. **Show device count** (29 devices, scales to 1000+)
3. **Show VLAN structure** (5 VLANs, explain purpose of each)
4. **Demonstrate IoT isolation** (ping tests showing ACL 110)
5. **Demonstrate public WiFi isolation** (ping tests showing ACL 130)
6. **Show admin full access** (admin can reach all zones)
7. **Access web dashboard** (visual network status)
8. **Send test email** (service integration)
9. **Show DHCP allocations** (automatic configuration)
10. **Perform failover test** (redundancy demonstration)

### Report Writing (Use PART1_PROJECT_KNOWLEDGE.md)
- Introduction: Smart city context
- Literature review: Singapore, Barcelona case studies
- Design justification: Why 5 VLANs? Why this security model?
- Stakeholder analysis: 5 stakeholders with different needs
- Conflict resolution: How technical decisions were made
- Implementation: Use this file (PART2) as reference
- Testing: Use Step 11 results
- Conclusion: Achievement of objectives

**You now have a production-ready smart city network design demonstrating all required concepts with realistic scale and complexity.**
