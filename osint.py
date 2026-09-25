import os
import re
import sys
import time
import socket
import hashlib
import requests

# ==========================================
# 🎨 ADVANCED GRADIENT RENDER ENGINE
# ==========================================
class RGB:
    START = (0, 255, 255) # Cyan (Default)
    END = (255, 0, 255)   # Magenta (Default)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def v_print(text, speed=0):
    """Mencetak teks multi-baris dengan gradasi VERTIKAL (Atas ke Bawah)"""
    lines = text.split('\n')
    L = max(1, len(lines) - 1)
    for i, line in enumerate(lines):
        if not line:
            print()
            continue
        ratio = i / L
        r = int(RGB.START[0] + (RGB.END[0] - RGB.START[0]) * ratio)
        g = int(RGB.START[1] + (RGB.END[1] - RGB.START[1]) * ratio)
        b = int(RGB.START[2] + (RGB.END[2] - RGB.START[2]) * ratio)
        color = f"\033[1m\033[38;2;{r};{g};{b}m"
        
        if speed > 0:
            sys.stdout.write(color)
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            sys.stdout.write("\033[0m\n")
        else:
            print(f"{color}{line}\033[0m")

def h_print(text):
    """Mencetak teks dengan gradasi HORIZONTAL (Kiri ke Kanan)"""
    lines = text.split('\n')
    for line in lines:
        if not line:
            print()
            continue
        L = max(1, len(line) - 1)
        res = ""
        for i, char in enumerate(line):
            ratio = i / L
            r = int(RGB.START[0] + (RGB.END[0] - RGB.START[0]) * ratio)
            g = int(RGB.START[1] + (RGB.END[1] - RGB.START[1]) * ratio)
            b = int(RGB.START[2] + (RGB.END[2] - RGB.START[2]) * ratio)
            res += f"\033[1m\033[38;2;{r};{g};{b}m{char}"
        print(res + "\033[0m")

def h_input(text):
    """Fungsi input dengan gradasi HORIZONTAL"""
    lines = text.split('\n')
    for line in lines[:-1]:
        if not line:
            print()
            continue
        h_print(line)
        
    last_line = lines[-1]
    L = max(1, len(last_line) - 1)
    res = ""
    for i, char in enumerate(last_line):
        ratio = i / L
        r = int(RGB.START[0] + (RGB.END[0] - RGB.START[0]) * ratio)
        g = int(RGB.START[1] + (RGB.END[1] - RGB.START[1]) * ratio)
        b = int(RGB.START[2] + (RGB.END[2] - RGB.START[2]) * ratio)
        res += f"\033[1m\033[38;2;{r};{g};{b}m{char}"
    return input(res + "\033[0m")

# ==========================================
# 🖼️ BANNER & MENU INTERFACE
# ==========================================
def print_banner():
    clear_screen()
    banner = """
  ██████  ███████ ██ ███    ██ ████████ 
 ██    ██ ██      ██ ████   ██    ██    
 ██    ██ ███████ ██ ██ ██  ██    ██    
 ██    ██      ██ ██ ██  ██ ██    ██    
  ██████  ███████ ██ ██   ████    ██    

 ╭──────────────────────────────────────────────────────────╮
 │ [>] TOOL     : MULTI-PURPOSE OSINT RECON FRAMEWORK       │
 │ [>] DEV      : DOCTOR BARMODS                            │
 │ [>] VERSION  : 7.0.0 (FULL GRADIENT EDITION)             │
 ╰──────────────────────────────────────────────────────────╯"""
    v_print(banner, speed=0.001)

def print_menu():
    menu = """
 [ MENU SELECTION ]
 [01] CEK KUOTA DAN NOMOR XL AXIS
 [02] IP & Domain Geolocation / ASN Lookup
 [03] Subdomain Certificate Recon (crt.sh)
 [04] GitHub Target Intelligence
 [05] Stealth Network Port Scanner
 [06] HTTP Header Grabber & Tech Recon
 [07] MAC Address Vendor Lookup
 [08] URL Unshortener & Redirect Tracer
 [09] DNS Record Scanner (A, MX, TXT) 
 [10] WHOIS Domain Intelligence Lookup
 [11] Hash & Crypto Generator (MD5/SHA256)
 [12] SUNTIK SOSMED 
 [99] Edit Tema Warna (Gradient Settings)
 [00] Exit Session
"""
    v_print(menu)

