# PART 2: CONFIGURATION
## 05 - WIRELESS SETUP (WiFi APs + Cellular Simulation)

**Configure all 8 wireless devices and connect mobile clients**

---

## ⚠️ IMPORTANT COMPATIBILITY NOTE

### **Cellular Tower Simulation:**
- ⚠️ Packet Tracer has **NO "Cell Tower" device** in any version (8.0, 8.1, 8.2+)
- ✅ Use **Linksys WRT300N** (wireless router) instead
- Configure as access point with SSID like `CityA-4G-LTE`
- **Works perfectly** for demonstrating cellular connectivity
- See `../COMPATIBILITY_GUIDE.md` for detailed setup

### **WiFi Access Points:**
- Use **AccessPoint-PT** (preferred) or **Linksys WRT300N**
- Both work identically in Packet Tracer
- Available in all PT versions

---

## 📋 WIRELESS DEVICE OVERVIEW

| City | Device | Type (Actual) | SSID | VLAN | IP Address |
|------|--------|---------------|------|------|------------|
| A | WiFi-Gov-AP1 | AccessPoint-PT | CityA-Gov-WiFi | 10 | 192.168.10.50 |
| A | WiFi-Res-AP1 | AccessPoint-PT | CityA-Residential | 20 | 192.168.20.50 |
| A | WiFi-Pub-AP1 | AccessPoint-PT | CityA-Public | 50 | 192.168.50.50 |
| A | CellTower-1 | **Linksys WRT300N** | CityA-4G-LTE | 20 | 192.168.20.60 |
| B | WiFi-Gov-AP1 | AccessPoint-PT | CityB-Gov-WiFi | 10 | 192.168.10.50 |
| B | WiFi-Res-AP1 | AccessPoint-PT | CityB-Residential | 20 | 192.168.20.50 |
| B | WiFi-Pub-AP1 | AccessPoint-PT | CityB-Public | 50 | 192.168.50.50 |
| B | CellTower-1 | **Linksys WRT300N** | CityB-4G-LTE | 20 | 192.168.20.60 |

---

## 🏙️ CITY A - WIRELESS CONFIGURATIONS

---

## 📶 **WIRELESS 1: CityA-WiFi-Gov-AP1** (Government WiFi)

### **Step 1: Configure Management IP**

1. Click **CityA-WiFi-Gov-AP1** device
2. Click **Config** tab
3. Click **Port 1** (or **Interface** section)

**Configure Static IP:**

| Field | Value |
|-------|-------|
| IP Configuration | Static |
| IP Address | 192.168.10.50 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.10.1 |
| DNS Server | 192.168.99.10 |

---

### **Step 2: Configure Wireless Settings**

1. In Config tab, click **Wireless** section
2. OR click **Port 1** → **Wireless** sub-section

**Configure:**

| Field | Value |
|-------|-------|
| SSID | `CityA-Gov-WiFi` |
| Authentication | **WPA2-PSK** |
| PSK Pass Phrase | `GovSecure2024` |
| Encryption Type | **AES** |
| Channel | **6** |
| SSID Broadcast | **Enabled** |

---

### **Step 3: Advanced Settings (Optional)**

| Field | Value |
|-------|-------|
| Max Number of Users | 25 |
| Radio Status | Enabled |

---

### **Step 4: Verification**

1. Wireless indicator should be **green**
2. SSID should appear in nearby wireless device scans

✅ **CityA-WiFi-Gov-AP1 Complete**

---

## 📶 **WIRELESS 2: CityA-WiFi-Res-AP1** (Residential WiFi)

### **Quick Configuration:**

**Management IP:**
- IP Address: `192.168.20.50`
- Subnet Mask: `255.255.255.0`
- Gateway: `192.168.20.1`
- DNS: `192.168.99.10`

**Wireless:**
- SSID: `CityA-Residential`
- Authentication: **WPA2-PSK**
- Password: `ResidentSecure2024`
- Encryption: **AES**
- Channel: **11**
- Broadcast: **Enabled**

✅ **CityA-WiFi-Res-AP1 Complete**

---

## 📶 **WIRELESS 3: CityA-WiFi-Pub-AP1** (Public WiFi)

### **Quick Configuration:**

**Management IP:**
- IP Address: `192.168.50.50`
- Subnet Mask: `255.255.255.0`
- Gateway: `192.168.50.1`
- DNS: `192.168.99.10`

**Wireless:**
- SSID: `CityA-Public`
- Authentication: **Open** (no password for public)
  - OR use **WPA2-PSK** with password: `PublicWiFi2024`
- Channel: **1**
- Broadcast: **Enabled**

✅ **CityA-WiFi-Pub-AP1 Complete**

---

