# CORRECTED TOPOLOGY DIAGRAM
## City A Network - Cisco 2911 Compatible Design

---

## 🗺️ COMPLETE TOPOLOGY (ASCII)

```
                              ISP-Border-R1
                                    ↑
                              Serial0/0/0
                                    ↑
                              Serial0/0/0
                            CityA-Border-R1
                                 Gig0/0
                                    ↑
                                 Gig0/2
                            ┌─────────────┐
                            │ CityA-Core  │
                            │    R1       │
                            │  (2911)     │
                            └─────────────┘
                            Gig0/0 │ │ Gig0/1
                                   │ │
                        (TRUNK)    │ │    (TRUNK)
                     All VLANs     │ │     All VLANs
                                   │ │
        ┌──────────────────────────┘ └─────────────────────────┐
        │                                                        │
    Gig1/0/1                                                 Gig1/0/1
┌────────────────┐                                      ┌────────────────┐
│ CityA-Core-SW1 │ Gig1/0/4 ←─────────────────→ Gig1/0/2│ CityA-Core-SW2 │
│   (2960-24TT)  │         (TRUNK - Redundancy)         │   (2960-24TT)  │
└────────────────┘                                      └────────────────┘
    │    │    │                                             │    │    │
    │    │    └──────┐                                      │    │    └──────┐
    │    │           │                                      │    │           │
    │    │      Gig1/0/2,3                            Gig1/0/3  │       Fa1/0/5,6
    │    │      (Layer2)                                    │    │      (TRUNK)
    │    │           │                                      │    │           │
    │    │    ┌──────┴───────┐                              │    │    ┌──────┴───────┐
    │    │    │               │                              │    │    │              │
Fa1/0/1-4    Gov-R1      Res-R1                         Com-R1   │  Trans-SW1   Util-SW1
(Servers)   (2911)       (2911)                         (2911)   │  (VLAN 40)   (VLAN 70)
            Gig0/1       Gig0/1                         Gig0/1   │
VLAN 99       │            │                              │      │
              │            │                              │    Internet
           Gov-SW1      Res-SW1                        Com-SW1   Servers
          (VLAN 10,    (VLAN 20)                    (VLAN 30,    (DNS, Web)
           VLAN 60)                                  VLAN 50)
              │            │                              │
         ┌────┴────┐  ┌────┴────┐                   ┌────┴────┐
         │         │  │         │                   │         │
    Gov Devices  Emergency  Residential         Commercial  Public
    (PCs, WiFi)  (Police,   (PCs, IoT,         (PCs, POS)  WiFi
                 Fire)      SmartHome)                      Devices
```

---

## 📋 KEY CONNECTIONS

### Core Router (CityA-Core-R1) - Only 3 Interfaces Used:
```
Gig0/0 ──→ Core-SW1 Gig1/0/1 (Trunk: VLANs 10-99)
Gig0/1 ──→ Core-SW2 Gig1/0/1 (Trunk: VLANs 10-99)
Gig0/2 ──→ Border-R1 Gig0/0  (Point-to-point: 10.0.0.0/30)
```

### Core Switch 1 (CityA-Core-SW1):
```
Gig1/0/1 ──→ Core-R1 Gig0/0        (Trunk: All VLANs)
Gig1/0/2 ──→ Gov-R1 Gig0/0         (Access: VLAN 99)
Gig1/0/3 ──→ Res-R1 Gig0/0         (Access: VLAN 99)
Gig1/0/4 ──→ Core-SW2 Gig1/0/2     (Trunk: All VLANs - Redundancy)
Fa1/0/1  ──→ DNS-Server            (Access: VLAN 99)
Fa1/0/2  ──→ DHCP-Server           (Access: VLAN 99)
Fa1/0/3  ──→ Web-Server            (Access: VLAN 99)
Fa1/0/4  ──→ Email-Server          (Access: VLAN 99)
```

### Core Switch 2 (CityA-Core-SW2):
```
Gig1/0/1 ──→ Core-R1 Gig0/1        (Trunk: All VLANs)
Gig1/0/2 ──→ Core-SW1 Gig1/0/4     (Trunk: All VLANs - Redundancy)
Gig1/0/3 ──→ Com-R1 Gig0/0         (Access: VLAN 99)
Fa1/0/5  ──→ Trans-SW1 Fa0/24      (Trunk: VLAN 40)
Fa1/0/6  ──→ Util-SW1 Fa0/24       (Trunk: VLAN 70)
```

---

## 🔄 OSPF ROUTING PATHS

### OSPF Area 10 (City A):
```
All routers connect via Layer 2 (VLAN 99) through core switches:

Border-R1 (10.0.0.2) ←─────→ Core-R1 (10.0.0.1)
                                  ↓
                          [VLAN 99 Domain]
                        via Core-SW1 & Core-SW2
                                  ↓
                    ┌─────────────┼─────────────┐
                    ↓             ↓             ↓
                 Gov-R1        Res-R1        Com-R1

All routers form OSPF adjacencies and exchange routes.
```

### Advertised Networks:
```
Border-R1:  203.0.113.0/30 (WAN), default route 0.0.0.0/0
Core-R1:    192.168.40.0/24, 192.168.50.0/24, 192.168.70.0/24, 192.168.99.0/24
Gov-R1:     192.168.10.0/24, 192.168.60.0/24
Res-R1:     192.168.20.0/24
Com-R1:     192.168.30.0/24
```