# ==========================================
# ⚙️ KONFIGURASI API OSINT & SMM PANEL
# ==========================================
KMSP_HEADERS = {
    "Authorization": "Basic c2lkb21wdWxhcGk6YXBpZ3drbXNw",
    "X-API-Key": "60ef29aa-a648-4668-90ae-20951ef90c55",
    "X-App-Version": "4.0.0",
    "User-Agent": "Mozilla/5.0"
}

SMM_API_URL = "https://pusatpanelsmm.com/api/json.php"  
SMM_API_KEY = "57356894783dbe9663b024e1c385ae2e2db3f87dab69ee4620278e35c40c5718"
SMM_SECRET_KEY = "37ba1b616ff5bed38617d6572ea775e2c587090373509eab6386c8b671af49bf"

def normalize_number(msisdn):
    s = re.sub(r'[\s().\-]', '', str(msisdn)).strip()
    if s.startswith("+"): s = s[1:]
    if s.startswith("0"): s = "62" + s[1:]
    elif s.startswith("8"): s = "62" + s
    if not s.isdigit() or len(s) < 10 or len(s) > 15:
        return None
    return s

def clean_html(text):
    if not text: return ""
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.replace("&nbsp;", " ").replace("&amp;", "&").replace("=", "").strip()

# ==========================================
# 🎨 MODUL 99: GRADIENT THEME SETTINGS
# ==========================================
def run_color_settings():
    menu = """
 [*] RGB GRADIENT EDITOR
 [1] Mode Cyberpunk (Cyan -> Magenta)
 [2] Mode Hacker (Lime Green -> Dark Green)
 [3] Mode Sunset (Orange -> Purple)
 [4] Mode Iceberg (White -> Deep Blue)
 [5] Mode Blood (Crimson Red -> Dark Gray)
 [6] Custom Gradient Manual
"""
    v_print(menu)
    c = h_input("\n [?] Pilih tema gradasi (1-6): ").strip()
    
    if c == '1':
        RGB.START = (0, 255, 255); RGB.END = (255, 0, 255)
    elif c == '2':
        RGB.START = (0, 255, 0); RGB.END = (0, 100, 0)
    elif c == '3':
        RGB.START = (255, 150, 0); RGB.END = (138, 43, 226)
    elif c == '4':
        RGB.START = (255, 255, 255); RGB.END = (0, 0, 255)
    elif c == '5':
        RGB.START = (255, 20, 60); RGB.END = (100, 100, 100)
    elif c == '6':
        h_print("\n [!] Masukkan RGB (0-255) format: R,G,B")
        try:
            p = h_input(" [?] Warna Atas / Kiri (START): ").strip()
            RGB.START = tuple(map(int, p.split(',')))
            s = h_input(" [?] Warna Bawah / Kanan (END): ").strip()
            RGB.END = tuple(map(int, s.split(',')))
        except:
            h_print(" [!] Format salah. Dibatalkan.")
            return
    else: return
    
    h_print("\n [+] Tema Gradasi Berhasil Diubah!")
    time.sleep(1)

# ==========================================
# 🛒 MODUL 12: SMM PANEL INTEGRATION
# ==========================================
def call_smm_api(action, **kwargs):
    payload = {
        "api_key": SMM_API_KEY,
        "secret_key": SMM_SECRET_KEY,
        "action": action
    }
    payload.update(kwargs)
    try:
        res = requests.post(SMM_API_URL, data=payload, timeout=20)
        return res.json()
    except Exception as e:
        h_print(f" [!] Koneksi API SMM Gagal / Timeout: {e}")
        return None

