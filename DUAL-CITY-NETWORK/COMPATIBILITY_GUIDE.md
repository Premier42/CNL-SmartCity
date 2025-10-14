# PACKET TRACER COMPATIBILITY GUIDE
## Ensuring Your Project Works with Your PT Version

**Last Updated:** October 2025

---

## 🎯 QUICK VERSION CHECK

### **Check Your Packet Tracer Version:**

1. Open Cisco Packet Tracer
2. Click **Help** → **About**
3. Look for version number (e.g., 8.2.1)

### **Minimum Requirements:**
- **Version:** 8.0 or newer
- **Recommended:** 8.2.0 or newer
- **Operating System:** Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 2GB free space

---

## 📊 FEATURE COMPATIBILITY MATRIX

| Feature | PT 8.0 | PT 8.1 | PT 8.2.0+ | Workaround if Missing |
|---------|--------|--------|-----------|----------------------|
| **Cisco 2911 Router** | ✅ | ✅ | ✅ | Use 1941 or 2901 |
| **Cisco 2960 Switch** | ✅ | ✅ | ✅ | Use 2950-24 |
| **VLANs** | ✅ | ✅ | ✅ | None needed |
| **OSPF** | ✅ | ✅ | ✅ | None needed |
| **NAT (Interface-based)** | ✅ | ✅ | ✅ | None needed |
| **DHCP Server** | ✅ | ✅ | ✅ | None needed |
| **DNS Server** | ✅ | ✅ | ✅ | None needed |
| **Web/Email Servers** | ✅ | ✅ | ✅ | None needed |
| **Access Point (WiFi)** | ✅ | ✅ | ✅ | None needed |
| **Linksys WRT300N** | ✅ | ✅ | ✅ | Use AccessPoint-PT |
| **Smartphones/Tablets** | ✅ | ✅ | ✅ | None needed |
| **IoT Devices** | ❌ | ⚠️ | ✅ | **Use PC-PT** |
| **IPv6 (Basic)** | ⚠️ | ✅ | ✅ | Skip IPv6, use IPv4 only |
| **OSPFv3** | ❌ | ⚠️ | ✅ | Use OSPF for IPv4 only |
| **QoS Commands** | ⚠️ | ⚠️ | ⚠️ | Config only, no effect |
| **Port Security** | ✅ | ✅ | ✅ | None needed |
| **STP/RSTP** | ✅ | ✅ | ✅ | None needed |

**Legend:**
- ✅ **Full Support** - Works perfectly
- ⚠️ **Partial Support** - Limited functionality or workaround needed
- ❌ **Not Available** - Feature missing, use workaround

---

## 🔧 VERSION-SPECIFIC WORKAROUNDS

### **FOR PACKET TRACER 8.0/8.1 (Older Versions)**

#### **Issue 1: No IoT Devices**

**Problem:** IoT Devices category doesn't exist

**Solution:** Use **PC-PT** as IoT simulator

**How to implement:**
1. Place **PC-PT** instead of IoT device
2. Label it: `IoT-Traffic-1`
3. Configure static IP
4. Treat as IoT sensor

**Example:**
```
❌ OLD: Motion Detector (IoT-Traffic-1)
✅ NEW: PC-PT (IoT-Traffic-1)

Configuration:
- IP: 192.168.40.101 (static)
- Gateway: 192.168.40.1
- Purpose: Simulates traffic sensor
```

**Works perfectly for demonstration!**

---

#### **Issue 2: Limited IPv6 Support**

**Problem:** IPv6 commands may not work or behave oddly

**Solution:** **Skip IPv6 entirely, use IPv4 only**

**What to skip:**
```cisco
! SKIP these commands in PT 8.0/8.1:
ipv6 unicast-routing
ipv6 address 2001:db8:a:10::1/64
ipv6 router ospf 1
```

**What to keep:**
```cisco
! KEEP these (IPv4):
ip routing
ip address 192.168.10.1 255.255.255.0
router ospf 1
```

**Impact:** None - all technologies still demonstrated with IPv4

---

