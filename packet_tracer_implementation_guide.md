# Packet Tracer Implementation Guide
## Smart City IoT Network with IPv6 and QoS

### Phase 1: Network Topology Setup

#### Step 1: Create the Physical Topology
1. **Add Routers** (Use 2811 or 2901 series):
   - City 1: Core-R1, Core-R2
   - City 2: Core-R3, Core-R4
   - Internet: ISP-R1, ISP-R2

2. **Add Switches** (Use 2960 series):
   - City 1: Dist-SW1, Dist-SW2, Dist-SW3, Access-SW1 to Access-SW5
   - City 2: Dist-SW4, Dist-SW5, Dist-SW6, Access-SW6 to Access-SW10

3. **Add IoT Devices**:
   - Use "Smart Things" from IoT devices
   - Traffic sensors, air quality monitors, smart waste bins
   - Weather stations, smart traffic lights
   - Wireless access points for public WiFi

4. **Add End Devices**:
   - PCs for administrative use
   - Servers for SMTP and HTTP services

#### Step 2: Physical Connections
```
Core Layer Connections:
- Core-R1 ↔ Core-R2 (Serial or GigabitEthernet)
- Core-R3 ↔ Core-R4 (Serial or GigabitEthernet)
- Core-R1/R2 ↔ ISP-R1 (Serial WAN links)
- Core-R3/R4 ↔ ISP-R2 (Serial WAN links)
- ISP-R1 ↔ ISP-R2 (Internet backbone)

Distribution Connections:
- Each Core Router connects to multiple Distribution Switches
- Use GigabitEthernet interfaces

Access Connections:
- Each Distribution Switch connects to multiple Access Switches
- Each Access Switch connects to end devices and IoT sensors
```

### Phase 2: IPv6 Configuration

#### Core Router Configuration (City 1 - Core-R1)
```cisco
enable
configure terminal
hostname Core-R1-Chattogram

! Enable IPv6 routing
ipv6 unicast-routing

! Configure interfaces
interface GigabitEthernet0/0
 description "Connection to Core-R2"
 ipv6 address 2001:db8:1::1/64
 ipv6 enable
 no shutdown

interface GigabitEthernet0/1
 description "Connection to Dist-SW1"
 ipv6 address 2001:db8:1:10::1/64
 ipv6 enable
 no shutdown

interface GigabitEthernet0/2
 description "Connection to Dist-SW2"
 ipv6 address 2001:db8:1:20::1/64
 ipv6 enable
 no shutdown

interface Serial0/0/0
 description "WAN to ISP"
 ipv6 address 2001:db8:ffff:1::1/64
 ipv6 enable
 clock rate 64000
 no shutdown

! Configure OSPFv3
ipv6 router ospf 1
 router-id 1.1.1.1
 area 0 range 2001:db8:1::/48

interface GigabitEthernet0/0
 ipv6 ospf 1 area 0

interface GigabitEthernet0/1
 ipv6 ospf 1 area 0

interface GigabitEthernet0/2
 ipv6 ospf 1 area 0

! Configure BGP for Internet connectivity
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 2001:db8:ffff:1::2 remote-as 65000
 address-family ipv6
  neighbor 2001:db8:ffff:1::2 activate
  network 2001:db8:1::/48

exit
exit
write memory
```

#### Distribution Switch Configuration (Dist-SW1)
```cisco
enable
configure terminal
hostname Dist-SW1-Chattogram

! Enable IPv6
ipv6 unicast-routing

! Create VLANs
vlan 10
 name Traffic-Management
vlan 20
 name Environmental-Monitoring
vlan 30
 name Waste-Management
vlan 40
 name Administrative
vlan 50
 name Public-WiFi

! Configure trunk ports to core
interface GigabitEthernet0/1
 description "Trunk to Core-R1"
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50

! Configure access ports
interface range FastEthernet0/1-5
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast

interface range FastEthernet0/6-10
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast

! Configure SVI for management
interface vlan 10
 ipv6 address 2001:db8:1:10::10/64
 ipv6 enable
 no shutdown

! Configure QoS
mls qos
class-map match-all CRITICAL
 match ip dscp ef
class-map match-all HIGH
 match ip dscp af31
class-map match-all MEDIUM
 match ip dscp af21
class-map match-all LOW
 match ip dscp af11

policy-map QOS-POLICY
 class CRITICAL
  priority percent 30
 class HIGH
  bandwidth percent 40
 class MEDIUM
  bandwidth percent 20
 class LOW
  bandwidth percent 10

interface range FastEthernet0/1-24
 service-policy output QOS-POLICY

exit
write memory
```

### Phase 3: IoT Device Configuration

#### Smart Traffic Sensor Configuration
```
Device: Smart Traffic Sensor
IPv6 Address: 2001:db8:1:10::100/64
Default Gateway: 2001:db8:1:10::1
VLAN: 10
QoS Marking: AF31 (High Priority)

Sensor Settings:
- Detection Range: 50 meters
- Update Interval: 30 seconds
- Data Type: Vehicle count, speed, congestion level
```