def run_smm_panel():
    while True:
        clear_screen()
        smm_menu = """
 ═════════════════[ SUNTIK SOSMED BY DOCTOR BARMODS ]═════════════════
 [1] Cek Profil & Saldo Akun
 [2] Lihat Daftar Layanan (Dashboard Pages & Search)
 [3] Buat Pesanan Baru (Order)
 [4] Cek Status Pesanan (Order Status)
 [5] Request Refill Layanan
 [6] Cek Status Refill
 [0] Kembali ke Menu Utama
"""
        v_print(smm_menu)
        pilihan = h_input("\n [?] Pilih menu SMM: ").strip()

        if pilihan == '1':
            data = call_smm_api("profile")
            if data and data.get("status"):
                d = data.get("data", {})
                out = f"""
 [+] PROFIL SMM BERHASIL DIAMBIL
  ├─ Username : {d.get('username')}
  ├─ Full Name: {d.get('full_name')}
  ├─ Email    : {d.get('email')}
  └─ Saldo    : Rp {d.get('balance')}
"""
                v_print(out)
            else:
                h_print(f"\n [!] Gagal: {data.get('data', {}).get('msg') if data else 'Error'}")

        elif pilihan == '2':
            h_print("\n [*] Mengambil seluruh data layanan dari server...")
            data = call_smm_api("services")
            if data and data.get("status"):
                all_services = data.get("data", [])
                filtered_services = all_services
                items_per_page = 10
                current_page = 0
                
                while True:
                    total_services = len(filtered_services)
                    total_pages = max(1, (total_services + items_per_page - 1) // items_per_page)
                    if current_page >= total_pages: current_page = max(0, total_pages - 1)
                    
                    clear_screen()
                    table = f"\n [+] DAFTAR LAYANAN SMM (Ditemukan: {total_services} | Hal: {current_page+1}/{total_pages})\n"
                    table += "  ID    | Harga    | Nama Layanan\n"
                    table += "  ──────┼──────────┼──────────────────────────────────────────────────\n"
                    
                    start_idx = current_page * items_per_page
                    end_idx = start_idx + items_per_page
                    
                    for s in filtered_services[start_idx:end_idx]:
                        s_id = str(s.get('id', ''))
                        s_price = f"Rp{s.get('price', '')}"
                        s_name = str(s.get('name', ''))
                        if len(s_name) > 48: s_name = s_name[:45] + "..."
                        table += f"  {s_id:<5} | {s_price:<8} | {s_name}\n"
                    
                    table += "  ──────┴──────────┴──────────────────────────────────────────────────\n"
                    table += "  [N] Next   [P] Prev   [S] Search   [R] Reset Search   [Q] Quit"
                    
                    v_print(table)
                    nav = h_input("\n [?] Pilih aksi (N/P/S/R/Q): ").strip().lower()
                    
                    if nav == 'n':
                        if current_page < total_pages - 1: current_page += 1
                        else: h_print(" [!] Ini halaman terakhir."); time.sleep(0.5)
                    elif nav == 'p':
                        if current_page > 0: current_page -= 1
                        else: h_print(" [!] Ini halaman pertama."); time.sleep(0.5)
                    elif nav == 's':
                        kw = h_input(" [?] Kata pencarian (misal: instagram): ").strip().lower()
                        filtered_services = [s for s in all_services if kw in str(s.get('name', '')).lower()]
                        current_page = 0
                    elif nav == 'r':
                        filtered_services = all_services
                        current_page = 0
                    elif nav == 'q':
                        break
                    else:
                        h_print(" [!] Input tidak valid."); time.sleep(0.5)
                continue
            else:
                h_print(f"\n [!] Gagal: {data.get('data', {}).get('msg') if data else 'Error'}")

        elif pilihan == '3':
            h_print("\n [*] PEMESANAN BARU")
            svc = h_input("  ├─ Masukkan ID Service: ").strip()
            tgt = h_input("  ├─ Target (URL/Username): ").strip()
            qty = h_input("  └─ Jumlah (Quantity): ").strip()
            
            data = call_smm_api("order", service=svc, data=tgt, quantity=qty)
            if data and data.get("status"):
                out = f"\n [+] PESANAN BERHASIL DIBUAT\n  └─ Order ID : {data.get('data', {}).get('id')}\n"
                v_print(out)
            else:
                h_print(f"\n [!] Order Gagal: {data.get('data', {}).get('msg') if data else 'Error'}")

        elif pilihan == '4':
            oid = h_input("\n [?] Masukkan Order ID: ").strip()
            data = call_smm_api("status", id=oid)
            if data and data.get("status"):
                d = data.get("data", {})
                out = f"""
 [+] STATUS PESANAN (ID: {oid})
  ├─ Status     : {d.get('status')}
  ├─ Start Count: {d.get('start_count')}
  └─ Remains    : {d.get('remains')}
"""
                v_print(out)
            else:
                h_print(f"\n [!] Gagal: {data.get('data', {}).get('msg') if data else 'Error'}")

        elif pilihan == '5':
            oid = h_input("\n [?] Masukkan Order ID yang akan di-Refill: ").strip()
            data = call_smm_api("refill", order=oid)
            if data and data.get("status"):
                d = data.get("data", [])[0] if data.get("data") else {}
                out = f"\n [+] REFILL BERHASIL DIREQUEST\n  └─ Refill ID : {d.get('refill')}\n"
                v_print(out)
            else:
                d = data.get("data", [])[0] if data and data.get("data") else {}
                h_print(f"\n [!] Refill Gagal: {d.get('msg', 'Error')}")

        elif pilihan == '6':
            rid = h_input("\n [?] Masukkan Refill ID: ").strip()
            data = call_smm_api("refill_status", refill=rid)
            if data and data.get("status"):
                d = data.get("data", [])[0] if data.get("data") else {}
                out = f"\n [+] STATUS REFILL (ID: {rid})\n  └─ Status : {d.get('status')}\n"
                v_print(out)
            else:
                d = data.get("data", [])[0] if data and data.get("data") else {}
                h_print(f"\n [!] Gagal: {d.get('msg', 'Error')}")

        elif pilihan == '0':
            h_print("\n [*] Kembali ke menu utama...")
            time.sleep(0.5)
            break
        else:
            h_print(" [!] Pilihan tidak valid.")

        h_input("\n [Tekan ENTER untuk kembali ke Menu SMM]")

# ==========================================
# 📡 MODUL OSINT & NET UTILS (1 - 11)
# ==========================================
def run_telco_recon():
    raw_num = h_input("\n [?] Masukkan Nomor Target (08xxx): ").strip()
    msisdn = normalize_number(raw_num)
    if not msisdn:
        h_print(" [!] Format nomor tidak valid.")
        return

    h_print(f" [*] Penetrasi data target {msisdn}...")
    
    try:
        url_bendith = f"https://bendith.my.id/end.php?check=package&number={msisdn}&version=2"
        b_res = requests.get(url_bendith, timeout=12).json()
        if b_res.get("success") and b_res.get("data", {}).get("subs_info"):
            info = b_res["data"].get("subs_info", {})
            pkgs = b_res["data"].get("package_info", {}).get("packages", [])
            
            out = f"""
 [+] TELCO RECON SUCCESS (BENDITH ENGINE)
  ├─ Target       : {msisdn}
  ├─ Provider     : {info.get('operator', 'XL')}
  ├─ Network      : {info.get('net_type', '-')}
  ├─ Masa Aktif   : {info.get('exp_date', '-')}
  └─ Masa Tenggang: {info.get('grace_until', '-')}
"""
            if pkgs:
                out += "\n 📊 DETAIL PAKET & KUOTA:\n"
                for p in pkgs:
                    out += f"  ┌─ {p.get('name', '-')} (Exp: {p.get('expiry', '-')})\n"
                    for q in p.get("quotas", []):
                        out += f"  │  └─ {q.get('name', '-')}: {q.get('remaining', '-')} / {q.get('total', '-')}\n"
            v_print(out)
            return
    except:
        pass

    h_print(" [*] Rerouting payload ke KMSP Engine...")
    try:
        url_kmsp = "https://apigw.kmsp-store.com/sidompul/v4/cek_kuota"
        k_res = requests.get(url_kmsp, headers=KMSP_HEADERS, params={"msisdn": msisdn, "isJSON": "true"}, timeout=15).json()
        if k_res.get("status"):
            sp = k_res.get("data", {}).get("data_sp", {})
            raw_hasil = k_res.get("data", {}).get("hasil", "")
            
            out = f"""
 [+] TELCO RECON SUCCESS (KMSP ENGINE)
  ├─ Target       : {msisdn}
  ├─ Provider     : {sp.get('prefix', {}).get('value', 'XL')}
  ├─ 4G Status    : {sp.get('status_4g', {}).get('value', '-')}
  ├─ Masa Aktif   : {sp.get('active_period', {}).get('value', '-')}
  └─ Masa Tenggang: {sp.get('grace_period', {}).get('value', '-')}
"""
            if raw_hasil:
                out += "\n 📊 DETAIL PAKET & KUOTA:\n"
                clean_txt = clean_html(raw_hasil)
                sections = re.split(r'(?=🎁 Quota:|🎁 Benefit:)', clean_txt)
                for sec in sections:
                    if sec.strip(): 
                        out += f"  {sec.strip()}\n"
            else:
                out += "\n [!] Tidak ada rincian paket di API KMSP.\n"
            v_print(out)
            return
    except:
        pass
    h_print(" [!] Target gagal dilacak atau nomor tidak aktif.")

def run_ip_recon():
    target = h_input("\n [?] Masukkan IP Address / Domain: ").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    if not target_clean: return
    h_print(" [*] Tracing network metadata...")
    try:
        res = requests.get(f"http://ip-api.com/json/{target_clean}?fields=status,country,city,isp,as,query,lat,lon", timeout=10).json()
        if res.get("status") == "success":
            out = f"""
 [+] GEO-IP INTELLIGENCE ACQUIRED
  ├─ IP / Domain  : {res.get('query')}
  ├─ Location     : {res.get('city')}, {res.get('country')}
  ├─ ISP / ASN    : {res.get('isp')} / {res.get('as')}
  └─ Coordinates  : {res.get('lat')}, {res.get('lon')}
"""
            v_print(out)
        else:
            h_print(" [!] Gagal mendapatkan data IP.")
    except:
        h_print(" [!] API Timeout.")

def run_subdomain_recon():
    target = h_input("\n [?] Masukkan Domain Utama: ").strip()
    domain = re.sub(r'^https?://', '', target).split('/')[0]
    if not domain: return
    h_print(" [*] Mining SSL logs via crt.sh...")
    try:
        res = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=20)
        if res.status_code == 200:
            subdomains = {name.strip().lower() for item in res.json() for name in item.get('name_value', '').split('\n') if name.strip().lower().endswith(domain) and '*' not in name}
            out = f"\n [+] Ditemukan {len(subdomains)} Subdomain Terdaftar:\n"
            for sub in sorted(subdomains)[:30]: 
                out += f"  └─ {sub}\n"
            if len(subdomains) > 30: 
                out += f"  ... dan {len(subdomains)-30} lainnya.\n"
            v_print(out)
    except:
        h_print(" [!] Gagal terkoneksi ke crt.sh.")

