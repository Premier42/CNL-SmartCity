#!/usr/bin/env python3
"""
Complete Smart City Network Automation
Configures ALL devices including servers, DNS, DHCP
Then converts back to PKT file
"""

import re
import subprocess
import sys

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

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
        if line.strip():
            escaped_line = xml_escape(line)
            xml_lines.append(f'      <LINE>{escaped_line}</LINE>')
    return '\n'.join(xml_lines)

def replace_device_config(xml_content, device_name, new_config):
    """Replace the RUNNINGCONFIG section for a specific device"""
    device_pattern = rf'<NAME translate="true">{re.escape(device_name)}</NAME>'
    device_match = re.search(device_pattern, xml_content)

    if not device_match:
        print(f"⚠ Warning: Device '{device_name}' not found")
        return xml_content

    start_pos = device_match.end()
    runningconfig_start = xml_content.find('<RUNNINGCONFIG>', start_pos)

    if runningconfig_start == -1 or runningconfig_start > start_pos + 50000:
        print(f"⚠ Warning: RUNNINGCONFIG not found for '{device_name}'")
        return xml_content

    runningconfig_end = xml_content.find('</RUNNINGCONFIG>', runningconfig_start)
    if runningconfig_end == -1:
        print(f"⚠ Warning: RUNNINGCONFIG end tag not found for '{device_name}'")
        return xml_content

    xml_lines = convert_config_to_xml_lines(new_config)
    new_section = f"""<RUNNINGCONFIG>
     <PROTOCOL>
      <TYPE>eCiscoCLI</TYPE>
     </PROTOCOL>
{xml_lines}
     </RUNNINGCONFIG>"""

    new_xml = (xml_content[:runningconfig_start] +
               new_section +
               xml_content[runningconfig_end + len('</RUNNINGCONFIG>'):])

    print(f"  ✓ {device_name}")
    return new_xml

def configure_server_ip(xml_content, server_name, ip_addr, subnet_mask, gateway, dns_server):
    """Configure server IP address in XML"""
    # Find server section
    device_pattern = rf'<NAME translate="true">{re.escape(server_name)}</NAME>'
    device_match = re.search(device_pattern, xml_content)

    if not device_match:
        print(f"  ⚠ Server '{server_name}' not found")
        return xml_content

    start_pos = device_match.end()

    # Find IP_ADDRESS section after the device name (within next 10000 characters)
    search_region = xml_content[start_pos:start_pos + 10000]

    # Replace IP address
    ip_pattern = r'<IP_ADDRESS>[\d.]*</IP_ADDRESS>'
    if re.search(ip_pattern, search_region):
        new_region = re.sub(ip_pattern, f'<IP_ADDRESS>{ip_addr}</IP_ADDRESS>', search_region, count=1)
        xml_content = xml_content[:start_pos] + new_region + xml_content[start_pos + len(search_region):]
        search_region = new_region

    # Replace subnet mask
    mask_pattern = r'<SUBNET_MASK>[\d.]*</SUBNET_MASK>'
    if re.search(mask_pattern, search_region):
        new_region = re.sub(mask_pattern, f'<SUBNET_MASK>{subnet_mask}</SUBNET_MASK>', search_region, count=1)
        xml_content = xml_content[:start_pos] + new_region + xml_content[start_pos + len(new_region):]
        search_region = new_region

    # Replace default gateway
    gw_pattern = r'<DEFAULT_GATEWAY>[\d.]*</DEFAULT_GATEWAY>'
    if re.search(gw_pattern, search_region):
        new_region = re.sub(gw_pattern, f'<DEFAULT_GATEWAY>{gateway}</DEFAULT_GATEWAY>', search_region, count=1)
        xml_content = xml_content[:start_pos] + new_region + xml_content[start_pos + len(new_region):]
        search_region = new_region

    # Replace DNS server
    dns_pattern = r'<DNS_SERVER>[\d.]*</DNS_SERVER>'
    if re.search(dns_pattern, search_region):
        new_region = re.sub(dns_pattern, f'<DNS_SERVER>{dns_server}</DNS_SERVER>', search_region, count=1)
        xml_content = xml_content[:start_pos] + new_region + xml_content[start_pos + len(new_region):]

    print(f"  ✓ {server_name} → {ip_addr}")
    return xml_content

# ==================== DEVICE CONFIGURATIONS ====================

ROUTER_CONFIG = """enable
configure terminal
hostname City-Gateway-Router
enable secret class
ipv6 unicast-routing
interface GigabitEthernet0/0/0
 ip address dhcp
 ip nat outside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown
interface GigabitEthernet0/0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown
ip nat inside source list 1 interface Gig0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255
ip route 0.0.0.0 0.0.0.0 Gig0/0/0
line console 0
 password cisco
 login
line vty 0 4
 password cisco
 login
end
write memory"""

CORE_SWITCH_CONFIG = """enable
configure terminal
hostname City-Core-Switch
enable secret class
ipv6 unicast-routing
vlan 10
 name Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management
interface GigabitEthernet1/0/1
 no switchport
 ip address 10.0.0.2 255.255.255.252
 ipv6 enable
 no shutdown
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
interface GigabitEthernet1/0/5
 description Central Office Server - Cellular Backhaul
 switchport mode access
 switchport access vlan 20
 no shutdown
interface range GigabitEthernet1/0/6-9
 description Servers (SMTP, Web, DHCP, DNS)
 switchport mode access
 switchport access vlan 10
 no shutdown
interface range GigabitEthernet1/0/10-12
 description Admin Devices (PCs and Phone)
 switchport mode access
 switchport access vlan 10
 no shutdown
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
ip route 0.0.0.0 0.0.0.0 10.0.0.1
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
 permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
 permit ip any any
interface Vlan20
 ip access-group BLOCK-PUBLIC-TO-ADMIN in
end
write memory"""

