# PART 2: CONFIGURATION
## 03 - SWITCH SETUP (VLANs, Trunks, STP)

**Configure all 16 switches with VLANs, trunking, and port security**

---

## ⚠️ IMPORTANT NOTES BEFORE STARTING

### **Switch Model Standard:**
- **ALL switches:** Cisco 2960-24TT (standardized for this project)
- Available in all Packet Tracer versions (8.0, 8.1, 8.2+)
- Full VLAN and trunking support
- **If unavailable:** Use 2950-24 (older but functional)

### **Trunk Configuration:**
- **DO NOT use:** `switchport trunk encapsulation dot1q`
- This command **fails on 2960 switches** (only supports dot1q anyway)
- Just use: `switchport mode trunk` directly
- **If you see errors about encapsulation:** Skip that command, it's not needed

### **Port Naming:**
- FastEthernet: `FastEthernet0/1`, `FastEthernet1/0/1` (varies by model)
- GigabitEthernet: `GigabitEthernet1/0/1`, `GigabitEthernet1/0/2`
- **Verify with:** `show ip interface brief`

### **Configuration Tips:**
- Copy-paste commands one at a time
- Wait for prompt before next command
- Save frequently: `write memory`
- If interface names differ, adjust accordingly

---

## 📋 SWITCH CONFIGURATION SUMMARY

| City | Switch | VLANs | Trunk Ports | Access Ports | Purpose |
|------|--------|-------|-------------|--------------|---------|
| A | Core-SW1 | All (10-99) | Gig1/0/1-2 | Fa1/0/1-4 | Core distribution + Servers |
| A | Core-SW2 | All (10-99) | Gig1/0/1-2 | Fa1/0/5-6 | Core distribution + Trans/Util |
| A | Gov-SW1 | 10, 60 | Fa0/24 | Fa0/1-8 | Government zone |
| A | Res-SW1 | 20 | Fa0/24 | Fa0/1-6 | Residential zone 1 |
| A | Res-SW2 | 20 | Fa0/24 | Fa0/1 | Residential zone 2 + Cell |
| A | Com-SW1 | 30, 50 | Fa0/24 | Fa0/1-4 | Commercial + Public WiFi |
| A | Trans-SW1 | 40 | Fa0/24 | Fa0/1-5 | Transportation IoT |
| A | Util-SW1 | 70 | Fa0/24 | Fa0/1-4 | Utilities IoT |

*City B: Identical configuration, replace "CityA" with "CityB"*

---

## 🔧 CITY A SWITCH CONFIGURATIONS

---

## **SWITCH 1: CityA-Core-SW1** (Distribution)

### **Step 1: Basic Configuration**

```cisco
enable
configure terminal
hostname CityA-Core-SW1

! Enable password
enable secret class

! Management VLAN IP
interface vlan 99
 ip address 192.168.99.11 255.255.255.0
 ipv6 address 2001:db8:a:99::11/64
 no shutdown
 exit

! Default gateway (points to core router)
ip default-gateway 192.168.99.1
```

---

### **Step 2: Create ALL VLANs**

```cisco
vlan 10
 name Government
 exit

vlan 20
 name Residential
 exit

vlan 30
 name Commercial
 exit

vlan 40
 name Transportation
 exit

vlan 50
 name Public-WiFi
 exit

vlan 60
 name Emergency
 exit

vlan 70
 name Utilities
 exit

vlan 99
 name Management
 exit
```

---

### **Step 3: Configure Trunk Ports**

#### **Trunk to Core Router (Gig1/0/1)**

```cisco
interface GigabitEthernet1/0/1
 description Trunk to CityA-Core-R1
 switchport mode trunk
 switchport trunk allowed vlan 40,50,70,99
 switchport trunk native vlan 99
 no shutdown
 exit
```

---

#### **Trunk to Core-SW2 (Redundancy)**

```cisco
interface GigabitEthernet1/0/2
 description Trunk to CityA-Core-SW2 (STP Backup)
 switchport mode trunk
 switchport trunk allowed vlan all
 switchport trunk native vlan 99
 no shutdown
 exit
```

---

### **Step 4: Configure Access Ports (Servers)**

```cisco
! DNS Server
interface FastEthernet1/0/1
 description CityA-DNS-Server
 switchport mode access
 switchport access vlan 99
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation restrict
 spanning-tree portfast
 no shutdown
 exit

! DHCP Server
interface FastEthernet1/0/2
 description CityA-DHCP-Server
 switchport mode access
 switchport access vlan 99
 switchport port-security
 switchport port-security maximum 1
 spanning-tree portfast
 no shutdown
 exit

! Web Server
interface FastEthernet1/0/3
 description CityA-Web-Server
 switchport mode access
 switchport access vlan 99
 switchport port-security
 switchport port-security maximum 1
 spanning-tree portfast
 no shutdown
 exit

! Email Server
interface FastEthernet1/0/4
 description CityA-Email-Server
 switchport mode access
 switchport access vlan 99
 switchport port-security
 switchport port-security maximum 1
 spanning-tree portfast
 no shutdown
 exit
```