def run_github_recon():
    username = h_input("\n [?] Masukkan Username GitHub Target: ").strip()
    try:
        res = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        if res.status_code == 200:
            data = res.json()
            out = f"""
 [+] GITHUB PROFILE IDENTIFIED
  ├─ Nama Lengkap : {data.get('name', '-')}
  ├─ Public Email : {data.get('email', 'Hidden')}
  ├─ Lokasi       : {data.get('location', '-')}
  └─ Repositori   : {data.get('public_repos', 0)} Repos
"""
            v_print(out)
    except:
        h_print(" [!] Gagal melacak profil.")

def run_port_scanner():
    target = h_input("\n [?] Masukkan IP/Domain Target: ").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    COMMON_PORTS = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MYSQL"}
    try:
        ip = socket.gethostbyname(target_clean)
        h_print(f"\n [*] Scanning {target_clean} ({ip})...")
        for port, service in COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                h_print(f"  [+] Port {port:<5} [OPEN] -> {service}")
            sock.close()
    except:
        h_print(" [!] Gagal melakukan scan port.")

def run_header_grabber():
    target = h_input("\n [?] URL Website Target: ").strip()
    if not target.startswith('http'): target = 'http://' + target
    h_print(" [*] Menarik HTTP Headers...")
    try:
        res = requests.head(target, timeout=10, allow_redirects=True, headers=KMSP_HEADERS)
        out = f"""
 [+] HTTP HEADERS ACQUIRED
  ├─ Server Tech  : {res.headers.get('Server', 'Unknown')}
  ├─ X-Powered-By : {res.headers.get('X-Powered-By', 'Unknown')}
  └─ Content-Type : {res.headers.get('Content-Type', 'Unknown')}
"""
        v_print(out)
    except Exception as e:
        h_print(f" [!] Gagal terhubung: {e}")

