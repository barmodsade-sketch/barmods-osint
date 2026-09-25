import os
import re
import sys
import time
import socket
import hashlib
import requests

# ==========================================
# 🎨 RGB TRUE COLOR ENGINE (DYNAMIC)
# ==========================================
class RGB:
    PRIMARY   = '\033[38;2;0;255;128m'    # Hijau Neon
    SECONDARY = '\033[38;2;0;200;255m'    # Biru Cyan
    ACCENT    = '\033[38;2;255;180;50m'   # Kuning / Emas
    DANGER    = '\033[38;2;255;50;80m'    # Merah Terang
    WHITE     = '\033[38;2;240;240;240m'  # Putih Bersih
    GRAY      = '\033[38;2;150;150;150m'  # Abu-abu
    RESET     = '\033[0m'
    BOLD      = '\033[1m'

    @classmethod
    def set_color(cls, name, r, g, b):
        setattr(cls, name, f'\033[38;2;{r};{g};{b}m')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text, speed=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_banner():
    clear_screen()
    banner = f"""{RGB.PRIMARY}{RGB.BOLD}
  ██████  ███████ ██ ███    ██ ████████ 
 ██    ██ ██      ██ ████   ██    ██    
 ██    ██ ███████ ██ ██ ██  ██    ██    
 ██    ██      ██ ██ ██  ██ ██    ██    
  ██████  ███████ ██ ██   ████    ██    
{RGB.SECONDARY}
 ╭──────────────────────────────────────────────────────────╮
 │ [>] TOOL     : MULTI-PURPOSE OSINT RECON FRAMEWORK            │
 │ [>]DEV        : DOCTOR BARMODS                                │
 │ [>] VERSION  : 1.0.0                                          │
 ╰──────────────────────────────────────────────────────────╯{RGB.RESET}
"""
    typing_print(banner)

def print_menu():
    menu = f"""{RGB.ACCENT}[ MENU SELECTION ]{RGB.RESET}
 {RGB.PRIMARY}[01]{RGB.RESET} {RGB.WHITE}CEK KUOTA DAN NOMOR XL AXIS{RGB.RESET}
 {RGB.PRIMARY}[02]{RGB.RESET} {RGB.WHITE}IP & Domain Geolocation / ASN Lookup{RGB.RESET}
 {RGB.PRIMARY}[03]{RGB.RESET} {RGB.WHITE}Subdomain Certificate Recon (crt.sh){RGB.RESET}
 {RGB.PRIMARY}[04]{RGB.RESET} {RGB.WHITE}GitHub Target Intelligence{RGB.RESET}
 {RGB.PRIMARY}[05]{RGB.RESET} {RGB.WHITE}Stealth Network Port Scanner{RGB.RESET}
 {RGB.SECONDARY}[06]{RGB.RESET} {RGB.WHITE}HTTP Header Grabber & Tech Recon{RGB.RESET}
 {RGB.SECONDARY}[07]{RGB.RESET} {RGB.WHITE}MAC Address Vendor Lookup{RGB.RESET}
 {RGB.SECONDARY}[08]{RGB.RESET} {RGB.WHITE}URL Unshortener & Redirect Tracer{RGB.RESET}
 {RGB.ACCENT}[09]{RGB.RESET} {RGB.WHITE}DNS Record Scanner (A, MX, TXT){RGB.RESET} 
 {RGB.ACCENT}[10]{RGB.RESET} {RGB.WHITE}WHOIS Domain Intelligence Lookup{RGB.RESET}
 {RGB.ACCENT}[11]{RGB.RESET} {RGB.WHITE}Hash & Crypto Generator (MD5/SHA256){RGB.RESET}
 {RGB.PRIMARY}[12]{RGB.RESET} {RGB.BOLD}{RGB.WHITE}SUNTIK SOSMED{RGB.RESET} 
 {RGB.GRAY}[99]{RGB.RESET} {RGB.ACCENT}Edit Tema Warna (RGB Settings){RGB.RESET}
 {RGB.DANGER}[00]{RGB.RESET} {RGB.DANGER}Exit Session{RGB.RESET}
"""
    print(menu)

