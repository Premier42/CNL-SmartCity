# Stage 3: Device Configuration
## Super Detailed Step-by-Step Guide - No Mistakes!

**Total Time: ~60 minutes**
**Difficulty: Easy (just follow exactly)**

---

## 📋 Before You Start

### Required Items Checklist:
- [x] Stage 2 complete (all 23 devices physically connected)
- [x] All cables showing (should be orange/yellow, will turn green after config)
- [x] Packet Tracer open with your topology
- [x] This guide open for reference

### Important Notes:
- ⚠️ Copy-paste configurations **exactly as written**
- ⚠️ Don't skip steps - do them in order
- ⚠️ Verify each step before moving to next
- ⚠️ If something fails, refer to troubleshooting section
- ⚠️ **CRITICAL:** Always use `exit` to leave interface mode before entering a new interface
  - While Cisco IOS allows jumping between interfaces, we use `exit` for clarity
  - This prevents confusion and ensures you're always in the right mode
  - Watch the prompt: `(config-if)#` means you're IN an interface, `(config)#` means global config

### Understanding Cisco IOS Configuration Modes:

```
Router>                          ← User mode (limited)
  ↓ (type: enable)
Router#                          ← Privileged mode (can view config)
  ↓ (type: configure terminal)
Router(config)#                  ← Global configuration mode
  ↓ (type: interface Gig0/0/0)
Router(config-if)#               ← Interface configuration mode
  ↓ (type: exit)
Router(config)#                  ← Back to global config
  ↓ (type: exit or end)
Router#                          ← Back to privileged mode
```

**Key Rule:** To move between different interfaces, ALWAYS exit to `(config)#` first!

---

## Phase 1: Router Configuration (10 minutes)

### Step 1.1: Access Router CLI

1. **Click** on `City-Gateway-Router` device
2. **Click** the **CLI tab** at the top
3. **Press Enter** if you see "Press RETURN to get started"
4. You should see `Router>` prompt

**What you see:**
```
Would you like to enter the initial configuration dialog? [yes/no]:
```

**What to do:**
- Type: `no`
- Press **Enter**

### Step 1.2: Enter Configuration Mode

**Type these commands EXACTLY (press Enter after each line):**

```
enable
configure terminal
```

**What you should see:**
```
Router>enable
Router#configure terminal
Router(config)#
```

✅ **Success:** You see `Router(config)#` prompt

### Step 1.3: Set Router Hostname and Password

**Copy and paste this block:**

```
hostname City-Gateway-Router
enable secret class
```

**What you should see:**
```
Router(config)#hostname City-Gateway-Router
City-Gateway-Router(config)#enable secret class
City-Gateway-Router(config)#
```

✅ **Success:** Prompt changed from `Router(config)#` to `City-Gateway-Router(config)#`

### Step 1.4: Enable IPv6 Routing

**Copy and paste:**

```
ipv6 unicast-routing
```

✅ **Success:** No error message = it worked

### Step 1.5: Configure WAN Interface (Internet)

**Copy and paste this block:**

```
interface GigabitEthernet0/0/0
 ip address dhcp
 ip nat outside
 ipv6 address autoconfig
 ipv6 enable
 no shutdown
```

**What you should see:**
```
City-Gateway-Router(config)#interface GigabitEthernet0/0/0
City-Gateway-Router(config-if)#ip address dhcp
City-Gateway-Router(config-if)#ip nat outside
City-Gateway-Router(config-if)#ipv6 address autoconfig
City-Gateway-Router(config-if)#ipv6 enable
City-Gateway-Router(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
```

✅ **Success:** You see "changed state to up" messages
✅ **Success:** Prompt shows `(config-if)#` (interface configuration mode)

### Step 1.6: Configure LAN Interface (to Core Switch)

**Copy and paste this block:**

```
interface GigabitEthernet0/0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 no shutdown
```

**Now configure IPv6 using autoconfig (this works on your PT!):**

```
ipv6 address autoconfig
ipv6 enable
```

**What you should see:**
```
City-Gateway-Router(config-if)#ipv6 address autoconfig
City-Gateway-Router(config-if)#ipv6 enable
City-Gateway-Router(config-if)#
```

✅ **Success!** IPv6 is now configured and will auto-generate an address

**What this does:**
- Auto-configures IPv6 address using SLAAC (Stateless Address Autoconfiguration)
- Works perfectly for your PT version
- Creates working IPv6 connectivity