## 📱 **WIRELESS 4: CityA-CellTower-1** (Cellular Simulation)

**⚠️ IMPORTANT: Packet Tracer has NO dedicated "Cell Tower" device!**
- Use **Linksys WRT300N** (wireless router) instead
- Configure as access point to simulate cellular backhaul
- Label as `CityA-CellTower-1` for clarity

---

### **Step 1: Configure Wired Interface (Internet Port)**

1. Click **CityA-CellTower-1** (Linksys WRT300N) device
2. Click **Config** tab
3. Click **Interface** → **Internet**

**Configure:**

| Field | Value |
|-------|-------|
| IP Configuration | Static IP |
| IP Address | 192.168.20.60 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.20.1 |

---

### **Step 2: Configure Wireless Settings**

1. Still in **Config** tab
2. Click **Wireless** section

**Configure:**

| Field | Value |
|-------|-------|
| Network Name (SSID) | `CityA-4G-LTE` |
| Network Mode | **Wireless-N Only** |
| Radio Band | **2.4 GHz** |
| Standard Channel | **11** (avoid conflicts with other APs) |
| SSID Broadcast | **Enabled** |

---

### **Step 3: Configure Wireless Security**

1. Still in **Wireless** section
2. Scroll to **Security** settings

**Configure:**

| Field | Value |
|-------|-------|
| Security Mode | **WPA2-PSK** |
| Encryption | **AES** |
| Passphrase | `Cellular2024` |

---

### **Step 4: DISABLE Built-in DHCP Server**

**⚠️ CRITICAL STEP - Do not skip!**

1. Click **Config** → **LAN** or **DHCP**
2. **Uncheck** "DHCP Server Enabled" or set to **Disabled**

**Why?** Router DHCP (via `ip helper-address`) should provide IPs, not the WRT300N

---

### **Step 5: Save & Verify**

1. Settings auto-save in PT
2. Verify:
   - SSID broadcasts as `CityA-4G-LTE`
   - Wired connection to switch
   - DHCP disabled

✅ **CityA-CellTower-1 (Cellular Simulation) Complete**

**Result:** Smartphones can connect to "CityA-4G-LTE" as if connecting to a cellular network

---

## 📱 CONNECTING MOBILE DEVICES (City A)

---

### **Device 1: CityA-Home-Smartphone-1** (to Residential WiFi)

**Step 1:** Click **CityA-Home-Smartphone-1**

**Step 2:** Click **Desktop** tab → **PC Wireless**

**Step 3:** Click **Connect** tab

**Step 4:** Scan for networks (list should show available SSIDs)

**Step 5:** Select **CityA-Residential**

**Step 6:** Click **Connect**

**Step 7:** Enter password: `ResidentSecure2024`

**Step 8:** Click **OK**

**Expected Result:**
- Connection Status: **Connected**
- Signal Strength: Green bars
- IP Address assigned via DHCP

**Step 9:** Verify connection
1. Click **Desktop** → **IP Configuration**
2. Should show:
   - IP: 192.168.20.xxx (DHCP-assigned)
   - Gateway: 192.168.20.1
   - DNS: 192.168.99.10

✅ **Smartphone connected to WiFi**

---

### **Device 2: CityA-Public-Phone-1** (to Public WiFi)

**Quick Steps:**
1. Click device → **Desktop** → **PC Wireless**
2. Click **Connect** tab
3. Select **CityA-Public**
4. Click **Connect**
5. If password: Enter `PublicWiFi2024`
6. Verify IP: 192.168.50.xxx

✅ **Public phone connected**

---

### **Device 3: CityA-Public-Tablet-1** (to Public WiFi)

**Repeat same steps as Public-Phone-1**

✅ **Public tablet connected**

---

### **Device 4: Connect to Cellular Network (Optional)**

**For devices with wireless capability:**

1. Click device → **Desktop** → **PC Wireless**
2. Select **Connect** tab
3. Scan for networks
4. Select **CityA-4G-LTE**
5. Enter password: `Cellular2024`
6. Connect

**Note:** In PT, "cellular" is WiFi-based. Smartphones connect to the Linksys WRT300N SSID (`CityA-4G-LTE`)

✅ **Mobile devices connected**

---

## 🏙️ CITY B - WIRELESS CONFIGURATIONS

**EXACT COPY of City A** with these changes:

### **SSIDs:**
- `CityA-Gov-WiFi` → `CityB-Gov-WiFi`
- `CityA-Residential` → `CityB-Residential`
- `CityA-Public` → `CityB-Public`
- `CityA-4G-LTE` → `CityB-4G-LTE`

### **IPs:**
- Same (192.168.x.x) - NAT isolates cities

### **Passwords:**
- Keep same or change (e.g., `CityBGov2024`)