#### **Issue 3: Some Router Models Missing**

**Problem:** ISR4331 may not be available

**Solution:** Use **Cisco 2911** or **1941**

**Substitution Chart:**
| Recommended | Substitute 1 | Substitute 2 |
|-------------|-------------|--------------|
| 2911 | 1941 | 2901 |
| ISR4331 | 2911 | 1941 |

**Interface naming changes:**
- 2911: `GigabitEthernet0/0`
- 1941: `GigabitEthernet0/0`
- ISR4331: `GigabitEthernet0/0/0` ← Different!

**Always check:** `show ip interface brief` to see actual interface names

---

### **FOR PACKET TRACER 8.2.0+ (Current Versions)**

#### **All Features Available!** ✅

If you have PT 8.2.0 or newer, you can use:
- ✅ IoT Devices (Motion Detector, Environmental Monitor, etc.)
- ✅ Full IPv6 support
- ✅ All router/switch models
- ✅ All configuration commands

**One Note:** Even in 8.2, **Cell Tower devices do NOT exist**

**Solution:** Use **Linksys WRT300N** configured as cellular backhaul

---

## 📱 CELLULAR TOWER WORKAROUND (ALL VERSIONS)

### **The Reality:**

**Packet Tracer does NOT have functional "Cell Tower" devices with Ethernet**
- Some PT versions may show "Cell Tower" in device list
- BUT: These devices are **wireless-only** (no Ethernet port)
- Cannot be connected via cable to switches
- No dedicated cellular infrastructure with wired backhaul

### **The Solution:**

Use **Linksys WRT300N** (Wireless Router) as cellular tower simulator

### **Why Linksys WRT300N:**
- ✅ Has physical Ethernet port (**Internet/WAN port**)
- ✅ Supports wireless clients (smartphones, tablets)
- ✅ Available in all PT versions (8.0, 8.1, 8.2+)
- ✅ Can be configured as access point
- ✅ Simulates cellular backhaul connection

### **How to Configure:**

**Step 1:** Place **Linksys WRT300N**
```
Network Devices → Wireless Devices → Linksys WRT300N
```

**Step 2:** Label as `CityA-CellTower-1`

**Step 3:** Connect to Switch
```
Cable: Copper Straight-Through
From: CityA-Res-SW2 FastEthernet0/1
To: Linksys WRT300N "Internet" port (WAN port)
```

**Step 4:** Configure Network Settings

1. Click device → **Config** tab → **Internet** (Setup)
2. **Connection Type:** Static IP
3. **Internet IP Address:** 192.168.20.60
4. **Subnet Mask:** 255.255.255.0
5. **Default Gateway:** 192.168.20.1

**Step 5:** Configure Wireless

1. Click **Wireless** tab
2. **Network Mode:** Mixed
3. **Network Name (SSID):** `CityA-4G-LTE`
4. **Channel:** 11
5. **SSID Broadcast:** Enable

**Step 6:** Configure Security

1. **Security Mode:** WPA2-PSK
2. **Passphrase:** `Cellular2024`

**Step 7:** Disable DHCP Server (IMPORTANT!)

1. Config → **DHCP**
2. **DHCP Server:** Disabled
3. Why? Network router will provide DHCP, not the WRT300N

**Step 8:** Connect Mobile Devices

1. Click smartphone/tablet
2. Config → Wireless0
3. Select SSID: `CityA-4G-LTE`
4. Enter password: `Cellular2024`
5. Should receive IP from network DHCP (192.168.20.100+)

**Result:** Simulates cellular tower with wired backhaul perfectly!

---

## 🔀 DEVICE MODEL SUBSTITUTIONS

### **If Specific Model Not Available:**

#### **Routers:**
| If Missing | Use Instead | Notes |
|------------|-------------|-------|
| 2911 | 1941 | Check interface names |
| ISR4331 | 2911 | Interface names differ |
| 2901 | 1941 | Similar features |
| 1841 | 1941 | Older, but works |

**Always verify interfaces:** `show ip interface brief`

---