---

### **Step 5: Configure Spanning Tree**

```cisco
! Enable Rapid PVST+
spanning-tree mode rapid-pvst

! Set as root bridge for all VLANs
spanning-tree vlan 1-99 priority 4096
```

---

### **Step 6: Save Configuration**

```cisco
end
write memory
```

**Verification:**
```cisco
show vlan brief
show interfaces trunk
show spanning-tree summary
show port-security interface FastEthernet1/0/1
```

---

## ✅ **CHECKPOINT:** Core-SW1 Complete

---

## **SWITCH 2: CityA-Core-SW2** (Distribution)

**Quick Configuration (Similar to Core-SW1):**

```cisco
enable
configure terminal
hostname CityA-Core-SW2

enable secret class

! Management IP
interface vlan 99
 ip address 192.168.99.12 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.99.1

! Create ALL VLANs (same as Core-SW1)
vlan 10
 name Government
 exit
vlan 20
 name Residential
 exit
vlan 30
 name Commercial
 exit
vlan 40
 name Transportation
 exit
vlan 50
 name Public-WiFi
 exit
vlan 60
 name Emergency
 exit
vlan 70
 name Utilities
 exit
vlan 99
 name Management
 exit

! Trunk to Core Router
interface GigabitEthernet1/0/1
 description Trunk to CityA-Core-R1
 switchport mode trunk
 switchport trunk allowed vlan 70,99
 switchport trunk native vlan 99
 no shutdown
 exit

! Trunk to Core-SW1 (Redundancy)
interface GigabitEthernet1/0/2
 description Trunk to CityA-Core-SW1
 switchport mode trunk
 switchport trunk allowed vlan all
 no shutdown
 exit

! Trunk to Trans-SW1
interface FastEthernet1/0/5
 description Trunk to CityA-Trans-SW1
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

! Trunk to Util-SW1
interface FastEthernet1/0/6
 description Trunk to CityA-Util-SW1
 switchport mode trunk
 switchport trunk allowed vlan 70
 no shutdown
 exit

! Spanning Tree (Secondary root)
spanning-tree mode rapid-pvst
spanning-tree vlan 1-99 priority 8192

end
write memory
```

---

## **SWITCH 3: CityA-Gov-SW1** (Government Zone)

```cisco
enable
configure terminal
hostname CityA-Gov-SW1

enable secret class

! Management IP
interface vlan 10
 ip address 192.168.10.10 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.10.1

! Create VLANs
vlan 10
 name Government
 exit
vlan 60
 name Emergency
 exit

! Trunk to Gov Router
interface FastEthernet0/24
 description Trunk to CityA-Gov-R1
 switchport mode trunk
 switchport trunk allowed vlan 10,60
 no shutdown
 exit

! Access Ports - Government (VLAN 10)
interface range FastEthernet0/1-2
 description Government PCs
 switchport mode access
 switchport access vlan 10
 switchport port-security
 spanning-tree portfast
 no shutdown
 exit

! Access Ports - Emergency (VLAN 60)
interface range FastEthernet0/3-4
 description Police/Fire PCs
 switchport mode access
 switchport access vlan 60
 switchport port-security
 spanning-tree portfast
 no shutdown
 exit

! WiFi AP (VLAN 10)
interface FastEthernet0/5
 description CityA-WiFi-Gov-AP1
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
 exit

! Security Cameras (VLAN 60)
interface range FastEthernet0/6-8
 description Cameras and Fire Sensor
 switchport mode access
 switchport access vlan 60
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## **SWITCH 4: CityA-Res-SW1** (Residential Zone 1)

```cisco
enable
configure terminal
hostname CityA-Res-SW1

enable secret class

interface vlan 20
 ip address 192.168.20.10 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.20.1

vlan 20
 name Residential
 exit

! Trunk
interface FastEthernet0/24
 description Trunk to CityA-Res-R1
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

! Access Ports (all VLAN 20)
interface range FastEthernet0/1-6
 description Residential Devices
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## **SWITCH 5: CityA-Res-SW2** (Residential Zone 2 + Cellular)