# ==========================================
# ⚙️ KONFIGURASI API OSINT & SMM PANEL
# ==========================================
KMSP_HEADERS = {
    "Authorization": "Basic c2lkb21wdWxhcGk6YXBpZ3drbXNw",
    "X-API-Key": "60ef29aa-a648-4668-90ae-20951ef90c55",
    "X-App-Version": "4.0.0",
    "User-Agent": "Mozilla/5.0"
}

# ⚠️ UBAH DATA SMM PANEL ANDA DI BAWAH INI
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
# 🎨 MODUL 99: RGB THEME SETTINGS
# ==========================================
def run_color_settings():
    print(f"\n{RGB.ACCENT}[*] RGB THEME EDITOR{RGB.RESET}")
    print(f" {RGB.PRIMARY}[1]{RGB.RESET} Mode Hacker (Matrix Green)")
    print(f" {RGB.PRIMARY}[2]{RGB.RESET} Mode Cyberpunk (Neon Pink & Cyan)")
    print(f" {RGB.PRIMARY}[3]{RGB.RESET} Mode Dark Blood (Crimson & Gray)")
    print(f" {RGB.PRIMARY}[4]{RGB.RESET} Custom RGB Manual")
    
    c = input(f"\n{RGB.SECONDARY}[?] Pilih tema (1-4): {RGB.RESET}").strip()
    
    if c == '1':
        RGB.set_color('PRIMARY', 0, 255, 0); RGB.set_color('SECONDARY', 0, 180, 0); RGB.set_color('ACCENT', 200, 255, 0)
    elif c == '2':
        RGB.set_color('PRIMARY', 255, 0, 150); RGB.set_color('SECONDARY', 0, 255, 255); RGB.set_color('ACCENT', 255, 255, 0)
    elif c == '3':
        RGB.set_color('PRIMARY', 220, 20, 60); RGB.set_color('SECONDARY', 150, 150, 150); RGB.set_color('ACCENT', 255, 100, 100)
    elif c == '4':
        print(f"\n{RGB.GRAY}[!] Masukkan nilai Red,Green,Blue (0-255) dipisah koma. Contoh: 255,0,0{RGB.RESET}")
        try:
            p = input(f"{RGB.SECONDARY}[?] Warna Utama (PRIMARY): {RGB.RESET}").strip()
            r, g, b = map(int, p.split(','))
            RGB.set_color('PRIMARY', r, g, b)
            
            s = input(f"{RGB.SECONDARY}[?] Warna Teks (SECONDARY): {RGB.RESET}").strip()
            r, g, b = map(int, s.split(','))
            RGB.set_color('SECONDARY', r, g, b)
        except:
            print(f"{RGB.DANGER}[!] Format salah, dibatalkan.{RGB.RESET}"); return
    else: return
    print(f"\n{RGB.PRIMARY}[+] Tema Terminal Berhasil Diubah!{RGB.RESET}")
    time.sleep(1)

# ==========================================
# 🛒 MODUL 12: SMM PANEL INTEGRATION
# ==========================================
def call_smm_api(action, **kwargs):
    if SMM_API_KEY == "API_KEY_ANDA_DISINI":
        print(f"{RGB.DANGER}[!] SMM_API_KEY dan SMM_SECRET_KEY belum disetting di dalam script!{RGB.RESET}")
        return None
    
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
        print(f"{RGB.DANGER}[!] Koneksi API SMM Gagal / Timeout: {e}{RGB.RESET}")
        return None

