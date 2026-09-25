import os
import re
import sys
import time
import socket
import requests

# ==========================================
# 🎨 COLOR & TERMINAL ENGINE
# ==========================================
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text, speed=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_banner():
    clear_screen()
    banner = f"""{Colors.RED}{Colors.BOLD}
  ██████  ███████ ██ ███    ██ ████████ 
 ██    ██ ██      ██ ████   ██    ██    
 ██    ██ ███████ ██ ██ ██  ██    ██    
 ██    ██      ██ ██ ██  ██ ██    ██    
  ██████  ███████ ██ ██   ████    ██    
{Colors.CYAN}
 ╔══════════════════════════════════════════════════════════╗
 ║ [>] TOOL     : MULTI-PURPOSE OSINT RECON FRAMEWORK       ║
 ║ [>] CODER    : DOCTOR BARMODS (BARMODS STORE)            ║
 ║ [>] VERSION  : 4.4.0 (EXTENDED FREE OSINT EDITION)       ║
 ╚══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    typing_print(banner)

def print_menu():
    menu = f"""{Colors.YELLOW}[ MENU SELECTION ]{Colors.RESET}
 {Colors.GREEN}[01]{Colors.RESET} XL / Axis Telco & Kuota Tracer
 {Colors.GREEN}[02]{Colors.RESET} IP & Domain Geolocation / ASN Lookup
 {Colors.GREEN}[03]{Colors.RESET} Subdomain Certificate Recon (crt.sh)
 {Colors.GREEN}[04]{Colors.RESET} GitHub Target Intelligence
 {Colors.GREEN}[05]{Colors.RESET} Stealth Network Port Scanner
 {Colors.CYAN}[06]{Colors.RESET} HTTP Header Grabber & Tech Recon
 {Colors.CYAN}[07]{Colors.RESET} MAC Address Vendor Lookup
 {Colors.CYAN}[08]{Colors.RESET} URL Unshortener & Redirect Tracer
 {Colors.RED}[00]{Colors.RESET} Exit Session
