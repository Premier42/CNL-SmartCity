# CORRECTED Smart City Network Configuration Guide
## Interface Naming Fixed for 2911 Router

---

## CRITICAL: Interface Naming Convention

Your router appears to be a **Cisco 2911** (or similar model), which uses:
- ✅ `GigabitEthernet0/0` (NOT GigabitEthernet0/0/0)
- ✅ `GigabitEthernet0/1` (NOT GigabitEthernet0/0/1)
- ✅ Subinterfaces: `GigabitEthernet0/0.10`, `GigabitEthernet0/0.20`, etc.

---

## Step-by-Step Configuration (Start Fresh)

### STEP 1: Go to Core-Router

Click on **Core-Router** → Click **CLI** tab

### STEP 2: Clear Any Existing Configuration (Optional but Recommended)

```cisco
enable
write erase
reload
```

When asked "Proceed with reload? [confirm]", press **Enter**

Wait for router to reload, then continue...

---

## STEP 3: Core Router Base Configuration

```cisco
enable
configure terminal
hostname Core-Router

! Enable routing
ip routing
ipv6 unicast-routing
```

---

## STEP 4: Configure Physical Interfaces

### Interface to Distribution Switch A

```cisco
interface GigabitEthernet0/0
 description "Link to Dist-SW-A"
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1000:1::1/64
 no shutdown
 exit
```

### Interface to Distribution Switch B

```cisco
interface GigabitEthernet0/1
 description "Link to Dist-SW-B"
 ip address 192.168.2.1 255.255.255.0
 ipv6 address 2001:db8:1000:2::1/64
 no shutdown
 exit
```

---

## STEP 5: Configure VLAN Subinterfaces on Gig0/0 (Distribution A Side)

### VLAN 10 - IoT Sensors

```cisco
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ipv6 address 2001:db8:1000:10::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

### VLAN 20 - Administrative

```cisco
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ipv6 address 2001:db8:1000:20::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

### VLAN 40 - Servers

```cisco
interface GigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ipv6 address 2001:db8:1000:40::1/64
 no shutdown
 exit
```

---

## STEP 6: Configure VLAN Subinterfaces on Gig0/1 (Distribution B Side)

### VLAN 30 - Public WiFi

```cisco
interface GigabitEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ipv6 address 2001:db8:1000:30::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

### VLAN 50 - Mobile Admin

```cisco
interface GigabitEthernet0/1.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ipv6 address 2001:db8:1000:50::1/64
 ip helper-address 192.168.40.20
 no shutdown
 exit
```

---

## STEP 7: Configure Access Control Lists (ACLs)

### IoT Security ACL

```cisco
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 110 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 110 deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 log
access-list 110 permit ip any any
```

### Public WiFi Restrictions ACL

```cisco
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 80
access-list 130 permit tcp 192.168.30.0 0.0.0.255 any eq 443
access-list 130 permit udp 192.168.30.0 0.0.0.255 192.168.40.10 0.0.0.0 eq 53
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 log
access-list 130 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255 log
access-list 130 permit ip any any
```

### Apply ACLs to Interfaces

```cisco
interface GigabitEthernet0/0.10
 ip access-group 110 in
 exit

interface GigabitEthernet0/1.30
 ip access-group 130 in
 exit
```

---

## STEP 8: Save Configuration

```cisco
end
write memory
```

You should see: `Building configuration... [OK]`

---

## STEP 9: Verify Router Configuration

```cisco
show ip interface brief
```

**Expected Output:**
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/0.10  192.168.10.1    YES manual up                    up
GigabitEthernet0/0.20  192.168.20.1    YES manual up                    up
GigabitEthernet0/0.40  192.168.40.1    YES manual up                    up
GigabitEthernet0/1     192.168.2.1     YES manual up                    up
GigabitEthernet0/1.30  192.168.30.1    YES manual up                    up
GigabitEthernet0/1.50  192.168.50.1    YES manual up                    up
```

```cisco
show vlan-switch
```

or

```cisco
show access-lists
```

---

## STEP 10: Configure Distribution Switch A (Dist-SW-A)

Click on **Dist-SW-A** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Dist-SW-A

! Create VLANs
vlan 10
 name IoT-Sensors
 exit
vlan 20
 name Administrative
 exit
vlan 40
 name Servers
 exit

! Trunk to Core Router (connects to Core-Router Gig0/0)
interface GigabitEthernet1/0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,40
 no shutdown
 exit

! Trunk to Access-SW1 (Servers)
interface FastEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

! Trunk to Access-SW2 (IoT)
interface FastEthernet1/0/2
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit

! Trunk to Access-SW3 (Admin)
interface FastEthernet1/0/3
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

