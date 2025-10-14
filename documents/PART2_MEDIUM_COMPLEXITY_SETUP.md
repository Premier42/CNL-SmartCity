# PART 2: MEDIUM COMPLEXITY IMPLEMENTATION GUIDE
## Smart City IoT Network with IPv6 and QoS

**Total Device Count: 41 devices**
- Infrastructure: 8 devices (1 router, 2 distribution switches, 5 access switches)
- Servers: 5 devices (DNS, DHCP, Email, Web, Monitoring)
- End Devices: 28 devices across 5 VLANs

This setup demonstrates complexity while remaining manageable for demonstration and testing.

---

## NETWORK TOPOLOGY OVERVIEW

```
                    CORE-R1 (Router 2911)
                         |
        +----------------+----------------+
        |                                 |
    DIST-SW1                          DIST-SW2
    (3560-24PS)                       (3560-24PS)
        |                                 |
   +----+----+                       +----+----+
   |    |    |                       |         |
  SW1  SW2  SW3                     SW4       SW5
       IoT  Admin                   WiFi    Servers
```

---

## DEVICE INVENTORY

### Infrastructure Devices (8)
1. **CORE-R1**: Cisco 2911 Router
2. **DIST-SW1**: Cisco 3560-24PS Switch
3. **DIST-SW2**: Cisco 3560-24PS Switch
4. **SW1-IoT**: Cisco 2960-24TT Switch
5. **SW2-Admin**: Cisco 2960-24TT Switch
6. **SW3-Mobile**: Cisco 2960-24TT Switch
7. **SW4-WiFi**: Cisco 2960-24TT Switch
8. **SW5-Servers**: Cisco 2960-24TT Switch

### Server Devices (5) - VLAN 40
9. **DNS-Server**: 192.168.40.10
10. **DHCP-Server**: 192.168.40.20
11. **Email-Server**: 192.168.40.30
12. **Web-Server**: 192.168.40.40
13. **Monitor-Server**: 192.168.40.50

### IoT Devices (6) - VLAN 10
14. **TrafficSensor-01**: Smart traffic light sensor
15. **TrafficSensor-02**: Traffic flow monitor
16. **AirQuality-01**: Air quality sensor
17. **AirQuality-02**: Air quality sensor
18. **SmartBin-01**: Waste management sensor
19. **WaterMeter-01**: Smart water meter

### Admin Devices (5) - VLAN 20
20. **Admin-PC-01**: Network administrator workstation
21. **Admin-PC-02**: City operations manager workstation
22. **Admin-PC-03**: Security monitoring workstation
23. **Printer-01**: Network printer
24. **Admin-Laptop-01**: Mobile admin laptop

### Public WiFi (8) - VLAN 30
25. **WiFi-AP-01**: AccessPoint-PT (north zone)
26. **WiFi-AP-02**: AccessPoint-PT (south zone)
27. **Public-Laptop-01**: Wireless client
28. **Public-Laptop-02**: Wireless client
29. **Public-Smartphone-01**: Wireless client
30. **Public-Smartphone-02**: Wireless client
31. **Public-Tablet-01**: Wireless tablet
32. **Public-Tablet-02**: Wireless tablet

### Mobile Admin (4) - VLAN 50
33. **Mobile-AP-01**: AccessPoint-PT (admin mobile access)
34. **Admin-Tablet-01**: iPad/Tablet for field engineers
35. **Admin-Tablet-02**: iPad/Tablet for maintenance crew
36. **Admin-Phone-01**: Smartphone for emergency response

### Test/Demo Devices (5 additional)
37. **IoT-Camera-01**: Security camera (VLAN 10)
38. **Emergency-PC-01**: Emergency services PC (VLAN 20)
39. **Kiosk-PC-01**: Public information kiosk (VLAN 30)
40. **Admin-Tablet-03**: Backup admin device (VLAN 50)
41. **Test-Laptop-01**: Testing device (can be moved between VLANs)

---

## VLAN STRUCTURE

