# PART 2: CONFIGURATION
## 04 - SERVER SETUP (DHCP, DNS, Web, Email)

**Configure all 10 servers with services**

---

## 📋 SERVER OVERVIEW

| City | Server | IP Address | Services | Domain |
|------|--------|------------|----------|--------|
| A | DNS-Server | 192.168.99.10 | DNS | city-a.local |
| A | DHCP-Server | 192.168.99.20 | DHCP | 8 pools |
| A | Web-Server | 192.168.99.30 | HTTP/HTTPS | www.city-a.local |
| A | Email-Server | 192.168.99.40 | SMTP/POP3 | mail.city-a.local |
| B | DNS-Server | 192.168.99.10 | DNS | city-b.local |
| B | DHCP-Server | 192.168.99.20 | DHCP | 8 pools |
| B | Web-Server | 192.168.99.30 | HTTP/HTTPS | www.city-b.local |
| B | Email-Server | 192.168.99.40 | SMTP/POP3 | mail.city-b.local |
| ISP | Internet-DNS-Root | 8.8.8.8 | DNS | Root server |
| ISP | Internet-Web-Server | 8.8.8.10 | HTTP | www.example.com |

---

## 🏙️ CITY A - SERVER CONFIGURATIONS

---

## 🔧 **SERVER 1: CityA-DNS-Server**

### **Step 1: Configure IP Address**

1. Click **CityA-DNS-Server** device
2. Click **Desktop** tab
3. Click **IP Configuration**

**Configure Static IP:**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.99.10 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.99.1 |
| DNS Server | 192.168.99.10 (itself) |
| IPv6 Address | 2001:db8:a:99::10 |
| IPv6 Gateway | 2001:db8:a:99::1 |
| IPv6 Prefix Length | 64 |

Click **Submit** / **Apply**

---

### **Step 2: Enable DNS Service**

1. Click **Services** tab
2. Click **DNS**
3. Turn DNS Service **ON**

---

### **Step 3: Add DNS Records**

**Add the following records:**

| Name | Type | Address | Purpose |
|------|------|---------|---------|
| `city-a.local` | A | 192.168.99.30 | City website |
| `www.city-a.local` | A | 192.168.99.30 | City website |
| `mail.city-a.local` | A | 192.168.99.40 | Email server |
| `dns.city-a.local` | A | 192.168.99.10 | DNS server |
| `dhcp.city-a.local` | A | 192.168.99.20 | DHCP server |
| `core-router.city-a.local` | A | 192.168.99.1 | Core router |
| `city-b.local` | A | 203.0.114.1 | City B (public IP) |
| `example.com` | A | 8.8.8.10 | Internet server |

**For each record:**
1. Enter **Name**
2. Enter **Address**
3. Click **Add**

---

### **Step 4: Configure IPv6 DNS (Optional)**

Add AAAA records:

| Name | Type | Address |
|------|------|---------|
| `city-a.local` | AAAA | 2001:db8:a:99::30 |
| `www.city-a.local` | AAAA | 2001:db8:a:99::30 |

---

### **Step 5: Verification**

1. Click **Desktop** → **Command Prompt**
2. Type: `nslookup www.city-a.local`

**Expected output:**
```
Name: www.city-a.local
Address: 192.168.99.30
```

✅ **CityA-DNS-Server Complete**

---

## 🔧 **SERVER 2: CityA-DHCP-Server**

### **Step 1: Configure IP Address**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.99.20 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.99.1 |
| DNS Server | 192.168.99.10 |
| IPv6 Address | 2001:db8:a:99::20 |
| IPv6 Gateway | 2001:db8:a:99::1 |

---

### **Step 2: Enable DHCP Service**

1. Click **Services** tab
2. Click **DHCP**
3. Service is ON by default

---

### **Step 3: Create DHCP Pools**

#### **Pool 1: VLAN 10 - Government**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN10_Government` |
| Default Gateway | `192.168.10.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.10.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `100` |

Click **Add**

---

#### **Pool 2: VLAN 20 - Residential**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN20_Residential` |
| Default Gateway | `192.168.20.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.20.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `120` |

Click **Add**

---

#### **Pool 3: VLAN 30 - Commercial**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN30_Commercial` |
| Default Gateway | `192.168.30.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.30.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `120` |

Click **Add**

---

#### **Pool 4: VLAN 40 - Transportation**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN40_Transportation` |
| Default Gateway | `192.168.40.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.40.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `50` |

Click **Add**

---

#### **Pool 5: VLAN 50 - Public WiFi**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN50_Public_WiFi` |
| Default Gateway | `192.168.50.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.50.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `120` |

Click **Add**

---

#### **Pool 6: VLAN 60 - Emergency**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN60_Emergency` |
| Default Gateway | `192.168.60.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.60.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `50` |

Click **Add**

---

#### **Pool 7: VLAN 70 - Utilities**

| Field | Value |
|-------|-------|
| Pool Name | `VLAN70_Utilities` |
| Default Gateway | `192.168.70.1` |
| DNS Server | `192.168.99.10` |
| Start IP Address | `192.168.70.100` |
| Subnet Mask | `255.255.255.0` |
| Maximum Number of Users | `50` |

Click **Add**

---

### **Step 4: Verification**

1. Check that 8 pools are listed
2. Note: Pool utilization shows after devices connect

✅ **CityA-DHCP-Server Complete**

---

## 🔧 **SERVER 3: CityA-Web-Server**

### **Step 1: Configure IP Address**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.99.30 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.99.1 |
| DNS Server | 192.168.99.10 |
| IPv6 Address | 2001:db8:a:99::30 |

---

### **Step 2: Enable HTTP/HTTPS Service**

1. Click **Services** tab
2. Click **HTTP**
3. Service is ON by default

---

### **Step 3: Edit Web Page (Optional)**

1. In HTTP service, click **Edit** next to `index.html`
2. Replace content:

```html
<html>
<head><title>City A Smart City Portal</title></head>
<body>
<h1>Welcome to City A</h1>
<p>Smart City IoT Network - City A Portal</p>
<ul>
  <li>Population: 500,000</li>
  <li>IoT Sensors: 15 active</li>
  <li>Network Status: Online</li>