"""
    print(menu)

# ==========================================
# ⚙️ KONFIGURASI ENGINE
# ==========================================
KMSP_HEADERS = {
    "Authorization": "Basic c2lkb21wdWxhcGk6YXBpZ3drbXNw",
    "X-API-Key": "60ef29aa-a648-4668-90ae-20951ef90c55",
    "X-App-Version": "4.0.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
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
# 📡 MODUL 1 - 5 (ORIGINAL OSINT)
# ==========================================
def run_telco_recon():
    raw_num = input(f"\n{Colors.CYAN}[?] Masukkan Nomor Target (08xxx): {Colors.RESET}").strip()
    msisdn = normalize_number(raw_num)
    if not msisdn:
        print(f"{Colors.RED}[!] Format nomor tidak valid.{Colors.RESET}")
        return

    print(f"{Colors.YELLOW}[*] Penetrasi data target {msisdn}...{Colors.RESET}")
    try:
        url_bendith = f"https://bendith.my.id/end.php?check=package&number={msisdn}&version=2"
        b_res = requests.get(url_bendith, timeout=12).json()
        if b_res.get("success") and b_res.get("data", {}).get("subs_info"):
            info = b_res["data"].get("subs_info", {})
            print(f"\n{Colors.GREEN}[+] TELCO RECON SUCCESS (BENDITH ENGINE){Colors.RESET}")
            print(f" ├─ Target       : {msisdn}")
            print(f" ├─ Provider     : {info.get('operator', 'XL')}")
            print(f" ├─ Masa Aktif   : {info.get('exp_date', '-')}")
            print(f" └─ Masa Tenggang: {info.get('grace_until', '-')}\n")
            return
    except:
        pass

    print(f"{Colors.YELLOW}[*] Rerouting payload ke KMSP Engine...{Colors.RESET}")
    try:
        url_kmsp = "https://apigw.kmsp-store.com/sidompul/v4/cek_kuota"
        k_res = requests.get(url_kmsp, headers=KMSP_HEADERS, params={"msisdn": msisdn, "isJSON": "true"}, timeout=15).json()
        if k_res.get("status"):
            sp = k_res.get("data", {}).get("data_sp", {})
            print(f"\n{Colors.GREEN}[+] TELCO RECON SUCCESS (KMSP ENGINE){Colors.RESET}")
            print(f" ├─ Target       : {msisdn}")
            print(f" ├─ Provider     : {sp.get('prefix', {}).get('value', 'XL')}")
            print(f" ├─ Masa Aktif   : {sp.get('active_period', {}).get('value', '-')}")
            print(f" └─ Masa Tenggang: {sp.get('grace_period', {}).get('value', '-')}\n")
            return
    except:
        pass
    print(f"{Colors.RED}[!] Target gagal dilacak atau nomor tidak aktif.{Colors.RESET}")

def run_ip_recon():
    target = input(f"\n{Colors.CYAN}[?] Masukkan IP Address / Domain: {Colors.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    if not target_clean: return
    try:
        res = requests.get(f"http://ip-api.com/json/{target_clean}?fields=status,country,city,isp,as,query,lat,lon", timeout=10).json()
        if res.get("status") == "success":
            print(f"\n{Colors.GREEN}[+] GEO-IP INTELLIGENCE ACQUIRED{Colors.RESET}")
            print(f" ├─ IP / Domain  : {res.get('query')}")
            print(f" ├─ Location     : {res.get('city')}, {res.get('country')}")
            print(f" ├─ ISP / ASN    : {res.get('isp')} / {res.get('as')}")
            print(f" └─ Coordinates  : {res.get('lat')}, {res.get('lon')}")
        else:
            print(f"{Colors.RED}[!] Gagal mendapatkan data IP.{Colors.RESET}")
    except:
        print(f"{Colors.RED}[!] API Timeout.{Colors.RESET}")

def run_subdomain_recon():
    target = input(f"\n{Colors.CYAN}[?] Masukkan Domain Utama: {Colors.RESET}").strip()
    domain = re.sub(r'^https?://', '', target).split('/')[0]
    if not domain: return
    print(f"{Colors.YELLOW}[*] Mining SSL logs via crt.sh...{Colors.RESET}")
    try:
        res = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=20)
        if res.status_code == 200:
            subdomains = {name.strip().lower() for item in res.json() for name in item.get('name_value', '').split('\n') if name.strip().lower().endswith(domain) and '*' not in name}
            print(f"\n{Colors.GREEN}[+] Ditemukan {len(subdomains)} Subdomain Terdaftar:{Colors.RESET}")
            for sub in sorted(subdomains)[:30]: print(f" {Colors.CYAN}└─ {sub}{Colors.RESET}")
            if len(subdomains) > 30: print(f" {Colors.YELLOW}... dan {len(subdomains)-30} lainnya.{Colors.RESET}")
    except:
        print(f"{Colors.RED}[!] Gagal terkoneksi ke crt.sh.{Colors.RESET}")

def run_github_recon():
    username = input(f"\n{Colors.CYAN}[?] Masukkan Username GitHub Target: {Colors.RESET}").strip()
    try:
        res = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        if res.status_code == 200:
            data = res.json()
            print(f"\n{Colors.GREEN}[+] GITHUB PROFILE IDENTIFIED{Colors.RESET}")
            print(f" ├─ Nama Lengkap : {data.get('name', '-')}")
            print(f" ├─ Public Email : {data.get('email', 'Hidden')}")
            print(f" ├─ Lokasi       : {data.get('location', '-')}")
            print(f" └─ Bio          : {data.get('bio', '-')}")
    except:
        print(f"{Colors.RED}[!] Gagal melacak profil.{Colors.RESET}")

def run_port_scanner():
    target = input(f"\n{Colors.CYAN}[?] Masukkan IP/Domain Target: {Colors.RESET}").strip()
    target_clean = re.sub(r'^https?://', '', target).split('/')[0]
    COMMON_PORTS = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MYSQL"}
    try:
        ip = socket.gethostbyname(target_clean)
        print(f"{Colors.YELLOW}[*] Scanning {target_clean} ({ip})...{Colors.RESET}")
        for port, service in COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                print(f" {Colors.GREEN}[+] Port {port:<5} [OPEN]{Colors.RESET} -> {service}")
            sock.close()
    except:
        print(f"{Colors.RED}[!] Gagal melakukan scan port.{Colors.RESET}")

# ==========================================
# 🚀 MODUL 6 - 8 (NEW EXTENDED OSINT)
# ==========================================
def run_header_grabber():
    target = input(f"\n{Colors.CYAN}[?] Masukkan URL Website Target (misal: google.com): {Colors.RESET}").strip()
    if not target.startswith('http'):
        target = 'http://' + target
    
    print(f"{Colors.YELLOW}[*] Menarik HTTP Headers dari {target}...{Colors.RESET}")
    try:
        res = requests.head(target, timeout=10, allow_redirects=True, headers=KMSP_HEADERS)
        print(f"\n{Colors.GREEN}[+] HTTP HEADERS ACQUIRED{Colors.RESET}")
        print(f" ├─ URL Final    : {res.url}")
        print(f" ├─ Status Code  : {res.status_code}")
        print(f" ├─ Server Tech  : {res.headers.get('Server', 'Unknown / Hidden')}")
        print(f" ├─ X-Powered-By : {res.headers.get('X-Powered-By', 'Unknown / Hidden')}")
        print(f" └─ Content-Type : {res.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"{Colors.RED}[!] Gagal terhubung ke target: {e}{Colors.RESET}")

def run_mac_lookup():
    mac = input(f"\n{Colors.CYAN}[?] Masukkan MAC Address (misal: 00:11:22:33:44:55): {Colors.RESET}").strip()
    print(f"{Colors.YELLOW}[*] Mencocokkan MAC Address dengan database OUI...{Colors.RESET}")
    try:
        res = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)
        if res.status_code == 200:
            print(f"\n{Colors.GREEN}[+] MAC VENDOR IDENTIFIED{Colors.RESET}")
            print(f" ├─ MAC Address  : {mac.upper()}")
            print(f" └─ Vendor / OUI : {Colors.BOLD}{res.text}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] MAC Address tidak ditemukan dalam database publik.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Koneksi ke database vendor gagal: {e}{Colors.RESET}")

def run_url_unshortener():
    url = input(f"\n{Colors.CYAN}[?] Masukkan URL Pendek (misal: bit.ly/xxx): {Colors.RESET}").strip()
    if not url.startswith('http'):
        url = 'http://' + url
        
    print(f"{Colors.YELLOW}[*] Menelusuri rantai pengalihan (redirect) URL...{Colors.RESET}")
    try:
        # Menggunakan session agar bisa melacak history redirect
        session = requests.Session()
        res = session.head(url, allow_redirects=True, timeout=10)
        
        print(f"\n{Colors.GREEN}[+] URL REDIRECT TRACED{Colors.RESET}")
        print(f" ├─ URL Asal     : {url}")
        print(f" ├─ URL Asli     : {Colors.BOLD}{res.url}{Colors.RESET}")
        
        if len(res.history) > 0:
            print(f" └─ Jalur (Hops) :")
            for i, resp in enumerate(res.history, 1):
                print(f"    {i}. {resp.status_code} -> {resp.url}")
        else:
            print(f" └─ Keterangan   : Tidak ada pengalihan (Bukan URL pendek/redirect).")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Tracing gagal: {e}{Colors.RESET}")

# ==========================================
# 🔄 MAIN LOOP
# ==========================================
def main():
    while True:
        try:
            print_banner()
            print_menu()
            choice = input(f"{Colors.RED}root@dr-barmods{Colors.RESET}:{Colors.CYAN}~# {Colors.RESET}").strip()

            if choice in ['1', '01']: run_telco_recon()
            elif choice in ['2', '02']: run_ip_recon()
            elif choice in ['3', '03']: run_subdomain_recon()
            elif choice in ['4', '04']: run_github_recon()
            elif choice in ['5', '05']: run_port_scanner()
            elif choice in ['6', '06']: run_header_grabber()
            elif choice in ['7', '07']: run_mac_lookup()
            elif choice in ['8', '08']: run_url_unshortener()
            elif choice in ['0', '00', 'exit', 'quit']:
                print(f"\n{Colors.YELLOW}[*] Session terminated by user.{Colors.RESET}")
                break
            else:
                continue

            input(f"\n{Colors.YELLOW}[Tekan ENTER untuk kembali ke Menu Utama]{Colors.RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[*] Session aborted. Keluar...{Colors.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
