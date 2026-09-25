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
        """Fungsi untuk mengubah warna RGB secara dinamis"""
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
    # Banner menggunakan PRIMARY dan SECONDARY agar ikut berubah saat tema diganti
    banner = f"""{RGB.PRIMARY}{RGB.BOLD}
  ██████  ███████ ██ ███    ██ ████████ 
 ██    ██ ██      ██ ████   ██    ██    
 ██    ██ ███████ ██ ██ ██  ██    ██    
 ██    ██      ██ ██ ██  ██ ██    ██    
  ██████  ███████ ██ ██   ████    ██    
{RGB.SECONDARY}
 ╭──────────────────────────────────────────────────────────╮
 │ [>] TOOL     : MULTI-PURPOSE OSINT RECON FRAMEWORK       │
 │ [>] CODER    : DOCTOR BARMODS (BARMODS STORE)            │
 │ [>] VERSION  : 5.1.0 (DYNAMIC RGB + FULL QUOTA ENGINE)   │
 ╰──────────────────────────────────────────────────────────╯{RGB.RESET}
"""
    typing_print(banner)

def print_menu():
    menu = f"""{RGB.ACCENT}[ MENU SELECTION ]{RGB.RESET}
 {RGB.PRIMARY}[01]{RGB.RESET} {RGB.WHITE}XL / Axis Telco & Kuota Tracer (Full Info){RGB.RESET}
 {RGB.PRIMARY}[02]{RGB.RESET} {RGB.WHITE}IP & Domain Geolocation / ASN Lookup{RGB.RESET}
 {RGB.PRIMARY}[03]{RGB.RESET} {RGB.WHITE}Subdomain Certificate Recon (crt.sh){RGB.RESET}
 {RGB.PRIMARY}[04]{RGB.RESET} {RGB.WHITE}GitHub Target Intelligence{RGB.RESET}
 {RGB.PRIMARY}[05]{RGB.RESET} {RGB.WHITE}Stealth Network Port Scanner{RGB.RESET}
 {RGB.SECONDARY}[06]{RGB.RESET} {RGB.GRAY}HTTP Header Grabber & Tech Recon{RGB.RESET}
 {RGB.SECONDARY}[07]{RGB.RESET} {RGB.GRAY}MAC Address Vendor Lookup{RGB.RESET}
 {RGB.SECONDARY}[08]{RGB.RESET} {RGB.GRAY}URL Unshortener & Redirect Tracer{RGB.RESET}
 {RGB.ACCENT}[09]{RGB.RESET} {RGB.WHITE}DNS Record Scanner (A, MX, TXT){RGB.RESET} 
 {RGB.ACCENT}[10]{RGB.RESET} {RGB.WHITE}WHOIS Domain Intelligence Lookup{RGB.RESET}
 {RGB.ACCENT}[11]{RGB.RESET} {RGB.WHITE}Hash & Crypto Generator (MD5/SHA256){RGB.RESET}
 {RGB.GRAY}[99]{RGB.RESET} {RGB.ACCENT}Edit Tema Warna (RGB Settings){RGB.RESET}
 {RGB.DANGER}[00]{RGB.RESET} {RGB.DANGER}Exit Session{RGB.RESET}
"""
    print(menu)

# ==========================================
# ⚙️ KONFIGURASI ENGINE
# ==========================================
KMSP_HEADERS = {
    "Authorization": "Basic c2lkb21wdWxhcGk6YXBpZ3drbXNw",
    "X-API-Key": "60ef29aa-a648-4668-90ae-20951ef90c55",
    "X-App-Version": "4.0.0",
    "User-Agent": "Mozilla/5.0"
}

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
        RGB.set_color('PRIMARY', 0, 255, 0)
        RGB.set_color('SECONDARY', 0, 180, 0)
        RGB.set_color('ACCENT', 200, 255, 0)
    elif c == '2':
        RGB.set_color('PRIMARY', 255, 0, 150)
        RGB.set_color('SECONDARY', 0, 255, 255)
        RGB.set_color('ACCENT', 255, 255, 0)
    elif c == '3':
        RGB.set_color('PRIMARY', 220, 20, 60)
        RGB.set_color('SECONDARY', 150, 150, 150)
        RGB.set_color('ACCENT', 255, 100, 100)
    elif c == '4':
        print(f"\n{RGB.GRAY}[!] Masukkan nilai Red,Green,Blue (0-255) dipisah koma. Contoh: 255,0,0{RGB.RESET}")
        try:
            p = input(f"{RGB.SECONDARY}[?] Warna Utama / Banner (PRIMARY): {RGB.RESET}").strip()
            r, g, b = map(int, p.split(','))
            RGB.set_color('PRIMARY', r, g, b)
            
            s = input(f"{RGB.SECONDARY}[?] Warna Garis / Teks (SECONDARY): {RGB.RESET}").strip()
            r, g, b = map(int, s.split(','))
            RGB.set_color('SECONDARY', r, g, b)
        except Exception:
            print(f"{RGB.DANGER}[!] Format salah, dibatalkan. Pastikan menggunakan format R,G,B{RGB.RESET}")
            return
    else:
        return
        
    print(f"\n{RGB.PRIMARY}[+] Tema Terminal Berhasil Diubah!{RGB.RESET}")
    time.sleep(1)

# ==========================================
# 📡 MODUL 1 - 5 (ORIGINAL OSINT & TELCO)
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

# ==========================================
# 🚀 MODUL 6 - 8 (HTTP & NET UTILS)
# ==========================================
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

# ==========================================
# 💎 MODUL 9 - 11 (NEW FEATURES)
# ==========================================
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
            if servers:
                print(f" └─ Name Servers : {servers[0] if servers else '-'}")
        else:
            print(f"{RGB.DANGER}[!] Data WHOIS diproteksi atau tidak ditemukan.{RGB.RESET}")
    except Exception as e:
        print(f"{RGB.DANGER}[!] API Error: {e}{RGB.RESET}")

def run_hash_generator():
    text = input(f"\n{RGB.SECONDARY}[?] Masukkan Text/String: {RGB.RESET}")
    if not text: return
    
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    
    print(f"\n{RGB.PRIMARY}[+] CRYPTOGRAPHY HASH GENERATED{RGB.RESET}")
    print(f" {RGB.ACCENT}├─ MD5   :{RGB.RESET} {md5_hash}")
    print(f" {RGB.ACCENT}├─ SHA1  :{RGB.RESET} {sha1_hash}")
    print(f" {RGB.ACCENT}└─ SHA256:{RGB.RESET} {sha256_hash}")

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