#### **Switches:**
| If Missing | Use Instead | Notes |
|------------|-------------|-------|
| 2960-24TT | 2950-24 | Older but functional |
| 3650-24PS | 2960-24TT | No functional loss |
| 3560-24PS | 2960-24TT | Simpler, adequate |

**Note:** All 2960 switches support VLANs, trunking, STP - perfect for this project

---

#### **Wireless:**
| If Missing | Use Instead | Notes |
|------------|-------------|-------|
| AccessPoint-PT | Linksys WRT300N | Disable DHCP server |
| WRT300N | AccessPoint-PT | Either works |
| Home Router | WRT300N | Configure as AP |

---

#### **End Devices:**
| If Missing | Use Instead | Notes |
|------------|-------------|-------|
| IoT-PT | PC-PT | Label appropriately |
| Tablet-PT | Laptop-PT | Both have wireless |
| Smartphone-PT | Tablet-PT | Both mobile devices |

---

## ⚠️ KNOWN PACKET TRACER LIMITATIONS

### **Limitation 1: QoS Has No Visible Effect**

**What Works:**
```cisco
policy-map CITYA-QOS
 class EMERGENCY
  priority percent 40
```
✅ Commands accepted
✅ Configuration saved
✅ Shows in `show policy-map`

**What Doesn't Work:**
❌ No actual packet prioritization
❌ No observable latency difference
❌ No queue management visible

**Bottom Line:** QoS is for **configuration demonstration only**

**How to explain to professor:**
"QoS policy is configured correctly per Cisco IOS standards. In production, this would prioritize emergency traffic. Packet Tracer accepts the configuration but doesn't simulate queue management."

---

### **Limitation 2: NAT Pools Can Be Unreliable**

**Problem:**
```cisco
ip nat pool CITYA-PUBLIC 203.0.113.10 203.0.113.250 netmask 255.255.255.0
ip nat inside source list 1 pool CITYA-PUBLIC overload
```
Sometimes works, sometimes doesn't show translations

**Fix:** Use **interface-based NAT** (more reliable)
```cisco
ip nat inside source list 1 interface Serial0/0/0 overload
```
✅ Works consistently in PT

---

### **Limitation 3: Serial Cable Direction Matters**

**Issue:** Must connect serial cable correct direction

**In Packet Tracer:**
1. Click cable
2. Look for **DCE** vs **DTE** markers
3. DCE side goes to ISP
4. DTE side goes to City

**If backwards:** Link won't come up, even with correct config

**Fix:** Delete cable, reconnect correctly

---

### **Limitation 4: Some Show Commands Limited**

**Commands that may not work fully:**
```cisco
show ip nat statistics  # May show zeros
show policy-map interface GigabitEthernet0/0  # May show no stats
show processes cpu  # Always shows 0%
```

**What to use instead:**
```cisco
show ip nat translations  # Works
show policy-map  # Works
show ip interface brief  # Works
show ip route  # Works
show vlan brief  # Works
```

---

## 🐛 TROUBLESHOOTING BY VERSION

### **PT 8.0 Specific Issues:**

**Issue:** IPv6 commands cause errors

**Fix:** Remove all IPv6 configurations
```cisco
! Remove:
ipv6 unicast-routing
ipv6 address ...
ipv6 route ...

! Keep IPv4 only
```

---

**Issue:** OSPF neighbors not forming

**Fix:** Check wildcard masks (not subnet masks!)
```cisco
! WRONG:
network 192.168.10.0 255.255.255.0 area 10

! RIGHT:
network 192.168.10.0 0.0.0.255 area 10
```

---

### **PT 8.1 Specific Issues:**

**Issue:** Trunk encapsulation command fails

**Fix:** Skip the encapsulation line
```cisco
! SKIP this line on 2960:
switchport trunk encapsulation dot1q

! Keep these:
switchport mode trunk
switchport trunk allowed vlan 10,20,30
```

---

### **PT 8.2 Specific Issues:**

**Issue:** Too many devices causes lag

