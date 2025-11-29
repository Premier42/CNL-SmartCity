# 🔧 DHCP TROUBLESHOOTING GUIDE

## Problem: DHCP Failed - APIPA Being Used

**Symptom:** Admin-PC-1 shows 169.254.x.x instead of 10.10.10.x

---

## ✅ STEP-BY-STEP DIAGNOSTICS

### CHECK 1: DHCP-Server IP Configuration ⭐ CRITICAL

1. Click **DHCP-Server**
2. Go to **Config** tab → **FastEthernet0**

**Verify these EXACT values:**
```
IP Address: 10.10.10.20
Subnet Mask: 255.255.255.0
```

3. Go to **Settings** tab (scroll down in Config)

**Verify:**
```
Gateway: 10.10.10.1
DNS Server: 10.10.10.10
```

**Status:**
- [ ] IP is 10.10.10.20 ✅
- [ ] Subnet is 255.255.255.0 ✅
- [ ] Gateway is 10.10.10.1 ✅

**If ANY of these are wrong, fix them NOW before continuing.**

---

### CHECK 2: DHCP Service Enabled ⭐ CRITICAL

1. Click **DHCP-Server**
2. Go to **Services** tab → **DHCP**

**Verify:**
```
Service: ON (should show radio button selected)
```

**Status:**
- [ ] Service is ON ✅

**If OFF, turn it ON now.**

---

### CHECK 3: DHCP Pool Configuration ⭐ CRITICAL

Still on **DHCP-Server** → **Services** → **DHCP**

**Scroll down to see the pool list.**

**Verify AdminPool exists with EXACT values:**
```
Pool Name: AdminPool
Default Gateway: 10.10.10.1
DNS Server: 10.10.10.10
Start IP Address: 10.10.10.100
Subnet Mask: 255.255.255.0
Maximum Number of Users: 50
```

**Status:**
- [ ] AdminPool exists ✅
- [ ] Default Gateway is 10.10.10.1 ✅
- [ ] DNS Server is 10.10.10.10 ✅
- [ ] Start IP is 10.10.10.100 ✅

**Common Error:** Pool exists but gateway or DNS is wrong.

---

### CHECK 4: Core Switch Port Configuration

1. Click **City-Core-Switch**
2. Go to **CLI** tab
3. Type these commands:

```
enable
show vlan brief
```

**Look for:**
```
10   Admin   active   Gi1/0/6, Gi1/0/7, Gi1/0/8, Gi1/0/9, Gi1/0/10, Gi1/0/11
```

**Verify:**
- [ ] VLAN 10 exists ✅
- [ ] Gi1/0/7 (DHCP-Server) is in VLAN 10 ✅
- [ ] Gi1/0/10 (Admin-PC-1) is in VLAN 10 ✅

Then type:
```
show ip interface brief
```

**Look for:**
```
Vlan10   10.10.10.1   YES manual up   up
```

**Verify:**
- [ ] Vlan10 interface is UP/UP ✅
- [ ] IP is 10.10.10.1 ✅

---

### CHECK 5: Physical Connection

1. Look at the cables in the topology

**Verify:**
- [ ] DHCP-Server to City-Core-Switch cable is GREEN ✅
- [ ] Admin-PC-1 to City-Core-Switch cable is GREEN ✅

**If cables are RED or ORANGE:**
- Click the cable and check both ends are connected
- Check port status on switch

---

### CHECK 6: Test Connectivity from Admin-PC-1

1. Click **Admin-PC-1**
2. Go to **Desktop** → **Command Prompt**

**Test 1: Ping Gateway**
```
ping 10.10.10.1
```

**Expected:** Replies from 10.10.10.1

**If this FAILS:**
- Problem is at Layer 2/3 (switching/routing)
- Check cable connections
- Check VLAN configuration

**Test 2: Ping DHCP Server**
```
ping 10.10.10.20
```

**Expected:** Replies from 10.10.10.20

**If gateway works but DHCP server ping fails:**
- DHCP-Server IP might be wrong
- DHCP-Server might be in wrong VLAN
- Check DHCP-Server cable connection

---

### CHECK 7: DHCP Relay (Probably Not Needed)

**For Admin-PC-1, you DON'T need DHCP relay because:**
- Admin-PC-1 is in VLAN 10
- DHCP-Server is in VLAN 10
- They're in the same subnet (10.10.10.0/24)

**DHCP relay is only needed for:**
- Public-Kiosk-PC (VLAN 20) to get DHCP from VLAN 10
- Resident-Home-PC (VLAN 30) to get DHCP from VLAN 10

**We'll configure relay after we get Admin-PC-1 working.**

---

### CHECK 8: Admin-PC-1 Network Adapter

1. Click **Admin-PC-1**
2. Go to **Config** tab → **FastEthernet0**

**Verify:**
```
Port Status: On
Bandwidth: Auto
Duplex: Auto
```

**Status:**
- [ ] Port Status is ON ✅

---

## 🔥 COMMON ISSUES & FIXES

### Issue 1: DHCP Pool Gateway Wrong
**Symptom:** DHCP assigns IP but PC can't reach network
**Fix:**
1. DHCP-Server → Services → DHCP
2. Find AdminPool
3. Check "Default Gateway" field
4. Must be exactly: `10.10.10.1`
5. Click Save