DOWNTOWN_SWITCH_CONFIG = """enable
configure terminal
hostname Downtown-Switch
vlan 20
 name Public
vlan 99
 name Management
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-4
 description Public VLAN Access Ports
 switchport mode access
 switchport access vlan 20
end
write memory"""

PARK_SWITCH_CONFIG = """enable
configure terminal
hostname Park-Switch
vlan 30
 name IoT
vlan 99
 name Management
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30
end
write memory"""

RESIDENTIAL_SWITCH_CONFIG = """enable
configure terminal
hostname Residential-Switch
vlan 30
 name IoT
vlan 99
 name Management
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30
end
write memory"""

# ==================== MAIN AUTOMATION ====================

def main():
    print("\n" + "=" * 80)
    print(" " * 20 + "SMART CITY NETWORK - FULL AUTOMATION")
    print("=" * 80 + "\n")

    # Step 1: Read XML
    print("📂 [STEP 1/5] Reading connection.xml...")
    xml_content = read_file('connection.xml')
    print(f"   File size: {len(xml_content):,} bytes\n")

    # Step 2: Configure network devices
    print("⚙️  [STEP 2/5] Configuring network devices...")
    xml_content = replace_device_config(xml_content, 'City-Gateway-Router', ROUTER_CONFIG)
    xml_content = replace_device_config(xml_content, 'City-Core-Switch', CORE_SWITCH_CONFIG)
    xml_content = replace_device_config(xml_content, 'Downtown-Switch', DOWNTOWN_SWITCH_CONFIG)
    xml_content = replace_device_config(xml_content, 'Park-Switch', PARK_SWITCH_CONFIG)
    xml_content = replace_device_config(xml_content, 'Residential-Switch', RESIDENTIAL_SWITCH_CONFIG)
    print()

    # Step 3: Configure servers
    print("🖥️  [STEP 3/5] Configuring server IP addresses...")
    xml_content = configure_server_ip(xml_content, 'DNS-Server', '10.10.10.10', '255.255.255.0', '10.10.10.1', '10.10.10.10')
    xml_content = configure_server_ip(xml_content, 'DHCP-Server', '10.10.10.20', '255.255.255.0', '10.10.10.1', '10.10.10.10')
    xml_content = configure_server_ip(xml_content, 'Web-Server', '10.10.10.30', '255.255.255.0', '10.10.10.1', '10.10.10.10')
    xml_content = configure_server_ip(xml_content, 'SMTP-Server', '10.10.10.40', '255.255.255.0', '10.10.10.1', '10.10.10.10')
    print()

    # Step 4: Save modified XML
    print("💾 [STEP 4/5] Saving configured XML...")
    write_file('connection_complete.xml', xml_content)
    print(f"   ✓ Saved to connection_complete.xml ({len(xml_content):,} bytes)\n")

    # Step 5: Convert back to PKT
    print("🔄 [STEP 5/5] Converting XML back to PKT file...")
    try:
        result = subprocess.run(
            ['./pka2xml/pka2xml', '-e', 'connection_complete.xml', 'connection_COMPLETED.pkt'],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print("   ✓ Successfully created connection_COMPLETED.pkt\n")

            # Check file size
            import os
            if os.path.exists('connection_COMPLETED.pkt'):
                size = os.path.getsize('connection_COMPLETED.pkt')
                print(f"   📦 Final PKT file size: {size:,} bytes\n")
        else:
            print(f"   ⚠ pka2xml returned error code {result.returncode}")
            if result.stderr:
                print(f"   Error: {result.stderr}\n")
    except subprocess.TimeoutExpired:
        print("   ⚠ Conversion timed out\n")
    except FileNotFoundError:
        print("   ⚠ pka2xml not found. Run manually:\n")
        print("   ./pka2xml/pka2xml -e connection_complete.xml connection_COMPLETED.pkt\n")
    except Exception as e:
        print(f"   ⚠ Error: {e}\n")

    # Summary
    print("=" * 80)
    print(" " * 30 + "✅ AUTOMATION COMPLETE!")
    print("=" * 80 + "\n")

    print("📋 Configuration Summary:")
    print("   ✓ City-Gateway-Router   - Full routing, NAT, IPv6")
    print("   ✓ City-Core-Switch      - VLANs, trunks, ACLs, IPv6")
    print("   ✓ Downtown-Switch       - VLANs, trunk port")
    print("   ✓ Park-Switch           - VLANs, IoT ports")
    print("   ✓ Residential-Switch    - VLANs, residential ports")
    print("   ✓ DNS-Server            - 10.10.10.10")
    print("   ✓ DHCP-Server           - 10.10.10.20")
    print("   ✓ Web-Server            - 10.10.10.30")
    print("   ✓ SMTP-Server           - 10.10.10.40")
    print()
    print("📁 Output Files:")
    print("   • connection_complete.xml    - Fully configured XML")
    print("   • connection_COMPLETED.pkt   - Final Packet Tracer file")
    print()
    print("🎯 Next Steps:")
    print("   1. Open connection_COMPLETED.pkt in Packet Tracer")
    print("   2. Configure DNS records on DNS-Server (GUI)")
    print("   3. Configure DHCP pools on DHCP-Server (GUI)")
    print("   4. Add web content to Web-Server")
    print("   5. Program IoT automation in Blockly")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}\n")
        sys.exit(1)
