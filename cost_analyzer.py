# Təməl Lojistik və Maliyyə Maliyyət Analizi Skripti

# 1. Aylıq Lojistik və Boşaltma Xərcləri Datası (Fiktif Şirkət Hesabatı)
loji_xərclər = [
    {"gün": "01.09.2026", "əməliyyat": "Gömrük rəsmiləşdirilməsi", "xərc": 1200, "limit": 1000},
    {"gün": "05.09.2026", "əməliyyat": "Xammal boşaldılması (Zavod)", "xərc": 2500, "limit": 2000},
    {"gün": "12.09.2026", "əməliyyat": "Daxili logistika (Nəqliyyat)", "xərc": 800, "limit": 1000},
    {"gün": "18.09.2026", "əməliyyat": "Anbarın idarə edilməsi", "xərc": 1500, "limit": 1500}
]

print("📊 Lojistik Maliyyə Analizi Başladı...")
print("----------------------------------------")

ümumi_itki = 0

# 2. Dövr (Loop) vasitəsilə xərcləri tək-tək yoxlayırıq və şərt (If) qoyuruq
for operasiya in loji_xərclər:
    cari_xərc = operasiya["xərc"]
    müəyyən_limit = operasiya["limit"]
    
    if cari_xərc > müəyyən_limit:
        fərq = cari_xərc - müəyyən_limit
        ümumi_itki += fərq
        print(f"🚨 LİMİT AŞIMI TAPILDI! Tarix: {operasiya['gün']} | {operasiya['əməliyyat']} | Aşın məbləğ: +{fərq} AZN")
    else:
        print(f"✅ Normal Əməliyyat: {operasiya['əməliyyat']} | Xərc: {cari_xərc} AZN")

print("----------------------------------------")
print(f"📉 HESABAT: Bu ay optimallaşdırılması vacib olan ümumi artıq xərc: {ümumi_itki} AZN")