def run_smm_panel():
    while True:
        clear_screen()
        print(f"{RGB.PRIMARY}{RGB.BOLD}═════════════════[ SUNTIK SOSMED BY DOCTOR BARMODS ]═════════════════{RGB.RESET}")
        smm_menu = f"""
 {RGB.ACCENT}[1]{RGB.RESET} Cek Profil & Saldo Akun
 {RGB.ACCENT}[2]{RGB.RESET} Lihat Daftar Layanan (Dashboard Pages & Search)
 {RGB.ACCENT}[3]{RGB.RESET} Buat Pesanan Baru (Order)
 {RGB.ACCENT}[4]{RGB.RESET} Cek Status Pesanan (Order Status)
 {RGB.ACCENT}[5]{RGB.RESET} Request Refill Layanan
 {RGB.ACCENT}[6]{RGB.RESET} Cek Status Refill
 {RGB.DANGER}[0]{RGB.RESET} Kembali ke Menu Utama
"""
        print(smm_menu)
        pilihan = input(f"{RGB.SECONDARY}[?] Pilih menu SMM: {RGB.RESET}").strip()

        if pilihan == '1':
            data = call_smm_api("profile")
            if data:
                if data.get("status"):
                    d = data.get("data", {})
                    print(f"\n{RGB.PRIMARY}[+] PROFIL SMM BERHASIL DIAMBIL{RGB.RESET}")
                    print(f" ├─ Username : {RGB.BOLD}{d.get('username')}{RGB.RESET}")
                    print(f" ├─ Full Name: {d.get('full_name')}")
                    print(f" ├─ Email    : {d.get('email')}")
                    print(f" └─ Saldo    : {RGB.ACCENT}Rp {d.get('balance')}{RGB.RESET}")
                else:
                    print(f"\n{RGB.DANGER}[!] Gagal: {data.get('data', {}).get('msg')}{RGB.RESET}")

        elif pilihan == '2':
            print(f"\n{RGB.ACCENT}[*] Mengambil seluruh data layanan dari server...{RGB.RESET}")
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
                    print(f"\n{RGB.PRIMARY}[+] DAFTAR LAYANAN SMM (Ditemukan: {total_services} | Hal: {current_page+1}/{total_pages}){RGB.RESET}")
                    print(f"{RGB.GRAY} ID    | Harga    | Nama Layanan{RGB.RESET}")
                    print(f"{RGB.GRAY} ──────┼──────────┼──────────────────────────────────────────────────{RGB.RESET}")
                    
                    start_idx = current_page * items_per_page
                    end_idx = start_idx + items_per_page
                    
                    for s in filtered_services[start_idx:end_idx]:
                        s_id = str(s.get('id', ''))
                        s_price = f"Rp{s.get('price', '')}"
                        s_name = str(s.get('name', ''))
                        if len(s_name) > 48: s_name = s_name[:45] + "..."
                        print(f" {RGB.ACCENT}{s_id:<5}{RGB.RESET} | {RGB.WHITE}{s_price:<8}{RGB.RESET} | {s_name}")
                    
                    print(f"{RGB.GRAY} ──────┴──────────┴──────────────────────────────────────────────────{RGB.RESET}")
                    print(f" {RGB.ACCENT}[N]{RGB.RESET} Next   {RGB.ACCENT}[P]{RGB.RESET} Prev   {RGB.PRIMARY}[S]{RGB.RESET} Search   {RGB.GRAY}[R]{RGB.RESET} Reset Search   {RGB.DANGER}[Q]{RGB.RESET} Quit")
                    
                    nav = input(f"\n{RGB.SECONDARY}[?] Pilih aksi (N/P/S/R/Q): {RGB.RESET}").strip().lower()
                    
                    if nav == 'n':
                        if current_page < total_pages - 1: current_page += 1
                        else:
                            print(f"{RGB.DANGER}[!] Ini halaman terakhir.{RGB.RESET}")
                            time.sleep(0.5)
                    elif nav == 'p':
                        if current_page > 0: current_page -= 1
                        else:
                            print(f"{RGB.DANGER}[!] Ini halaman pertama.{RGB.RESET}")
                            time.sleep(0.5)
                    elif nav == 's':
                        kw = input(f"{RGB.SECONDARY}[?] Masukkan kata pencarian (misal: instagram): {RGB.RESET}").strip().lower()
                        filtered_services = [s for s in all_services if kw in str(s.get('name', '')).lower()]
                        current_page = 0
                    elif nav == 'r':
                        filtered_services = all_services
                        current_page = 0
                    elif nav == 'q':
                        break
                    else:
                        print(f"{RGB.DANGER}[!] Input tidak valid.{RGB.RESET}")
                        time.sleep(0.5)
                continue
            
            elif data:
                print(f"\n{RGB.DANGER}[!] Gagal: {data.get('data', {}).get('msg')}{RGB.RESET}")

        elif pilihan == '3':
            print(f"\n{RGB.ACCENT}[*] PEMESANAN BARU{RGB.RESET}")
            svc = input(f" {RGB.SECONDARY}├─ Masukkan ID Service: {RGB.RESET}").strip()
            tgt = input(f" {RGB.SECONDARY}├─ Target (URL/Username): {RGB.RESET}").strip()
            qty = input(f" {RGB.SECONDARY}└─ Jumlah (Quantity): {RGB.RESET}").strip()
            
            data = call_smm_api("order", service=svc, data=tgt, quantity=qty)
            if data:
                if data.get("status"):
                    print(f"\n{RGB.PRIMARY}[+] PESANAN BERHASIL DIBUAT{RGB.RESET}")
                    print(f" └─ Order ID : {RGB.BOLD}{data.get('data', {}).get('id')}{RGB.RESET}")
                else:
                    print(f"\n{RGB.DANGER}[!] Order Gagal: {data.get('data', {}).get('msg')}{RGB.RESET}")

        elif pilihan == '4':
            oid = input(f"\n{RGB.SECONDARY}[?] Masukkan Order ID: {RGB.RESET}").strip()
            data = call_smm_api("status", id=oid)
            if data:
                if data.get("status"):
                    d = data.get("data", {})
                    print(f"\n{RGB.PRIMARY}[+] STATUS PESANAN (ID: {oid}){RGB.RESET}")
                    print(f" ├─ Status     : {RGB.BOLD}{d.get('status')}{RGB.RESET}")
                    print(f" ├─ Start Count: {d.get('start_count')}")
                    print(f" └─ Remains    : {d.get('remains')}")
                else:
                    print(f"\n{RGB.DANGER}[!] Gagal: {data.get('data', {}).get('msg')}{RGB.RESET}")

        elif pilihan == '5':
            oid = input(f"\n{RGB.SECONDARY}[?] Masukkan Order ID yang akan di-Refill: {RGB.RESET}").strip()
            data = call_smm_api("refill", order=oid)
            if data:
                if data.get("status"):
                    d = data.get("data", [])[0] if data.get("data") else {}
                    print(f"\n{RGB.PRIMARY}[+] REFILL BERHASIL DIREQUEST{RGB.RESET}")
                    print(f" └─ Refill ID : {RGB.BOLD}{d.get('refill')}{RGB.RESET}")
                else:
                    d = data.get("data", [])[0] if data.get("data") else {}
                    print(f"\n{RGB.DANGER}[!] Refill Gagal: {d.get('msg', 'Permintaan tidak sesuai')}{RGB.RESET}")

        elif pilihan == '6':
            rid = input(f"\n{RGB.SECONDARY}[?] Masukkan Refill ID: {RGB.RESET}").strip()
            data = call_smm_api("refill_status", refill=rid)
            if data:
                if data.get("status"):
                    d = data.get("data", [])[0] if data.get("data") else {}
                    print(f"\n{RGB.PRIMARY}[+] STATUS REFILL (ID: {rid}){RGB.RESET}")
                    print(f" └─ Status : {RGB.BOLD}{d.get('status')}{RGB.RESET}")
                else:
                    d = data.get("data", [])[0] if data.get("data") else {}
                    print(f"\n{RGB.DANGER}[!] Gagal: {d.get('msg', 'Refill Id Tidak Ditemukan')}{RGB.RESET}")

        elif pilihan == '0':
            print(f"\n{RGB.GRAY}[*] Kembali ke menu utama...{RGB.RESET}")
            time.sleep(0.5)
            break
        else:
            print(f"{RGB.DANGER}[!] Pilihan tidak valid.{RGB.RESET}")

        input(f"\n{RGB.GRAY}[Tekan ENTER untuk kembali ke Menu SMM]{RGB.RESET}")

