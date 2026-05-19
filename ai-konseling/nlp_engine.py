import re

def calculate_emotion_score(text):
    text = text.lower()
    
    # =================================================================
    # 1. KATEGORI 1: KESESUAIAN MASALAH (Maksimal 30 Poin)
    # =================================================================
    kategori_1_rules = [
        # -- Kelompok A: Akademik & Perkuliahan --
        (r'\b(skripsi|ta|bimbingan)\b', 8),
        (r'\b(dosen killer|dosen ribet|dosen galak)\b', 7),
        (r'\b(dibantai tugas|deadline|tugas numpuk)\b', 6),
        
        # -- Kelompok B: Sosial & Hubungan --
        (r'\b(teman toxic|circle|dijauhi)\b', 5),
        (r'\b(putus|breakup|diselingkuhi)\b', 9),
        
        # -- Kelompok C: Pribadi & Internal --
        (r'\b(overthinking parah)\b', 7),
        (r'\b(merasa gagal|useless|nggak berguna)\b', 8)
    ]
    
    skor_k1 = sum(poin for pola, poin in kategori_1_rules if re.search(pola, text))
    skor_k1 = min(skor_k1, 30) # Sesuai rule: Kategori 1 mentok di 30 poin
    
    # =================================================================
    # 2. KATEGORI 2: URGENSI & KEDALAMAN EMOSI
    # =================================================================
    kategori_2_rules = [
        (r'\b(otak ngeblank|blank)\b', 4),
        (r'\b(duniaku terasa runtuh|duniaku runtuh)\b', 9),
        (r'\b(dada sesak|sesak)\b', 5),
        (r'\b(capek hati|lelah pikiran|burnout)\b', 4),
        (r'\b(nangis tiba-tiba|sering menangis)\b', 5)
    ]
    skor_k2 = sum(poin for pola, poin in kategori_2_rules if re.search(pola, text))
    
    # =================================================================
    # 3. KATEGORI 3: RISIKO & INTERVENSI DINI
    # =================================================================
    kategori_3_rules = [
        (r'\b(ingin menghilang|hanya ingin menghilang)\b', 3),
        (r'\b(bunuh diri|ingin mengakhiri hidup)\b', 10),
        (r'\b(keberadaanku hanya menyusahkan)\b', 3)
    ]
    skor_k3 = sum(poin for pola, poin in kategori_3_rules if re.search(pola, text))
    
    # =================================================================
    # 4. RULE MINUS: REGULASI EMOSI POSITIF
    # =================================================================
    rule_minus = [
        (r'\b(gapapa|gpp|santai|it\'s okay|aku usaha)\b', -2),
        (r'\b(bisa dilewatin|pasti bisa|semangat)\b', -5)
    ]
    skor_minus = sum(poin for pola, poin in rule_minus if re.search(pola, text))
    
    # =================================================================
    # 5. KALKULASI TOTAL & PENENTUAN INDIKATOR
    # =================================================================
    total_skor = skor_k1 + skor_k2 + skor_k3 + skor_minus
    total_skor = max(total_skor, 0) # Mencegah skor menjadi minus (kurang dari 0)

    if total_skor > 70:
        indicator = "Merah"
    elif total_skor >= 36:
        indicator = "Kuning"
    else:
        indicator = "Hijau"
        
    return total_skor, indicator