# Sun'iy intellektni kiberxavfsizlikda qo'llash — amaliy misollar

"Sun'iy intellektni kiberxavfsizlikda qo'llash" darsligidagi barcha Python misollari Jupyter daftarlari ko'rinishida.
Darslik 60610700 – "Sun'iy intellekt" ta'lim yo'nalishining 4-kurs talabalari uchun mo'ljallangan.

**Boblar bo'yicha sahifalar (kitobdagi QR kodlar shu sahifalarga olib boradi):** https://mrmsi.github.io/si-kiberxavfsizlik/

## Qanday ishlatiladi

**Google Colab'da (tavsiya etiladi).** Quyidagi jadvaldagi "Open in Colab" belgisini bosing, Google akkauntingiz bilan
kiring va *Runtime → Run all* ni tanlang. Barcha kerakli kutubxonalar Colab'da oldindan o'rnatilgan, ma'lumotlar esa
dasturning o'zida yaratiladi. O'zgartirishlarni saqlash uchun *File → Save a copy in Drive* dan foydalaning.

**O'z kompyuteringizda.**

    git clone https://github.com/mrmsi/si-kiberxavfsizlik.git
    cd si-kiberxavfsizlik
    pip install -r requirements.txt jupyter
    jupyter notebook

Internet bo'lmagan joyda ishlash uchun omborni *Code → Download ZIP* orqali yuklab olish mumkin.

## Daftarlar ro'yxati