# ==========================================
# 📡 MODUL OSINT & NET UTILS (1 - 11)
# ==========================================
def run_telco_recon():
    raw_num = input(f"\n{RGB.SECONDARY}[?] Masukkan Nomor Target (08xxx): {RGB.RESET}").strip()
    msisdn = normalize_number(raw_num)
    if not msisdn:
        print(f"{RGB.DANGER}[!] Format nomor tidak valid.{RGB.RESET}")
        return

    print(f"{RGB.ACCENT}[*] Penetrasi data target {msisdn}...{RGB.RESET}")
    
    try:
        url_bendith = f"https://bendith.my.id/end.php?check=package&number={msisdn}&version=2"
        b_res = requests.get(url_bendith, timeout=12).json()
        if b_res.get("success") and b_res.get("data", {}).get("subs_info"):
            info = b_res["data"].get("subs_info", {})
            pkgs = b_res["data"].get("package_info", {}).get("packages", [])
            
            print(f"\n{RGB.PRIMARY}[+] TELCO RECON SUCCESS (BENDITH ENGINE){RGB.RESET}")
            print(f" ├─ Target       : {msisdn}")
            print(f" ├─ Provider     : {info.get('operator', 'XL')}")
            print(f" ├─ Network      : {info.get('net_type', '-')}")
            print(f" ├─ Masa Aktif   : {info.get('exp_date', '-')}")
            print(f" └─ Masa Tenggang: {info.get('grace_until', '-')}\n")
            
            if pkgs:
                print(f"{RGB.ACCENT}📊 DETAIL PAKET & KUOTA:{RGB.RESET}")
                for p in pkgs:
                    print(f"{RGB.SECONDARY} ┌─ {p.get('name', '-')} (Exp: {p.get('expiry', '-')}){RGB.RESET}")
                    for q in p.get("quotas", []):
                        print(f" │  └─ {q.get('name', '-')}: {RGB.PRIMARY}{q.get('remaining', '-')} / {q.get('total', '-')}{RGB.RESET}")
            return
    except:
        pass

    print(f"{RGB.ACCENT}[*] Rerouting payload ke KMSP Engine...{RGB.RESET}")
    try:
        url_kmsp = "https://apigw.kmsp-store.com/sidompul/v4/cek_kuota"
        k_res = requests.get(url_kmsp, headers=KMSP_HEADERS, params={"msisdn": msisdn, "isJSON": "true"}, timeout=15).json()
        if k_res.get("status"):
            sp = k_res.get("data", {}).get("data_sp", {})
            raw_hasil = k_res.get("data", {}).get("hasil", "")
            
            print(f"\n{RGB.PRIMARY}[+] TELCO RECON SUCCESS (KMSP ENGINE){RGB.RESET}")
            print(f" ├─ Target       : {msisdn}")
            print(f" ├─ Provider     : {sp.get('prefix', {}).get('value', 'XL')}")
            print(f" ├─ 4G Status    : {sp.get('status_4g', {}).get('value', '-')}")
            print(f" ├─ Masa Aktif   : {sp.get('active_period', {}).get('value', '-')}")
            print(f" └─ Masa Tenggang: {sp.get('grace_period', {}).get('value', '-')}\n")
            
            if raw_hasil:
                print(f"{RGB.ACCENT}📊 DETAIL PAKET & KUOTA:{RGB.RESET}")
                clean_txt = clean_html(raw_hasil)
                sections = re.split(r'(?=🎁 Quota:|🎁 Benefit:)', clean_txt)
                for sec in sections:
                    if sec.strip(): 
                        print(f"{RGB.SECONDARY}{sec.strip()}{RGB.RESET}\n")
            else:
                print(f"{RGB.GRAY}[!] Tidak ada rincian paket di API KMSP.{RGB.RESET}")
            return
    except:
        pass
    print(f"{RGB.DANGER}[!] Target gagal dilacak atau nomor tidak aktif.{RGB.RESET}")

