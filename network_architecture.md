# Smart City IoT Network Architecture
## IPv6-Based Two-City Network Design

```
                    ┌─────────────────────────────────────────────────────────────────┐
                    │                        INTERNET                                 │
                    │                   ISP Routers (BGP)                            │
                    │                2001:db8:ffff::/48                              │
                    └─────────────────┬───────────────────┬───────────────────────────┘
                                      │                   │
                    ┌─────────────────▼─────────────────┐ │ ┌─────────────────▼─────────────────┐
                    │     SMART CITY 1 (Chattogram)    │ │ │      SMART CITY 2 (Dhaka)        │
                    │      2001:db8:1::/48              │ │ │       2001:db8:2::/48             │
                    └───────────────────────────────────┘ │ └───────────────────────────────────┘
                                                          │
    ╔═══════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                CORE LAYER                                                 ║
    ╠═══════════════════════════════════════════════════════════════════════════════════════════╣
    ║  City 1:                                      │  City 2:                                  ║
    ║  ┌─────────────┐    ┌─────────────┐          │  ┌─────────────┐    ┌─────────────┐       ║
    ║  │Core Router 1│────│Core Router 2│          │  │Core Router 3│────│Core Router 4│       ║
    ║  │2001:db8:1::1│    │2001:db8:1::2│          │  │2001:db8:2::1│    │2001:db8:2::2│       ║
    ║  │   /64       │    │   /64       │          │  │   /64       │    │   /64       │       ║
    ║  └─────────────┘    └─────────────┘          │  └─────────────┘    └─────────────┘       ║
    ║         │                    │               │         │                    │             ║
    ╚═════════╪════════════════════╪═══════════════════════════╪════════════════════╪═════════════╝
              │                    │                           │                    │
    ╔═════════╪════════════════════╪═══════════════════════════╪════════════════════╪═════════════╗
    ║         │    DISTRIBUTION LAYER                          │                    │             ║
    ╠═════════╪════════════════════╪═══════════════════════════╪════════════════════╪═════════════╣
    ║  ┌──────▼──┐ ┌──────────┐ ┌──▼─────┐          ┌──────▼──┐ ┌──────────┐ ┌──▼─────┐        ║
    ║  │Dist SW 1│ │Dist SW 2 │ │Dist SW3│          │Dist SW 4│ │Dist SW 5 │ │Dist SW6│        ║
    ║  │VLAN 10-20│ │VLAN 30-40│ │VLAN 50 │          │VLAN 60-70│ │VLAN 80-90│ │VLAN100 │        ║
    ║  │2001:db8:│ │2001:db8: │ │2001:db8│          │2001:db8:│ │2001:db8: │ │2001:db8│        ║
    ║  │10::1/64 │ │11::1/64  │ │12::1/64│          │20::1/64 │ │21::1/64  │ │22::1/64│        ║
    ║  └─────────┘ └──────────┘ └────────┘          └─────────┘ └──────────┘ └────────┘        ║
    ║      │           │           │                     │           │           │              ║
    ╚══════╪═══════════╪═══════════╪═════════════════════╪═══════════╪═══════════╪══════════════╝
           │           │           │                     │           │           │
    ╔══════╪═══════════╪═══════════╪═════════════════════╪═══════════╪═══════════╪══════════════╗
    ║      │     ACCESS LAYER      │                     │           │           │              ║
    ╠══════╪═══════════╪═══════════╪═════════════════════╪═══════════╪═══════════╪══════════════╣
    ║ ┌────▼──┐ ┌──▼───┐ ┌──▼───┐ ┌▼────┐        ┌────▼──┐ ┌──▼───┐ ┌──▼───┐ ┌▼────┐         ║
    ║ │Access │ │Access│ │Access│ │Acc. │        │Access │ │Access│ │Access│ │Acc. │         ║
    ║ │SW 1   │ │SW 2  │ │SW 3  │ │SW 4 │        │SW 5   │ │SW 6  │ │SW 7  │ │SW 8 │         ║
    ║ │VLAN 10│ │VLAN20│ │VLAN30│ │VLAN │        │VLAN 60│ │VLAN70│ │VLAN80│ │VLAN │         ║
    ║ └───────┘ └──────┘ └──────┘ └─────┘        └───────┘ └──────┘ └──────┘ └─────┘         ║
    ║     │        │        │       │                │        │        │       │             ║
    ╚═════╪════════╪════════╪═══════╪════════════════╪════════╪════════╪═══════╪═════════════╝
          │        │        │       │                │        │        │       │
    ╔═════╪════════╪════════╪═══════╪════════════════╪════════╪════════╪═══════╪═════════════╗
    ║     │   IoT DEVICES & ENDPOINTS                 │        │        │       │             ║
    ╠═════╪════════╪════════╪═══════╪════════════════╪════════╪════════╪═══════╪═════════════╣
    ║     │        │        │       │                │        │        │       │             ║
    ║ ┌───▼──┐ ┌───▼──┐ ┌───▼──┐ ┌──▼──┐         ┌───▼──┐ ┌───▼──┐ ┌───▼──┐ ┌──▼──┐          ║
    ║ │Traffic│ │Air   │ │Waste │ │Admin│         │Traffic│ │Air   │ │Waste │ │Admin│          ║
    ║ │Sensors│ │Qual. │ │Mgmt  │ │PCs  │         │Sensors│ │Qual. │ │Mgmt  │ │PCs  │          ║
    ║ │      │ │Monit.│ │Smart │ │SMTP │         │      │ │Monit.│ │Smart │ │HTTP │          ║
    ║ │VLAN10│ │VLAN20│ │VLAN30│ │VLAN │         │VLAN60│ │VLAN70│ │VLAN80│ │VLAN │          ║
    ║ └──────┘ └──────┘ └──────┘ └─────┘         └──────┘ └──────┘ └──────┘ └─────┘          ║
    ║                                                                                         ║
    ║ Additional IoT Devices per City:                                                        ║
    ║ • Weather Stations     • Smart Traffic Lights    • Public WiFi APs                     ║
    ║ • Noise Sensors       • Water Quality Sensors    • Security Cameras                    ║
    ║ • Smart Parking       • Emergency Call Boxes     • Environmental Monitors              ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════╝
```