**Then continue:**
```
exit
```

**What you should see:**
```
City-Gateway-Router(config-if)#interface GigabitEthernet0/0/1
City-Gateway-Router(config-if)#ip address 10.0.0.1 255.255.255.252
City-Gateway-Router(config-if)#ip nat inside
City-Gateway-Router(config-if)#ipv6 address 2001:DB8:CITY:0::1/64
City-Gateway-Router(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/0/1, changed state to up
```

✅ **Success:** Interface comes up

### Step 1.7: Configure NAT

**Copy and paste this block:**

```
exit
ip nat inside source list 1 interface Gig0/0/0 overload
access-list 1 permit 10.10.0.0 0.0.255.255
```

**Note:** `exit` takes you back to `(config)#` mode from `(config-if)#`

✅ **Success:** Prompt changed back to `City-Gateway-Router(config)#`

### Step 1.8: Configure Default Routes

**Copy and paste:**

```
ip route 0.0.0.0 0.0.0.0 Gig0/0/0
ipv6 route ::/0 Gig0/0/0
```

✅ **Success:** No error messages

### Step 1.9: Configure Console and VTY Access

**Copy and paste this block:**

```
line console 0
 password cisco
 login
line vty 0 4
 password cisco
 login
```

**What you should see:**
```
City-Gateway-Router(config)#line console 0
City-Gateway-Router(config-line)#password cisco
City-Gateway-Router(config-line)#login
City-Gateway-Router(config-line)#line vty 0 4
City-Gateway-Router(config-line)#password cisco
City-Gateway-Router(config-line)#login
```

✅ **Success:** Prompt shows `(config-line)#`

### Step 1.10: Save Router Configuration

**Copy and paste:**

```
end
write memory
```

**What you should see:**
```
City-Gateway-Router(config-line)#end
City-Gateway-Router#write memory
Building configuration...
[OK]
City-Gateway-Router#
```

✅ **Success:** You see `[OK]` message
✅ **Success:** Prompt is now `City-Gateway-Router#` (no longer in config mode)

### Step 1.11: Verify Router Configuration

**Type this command:**

```
show ip interface brief
```

**What you should see:**
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   192.168.1.X     YES DHCP   up                    up
GigabitEthernet0/0/1   10.0.0.1        YES manual up                    up
```

**Check these:**
- ✅ Gig0/0/0 has an IP from DHCP (any IP like 192.168.x.x)
- ✅ Gig0/0/1 shows 10.0.0.1
- ✅ Both show "up" and "up" for Status and Protocol

**Type this command:**

```
show ipv6 interface brief
```

**What you should see:**
```
GigabitEthernet0/0/0   [up/up]
    FE80::...
    (may show additional IPv6 addresses)
GigabitEthernet0/0/1   [up/up]
    FE80::...
    2001:DB8:CITY:0::1
```

**Check:**
- ✅ Both interfaces show [up/up]
- ✅ Gig0/0/1 shows 2001:DB8:CITY:0::1

---

## ✅ **ROUTER COMPLETE! - Take a 2 minute break**

**What should have happened:**
- Cable between Router and Core Switch turned **green**
- Router has IP addresses on both interfaces
- Ready for next step

---

## Phase 2: Core Switch Configuration (15 minutes)

### Step 2.1: Access Core Switch CLI

1. **Click** on `City-Core-Switch` device
2. **Click** the **CLI tab**
3. **Press Enter** if prompted

**Type:**
```
no
```
(if asked about initial configuration dialog)

### Step 2.2: Enter Configuration Mode

```
enable
configure terminal
```

**What you should see:**
```
Switch>enable
Switch#configure terminal
Switch(config)#
```

### Step 2.3: Set Hostname and Password

```
hostname City-Core-Switch
enable secret class
```

✅ **Success:** Prompt changes to `City-Core-Switch(config)#`

### Step 2.4: Enable IPv6 Routing

```
ipv6 unicast-routing
```

⚠️ **Important:** This is CRITICAL for Layer 3 switching

### Step 2.5: Create VLANs

**Copy and paste this ENTIRE block:**

```
vlan 10
 name Admin
vlan 20
 name Public
vlan 30
 name IoT
vlan 99
 name Management
```

