# IoT DEVICE CONNECTIVITY GUIDE
## Packet Tracer 8.2+ - Wired vs Wireless IoT Devices

**CRITICAL:** Not all IoT devices have Ethernet ports! Some are wireless-only.

---

## 🔌 CONNECTIVITY MATRIX

### IoT Devices with ETHERNET Ports (Can be wired):

| Device Category | Device Name in PT | Has Ethernet? | Notes |
|----------------|-------------------|---------------|-------|
| **SBC (Single Board Computer)** | SBC-PT | ✅ YES | Has FastEthernet0 - USE THIS! |
| **Home Gateway** | Home Gateway | ✅ YES | Has Ethernet0 |
| **MCU (Microcontroller)** | MCU-PT | ✅ YES | Has FastEthernet0 |
| **Old Tablet** | Old Tablet | ✅ YES | Has FastEthernet0 |

### IoT Devices with WIRELESS-ONLY (No Ethernet):

| Device Category | Device Name in PT | Has Ethernet? | Connectivity |
|----------------|-------------------|---------------|-------------|
| **Webcam** | Webcam | ❌ NO | Bluetooth/WiFi only |
| **Motion Detector** | Motion Detector | ❌ NO | Bluetooth/WiFi only |
| **Siren** | Siren | ❌ NO | Bluetooth/WiFi only |
| **Fan** | Fan | ❌ NO | Bluetooth/WiFi only |
| **Smoke Detector** | Smoke Detector | ❌ NO | Bluetooth/WiFi only |
| **Solar Panel** | Solar Panel | ❌ NO | Bluetooth/WiFi only |
| **Lawn Sprinkler** | Lawn Sprinkler | ❌ NO | Bluetooth/WiFi only |
| **GPS** | GPS | ❌ NO | Wireless only |
| **Cell Tower** | Cell Tower | ❌ NO | Wireless only (if exists) |

### Wireless Access Devices with ETHERNET (Can be wired):

| Device Category | Device Name in PT | Has Ethernet? | Wired Port | Notes |
|----------------|-------------------|---------------|------------|-------|
| **Linksys WRT300N** | Linksys WRT300N | ✅ YES | **Internet** port | Use for Cell Tower! |
| **AccessPoint-PT** | AccessPoint-PT | ✅ YES | Ethernet1 | Use for WiFi APs |

### Hybrid Devices (Check Configuration Tab):

| Device Category | Device Name in PT | Notes |
|----------------|-------------------|-------|
| **Environmental Monitor** | Environmental Monitor | Check model - some have Ethernet, some don't |
| **Smart Home Device** | Various smart devices | Depends on specific device |

---

## ✅ RECOMMENDED IoT DEVICES FOR WIRED CONNECTIONS

### For Smart City Project - Use These:

#### 1. **SBC-PT (Single Board Computer)** - BEST CHOICE
- **Has:** FastEthernet0 port
- **Use for:** Traffic sensors, smart grid, environmental monitoring, any general IoT
- **Location:** End Devices → IoT Devices → SBC

#### 2. **MCU-PT (Microcontroller)**
- **Has:** FastEthernet0 port
- **Use for:** Simple sensors, controllers, data collection
- **Location:** End Devices → IoT Devices → MCU

#### 3. **Home Gateway**
- **Has:** Ethernet0 port
- **Use for:** Smart home hubs, data aggregation
- **Location:** End Devices → IoT Devices → Home Gateway

#### 4. **Old Tablet**
- **Has:** FastEthernet0 + WiFi
- **Use for:** Mobile monitoring stations, kiosks
- **Location:** End Devices → End Devices → Old Tablet

---

## 🔄 CORRECTED DEVICE ASSIGNMENTS

### Cellular Tower (VLAN 20 - Residential):

| Old (Incorrect) | New (Correct) | Connection |
|----------------|---------------|------------|
| ❌ Cell Tower (wireless-only) | ✅ **Linksys WRT300N** (Cell Tower Sim) | **Internet** port to switch |

**Configuration:**
- Connect Internet (WAN) port to switch
- Static IP: 192.168.20.60
- SSID: `CityA-4G-LTE`
- Disable DHCP server
- Mobile devices connect wirelessly