| VLAN | Name | Network | IPv6 Network | Devices |
|------|------|---------|--------------|---------|
| 10 | IoT | 192.168.10.0/24 | 2001:db8:1000:10::/64 | 7 IoT sensors/cameras |
| 20 | Admin | 192.168.20.0/24 | 2001:db8:1000:20::/64 | 6 admin devices |
| 30 | Public WiFi | 192.168.30.0/24 | 2001:db8:1000:30::/64 | 10 public wireless |
| 40 | Servers | 192.168.40.0/24 | 2001:db8:1000:40::/64 | 5 servers |
| 50 | Mobile Admin | 192.168.50.0/24 | 2001:db8:1000:50::/64 | 5 mobile devices |

---

## STEP 1: PLACE ALL DEVICES

### 1.1 Infrastructure Layer
1. Place **Router-PT** (rename to CORE-R1) - center top
2. Place **3560-24PS** (rename to DIST-SW1) - left middle
3. Place **3560-24PS** (rename to DIST-SW2) - right middle
4. Place five **2960-24TT** switches below:
   - SW1-IoT (far left)
   - SW2-Admin (center left)
   - SW3-Mobile (center)
   - SW4-WiFi (center right)
   - SW5-Servers (far right)

### 1.2 Server Layer (Connect to SW5-Servers)
5. Place 5 **Server-PT** devices:
   - DNS-Server
   - DHCP-Server
   - Email-Server
   - Web-Server
   - Monitor-Server

### 1.3 IoT Layer (Connect to SW1-IoT)
6. Place IoT devices (use appropriate icons from End Devices > Custom Made):
   - TrafficSensor-01 (SBC-PT or Custom)
   - TrafficSensor-02
   - AirQuality-01
   - AirQuality-02
   - SmartBin-01
   - WaterMeter-01
   - IoT-Camera-01 (IP Camera or Webcam)

### 1.4 Admin Layer (Connect to SW2-Admin)
7. Place admin devices:
   - Admin-PC-01 (PC-PT)
   - Admin-PC-02 (PC-PT)
   - Admin-PC-03 (PC-PT)
   - Printer-01 (Printer-PT)
   - Admin-Laptop-01 (Laptop-PT)
   - Emergency-PC-01 (PC-PT)

### 1.5 Public WiFi Layer (Connect to SW4-WiFi)
8. Place 2 **AccessPoint-PT** (WiFi-AP-01, WiFi-AP-02)
9. Place wireless clients (connect wirelessly):
   - Public-Laptop-01 (Laptop-PT)
   - Public-Laptop-02 (Laptop-PT)
   - Public-Smartphone-01 (Smartphone)
   - Public-Smartphone-02 (Smartphone)
   - Public-Tablet-01 (Tablet-PT)
   - Public-Tablet-02 (Tablet-PT)
   - Kiosk-PC-01 (PC-PT)
   - Test-Laptop-01 (Laptop-PT)

### 1.6 Mobile Admin Layer (Connect to SW3-Mobile)
10. Place 1 **AccessPoint-PT** (Mobile-AP-01)
11. Place wireless admin devices:
    - Admin-Tablet-01 (Tablet-PT)
    - Admin-Tablet-02 (Tablet-PT)
    - Admin-Tablet-03 (Tablet-PT)
    - Admin-Phone-01 (Smartphone)

---

## STEP 2: CABLE CONNECTIONS

### 2.1 Core to Distribution (Trunks)
```
CORE-R1 Gig0/0 -----(straight)-----> DIST-SW1 Gig0/1
CORE-R1 Gig0/1 -----(straight)-----> DIST-SW2 Gig0/1
```

### 2.2 Distribution to Access (Trunks)
```
DIST-SW1 Fa0/1 -----(straight)-----> SW1-IoT Gig0/1
DIST-SW1 Fa0/2 -----(straight)-----> SW2-Admin Gig0/1
DIST-SW1 Fa0/3 -----(straight)-----> SW3-Mobile Gig0/1

DIST-SW2 Fa0/1 -----(straight)-----> SW4-WiFi Gig0/1
DIST-SW2 Fa0/2 -----(straight)-----> SW5-Servers Gig0/1
```