### Issue 2: DHCP Server IP Wrong Subnet
**Symptom:** DHCP server unreachable
**Fix:**
1. DHCP-Server → Config → FastEthernet0
2. IP must be: `10.10.10.20`
3. Subnet must be: `255.255.255.0`

### Issue 3: DNS Server Not Set in Pool
**Symptom:** DHCP works but DNS doesn't resolve
**Fix:**
1. DHCP-Server → Services → DHCP → AdminPool
2. DNS Server: `10.10.10.10`
3. Click Save

### Issue 4: DHCP Service Not Saved
**Symptom:** Pool created but DHCP still fails
**Fix:**
1. After creating pool, click **Save** button
2. Make sure Service is ON
3. Close and reopen DHCP-Server to verify pool is still there

---

## 🧪 STEP-BY-STEP VERIFICATION

**Do these IN ORDER:**

### Step 1: Verify DHCP Server Can Ping Gateway
1. DHCP-Server → Desktop → Command Prompt
2. `ping 10.10.10.1`
3. **Must get replies**

**If this fails:**
- DHCP-Server IP configuration is wrong
- DHCP-Server cable not connected
- Core switch VLAN 10 interface down

### Step 2: Verify Admin-PC-1 Can Ping Gateway (Using Static IP First)
1. Admin-PC-1 → Desktop → IP Configuration
2. Select **Static**
3. IP Address: `10.10.10.99`
4. Subnet Mask: `255.255.255.0`
5. Default Gateway: `10.10.10.1`
6. Go to Command Prompt
7. `ping 10.10.10.1`

**If this works:**
- Layer 2/3 connectivity is good
- Problem is DHCP configuration

**If this fails:**
- Physical connection problem
- VLAN problem
- Switch port problem

### Step 3: From Admin-PC-1 Static IP, Ping DHCP Server
```
ping 10.10.10.20
```

**If this works:**
- DHCP server is reachable
- Problem is DHCP service or pool configuration

**If this fails:**
- DHCP-Server not configured properly
- DHCP-Server in wrong VLAN

### Step 4: Retry DHCP
1. Admin-PC-1 → Desktop → IP Configuration
2. Select **Static** (to reset)
3. Wait 2 seconds
4. Select **DHCP**
5. Wait for response

---

## 🎯 MOST LIKELY CAUSES (In Order)

### 1. DHCP Pool Not Saved Properly (80% of cases)
**Fix:**
- DHCP-Server → Services → DHCP
- Recreate AdminPool
- **Click SAVE button after entering all values**
- Verify pool appears in list below

### 2. DHCP-Server IP Not Set (15% of cases)
**Fix:**
- DHCP-Server → Config → FastEthernet0
- Set IP: `10.10.10.20`, Subnet: `255.255.255.0`
- Settings → Gateway: `10.10.10.1`

### 3. DHCP Service Not Enabled (3% of cases)
**Fix:**
- DHCP-Server → Services → DHCP
- Click ON radio button

### 4. Physical Connection Problem (2% of cases)
**Fix:**
- Check cable is green
- Check switch port is up

---

## 📋 QUICK DIAGNOSTIC CHECKLIST

Run through this checklist and tell me which step fails:

**DHCP Server Checks:**
- [ ] 1. DHCP-Server IP is 10.10.10.20 ✅
- [ ] 2. DHCP-Server subnet is 255.255.255.0 ✅
- [ ] 3. DHCP-Server gateway is 10.10.10.1 ✅
- [ ] 4. DHCP Service is ON ✅
- [ ] 5. AdminPool exists in pool list ✅
- [ ] 6. AdminPool gateway is 10.10.10.1 ✅
- [ ] 7. AdminPool DNS is 10.10.10.10 ✅
- [ ] 8. AdminPool start IP is 10.10.10.100 ✅
- [ ] 9. DHCP-Server can ping 10.10.10.1 ✅

**Admin-PC-1 Checks:**
- [ ] 10. Cable to switch is GREEN ✅
- [ ] 11. With static IP 10.10.10.99, can ping 10.10.10.1 ✅
- [ ] 12. With static IP 10.10.10.99, can ping 10.10.10.20 ✅

**If all 12 checks pass and DHCP still fails:**
- Packet Tracer bug (rare)
- Try saving and reopening the file
- Try different PC

---

## 🚨 EMERGENCY FIX: Use Static IPs

If DHCP absolutely won't work after all checks:

**Admin-PC-1 Static Configuration:**
```
IP Address: 10.10.10.100
Subnet Mask: 255.255.255.0
Default Gateway: 10.10.10.1
DNS Server: 10.10.10.10
```

**Admin-PC-2 Static Configuration:**
```
IP Address: 10.10.10.101
Subnet Mask: 255.255.255.0
Default Gateway: 10.10.10.1
DNS Server: 10.10.10.10
```

---

## 📞 TELL ME WHICH CHECK FAILED

Go through the diagnostic checklist above and tell me:

1. **Which of the 12 checks FAILED?**
2. **What was the error message?**
3. **Can Admin-PC-1 ping 10.10.10.1 with static IP?**
4. **Can Admin-PC-1 ping 10.10.10.20 with static IP?**

This will tell us exactly where the problem is!