---

## ✅ WIRELESS CONFIGURATION CHECKLIST

**City A:**
- [ ] CityA-WiFi-Gov-AP1 (SSID, WPA2-PSK)
- [ ] CityA-WiFi-Res-AP1 (SSID, WPA2-PSK)
- [ ] CityA-WiFi-Pub-AP1 (SSID, Open/WPA2)
- [ ] CityA-CellTower-1 (4G network)
- [ ] CityA-Home-Smartphone-1 (connected)
- [ ] CityA-Public-Phone-1 (connected)
- [ ] CityA-Public-Tablet-1 (connected)

**City B:**
- [ ] 4 wireless APs/towers (mirror City A)
- [ ] 3 wireless clients (connected)

**Total: 8 APs/towers, 6+ wireless clients** ✅

---

## 🔍 VERIFICATION TESTS

### **Test 1: SSID Visibility**
From any wireless device:
1. Desktop → PC Wireless → Connect tab
2. Scan
3. Should see all City A SSIDs

Expected:
- `CityA-Gov-WiFi`
- `CityA-Residential`
- `CityA-Public`

---

### **Test 2: WiFi Connection**
1. Connect smartphone to `CityA-Residential`
2. Check IP: `ipconfig`
3. Expected: IP in 192.168.20.100-220 range

---

### **Test 3: Internet Access from WiFi**
From connected smartphone:
1. Desktop → Web Browser
2. Navigate to `http://www.city-a.local`
3. Should load city website

---

### **Test 4: Roaming (Optional)**
1. Connect device to `CityA-Residential`
2. Disconnect
3. Connect to `CityA-Public`
4. Should get new IP in VLAN 50 range

---

### **Test 5: Public WiFi Isolation**
From public WiFi device:
1. Try to ping government device: `ping 192.168.10.101`
2. Expected: **Request timed out** (ACL blocks)
3. Try to access internet: `ping 8.8.8.8`
4. Expected: **Success** (ACL allows internet)

---

## 📊 WIRELESS NETWORK SUMMARY

### **WiFi Coverage Map:**

```
City A Wireless Coverage:

┌─────────────────────────────────────────┐
│  Government Zone                        │
│  🔒 [CityA-Gov-WiFi]                    │
│  ├─ WPA2-PSK encrypted                  │
│  └─ VLAN 10                             │
├─────────────────────────────────────────┤
│  Residential Zone                       │
│  🏠 [CityA-Residential]                 │
│  ├─ WPA2-PSK encrypted                  │
│  └─ VLAN 20                             │
│                                         │
│  📡 [CityA-4G-LTE]                      │
│  ├─ Linksys WRT300N (cellular sim)     │
│  └─ VLAN 20                             │
├─────────────────────────────────────────┤
│  Commercial Zone                        │
│  🌐 [CityA-Public]                      │
│  ├─ Open or WPA2-PSK                    │
│  ├─ VLAN 50                             │
│  └─ ACL restricted (internet only)      │
└─────────────────────────────────────────┘
```

---

## 🔐 WIRELESS SECURITY SUMMARY

| SSID | Encryption | Password | VLAN | Access |
|------|------------|----------|------|--------|
| CityA-Gov-WiFi | WPA2-PSK | GovSecure2024 | 10 | Full network |
| CityA-Residential | WPA2-PSK | ResidentSecure2024 | 20 | Full network |
| CityA-Public | Open/WPA2 | PublicWiFi2024 | 50 | Internet only |
| CityA-4G-LTE | WPA2-PSK | Cellular2024 | 20 | Full network |

---

## 💡 WIRELESS BEST PRACTICES

### **Channel Selection:**
- Channel 1, 6, 11 (non-overlapping)
- Gov: Channel 6 (center)
- Res: Channel 11 (high)
- Public: Channel 1 (low)

### **Security:**
- Government/Residential: **WPA2-PSK with strong passwords**
- Public: **Open** (or weak WPA2 for demo)
- Emergency: Separate encrypted network (future)

### **Coverage:**
- Cellular simulation (Linksys WRT300N): Maximum radius (covers residential zone)
- WiFi APs: Medium radius (zone-specific coverage)

---

## ⏱️ ESTIMATED TIME

- WiFi APs (6 total): 30 minutes
- Cellular simulation (2 Linksys WRT300N): 20 minutes
- Connecting mobile clients: 15 minutes
- **Total: ~1 hour 5 minutes**

**Note:** Configuration times assume familiarity with PT interface

---

## 📝 NEXT STEP

✅ **All wireless devices configured**

➡️ **Next:** `PART3_VERIFICATION/01_VERIFICATION_COMMANDS.md` for final testing!

**Wireless configuration complete!** 🚀