**What you should see:**
```
City-Core-Switch(config)#vlan 10
City-Core-Switch(config-vlan)#name Admin
City-Core-Switch(config-vlan)#vlan 20
City-Core-Switch(config-vlan)#name Public
...
```

✅ **Success:** Prompt shows `(config-vlan)#` while in VLAN config

### Step 2.6: Verify VLANs Created

**Type:**
```
exit
do show vlan brief
```

**What you should see:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gig0/1, Gig0/2, Fa0/1, Fa0/2...
10   Admin                            active
20   Public                           active
30   IoT                              active
99   Management                       active
```

✅ **Success:** All 4 VLANs appear (10, 20, 30, 99)

### Step 2.7: Configure Router Connection (Layer 3 Port)

**⚠️ CRITICAL: This is a Layer 3 routed port, NOT a switch port!**

**First, configure IPv4:**

```
interface GigabitEthernet0/1
 no switchport
 ip address 10.0.0.2 255.255.255.252
 no shutdown
```

**Configure IPv6 (this will work since router IPv6 worked!):**

```
ipv6 enable
```

✅ **This should work without errors**

**What you should see:**
```
City-Core-Switch(config)#interface GigabitEthernet0/1
City-Core-Switch(config-if)#no switchport
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down
City-Core-Switch(config-if)#ip address 10.0.0.2 255.255.255.252
City-Core-Switch(config-if)#ipv6 address 2001:DB8:CITY:0::2/64
City-Core-Switch(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up
```

✅ **Success:** Interface comes up
✅ **Success:** Cable to router should now be **GREEN**

### Step 2.8: Exit Interface Mode and Test

**Type:**
```
exit
```

**What you should see:**
```
City-Core-Switch(config-if)#exit
City-Core-Switch(config)#
```

✅ **Success:** Prompt changed from `(config-if)#` to `(config)#`

**Now test router connection:**
```
do ping 10.0.0.1
```

**What you should see:**
```
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.0.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 0/0/1 ms
```

✅ **Success:** You see `!!!!!` (5 exclamation marks = 5 successful pings)

⚠️ **If you see `.....` (5 dots):**
- Go back and check router Gig0/0/1 is configured
- Check cable is connected
- Verify IP addresses match (10.0.0.1 on router, 10.0.0.2 on switch)

### Step 2.9: Configure Trunk to Downtown-Switch

**Now configure the first trunk port:**

```
interface GigabitEthernet0/2
 description Trunk to Downtown-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
```

✅ **Success:** No error messages

### Step 2.10: Exit and Configure Trunk to Park-Switch

**First, exit the interface:**
```
exit
```

**Then configure Park-Switch trunk:**
```
interface GigabitEthernet0/3
 description Trunk to Park-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
```

### Step 2.11: Exit and Configure Trunk to Residential-Switch

**Exit the interface:**
```
exit
```

**Configure Residential-Switch trunk:**
```
interface GigabitEthernet0/4
 description Trunk to Residential-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
```

### Step 2.12: Exit and Configure Cellular Backhaul Port

**Exit the interface:**
```
exit
```

**Configure cellular backhaul port:**
```
interface FastEthernet0/3
 description Central Office Server - Cellular Backhaul
 switchport mode access
 switchport access vlan 20
 no shutdown
```

### Step 2.13: Exit and Configure Server and Admin Ports

**Exit the interface:**
```
exit
```

**Configure server and admin ports (all at once using range):**
```
interface range FastEthernet0/4-10
 description Servers and Admin Devices
 switchport mode access
 switchport access vlan 10
 no shutdown
```

✅ **Success:** All 7 ports (Fa0/4 through Fa0/10) configured at once

### Step 2.14: Exit and Configure VLAN 10 Interface (Admin)

**Exit the interface range:**
```
exit
```

**You should now be at `City-Core-Switch(config)#` prompt**

**Configure VLAN 10 SVI (Switch Virtual Interface):**

**IPv4 first:**
```
interface Vlan10
 description Admin VLAN Gateway
 ip address 10.10.10.1 255.255.255.0
 no shutdown
```

**IPv6:**
```
ipv6 enable
```

**What you should see:**
```
%LINK-5-CHANGED: Interface Vlan10, changed state to up
```

### Step 2.15: Exit and Configure VLAN 20 Interface (Public)

**Exit VLAN 10 interface:**
```
exit
```

**Configure VLAN 20 SVI:**
```
interface Vlan20
 description Public VLAN Gateway
 ip address 10.10.20.1 255.255.255.0
 no shutdown
```

**IPv6:**
```
ipv6 enable
```

### Step 2.16: Exit and Configure VLAN 30 Interface (IoT)

**Exit VLAN 20 interface:**
```
exit
```

**Configure VLAN 30 SVI:**
```
interface Vlan30
 description IoT VLAN Gateway
 ip address 10.10.30.1 255.255.255.0
 no shutdown
 ipv6 enable
```

### Step 2.17: Exit and Configure VLAN 99 Interface (Management)

**Exit VLAN 30 interface:**
```
exit
```

**Configure VLAN 99 SVI:**
```
interface Vlan99
 description Management VLAN Gateway
 ip address 10.10.99.1 255.255.255.0
 no shutdown
 ipv6 enable
```

### Step 2.18: Configure Default Routes

```
exit
ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

✅ **Success:** No error messages

**Note:** IPv6 routing will work automatically with `ipv6 enable` - no manual route needed!

### Step 2.19: Configure IPv4 Security ACL

**⚠️ IMPORTANT: This ACL allows DNS while blocking other Admin access**

**Copy and paste this ENTIRE block carefully:**

```
ip access-list extended BLOCK-PUBLIC-TO-ADMIN
 permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
 deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
 permit ip any any
```

**What you should see:**
```
City-Core-Switch(config)#ip access-list extended BLOCK-PUBLIC-TO-ADMIN
City-Core-Switch(config-ext-nacl)#permit udp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
City-Core-Switch(config-ext-nacl)#permit tcp 10.10.20.0 0.0.0.255 host 10.10.10.10 eq 53
City-Core-Switch(config-ext-nacl)#deny ip 10.10.20.0 0.0.0.255 10.10.10.0 0.0.0.255
City-Core-Switch(config-ext-nacl)#permit ip any any
```

✅ **Success:** Prompt shows `(config-ext-nacl)#`

### Step 2.20: Apply IPv4 ACL to VLAN 20

**Enter VLAN 20 interface:**
```
interface Vlan20
 ip access-group BLOCK-PUBLIC-TO-ADMIN in
```

**Exit back to config mode:**
```
exit
```

### Step 2.21: IPv6 Security ACL (SKIP - Not needed with autoconfig)

**Since we're using IPv6 autoconfig (link-local addresses), we don't need IPv6 ACLs.**

**IPv4 ACL is sufficient for security - skip this step and continue to save configuration.**

✅ **This is fine** - IPv4 ACL provides the security we need

### Step 2.23: Save Core Switch Configuration

```
end
write memory
```

**What you should see:**
```
City-Core-Switch#write memory
Building configuration...
[OK]
```

✅ **Success:** See `[OK]`

### Step 2.24: Verify Core Switch Configuration

**Type these verification commands:**

```
show ip interface brief
```

**Check for:**
- ✅ Gig0/1 shows 10.0.0.2 and is up/up
- ✅ Vlan10 shows 10.10.10.1 and is up/up
- ✅ Vlan20 shows 10.10.20.1 and is up/up
- ✅ Vlan30 shows 10.10.30.1 and is up/up
- ✅ Vlan99 shows 10.10.99.1 and is up/up

```
show vlan brief
```

**Check for:**
- ✅ Fa0/3 in VLAN 20
- ✅ Fa0/4-10 in VLAN 10
- ✅ Gig0/2, Gig0/3, Gig0/4 should NOT appear (they're trunks)

```
show interfaces trunk
```

**Check for:**
- ✅ Gig0/2, Gig0/3, Gig0/4 listed as trunks
- ✅ Native VLAN: 99
- ✅ VLANs allowed: 10,20,30,99

---

## ✅ **CORE SWITCH COMPLETE! - Take a 5 minute break**

**Critical cables should now be GREEN:**
- ✅ Router ↔ Core Switch = GREEN
- 🟠 Core Switch ↔ District Switches = Still orange (switches not configured yet)

---

## Phase 3: District Switches Configuration (10 minutes)

### Step 3.1: Configure Downtown-Switch

1. **Click** on `Downtown-Switch`
2. **Click** CLI tab
3. **Type:**

```
no
enable
configure terminal
hostname Downtown-Switch
enable secret class
```

4. **Create VLANs:**

```
vlan 20
 name Public
vlan 99
 name Management
```

5. **Configure Trunk Port:**

```
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 no shutdown
```

6. **Configure Access Ports:**

```
interface range FastEthernet0/2-4
 description Public VLAN Access Ports
 switchport mode access
 switchport access vlan 20
 no shutdown
```

7. **Save:**

```
end
write memory
```

✅ **Success:** Cable to Core Switch should turn **GREEN**

### Step 3.2: Configure Park-Switch

1. **Click** on `Park-Switch`
2. **Click** CLI tab
3. **Copy and paste:**

```
no
enable
configure terminal
hostname Park-Switch
enable secret class
vlan 30
 name IoT
vlan 99
 name Management
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 no shutdown
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30
 no shutdown
end
write memory
```

✅ **Success:** Cable to Core Switch turns **GREEN**

### Step 3.3: Configure Residential-Switch

1. **Click** on `Residential-Switch`
2. **Click** CLI tab
3. **Copy and paste:**

```
no
enable
configure terminal
hostname Residential-Switch
enable secret class
vlan 30
 name IoT
vlan 99
 name Management
interface FastEthernet0/1
 description Trunk to City-Core-Switch
 switchport mode trunk
 switchport trunk native vlan 99
 no shutdown
interface range FastEthernet0/2-3
 description IoT VLAN Access Ports
 switchport mode access
 switchport access vlan 30
 no shutdown
end
write memory
```

✅ **Success:** Cable to Core Switch turns **GREEN**

### Step 3.4: Verify District Switches

**On each district switch, type:**

```
show vlan brief
```

**Downtown-Switch should show:**
- ✅ VLAN 20 (Public)
- ✅ VLAN 99 (Management)
- ✅ Fa0/2, Fa0/3, Fa0/4 in VLAN 20

**Park-Switch should show:**
- ✅ VLAN 30 (IoT)
- ✅ VLAN 99 (Management)
- ✅ Fa0/2, Fa0/3 in VLAN 30

**Residential-Switch should show:**
- ✅ VLAN 30 (IoT)
- ✅ VLAN 99 (Management)
- ✅ Fa0/2, Fa0/3 in VLAN 30

---

## ✅ **ALL SWITCHES COMPLETE! - Take a 2 minute break**

**What should have happened:**
- All switch-to-switch cables are now **GREEN**
- VLANs created on all switches
- Ready for server configuration

---

## Phase 4: Server Configuration (20 minutes)

### Step 4.1: Configure DNS Server

1. **Click** on `DNS-Server`
2. **Click** Desktop tab
3. **Click** IP Configuration

**Configure IPv4:**
- IPv4 Address: `10.10.10.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`

4. **Configure IPv6:**
- **Check** the "IPv6" checkbox
- IPv6 Address: `2001:DB8:CITY:10::10/64`
- IPv6 Gateway: `2001:DB8:CITY:10::1`

5. **Close** IP Configuration window

6. **Click** Services tab
7. **Click** DNS

8. **Turn DNS ON:**
- Click the **ON** radio button

9. **Add DNS A Records (IPv4):**

Click "Add" for each record:

| Name | Type | Address |
|------|------|---------|
| smartcity.local | A Record | 10.10.10.30 |
| dns.smartcity.local | A Record | 10.10.10.10 |
| dhcp.smartcity.local | A Record | 10.10.10.20 |
| web.smartcity.local | A Record | 10.10.10.30 |
| mail.smartcity.local | A Record | 10.10.10.40 |
| centraloffice.smartcity.local | A Record | 10.10.20.50 |

**How to add a record:**
- Name: `smartcity.local`
- Type: Select `A Record`
- Address: `10.10.10.30`
- Click **Add**

Repeat for all 6 records.

10. **Add AAAA Records (IPv6) - IF AVAILABLE:**

If you see option for AAAA records, add these:

| Name | Type | Address |
|------|------|---------|
| smartcity.local | AAAA Record | 2001:DB8:CITY:10::30 |
| dns.smartcity.local | AAAA Record | 2001:DB8:CITY:10::10 |
| dhcp.smartcity.local | AAAA Record | 2001:DB8:CITY:10::20 |
| web.smartcity.local | AAAA Record | 2001:DB8:CITY:10::30 |
| mail.smartcity.local | AAAA Record | 2001:DB8:CITY:10::40 |
| centraloffice.smartcity.local | AAAA Record | 2001:DB8:CITY:20::50 |

**⚠️ If AAAA not available:** Skip this - it's a Packet Tracer limitation, not your fault

✅ **DNS Server Complete**

### Step 4.2: Configure DHCP Server

1. **Click** on `DHCP-Server`
2. **Click** Desktop tab
3. **Click** IP Configuration

**Configure IPv4:**
- IPv4 Address: `10.10.10.20`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`

**Configure IPv6:**
- IPv6 Address: `2001:DB8:CITY:10::20/64`
- IPv6 Gateway: `2001:DB8:CITY:10::1`

4. **Close** IP Configuration

5. **Click** Services tab
6. **Click** DHCP

**Configure Admin Pool:**
- Pool Name: `AdminPool`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`
- Start IP Address: `10.10.10.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `50`
- Click **Add**

**Configure Public Pool:**
- Click "+" to add new pool
- Pool Name: `PublicPool`
- Default Gateway: `10.10.20.1`
- DNS Server: `10.10.10.10`
- Start IP Address: `10.10.20.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `100`
- Click **Add**

**Configure IoT Pool:**
- Click "+" to add new pool
- Pool Name: `IoTPool`
- Default Gateway: `10.10.30.1`
- DNS Server: `10.10.10.10`
- Start IP Address: `10.10.30.100`
- Subnet Mask: `255.255.255.0`
- Maximum Number of Users: `50`
- Click **Add**

7. **Turn DHCP Service ON**
- Make sure DHCP is set to **ON**

✅ **DHCP Server Complete**

### Step 4.3: Configure Web Server

1. **Click** on `Web-Server`
2. **Click** Desktop → IP Configuration

**Configure IPv4:**
- IPv4 Address: `10.10.10.30`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`

**Configure IPv6:**
- IPv6 Address: `2001:DB8:CITY:10::30/64`
- IPv6 Gateway: `2001:DB8:CITY:10::1`

3. **Click** Services tab
4. **Click** HTTP

5. **Turn HTTP ON**
- Click **ON** radio button

6. **(Optional) Customize webpage:**
- Click on `index.html`
- Edit the HTML to say "Smart City Dashboard"
- Example:
```html
<html>
<head><title>Smart City</title></head>
<body>
<h1>Welcome to Smart City Dashboard</h1>
<p>Network Status: Online</p>
</body>
</html>
```

✅ **Web Server Complete**

### Step 4.4: Configure SMTP Server

1. **Click** on `SMTP-Server`
2. **Click** Desktop → IP Configuration

**Configure IPv4:**
- IPv4 Address: `10.10.10.40`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`

**Configure IPv6:**
- IPv6 Address: `2001:DB8:CITY:10::40/64`
- IPv6 Gateway: `2001:DB8:CITY:10::1`

3. **Click** Services tab
4. **Click** EMAIL

5. **Set Domain Name:**
- Domain Name: `smartcity.local`

6. **Create User Account:**
- User: `admin`
- Password: `admin`
- Click **+** to add user

7. **Turn Email Service ON** (if not already on)

✅ **SMTP Server Complete**

### Step 4.5: Configure Central Office Server

1. **Click** on `Central-Office-Server`
2. **Click** Desktop → IP Configuration

**Configure IPv4:**
- IPv4 Address: `10.10.20.50`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.20.1`
- DNS Server: `10.10.10.10`

**Configure IPv6:**
- IPv6 Address: `2001:DB8:CITY:20::50/64`
- IPv6 Gateway: `2001:DB8:CITY:20::1`

**No services needed** - this server acts as cellular gateway only

✅ **Central Office Server Complete**

### Step 4.6: Test Server Connectivity

**From Admin-PC-1:**

1. Click Admin-PC-1
2. Desktop → Command Prompt
3. Type:

```
ping 10.10.10.10
ping 10.10.10.20
ping 10.10.10.30
ping 10.10.10.40
```

**Expected:**
- ✅ All should reply successfully
- ✅ See "Reply from..." messages

**If ping fails:**
- Check IP addresses are correct
- Check cable is connected
- Check VLAN assignments

---

## ✅ **ALL SERVERS COMPLETE! - Take a 5 minute break**

---

## Phase 5: End User Devices (10 minutes)

### Step 5.1: Configure Admin PCs

**Admin-PC-1:**
1. Click Admin-PC-1
2. Desktop → IP Configuration
3. Select **DHCP** radio button
4. Wait 5 seconds
5. Should get IP in range 10.10.10.100-150

**Admin-PC-2:**
- Same process
- Should get different IP in same range

✅ **Verify:** Both PCs have IPs starting with 10.10.10.x

### Step 5.2: Configure City Hall Phone

1. Click City-Hall-Phone
2. It should auto-configure via DHCP
3. Check Config tab → FastEthernet0
4. Should show IP in 10.10.10.x range

### Step 5.3: Configure Public Kiosk PC

1. Click Public-Kiosk-PC
2. Desktop → IP Configuration
3. Select **DHCP**
4. Should get IP in 10.10.20.100-200 range

✅ **Verify:** IP starts with 10.10.20.x (Public VLAN)

### Step 5.4: Configure Info Line Phone

1. Click Info-Line-Phone
2. Should auto-configure
3. Check IP is in 10.10.20.x range

### Step 5.5: Configure Resident Home PC

1. Click Resident-Home-PC
2. Desktop → IP Configuration
3. Select **DHCP**
4. Should get IP in 10.10.30.100-150 range

✅ **Verify:** IP starts with 10.10.30.x (IoT VLAN)

---

## Phase 6: Wireless Configuration (5 minutes)

### Step 6.1: Configure Public WiFi AP

1. **Click** Public-WiFi-AP
2. **Click** GUI tab (not Config, not CLI)
3. **Click** "Wireless" or "Setup"

**Configure:**
- Network Name (SSID): `City-Public-WiFi`
- Security Mode: `WPA2 Personal` or `WPA2-PSK`
- Passphrase: `publicaccess`
- Channel: `Auto` or `6`

4. **Network Setup:**
- Connection Type: `Automatic Configuration - DHCP`

5. **Save Settings** (if button available)

### Step 6.2: Configure Residential WiFi AP

1. **Click** Residential-WiFi-AP
2. **Click** GUI tab

**Configure:**
- Network Name (SSID): `Residential-Network`
- Security Mode: `WPA2 Personal` or `WPA2-PSK`
- Passphrase: `homeaccess`
- Channel: `Auto` or `11`

**Network Setup:**
- Connection Type: `Automatic Configuration - DHCP`

### Step 6.3: Connect Smartphone to WiFi

1. **Click** Citizen-Smartphone
2. **Click** Desktop tab
3. **Click** PC Wireless

4. **Connect to WiFi:**
- You should see `City-Public-WiFi` in the list
- Click on it
- Click **Connect**
- Enter password: `publicaccess`
- Click **Connect**

5. **Verify Connection:**
- Should show "Connected"
- Should get IP in 10.10.20.x range
- Click "More Information" to see IP

✅ **Success:** Smartphone connected to WiFi with IP address

---

## Phase 7: IoT Configuration (10 minutes)

### Step 7.1: Configure Smart Streetlight

1. **Click** Smart-Streetlight
2. **Click** Config tab
3. **Click** FastEthernet0 (or whatever port shows)

**Set Static IP:**
- IP Address: `10.10.30.20`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.30.1`
- DNS Server: `10.10.10.10`

**Or use Desktop → IP Configuration:**
- Select **Static**
- Enter same values above

✅ **Success:** Smart LED has IP 10.10.30.20

### Step 7.2: Configure Park IoT Gateway

1. **Click** Park-IoT-Gateway
2. **Click** Desktop → IP Configuration

**Set Static IP:**
- IPv4 Address: `10.10.30.10`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.30.1`
- DNS Server: `10.10.10.10`

### Step 7.3: Program IoT Automation (Blockly)

1. Still on Park-IoT-Gateway
2. **Click** Programming tab

**⚠️ Note:** Blockly interface varies by PT version. Follow this logic:

**Create this automation:**

```
WHEN [Motion Sensor on D0] IS ACTIVATED
 THEN
   Set IoT Device at 10.10.30.20 brightness to 1023
 WAIT 60 seconds
 THEN
   Set IoT Device at 10.10.30.20 brightness to 0
 AND
   Send Email:
     To: admin@smartcity.local
     From: iot@smartcity.local
     Subject: "Park Alert"
     Message: "Motion detected - light activated"
     SMTP Server: 10.10.10.40
```

**How to build in Blockly:**

1. **Add Condition Block:**
   - Find "When" or "If" block
   - Set to: Motion Sensor (D0) is activated

2. **Add Action Block:**
   - Find "Set IoT Device" or "Control Device"
   - IP: 10.10.30.20
   - Property: brightness
   - Value: 1023

3. **Add Wait Block:**
   - Find "Wait" block
   - Set: 60 seconds

4. **Add Turn Off Block:**
   - IP: 10.10.30.20
   - brightness: 0

5. **Add Email Block:**
   - Find "Send Email" block
   - Configure all fields as above

6. **Save/Run** the program

⚠️ **If you can't find exact blocks:** Use similar logic blocks available in your PT version

---

## Final Verification (5 minutes)

### Test 1: Basic Connectivity (from Admin-PC-1)

```
ping 10.10.10.1
ping 10.10.20.1
ping 10.10.30.1
ping 10.0.0.1
ping 8.8.8.8
```

✅ **All should succeed**

### Test 2: DNS Resolution

```
nslookup smartcity.local
```

✅ **Should return: 10.10.10.30**

### Test 3: Web Access

1. Admin-PC-1 → Desktop → Web Browser
2. Enter: `http://smartcity.local`
3. Should see Smart City Dashboard

✅ **Success**

### Test 4: Security ACL (from Public-Kiosk-PC)

```
nslookup smartcity.local
```
✅ **Should WORK** (DNS allowed)

```
ping 10.10.10.10
```
❌ **Should FAIL** (ICMP blocked)

```
ping 10.10.10.1
```
❌ **Should FAIL** (Admin VLAN blocked)

### Test 5: IoT Automation

1. Click Park-Motion-Sensor
2. Click "Activate" or toggle it
3. Watch Smart-Streetlight
4. Should turn ON (blue, brightness 1023)
5. Wait 60 seconds
6. Should turn OFF (brightness 0)

### Test 6: VoIP

1. Click City-Hall-Phone
2. Dial the number of Info-Line-Phone
3. Call should connect

---

## ✅ CONFIGURATION COMPLETE!

**All 23 devices configured and working!**

---

## Common Issues & Solutions

### Issue: Router Gig0/0/1 won't come up
**Solution:**
- Check cable is connected
- Type: `no shutdown` on the interface
- Verify Core Switch Gig0/1 is configured

### Issue: DHCP not working
**Solution:**
- Check DHCP Server is in VLAN 10
- Verify DHCP service is ON
- Check IP Helper if needed (not needed in this design)

### Issue: Ping works but DNS doesn't
**Solution:**
- Check DNS server IP is 10.10.10.10
- Verify DNS service is ON
- Check A records are added correctly

### Issue: ACL blocks everything including DNS
**Solution:**
- Make sure DNS permit lines are BEFORE deny line
- Order matters in ACLs!

### Issue: IoT automation not working
**Solution:**
- Verify Smart LED has correct IP (10.10.30.20)
- Check SMTP server is configured
- Verify Blockly program saved

### Issue: Can't ping between VLANs
**Solution:**
- Check VLAN interfaces are up (no shutdown)
- Verify default routes on Core Switch
- Check devices have correct gateway

---

## Troubleshooting Commands

**On Router:**
```
show ip interface brief
show ipv6 interface brief
show ip route
show ip nat translations
```

**On Core Switch:**
```
show ip interface brief
show vlan brief
show interfaces trunk
show ip route
show access-lists
show ipv6 interface brief
```

**On PCs:**
```
ipconfig
ipconfig /all
ping [ip]
tracert [ip]
nslookup [domain]
```

---

## Success Checklist

- [ ] All cables are GREEN
- [ ] Router has IP on both interfaces
- [ ] Core Switch has all VLAN interfaces up
- [ ] All district switches configured
- [ ] All servers have correct IPs
- [ ] DHCP working (PCs get IPs automatically)
- [ ] DNS working (nslookup returns correct IPs)
- [ ] Web server accessible via browser
- [ ] ACL blocks Public→Admin but allows DNS
- [ ] IoT automation working
- [ ] VoIP phones can call each other
- [ ] Smartphone connected to WiFi

---

**🎉 CONGRATULATIONS! You've successfully configured a complete smart city network!**

Next: Test everything thoroughly and prepare for demonstration!