### 2.3 Inter-Distribution Link (Trunk)
```
DIST-SW1 Gig0/2 -----(crossover)-----> DIST-SW2 Gig0/2
```

### 2.4 Server Connections (Access Ports)
```
SW5-Servers Fa0/1 -----> DNS-Server (FastEthernet)
SW5-Servers Fa0/2 -----> DHCP-Server (FastEthernet)
SW5-Servers Fa0/3 -----> Email-Server (FastEthernet)
SW5-Servers Fa0/4 -----> Web-Server (FastEthernet)
SW5-Servers Fa0/5 -----> Monitor-Server (FastEthernet)
```

### 2.5 IoT Device Connections
```
SW1-IoT Fa0/1 -----> TrafficSensor-01
SW1-IoT Fa0/2 -----> TrafficSensor-02
SW1-IoT Fa0/3 -----> AirQuality-01
SW1-IoT Fa0/4 -----> AirQuality-02
SW1-IoT Fa0/5 -----> SmartBin-01
SW1-IoT Fa0/6 -----> WaterMeter-01
SW1-IoT Fa0/7 -----> IoT-Camera-01
```

### 2.6 Admin Device Connections
```
SW2-Admin Fa0/1 -----> Admin-PC-01
SW2-Admin Fa0/2 -----> Admin-PC-02
SW2-Admin Fa0/3 -----> Admin-PC-03
SW2-Admin Fa0/4 -----> Printer-01
SW2-Admin Fa0/5 -----> Admin-Laptop-01
SW2-Admin Fa0/6 -----> Emergency-PC-01
```

### 2.7 WiFi Infrastructure
```
SW4-WiFi Fa0/1 -----> WiFi-AP-01 (Ethernet port)
SW4-WiFi Fa0/2 -----> WiFi-AP-02 (Ethernet port)
SW4-WiFi Fa0/3 -----> Kiosk-PC-01 (wired kiosk)
```

### 2.8 Mobile Admin Infrastructure
```
SW3-Mobile Fa0/1 -----> Mobile-AP-01 (Ethernet port)
```

**Wireless connections** (automatic once APs are configured):
- Public wireless devices connect to WiFi-AP-01 or WiFi-AP-02
- Mobile admin devices connect to Mobile-AP-01

---

## STEP 3: ROUTER CONFIGURATION (CORE-R1)

Click on **CORE-R1** > **CLI** tab > Press Enter

```cisco
enable
configure terminal
hostname CORE-R1

! Enable IPv6 routing
ipv6 unicast-routing

! Subinterface for VLAN 10 (IoT)
interface GigabitEthernet0/0.10
 description IoT-Sensors-VLAN
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.20
 no shutdown

! Subinterface for VLAN 20 (Admin)
interface GigabitEthernet0/0.20
 description Admin-Devices-VLAN
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.20
 no shutdown

! Subinterface for VLAN 30 (Public WiFi)
interface GigabitEthernet0/0.30
 description Public-WiFi-VLAN
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.20
 no shutdown

! Subinterface for VLAN 40 (Servers)
interface GigabitEthernet0/1.40
 description Server-VLAN
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown

! Subinterface for VLAN 50 (Mobile Admin)
interface GigabitEthernet0/1.50
 description Mobile-Admin-VLAN
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64
 ip helper-address 192.168.40.20
 no shutdown

! Enable physical interfaces
interface GigabitEthernet0/0
 no shutdown

interface GigabitEthernet0/1
 no shutdown

! ACL 110: IoT Security (Block IoT from Admin)
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 permit ip any any

! ACL 130: Public WiFi Restrictions
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 130 permit ip any any

! Apply ACLs
interface GigabitEthernet0/0.10
 ip access-group 110 in

interface GigabitEthernet0/0.30
 ip access-group 130 in

! Save configuration
end
write memory
```

---

## STEP 4: DISTRIBUTION SWITCHES CONFIGURATION

### 4.1 DIST-SW1 Configuration

Click on **DIST-SW1** > **CLI** tab