### Government Zone (VLAN 60 - Emergency):

| Old (Incorrect) | New (Correct) | Connection |
|----------------|---------------|------------|
| ❌ Webcam (wireless-only) | ✅ **SBC-PT** (Security Camera) | Wired to Gov-SW1 |
| ❌ Webcam (wireless-only) | ✅ **SBC-PT** (Security Camera) | Wired to Gov-SW1 |
| ❌ Motion Detector (wireless-only) | ✅ **SBC-PT** (Fire Sensor) | Wired to Gov-SW1 |

### Transportation Zone (VLAN 40):

| Old (Incorrect) | New (Correct) | Connection |
|----------------|---------------|------------|
| Smart Home Device | ✅ **SBC-PT** (Traffic Light Controller) | Wired to Trans-SW1 |
| Smart Home Device | ✅ **SBC-PT** (Traffic Light Controller) | Wired to Trans-SW1 |
| ❌ Motion Detector (wireless-only) | ✅ **SBC-PT** (Parking Sensor) | Wired to Trans-SW1 |
| ❌ Motion Detector (wireless-only) | ✅ **SBC-PT** (Parking Sensor) | Wired to Trans-SW1 |
| ❌ GPS (wireless-only) | ✅ **SBC-PT** (Bus Tracker) | Wired to Trans-SW1 |

### Utilities Zone (VLAN 70):

| Old (Incorrect) | New (Correct) | Connection |
|----------------|---------------|------------|
| Environmental Monitor | ✅ **SBC-PT** (Smart Grid Sensor) | Wired to Util-SW1 |
| Environmental Monitor | ✅ **SBC-PT** (Smart Grid Sensor) | Wired to Util-SW1 |
| Humidity Sensor | ✅ **SBC-PT** (Water Monitor) | Wired to Util-SW1 |
| Humidity Sensor | ✅ **SBC-PT** (Water Monitor) | Wired to Util-SW1 |

### Residential Zone (VLAN 20):

| Old (Incorrect) | New (Correct) | Connection |
|----------------|---------------|------------|
| Smart Home Device | ✅ **Home Gateway** (Smart Home Hub) | Wired to Res-SW1 |
| Smart Home Device | ✅ **Home Gateway** (Smart Home Hub) | Wired to Res-SW1 |
| Environmental Monitor | ✅ **SBC-PT** (Air Quality Sensor) | Wired to Res-SW1 |

---

## 📝 HOW TO USE SBC-PT FOR ANY IoT DEVICE

### Step 1: Add SBC-PT to Workspace
```
1. Click "End Devices" in bottom toolbar
2. Navigate to "IoT Devices" section
3. Select "SBC" (Single Board Computer)
4. Place on workspace
```

### Step 2: Label Appropriately
```
Example labels:
- "CityA-TrafficLight-1"
- "CityA-Gov-Camera-1"
- "CityA-SmartGrid-1"
- "CityA-ParkingSensor-1"

Just because it's an SBC doesn't mean you can't label it as a camera or sensor!
```

### Step 3: Connect via Ethernet
```
1. Select "Connections" from bottom toolbar
2. Choose "Copper Straight-Through" cable
3. Click SBC → Select "FastEthernet0"
4. Click Switch → Select appropriate port
5. Cable turns green when connected
```

### Step 4: Configure Network (Two Options)

#### Option A: DHCP (Recommended)
```
1. Click SBC device
2. Go to "Config" tab
3. Click "FastEthernet0"
4. Select "DHCP"
5. Wait for IP assignment
```

#### Option B: Static IP
```
1. Click SBC device
2. Go to "Config" tab
3. Click "FastEthernet0"
4. Select "Static"
5. Enter:
   - IPv4 Address: 192.168.X.10X (based on VLAN)
   - Subnet Mask: 255.255.255.0
   - Default Gateway: 192.168.X.1
```

---

## 🔧 ALTERNATIVE: Use PC-PT for All IoT

If you want to avoid IoT device complexity entirely:

### Simple Approach:
1. **Use PC-PT for ALL IoT devices**
2. **Label each PC with IoT name** (e.g., "IoT-Camera-1")
3. **Connect via Ethernet** (PC-PT has FastEthernet0)
4. **Configure DHCP or Static IP**