def run_mac_lookup():
    mac = h_input("\n [?] MAC Address (00:11:22:33:44:55): ").strip()
    try:
        res = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)
        if res.status_code == 200:
            out = f"\n [+] MAC VENDOR IDENTIFIED\n  └─ Vendor : {res.text}\n"
            v_print(out)
        else:
            h_print(" [!] MAC Address tidak ditemukan.")
    except:
        h_print(" [!] Koneksi gagal.")

def run_url_unshortener():
    url = h_input("\n [?] URL Pendek (bit.ly/xxx): ").strip()
    if not url.startswith('http'): url = 'http://' + url
    try:
        res = requests.Session().head(url, allow_redirects=True, timeout=10)
        out = f"\n [+] URL REDIRECT TRACED\n  └─ URL Asli : {res.url}\n"
        v_print(out)
    except Exception as e:
        h_print(f" [!] Tracing gagal: {e}")

def run_dns_scanner():
    target = h_input("\n [?] Masukkan Domain Target: ").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    h_print(" [*] Querying DNS Records...")
    try:
        res = requests.get(f"https://networkcalc.com/api/dns/lookup/{target_clean}", timeout=15).json()
        if res.get("status") == "OK":
            records = res.get("records", {})
            out = "\n [+] DNS RECORDS AQUIRED\n"
            if records.get("A"):
                out += "  ├─ [A] Records (IPv4):\n"
                for r in records["A"]: out += f"  │  └─ {r['address']}\n"
            if records.get("MX"):
                out += "  ├─ [MX] Mail Servers:\n"
                for r in records["MX"]: out += f"  │  └─ {r['exchange']} (Priority: {r['priority']})\n"
            if records.get("TXT"):
                out += "  └─ [TXT] Verifications:\n"
                for r in records["TXT"]: out += f"     └─ {r[:60]}...\n"
            v_print(out)
        else:
            h_print(" [!] Gagal mengambil data DNS.")
    except Exception as e:
        h_print(f" [!] API Error: {e}")

