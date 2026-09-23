import os
# Google AI Studio'nun (Gemini) resmi kitapxanasını qoşuruq
import google.generativeai as gemini

# 1. AI API Açarını Təhlükəsiz Şəkildə Sistemdən Oxuyuruq
gemini.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Real Logistika Datası (Gömrük və Gecikmə Hesabatı)
logistika_datası = """
- Shipment ID: TR-994-01 | Status: Delayed at Baku Customs | Delay Reason: Paperwork Missing
- Shipment ID: CN-994-02 | Status: Completed | Cost: Optimized (-15%)
- Shipment ID: DE-994-03 | Status: Out for Delivery | Inbound Logistics: Smooth
"""

# 3. AI üçün Prompt-u (Tapşırığı) və Rolu Müəyyən Edirik
prompt = f"""
Sən peşəkar Logistika və Təchizat Zənciri Analitikisən. 
Aşağıdakı data hesabatını analiz et, problemləri tap və menecer üçün 
ingilis dilində qısa, professional xülasə (Executive Summary) hazırlat:

Hesabat Datası:
{logistika_datası}
"""

print("🚀 Süni İntellekt Analizə Başladı...")

# 4. Google AI Studio Modelini Çağırırıq və Cavabı Alırıq
model = gemini.GenerativeModel("gemini-1.5-flash")
cavab = model.generate_content(prompt)

# 5. Yekun Hesabatı Ekrana Çıxarırıq
print("\n--- MANAGER REPORT (AI GENERATED) ---")
print(cavab.text)