def run_ip_recon():
    target = input(f"\n{RGB.SECONDARY}[?] Masukkan IP Address / Domain: {RGB.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    if not target_clean: return
    print(f"{RGB.ACCENT}[*] Tracing network metadata...{RGB.RESET}")
    try:
        res = requests.get(f"http://ip-api.com/json/{target_clean}?fields=status,country,city,isp,as,query,lat,lon", timeout=10).json()
        if res.get("status") == "success":
            print(f"\n{RGB.PRIMARY}[+] GEO-IP INTELLIGENCE ACQUIRED{RGB.RESET}")
            print(f" ├─ IP / Domain  : {res.get('query')}")
            print(f" ├─ Location     : {res.get('city')}, {res.get('country')}")
            print(f" ├─ ISP / ASN    : {res.get('isp')} / {res.get('as')}")
            print(f" └─ Coordinates  : {res.get('lat')}, {res.get('lon')}")
        else:
            print(f"{RGB.DANGER}[!] Gagal mendapatkan data IP.{RGB.RESET}")
    except:
        print(f"{RGB.DANGER}[!] API Timeout.{RGB.RESET}")

def run_subdomain_recon():
    target = input(f"\n{RGB.SECONDARY}[?] Masukkan Domain Utama: {RGB.RESET}").strip()
    domain = re.sub(r'^https?://', '', target).split('/')[0]
    if not domain: return
    print(f"{RGB.ACCENT}[*] Mining SSL logs via crt.sh...{RGB.RESET}")
    try:
        res = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=20)
        if res.status_code == 200:
            subdomains = {name.strip().lower() for item in res.json() for name in item.get('name_value', '').split('\n') if name.strip().lower().endswith(domain) and '*' not in name}
            print(f"\n{RGB.PRIMARY}[+] Ditemukan {len(subdomains)} Subdomain Terdaftar:{RGB.RESET}")
            for sub in sorted(subdomains)[:30]: print(f" {RGB.SECONDARY}└─ {sub}{RGB.RESET}")
            if len(subdomains) > 30: print(f" {RGB.ACCENT}... dan {len(subdomains)-30} lainnya.{RGB.RESET}")
    except:
        print(f"{RGB.DANGER}[!] Gagal terkoneksi ke crt.sh.{RGB.RESET}")