#### Air Quality Monitor Configuration
```
Device: Air Quality Monitor
IPv6 Address: 2001:db8:1:20::100/64
Default Gateway: 2001:db8:1:20::1
VLAN: 20
QoS Marking: AF21 (Medium Priority)

Sensor Settings:
- Measurement Interval: 60 seconds
- Parameters: PM2.5, PM10, CO2, NO2
- Alert Threshold: Configurable
```

### Phase 4: Security Configuration

#### Access Control Lists (ACLs)
```cisco
! Traffic Management VLAN ACL
ipv6 access-list TRAFFIC-VLAN-ACL
 permit ipv6 2001:db8:1:10::/64 any
 permit ipv6 any 2001:db8:1:40::/64
 deny ipv6 any any log

! Environmental Monitoring ACL
ipv6 access-list ENV-VLAN-ACL
 permit ipv6 2001:db8:1:20::/64 any
 permit ipv6 any 2001:db8:1:40::/64
 deny ipv6 2001:db8:1:20::/64 2001:db8:1:50::/64
 deny ipv6 any any log

! Apply ACLs to interfaces
interface vlan 10
 ipv6 traffic-filter TRAFFIC-VLAN-ACL in

interface vlan 20
 ipv6 traffic-filter ENV-VLAN-ACL in
```

#### Port Security Configuration
```cisco
! Configure port security on access ports
interface range FastEthernet0/1-24
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

### Phase 5: Services Configuration

#### SMTP Server Configuration (City 1)
```
Server: SMTP-Server-Chattogram
IPv6 Address: 2001:db8:1:40::10/64
Services: SMTP enabled
Port: 25
Authentication: Basic
Domain: chattogram.smartcity.local

Email Alert Configuration:
- Critical Network Events
- IoT Device Failures
- Security Violations
- QoS Threshold Breaches
```

#### HTTP Server Configuration (City 2)
```
Server: HTTP-Server-Dhaka
IPv6 Address: 2001:db8:2:90::10/64
Services: HTTP/HTTPS enabled
Port: 80/443
Document Root: /var/www/html

Dashboard Features:
- Real-time IoT data visualization
- Network topology status
- Traffic flow monitoring
- Environmental data trends
```

### Phase 6: Inter-City Connectivity

#### BGP Configuration for Internet Routing
```cisco
! ISP Router Configuration
router bgp 65000
 bgp router-id 200.200.200.200
 neighbor 2001:db8:ffff:1::1 remote-as 65001
 neighbor 2001:db8:ffff:2::1 remote-as 65002
 
 address-family ipv6
  neighbor 2001:db8:ffff:1::1 activate
  neighbor 2001:db8:ffff:2::1 activate
  network 2001:db8:ffff::/48
```

### Phase 7: Testing and Validation

#### Connectivity Tests
1. **IPv6 Ping Tests**:
   ```
   ping 2001:db8:2:60::100 (City 1 to City 2 IoT device)
   ping 2001:db8:1:40::10 (Inter-city server communication)
   ```

2. **Traceroute Analysis**:
   ```
   tracert 2001:db8:2:90::10 (Path analysis between cities)
   ```

3. **QoS Verification**:
   - Generate traffic with different priorities
   - Monitor bandwidth allocation
   - Verify emergency traffic precedence

#### Failover Testing
1. **Core Router Failure**:
   - Shutdown Core-R1
   - Verify traffic reroutes through Core-R2
   - Check convergence time

2. **Link Failure Simulation**:
   - Disconnect distribution links
   - Verify alternate path activation
   - Monitor OSPF reconvergence

### Phase 8: Monitoring and Alerts

#### SNMP Configuration
```cisco
! Enable SNMP for monitoring
snmp-server community public ro
snmp-server community private rw
snmp-server host 2001:db8:1:40::20 version 2c public
```

#### Syslog Configuration
```cisco
! Configure logging
logging 2001:db8:1:40::10
logging trap informational
logging facility local0
```

### Device Requirements Summary

**Routers Needed**: 6 total
- 4 Core routers (2 per city)
- 2 ISP routers

**Switches Needed**: 16 total
- 6 Distribution switches (3 per city)
- 10 Access switches (5 per city)

**IoT Devices**: 30+ total
- 15+ devices per city
- Various sensor types

**Servers**: 4 total
- SMTP servers (1 per city)
- HTTP servers (1 per city)

**End Devices**: 8+ total
- Administrative PCs
- Monitoring workstations

This implementation provides:
✅ Complete IPv6 addressing
✅ VLAN segmentation
✅ QoS implementation
✅ Security measures
✅ Inter-city connectivity
✅ Redundancy and failover
✅ Monitoring capabilities
✅ Real-world IoT scenarios
