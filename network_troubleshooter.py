# Təməl Lojistik Şəbəkə və Altyapı Troubleshoot (Nasazlıq) Skripti

# 1. Şirkətin Daxili Şəbəkə Cihazlarının və Qoşulma Statuslarının Datası
sebeke_cihazlari = [
    {"cihaz": "Router-HQ", "ip": "192.168.1.1", "status": "Active", "kabel": "Straight-Through"},
    {"cihaz": "Switch-Customs", "ip": "192.168.1.2", "status": "Active", "kabel": "Straight-Through"},
    {"cihaz": "Warehouse-PC", "ip": "192.168.2.5", "status": "Error", "kabel": "Wrong Cable Type"},
    {"cihaz": "Backup-Gateway", "ip": "192.168.1.1", "status": "Active", "kabel": "Straight-Through"}  # IP Çakışması riski
]

print("⚡ Şəbəkə Altyapı və Bağlantı Analizi Başladı...")
print("--------------------------------------------------")

# 2. Dövr və Şərt operatorları ilə Troubleshooting məntiqini işlədirik
for sebeke in sebeke_cihazlari:
    cihaz_adi = sebeke["cihaz"]
    status = sebeke["status"]
    kabel_tipi = sebeke["kabel"]
    
    # Problem 1: Yanlış kabel və ya bağlantı xətası
    if status == "Error" or "Wrong" in kabel_tipi:
        print(f"🚨 NASAZLIQ TAPILDI! -> {cihaz_adi} qoşula bilmir. Səbəb: Yanlış kabel seçimi!")
    
    # Problem 2: IP Çakışması (Eyni IP-nin iki fərqli cihazda olması)
    elif sebeke["ip"] == "192.168.1.1" and cihaz_adi != "Router-HQ":
        print(f"⚠️ TƏHLÜKƏ! -> {cihaz_adi} cihazında IP Çakışması riski var (192.168.1.1).")
        
    else:
        print(f"✅ Şəbəkə Stabil: {cihaz_adi} | Status: {status} | IP: {sebeke['ip']}")

print("--------------------------------------------------")
print("🎯 TROUBLESHOOTING BAŞA ÇATDI: Zəhmət olmasa qırmızı və sarı xəbərdarlıqları yoxlayın.")
