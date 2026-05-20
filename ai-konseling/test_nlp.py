import sys
sys.path.append("c:/laragon/www/student-emotional-consultation-web-with-AI-main/ai-konseling")
from nlp_engine import calculate_emotion_score
from predefined_responses import PREDEFINED_RESPONSES

test_curhat = "Aku benci keadaan ini... Skripsi bener-bener bikin otak ngeblank dan aku ngerasa useless banget sebagai manusia. Udah berbulan-bulan aku gak bisa tidur karena overthinking parah. Rasanya duniaku sudah runtuh dan aku cuma ingin menghilang aja dari semuanya karena keberadaanku hanya menyusahkan orang tua."

score, indicator, details = calculate_emotion_score(test_curhat)
print(f"TEST CURHAT:")
print(f"Score: {score}")
print(f"Indicator: {indicator}")
print("Details:")
for d in details:
    print(f"  - {d['category']} ('{d['keyword']}'): {d['points']} Poin")

print("\nPREDEFINED CASES TEST:")
test_inputs = [
    "Aku lagi sedih banget hari ini.",
    "Asli, aku bingung mau mulai tugas dari mana.",
    "Gue mager parah, pen nangis.",
    "Udah tamat deh idup gue kali ini."
]

for inp in test_inputs:
    cleaned = inp.lower().strip()
    ans = PREDEFINED_RESPONSES.get(cleaned)
    if not ans:
        # Fallback to key without trailing period
        cleaned_no_dot = cleaned.rstrip(".")
        ans = PREDEFINED_RESPONSES.get(cleaned_no_dot, "NOT FOUND")
    print(f"Input: {inp}")
    print(f"Matched Key: {cleaned}")
    print(f"Response: {ans}\n")