**Advantages:**
- ✅ Always has Ethernet port
- ✅ Easy to configure
- ✅ Works in all PT versions (8.0+)
- ✅ Demonstrates same networking concepts

**What professor sees:**
- Properly labeled devices ("Camera-1", "Traffic-Sensor-1")
- Correct VLAN assignments
- Working DHCP/Static IPs
- Full network connectivity

**They won't care that it's PC-PT vs SBC-PT!**

---

## 🎯 WIRELESS IoT DEVICE SETUP (Alternative)

If you WANT to use wireless IoT devices (Webcam, Motion Detector, etc.):

### Requirements:
1. **Access Point with Bluetooth** (Home Gateway configured as AP)
2. **IoT Registration** on the gateway
3. **Network configuration** on gateway (not on IoT device directly)

### Configuration Steps:

#### 1. Setup Home Gateway as IoT Hub
```
1. Place Home Gateway near IoT devices
2. Connect Home Gateway to switch via Ethernet
3. Configure Home Gateway:
   - IP: Static (192.168.X.50)
   - Enable IoT registration
```

#### 2. Register Wireless IoT Devices
```
1. Click Home Gateway
2. Go to "Config" tab
3. Click "IoT Server"
4. Enable registration
5. Click wireless IoT device
6. Go to "Config" tab
7. Select Home Gateway from list
8. Register device
```

#### 3. Network Traffic Flow
```
Wireless IoT Device (Webcam)
    ↓ [Bluetooth/WiFi]
Home Gateway (IoT Hub)
    ↓ [Ethernet]
Switch (VLAN X)
    ↓
Router (Gateway)
```

### Limitations:
- ❌ More complex setup
- ❌ Difficult to troubleshoot
- ❌ Requires Home Gateway for each wireless cluster
- ❌ May not show up in routing tables clearly

**Recommendation:** Stick with wired devices (SBC-PT or PC-PT)

---

## 📊 FINAL DEVICE COUNT SUMMARY

### Updated IoT Device List (All Wired):

**City A:**
- **Government Zone:** 3× SBC-PT (cameras + fire sensor)
- **Transportation Zone:** 5× SBC-PT (traffic lights, parking, bus tracker)
- **Utilities Zone:** 4× SBC-PT (smart grid, water monitors)
- **Residential Zone:** 2× Home Gateway (smart home hubs) + 1× SBC-PT (air quality)

**Total per city:** 15 IoT devices (all with Ethernet connectivity)

---

## ✅ QUICK REFERENCE CHECKLIST

Before connecting IoT device to switch:

- [ ] Device has physical Ethernet port icon in PT
- [ ] Port is labeled (FastEthernet0, Ethernet0, etc.)
- [ ] NOT a Bluetooth/WiFi-only icon
- [ ] Can select port when using connection cable

**If any checkbox fails:** Use SBC-PT or PC-PT instead!

---

## 🆘 TROUBLESHOOTING

### Problem: "I can't connect cable to my IoT device"

**Solution:** Device is wireless-only. Replace with:
- SBC-PT (recommended)
- MCU-PT
- PC-PT (easiest)

### Problem: "IoT device shows red X on cable"

**Solution:**
- Check if port is selected correctly (FastEthernet0)
- Verify switch port is correct
- Try different cable type
- Check interface is not shutdown

### Problem: "Can't find SBC-PT in device list"

**Solution:**
- Go to End Devices → IoT Devices
- Look for "SBC" or "Single Board Computer"
- If not available (older PT), use PC-PT instead

---

## 📖 SUMMARY

### For Your Smart City Project:

1. ✅ **Use SBC-PT for all IoT devices** - Has Ethernet, professional, works great
2. ✅ **Alternative: Use PC-PT** - Simplest, always works, Ethernet included
3. ❌ **Avoid: Webcam, Motion Detector, GPS** - Wireless-only, complex setup
4. ✅ **Label clearly** - Name tells purpose, not hardware model
5. ✅ **Connect via Ethernet** - Direct to switch, DHCP or Static IP

**Your professor evaluates networking concepts, not IoT hardware realism!**

---

**Ready to rebuild your IoT device list with correct connectivity!** 🚀
