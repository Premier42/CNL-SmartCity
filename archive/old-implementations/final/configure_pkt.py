#!/usr/bin/env python3
"""
Automated Packet Tracer Configuration Script
Modifies connection.xml to add complete network configuration
"""

import re
import sys

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Router Configuration
ROUTER_CONFIG = """enable
configure terminal
hostname City-Gateway-Router
enable secret class

! Enable IPv6 routing
ipv6 unicast-routing

! WAN Interface - Internet connection
interface GigabitEthernet0/0/0
 ip address dhcp
 ip nat outside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown

! LAN Interface - Core switch connection
interface GigabitEthernet0/0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown

! NAT Configuration
ip nat inside source list 1 interface Gig0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255

! Default Routes
ip route 0.0.0.0 0.0.0.0 Gig0/0/0

! Console and VTY access
line console 0
 password cisco
 login
line vty 0 4
 password cisco
 login

end
write memory"""

# Core Switch Configuration
CORE_SWITCH_CONFIG = """enable
configure terminal
hostname City-Core-Switch
enable secret class

! Enable IPv6 routing
ipv6 unicast-routing

! Create VLANs
vlan 10
 name Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management

! Router connection (Layer 3 routed port)
interface GigabitEthernet1/0/1
 no switchport
 ip address 10.0.0.2 255.255.255.252
 ipv6 enable
 no shutdown

! District switch trunk connections
interface GigabitEthernet1/0/2
 description Trunk to Downtown-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

interface GigabitEthernet1/0/3
 description Trunk to Park-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

interface GigabitEthernet1/0/4
 description Trunk to Residential-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown

! Cellular backhaul connection (Public VLAN)
interface GigabitEthernet1/0/5
 description Central Office Server - Cellular Backhaul
 switchport mode access
 switchport access vlan 20
 no shutdown

! Server connections (Admin VLAN)
interface range GigabitEthernet1/0/6-9
 description Servers (SMTP, Web, DHCP, DNS)
 switchport mode access
 switchport access vlan 10
 no shutdown

! Admin device connections (Admin VLAN)
interface range GigabitEthernet1/0/10-12
 description Admin Devices (PCs and Phone)
 switchport mode access
 switchport access vlan 10
 no shutdown

! VLAN Interfaces (SVIs) - Dual Stack IPv4/IPv6
interface Vlan10
 description Admin VLAN Gateway
 ip address 10.10.10.1 255.255.255.0
 ipv6 enable
 no shutdown

interface Vlan20
 description Public VLAN Gateway
 ip address 10.10.20.1 255.255.255.0
 ipv6 enable
 no shutdown

interface Vlan30
 description IoT VLAN Gateway
 ip address 10.10.30.1 255.255.255.0
 ipv6 enable
 no shutdown

interface Vlan99
 description Management VLAN Gateway
 ip address 10.10.99.1 255.255.255.0
 ipv6 enable
 no shutdown

! Default Routes
ip route 0.0.0.0 0.0.0.0 10.0.0.1

! Security ACLs - IPv4
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
 permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
 permit ip any any

interface Vlan20
 ip access-group BLOCK-PUBLIC-TO-ADMIN in

end
write memory"""

# Downtown Switch Configuration
DOWNTOWN_SWITCH_CONFIG = """enable
configure terminal
hostname Downtown-Switch

! Create VLANs
vlan 20
 name Public
vlan 99
 name Management

! Trunk to core switch
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99

! Access ports for public services
interface range FastEthernet0/2-4
 description Public VLAN Access Ports
 switchport mode access
 switchport access vlan 20

end
write memory"""

# Park Switch Configuration
PARK_SWITCH_CONFIG = """enable
configure terminal
hostname Park-Switch

! Create VLANs
vlan 30
 name IoT
vlan 99
 name Management

! Trunk to core switch
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99

! Access ports for IoT devices
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30

end
write memory"""

# Residential Switch Configuration
RESIDENTIAL_SWITCH_CONFIG = """enable
configure terminal
hostname Residential-Switch

! Create VLANs
vlan 30
 name IoT
vlan 99
 name Management

! Trunk to core switch
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99

! Access ports for residential devices
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30

end
write memory"""