def run_github_recon():
    username = input(f"\n{RGB.SECONDARY}[?] Masukkan Username GitHub Target: {RGB.RESET}").strip()
    try:
        res = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        if res.status_code == 200:
            data = res.json()
            print(f"\n{RGB.PRIMARY}[+] GITHUB PROFILE IDENTIFIED{RGB.RESET}")
            print(f" ├─ Nama Lengkap : {data.get('name', '-')}")
            print(f" ├─ Public Email : {data.get('email', 'Hidden')}")
            print(f" ├─ Lokasi       : {data.get('location', '-')}")
            print(f" └─ Repositori   : {data.get('public_repos', 0)} Repos")
    except:
        print(f"{RGB.DANGER}[!] Gagal melacak profil.{RGB.RESET}")

def run_port_scanner():
    target = input(f"\n{RGB.SECONDARY}[?] Masukkan IP/Domain Target: {RGB.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    COMMON_PORTS = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MYSQL"}
    try:
        ip = socket.gethostbyname(target_clean)
        print(f"{RGB.ACCENT}[*] Scanning {target_clean} ({ip})...{RGB.RESET}")
        for port, service in COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                print(f" {RGB.PRIMARY}[+] Port {port:<5} [OPEN]{RGB.RESET} -> {service}")
            sock.close()
    except:
        print(f"{RGB.DANGER}[!] Gagal melakukan scan port.{RGB.RESET}")

def run_header_grabber():
    target = input(f"\n{RGB.SECONDARY}[?] URL Website Target: {RGB.RESET}").strip()
    if not target.startswith('http'): target = 'http://' + target
    print(f"{RGB.ACCENT}[*] Menarik HTTP Headers...{RGB.RESET}")
    try:
        res = requests.head(target, timeout=10, allow_redirects=True, headers=KMSP_HEADERS)
        print(f"\n{RGB.PRIMARY}[+] HTTP HEADERS ACQUIRED{RGB.RESET}")
        print(f" ├─ Server Tech  : {res.headers.get('Server', 'Unknown')}")
        print(f" ├─ X-Powered-By : {res.headers.get('X-Powered-By', 'Unknown')}")
        print(f" └─ Content-Type : {res.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"{RGB.DANGER}[!] Gagal terhubung: {e}{RGB.RESET}")

def run_mac_lookup():
    mac = input(f"\n{RGB.SECONDARY}[?] MAC Address (00:11:22:33:44:55): {RGB.RESET}").strip()
    try:
        res = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)
        if res.status_code == 200:
            print(f"\n{RGB.PRIMARY}[+] MAC VENDOR IDENTIFIED{RGB.RESET}")
            print(f" └─ Vendor : {RGB.BOLD}{res.text}{RGB.RESET}")
        else:
            print(f"{RGB.DANGER}[!] MAC Address tidak ditemukan.{RGB.RESET}")
    except:
        print(f"{RGB.DANGER}[!] Koneksi gagal.{RGB.RESET}")

def run_url_unshortener():
    url = input(f"\n{RGB.SECONDARY}[?] URL Pendek (bit.ly/xxx): {RGB.RESET}").strip()
    if not url.startswith('http'): url = 'http://' + url
    try:
        res = requests.Session().head(url, allow_redirects=True, timeout=10)
        print(f"\n{RGB.PRIMARY}[+] URL REDIRECT TRACED{RGB.RESET}")
        print(f" └─ URL Asli : {RGB.BOLD}{res.url}{RGB.RESET}")
    except Exception as e:
        print(f"{RGB.DANGER}[!] Tracing gagal: {e}{RGB.RESET}")