end
write memory
```

---

## STEP 11: Configure Distribution Switch B (Dist-SW-B)

Click on **Dist-SW-B** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Dist-SW-B

! Create VLANs
vlan 30
 name Public-WiFi
 exit
vlan 50
 name Mobile-Admin
 exit

! Trunk to Core Router (connects to Core-Router Gig0/1)
interface GigabitEthernet1/0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

! Trunk to Access-SW4 (WiFi Zone 1)
interface FastEthernet1/0/1
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit

! Trunk to Access-SW5 (WiFi Zone 2 + Mobile Admin)
interface FastEthernet1/0/2
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

end
write memory
```

---

## STEP 12: Configure Access-SW1 (Servers VLAN 40)

Click on **Access-SW1** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW1

! Create VLAN
vlan 40
 name Servers
 exit

! Trunk uplink to Dist-SW-A
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

! Access ports for servers (ports 1-3)
interface range FastEthernet0/1-3
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## STEP 13: Configure Access-SW2 (IoT VLAN 10)

Click on **Access-SW2** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW2

! Create VLAN
vlan 10
 name IoT-Sensors
 exit

! Trunk uplink to Dist-SW-A
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10
 no shutdown
 exit

! Access ports for IoT devices (ports 1-8)
interface range FastEthernet0/1-8
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## STEP 14: Configure Access-SW3 (Admin VLAN 20)

Click on **Access-SW3** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW3

! Create VLAN
vlan 20
 name Administrative
 exit

! Trunk uplink to Dist-SW-A
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

! Access ports for Admin devices (ports 1-4)
interface range FastEthernet0/1-4
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## STEP 15: Configure Access-SW4 (WiFi Zone 1 VLAN 30)

Click on **Access-SW4** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW4

! Create VLAN
vlan 30
 name Public-WiFi
 exit

! Trunk uplink to Dist-SW-B
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 30
 no shutdown
 exit

! Access port for WiFi AP (port 1)
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## STEP 16: Configure Access-SW5 (WiFi + Mobile Admin VLANs 30,50)

Click on **Access-SW5** → Click **CLI** tab

```cisco
enable
configure terminal
hostname Access-SW5

! Create VLANs
vlan 30
 name Public-WiFi
 exit
vlan 50
 name Mobile-Admin
 exit

! Trunk uplink to Dist-SW-B
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

! Access port for WiFi AP (port 1 - VLAN 30)
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

! Access ports for Mobile Admin tablets (ports 2-4 - VLAN 50)
interface range FastEthernet0/2-4
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown
 exit

end
write memory
```

---

## STEP 17: Configure DNS Server (192.168.40.10)

1. Click on **DNS-Server**
2. Click **Desktop** tab → **IP Configuration**

**Settings:**
- IPv4 Address: `192.168.40.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

3. Click **Services** tab → **DNS**
4. Turn DNS Service **ON**
5. Add these DNS records (click "Add" for each):

| Name | Address |
|------|---------|
| core-router.smart-city.local | 192.168.1.1 |
| dhcp.smart-city.local | 192.168.40.20 |
| email.smart-city.local | 192.168.40.30 |
| dns.smart-city.local | 192.168.40.10 |

---

## STEP 18: Configure DHCP Server (192.168.40.20)

1. Click on **DHCP-Server**
2. Click **Desktop** tab → **IP Configuration**

**Settings:**
- IPv4 Address: `192.168.40.20`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

3. Click **Services** tab → **DHCP**
4. Create the following pools:

### Pool 1: IoT_SENSORS
- Pool Name: `IoT_SENSORS`
- Default Gateway: `192.168.10.1`
- DNS Server: `192.168.40.10`
- Start IP Address: `192.168.10.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `50`
- Click **Add**

### Pool 2: ADMIN_DEVICES
- Pool Name: `ADMIN_DEVICES`
- Default Gateway: `192.168.20.1`
- DNS Server: `192.168.40.10`
- Start IP Address: `192.168.20.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `20`
- Click **Add**

### Pool 3: PUBLIC_WIFI
- Pool Name: `PUBLIC_WIFI`
- Default Gateway: `192.168.30.1`
- DNS Server: `192.168.40.10`
- Start IP Address: `192.168.30.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `100`
- Click **Add**

### Pool 4: MOBILE_ADMIN
- Pool Name: `MOBILE_ADMIN`
- Default Gateway: `192.168.50.1`
- DNS Server: `192.168.40.10`
- Start IP Address: `192.168.50.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `20`
- Click **Add**

---

## STEP 19: Configure Email Server (192.168.40.30)

1. Click on **Email-Server**
2. Click **Desktop** tab → **IP Configuration**

**Settings:**
- IPv4 Address: `192.168.40.30`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.40.1`
- DNS Server: `192.168.40.10`