## Network Specifications

### IPv6 Addressing Scheme
```
Global Prefix: 2001:db8::/32 (Documentation prefix for testing)

City 1 (Chattogram): 2001:db8:1::/48
├── Core Network:        2001:db8:1:0::/64
├── Distribution 1:      2001:db8:1:10::/64  (VLAN 10 - Traffic)
├── Distribution 2:      2001:db8:1:20::/64  (VLAN 20 - Environment)
├── Distribution 3:      2001:db8:1:30::/64  (VLAN 30 - Waste Mgmt)
├── Distribution 4:      2001:db8:1:40::/64  (VLAN 40 - Admin)
└── Distribution 5:      2001:db8:1:50::/64  (VLAN 50 - Public WiFi)

City 2 (Dhaka): 2001:db8:2::/48
├── Core Network:        2001:db8:2:0::/64
├── Distribution 1:      2001:db8:2:60::/64  (VLAN 60 - Traffic)
├── Distribution 2:      2001:db8:2:70::/64  (VLAN 70 - Environment)
├── Distribution 3:      2001:db8:2:80::/64  (VLAN 80 - Waste Mgmt)
├── Distribution 4:      2001:db8:2:90::/64  (VLAN 90 - Admin)
└── Distribution 5:      2001:db8:2:100::/64 (VLAN 100 - Public WiFi)

Internet/WAN:    2001:db8:ffff::/48
```

### VLAN Segmentation Strategy
| VLAN ID | Purpose | City 1 Subnet | City 2 Subnet | QoS Priority |
|---------|---------|---------------|---------------|--------------|
| 10/60   | Traffic Management | 2001:db8:1:10::/64 | 2001:db8:2:60::/64 | High |
| 20/70   | Environmental Monitoring | 2001:db8:1:20::/64 | 2001:db8:2:70::/64 | Medium |
| 30/80   | Waste Management | 2001:db8:1:30::/64 | 2001:db8:2:80::/64 | Medium |
| 40/90   | Administrative | 2001:db8:1:40::/64 | 2001:db8:2:90::/64 | Critical |
| 50/100  | Public WiFi | 2001:db8:1:50::/64 | 2001:db8:2:100::/64 | Low |

### QoS Classification (4-Tier System)
1. **Critical (Emergency)** - Administrative traffic, SMTP alerts
2. **High** - Traffic management, emergency services
3. **Medium** - Environmental monitoring, waste management
4. **Low** - Public WiFi, general IoT data

### Device Count per City
- **Core Routers**: 2 (redundancy)
- **Distribution Switches**: 3
- **Access Switches**: 5
- **IoT Devices**: 15+
  - Traffic Sensors: 3
  - Air Quality Monitors: 2
  - Smart Waste Bins: 3
  - Weather Stations: 1
  - Smart Traffic Lights: 2
  - Public WiFi APs: 3
  - Administrative PCs: 2
  - Servers (SMTP/HTTP): 2

### Inter-City Data Flow Examples
1. **Traffic Data Sharing**: Chattogram traffic sensors → Internet → Dhaka traffic management
2. **Environmental Coordination**: Air quality data exchange between cities
3. **Administrative Reporting**: Centralized monitoring from both cities
4. **Emergency Alerts**: SMTP notifications across city boundaries

### Redundancy & Failover
- **Dual Core Routers** in each city
- **Multiple paths** between layers
- **Link redundancy** to Internet
- **Automatic failover** using OSPFv3
- **Load balancing** across distribution switches

This architecture demonstrates:
✅ Scalable IPv6 implementation
✅ Proper network segmentation
✅ QoS prioritization
✅ Inter-city connectivity
✅ Redundancy and resilience
✅ Real-world smart city scenarios
