# ⚡ CRITICAL PATH - 15 MINUTES TO WORKING NETWORK
## Use with connection_COMPLETED.pkt

**Time: 15 minutes | Steps: 6 critical tasks**

---

## ✅ WHAT'S ALREADY WORKING (95%)

- ✅ Router: Full config (NAT, routing, IPv6)
- ✅ Core Switch: VLANs, trunks, ACLs
- ✅ All 3 district switches: Configured
- ✅ All connections: Ready

---

## ⚡ CRITICAL STEPS (DO THESE ONLY)

### STEP 1: Server IPs (3 minutes) ⭐ CRITICAL

**DNS-Server:**
1. Click DNS-Server → **Config** → FastEthernet0
2. **IP Address:** `10.10.10.10`
3. **Subnet Mask:** `255.255.255.0`
4. Go to Settings → **Gateway:** `10.10.10.1`

**DHCP-Server:**
1. Click DHCP-Server → **Config** → FastEthernet0
2. **IP:** `10.10.10.20`, **Mask:** `255.255.255.0`
3. **Gateway:** `10.10.10.1`

**Web-Server:**
1. Click Web-Server → **Config** → FastEthernet0
2. **IP:** `10.10.10.30`, **Mask:** `255.255.255.0`
3. **Gateway:** `10.10.10.1`

**SMTP-Server:**
1. Click SMTP-Server → **Config** → FastEthernet0
2. **IP:** `10.10.10.40`, **Mask:** `255.255.255.0`
3. **Gateway:** `10.10.10.1`

---

### STEP 2: DHCP Pools (4 minutes) ⭐ CRITICAL

1. Click **DHCP-Server** → Services → **DHCP**
2. **Service:** ON

**Pool 1:**
- Name: `AdminPool`
- Default Gateway: `10.10.10.1`
- DNS Server: `10.10.10.10`
- Start IP: `10.10.10.100`
- Subnet Mask: `255.255.255.0`
- Max Users: `50`
- Click **Save**

**Pool 2:**
- Name: `PublicPool`
- Gateway: `10.10.20.1`
- DNS: `10.10.10.10`
- Start IP: `10.10.20.100`
- Mask: `255.255.255.0`
- Max Users: `100`
- **Save**

**Pool 3:**
- Name: `IoTPool`
- Gateway: `10.10.30.1`
- DNS: `10.10.10.10`
- Start IP: `10.10.30.100`
- Mask: `255.255.255.0`
- Max Users: `50`
- **Save**

---

### STEP 3: Enable DHCP on PCs (2 minutes)

**Admin-PC-1:**
1. Click → Desktop → IP Configuration
2. Select **DHCP** radio button
3. Wait for IP (should get 10.10.10.100-150)

**Repeat for:**
- Admin-PC-2 (DHCP)
- Public-Kiosk-PC (DHCP → gets 10.10.20.x)
- Resident-Home-PC (DHCP → gets 10.10.30.x)

---

### STEP 4: DNS Records (3 minutes) ⭐ CRITICAL

1. Click **DNS-Server** → Services → **DNS**
2. **Service:** ON
3. Add these 3 MINIMUM records:

| Name | IP |
|------|-----|
| `smartcity.local` | `10.10.10.30` |
| `dns.smartcity.local` | `10.10.10.10` |
| `mail.smartcity.local` | `10.10.10.40` |

*(Add others if you have time, but these 3 are critical)*

---

### STEP 5: Central Office Server IP (1 minute)

1. Click **Central Office Server** (or Central-Office-Server)
2. Desktop → IP Configuration
3. **Static:**
   - IP: `10.10.20.50`
   - Mask: `255.255.255.0`
   - Gateway: `10.10.20.1`
   - DNS: `10.10.10.10`

---

### STEP 6: Park IoT Gateway (2 minutes)

1. Click **Park-IoT-Gateway**
2. Config → FastEthernet0
3. **IP:** `10.10.30.10`
4. **Mask:** `255.255.255.0`
5. Settings → **Gateway:** `10.10.30.1`

---

## 🧪 QUICK TESTS (2 minutes)

### Test 1: Ping Gateway
From Admin-PC-1 → Desktop → Command Prompt:
```
ping 10.10.10.1
```
✅ Should get replies

### Test 2: Ping DNS
```
ping 10.10.10.10
```
✅ Should get replies

### Test 3: DNS Works
```
nslookup smartcity.local
```
✅ Should return 10.10.10.30

### Test 4: ACL Works
From Public-Kiosk-PC:
```
ping 10.10.10.10
```
✅ Should FAIL (timeout) - This proves ACL is working!

---

## ✅ OPTIONAL (If You Have Time)

### WiFi APs (3 minutes each):
**Public-WiFi-AP:**
- Config → Wireless
- SSID: `City-Public-WiFi`
- WPA2-PSK: `publicaccess`

**Residential-WiFi-AP:**
- Config → Wireless
- SSID: `Residential-Network`
- WPA2-PSK: `homeaccess`

### SMTP Users (1 minute):
- SMTP-Server → Services → EMAIL
- Domain: `smartcity.local`
- Add user: `admin` / `cisco`
- Add user: `iot` / `cisco`

### IoT Blockly (5 minutes):
- Park-IoT-Gateway → Programming → Blockly
- When Motion D0 → Set 10.10.30.20 brightness 1023 → Wait 60s → Set brightness 0 → Send Email

---

## 💯 SUCCESS CRITERIA

**Your network is working when:**

1. ✅ Admin-PC-1 has IP 10.10.10.x (DHCP working)
2. ✅ Can ping 10.10.10.1 (routing working)
3. ✅ Can ping 10.10.10.10 (DNS server reachable)
4. ✅ `nslookup smartcity.local` returns 10.10.10.30 (DNS working)
5. ✅ Public-Kiosk-PC CANNOT ping 10.10.10.10 (ACL working)

**If all 5 tests pass = YOUR NETWORK IS 100% FUNCTIONAL** ✅

---

## 🚨 TROUBLESHOOTING

**Problem:** PCs not getting DHCP
- **Fix:** Check DHCP pools saved on DHCP-Server
- Re-select DHCP on PC (Static → DHCP)

**Problem:** Can't ping gateway
- **Fix:** Check router CLI: `show ip interface brief`
- Check cables are green

**Problem:** DNS not resolving
- **Fix:** Check DNS records added on DNS-Server
- Check DNS service is ON

---

## ⏱️ TIME BREAKDOWN

| Step | Time | Critical? |
|------|------|-----------|
| Server IPs | 3 min | ⭐ YES |
| DHCP Pools | 4 min | ⭐ YES |
| PC DHCP | 2 min | ⭐ YES |
| DNS Records | 3 min | ⭐ YES |
| Central Office | 1 min | ⭐ YES |
| IoT Gateway | 2 min | ⭐ YES |
| **TOTAL CRITICAL** | **15 min** | |
| WiFi (optional) | +6 min | Optional |
| SMTP (optional) | +1 min | Optional |
| IoT Code (optional) | +5 min | Optional |

---

**FOCUS ON THE 6 CRITICAL STEPS = 15 MINUTES = WORKING NETWORK** ⚡

**Good luck! You got this!** 🚀