def run_whois_lookup():
    target = h_input("\n [?] Masukkan Domain Target: ").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    h_print(" [*] Mengambil data kepemilikan domain (WHOIS)...")
    try:
        res = requests.get(f"https://networkcalc.com/api/dns/whois/{target_clean}", timeout=15).json()
        if res.get("status") == "OK" and res.get("whois"):
            w = res["whois"]
            out = f"""
 [+] WHOIS DATA ACQUIRED
  ├─ Domain       : {target_clean}
  ├─ Registrar    : {w.get('registrar', 'Hidden')}
  ├─ Dibuat Pada  : {w.get('creation_date', '-')}
  ├─ Berakhir Pada: {w.get('expiration_date', '-')}
"""
            servers = w.get("name_servers")
            if servers: out += f"  └─ Name Servers : {servers[0] if servers else '-'}\n"
            v_print(out)
        else:
            h_print(" [!] Data WHOIS diproteksi atau tidak ditemukan.")
    except Exception as e:
        h_print(f" [!] API Error: {e}")

def run_hash_generator():
    text = h_input("\n [?] Masukkan Text/String: ").strip()
    if not text: return
    out = f"""
 [+] CRYPTOGRAPHY HASH GENERATED
  ├─ MD5   : {hashlib.md5(text.encode()).hexdigest()}
  ├─ SHA1  : {hashlib.sha1(text.encode()).hexdigest()}
  └─ SHA256: {hashlib.sha256(text.encode()).hexdigest()}
"""
    v_print(out)

# ==========================================
# 🔄 MAIN LOOP
# ==========================================
def main():
    while True:
        try:
            print_banner()
            print_menu()
            choice = h_input("\n root@dr-barmods:~# ").strip()

            if choice in ['1', '01']: run_telco_recon()
            elif choice in ['2', '02']: run_ip_recon()
            elif choice in ['3', '03']: run_subdomain_recon()
            elif choice in ['4', '04']: run_github_recon()
            elif choice in ['5', '05']: run_port_scanner()
            elif choice in ['6', '06']: run_header_grabber()
            elif choice in ['7', '07']: run_mac_lookup()
            elif choice in ['8', '08']: run_url_unshortener()
            elif choice in ['9', '09']: run_dns_scanner()
            elif choice in ['10']: run_whois_lookup()
            elif choice in ['11']: run_hash_generator()
            elif choice in ['12']: run_smm_panel() 
            elif choice in ['99']: run_color_settings()
            elif choice in ['0', '00', 'exit', 'quit']:
                h_print("\n [*] Session terminated by user.")
                break
            else:
                continue

            h_input("\n [Tekan ENTER untuk kembali ke Menu Utama]")

        except KeyboardInterrupt:
            h_print("\n\n [*] Session aborted. Keluar...")
            sys.exit(0)

if __name__ == "__main__":
    main()