def xml_escape(text):
    """Escape special XML characters"""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

def convert_config_to_xml_lines(config_text):
    """Convert multiline config to XML <LINE> tags"""
    lines = config_text.strip().split('\n')
    xml_lines = []
    for line in lines:
        if line.strip():  # Skip empty lines
            escaped_line = xml_escape(line)
            xml_lines.append(f'      <LINE>{escaped_line}</LINE>')
    return '\n'.join(xml_lines)

def replace_device_config(xml_content, device_name, new_config):
    """Replace the RUNNINGCONFIG section for a specific device"""
    # Find the device section
    device_pattern = rf'<NAME translate="true">{re.escape(device_name)}</NAME>'
    device_match = re.search(device_pattern, xml_content)

    if not device_match:
        print(f"Warning: Device '{device_name}' not found in XML")
        return xml_content

    # Find the RUNNINGCONFIG section after this device
    start_pos = device_match.end()
    runningconfig_start = xml_content.find('<RUNNINGCONFIG>', start_pos)

    if runningconfig_start == -1 or runningconfig_start > start_pos + 50000:  # Safety limit
        print(f"Warning: RUNNINGCONFIG not found for '{device_name}'")
        return xml_content

    runningconfig_end = xml_content.find('</RUNNINGCONFIG>', runningconfig_start)

    if runningconfig_end == -1:
        print(f"Warning: RUNNINGCONFIG end tag not found for '{device_name}'")
        return xml_content

    # Convert config to XML format
    xml_lines = convert_config_to_xml_lines(new_config)

    # Build new RUNNINGCONFIG section
    new_section = f"""<RUNNINGCONFIG>
     <PROTOCOL>
      <TYPE>eCiscoCLI</TYPE>
     </PROTOCOL>
{xml_lines}
     </RUNNINGCONFIG>"""

    # Replace the section
    new_xml = (xml_content[:runningconfig_start] +
               new_section +
               xml_content[runningconfig_end + len('</RUNNINGCONFIG>'):])

    print(f"✓ Updated configuration for {device_name}")
    return new_xml

def main():
    print("=" * 70)
    print("Smart City Network - Automated PT Configuration")
    print("=" * 70)
    print()

    # Read the XML file
    print("[1/6] Reading connection.xml...")
    xml_content = read_file('connection.xml')
    original_size = len(xml_content)
    print(f"      File size: {original_size:,} bytes")
    print()

    # Update router configuration
    print("[2/6] Configuring City-Gateway-Router...")
    xml_content = replace_device_config(xml_content, 'City-Gateway-Router', ROUTER_CONFIG)
    print()

    # Update core switch configuration
    print("[3/6] Configuring City-Core-Switch...")
    xml_content = replace_device_config(xml_content, 'City-Core-Switch', CORE_SWITCH_CONFIG)
    print()

    # Update district switches
    print("[4/6] Configuring Downtown-Switch...")
    xml_content = replace_device_config(xml_content, 'Downtown-Switch', DOWNTOWN_SWITCH_CONFIG)
    print()

    print("[5/6] Configuring Park-Switch...")
    xml_content = replace_device_config(xml_content, 'Park-Switch', PARK_SWITCH_CONFIG)
    print()

    print("      Configuring Residential-Switch...")
    xml_content = replace_device_config(xml_content, 'Residential-Switch', RESIDENTIAL_SWITCH_CONFIG)
    print()

    # Write modified XML
    print("[6/6] Writing modified XML to connection_configured.xml...")
    write_file('connection_configured.xml', xml_content)
    new_size = len(xml_content)
    print(f"      New file size: {new_size:,} bytes")
    print(f"      Change: +{new_size - original_size:,} bytes")
    print()

    print("=" * 70)
    print("✓ Configuration complete!")
    print("=" * 70)
    print()
    print("Next step: Convert XML back to PKT")
    print("Run: ./pka2xml/pka2xml -e connection_configured.xml connection_completed.pkt")
    print()

if __name__ == '__main__':
    main()