```cisco
enable
configure terminal
hostname CityA-Res-SW2

enable secret class

interface vlan 20
 ip address 192.168.20.11 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.20.2

vlan 20
 name Residential
 exit

interface FastEthernet0/24
 description Trunk to CityA-Res-R1
 switchport mode trunk
 switchport trunk allowed vlan 20
 no shutdown
 exit

! Cell Tower
interface FastEthernet0/1
 description CityA-CellTower-1
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## **SWITCH 6: CityA-Com-SW1** (Commercial Zone)

```cisco
enable
configure terminal
hostname CityA-Com-SW1

enable secret class

interface vlan 30
 ip address 192.168.30.10 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.30.1

vlan 30
 name Commercial
 exit

vlan 50
 name Public-WiFi
 exit

interface FastEthernet0/24
 description Trunk to CityA-Com-R1
 switchport mode trunk
 switchport trunk allowed vlan 30,50
 no shutdown
 exit

! Commercial devices (VLAN 30)
interface range FastEthernet0/1-3
 description Commercial PCs
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit

! Public WiFi AP (VLAN 50)
interface FastEthernet0/4
 description CityA-WiFi-Pub-AP1
 switchport mode access
 switchport access vlan 50
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## **SWITCH 7: CityA-Trans-SW1** (Transportation)

```cisco
enable
configure terminal
hostname CityA-Trans-SW1

enable secret class

interface vlan 40
 ip address 192.168.40.10 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.40.1

vlan 40
 name Transportation
 exit

interface FastEthernet0/24
 description Trunk to CityA-Core-SW2
 switchport mode trunk
 switchport trunk allowed vlan 40
 no shutdown
 exit

! IoT Devices (all VLAN 40)
interface range FastEthernet0/1-5
 description Transportation IoT
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## **SWITCH 8: CityA-Util-SW1** (Utilities)

```cisco
enable
configure terminal
hostname CityA-Util-SW1

enable secret class

interface vlan 70
 ip address 192.168.70.10 255.255.255.0
 no shutdown
 exit

ip default-gateway 192.168.70.1

vlan 70
 name Utilities
 exit

interface FastEthernet0/24
 description Trunk to CityA-Core-SW2
 switchport mode trunk
 switchport trunk allowed vlan 70
 no shutdown
 exit

! IoT Devices (all VLAN 70)
interface range FastEthernet0/1-4
 description Utilities IoT
 switchport mode access
 switchport access vlan 70
 spanning-tree portfast
 no shutdown
 exit

spanning-tree mode rapid-pvst

end
write memory
```

---

## 🏙️ CITY B SWITCHES

**EXACT COPY of City A** - Replace:
- Hostname: `CityA-XXX-SW` → `CityB-XXX-SW`
- Management IPs: Same (192.168.x.10/11)
- IPv6: `2001:db8:a` → `2001:db8:b`

---

## ✅ SWITCH CONFIGURATION CHECKLIST

**City A:**
- [ ] CityA-Core-SW1 (all VLANs, STP root)
- [ ] CityA-Core-SW2 (all VLANs, STP secondary)
- [ ] CityA-Gov-SW1 (VLANs 10, 60)
- [ ] CityA-Res-SW1 (VLAN 20)
- [ ] CityA-Res-SW2 (VLAN 20)
- [ ] CityA-Com-SW1 (VLANs 30, 50)
- [ ] CityA-Trans-SW1 (VLAN 40)
- [ ] CityA-Util-SW1 (VLAN 70)

**City B:**
- [ ] 8 switches (mirror City A)

**Total: 16 switches** ✅

---

## 🔍 VERIFICATION COMMANDS

```cisco
! Check VLANs
show vlan brief

! Check trunks
show interfaces trunk

! Check STP
show spanning-tree
show spanning-tree summary

! Check port security
show port-security
show port-security interface FastEthernet0/1

! Check interfaces
show ip interface brief
```

---

## 📊 EXPECTED RESULTS

### **Core-SW1:**
- VLANs: 1, 10, 20, 30, 40, 50, 60, 70, 99
- Trunks: Gig1/0/1, Gig1/0/2
- STP: Root for all VLANs
- Port security: Active on Fa1/0/1-4

### **Access Switches:**
- VLANs: Only relevant VLANs
- Trunk: Port 24
- All access ports: Portfast enabled

---

## ⏱️ ESTIMATED TIME

- Core switches: 30 minutes (2 switches)
- Access switches: 1 hour (6 switches)
- City B: 1 hour (copying pattern)
- **Total: ~2.5 hours**

---

## 📝 NEXT STEP

✅ **All switches configured**

➡️ **Next:** `04_SERVER_SETUP.md` for DHCP and DNS!

**Switch configuration complete!** 🚀