3. Click **Services** tab → **EMAIL**
4. Set Domain Name: `smart-city.local`
5. Add users:
   - User: `admin` Password: `admin123`
   - User: `operations` Password: `ops123`

---

## STEP 20: Configure WiFi Access Points

### WiFi-Zone1 Configuration

1. Click on **WiFi-Zone1** access point
2. Click **Config** tab → **Port 1**

**Settings:**
- SSID: `SmartCity_Zone1`
- Authentication: `WPA2-PSK`
- PSK Pass Phrase: `SmartCity2024`
- Channel: `6`

3. Click **Port 1** (Network settings):
- Static IP: `192.168.30.50`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.30.1`

### WiFi-Zone2 Configuration

1. Click on **WiFi-Zone2** access point
2. Click **Config** tab → **Port 1**

**Settings:**
- SSID: `SmartCity_Zone2`
- Authentication: `WPA2-PSK`
- PSK Pass Phrase: `SmartCity2024`
- Channel: `11`

3. Click **Port 1** (Network settings):
- Static IP: `192.168.30.51`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `192.168.30.1`

---

## STEP 21: Configure End Devices

### Admin PCs and Laptops (VLAN 20)
- Click each device → **Desktop** → **IP Configuration**
- Set to **DHCP**
- Expected IPs: `192.168.20.100` - `192.168.20.103`

### IoT Devices (VLAN 10)
- Click each IoT device → **Config** tab
- Set to **DHCP**
- Expected IPs: `192.168.10.100` - `192.168.10.107`

### Mobile Admin Tablets (VLAN 50)
- Click each tablet → **Desktop** → **IP Configuration**
- Set to **DHCP**
- Expected IPs: `192.168.50.100` - `192.168.50.102`

### WiFi Devices (Smartphones/Tablets on WiFi)
1. Click device → **Desktop** → **PC Wireless**
2. Click **Connect** tab
3. Select appropriate SSID (`SmartCity_Zone1` or `SmartCity_Zone2`)
4. Enter password: `SmartCity2024`
5. Click **Connect**

---

## STEP 22: Testing and Verification

### Test 1: Check Router Interfaces
```cisco
! On Core-Router
show ip interface brief
show ipv6 interface brief
```

### Test 2: Verify VLAN Configuration
```cisco
! On each switch
show vlan brief
show interfaces trunk
```

### Test 3: Test DHCP
From any PC in Admin VLAN:
1. Click **Desktop** → **Command Prompt**
2. Type: `ipconfig`
3. Verify you received an IP in the correct range

### Test 4: Test Connectivity
```
! From Admin PC (192.168.20.x)
ping 192.168.40.10   (DNS Server - should work)
ping 192.168.10.100  (IoT device - should work)
ping 192.168.30.100  (WiFi device - should work)

! From IoT device (192.168.10.x)
ping 192.168.40.10   (DNS Server - should work)
ping 192.168.20.100  (Admin PC - should work)
ping 192.168.30.100  (WiFi - should FAIL due to ACL)

! From WiFi device (192.168.30.x)
ping 192.168.40.10   (DNS - should work)
ping 192.168.10.100  (IoT - should FAIL due to ACL)
ping 192.168.20.100  (Admin - should FAIL due to ACL)
```

### Test 5: Test DNS Resolution
```
nslookup dhcp.smart-city.local
nslookup email.smart-city.local
```

---

## Quick Reference: Interface Naming by Router Model

| Router Model | Interface Format | Example |
|--------------|------------------|---------|
| ISR4331, ISR4321 | GigabitEthernet0/0/0 | Gig0/0/0.10 |
| 2911, 2901 | GigabitEthernet0/0 | Gig0/0.10 |
| 1941 | GigabitEthernet0/0 | Gig0/0.10 |
| 2621XM | FastEthernet0/0 | Fa0/0.10 |

---

## Common Errors and Fixes

### Error: "Invalid interface"
**Solution:** You're using the wrong interface naming. Use `show ip interface brief` to see available interfaces.

### Error: "% Incomplete command"
**Solution:** You forgot the encapsulation command before assigning IP to subinterface.

### Error: ACL not working
**Solution:** Make sure you applied ACL with `ip access-group 110 in` on the correct interface.

### Error: DHCP not working
**Solution:** Check `ip helper-address` is configured on router subinterfaces.

---

## Summary of Corrected Changes

✅ Changed `GigabitEthernet0/0/0` → `GigabitEthernet0/0`
✅ Changed `GigabitEthernet0/0/1` → `GigabitEthernet0/1`
✅ Changed all subinterfaces to match: `Gig0/0.10`, `Gig0/0.20`, etc.
✅ Added explicit step-by-step instructions
✅ Added verification commands
✅ Added troubleshooting section

**This configuration should now work perfectly with your router!**
