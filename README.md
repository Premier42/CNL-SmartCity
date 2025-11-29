# Smart City IoT Network

> A fully functional Smart City network infrastructure demonstrating VLAN segmentation, inter-VLAN routing, network services, and IoT integration using Cisco Packet Tracer.

[![Platform](https://img.shields.io/badge/Platform-Cisco%20Packet%20Tracer-blue)](https://www.netacad.com/courses/packet-tracer)
[![Status](https://img.shields.io/badge/Status-Fully%20Operational-success)](connection.pkt)
[![Devices](https://img.shields.io/badge/Devices-13-informational)](#network-overview)
[![VLANs](https://img.shields.io/badge/VLANs-4-informational)](#vlan-design)

---

## 🚀 Quick Start

### For Technical Implementation
**Read:** [SIMPLE_WORKING_CONFIG.md](SIMPLE_WORKING_CONFIG.md)
- Complete step-by-step configuration guide
- Copy/paste commands for all devices
- Designed for easiest path to success

### For Troubleshooting
**Read:** [PACKET_FIX.md](PACKET_FIX.md)
- Fixes inter-VLAN routing issues
- Diagnostic commands
- Verification steps

### For Presenters
**Read:** [PRESENTER_GUIDE.md](PRESENTER_GUIDE.md)
- Quick overview for presentations
- Common Q&A (20+ questions answered)
- 5-minute demo walkthrough
- Perfect for non-technical presenters

### For Technical Details
**Read:** [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)
- Complete technical documentation
- Architecture design rationale
- Security implementation
- Testing methodology
- Future enhancements

---

## 📋 Project Overview

### What Is This?

A **production-ready Smart City network** demonstrating modern network infrastructure for municipal services. Built entirely in Cisco Packet Tracer, this project showcases:

- **Three isolated network zones** for security and organization
- **Automated network services** (DHCP, DNS, Web, Email)
- **IoT infrastructure** with dedicated secure segment
- **Layer 3 switching** for high-performance inter-VLAN routing
- **Security policies** using Access Control Lists

### Network Zones

| Zone | VLAN | Network | Purpose |
|------|------|---------|---------|
| **Servers/Admin** | 10 | 10.10.10.0/24 | Critical infrastructure and administration |
| **Public Access** | 20 | 10.10.20.0/24 | Citizen services and public Wi-Fi |
| **IoT Devices** | 30 | 10.10.30.0/24 | Smart sensors and monitoring systems |
| **Management** | 99 | 10.10.99.0/24 | Network device management |

---

## 🏗️ Network Architecture

```
City-Gateway-Router (ISR4321)
         |
         | Gi0/0/1
         |
City-Core-Switch (Layer 3)
  Catalyst 3650-24PS
    /      |      \
   /       |       \
  /        |        \
Downtown  Park  Residential
Switch    Switch   Switch
  |         |         |
Public   IoT      Admin
Devices  Sensors   PCs
```

**Design Approach:** Layer 3 switching with centralized routing at the core.

---

## 🛠️ Technologies Implemented

### Networking
- ✅ **VLANs** - Network segmentation (802.1Q)
- ✅ **Inter-VLAN Routing** - Layer 3 switching with SVIs
- ✅ **Trunk Ports** - Multi-VLAN transport
- ✅ **Access Ports** - End device connectivity
- ✅ **Spanning Tree Protocol** - Loop prevention

### Services
- ✅ **DHCP** - Automated IP assignment (3 pools, 200 device capacity)
- ✅ **DNS** - Name resolution (smartcity.local domain)
- ✅ **Web Server** - HTTP/HTTPS services
- ✅ **Email Server** - SMTP with 4 user accounts

### Security
- ✅ **ACLs** - Traffic filtering between zones
- ✅ **VLAN Isolation** - Segmented broadcast domains
- ✅ **DHCP Relay** - Centralized IP management

---

## 📊 Network Statistics

| Metric | Value |
|--------|-------|
| **Total Devices** | 13 |
| **Routers** | 1 (ISR4321) |
| **Switches** | 4 (1 Core L3, 3 Access L2) |
| **Servers** | 4 (DNS, DHCP, Web, SMTP) |
| **End Devices** | 4 PCs |
| **VLANs** | 4 |
| **IP Networks** | 4 x /24 subnets |
| **DHCP Capacity** | 200 concurrent devices |
| **Services Active** | 4 (DHCP, DNS, HTTP, SMTP) |

---

## 🎯 Key Features

### 1. Layer 3 Switching
Uses **Cisco Catalyst 3650** multilayer switch for inter-VLAN routing instead of traditional router-on-a-stick. Benefits:
- Higher throughput (backplane switching)
- Lower latency
- Simplified configuration
- Better scalability

### 2. Centralized Services
All network services (DHCP, DNS, Web, Email) run on dedicated servers in VLAN 10. DHCP relay (`ip helper-address`) allows devices in all VLANs to obtain IPs from centralized server.

### 3. Security by Design
- **IoT devices** cannot access Public network
- **Public users** limited to Web, DNS, and Email services only
- **Administrative** zone has unrestricted access
- Enforced via Access Control Lists on VLAN interfaces

### 4. Professional Documentation
Complete documentation suite:
- Technical implementation guide
- Presenter/Q&A guide
- Troubleshooting documentation
- Network topology diagrams

---

## 📁 Project Files

### Main Project
- **`connection.pkt`** - Main Packet Tracer file (fully configured network)

### Documentation
- **`SIMPLE_WORKING_CONFIG.md`** - Primary configuration guide ⭐
- **`PROJECT_DOCUMENTATION.md`** - Complete technical documentation
- **`PRESENTER_GUIDE.md`** - Presentation and Q&A guide
- **`PACKET_FIX.md`** - Troubleshooting inter-VLAN routing
- **`ACTUAL_NETWORK_TOPOLOGY.md`** - Network topology details

### Archive
- **`archive/`** - Old implementations and documentation

---

## ✅ Testing & Verification

All tests **PASSED** ✓

### Connectivity Tests
- ✅ VLAN gateway reachability (all VLANs can reach gateways)
- ✅ Inter-VLAN routing (devices in different VLANs communicate)
- ✅ DHCP assignment (all PCs receive IPs automatically)
- ✅ DNS resolution (names resolve to IP addresses)

### Service Tests
- ✅ Web server accessible (http://web.smartcity.local)
- ✅ Email send/receive (between user accounts)
- ✅ DNS queries (nslookup returns correct IPs)

### Security Tests
- ✅ IoT → Public blocked (ACL working)
- ✅ Public → IoT blocked (ACL working)
- ✅ Public users limited to approved services only

---

## 🔧 Requirements

### Software
- **Cisco Packet Tracer** 8.0 or newer
- Download: [Cisco Networking Academy](https://www.netacad.com/courses/packet-tracer)

### Knowledge Prerequisites
- Basic networking concepts (IP addressing, subnets)
- VLAN fundamentals
- Cisco IOS command-line basics
- Understanding of network services (DHCP, DNS)

---

## 🚦 Getting Started

### Option 1: Use Existing Configuration
1. Open `connection.pkt` in Cisco Packet Tracer
2. Review configurations (already complete)
3. Test connectivity (see Testing section)
4. Done! Network is fully operational

### Option 2: Build From Scratch
1. Follow [SIMPLE_WORKING_CONFIG.md](SIMPLE_WORKING_CONFIG.md)
2. Configure router and switches (20-30 minutes)
3. Configure servers via GUI (15-20 minutes)
4. Test all services (10-15 minutes)
5. Total time: ~60 minutes

### Option 3: Troubleshooting Existing Setup
1. If packets aren't routing between VLANs
2. Follow [PACKET_FIX.md](PACKET_FIX.md)
3. Likely issue: `ip routing` not enabled on core switch
4. Fix time: 2 minutes

---

## 🎓 Learning Outcomes

By studying/implementing this project, you will learn:

### Technical Skills
- VLAN configuration and trunk ports
- Layer 3 switching vs traditional routing
- DHCP relay agents (`ip helper-address`)
- DNS server configuration
- Access Control Lists (ACLs)
- Network troubleshooting methodology

### Design Principles
- Hierarchical network design (Core/Distribution/Access)
- Network segmentation for security
- Centralized service architecture
- Scalable infrastructure planning

### Professional Practice
- Technical documentation writing
- Network testing and verification
- Configuration backup and version control
- Presentation of technical projects

---

## 🔐 Security Implementation

### VLAN Segmentation
Isolates different network zones:
- Prevents unauthorized access between segments
- Limits blast radius of security incidents
- Enables granular traffic control

### Access Control Lists
**ACL 110 - IoT Security:**
- IoT devices CAN access Servers (VLAN 10)
- IoT devices CANNOT access Public network (VLAN 20)
- Prevents compromised IoT device from attacking public services

**ACL 120 - Public Access Restriction:**
- Public users CAN access: Web (80/443), DNS (53), Email (25)
- Public users CANNOT access: IoT network, unrestricted server access
- Limits public exposure to essential services only

### Management VLAN
- VLAN 99 dedicated for switch management
- Separates management traffic from user data
- Enables secure administrative access

---

## 📈 Future Enhancements

### Phase 2 - Advanced Features
- [ ] **IPv6 deployment** - Dual-stack with DHCPv6
- [ ] **Redundancy** - HSRP for gateway redundancy
- [ ] **QoS** - Traffic prioritization and bandwidth management
- [ ] **Monitoring** - SNMP, Syslog, NetFlow

### Phase 3 - IoT Expansion
- [ ] **Additional IoT services** - Smart lighting, environmental sensors
- [ ] **IoT platform** - MQTT broker, data analytics
- [ ] **Real-time monitoring** - Dashboard for city metrics

### Phase 4 - Enhanced Security
- [ ] **Port security** - MAC address limiting
- [ ] **DHCP snooping** - Prevent rogue DHCP servers
- [ ] **802.1X** - Port-based authentication
- [ ] **VPN** - Remote access for administrators

---

## 🤝 Contributing

This is an academic project, but suggestions are welcome:
- Report issues or bugs
- Suggest improvements
- Share your implementations

---

## 📞 Support

### Documentation
- Technical details → [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)
- Configuration help → [SIMPLE_WORKING_CONFIG.md](SIMPLE_WORKING_CONFIG.md)
- Troubleshooting → [PACKET_FIX.md](PACKET_FIX.md)
- Presentation → [PRESENTER_GUIDE.md](PRESENTER_GUIDE.md)

### Common Issues
See troubleshooting section in [PACKET_FIX.md](PACKET_FIX.md)

---

## 📜 License

This project is created for educational purposes.

---

## 🏆 Project Status

**Status:** ✅ Complete and Fully Operational

- All devices configured
- All services tested and working
- Documentation complete
- Security policies implemented
- Ready for presentation or deployment

---

## 🙏 Acknowledgments

- **Cisco Networking Academy** - For Packet Tracer software
- **Cisco IOS** - Industry-standard network operating system
- **Smart City initiatives worldwide** - For inspiration

---

**Built with:** Cisco Packet Tracer
**Platform:** Cisco IOS
**Project Type:** Network Infrastructure Design
**Status:** Production Ready ✅

---

*This Smart City IoT Network demonstrates production-ready infrastructure using industry-standard technologies and best practices. Perfect for learning, presentations, or as a foundation for expansion.*
