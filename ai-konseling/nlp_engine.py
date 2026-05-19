import re

def calculate_emotion_score(text):
    original_text = text
    text = text.lower()
    
    details = []

    # ---------------------------------------------------------
    # Helper to check if any pattern matches the normalized text
    # ---------------------------------------------------------
    def match_any(patterns, txt):
        for pattern in patterns:
            escaped = re.escape(pattern)
            if pattern[0].isalnum():
                escaped = r'\b' + escaped
            if pattern[-1].isalnum():
                escaped = escaped + r'\b'
            if re.search(escaped, txt):
                return True
        return False

    def find_matching_keyword(patterns, txt):
        for pattern in patterns:
            escaped = re.escape(pattern)
            if pattern[0].isalnum():
                escaped = r'\b' + escaped
            if pattern[-1].isalnum():
                escaped = escaped + r'\b'
            if re.search(escaped, txt):
                return pattern
        return None

    # =================================================================
    # KATEGORI 1: KESESUAIAN MASALAH (Context Matching) - Maks 30 Poin
    # =================================================================
    k1_score = 0
    
    # Kelompok A: Masalah Akademik & Perkuliahan
    k1_a_rules = [
        (["dibantai tugas", "project ga ngotak", "kerjaan kampus"], 5),
        (["deadline mepet", "kejar deadline", "dikejar deadline", "deadline", "numpuk"], 6),
        (["dosen aneh", "ditegur dosen", "matkul setan", "kelas"], 5),
        (["ujian", "uts", "uas", "quiz"], 7),
        (["skripsi", "ta", "bimbingan"], 8),
        (["ipk", "nilai jelek", "remedial"], 6),
        (["presentasi", "sidang"], 6),
        (["telat ngumpul", "revisi"], 5),
        (["jadwal padat", "bentrok kelas", "telat masuk"], 6),
        (["mager kuliah", "skip kelas"], 5),
        (["tugas numpuk", "kerjaan numpuk", "project numpuk"], 6),
        (["revisian mulu", "revisi terus", "revisi endless"], 7),
        (["dosen killer", "dosen ribet", "dosen galak"], 7),
        (["matkul susah", "materi susah", "pelajaran susah"], 6),
        (["gak ngerti materi", "blank", "otak blank", "plenger"], 6),
        (["stuck skripsi", "skripsi mandek", "skripsi gak jalan"], 8),
        (["bimbingan zonk", "dosen susah ditemui", "gak dibales dosen"], 7),
        (["ipk ancur", "nilai drop", "nilai jelek"], 7),
        (["telat submit", "telat ngumpul", "lupa submit"], 5),
        (["mager ngerjain", "males nugas", "males belajar", "mls"], 5),
        (["burnout kuliah", "capek kuliah", "lelah kuliah"], 8),
        (["jadwal padat", "jadwal penuh", "bentrok jadwal"], 6),
        (["presentasi tegang", "takut presentasi", "grogi presentasi"], 6),
        (["sidang takut", "sidang deg-degan", "sidang stres"], 7)
    ]
    
    # Kelompok B: Masalah Sosial & Relasi
    k1_b_rules = [
        (["teman anj", "circle", "lingkungan buruk", "jahat"], 5),
        (["dijauhi", "gak diajak"], 8),
        (["pacar", "relationship", "doi"], 8),
        (["putus", "breakup"], 9),
        (["orang tua", "keluarga"], 10),
        (["toxic", "konflik"], 9),
        (["organisasi", "hima", "kepanitiaan"], 5),
        (["dibanding-bandingkan"], 8),
        (["bully", "diejek", "sombong"], 10),
        (["kesepian di lingkungan sosial"], 8),
        (["circle toxic", "temen toxic", "lingkungan toxic"], 9),
        (["temen fake", "fake friend", "pura-pura baik"], 8),
        (["di ghosting", "di-ghosting", "ghosting"], 8),
        (["dicuekin", "gak direspon", "diabaikan"], 7),
        (["gak dianggap", "gak dihargai", "diremehkan"], 7),
        (["dibandingin mulu", "dibanding-bandingkan"], 8),
        (["keluarga toxic", "ortu toxic", "rumah toxic", "pacar toxic", "temen toxic", "toxic"], 10),
        (["dimarahin ortu", "ditekan ortu", "dituntut ortu"], 10),
        (["hubungan toxic", "relationship toxic"], 9),
        (["putus", "breakup", "putus sama doi"], 9),
        (["capek relationship", "capek pacaran"], 8),
        (["lonely banget", "kesepian banget", "sendiri banget"], 8),
        (["social anxiety", "takut sosial", "canggung sosial"], 9),
        (["gak punya temen", "friendless", "no friend"], 9),
        (["dijauhi", "gak diajak", "dikucilkan", "sendiri lagi"], 8)
    ]
    
    # Kelompok C: Masalah Pribadi & Internal
    k1_c_rules = [
        (["overthinking parah", "overthinking banget"], 7),
        (["mental down", "lagi down", "down banget"], 8),
        (["ngerasa useless", "merasa gak berguna", "useless"], 8),
        (["ngerasa gagal", "merasa gagal", "failure"], 8),
        (["insecure parah", "insecure banget", "insecure"], 8),
        (["self doubt", "ragu diri", "gak pede"], 7),
        (["capek hidup", "capek banget hidup"], 8),
        (["hidup berat", "hidup susah"], 8),
        (["lost arah hidup", "kehilangan arah", "hilang arah", "sesat", "tersesat"], 6),
        (["hidup gak jelas", "bingung hidup"], 8),
        (["feeling empty", "kosong", "hampa"], 4),
        (["numb", "mati rasa", "bodoh", "kosong", "kepikiran"], 7),
        (["burnout", "burnout parah", "burnout banget"], 6),
        (["anxiety naik", "cemas banget"], 6),
        (["panic attack", "panik banget"], 7),
        (["gak bisa tidur", "insomnia", "susah tidur", "mata melek terus", "jarang tidur"], 7),
        (["stress", "gaguna", "gak guna", "apaan coba", "stress banget", "stres parah"], 7),
        (["overwhelmed", "kewalahan"], 8),
        (["capek mental", "lelah mental", "gak kuat", "udah capek banget", "mls bgt"], 8)
    ]

    has_academic = False
    has_social = False
    has_pribadi = False

    for keywords, score in k1_a_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k1_score += score
            has_academic = True
            details.append({"category": "Akademik/Perkuliahan", "keyword": matched, "points": score})
            
    for keywords, score in k1_b_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k1_score += score
            has_social = True
            details.append({"category": "Sosial & Relasi", "keyword": matched, "points": score})
            
    for keywords, score in k1_c_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k1_score += score
            has_pribadi = True
            details.append({"category": "Pribadi & Internal", "keyword": matched, "points": score})

    # Kelompok D: Kompleksitas Konteks
    # 71: karena, jadi, makanya, gara-gara (+10)
    matched = find_matching_keyword(["karena", "jadi", "makanya", "gara-gara"], text)
    if matched:
        k1_score += 10
        details.append({"category": "Pola Hubung (Sebab-Akibat)", "keyword": matched, "points": 10})
        
    # 72: curhat panjang (> 2 sentences or > 120 chars) (+7)
    if len(re.split(r'[.!?]+', text)) > 2 or len(text) > 120:
        k1_score += 7
        details.append({"category": "Panjang Curhatan", "keyword": "teks panjang", "points": 7})
        
    # 73: campur indo-english (+5)
    en_words = ["burnout", "relationship", "toxic", "literally", "useless", "worthlessness", "social anxiety", "fake friend", "overthinking", "clueless", "worthless", "failed", "empty", "lonely", "panic attack", "insomnia", "survive", "strong", "flow", "coping"]
    matched = find_matching_keyword(en_words, text)
    if matched:
        k1_score += 5
        details.append({"category": "Campuran Bahasa (Indo-English)", "keyword": matched, "points": 5})
        
    # 74: banget, parah, banget banget, laknat, plenger, dongo (+5)
    matched = find_matching_keyword(["banget", "parah", "banget banget", "laknat", "plenger", "dongo"], text)
    if matched:
        k1_score += 5
        details.append({"category": "Penguat Emosi", "keyword": matched, "points": 5})
        
    # 75: ALL CAPS (+6)
    if any(word.isupper() and len(word) >= 4 for word in original_text.split()):
        k1_score += 6
        details.append({"category": "Huruf Kapital Semua", "keyword": "kapital/berteriak", "points": 6})
        
    # 76: elongated words (+6)
    match_elongated = re.search(r'([a-zA-Z])\1{2,}', original_text)
    if match_elongated:
        k1_score += 6
        details.append({"category": "Pemanjangan Kata", "keyword": match_elongated.group(0), "points": 6})
        
    # 77: repeated punctuation (+6)
    match_punct = re.search(r'(!{2,}|\?{2,})', original_text)
    if match_punct:
        k1_score += 6
        details.append({"category": "Tanda Baca Berulang", "keyword": match_punct.group(0), "points": 6})
        
    # 78: multiple periods (+4)
    match_periods = re.search(r'\.{3,}', original_text)
    if match_periods:
        k1_score += 4
        details.append({"category": "Titik Berulang (...)", "keyword": match_periods.group(0), "points": 4})
        
    # 79: storytelling (+10)
    if len(original_text) > 180:
        k1_score += 10
        details.append({"category": "Gaya Bercerita", "keyword": "teks > 180 karakter", "points": 10})
        
    # 80: lebih dari 1 topik (+10)
    if sum([has_academic, has_social, has_pribadi]) > 1:
        k1_score += 10
        details.append({"category": "Kompleksitas Topik", "keyword": "multi-topik", "points": 10})
        
    # 81: tekanan (dituntut, dipaksa, ditekan) (+8)
    matched = find_matching_keyword(["dituntut", "dipaksa", "ditekan"], text)
    if matched:
        k1_score += 8
        details.append({"category": "Tekanan Eksternal", "keyword": matched, "points": 8})
        
    # 82: konflik (bingung, dilema, gak tau harus gimana, gak suka, gak like, ga suka aja) (+4)
    matched = find_matching_keyword(["bingung", "dilema", "gak tau harus gimana", "gak suka", "gak like", "ga suka aja"], text)
    if matched:
        k1_score += 4
        details.append({"category": "Konflik Internal/Bingung", "keyword": matched, "points": 4})
        
    # 83: perbandingan (dulu vs sekarang) (+5)
    if "dulu" in text and "sekarang" in text:
        k1_score += 5
        details.append({"category": "Perbandingan Garis Waktu", "keyword": "dulu vs sekarang", "points": 5})
        
    # 84: frekuensi (tiap hari, terus-terusan) (+6)
    matched = find_matching_keyword(["tiap hari", "terus-terusan"], text)
    if matched:
        k1_score += 6
        details.append({"category": "Frekuensi Gejala", "keyword": matched, "points": 6})
        
    # 85: durasi (udah lama, berbulan-bulan) (+6)
    matched = find_matching_keyword(["udah lama", "berbulan-bulan"], text)
    if matched:
        k1_score += 6
        details.append({"category": "Durasi Masalah", "keyword": matched, "points": 6})
        
    # 86: lokasi (di kos, di rumah, di kampus) (+5)
    matched = find_matching_keyword(["di kos", "di rumah", "di kampus", "kamar kos", "kosan"], text)
    if matched:
        k1_score += 5
        details.append({"category": "Lokasi Kejadian", "keyword": matched, "points": 5})
        
    # 87: usaha gagal (udah coba tapi gagal) (+10)
    matched = find_matching_keyword(["udah coba", "tapi gagal", "perjuangan gue", "perjuangan saya"], text)
    if matched:
        k1_score += 10
        details.append({"category": "Usaha Pemecahan Gagal", "keyword": matched, "points": 10})
        
    # 88: harapan vs realita (ekspektasi vs kenyataan) (+7)
    matched = find_matching_keyword(["ekspektasi", "kenyataan", "harapan", "realita"], text)
    if matched:
        k1_score += 7
        details.append({"category": "Harapan vs Realita", "keyword": matched, "points": 7})
        
    # 89: tekanan sosial (harus, tuntutan orang lain) (+8)
    matched = find_matching_keyword(["harus", "tuntutan"], text)
    if matched:
        k1_score += 8
        details.append({"category": "Tuntutan/Kewajiban", "keyword": matched, "points": 8})
        
    # 90: konflik batin (bingung, galau, ragu) (+6)
    matched = find_matching_keyword(["galau", "ragu", "bingung"], text)
    if matched:
        k1_score += 6
        details.append({"category": "Konflik Batin", "keyword": matched, "points": 6})

    # Capped K1 score at 30
    k1_score_capped = min(k1_score, 30)
    if k1_score > 30:
        details.append({"category": "Batas Kategori 1", "keyword": "maksimal k1", "points": -(k1_score - 30)})

    # =================================================================
    # KATEGORI 2: URGENSI & KEDALAMAN EMOSI (NLP Analysis)
    # =================================================================
    k2_score = 0
    
    # Kelompok C
    k2_c_rules = [
        (["selalu", "selamanya", "tidak pernah"], 5),
        (["kosong", "hampa", "datar", "hollow"], 7),
        (["semua salahku", "aku gagal", "salahku"], 6),
        (["gak ada yang peduli", "sendirian", "sendiri lagi"], 7),
        (["!!!!!!!!!!!!!!!!"], 5),
        (["gak ada harapan", "sia-sia", "sia-sia saja", "sia sia"], 8),
        (["gak tahan lagi", "mau meledak", "gak tahan"], 8),
        (["sudah berbulan-bulan", "berbulan-bulan"], 7),
        (["hancur", "hancur berkeping-keping"], 9),
        (["terasa gelap", "tidak ada cahaya", "terasa gelap", "gelap banget"], 8),
        (["tidak merasakan apa-apa lagi", "tidak merasakan apa-apa"], 9),
        (["benci diriku sendiri", "benci diriku"], 9),
        (["di batas kemampuan"], 8),
        (["salah"], 8),
        (["tercekik"], 9),
        (["trauma"], 8),
        (["duniaku terasa runtuh", "duniaku runtuh"], 9),
        (["tidak berharga"], 9),
        (["tidur dan tidak bangun lagi"], 10),
        (["tidak ada lagi jalan keluar", "tidak ada jalan keluar"], 10),
        (["penjara", "terjebak"], 8),
        (["terisolasi"], 8),
        (["sakit di dada", "perih di dada", "nyesek banget di dada"], 8),
        (["semua orang akan lebih baik tanpa aku"], 10),
        (["kehilangan jati diri"], 8),
        (["sudah terlambat"], 9),
        (["jijik"], 8),
        (["mati di dalam"], 10),
        (["menghancurkan barang", "hancurin barang"], 9),
        (["tidak sanggup menanggung"], 10),
        (["tamat", "selesai"], 10),
        (["ditinggalkan oleh tuhan", "ditinggalkan oleh nasib"], 8),
        (["seperti neraka"], 9),
        (["menyerah sepenuhnya"], 10)
    ]

    # Kelompok B
    k2_b_rules = [
        (["sangat", "banget", "sekali"], 3),
        (["cemas", "khawatir", "takut", "panik"], 3),
        (["pusing", "mual", "deg-degan", "deg degan"], 4),
        (["males ngapa-ngapain", "males ngapa2in", "gak semangat"], 3),
        (["kesal", "marah", "muak"], 3),
        (["capek hati", "lelah pikiran", "capek mental", "lelah mental"], 4),
        (["burnout"], 5),
        (["tertekan", "under pressure"], 4),
        (["sesak", "sesak dada", "sulit bernapas"], 5),
        (["anjing", "anj", "bangsat", "bego", "dongo", "bangsad"], 4),
        (["ingin menyendiri", "menyendiri"], 4),
        (["gelisah"], 4),
        (["banget banget"], 4),
        (["otak ngeblank", "blank"], 4),
        (["menangis tiba-tiba", "menangis tiba2"], 5),
        (["beban"], 5),
        (["kecewa berat"], 4),
        (["asam lambung", "maag"], 5),
        (["aku benci keadaan ini", "benci banget sama diriku"], 4),
        (["takut salah"], 4),
        (["tidak tenang", "pikiran kalut"], 4),
        (["kehilangan selera makan", "gak nafsu makan", "males makan"], 4),
        (["!!"], 3),
        (["merasa tertinggal", "tertinggal jauh"], 5),
        (["muak"], 5),
        (["ingin teriak", "pen teriak"], 5),
        (["paranoia", "dihakimi"], 4),
        (["sulit diajak bicara", "bungkam"], 4),
        (["rasanya mau marah"], 5),
        (["badan gemetar", "gemetar"], 5),
        (["tidur kacau", "pola tidur kacau", "jarang tidur"], 4)
    ]

    # Kelompok A
    k2_a_rules = [
        (["sedih", "bingung", "bosan"], 2),
        (["cuma", "agak", "sedikit"], 2),
        (["kenapa ya aku", "kenapa aku begini"], 2),
        (["senang tapi", "bahagia tapi", "lulus tapi"], 2),
        (["gitu-gitu aja", "kuliah pulang"], 2),
        (["mager"], 2),
        (["kurang"], 1),
        (["sepi", "berisik"], 1),
        (["flat"], 2),
        (["kok orang lain", "insecure liat"], 2),
        (["overthinking"], 3),
        (["moody", "mood swing"], 2),
        (["kapan ya ini selesai", "kapan selesai"], 2),
        (["linglung", "clueless"], 2),
        (["lumayan"], 1),
        (["waktu berasa lambat", "waktu lambat"], 1),
        (["self-reward", "self reward"], 2),
        (["malu", "sungkan"], 2),
        (["heran"], 2),
        (["deh", "sih"], 1),
        (["healing"], 3),
        (["aku cuma", "saya hanya"], 2),
        (["ingin tidur cepat", "tidur cepat"], 2),
        (["entahlah"], 2),
        (["nyesek"], 2),
        (["?"], 1),
        (["sensitif"], 2),
        (["lelah fisik", "badan lelah", "capek fisik"], 2),
        (["ingin jeda", "jeda sebentar"], 2),
        (["was-was", "was was"], 2),
        (["sayang banget", "andai tadi"], 2),
        (["kok gini ya"], 2),
        (["apresiasi diri", "kurang apresiasi"], 2)
    ]

    c_triggered = False
    for keywords, score in k2_c_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k2_score += score
            c_triggered = True
            details.append({"category": "Kedalaman Emosi (Krisis)", "keyword": matched, "points": score})

    b_triggered = False
    for keywords, score in k2_b_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k2_score += score
            b_triggered = True
            details.append({"category": "Kedalaman Emosi (Sedang)", "keyword": matched, "points": score})

    for keywords, score in k2_a_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k2_score += score
            details.append({"category": "Kedalaman Emosi (Ringan)", "keyword": matched, "points": score})

    if original_text.isupper() and len(original_text) > 10:
        k2_score += 5
        details.append({"category": "Urgensi Emosi (SHOUTING)", "keyword": "huruf kapital semua", "points": 5})

    # =================================================================
    # KATEGORI 3: KEBUTUHAN INTERVENSI DINI (Risk & Safety)
    # =================================================================
    k3_score = 0
    
    # Kelompok C
    k3_c_rules = [
        (["bunuh diri"], 10),
        (["ingin mengakhiri hidup", "mengakhiri hidup"], 10),
        (["gantung diri"], 10),
        (["minum racun", "minum obat serangga", "minum racun/obat"], 10),
        (["titip pesan untuk"], 10),
        (["maafkan aku, aku harus pergi"], 10),
        (["sudah memegang alat berbahaya"], 10),
        (["malam ini adalah terakhir kali", "terakhir kali kalian melihatku"], 10),
        (["sudah tidak punya siapa-siapa lagi"], 9),
        (["tolong, darurat, segera ke sini"], 10),
        (["ada suara menyuruhku mati"], 10),
        (["melihat bayangan kematian"], 9),
        (["membunuh orang lain"], 10),
        (["baru saja melukai diriku", "melukai diriku"], 10),
        (["tidak ada gunanya menelepon bantuan"], 9),
        (["sakaratul maut"], 10),
        (["bukan di dunia nyata"], 9),
        (["ini surat terakhirku"], 10),
        (["selamat tinggal semuanya"], 10),
        (["gedung tinggi untuk melompat", "melompat dari gedung"], 10),
        (["sudah siap untuk pergi"], 9),
        (["tali", "pisau", "obat serangga"], 10),
        (["cabut nyawaku", "tuhan cabut nyawaku"], 9),
        (["tidak sanggup menahan sakit ini satu detik lagi"], 10),
        (["keputusan sudah bulat untuk mati"], 10),
        (["hanya kematian yang bisa menolongku"], 10),
        (["meledakkan diri"], 10),
        (["mengunci diri di kamar dengan alat bahaya"], 10),
        (["kematian adalah satu-satunya solusi", "kematian solusi"], 10),
        (["panggil polisi untuk jenazahku", "panggil ambulans untuk jenazahku"], 10)
    ]

    # Kelompok B
    k3_b_rules = [
        (["alkohol", "miras"], 6),
        (["obat penenang tanpa resep", "obat penenang"], 7),
        (["mengiris pergelangan tangan", "iris pergelangan", "silet tangan"], 9),
        (["memukul diri sendiri", "memukul diri"], 6),
        (["membenturkan kepala ke tembok", "benturin kepala"], 8),
        (["aku layak mendapatkan rasa sakit fisik"], 7),
        (["tidak makan berhari-hari"], 6),
        (["pengabaian total pada kesehatan"], 6),
        (["menghukum diriku sendiri", "menghukum diriku"], 7),
        (["besok sudah tidak penting lagi"], 7),
        (["cara untuk mati tanpa rasa sakit"], 10),
        (["merasakan sakit fisik agar lupa sakit hati"], 8),
        (["membakar kulit sendiri", "membakar kulit"], 9),
        (["narkoba"], 8),
        (["hidupku sudah tamat"], 7),
        (["tidak ada masa depan untuk orang sepertiku"], 6),
        (["mencelakai diri secara perlahan", "mencelakai diri"], 8),
        (["kebencianku pada diri sendiri sudah memuncak"], 7),
        (["ingin menabrakkan diri", "menabrakkan diri"], 10),
        (["menghapus semua foto dan kenangan"], 6),
        (["memberikan barang kesayangan"], 8),
        (["tidak ada yang akan merindukanku"], 7),
        (["ingin terjun dari tempat tinggi", "terjun dari tempat tinggi"], 10),
        (["menghentikan detak jantung"], 9),
        (["mengurung diri di tempat berbahaya"], 7),
        (["aku lebih baik mati saja"], 8),
        (["darah", "luka", "silet"], 8),
        (["merencanakan kepergian selamanya"], 9),
        (["semuanya akan selesai malam ini"], 9),
        (["perpisahan yang abadi"], 8),
        (["tidak peduli lagi dengan nyawa"], 8),
        (["ingin lenyap sekarang juga", "ingin lenyap"], 8)
    ]

    # Kelompok A
    k3_a_rules = [
        (["menyerah sama keadaan", "menyerah saja"], 2),
        (["sudah tak sanggup lagi berdiri", "tak sanggup berdiri"], 2),
        (["pasrah biarkan semua hancur"], 2),
        (["ingin tidur dan tidak bangun lagi"], 4),
        (["untuk apa aku ada di sini"], 3),
        (["ingin pergi ke tempat yang sangat jauh", "pergi ke tempat yang sangat jauh"], 3),
        (["merasa dunia lebih baik tanpa aku", "dunia lebih baik tanpa aku"], 4),
        (["keberadaanku hanya menyusahkan", "menyusahkan orang tua"], 3),
        (["beban bagi orang tua", "beban bagi keluarga", "beban kelompok"], 3),
        (["capek hidup", "lelah hidup"], 3),
        (["sudah tidak ada alasan untuk bertahan", "tidak ada alasan bertahan"], 3),
        (["hanya ingin menghilang", "ingin menghilang"], 3),
        (["semuanya sia-sia"], 2),
        (["aku gagal sebagai manusia", "gagal sebagai anak"], 4),
        (["jiwaku sudah mati", "mati di dalam jiwanya"], 4),
        (["tidak ada tempat untukku di dunia ini", "tidak ada tempat untukku"], 3),
        (["ingin menghapus diri sendiri"], 5),
        (["titik nadir", "titik terendah"], 3),
        (["harapanku sudah habis", "harapan habis"], 3),
        (["tidak ada yang bisa menyelamatkanku"], 4),
        (["semua pintu sudah tertutup"], 2),
        (["ingin berhenti merasakan apa pun"], 4),
        (["duniaku sudah runtuh"], 3),
        (["tidak punya energi untuk bernapas"], 4),
        (["kenapa aku harus lahir"], 3),
        (["semua orang akan senang jika aku pergi"], 5),
        (["gelap, tidak ada cahaya lagi", "tidak ada cahaya lagi"], 3),
        (["sudah tidak bisa melihat hari esok"], 4),
        (["sudahlah, jangan cari aku lagi"], 5),
        (["terjebak dalam kegelapan abadi"], 3),
        (["aku hanya sampah masyarakat"], 4),
        (["rasanya ingin mengakhiri semua ini"], 5)
    ]

    for keywords, score in k3_c_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k3_score += score
            details.append({"category": "Intervensi Krisis (Tinggi)", "keyword": matched, "points": score})
            
    for keywords, score in k3_b_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k3_score += score
            details.append({"category": "Risiko Perilaku (Sedang)", "keyword": matched, "points": score})
            
    for keywords, score in k3_a_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            k3_score += score
            details.append({"category": "Waspada / Ketidakberdayaan", "keyword": matched, "points": score})

    # =================================================================
    # RULE MINUS: REGULASI EMOSI POSITIF (Maksimal -30 Poin)
    # =================================================================
    minus_score = 0
    
    # Kelompok A
    minus_a_rules = [
        (["gpp", "gapapa", "ga papa", "it's okay", "its okay"], -2),
        (["santai", "santai aja", "santuy", "chill", "chill aja"], -2),
        (["aman", "aman kok", "still safe", "aman sih"], -2),
        (["oke", "oke sih", "fine", "i'm fine", "all good", "i'm okay", "gacor"], -2),
        (["yaudah", "yaudahlah", "yaudah sih", "yasudah", "biarin"], -2),
        (["wkwk", "wkwkwk", "wk", "lol", "lmao", "mwehe", "awokwok", "sksksk"], -2),
        (["hehe", "haha", "hihi", "ngakak", "ngabrut", "lucu", "jelas"], -2),
        (["bercanda", "bercanda doang", "just kidding", "kidding"], -2),
        (["seru", "asik", "enjoy", "fun"], -2),
        (["take it easy", "slow aja", "pelan aja", "bawa santai"], -2),
        (["santai bro", "santai sis", "chill bro", "chill guys"], -2),
        (["lucu sih", "kocak", "ngakak sih"], -2),
        (["santai dulu", "rebahan dulu", "leha-leha"], -2),
        (["healing dulu", "self care dulu", "me time dulu"], -3),
        (["gak seburuk itu", "not that bad", "masih mending"], -3),
        (["santai aja lah", "santuy aja lah", "chill aja lah", "santai ae"], -2),
        (["gak usah dipikir berat", "gausah dipikir", "dont overthink"], -3),
        (["bodo amat dikit", "bodo amat", "bodoamat", "idc", "i don't care"], -2),
        (["jalanin aja lah", "flow aja", "let it flow", "go with flow"], -3),
        (["ikuti aja", "ikut alur aja", "ngikut aja", "just go with it", "ya jalan aja", "jalanin", "jalanin dulu"], -3)
    ]

    # Kelompok B
    minus_b_rules = [
        (["aku coba", "gue coba", "lagi coba", "i'm trying", "trying", "cobain dulu"], -4),
        (["aku usaha", "gue usaha", "lagi usaha", "keep trying", "gw usaha"], -4),
        (["pelan-pelan", "step by step", "one by one", "slowly", "pelan"], -3),
        (["dicicil", "dicicil aja", "jalanin aja", "dijalanin"], -3),
        (["aku belajar", "gue belajar", "lesson learned", "ambil pelajaran"], -4),
        (["ambil hikmah", "ada hikmahnya", "ada pelajaran"], -5),
        (["sabar", "aku sabar", "gue sabar", "sabar aja"], -3),
        (["tahan", "tahan dikit", "aku tahan", "still holding"], -4),
        (["aku kontrol", "gue kontrol", "aku atur", "manage diri"], -4),
        (["tarik napas", "napas dulu", "coba tenang", "calming down"], -3),
        (["istirahat dulu", "take a break", "rest dulu", "turu sek", "napas dulu", "rilex"], -3),
        (["gak usah overthinking", "no need overthinking", "chill pikiran"], -3),
        (["gue handle", "i can handle", "handle this"], -5),
        (["coping aja", "i'm coping", "lagi coping"], -3),
        (["tetap jalan", "keep going", "keep moving"], -6)
    ]

    # Kelompok C
    minus_c_rules = [
        (["aku bisa", "gue bisa", "i can do this", "i can", "bisa aja"], -5),
        (["pasti bisa", "bakal bisa", "sure can"], -5),
        (["masih kuat", "gue kuat", "still strong"], -5),
        (["masih bertahan", "still holding on", "bertahan"], -5),
        (["aku yakin", "gue yakin", "i'm sure"], -5),
        (["percaya proses", "trust the process", "proses aja"], -5),
        (["semoga", "hopefully", "mudah-mudahan", "moga aja"], -3),
        (["masih ada harapan", "there is hope", "masih berharap"], -4),
        (["it'll get better", "bakal better", "get better", "baiklah"], -4),
        (["aku ngerti", "gue ngerti", "i get it", "gue paham", "pahamlah"], -3),
        (["aku sadar", "gue sadar", "i'm aware"], -4),
        (["masih oke", "masih oke kok", "masih fine"], -3),
        (["masih bisa jalan", "masih survive", "still going"], -4),
        (["gue survive", "i'm surviving", "survive"], -4),
        (["kuat kok", "aman kok", "masih aman"], -3),
        (["bisa dilewatin", "bisa dilalui", "will pass"], -5),
        (["stay positive", "tetap positif", "positive thinking"], -5),
        (["ada jalan keluar", "pasti ada jalan", "solusi ada"], -5),
        (["ini cuma fase", "hanya sementara", "just a phase"], -4),
        (["nanti juga lewat", "bakal lewat", "will pass soon"], -4)
    ]

    # Kelompok D
    minus_d_rules = [
        (["curhat sama temen", "cerita ke temen", "cerita2", "curcol", "curhat2", "cerita ke bestie"], -4),
        (["temen support", "temen bantu", "temen ada", "tmn support", "bestie support"], -5),
        (["masih punya temen", "ada temen kok", "gak sendirian", "ga sendiri", "not alone"], -5),
        (["dibantu temen", "ditemenin temen", "ditemenin", "ditemenin tmn", "ditemenin bestie"], -4),
        (["ada yang dengerin", "ada yg peduli", "ada yg care", "someone cares"], -5),
        (["bareng temen", "kumpul bareng", "nongkrong", "nongki", "ngumpul"], -3),
        (["main sama temen", "hangout", "jalan bareng", "jalan2", "main bareng"], -3),
        (["ketawa bareng", "seru bareng", "have fun bareng", "fun bareng"], -3),
        (["becanda aja", "bercanda mulu", "gua becanda", "just kidding", "jk"], -2),
        (["ketawa aja", "ditertawain aja", "ya ketawa", "laugh aja", "ketawa2"], -3),
        (["diketawain hidup", "ya diketawain aja", "laugh it off", "lol aja"], -2),
        (["hidup lucu juga", "lucu banget hidup", "hidup kocak", "absurd banget"], -3),
        (["drama dikit", "lebay dikit", "over dikit", "overthinking dikit"], -2),
        (["ya elah", "anjir lucu", "wtf lucu", "njir lucu", "bjir"], -3),
        (["yaudah ketawa aja", "laugh it off", "ketawain aja", "santai ketawa"], -2),
        (["yaudahlah ya", "yaelah", "yaelah ya", "yaelah hidup"], -2),
        (["anjir dah", "njir dah", "bjir dah", "wkwk dah"], -2),
        (["ketawa pahit", "ketawa doang", "ketawa getir"], -2),
        (["hidup mah gini", "hidup ya gini", "namanya juga hidup"], -2),
        (["yaudah nikmatin aja", "nikmatin aja dah", "enjoy aja dah"], -3)
    ]

    for keywords, score in minus_a_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            minus_score += score
            details.append({"category": "Regulasi Positif (Santai)", "keyword": matched, "points": score})
            
    for keywords, score in minus_b_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            minus_score += score
            details.append({"category": "Regulasi Positif (Coping)", "keyword": matched, "points": score})
            
    for keywords, score in minus_c_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            minus_score += score
            details.append({"category": "Regulasi Positif (Resilience)", "keyword": matched, "points": score})
            
    for keywords, score in minus_d_rules:
        matched = find_matching_keyword(keywords, text)
        if matched:
            minus_score += score
            details.append({"category": "Regulasi Positif (Sosial/Humor)", "keyword": matched, "points": score})

    # Limit minus score to -30
    minus_score_capped = max(minus_score, -30)
    if minus_score < -30:
        details.append({"category": "Batas Regulasi Positif", "keyword": "maksimal minus", "points": -(minus_score - (-30))})

    # =================================================================
    # KALKULASI AKHIR & PENENTUAN STATUS
    # =================================================================
    total_skor = k1_score_capped + k2_score + k3_score + minus_score_capped
    total_skor = max(total_skor, 0)
    
    # Safety overriding
    if total_skor > 70 or k3_score >= 8:
        indicator = "Merah"
    elif total_skor >= 36:
        indicator = "Kuning"
    else:
        indicator = "Hijau"
        
    return total_skor, indicator, details