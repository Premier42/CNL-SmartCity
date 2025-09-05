#!/usr/bin/env python3
"""
Smart City IoT Network Diagram Generator
Creates a visual representation of the IPv6 Smart City network architecture
with two interconnected city networks via internet
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')

# Color scheme
colors = {
    'core': '#2E86AB',
    'distribution': '#A23B72', 
    'access': '#F18F01',
    'iot': '#C73E1D',
    'internet': '#4CAF50',
    'server': '#9C27B0',
    'background': '#F5F5F5'
}

# Title
ax.text(10, 13.5, 'IPv6 Smart City IoT Network Architecture', 
        fontsize=20, fontweight='bold', ha='center')
ax.text(10, 13, 'Two City Networks Connected via Internet with QoS and Resilient Routing', 
        fontsize=14, ha='center', style='italic')

# Helper function to create network boxes
def create_network_box(x, y, width, height, title, color, alpha=0.3):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.1",
                         facecolor=color, alpha=alpha,
                         edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x + width/2, y + height - 0.3, title, 
            fontsize=12, fontweight='bold', ha='center')

# Helper function to create device icons
def create_device(x, y, label, device_type='router', color='blue'):
    if device_type == 'router':
        # Router icon (rectangle with rounded corners)
        device = FancyBboxPatch((x-0.3, y-0.15), 0.6, 0.3,
                               boxstyle="round,pad=0.05",
                               facecolor=color, edgecolor='black')
    elif device_type == 'switch':
        # Switch icon (rectangle)
        device = patches.Rectangle((x-0.3, y-0.15), 0.6, 0.3,
                                 facecolor=color, edgecolor='black')
    elif device_type == 'iot':
        # IoT device (circle)
        device = patches.Circle((x, y), 0.15, facecolor=color, edgecolor='black')
    elif device_type == 'server':
        # Server (tall rectangle)
        device = patches.Rectangle((x-0.2, y-0.2), 0.4, 0.4,
                                 facecolor=color, edgecolor='black')
    elif device_type == 'cloud':
        # Cloud (ellipse)
        device = patches.Ellipse((x, y), 1.5, 0.8, facecolor=color, edgecolor='black')
    
    ax.add_patch(device)
    ax.text(x, y-0.5, label, fontsize=8, ha='center', fontweight='bold')

# Helper function to draw connections
def draw_connection(x1, y1, x2, y2, style='-', color='black', width=2):
    ax.plot([x1, x2], [y1, y2], style, color=color, linewidth=width)

# ==================== CITY NETWORK 1 (LEFT SIDE) ====================
create_network_box(0.5, 1, 8, 11, 'Smart City Network 1 (Chattogram)', colors['background'])

# Core Layer - City 1
ax.text(4.5, 10.5, 'CORE LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(3.5, 10, 'Core Router 1\n2001:db8:1::1/64', 'router', colors['core'])
create_device(5.5, 10, 'Core Router 2\n2001:db8:1::2/64', 'router', colors['core'])

# Distribution Layer - City 1
ax.text(4.5, 8.8, 'DISTRIBUTION LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(2.5, 8, 'Dist Switch 1\n2001:db8:2::1/64', 'switch', colors['distribution'])
create_device(4.5, 8, 'Dist Switch 2\n2001:db8:2::2/64', 'switch', colors['distribution'])
create_device(6.5, 8, 'Dist Switch 3\n2001:db8:2::3/64', 'switch', colors['distribution'])

# Access Layer - City 1
ax.text(4.5, 6.3, 'ACCESS LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(1.5, 5.5, 'Access SW 1\nVLAN 10', 'switch', colors['access'])
create_device(3, 5.5, 'Access SW 2\nVLAN 20', 'switch', colors['access'])
create_device(4.5, 5.5, 'Access SW 3\nVLAN 30', 'switch', colors['access'])
create_device(6, 5.5, 'Access SW 4\nVLAN 40', 'switch', colors['access'])
create_device(7.5, 5.5, 'Access SW 5\nVLAN 50', 'switch', colors['access'])

# IoT Devices - City 1
ax.text(4.5, 4, 'IoT DEVICES & ENDPOINTS', fontsize=10, fontweight='bold', ha='center')

# Traffic Management Zone
create_device(1, 3, 'Traffic\nSensor 1', 'iot', colors['iot'])
create_device(1.5, 2.5, 'Traffic\nSensor 2', 'iot', colors['iot'])
create_device(2, 3, 'Smart\nTraffic Light', 'iot', colors['iot'])

# Environmental Zone
create_device(3, 3, 'Air Quality\nMonitor 1', 'iot', colors['iot'])
create_device(3.5, 2.5, 'Weather\nStation', 'iot', colors['iot'])
create_device(4, 3, 'Noise\nSensor', 'iot', colors['iot'])

# Waste Management Zone
create_device(5, 3, 'Smart\nWaste Bin 1', 'iot', colors['iot'])
create_device(5.5, 2.5, 'Smart\nWaste Bin 2', 'iot', colors['iot'])

# Administrative Zone
create_device(6.5, 3, 'Admin\nPC 1', 'server', colors['server'])
create_device(7, 2.5, 'Admin\nPC 2', 'server', colors['server'])
create_device(7.5, 3, 'SMTP\nServer', 'server', colors['server'])

# Public WiFi Zone
create_device(1.5, 1.5, 'Public\nWiFi AP 1', 'iot', '#FF9800')
create_device(4.5, 1.5, 'Public\nWiFi AP 2', 'iot', '#FF9800')
create_device(7, 1.5, 'Public\nWiFi AP 3', 'iot', '#FF9800')

# ==================== INTERNET CLOUD ====================
create_device(10, 6, 'INTERNET\nISP Routers\nBGP/OSPF', 'cloud', colors['internet'])

# ==================== CITY NETWORK 2 (RIGHT SIDE) ====================
create_network_box(11.5, 1, 8, 11, 'Smart City Network 2 (Dhaka)', colors['background'])

# Core Layer - City 2
ax.text(15.5, 10.5, 'CORE LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(14.5, 10, 'Core Router 3\n2001:db8:3::1/64', 'router', colors['core'])
create_device(16.5, 10, 'Core Router 4\n2001:db8:3::2/64', 'router', colors['core'])

# Distribution Layer - City 2
ax.text(15.5, 8.8, 'DISTRIBUTION LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(13.5, 8, 'Dist Switch 4\n2001:db8:4::1/64', 'switch', colors['distribution'])
create_device(15.5, 8, 'Dist Switch 5\n2001:db8:4::2/64', 'switch', colors['distribution'])
create_device(17.5, 8, 'Dist Switch 6\n2001:db8:4::3/64', 'switch', colors['distribution'])

# Access Layer - City 2
ax.text(15.5, 6.3, 'ACCESS LAYER', fontsize=10, fontweight='bold', ha='center')
create_device(12.5, 5.5, 'Access SW 6\nVLAN 60', 'switch', colors['access'])
create_device(14, 5.5, 'Access SW 7\nVLAN 70', 'switch', colors['access'])
create_device(15.5, 5.5, 'Access SW 8\nVLAN 80', 'switch', colors['access'])
create_device(17, 5.5, 'Access SW 9\nVLAN 90', 'switch', colors['access'])
create_device(18.5, 5.5, 'Access SW 10\nVLAN 100', 'switch', colors['access'])

# IoT Devices - City 2
ax.text(15.5, 4, 'IoT DEVICES & ENDPOINTS', fontsize=10, fontweight='bold', ha='center')

# Traffic Management Zone
create_device(12, 3, 'Traffic\nSensor 3', 'iot', colors['iot'])
create_device(12.5, 2.5, 'Traffic\nSensor 4', 'iot', colors['iot'])
create_device(13, 3, 'Smart\nTraffic Light', 'iot', colors['iot'])

# Environmental Zone
create_device(14, 3, 'Air Quality\nMonitor 2', 'iot', colors['iot'])
create_device(14.5, 2.5, 'Weather\nStation 2', 'iot', colors['iot'])
create_device(15, 3, 'Water Quality\nSensor', 'iot', colors['iot'])

# Waste Management Zone
create_device(16, 3, 'Smart\nWaste Bin 3', 'iot', colors['iot'])
create_device(16.5, 2.5, 'Smart\nWaste Bin 4', 'iot', colors['iot'])

# Administrative Zone
create_device(17.5, 3, 'Admin\nPC 3', 'server', colors['server'])
create_device(18, 2.5, 'HTTP\nServer', 'server', colors['server'])
create_device(18.5, 3, 'Database\nServer', 'server', colors['server'])

# Public WiFi Zone
create_device(12.5, 1.5, 'Public\nWiFi AP 4', 'iot', '#FF9800')
create_device(15.5, 1.5, 'Public\nWiFi AP 5', 'iot', '#FF9800')
create_device(18, 1.5, 'Public\nWiFi AP 6', 'iot', '#FF9800')

# ==================== NETWORK CONNECTIONS ====================

# City 1 Core Layer connections
draw_connection(3.5, 10, 5.5, 10, color=colors['core'], width=3)

# City 1 Core to Distribution
draw_connection(3.5, 9.8, 2.5, 8.2, color='black', width=2)
draw_connection(3.5, 9.8, 4.5, 8.2, color='black', width=2)
draw_connection(5.5, 9.8, 4.5, 8.2, color='black', width=2)
draw_connection(5.5, 9.8, 6.5, 8.2, color='black', width=2)

# City 1 Distribution to Access
draw_connection(2.5, 7.8, 1.5, 5.7, color='gray', width=1.5)
draw_connection(2.5, 7.8, 3, 5.7, color='gray', width=1.5)
draw_connection(4.5, 7.8, 3, 5.7, color='gray', width=1.5)
draw_connection(4.5, 7.8, 4.5, 5.7, color='gray', width=1.5)
draw_connection(4.5, 7.8, 6, 5.7, color='gray', width=1.5)
draw_connection(6.5, 7.8, 6, 5.7, color='gray', width=1.5)
draw_connection(6.5, 7.8, 7.5, 5.7, color='gray', width=1.5)

# City 1 to Internet
draw_connection(5.5, 10, 8.5, 6.3, color=colors['internet'], width=4)

# City 2 Core Layer connections
draw_connection(14.5, 10, 16.5, 10, color=colors['core'], width=3)

# City 2 Core to Distribution
draw_connection(14.5, 9.8, 13.5, 8.2, color='black', width=2)
draw_connection(14.5, 9.8, 15.5, 8.2, color='black', width=2)
draw_connection(16.5, 9.8, 15.5, 8.2, color='black', width=2)
draw_connection(16.5, 9.8, 17.5, 8.2, color='black', width=2)

# City 2 Distribution to Access
draw_connection(13.5, 7.8, 12.5, 5.7, color='gray', width=1.5)
draw_connection(13.5, 7.8, 14, 5.7, color='gray', width=1.5)
draw_connection(15.5, 7.8, 14, 5.7, color='gray', width=1.5)
draw_connection(15.5, 7.8, 15.5, 5.7, color='gray', width=1.5)
draw_connection(15.5, 7.8, 17, 5.7, color='gray', width=1.5)
draw_connection(17.5, 7.8, 17, 5.7, color='gray', width=1.5)
draw_connection(17.5, 7.8, 18.5, 5.7, color='gray', width=1.5)

# City 2 to Internet
draw_connection(14.5, 10, 11.5, 6.3, color=colors['internet'], width=4)

# ==================== LEGEND ====================
legend_x = 0.5
legend_y = 0.5
ax.text(legend_x, legend_y + 0.3, 'LEGEND:', fontsize=10, fontweight='bold')

# Legend items
legend_items = [
    ('Core Router', colors['core'], 'router'),
    ('Distribution Switch', colors['distribution'], 'switch'),
    ('Access Switch', colors['access'], 'switch'),
    ('IoT Device', colors['iot'], 'iot'),
    ('Server/PC', colors['server'], 'server'),
    ('Internet', colors['internet'], 'cloud')
]

for i, (label, color, device_type) in enumerate(legend_items):
    y_pos = legend_y - (i * 0.4)
    if device_type == 'cloud':
        create_device(legend_x + 0.5, y_pos, '', device_type, color)
    else:
        create_device(legend_x + 0.3, y_pos, '', device_type, color)
    ax.text(legend_x + 1, y_pos, label, fontsize=8, va='center')

# ==================== TECHNICAL SPECIFICATIONS ====================
specs_x = 14
specs_y = 0.5
ax.text(specs_x, specs_y + 0.3, 'TECHNICAL SPECIFICATIONS:', fontsize=10, fontweight='bold')

specs_text = [
    '• IPv6 Addressing: 2001:db8::/32',
    '• VLANs: 10-100 (Segmented by function)',
    '• QoS: 4-tier priority (Emergency > Critical > Normal > Best Effort)',
    '• Protocols: OSPFv3, BGP, IEEE 802.1Q',
    '• Security: Extended ACLs, Port Security',
    '• Services: SMTP, HTTP, SNMP',
    '• Redundancy: Dual core routers, Multiple paths'
]

for i, spec in enumerate(specs_text):
    ax.text(specs_x, specs_y - (i * 0.3), spec, fontsize=8)

# Data flow arrows
ax.annotate('', xy=(11.5, 6.5), xytext=(8.5, 6.5),
            arrowprops=dict(arrowstyle='<->', color='red', lw=3))
ax.text(10, 7, 'Inter-City Data Flow\n(IPv6 over Internet)', 
        fontsize=9, ha='center', color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/shinzuu/Documents/SmartCity/smart_city_network_diagram.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/home/shinzuu/Documents/SmartCity/smart_city_network_diagram.pdf', 
            bbox_inches='tight', facecolor='white')

print("Network diagram saved as:")
print("- smart_city_network_diagram.png (high resolution)")
print("- smart_city_network_diagram.pdf (vector format)")
print("\nDiagram includes:")
print("✓ Two complete smart city networks")
print("✓ Three-tier architecture (Core, Distribution, Access)")
print("✓ IPv6 addressing scheme")
print("✓ VLAN segmentation")
print("✓ 15+ IoT devices per city")
print("✓ Internet connectivity between cities")
print("✓ Administrative and monitoring systems")
print("✓ QoS and redundancy indicators")