```cisco
enable
configure terminal
hostname DIST-SW1

! Create VLANs
vlan 10
 name IoT-Devices
vlan 20
 name Admin-Devices
vlan 30
 name Public-WiFi
vlan 40
 name Servers
vlan 50
 name Mobile-Admin

! Configure trunk to router
interface GigabitEthernet0/1
 description Trunk-to-CORE-R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Configure trunk to SW1-IoT
interface FastEthernet0/1
 description Trunk-to-SW1-IoT
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown

! Configure trunk to SW2-Admin
interface FastEthernet0/2
 description Trunk-to-SW2-Admin
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown

! Configure trunk to SW3-Mobile
interface FastEthernet0/3
 description Trunk-to-SW3-Mobile
 switchport mode trunk
 switchport trunk allowed vlan 50
 no shutdown

! Configure trunk to DIST-SW2
interface GigabitEthernet0/2
 description Trunk-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Enable Spanning Tree
spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,50 priority 24576

end
write memory
```

### 4.2 DIST-SW2 Configuration

Click on **DIST-SW2** > **CLI** tab

```cisco
enable
configure terminal
hostname DIST-SW2

! Create VLANs
vlan 10
 name IoT-Devices
vlan 20
 name Admin-Devices
vlan 30
 name Public-WiFi
vlan 40
 name Servers
vlan 50
 name Mobile-Admin

! Configure trunk to router
interface GigabitEthernet0/1
 description Trunk-to-CORE-R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Configure trunk to SW4-WiFi
interface FastEthernet0/1
 description Trunk-to-SW4-WiFi
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown

! Configure trunk to SW5-Servers
interface FastEthernet0/2
 description Trunk-to-SW5-Servers
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown

! Configure trunk to DIST-SW1
interface GigabitEthernet0/2
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
 no shutdown

! Enable Spanning Tree
spanning-tree mode rapid-pvst
spanning-tree vlan 30,40 priority 24576

end
write memory
```

---

## STEP 5: ACCESS SWITCHES CONFIGURATION

### 5.1 SW1-IoT Configuration

```cisco
enable
configure terminal
hostname SW1-IoT

vlan 10
 name IoT-Devices

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown

! Access ports for IoT devices
interface range FastEthernet0/1-7
 description IoT-Sensors
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 no shutdown

spanning-tree mode rapid-pvst
end
write memory
```

### 5.2 SW2-Admin Configuration

```cisco
enable
configure terminal
hostname SW2-Admin

vlan 20
 name Admin-Devices

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown

! Access ports for admin devices
interface range FastEthernet0/1-6
 description Admin-Workstations
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 no shutdown

spanning-tree mode rapid-pvst
end
write memory
```

### 5.3 SW3-Mobile Configuration

```cisco
enable
configure terminal
hostname SW3-Mobile

vlan 50
 name Mobile-Admin

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW1
 switchport mode trunk
 switchport trunk allowed vlan 50
 no shutdown

! Access port for Mobile AP
interface FastEthernet0/1
 description Mobile-Admin-AP
 switchport mode access
 switchport access vlan 50
 no shutdown

spanning-tree mode rapid-pvst
end
write memory
```

### 5.4 SW4-WiFi Configuration

```cisco
enable
configure terminal
hostname SW4-WiFi

vlan 30
 name Public-WiFi

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown

! Access ports for WiFi APs
interface range FastEthernet0/1-3
 description WiFi-Access-Points
 switchport mode access
 switchport access vlan 30
 no shutdown

spanning-tree mode rapid-pvst
end
write memory
```

### 5.5 SW5-Servers Configuration

```cisco
enable
configure terminal
hostname SW5-Servers

vlan 40
 name Servers

! Trunk to distribution
interface GigabitEthernet0/1
 description Trunk-to-DIST-SW2
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown

! Access ports for servers
interface range FastEthernet0/1-5
 description Server-Devices
 switchport mode access
 switchport access vlan 40
 no shutdown

spanning-tree mode rapid-pvst
end
write memory
```

---

## STEP 6: SERVER CONFIGURATIONS

### 6.1 DNS Server (192.168.40.10)

Click on **DNS-Server** > **Config** tab > **FastEthernet0**
- IP Address: `192.168.40.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`