---

## 🎯 VLAN DISTRIBUTION MAP

### Core Router Sub-Interfaces:
```
Gig0/0.40  →  VLAN 40 (Transportation)  →  192.168.40.1/24  →  Trans-SW1
Gig0/0.50  →  VLAN 50 (Public WiFi)     →  192.168.50.1/24  →  Com-SW1
Gig0/1.70  →  VLAN 70 (Utilities)       →  192.168.70.1/24  →  Util-SW1
Gig0/1.99  →  VLAN 99 (Management)      →  192.168.99.1/24  →  Servers
```

### Zone Router Sub-Interfaces:
```
Gov-R1:
    Gig0/1.10  →  VLAN 10 (Government)  →  192.168.10.1/24  →  Gov-SW1
    Gig0/1.60  →  VLAN 60 (Emergency)   →  192.168.60.1/24  →  Gov-SW1

Res-R1:
    Gig0/1.20  →  VLAN 20 (Residential) →  192.168.20.1/24  →  Res-SW1

Com-R1:
    Gig0/1.30  →  VLAN 30 (Commercial)  →  192.168.30.1/24  →  Com-SW1
```

---

## 📊 DATA FLOW EXAMPLES

### Example 1: Home PC (VLAN 20) → Web Server (VLAN 99)
```
Home-PC-1 (192.168.20.101)
    ↓
Res-SW1 (VLAN 20)
    ↓
Res-R1 Gig0/1.20 (gateway: 192.168.20.1)
    ↓ [ROUTING]
Res-R1 Gig0/0 (10.0.2.2)
    ↓ [Layer 2 via Core-SW1]
Core-R1 learns route via OSPF
    ↓
Core-R1 Gig0/0.99 (192.168.99.1)
    ↓
Core-SW1 (VLAN 99)
    ↓
Web-Server (192.168.99.30)
```

### Example 2: Police PC (VLAN 60) → Internet
```
Police-PC-1 (192.168.60.101)
    ↓
Gov-SW1 (VLAN 60)
    ↓
Gov-R1 Gig0/1.60 (gateway: 192.168.60.1)
    ↓ [ROUTING]
Gov-R1 Gig0/0 → Core-SW1 → Core-R1 (via OSPF)
    ↓
Core-R1 Gig0/2 → Border-R1
    ↓ [NAT: 192.168.60.101 → 203.0.113.X]
Border-R1 Serial0/0/0 → ISP-Border-R1
    ↓
Internet
```

### Example 3: IoT Sensor (VLAN 40) → DHCP Server (VLAN 99)
```
TrafficLight-1 (DHCP request on VLAN 40)
    ↓
Trans-SW1 (VLAN 40)
    ↓
Core-SW2 (VLAN 40)
    ↓
Core-R1 Gig0/0.40 (192.168.40.1)
    ↓ [DHCP relay via ip helper-address]
Core-R1 forwards to 192.168.99.20
    ↓
Core-R1 Gig0/0.99
    ↓
Core-SW1 (VLAN 99)
    ↓
DHCP-Server (192.168.99.20)
```

---

## 🔥 STP (Spanning Tree) Behavior

### Redundant Path:
```
Core-SW1 Gig1/0/4 ←────────────→ Gig1/0/2 Core-SW2
         ↑                                  ↑
         │                                  │
      Gig1/0/1                          Gig1/0/1
         │                                  │
         └───────→ Core-R1 Gig0/0,1 ←───────┘
```

**Spanning Tree will:**
1. Make Core-SW1 the root bridge (configured manually)
2. Block ONE of the redundant links to prevent loops
3. Likely blocks: Core-SW2 → Core-SW1 link (Gig1/0/2)
4. If primary path fails, blocked port activates (convergence)

---

## ✅ ADVANTAGES OF THIS DESIGN

1. **Works with 2911 hardware** - Only uses 3 available interfaces
2. **Hierarchical** - Follows Cisco three-tier model
3. **Scalable** - Easy to add zone routers to core switches
4. **Redundant** - Multiple paths between core switches
5. **Efficient** - OSPF provides dynamic routing
6. **Realistic** - Mimics real enterprise networks

---

## 🎓 VERIFICATION CHECKLIST

### Physical Connectivity:
- [ ] Core-R1 Gig0/0, 0/1, 0/2 all show green/up
- [ ] Core-SW1 Gig1/0/1-4 all show green/up
- [ ] Core-SW2 Gig1/0/1-3 all show green/up
- [ ] Zone routers Gig0/0 show green/up

### OSPF:
- [ ] `show ip ospf neighbor` shows all 5 routers on each router
- [ ] Router IDs: Border=1.1.1.1, Core=1.1.1.2, Gov=1.1.1.3, Res=1.1.1.4, Com=1.1.1.5

### Routing:
- [ ] All routers can ping all VLAN gateways (192.168.X.1)
- [ ] `show ip route` shows OSPF routes (O) to other VLANs
- [ ] End devices receive DHCP addresses

### VLANs:
- [ ] `show vlan brief` on switches shows correct VLAN assignments
- [ ] Trunk ports show "trunking" in `show interfaces trunk`
- [ ] Inter-VLAN communication works (ping across VLANs)

---

**This topology is ready for implementation in Packet Tracer!** 🚀