</ul>
<p>Services: Government | Residential | Commercial | Transportation | Utilities</p>
</body>
</html>
```

3. Click **Save**

---

### **Step 4: Enable HTTPS (Optional)**

1. In HTTP service, check **HTTPS** box
2. Service starts on port 443

---

### **Step 5: Verification**

1. From **CityA-Gov-PC-1**:
2. Click **Desktop** → **Web Browser**
3. Enter URL: `http://192.168.99.30`
4. Should see City A welcome page

✅ **CityA-Web-Server Complete**

---

## 🔧 **SERVER 4: CityA-Email-Server**

### **Step 1: Configure IP Address**

| Field | Value |
|-------|-------|
| IPv4 Address | 192.168.99.40 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.99.1 |
| DNS Server | 192.168.99.10 |
| IPv6 Address | 2001:db8:a:99::40 |

---

### **Step 2: Enable Email Service**

1. Click **Services** tab
2. Click **EMAIL**
3. Service is ON by default

---

### **Step 3: Configure Domain**

| Field | Value |
|-------|-------|
| Domain Name | `city-a.local` |

---

### **Step 4: Add Email Users**

**User 1: Administrator**
- User: `admin`
- Password: `admin123`
- Click **+** button

**User 2: Government**
- User: `gov.admin`
- Password: `gov123`
- Click **+**

**User 3: Police**
- User: `police`
- Password: `police123`
- Click **+**

**User 4: Operations**
- User: `operations`
- Password: `ops123`
- Click **+**

---

### **Step 5: Verification**

1. From **CityA-Gov-PC-1**:
2. Click **Desktop** → **Email**
3. Configure:
   - Your Name: `Administrator`
   - Email Address: `admin@city-a.local`
   - Incoming/Outgoing Mail Server: `192.168.99.40`
   - User: `admin`
   - Password: `admin123`
4. Click **Compose** → Send test email

✅ **CityA-Email-Server Complete**

---

## 🏙️ CITY B - SERVER CONFIGURATIONS

**EXACT COPY of City A servers**

### **Changes Required:**
1. **DNS Records:** Change to `city-b.local` domain
2. **DHCP Pools:** Same (private IPs identical)
3. **Web Page:** Change to "City B"
4. **Email Domain:** `city-b.local`

### **Example: CityB-DNS-Server Records**

| Name | Address |
|------|---------|
| `city-b.local` | 192.168.99.30 |
| `www.city-b.local` | 192.168.99.30 |
| `mail.city-b.local` | 192.168.99.40 |
| `city-a.local` | 203.0.113.1 |

---

## 🌐 ISP - INTERNET SERVERS

---

## 🔧 **Internet-DNS-Root**

### **Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 8.8.8.8 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 8.8.8.1 |

### **DNS Records:**

| Name | Address |
|------|---------|
| `example.com` | 8.8.8.10 |
| `www.example.com` | 8.8.8.10 |
| `google.com` | 8.8.8.8 |

---

## 🔧 **Internet-Web-Server**

### **Configuration:**

| Field | Value |
|-------|-------|
| IPv4 Address | 8.8.8.10 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 8.8.8.1 |
| DNS Server | 8.8.8.8 |

### **HTTP Service:**
- Enable HTTP
- Edit `index.html`:

```html
<html>
<head><title>Internet Test Page</title></head>
<body>
<h1>Welcome to the Internet!</h1>
<p>This page simulates www.example.com</p>
<p>You have successfully accessed the internet from your smart city!</p>
</body>
</html>
```

---

## ✅ SERVER CONFIGURATION CHECKLIST

**City A:**
- [ ] CityA-DNS-Server (8+ DNS records)
- [ ] CityA-DHCP-Server (8 DHCP pools)
- [ ] CityA-Web-Server (HTTP/HTTPS)
- [ ] CityA-Email-Server (4 users)

**City B:**
- [ ] 4 servers (mirror City A with domain changes)

**ISP:**
- [ ] Internet-DNS-Root (DNS service)
- [ ] Internet-Web-Server (HTTP service)

**Total: 10 servers** ✅

---

## 🔍 VERIFICATION TESTS

### **DNS Test:**
From any PC:
```
nslookup www.city-a.local
nslookup www.city-b.local
nslookup www.example.com
```

### **DHCP Test:**
1. Set PC to DHCP
2. Check `ipconfig` for IP in correct range

### **Web Test:**
1. Open Web Browser
2. Navigate to `http://www.city-a.local`
3. Should see city portal

### **Email Test:**
1. Configure Email client
2. Send test email
3. Check receive

---

## ⏱️ ESTIMATED TIME

- DNS servers: 15 minutes (2 servers)
- DHCP servers: 20 minutes (2 servers)
- Web servers: 10 minutes (2 servers)
- Email servers: 15 minutes (2 servers)
- ISP servers: 10 minutes (2 servers)
- **Total: ~1.5 hours**

---

## 📝 NEXT STEP

✅ **All servers configured**

➡️ **Next:** `05_WIRELESS_SETUP.md` for WiFi and cellular!

**Server configuration complete!** 🚀