| Bob | Misol | Colab |
| --- | --- | --- |
| 1 | [Amaliy misol: qoidaga asoslangan usul va mashinali o'qitish](01-bob/1-1_qoidaga-asoslangan-usul-va-mashinali.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/01-bob/1-1_qoidaga-asoslangan-usul-va-mashinali.ipynb) |
| 1 | [Kengaytirilgan amaliy ish: chegarani ogohlantirishlar byudjeti asosida tanlash](01-bob/1-2_chegarani-ogohlantirishlar-byudjeti-asosida-tanlash.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/01-bob/1-2_chegarani-ogohlantirishlar-byudjeti-asosida-tanlash.ipynb) |
| 2 | [Amaliy misol: veb-server jurnalidan xususiyatlar ajratish](02-bob/2-1_veb-server-jurnalidan-xususiyatlar-ajratish.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/02-bob/2-1_veb-server-jurnalidan-xususiyatlar-ajratish.ipynb) |
| 2 | [Kengaytirilgan amaliy ish: provenans grafida hujum zanjirini tiklash](02-bob/2-2_provenans-grafida-hujum-zanjirini-tiklash.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/02-bob/2-2_provenans-grafida-hujum-zanjirini-tiklash.ipynb) |
| 3 | [Amaliy misol: uchta tasniflash algoritmini taqqoslash](03-bob/3-1_uchta-tasniflash-algoritmini-taqqoslash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/03-bob/3-1_uchta-tasniflash-algoritmini-taqqoslash.ipynb) |
| 3 | [Amaliy misol: xodim faoliyatidagi anomaliyalarni aniqlash](03-bob/3-2_xodim-faoliyatidagi-anomaliyalarni-aniqlash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/03-bob/3-2_xodim-faoliyatidagi-anomaliyalarni-aniqlash.ipynb) |
| 3 | [Kengaytirilgan amaliy ish: faol va tasodifiy belgilashni taqqoslash](03-bob/3-3_faol-va-tasodifiy-belgilashni-taqqoslash.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/03-bob/3-3_faol-va-tasodifiy-belgilashni-taqqoslash.ipynb) |
| 4 | [Kengaytirilgan amaliy ish: belgilash funksiyalari bilan model o'qitish](04-bob/4-1_belgilash-funksiyalari-bilan-model-oqitish.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/04-bob/4-1_belgilash-funksiyalari-bilan-model-oqitish.ipynb) |
| 4 | [Amaliy misol: URL manzillardan xususiyatlar ajratish](04-bob/4-2_url-manzillardan-xususiyatlar-ajratish.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/04-bob/4-2_url-manzillardan-xususiyatlar-ajratish.ipynb) |
| 4 | [Amaliy misol: tasodifiy va vaqt bo'yicha ajratishni taqqoslash](04-bob/4-3_tasodifiy-va-vaqt-boyicha-ajratishni.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/04-bob/4-3_tasodifiy-va-vaqt-boyicha-ajratishni.ipynb) |
| 5 | [Kengaytirilgan amaliy ish: bootstrap yordamida ishonch oraliqlari](05-bob/5-1_bootstrap-yordamida-ishonch-oraliqlari.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/05-bob/5-1_bootstrap-yordamida-ishonch-oraliqlari.ipynb) |
| 5 | [Amaliy misol: "99 foiz aniq" tizim](05-bob/5-2_99-foiz-aniq-tizim.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/05-bob/5-2_99-foiz-aniq-tizim.ipynb) |
| 5 | [Xatolar narxini hisobga olish](05-bob/5-3_xatolar-narxini-hisobga-olish.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/05-bob/5-3_xatolar-narxini-hisobga-olish.ipynb) |
| 6 | [Amaliy misol: o'zbek tilidagi xabarlarni tasniflash](06-bob/6-1_ozbek-tilidagi-xabarlarni-tasniflash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/06-bob/6-1_ozbek-tilidagi-xabarlarni-tasniflash.ipynb) |
| 6 | [Kengaytirilgan amaliy ish: o'xshash domenlarni aniqlovchi kuzatuv tizimi](06-bob/6-2_oxshash-domenlarni-aniqlovchi-kuzatuv-tizimi.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/06-bob/6-2_oxshash-domenlarni-aniqlovchi-kuzatuv-tizimi.ipynb) |
| 7 | [Kengaytirilgan amaliy ish: MinHash yordamida zararli dastur variantlarini guruhlash](07-bob/7-1_minhash-yordamida-zararli-dastur-variantlarini.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/07-bob/7-1_minhash-yordamida-zararli-dastur-variantlarini.ipynb) |
| 7 | [Amaliy misol: entropiya va bayt n-gramlari](07-bob/7-2_entropiya-va-bayt-n-gramlari.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/07-bob/7-2_entropiya-va-bayt-n-gramlari.ipynb) |
| 7 | [Amaliy misol: statik xususiyatlar asosidagi detektor](07-bob/7-3_statik-xususiyatlar-asosidagi-detektor.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/07-bob/7-3_statik-xususiyatlar-asosidagi-detektor.ipynb) |
| 8 | [Amaliy misol: API chaqiruvlari bo'yicha tasniflash](08-bob/8-1_api-chaqiruvlari-boyicha-tasniflash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/08-bob/8-1_api-chaqiruvlari-boyicha-tasniflash.ipynb) |
| 8 | [Kengaytirilgan amaliy ish: n-gram modeli va LSTM axlat chaqiruvlarga qarshi](08-bob/8-2_n-gram-modeli-va-lstm.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/08-bob/8-2_n-gram-modeli-va-lstm.ipynb) |
| 8 | [Amaliy misol: fayllarni tasvirga aylantirish va oilalarga ajratish](08-bob/8-3_fayllarni-tasvirga-aylantirish-va-oilalarga.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/08-bob/8-3_fayllarni-tasvirga-aylantirish-va-oilalarga.ipynb) |
| 8 | [Amaliy misol: shifrlash xatti-harakatini aniqlash](08-bob/8-4_shifrlash-xatti-harakatini-aniqlash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/08-bob/8-4_shifrlash-xatti-harakatini-aniqlash.ipynb) |
| 9 | [Amaliy misol: paketlardan oqimlar va xost xususiyatlariga](09-bob/9-1_paketlardan-oqimlar-va-xost-xususiyatlariga.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/09-bob/9-1_paketlardan-oqimlar-va-xost-xususiyatlariga.ipynb) |
| 9 | [Amaliy misol: ma'lum va yangi hujumlarni aniqlash](09-bob/9-2_malum-va-yangi-hujumlarni-aniqlash.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/09-bob/9-2_malum-va-yangi-hujumlarni-aniqlash.ipynb) |
| 9 | [Kengaytirilgan amaliy ish: uch tashkilot uchun federativ hujumlarni aniqlash modeli](09-bob/9-3_uch-tashkilot-uchun-federativ-hujumlarni.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/09-bob/9-3_uch-tashkilot-uchun-federativ-hujumlarni.ipynb) |
| 10 | [Amaliy misol: uch xil detektor va kontekstning ahamiyati](10-bob/10-1_uch-xil-detektor-va-kontekstning.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/10-bob/10-1_uch-xil-detektor-va-kontekstning.ipynb) |
| 10 | [Kengaytirilgan amaliy ish: mavsumiylikni hisobga oluvchi detektor](10-bob/10-2_mavsumiylikni-hisobga-oluvchi-detektor.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/10-bob/10-2_mavsumiylikni-hisobga-oluvchi-detektor.ipynb) |
| 10 | [Amaliy misol: umumiy chegara va shaxsiy odatiy holat](10-bob/10-3_umumiy-chegara-va-shaxsiy-odatiy.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/10-bob/10-3_umumiy-chegara-va-shaxsiy-odatiy.ipynb) |
| 11 | [Amaliy misol: klaviatura dinamikasi bo'yicha foydalanuvchini tanish](11-bob/11-1_klaviatura-dinamikasi-boyicha-foydalanuvchini-tanish.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/11-bob/11-1_klaviatura-dinamikasi-boyicha-foydalanuvchini-tanish.ipynb) |
| 11 | [Amaliy misol: tranzaksiya belgilari va xatti-harakat belgilari](11-bob/11-2_tranzaksiya-belgilari-va-xatti-harakat.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/11-bob/11-2_tranzaksiya-belgilari-va-xatti-harakat.ipynb) |
| 11 | [Kengaytirilgan amaliy ish: o'tkazma hisoblari tarmog'ini topish](11-bob/11-3_otkazma-hisoblari-tarmogini-topish.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/11-bob/11-3_otkazma-hisoblari-tarmogini-topish.ipynb) |
| 12 | [Amaliy misol: jurnal shablonlari va korrelyatsiya qoidasi](12-bob/12-1_jurnal-shablonlari-va-korrelyatsiya-qoidasi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/12-bob/12-1_jurnal-shablonlari-va-korrelyatsiya-qoidasi.ipynb) |
| 12 | [Amaliy misol: signallarni saralash modeli](12-bob/12-2_signallarni-saralash-modeli.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/12-bob/12-2_signallarni-saralash-modeli.ipynb) |
| 12 | [Kengaytirilgan amaliy ish: ogohlantirishlarni hodisalarga birlashtirish](12-bob/12-3_ogohlantirishlarni-hodisalarga-birlashtirish.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/12-bob/12-3_ogohlantirishlarni-hodisalarga-birlashtirish.ipynb) |
| 13 | [Amaliy misol: qo'shish orqali chetlab o'tish va unga qarshi himoya](13-bob/13-1_qoshish-orqali-chetlab-otish-va.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/13-bob/13-1_qoshish-orqali-chetlab-otish-va.ipynb) |
| 13 | [Amaliy misol: spam filtriga orqa eshik o'rnatish](13-bob/13-2_spam-filtriga-orqa-eshik-ornatish.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/13-bob/13-2_spam-filtriga-orqa-eshik-ornatish.ipynb) |
| 13 | [Kengaytirilgan amaliy ish: a'zolikni aniqlash hujumi](13-bob/13-3_azolikni-aniqlash-hujumi.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/13-bob/13-3_azolikni-aniqlash-hujumi.ipynb) |
| 14 | [Amaliy misol: eng kichik "til modeli"](14-bob/14-1_eng-kichik-til-modeli.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/14-bob/14-1_eng-kichik-til-modeli.ipynb) |
| 14 | [Amaliy misol: prompt in'yeksiya detektori va eng kichik imtiyoz tamoyili](14-bob/14-2_prompt-inyeksiya-detektori-va-eng.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/14-bob/14-2_prompt-inyeksiya-detektori-va-eng.ipynb) |
| 14 | [Kengaytirilgan amaliy ish: bilimlar bazasini zaharlash](14-bob/14-3_bilimlar-bazasini-zaharlash.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/14-bob/14-3_bilimlar-bazasini-zaharlash.ipynb) |
| 15 | [Amaliy misol: tushuntirish yashirin yorliqni fosh etadi](15-bob/15-1_tushuntirish-yashirin-yorliqni-fosh-etadi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/15-bob/15-1_tushuntirish-yashirin-yorliqni-fosh-etadi.ipynb) |
| 15 | [Amaliy misol: taxalluslashning to'g'ri va noto'g'ri usuli](15-bob/15-2_taxalluslashning-togri-va-notogri-usuli.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/15-bob/15-2_taxalluslashning-togri-va-notogri-usuli.ipynb) |
| 15 | [Kengaytirilgan amaliy ish: spam filtrining adolati](15-bob/15-3_spam-filtrining-adolati.ipynb) ¹ | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrmsi/si-kiberxavfsizlik/blob/main/15-bob/15-3_spam-filtrining-adolati.ipynb) |

¹ Kengaytirilgan amaliy ish: darslikning 60610700 – Sun'iy intellekt yo'nalishi versiyasida keltirilgan.

## Natijalar

Har bir daftar oxirida darslikdagi natija va uning tahlili keltirilgan. Tasodifiy sonlar generatorining urug'i
qat'iy belgilangani uchun natija odatda kitobdagi bilan aynan bir xil bo'ladi. Faqat bajarilish vaqti va har safar
yangi yaratiladigan tasodifiy kalitlar farq qilishi mumkin. Barcha daftarlar har oy avtomatik ravishda qayta ishga
tushirib tekshiriladi (*Actions* bo'limi).

## Xato topdingizmi?

*Issues* bo'limida xabar qoldiring: qaysi daftar, qaysi katak va qanday xato chiqqanini yozing.