def run_dns_scanner():
    target = input(f"\n{RGB.SECONDARY}[?] Masukkan Domain Target: {RGB.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    print(f"{RGB.ACCENT}[*] Querying DNS Records...{RGB.RESET}")
    try:
        res = requests.get(f"https://networkcalc.com/api/dns/lookup/{target_clean}", timeout=15).json()
        if res.get("status") == "OK":
            records = res.get("records", {})
            print(f"\n{RGB.PRIMARY}[+] DNS RECORDS AQUIRED{RGB.RESET}")
            if records.get("A"):
                print(f" {RGB.ACCENT}├─ [A] Records (IPv4):{RGB.RESET}")
                for r in records["A"]: print(f" │  └─ {r['address']}")
            if records.get("MX"):
                print(f" {RGB.ACCENT}├─ [MX] Mail Servers:{RGB.RESET}")
                for r in records["MX"]: print(f" │  └─ {r['exchange']} (Priority: {r['priority']})")
            if records.get("TXT"):
                print(f" {RGB.ACCENT}└─ [TXT] Verifications:{RGB.RESET}")
                for r in records["TXT"]: print(f"    └─ {r[:60]}...")
        else:
            print(f"{RGB.DANGER}[!] Gagal mengambil data DNS.{RGB.RESET}")
    except Exception as e:
        print(f"{RGB.DANGER}[!] API Error: {e}{RGB.RESET}")

def run_whois_lookup():
    target = input(f"\n{RGB.SECONDARY}[?] Masukkan Domain Target: {RGB.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    print(f"{RGB.ACCENT}[*] Mengambil data kepemilikan domain (WHOIS)...{RGB.RESET}")
    try:
        res = requests.get(f"https://networkcalc.com/api/dns/whois/{target_clean}", timeout=15).json()
        if res.get("status") == "OK" and res.get("whois"):
            w = res["whois"]
            print(f"\n{RGB.PRIMARY}[+] WHOIS DATA ACQUIRED{RGB.RESET}")
            print(f" ├─ Domain       : {target_clean}")
            print(f" ├─ Registrar    : {w.get('registrar', 'Hidden')}")
            print(f" ├─ Dibuat Pada  : {w.get('creation_date', '-')}")
            print(f" ├─ Berakhir Pada: {w.get('expiration_date', '-')}")
            servers = w.get("name_servers")
            if servers: print(f" └─ Name Servers : {servers[0] if servers else '-'}")
        else:
            print(f"{RGB.DANGER}[!] Data WHOIS diproteksi atau tidak ditemukan.{RGB.RESET}")
    except Exception as e:
        print(f"{RGB.DANGER}[!] API Error: {e}{RGB.RESET}")

def run_hash_generator():
    text = input(f"\n{RGB.SECONDARY}[?] Masukkan Text/String: {RGB.RESET}")
    if not text: return
    print(f"\n{RGB.PRIMARY}[+] CRYPTOGRAPHY HASH GENERATED{RGB.RESET}")
    print(f" {RGB.ACCENT}├─ MD5   :{RGB.RESET} {hashlib.md5(text.encode()).hexdigest()}")
    print(f" {RGB.ACCENT}├─ SHA1  :{RGB.RESET} {hashlib.sha1(text.encode()).hexdigest()}")
    print(f" {RGB.ACCENT}└─ SHA256:{RGB.RESET} {hashlib.sha256(text.encode()).hexdigest()}")

# ==========================================
# 🔄 MAIN LOOP
# ==========================================
def main():
    while True:
        try:
            print_banner()
            print_menu()
            choice = input(f"{RGB.DANGER}root@dr-barmods{RGB.RESET}:{RGB.SECONDARY}~# {RGB.RESET}").strip()

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
                print(f"\n{RGB.ACCENT}[*] Session terminated by user.{RGB.RESET}")
                break
            else:
                continue

            input(f"\n{RGB.GRAY}[Tekan ENTER untuk kembali ke Menu Utama]{RGB.RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{RGB.ACCENT}[*] Session aborted. Keluar...{RGB.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