Go to **Services** tab > **DNS**:
- DNS Service: **On**
- Add Records:
  - `dns.smartcity.local` → `192.168.40.10`
  - `dhcp.smartcity.local` → `192.168.40.20`
  - `mail.smartcity.local` → `192.168.40.30`
  - `web.smartcity.local` → `192.168.40.40`
  - `monitor.smartcity.local` → `192.168.40.50`

### 6.2 DHCP Server (192.168.40.20)

Click on **DHCP-Server** > **Config** tab > **FastEthernet0**
- IP Address: `192.168.40.20`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

Go to **Services** tab > **DHCP**:
- Service: **On**

**Pool 1 - IoT VLAN 10:**
- Pool Name: `IoT-Pool`
- Default Gateway: `192.168.10.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.10.100`
- Subnet Mask: `255.255.255.0`
- Max Users: `50`
- Click **Add**

**Pool 2 - Admin VLAN 20:**
- Pool Name: `Admin-Pool`
- Default Gateway: `192.168.20.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.20.100`
- Subnet Mask: `255.255.255.0`
- Max Users: `30`
- Click **Add**

**Pool 3 - Public WiFi VLAN 30:**
- Pool Name: `WiFi-Pool`
- Default Gateway: `192.168.30.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.30.100`
- Subnet Mask: `255.255.255.0`
- Max Users: `100`
- Click **Add**

**Pool 4 - Mobile Admin VLAN 50:**
- Pool Name: `Mobile-Pool`
- Default Gateway: `192.168.50.1`
- DNS Server: `192.168.40.10`
- Start IP: `192.168.50.100`
- Subnet Mask: `255.255.255.0`
- Max Users: `20`
- Click **Add**

### 6.3 Email Server (192.168.40.30)

Click on **Email-Server** > **Config** tab > **FastEthernet0**
- IP Address: `192.168.40.30`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

Go to **Services** tab > **EMAIL**:
- Service: **On**
- Domain Name: `smartcity.local`
- Add user accounts:
  - User: `admin`, Password: `admin123`
  - User: `iot`, Password: `iot123`
  - User: `monitor`, Password: `monitor123`

### 6.4 Web Server (192.168.40.40)

Click on **Web-Server** > **Config** tab > **FastEthernet0**
- IP Address: `192.168.40.40`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

Go to **Services** tab > **HTTP**:
- Service: **On**
- Edit `index.html`:
```html
<html>
<head><title>Smart City Dashboard</title></head>
<body>
<h1>Smart City IoT Network</h1>
<h2>Network Status: ONLINE</h2>
<p>Total Devices: 41</p>
<p>VLANs Active: 5</p>
<ul>
<li>IoT Sensors: 7 devices</li>
<li>Admin Workstations: 6 devices</li>
<li>Public WiFi Users: 10 devices</li>
<li>Servers: 5 systems</li>
<li>Mobile Admin: 5 devices</li>
</ul>
</body>
</html>
```

### 6.5 Monitoring Server (192.168.40.50)

Click on **Monitor-Server** > **Config** tab > **FastEthernet0**
- IP Address: `192.168.40.50`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

---

## STEP 7: WIRELESS ACCESS POINTS CONFIGURATION

### 7.1 WiFi-AP-01 (Public WiFi)

Click on **WiFi-AP-01** > **Config** tab > **Port 1**
- SSID: `SmartCity-Public`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `publicwifi2025`
- Encryption Type: **AES**
- Channel: `6`

### 7.2 WiFi-AP-02 (Public WiFi)

Click on **WiFi-AP-02** > **Config** tab > **Port 1**
- SSID: `SmartCity-Public`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `publicwifi2025`
- Encryption Type: **AES**
- Channel: `11`

### 7.3 Mobile-AP-01 (Admin Mobile)

Click on **Mobile-AP-01** > **Config** tab > **Port 1**
- SSID: `SmartCity-Admin-Mobile`
- Authentication: **WPA2-PSK**
- PSK Pass Phrase: `adminmobile2025`
- Encryption Type: **AES**
- Channel: `1`