**Fix:** Use **Option B: Medium** (60 devices) or **Option C: Minimal** (30 devices)

See `00_SCALING_OPTIONS.md`

---

## ✅ PRE-FLIGHT CHECKLIST

**Before starting your project:**

- [ ] Check PT version (`Help → About`)
- [ ] Verify RAM (4GB minimum, 8GB recommended)
- [ ] Read `00_SCALING_OPTIONS.md` (choose size)
- [ ] If PT 8.0/8.1: Plan to use PC-PT for IoT
- [ ] If PT 8.0/8.1: Plan to skip IPv6
- [ ] Test one router + one switch before building full network
- [ ] Save frequently (every 15-30 minutes)
- [ ] Create backups (`File → Save As` with different names)

---

## 🆘 COMPATIBILITY PROBLEMS?

### **Problem: Device Not Available**

**Solution:** Check substitution tables above

---

### **Problem: Command Not Recognized**

**Solution:**
1. Check spelling/syntax
2. Check interface name (`show ip interface brief`)
3. If IPv6 command → skip if PT 8.0/8.1
4. Try simpler version of command

---

### **Problem: PT Runs Slowly**

**Solution:**
1. Close other applications
2. Use Option B (Medium) or Option C (Minimal)
3. Don't run simulation mode continuously
4. Save and restart PT periodically

---

### **Problem: Links Won't Come Up**

**Solution:**
1. Check both ends show "up/up" eventually (wait 30s)
2. Verify `no shutdown` on both sides
3. Check cable type (use straight-through for most connections)
4. For serial: Verify clock rate on DCE side only

---

## 📋 VERSION RECOMMENDATION

### **Best Version for This Project:**

**Packet Tracer 8.2.1** or newer

**Why:**
- ✅ All features available
- ✅ IoT devices included
- ✅ Full IPv6 support
- ✅ Most stable
- ✅ Best documentation

**If you have older:**
- PT 8.0/8.1: Still works fine with workarounds
- PT 7.x: May have issues, upgrade recommended

**Where to get latest:**
- Cisco NetAcad account
- netacad.com (requires instructor enrollment)
- Free with NetAcad course registration

---

## 💾 SAVE FILE COMPATIBILITY

**Packet Tracer files (.pkt) are backwards/forwards compatible**

✅ File created in PT 8.0 opens in PT 8.2
✅ File created in PT 8.2 opens in PT 8.1 (may lose some features)

**Best practice:**
- Create in version you have
- If sharing, note PT version used
- Test on target version before submission

---

## 🎓 PROFESSOR EXPECTATIONS

**What professors typically have:**
- Usually PT 8.2.x (latest)
- Sometimes PT 8.1 (one version behind)
- Rarely PT 8.0 (older)

**Safe bet:**
- Build in PT 8.1+ features (VLANs, OSPF, NAT, DHCP, DNS)
- Avoid PT 8.2-only features if professor has 8.1
- Always include `.pkt` file + compatibility note

**Compatibility Note Example:**
```
Built with: Packet Tracer 8.2.1
Compatible with: PT 8.0+ (uses PC-PT for IoT in older versions)
Features used: OSPF, NAT, VLANs, DHCP, DNS, ACLs, Wireless
Special notes: IPv6 is optional (can be removed for PT 8.0)
```

---

## ✅ SUMMARY

### **Key Takeaways:**

1. **PT 8.0+** = Project works with workarounds
2. **PT 8.2+** = All features available
3. **No Cell Towers** = Use Linksys WRT300N in all versions
4. **No IoT in PT 8.0/8.1** = Use PC-PT substitute
5. **QoS** = Configuration only, no visible effect
6. **NAT** = Use interface-based, not pool
7. **Scaling** = Adjust project size to hardware

### **You're Good to Go If:**
- ✅ You have PT 8.0 or newer
- ✅ You read this guide
- ✅ You chose appropriate scaling option
- ✅ You know your workarounds

**This project WILL work on your version!** 🚀

---

**Next:** Proceed to `PART1_PHYSICAL_SETUP/01_DEVICE_LIST.md`
