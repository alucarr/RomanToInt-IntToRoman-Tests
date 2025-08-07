def roman_to_int(roman):
    roman = roman.upper()

    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    max_repeat = {
        'I': 3, 'X': 3, 'C': 3, 'M': 3,
        'V': 1, 'L': 1, 'D': 1
    }

    valid_subtract = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M']
    }

    for ch in roman:
        if ch not in roman_num:
            print(f"Hata: '{ch}' geçerli bir Roma rakamı değil.")
            return None

    counts = {k: 0 for k in roman_num}
    prev_char = ''
    repeat_count = 0

    for ch in roman:
        counts[ch] += 1
        if ch == prev_char:
            repeat_count += 1
            if repeat_count > max_repeat[ch]:
                print(f"Hata: '{ch}' karakteri en fazla {max_repeat[ch]} defa tekrar edebilir.")
                return None
        else:
            repeat_count = 1
            prev_char = ch

    for ch in ['D', 'L', 'V']:
        if counts[ch] > 1:
            print(f"Hata: '{ch}' karakteri sadece bir kere kullanılabilir.")
            return None

    toplam = 0
    i = 0
    used_subtract_pairs = set()
    banned_chars = set()

    last_value = None

    while i < len(roman):
        ch = roman[i]
        val = roman_num[ch]

        if ch in banned_chars:
            print(f"Hata: '{ch}' çıkarma işleminde kullanıldığı için tekrar edilemez.")
            return None

        if i + 1 < len(roman):
            next_ch = roman[i + 1]
            next_val = roman_num[next_ch]

            if val < next_val:
                if ch not in valid_subtract or next_ch not in valid_subtract[ch]:
                    print(f"Hata: '{ch}{next_ch}' geçerli bir çıkarma çifti değil.")
                    return None

                pair = ch + next_ch
                if pair in used_subtract_pairs:
                    print(f"Hata: '{pair}' çıkarma kombinasyonu birden fazla kullanılamaz.")
                    return None
                used_subtract_pairs.add(pair)
                banned_chars.add(ch)

                diff = next_val - val

                if last_value is not None and diff > last_value:
                    print("Hata: Geçersiz örüntü. Çıkarma yapılan sayıdan sonra daha büyük bir sayı gelemez.")
                    return None
                last_value = diff

                toplam += diff
                i += 2
                continue

        if last_value is not None and val > last_value:
            print("Hata: Roma rakamları azalan sırada olmalı.")
            return None
        last_value = val

        toplam += val
        i += 1

    if toplam > 3999:
        print("Hata: 3999'dan büyük Roma rakamları klasik sistemde desteklenmez.")
        return None

    return toplam


while True:
    girdi = input("Roman rakamı girin (çıkmak için 'q'): ").strip()
    if girdi.lower() == 'q':
        print("Programdan çıkılıyor.")
        break

    sonuc = roman_to_int(girdi)
    if sonuc is not None:
        print("Tam sayı değeri:", sonuc)