---

## STEP 8: END DEVICE CONFIGURATION

### 8.1 IoT Devices (Auto-DHCP)

For each IoT device, click **Config** tab > **FastEthernet0**:
- IP Configuration: **DHCP**
- All should receive addresses in `192.168.10.100-150` range

### 8.2 Admin Devices

**Static IP for Admin-PC-01:**
- IP: `192.168.20.10`
- Mask: `255.255.255.0`
- Gateway: `192.168.20.1`
- DNS: `192.168.40.10`

**DHCP for others:**
- Admin-PC-02, Admin-PC-03, Printer-01, Admin-Laptop-01, Emergency-PC-01: **DHCP**

### 8.3 Wireless Client Configuration

**For all Public WiFi devices** (Laptops, Smartphones, Tablets, Kiosk):
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-Public`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `publicwifi2025`
5. IP Configuration: **DHCP**

**For all Mobile Admin devices** (Tablets, Phone):
1. Click device > **Config** tab > **Wireless0**
2. SSID: `SmartCity-Admin-Mobile`
3. Authentication: **WPA2-PSK**
4. PSK Pass Phrase: `adminmobile2025`
5. IP Configuration: **DHCP**

---

## STEP 9: TESTING AND VERIFICATION

### 9.1 Basic Connectivity Tests

From **Admin-PC-01** > **Desktop** tab > **Command Prompt**:

```
ping 192.168.40.10    (DNS Server - Should work)
ping 192.168.40.20    (DHCP Server - Should work)
ping 192.168.10.100   (IoT Device - Should FAIL due to ACL 110)
ping 192.168.30.100   (Public WiFi - Should work)
```

### 9.2 Public WiFi Restriction Test

From **Public-Laptop-01** > **Desktop** > **Command Prompt**:

```
ping 192.168.40.40    (Web Server - Should FAIL due to ACL 130)
ping 192.168.20.10    (Admin PC - Should FAIL due to ACL 130)
ping 192.168.30.1     (Own gateway - Should work)
```

### 9.3 Web Server Access Test

From **Admin-PC-01** > **Desktop** > **Web Browser**:
- URL: `http://192.168.40.40` or `http://web.smartcity.local`
- Should display Smart City Dashboard

### 9.4 Email Test

From **Admin-PC-02** > **Desktop** > **Email**:
- Email Address: `admin@smartcity.local`
- Incoming/Outgoing Mail Server: `192.168.40.30`
- User: `admin`, Password: `admin123`
- Send test email to `iot@smartcity.local`

### 9.5 DHCP Verification

From **DHCP-Server** > **Services** > **DHCP**:
- Check "IP Address Allocated" list
- Should show multiple devices with assigned IPs

### 9.6 Spanning Tree Verification

From **DIST-SW1** > **CLI**:
```
show spanning-tree
show spanning-tree vlan 10
```

### 9.7 Failover Test

1. Disconnect **CORE-R1 Gig0/0** from **DIST-SW1**
2. Wait 30 seconds
3. Test connectivity from Admin-PC-01 to servers
4. Traffic should reroute through DIST-SW2
5. Reconnect cable
6. Verify restoration

---

## STEP 10: DEMONSTRATION SCENARIOS

### Scenario 1: IoT Security Isolation
**Objective:** Prove IoT devices cannot access Admin network

1. From **TrafficSensor-01**: Ping `192.168.20.10` → **BLOCKED**
2. From **Admin-PC-01**: Ping IoT sensor → **BLOCKED**
3. Both can ping servers → **ALLOWED**

### Scenario 2: Public WiFi Restrictions
**Objective:** Prove public users cannot reach critical infrastructure

1. Connect **Public-Laptop-01** to `SmartCity-Public` WiFi
2. Attempt to access `192.168.40.30` (Email) → **BLOCKED**
3. Access `192.168.40.40` (Web Server) → **BLOCKED**
4. Ping gateway `192.168.30.1` → **ALLOWED**

### Scenario 3: Email Alerting System
**Objective:** Demonstrate automated monitoring alerts

1. Configure **Monitor-Server** with email client
2. Set up rule: If ping fails, send email to `admin@smartcity.local`
3. Disconnect IoT device
4. Admin receives alert email

### Scenario 4: Load Distribution
**Objective:** Show multiple devices across VLANs

1. Open **DHCP-Server** > Services > DHCP
2. Show IoT Pool: 7 devices allocated
3. Show WiFi Pool: 10 devices allocated
4. Show Admin Pool: 6 devices allocated
5. Show Mobile Pool: 5 devices allocated
6. **Total: 28 end devices managed**

### Scenario 5: Mobile Admin Access
**Objective:** Field engineers can securely access network

1. Connect **Admin-Tablet-01** to `SmartCity-Admin-Mobile`
2. Receive IP from VLAN 50 pool
3. Access servers and admin resources
4. Show separation from public WiFi

---

## NETWORK COMPLEXITY HIGHLIGHTS

### Quantitative Metrics
- **Total Devices:** 41 (infrastructure + servers + endpoints)
- **VLANs Configured:** 5 (IoT, Admin, Public, Servers, Mobile)
- **Trunk Links:** 7 redundant trunk connections
- **Wireless Networks:** 3 SSIDs (2 public, 1 admin)
- **DHCP Pools:** 4 separate pools managing 220 addresses
- **ACL Rules:** 2 ACLs with 5 rules total
- **Server Services:** DNS, DHCP, Email, Web, Monitoring

### Complexity Demonstrations

**1. Multi-VLAN Traffic Segregation:**
- 5 isolated broadcast domains
- Router-on-a-stick inter-VLAN routing
- ACL-enforced security between segments

**2. Redundant Infrastructure:**
- Dual distribution switches with cross-link
- Spanning Tree preventing loops
- Automatic failover capability

**3. Wireless Integration:**
- Dual public APs for coverage
- Separate admin mobile network
- 15 wireless clients across 2 SSIDs

**4. Service Integration:**
- Centralized DNS resolution
- DHCP relay across VLANs
- Email alerting system
- Web dashboard monitoring

**5. Security Layers:**
- VLAN segmentation
- Extended ACLs
- Port security on access switches
- WPA2 wireless authentication

---

## TROUBLESHOOTING GUIDE

### Issue 1: Device Not Getting IP
- Check DHCP pools active on `192.168.40.20`
- Verify `ip helper-address` on router subinterface
- Confirm device VLAN matches DHCP pool

### Issue 2: Cannot Ping Across VLANs
- Verify router subinterfaces are `no shutdown`
- Check trunk allowed VLANs on switches
- Confirm ACLs are not blocking traffic

### Issue 3: Wireless Clients Not Connecting
- Verify AP SSID and password match client
- Check AP connected to correct switch port
- Ensure VLAN 30 or 50 configured on path to router

### Issue 4: Spanning Tree Loop
- Check for duplicate VLAN on wrong port
- Verify trunk configuration matches both ends
- Use `show spanning-tree` to identify blocked ports

### Issue 5: ACL Too Restrictive
- Review ACL 110 and 130 rules on router
- Use `show access-lists` to verify configuration
- Ensure permit any any at end of each ACL

---

## SUMMARY

✅ **41 total devices** demonstrating enterprise network complexity
✅ **5 VLANs** with complete segmentation and security
✅ **3-tier architecture** (Core/Distribution/Access)
✅ **Dual distribution switches** with redundancy
✅ **7 IoT sensors** showing smart city monitoring
✅ **6 admin devices** for city operations
✅ **10 public WiFi users** demonstrating public access
✅ **5 mobile admin devices** for field operations
✅ **5 servers** providing critical services
✅ **ACL security policies** enforcing network isolation
✅ **Wireless integration** with multiple SSIDs
✅ **DHCP relay** across all VLANs
✅ **DNS resolution** for service discovery
✅ **Email alerting** for monitoring
✅ **Web dashboard** for status viewing
✅ **Spanning Tree** preventing loops
✅ **Failover capability** validated

**This medium-complexity setup clearly demonstrates all major networking concepts while remaining manageable for testing and presentation.**
