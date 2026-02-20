<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esnaf Araç ve İletişim Rehberi</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 25px;
        }
        .header h2 {
            margin: 0;
            color: #1a73e8;
        }
        .search-box {
            width: 100%;
            padding: 18px;
            font-size: 18px;
            border: 2px solid #ddd;
            border-radius: 12px;
            box-sizing: border-box;
            outline: none;
            transition: border-color 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        .search-box:focus {
            border-color: #1a73e8;
        }
        #results {
            margin-top: 20px;
        }
        .result-card {
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.08);
            border-left: 5px solid #1a73e8;
        }
        .name {
            font-size: 20px;
            font-weight: bold;
            color: #202124;
            margin-bottom: 8px;
        }
        .plate {
            font-size: 18px;
            color: #1a73e8;
            font-weight: bold;
            margin-bottom: 8px;
            background: #e8f0fe;
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .phone {
            font-size: 17px;
            color: #188038;
            font-weight: 500;
        }
        .no-result {
            text-align: center;
            color: #777;
            font-size: 16px;
            margin-top: 30px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h2>Araç Sorgulama Sistemi</h2>
        <p>Plaka (örn: 171), İsim veya Telefon numarası yazın</p>
    </div>

    <input type="text" id="searchInput" class="search-box" placeholder="Aranacak bilgiyi yazın..." autocomplete="off">
    
    <div id="results">
        <div class="no-result">Arama yapmak için yukarıya plaka veya isim yazın.</div>
    </div>
</div>

<script>
    // Tüm fotoğraflardan çıkardığımız eksiksiz veritabanı
    const veriler = [
        {p: "16 M 00002", i: "AHMET KEZKEÇ", t: "0 532 7322736"},
        {p: "16 M 00007", i: "SÜLEYMAN AYDEMİR", t: "0 535 7143956"},
        {p: "16 M 00009", i: "MURAT KAHRİMAN", t: "0 532 6403403"},
        {p: "16 M 00013", i: "PAŞA ÇELİK", t: "0 532 3601648"},
        {p: "16 M 00015", i: "NURULLAH AYDEMİR", t: "0 535 7143956"},
        {p: "16 M 00024", i: "NEJDET ASLAN", t: "0 532 2925341"},
        {p: "16 M 00028", i: "MEHMET İNANÇ", t: "0 536 5162463"},
        {p: "16 M 00034", i: "EMRAH ASLAN", t: "0 536 7674486"},
        {p: "16 M 00035", i: "İBRAHİM AYDIN", t: "0 536 3038070"},
        {p: "16 M 00036", i: "YUSUF AKAGÜNDÜZ", t: "0 532 5115181"},
        {p: "16 M 00036", i: "DERYA KARADAĞ", t: "0 553 2220268"},
        {p: "16 M 00044", i: "HÜSEYİN BABALAR", t: "0 533 3485212"},
        {p: "16 M 00048", i: "AYHAN ÇİMCİK", t: "0 532 3601649"},
        {p: "16 M 00054-050-312", i: "NESLİHAN GÜZELTAŞ", t: "0 532 5012583"},
        {p: "16 M 00058-96", i: "HARUN YAZICI", t: "0 507 2295652"},
        {p: "16 M 00059", i: "NURULLAH ALTUN", t: "0 545 2522058"},
        {p: "16 M 00060", i: "ERCAN EKREM", t: "0 533 3984244"},
        {p: "16 M 00061", i: "LEVENT UMUR", t: "0 532 6046630"},
        {p: "16 M 00062", i: "VELİ PELİT", t: "0 536 2857901"},
        {p: "16 M 00063", i: "RAMAZAN UMUR", t: "0 532 3778914"},
        {p: "16 M 00063", i: "YUSUF İRFAN ATAŞ", t: "0 506 1549215"},
        {p: "16 M 00064", i: "LOKMAN TURGAY", t: "0 536 2698437"},
        {p: "16 M 00067", i: "MEHMET TUNA", t: "0 537 4505009"},
        {p: "16 M 00068", i: "VEYSİ ADNAN YÜKSEL", t: "0 532 6427537"},
        {p: "16 M 00070", i: "MUSTAFA NERGİZ", t: "0 532 4748685"},
        {p: "16 M 00071", i: "YILMAZ ÇOLHAK", t: "0 532 0657047"},
        {p: "16 M 00072", i: "EDİM BOZKURT", t: "0 537 6897347"},
        {p: "16 M 00074", i: "AYŞEGÜL BURKAY", t: "0 533 4276205"},
        {p: "16 M 00075-00065-066", i: "ÖZKAN BOZKURT", t: "0 536 4576815"},
        {p: "16 M 00076", i: "SEÇKİN UMUR", t: "0 532 4259265"},
        {p: "16 M 00077-00087", i: "GÜLBAHAR MEN", t: "0 539 4779192"},
        {p: "16 M 00078", i: "ERCAN ZORBA", t: "0 535 4940525"},
        {p: "16 M 00079", i: "GÖKHAN KAYA", t: "0 532 2071114"},
        {p: "16 M 00080", i: "ERKAN ZORBA", t: "0 532 2154168"},
        {p: "16 M 00081", i: "ALİ BURKAY", t: "0 544 2894234"},
        {p: "16 M 00082", i: "MEHMET YERTÜM", t: "0 537 4626049"},
        {p: "16 M 00083-00095", i: "AHMET NEDİR", t: "0 533 3461839"},
        {p: "16 M 00084", i: "MEHMET BEŞİR KELEŞ", t: "0 532 6751939"},
        {p: "16 M 00085", i: "AYLA ZEYBEL", t: "0 532 6412496"},
        {p: "16 M 00086", i: "MEHMET TAHİR BİLEM", t: "0 532 3425418"},
        {p: "16 M 00088", i: "YADİGAR İLİĞ", t: "0 535 2310199"},
        {p: "16 M 00089", i: "ABDULKADİR TORAMAN", t: "0 532 2327213"},
        {p: "16 M 00090", i: "HÜSEYİN AKTAK", t: "0 536 7354744"},
        {p: "16 M 00091", i: "MEHMET KAYA", t: "0 532 2743050"},
        {p: "16 M 00093", i: "MAHMUT PADIR", t: "0 535 8586115"},
        {p: "16 M 00097", i: "DURMUŞ ÇARIK", t: "0 532 5248628"},
        {p: "16 M 00099-00057", i: "FARUK AMAK", t: "0 532 2771009"},
        {p: "16 M 00100", i: "ŞENEL SEMİZ", t: "0 532 2502374"},
        {p: "16 M 00101", i: "MUSA AŞA", t: "0 535 2475753"},
        {p: "16 M 00102", i: "MUSTAFA YAYLA", t: "0 532 4329580"},
        {p: "16 M 00103", i: "SUPHİ BOZKURT", t: "0 537 0386313"},
        {p: "16 M 00104", i: "MURAT BAYRAM GEZER", t: "0 533 7278997"},
        {p: "16 M 00105", i: "NECDAT İŞLER", t: "0 536 2795425"},
        {p: "16 M 00105", i: "ÖMER KİREÇÇİ", t: "0 532 4178062"},
        {p: "16 M 00106", i: "MEHMET ATA EYBEK", t: "0 535 8641564"},
        {p: "16 M 00108", i: "HAMZA OPUZ", t: "0 554 1664421"},
        {p: "16 M 00109", i: "ENGİN ŞÜLEKOĞLU", t: "0 532 4357344"},
        {p: "16 M 00111", i: "ABUZER KAYA", t: "0 541 4986416"},
        {p: "16 M 00112-092-110-098", i: "İSAK POLAT", t: "0 530 8815724"},
        {p: "16 M 00114", i: "AYGÜL ÖZKAN", t: "0 542 7629246"},
        {p: "16 M 00115", i: "CAFER DAMAR", t: "0 532 3871295"},
        {p: "16 M 00116-10225", i: "METİN GÜZELTAŞ", t: "0 532 5703613"},
        {p: "16 M 00120-031-046", i: "MUHAMMED DEMİR", t: "0 534 9181981"},
        {p: "16 M 00121", i: "HASAN KARAHAN", t: "0 532 7245443"},
        {p: "16 M 00121", i: "SEYDİ EREK", t: "0 533 4722797"},
        {p: "16 M 00122", i: "NURULLAH AYDOĞAN", t: "0 535 3176909"},
        {p: "16 M 00124", i: "SALİH EYLİ", t: "0 532 7870919"},
        {p: "16 M 00127", i: "ADNAN CEYLAN", t: "0 530 4556397"},
        {p: "16 M 00129", i: "ŞEYHMUS YALÇIN", t: "0 532 6167684"},
        {p: "16 M 00129", i: "SELVİNAZ YALÇIN", t: "0 532 6167684"},
        {p: "16 M 00130", i: "MURAT ÖZTEN", t: "0 532 4149274"},
        {p: "16 M 00130", i: "DENİZ KAYAN", t: "0 537 7907827"},
        {p: "16 M 00132-142", i: "ERKAN DURSUN", t: "0 507 9465495"},
        {p: "16 M 00133", i: "BÜLENT GÜLER", t: "0 534 2323349"},
        {p: "16 M 00133", i: "MESUT SEZGİN", t: "0 535 5646439"},
        {p: "16 M 00136", i: "SEBAHATTİN KARDOĞAN", t: "0 534 3893633"},
        {p: "16 M 00138", i: "MURAT YILDIRAK", t: "0 538 0296204"},
        {p: "16 M 00138", i: "AMİNE AKTAR", t: "0 532 1349992"},
        {p: "16 M 00139", i: "FİKRİ BAPLİ", t: "0 505 3752737"},
        {p: "16 M 00139", i: "MEHMET KABA", t: "0 545 9166516"},
        {p: "16 M 00140", i: "HALEF ÖZKAN", t: "0 535 6614224"},
        {p: "16 M 00141", i: "NİHAT SEYMEN", t: "0 536 4276711"},
        {p: "16 M 00143", i: "İSMAİL ASLAN", t: "0 535 6839227"},
        {p: "16 M 00145", i: "MUAMMER YILDIZ", t: "0 532 2110586"},
        {p: "16 M 00148", i: "FUAT GÜNEY", t: "0 535 6369136"},
        {p: "16 M 00149", i: "YUSUF DAMAR", t: "0 532 4197110"},
        {p: "16 M 00149-00115", i: "ŞEFİK TUNÇ", t: "0 532 7708002"},
        {p: "16 M 00150", i: "MEHMET ŞAKİR TOSUN", t: "0 532 6345635"},
        {p: "16 M 00151", i: "MEHMET NURİ KIZILARSLAN", t: "0 533 3266903"},
        {p: "16 M 00155", i: "BURHAN GÜLER", t: "0 546 7713465"},
        {p: "16 M 00158", i: "NECMETTİN KOTAN", t: "0 536 6734916"},
        {p: "16 M 00159", i: "RABİYA NUR YARDIM", t: "0 539 7498956"},
        {p: "16 M 00162", i: "MEHMET REŞİT EKİN", t: "0 535 7474719"},
        {p: "16 M 00163", i: "MELİHA KOTAN", t: "0 532 5499776"},
        {p: "16 M 00165-00014", i: "YUSUF KÖSE", t: "0 532 6560510"},
        {p: "16 M 00166", i: "OSMAN ASLAN", t: "0 532 7057056"},
        {p: "16 M 00167", i: "BARIŞ KORKMAZER", t: "0 530 6149596"},
        {p: "16 M 00167", i: "ÖZGÜR KARAMAN", t: "0 533 9551436"},
        {p: "16 M 00168-00019", i: "ERSEL ER", t: "0 551 1701849"},
        {p: "16 M 00170", i: "MURAT TOSUN", t: "0 536 3467749"},
        {p: "16 M 00172", i: "MEHMET SIDDIK KOTAN", t: "0 532 5499776"},
        {p: "16 M 00173", i: "MUSA DÖNMEZ", t: "0 536 2877883"},
        {p: "16 M 00179", i: "MEHMET HANİF KARAKOYUN", t: "0 536 5093351"},
        {p: "16 M 00186", i: "MEHMET KIZILARSLAN", t: "0 538 6189788"},
        {p: "16 M 00187", i: "ŞEREF ALAN", t: "0 535 5454894"},
        {p: "16 M 00190", i: "HALİL İBRAHİM ALTINTAŞ", t: "0 543 8080047"},
        {p: "16 M 00191", i: "RAMAZAN DÖNMEZ", t: "0 537 4407691"},
        {p: "16 M 00191", i: "MURAT ÖĞÜT", t: "0 553 0698549"},
        {p: "16 M 00193", i: "HÜSEYİN YILMAZ", t: "0 536 3855011"},
        {p: "16 M 00193", i: "TEKİN NERGİZ", t: "0 534 8495598"},
        {p: "16 M 00194-10005", i: "BAYRAM TURHAN", t: "0 532 4060854"},
        {p: "16 M 00195", i: "SAVAŞ PEKER", t: "0 533 6405842"},
        {p: "16 M 00198", i: "KADİR GÜLŞEN", t: "0 536 4985553"},
        {p: "16 M 00199", i: "SİBEL ALP", t: "0 537 3997321"},
        {p: "16 M 00200", i: "KEMAL ORUÇ", t: "0 530 5193276"},
        {p: "16 M 00203", i: "DENİZ YUMUŞAK", t: "0 530 2342068"},
        {p: "16 M 00206", i: "TAHSİN ÇELİK", t: "0 531 0825009"},
        {p: "16 M 00208", i: "ABDULLAH TÜMERDEM", t: "0 530 6957646"},
        {p: "16 M 00208", i: "ZELAL PINAR AKTAN", t: "0 532 3950118"},
        {p: "16 M 00209", i: "ABDÜLBAKİ ÇELİK", t: "0 533 4166393"},
        {p: "16 M 00210", i: "KADİR OKTAY", t: "0 532 3429220"},
        {p: "16 M 00213", i: "HASAN DERMAN", t: "0 532 3429613"},
        {p: "16 M 00214", i: "BURAK BAYTEMUR", t: "0 552 2130123"},
        {p: "16 M 00214", i: "FADİME ÖZATA", t: "0 552 2130123"},
        {p: "16 M 00219", i: "KAMİL ESEN", t: "0 542 4085141"},
        {p: "16 M 00221", i: "HALİT DÖNMEZ", t: "0 536 8116279"},
        {p: "16 M 00222", i: "TEKİN UÇAR", t: "0 532 6743599"},
        {p: "16 M 00226-00010-252", i: "ESRA GÜZELTAŞ", t: "0 553 0480013"},
        {p: "16 M 00231", i: "MERVE ÖZATA", t: "0 552 2130123"},
        {p: "16 M 0023-10273", i: "EROL KOTAN", t: "0 533 5693437"},
        {p: "16 M 00235", i: "NİMET ER", t: "0 532 3454716"},
        {p: "16 M 00238", i: "ARZU ŞİMŞEK", t: "0 535 4320768"},
        {p: "16 M 00239-00253", i: "DAVUT MEYDAN", t: "0 538 4436834"},
        {p: "16 M 00242", i: "CENGİZ EREK", t: "0 535 7484833"},
        {p: "16 M 00242", i: "İBRAHİM EREK", t: "0 546 9753756"},
        {p: "16 M 00243", i: "RAFET OKULEVİ", t: "0 538 2232656"},
        {p: "16 M 00243", i: "BAHATTİN BUDAK", t: "0 533 5294046"},
        {p: "16 M 00245", i: "SEVGİ ALEV", t: "0 530 0180021"},
        {p: "16 M 00246", i: "HALİL İBRAHİM ARZU", t: "0 532 5150040"},
        {p: "16 M 00248", i: "HAVVA ALP", t: "0 537 7407116"},
        {p: "16 M 00250", i: "YASEMİN ÖZBEY", t: "0 537 2668770"},
        {p: "16 M 00254", i: "DAVUT ÖZKAN", t: "0 552 2327922"},
        {p: "16 M 00254", i: "ARJİN SÖNMEZ", t: "0 541 3640049"},
        {p: "16 M 00255", i: "HAKİM KOTAN", t: "0 530 0441554"},
        {p: "16 M 00256", i: "AHMET SİRAÇ MEN", t: "0 541 8874454"},
        {p: "16 M 00258", i: "AYŞE BİLGİN", t: "0 507 9173233"},
        {p: "16 M 00258", i: "ABDULKADİR YALÇIN", t: "0 546 2619811"},
        {p: "16 M 00262", i: "ESET ÖZKAN", t: "0 532 7629246"},
        {p: "16 M 00265", i: "CUMALİ ALP", t: "0 537 3997321"},
        {p: "16 M 00268", i: "ŞÜKRÜ DÜŞ", t: "0 533 7150650"},
        {p: "16 M 00269", i: "CEMAL GAZİ", t: "0 533 4169120"},
        {p: "16 M 00270", i: "MEHMET GÖKSU", t: "0 532 3151607"},
        {p: "16 M 00271", i: "MEHMET CÜNEYT KOTAN", t: "0 506 6925148"},
        {p: "16 M 00273", i: "MELİH GEÇİT", t: "0 532 3958035"},
        {p: "16 M 00276-10271-272", i: "MUSTAFA KOÇDEMİR", t: "0 537 8722944"},
        {p: "16 M 00277", i: "HASAN YÖRÜMEZ", t: "0 537 7201744"},
        {p: "16 M 00279", i: "GÜLMEHMET ARSLAN", t: "0 536 3944969"},
        {p: "16 M 00280", i: "CEVDET BAPLİ", t: "0 532 7260892"},
        {p: "16 M 00281", i: "YUSUF ENGÜDAROĞLU", t: "0 538 9342667"},
        {p: "16 M 00282", i: "EDİP SAĞCAN", t: "0 532 4470569"},
        {p: "16 M 00283-10022", i: "ALİ RIZA KOCAMAN", t: "0 533 5674594"},
        {p: "16 M 00284", i: "ALİ SEYMEN", t: "0 536 4304551"},
        {p: "16 M 00286", i: "NURETTİN ORUÇ", t: "0 532 4555855"},
        {p: "16 M 00286", i: "TAHSİN ÖZTÜRK", t: "0 532 4280122"},
        {p: "16 M 00288", i: "CAFER ÖZKAN", t: "0 535 6614224"},
        {p: "16 M 00295", i: "MUHSİN DURMUŞ", t: "0 537 3955271"},
        {p: "16 M 00296", i: "ÖMER ARSLAN", t: "0 544 5601275"},
        {p: "16 M 00299", i: "EYUP ALP", t: "0 546 7148621"},
        {p: "16 M 00303", i: "FATİH TEKİN", t: "0 535 9360903"},
        {p: "16 M 00304", i: "ÇETİN ÇAKIR", t: "0 538 5591697"},
        {p: "16 M 00306-10145", i: "RAMAZAN CEYLAN", t: "0 532 5983123"},
        {p: "16 M 00309", i: "ORHAN İNAN", t: "0 533 4228116"},
        {p: "16 M 00313", i: "SANİ KARDAŞ", t: "0 532 4055186"},
        {p: "16 M 00315", i: "FAYSAL ÖZCAN", t: "0 532 5472743"},
        {p: "16 M 00315", i: "ÖMER İŞCEN", t: "0 535 8994947"},
        {p: "16 M 00318", i: "MUSTAFA YENİDOĞDU", t: "0 532 7131329"},
        {p: "16 M 00318", i: "İHSAN KURT", t: "0 537 8346570"},
        {p: "16 M 00319", i: "ŞERAFETTİN DÖNMEZ", t: "0 536 4849714"},
        {p: "16 M 00323", i: "MEHMET ATA ALKAN", t: "0 532 7943179"},
        {p: "16 M 00325", i: "SAİT YAŞAR", t: "0 546 6767824"},
        {p: "16 M 00325", i: "ŞABAN ÖZKUL", t: "0 534 2876948"},
        {p: "16 M 00329", i: "KAZIM ÖZMEN", t: "0 532 3708204"},
        {p: "16 M 00330", i: "EMİN ELÇİN", t: "0 532 6513674"},
        {p: "16 M 00332", i: "MEHMET DENİZ", t: "0 532 7131317"},
        {p: "16 M 00334", i: "FİKRET KOÇAK", t: "0 536 4872457"},
        {p: "16 M 00337", i: "ŞAHİN ARSLAN", t: "0 541 9133360"},
        {p: "16 M 00338", i: "ABDURRAHMAN İRVEN", t: "0 532 4508178"},
        {p: "16 M 00340", i: "ÖZCAN ARSLAN", t: "0 532 4637671"},
        {p: "16 M 00341", i: "AYŞE YARDIM", t: "0 532 5215268"},
        {p: "16 M 00342", i: "NEMETULLAH İNANÇ", t: "0 535 4617732"},
        {p: "16 M 00344", i: "FAYSAL ÇOKAN", t: "0 533 6810144"},
        {p: "16 M 00344", i: "MEHMET MUHSİN KELEŞ", t: "0 533 6810141"},
        {p: "16 M 00347", i: "HAMİT KANTARCI", t: "0 532 3912379"},
        {p: "16 M 00347", i: "ERHAN ERDUMAN", t: "0 538 9837600"},
        {p: "16 M 00350-055", i: "YÜKSEL ARSLAN", t: "0 537 5116278"},
        {p: "16 M 00351", i: "MUSTAFA ERTAN", t: "0 535 5819658"},
        {p: "16 M 00351", i: "AYŞE AYDIN", t: "0 542 6169908"},
        {p: "16 M 00352", i: "MUHAMMED FATİH DEMİR", t: "0 543 2606127"},
        {p: "16 M 00352", i: "SİNAN ÇINAR", t: "0 536 4093080"},
        {p: "16 M 00355", i: "MEHMET GÜRBÜZ", t: "0 535 8569992"},
        {p: "16 M 10001", i: "UMADETTİN OKULEVİ", t: "0 532 7405067"},
        {p: "16 M 10002", i: "ŞÜKRÜ ÖZMEN", t: "0 535 9652577"},
        {p: "16 M 10003", i: "FERİT ÇELİK", t: "0 539 6464013"},
        {p: "16 M 10004", i: "ERGİN ÇELİK", t: "0 532 4064856"},
        {p: "16 M 10006", i: "HASAN HÜSEYİN TURHAN", t: "0 530 5606505"},
        {p: "16 M 10007", i: "RÜSTEM MUTLU", t: "0 533 5658733"},
        {p: "16 M 10008", i: "MUAMMER TOSO", t: "0 538 7038816"},
        {p: "16 M 10009", i: "EKREM GÜRBÜZ", t: "0 535 3518360"},
        {p: "16 M 10010", i: "BAYRAM GÜRBÜZ", t: "0 539 6951194"},
        {p: "16 M 10011", i: "VAHDETTİN YARDIM", t: "0 549 3707610"},
        {p: "16 M 10012", i: "NİZAMEDDİN YARDIM", t: "0 542 4519856"},
        {p: "16 M 10013", i: "NUSRETTİN YARDIM", t: "0 532 5215368"},
        {p: "16 M 10014", i: "KEMALETTİN YARDIM", t: "0 542 4519856"},
        {p: "16 M 10015", i: "AYŞE CAN", t: "0 538 2951502"},
        {p: "16 M 10016-00200", i: "MUSTAFA CAN", t: "0 533 5703810"},
        {p: "16 M 10017", i: "TURGUT KARAKURT", t: "0 532 4456904"},
        {p: "16 M 10018", i: "HAMDULLAH YILDIZ", t: "0 532 6380273"},
        {p: "16 M 10019", i: "FEYAZ ÖZKAN", t: "0 552 4318716"},
        {p: "16 M 10020", i: "NİHAT HASANOĞLU", t: "0 530 6957646"},
        {p: "16 M 10021", i: "AHMET GETİREN", t: "0 544 5032803"},
        {p: "16 M 10023", i: "YUSUF İNAN", t: "0 535 7979164"},
        {p: "16 M 10024", i: "SAMET HARMAN", t: "0 532 3425923"},
        {p: "16 M 10025", i: "AHMET BEYTAR", t: "0 532 4726447"},
        {p: "16 M 10026", i: "AZİZ ALP", t: "0 532 0672936"},
        {p: "16 M 10027", i: "MEHMET FARUK AKTAŞ", t: "0 532 2703742"},
        {p: "16 M 10028", i: "İLHAN AKTAŞ", t: "0 544 3600447"},
        {p: "16 M 10029", i: "REŞAT KAYGIN", t: "0 507 7509649"},
        {p: "16 M 10030", i: "SEMİH TAYIR", t: "0 536 8471997"},
        {p: "16 M 10031-32", i: "MEHMET SALAH GÜNGÖR", t: "0 506 1226473"},
        {p: "16 M 10033", i: "BEDRETTİN ÖZDEMİR", t: "0 533 4149235"},
        {p: "16 M 10034", i: "MEHMET TUNÇ", t: "0 532 6609051"},
        {p: "16 M 10035", i: "İSMAİL MUTLU", t: "0 536 2777452"},
        {p: "16 M 10036", i: "MUHAMMED DÖNMEZ", t: "0 505 9724849"},
        {p: "16 M 10037", i: "SAADETTİN ÖZCANLIGİLLER", t: "0 535 9583791"},
        {p: "16 M 10038", i: "YUSUF AKAY", t: "0 542 3961819"},
        {p: "16 M 10039", i: "OSMAN BAYTEMUR", t: "0 546 2770123"},
        {p: "16 M 10040", i: "BÜLENT ŞAHİN", t: "0 532 5600344"},
        {p: "16 M 10041", i: "RAMAZAN ÇALAN", t: "0 532 2218921"},
        {p: "16 M 10042", i: "AZZEDİN KARAKUŞ", t: "0 536 3571821"},
        {p: "16 M 10043", i: "CEZMİ ÖZDEMİR", t: "0 542 6400420"},
        {p: "16 M 10044", i: "İDRİS DÖNMEZ", t: "0 544 9101786"},
        {p: "16 M 10045", i: "ENVER ÖNEL", t: "0 532 6829549"},
        {p: "16 M 10046", i: "İDRİS İPEK", t: "0 533 6782168"},
        {p: "16 M 10047", i: "NİLÜFER BULCA", t: "0 537 3257085"},
        {p: "16 M 10048", i: "BÜLENT BULCA", t: "0 533 3530428"},
        {p: "16 M 10049", i: "HAKDAN SANCAK", t: "0 532 5011644"},
        {p: "16 M 10049", i: "YAVUZ KIZILARSLAN", t: "0 535 6615136"},
        {p: "16 M 10050", i: "ERCAN KIZILARSLAN", t: "0 536 3219049"},
        {p: "16 M 10051", i: "KAMİL TURHAN", t: "0 533 6890470"},
        {p: "16 M 10052", i: "AHMET TURHAN", t: "0 532 4060854"},
        {p: "16 M 10053-00157", i: "HASAN ALP", t: "0 532 6600086"},
        {p: "16 M 10054-00157", i: "SALİH ALP", t: "0 535 8559510"},
        {p: "16 M 10055", i: "ERCAN AKYÜZ", t: "0 532 6010141"},
        {p: "16 M 10056", i: "CEM ANLATICI", t: "0 534 7632616"},
        {p: "16 M 10057", i: "FERZENDE YILDIZ", t: "0 546 5538584"},
        {p: "16 M 10058", i: "HAKAN YUMUŞAK", t: "0 546 2962141"},
        {p: "16 M 10059", i: "AYDIN BALKAYA", t: "0 541 5417208"},
        {p: "16 M 10060", i: "FIRAT BALKAYA", t: "0 531 4215444"},
        {p: "16 M 10061", i: "KEREM AKALIN", t: "0 553 0025500"},
        {p: "16 M 10062", i: "BEDRETTİN ARSLAN", t: "0 536 5783474"},
        {p: "16 M 10063", i: "EMRAH İŞCEN", t: "0 535 2647649"},
        {p: "16 M 10064", i: "KENAN ARSLAN", t: "0 539 2016449"},
        {p: "16 M 10065", i: "GÜRSEL DENİZ", t: "0 533 5205110"},
        {p: "16 M 10066", i: "İLKAN ŞAHİN", t: "0 532 4825245"},
        {p: "16 M 10067", i: "METİN BALKAYA", t: "0 541 5417208"},
        {p: "16 M 10068", i: "ŞAKİR ÖZKAN", t: "0 542 7629246"},
        {p: "16 M 10069", i: "MEHMET SABRİ GEÇER", t: "0 536 6770136"},
        {p: "16 M 10070", i: "ARİFE TEKİN ÇAYHAN", t: "0 538 3466438"},
        {p: "16 M 10071", i: "ALİ ÇALAN", t: "0 534 6676954"},
        {p: "16 M 10072", i: "MUSTAFA TEKDEMİR", t: "0 532 1584121"},
        {p: "16 M 10073", i: "CİHAT AYDIN", t: "0 530 8948556"},
        {p: "16 M 10074", i: "TURGUT ŞAHİN", t: "0 532 4476752"},
        {p: "16 M 10075", i: "ORHAN BAYRAM", t: "0 533 6411855"},
        {p: "16 M 10076", i: "AHMET KÖKLÜ", t: "0 536 3570249"},
        {p: "16 M 10077", i: "YAVUZ ESER", t: "0 533 2269272"},
        {p: "16 M 10078", i: "EMİN DEMİR", t: "0 532 5538799"},
        {p: "16 M 10079", i: "FETHİ İŞİTTİREN", t: "0 533 4359851"},
        {p: "16 M 10080", i: "VEDAT SÖNMEZ", t: "0 537 2378624"},
        {p: "16 M 10081", i: "NECATİ ÖZTÜRK", t: "0 532 5659306"},
        {p: "16 M 10082", i: "SEVİL ORUÇ", t: "0 539 3498802"},
        {p: "16 M 10083", i: "SEDAT ARSLAN", t: "0 535 2385293"},
        {p: "16 M 10084", i: "ENES ARSLAN", t: "0 537 5762649"},
        {p: "16 M 10085", i: "MEHMET ARSLAN", t: "0 546 8913446"},
        {p: "16 M 10086", i: "İZZETTİN ARSLAN", t: "0 534 0810007"},
        {p: "16 M 10087", i: "MEHMET MİSBAH ALKAN", t: "0 532 4151203"},
        {p: "16 M 10088", i: "BİLAL ALKAN", t: "0 537 3723442"},
        {p: "16 M 10089", i: "ÖZCAN ÖZTÜRK", t: "0 533 4665822"},
        {p: "16 M 10090", i: "ÖMER SAKİN", t: "0 535 6110924"},
        {p: "16 M 10091", i: "YAŞAR BAYTEMÜR", t: "0 533 7619222"},
        {p: "16 M 10092", i: "SEVİNÇ COŞKUN", t: "0 535 9827384"},
        {p: "16 M 10093", i: "AHMET KURT", t: "0 537 8346570"},
        {p: "16 M 10094", i: "YUNUS ÖNEN", t: "0 535 4858367"},
        {p: "16 M 10095", i: "FİRDEVS BALICI", t: "0 535 6876556"},
        {p: "16 M 10096", i: "YUNUS KAPŞİGAY", t: "0 538 8860477"},
        {p: "16 M 10097", i: "YÜKSEL KAYGIN", t: "0 530 4669030"},
        {p: "16 M 10098", i: "SEDAT SERKAN KAÇAN", t: "0 505 0437465"},
        {p: "16 M 10099", i: "MUHAMMETBAHTİYA TEKİN", t: "0 534 2550049"},
        {p: "16 M 10100", i: "ŞAFAK AYYILDIZ", t: "0 551 9506929"},
        {p: "16 M 10101", i: "MEHMET YAŞAR DÖNMEZ", t: "0 535 3448075"},
        {p: "16 M 10102", i: "MUHSİN DÖNMEZ", t: "0 506 7359630"},
        {p: "16 M 10103", i: "ENGİN KAYGIN", t: "0 537 3489037"},
        {p: "16 M 10104", i: "MEHMET NEDİM KAŞTAŞ", t: "0 531 0241349"},
        {p: "16 M 10105-00319", i: "MEDENİ DÖNMEZ", t: "0 535 9694706"},
        {p: "16 M 10106", i: "HÜSEYİN TUTKUN", t: "0 533 3613685"},
        {p: "16 M 10107", i: "RECEP SEVİNÇ", t: "0 536 7650838"},
        {p: "16 M 10108", i: "YAŞAR TEPELİOĞLU", t: "0 532 5256831"},
        {p: "16 M 10109", i: "ÖZCAN SAYLA", t: "0 535 3593182"},
        {p: "16 M 10110", i: "SÜLEYMAN SAYLA", t: "0 532 7779295"},
        {p: "16 M 10111", i: "DURAK ÖZAY", t: "0 532 5634982"},
        {p: "16 M 10112", i: "ÖNDER ERDUMAN", t: "0 533 3698916"},
        {p: "16 M 10113", i: "VEYSİ KAYNAR", t: "0 536 9235645"},
        {p: "16 M 10114", i: "MEHMET ŞERİF SELİK", t: "0 533 2121491"},
        {p: "16 M 10115", i: "MUSTAFA SAKİN", t: "0 536 7843347"},
        {p: "16 M 10116-066", i: "SELÇUK UMUR", t: "0 531 7934870"},
        {p: "16 M 10117", i: "YILMAZ KARADAĞ", t: "0 532 6458989"},
        {p: "16 M 10118", i: "BARIŞ BULUT", t: "0 541 6184740"},
        {p: "16 M 10119", i: "VEYSİ SEZGİN", t: "0 532 6345637"},
        {p: "16 M 10120", i: "FEVZİ SEZGİN", t: "0 533 3074213"},
        {p: "16 M 10121", i: "RAHMAN NEFİS", t: "0 536 4885342"},
        {p: "16 M 10122", i: "ERKUT ERDEM", t: "0 533 0255333"},
        {p: "16 M 10123", i: "NEDİP MURATAKAN", t: "0 537 6121090"},
        {p: "16 M 10124", i: "VEDAT ÖZKAN", t: "0 535 5655129"},
        {p: "16 M 10125-126-008", i: "MEHMET AYDEMİR", t: "0 532 5680915"},
        {p: "16 M 10127", i: "MİRZE MEHMET ARSLAN", t: "0 536 4344349"},
        {p: "16 M 10128", i: "İLHAN ÖZMEN", t: "0 553 0659049"},
        {p: "16 M 10129", i: "ERŞAN KETECİ", t: "0 536 8692563"},
        {p: "16 M 10130", i: "KADRİ KARDAŞ", t: "0 530 0602758"},
        {p: "16 M 10131", i: "MEHMET NACİ DURGUN", t: "0 532 7962299"},
        {p: "16 M 10132", i: "ŞÜKRÜ EREK", t: "0 535 5855992"},
        {p: "16 M 10133", i: "MUAMMER YİĞİT", t: "0 536 6688788"},
        {p: "16 M 10134", i: "MEMET ŞİRİN EVİN", t: "0 532 7718689"},
        {p: "16 M 10135", i: "FİKRİ KARADEMİR", t: "0 532 3854215"},
        {p: "16 M 10136", i: "MUHAMMET KARADEMİR", t: "0 533 1604767"},
        {p: "16 M 10137", i: "GÜRSOY TURHAN", t: "0 535 2712342"},
        {p: "16 M 10138", i: "HALİM ZAİMOĞLU", t: "0 532 2110586"},
        {p: "16 M 10139", i: "BİLAL MEMİŞOĞLU", t: "0 532 6628284"},
        {p: "16 M 10140", i: "SAİM KOÇAK", t: "0 532 5959830"},
        {p: "16 M 10141", i: "BEHÇET MEN", t: "0 535 3279812"},
        {p: "16 M 10142", i: "SİNAN MEN", t: "0 541 9467572"},
        {p: "16 M 10143", i: "EROL GÜREL", t: "0 530 9346043"},
        {p: "16 M 10144", i: "ŞEMSETTİN YILDIZ", t: "0 533 0324213"},
        {p: "16 M 10146", i: "TOLGA CEYLAN", t: "0 553 2806336"},
        {p: "16 M 10147", i: "SEYİDGÜL ER", t: "0 532 6356295"},
        {p: "16 M 10148", i: "ÖMER CANBAY", t: "0 535 4632627"},
        {p: "16 M 10149", i: "ESER TAVLİ", t: "0 536 3573649"},
        {p: "16 M 10150", i: "EROL FERİK", t: "0 533 2042029"},
        {p: "16 M 10151", i: "HATİCE BÖRÜ", t: "0 532 2451110"},
        {p: "16 M 10152", i: "MEHMET REFİK ALKAN", t: "0 535 2197429"},
        {p: "16 M 10153", i: "YAVUZ ÇAKMAK", t: "0 532 3446073"},
        {p: "16 M 10154", i: "HAMDULLAH ÖZKAN", t: "0 536 7136040"},
        {p: "16 M 10155", i: "MESUT FERİK", t: "0 537 8112201"},
        {p: "16 M 10156", i: "ŞEMSETTİN EREK", t: "0 537 4086851"},
        {p: "16 M 10157", i: "BURHAN BALKAYA", t: "0 537 3557142"},
        {p: "16 M 10158", i: "KENAN ÖNGEL", t: "0 536 8142608"},
        {p: "16 M 10159-160-00316", i: "MURAT IŞIK", t: "0 532 4060530"},
        {p: "16 M 10161", i: "MESUT GEZEK", t: "0 534 4428837"},
        {p: "16 M 10161", i: "KADRİ ÇİFÇİLER", t: "0 531 8524001"},
        {p: "16 M 10162", i: "OĞUZHAN DÜNDAR", t: "0 539 2292370"},
        {p: "16 M 10163", i: "AHMET OSKAY", t: "0 533 3422156"},
        {p: "16 M 10164", i: "ADEM KARADEMİR", t: "0 538 6918834"},
        {p: "16 M 10165", i: "NEVZAT ERDOĞAN", t: "0 544 5611656"},
        {p: "16 M 10166", i: "ÜVEYS KEZKEÇ", t: "0 551 5912349"},
        {p: "16 M 10167", i: "FATİH KEZKEÇ", t: "0 534 3221949"},
        {p: "16 M 10168", i: "HASANALİ ÖZTÜRK", t: "0 532 0585586"},
        {p: "16 M 10169", i: "MEHMET KARABULUT", t: "0 532 6632539"},
        {p: "16 M 10170", i: "MEHMET KARABULUT", t: "0 549 4635863"},
        {p: "16 M 10171", i: "ALİ GÜLER", t: "0 530 7832262"},
        {p: "16 M 10172", i: "ORHAN ŞAHİN", t: "0 536 6343738"},
        {p: "16 M 10173", i: "OSMAN KORKMAZER", t: "0 532 7641605"},
        {p: "16 M 10174", i: "ABDURRAZZAK KURTAY", t: "0 537 9392614"},
        {p: "16 M 10175", i: "MEHMET SIDDIK PEKER", t: "0 532 6808478"},
        {p: "16 M 10176", i: "TAHSİN PEKER", t: "0 532 3269737"},
        {p: "16 M 10177", i: "HÜSEYİN GÖKSU", t: "0 535 8973644"},
        {p: "16 M 10178", i: "HAKAN GÖKSU", t: "0 507 0446895"},
        {p: "16 M 10179", i: "ŞEYHMUS BAŞ", t: "0 532 5788147"},
        {p: "16 M 10180", i: "HAŞİM KARAHAN", t: "0 532 7245443"},
        {p: "16 M 10181", i: "ZÜLKİF YUMUŞAK", t: "0 532 2875707"},
        {p: "16 M 10182", i: "METİN DURMAZ", t: "0 543 8501964"},
        {p: "16 M 10183", i: "SELAHATTİN ENGÜDAROĞLU", t: "0 533 3440216"},
        {p: "16 M 10184", i: "KAMRAN YILDIZ", t: "0 535 4023826"},
        {p: "16 M 10185", i: "MURAT DEMİR", t: "0 553 0961649"},
        {p: "16 M 10186", i: "MEHMET EMİN ÇINAR", t: "0 536 5999341"},
        {p: "16 M 10187", i: "ŞEFİK DİNÇER", t: "0 535 4620006"},
        {p: "16 M 10188", i: "ABDURRAHİM GÜRKAN", t: "0 536 4179435"},
        {p: "16 M 10189", i: "SONER ALP", t: "0 539 4627508"},
        {p: "16 M 10190", i: "AYDIN ARSLAN", t: "0 537 2306539"},
        {p: "16 M 10191-0052", i: "ATİYE KELEŞ", t: "0 533 6810141"},
        {p: "16 M 10192-00354", i: "HİLAL BURKAY", t: "0 536 6152029"},
        {p: "16 M 10193", i: "ERKAN GÜLER", t: "0 536 6920176"},
        {p: "16 M 10194", i: "ERHAN GÜLER", t: "0 535 2955877"},
        {p: "16 M 10195", i: "AGİT ÖZKAN", t: "0 532 7629246"},
        {p: "16 M 10196", i: "MEHMET ZEKİ ÖZKAN", t: "0 532 7087236"},
        {p: "16 M 10197", i: "SAİT TOSUN", t: "0 536 8974549"},
        {p: "16 M 10198", i: "SİRACETTİN BALKAYA", t: "0 532 1575349"},
        {p: "16 M 10199", i: "LEVENT HAKER", t: "0 533 5627328"},
        {p: "16 M 10200", i: "SADİ EREN", t: "0 532 3160371"},
        {p: "16 M 10201", i: "KADİR KUTLU", t: "0 536 5866885"},
        {p: "16 M 10202", i: "İSMAİL KORKMAZ", t: "0 532 2246091"},
        {p: "16 M 10203", i: "HÜSEYİN GEÇER", t: "0 536 6770136"},
        {p: "16 M 10204", i: "KADRİ BİÇER", t: "0 543 2510417"},
        {p: "16 M 10205", i: "YAHYA EREK", t: "0 505 6609092"},
        {p: "16 M 10206", i: "ÖMER KARABAŞ", t: "0 533 5576416"},
        {p: "16 M 10207", i: "M.SİRİN KOTAN", t: "0 530 1757946"},
        {p: "16 M 10208", i: "GÖKHAN LEVENT", t: "0 539 2367949"},
        {p: "16 M 10209", i: "NEDİM ELÇİN", t: "0 534 5991621"},
        {p: "16 M 10210", i: "NACİ KORKMAZER", t: "0 532 2240991"},
        {p: "16 M 10211", i: "EKREM ÖTER", t: "0 530 3218347"},
        {p: "16 M 10212", i: "OKTAY ÇELİK", t: "0 532 2932294"},
        {p: "16 M 10213", i: "RIDVAN DÖNMEZ", t: "0 538 8822367"},
        {p: "16 M 10214", i: "VESFEDDİN GÜRBÜZ", t: "0 535 2465977"},
        {p: "16 M 10215-10216", i: "İRFAN ÇİMCİK", t: "0 532 2622368"},
        {p: "16 M 10217", i: "KENAN DÖNMEZ", t: "0 545 9567749"},
        {p: "16 M 10218", i: "İBRAHİM MEN", t: "0 535 0624063"},
        {p: "16 M 10219", i: "ONUR KAYA", t: "0 532 4115253"},
        {p: "16 M 10220", i: "CANER KAYA", t: "0 532 4115253"},
        {p: "16 M 10221", i: "ÖZCAN AYDEMİR", t: "0 545 2163406"},
        {p: "16 M 10222", i: "YUSUF ABAY", t: "0 536 3142109"},
        {p: "16 M 10223", i: "NASIR YUMUŞAK", t: "0 537 2578415"},
        {p: "16 M 10224", i: "BARIŞ GÜZELTAŞ", t: "0 542 3451172"},
        {p: "16 M 10226", i: "ÖNDER GÜZELTAŞ", t: "0 532 5012583"},
        {p: "16 M 10227", i: "DAVUT YAPICI", t: "0 533 8103239"},
        {p: "16 M 10228", i: "ROHAT YUMUŞAK", t: "0 542 5788798"},
        {p: "16 M 10229", i: "YILMAZ ESEN", t: "0 532 4774611"},
        {p: "16 M 10230", i: "KEMALETTİN BERK", t: "0 537 4576331"},
        {p: "16 M 10231", i: "ELİF KÖSE", t: "0 532 6560510"},
        {p: "16 M 10232", i: "MESUT AYDIN", t: "0 541 5691280"},
        {p: "16 M 10233", i: "İSMET USLU", t: "0 532 4871910"},
        {p: "16 M 10234-00219", i: "AHMET CEMİL IŞIK", t: "0 536 7108316"},
        {p: "16 M 10235-10236", i: "CANİP GÜLMEZ", t: "0 532 3429220"},
        {p: "16 M 10237", i: "ERKAN KIZILARSLAN", t: "0 537 6421649"},
        {p: "16 M 10238", i: "AYTAÇ YÖRÜMEZ", t: "0 554 2364674"},
        {p: "16 M 10239", i: "SALİM ENGÜDAROĞLU", t: "0 534 5601983"},
        {p: "16 M 10240-00201", i: "ABDULGAFUR GEYLANİ", t: "0 532 2725241"},
        {p: "16 M 10241", i: "MUSTAFA ŞAHİN", t: "0 535 9660215"},
        {p: "16 M 10242", i: "AHMET ÖZKORKMAZ", t: "0 538 3784302"},
        {p: "16 M 10243", i: "TAKYEDDİN OKULEVİ", t: "0 533 3800456"},
        {p: "16 M 10244", i: "MAHMUT AYDIN", t: "0 536 2438590"},
        {p: "16 M 10245", i: "KÖKSAL DÜNDAR", t: "0 536 3919129"},
        {p: "16 M 10246", i: "AHMET ÇOBUR", t: "0 553 6294102"},
        {p: "16 M 10247", i: "İSMAİL ÖZAN", t: "0 543 2890175"},
        {p: "16 M 10248", i: "SÜLEYMAN ERDUMAN", t: "0 534 2612761"},
        {p: "16 M 10249", i: "FEVZİ ÖZAY", t: "0 535 6916832"},
        {p: "16 M 10250", i: "KADRİ ÖZAY", t: "0 530 8937730"},
        {p: "16 M 10251", i: "YAHYA TURHAN", t: "0 553 0558582"},
        {p: "16 M 10252", i: "ZEKERİYA TURHAN", t: "0 534 6866276"},
        {p: "16 M 10253", i: "CAHİT AKDENİZ", t: "0 533 3592574"},
        {p: "16 M 10254", i: "RİZVAN KOCAK", t: "0 533 3656899"},
        {p: "16 M 10255", i: "İSMAİL KAYA", t: "0 532 2139826"},
        {p: "16 M 10256", i: "AZİZ ÖZKAN", t: "0 536 4773198"},
        {p: "16 M 10257", i: "REYSİ KARACA", t: "0 537 2620138"},
        {p: "16 M 10258", i: "KAMİL MEHMET AYDIN", t: "0 541 5691280"},
        {p: "16 M 10259", i: "ÖZCAN ASLAN", t: "0 537 6393898"},
        {p: "16 M 10260", i: "CİHAT ASLAN", t: "0 543 4693483"},
        {p: "16 M 10261", i: "ERTAN EYLİ", t: "0 532 2264389"},
        {p: "16 M 10262", i: "MUSTAFA ÇAKANLAR", t: "0 533 5501859"},
        {p: "16 M 10263", i: "FATMA ÇOBUR", t: "0 553 6294102"},
        {p: "16 M 10264", i: "EMİN KOTAN", t: "0 542 5300829"},
        {p: "16 M 10265", i: "HAYRULLAH YILMAZ", t: "0 532 1553252"},
        {p: "16 M 10266-00021", i: "ÖZBEY KOTAN", t: "0 532 7205851"},
        {p: "16 M 10267", i: "AHMET ERDAL YILMAZ", t: "0 530 0317420"},
        {p: "16 M 10268", i: "BÜLENT YILMAZ", t: "0 535 6290992"},
        {p: "16 M 10269-10270", i: "RIDVAN YALÇIN", t: "0 532 6712173"},
        {p: "16 M 10274", i: "YÜKSEL SOYLU", t: "0 536 7919997"},
        {p: "16 M 10275", i: "NAHİT BAPLİ", t: "0 545 9091649"},
        {p: "16 M 10276", i: "KEREM BAPLİ", t: "0 532 6356204"},
        {p: "16 M 10277", i: "YUNUS DÖNMEZ", t: "0 537 5826298"},
        {p: "16 M 10278", i: "İSMET AKDAĞ", t: "0 532 6061669"},
        {p: "16 M 10281", i: "ŞABAN AKTAR", t: "0 532 1349992"},
        {p: "16 M 10282", i: "NİHAT OKULEVİ", t: "0 533 2559480"},
        {p: "16 M 10283", i: "MUSTAFA ACELECİ", t: "0 532 5482770"},
        {p: "16 M 10284-00183", i: "İDRİS GÜRKAN", t: "0 531 9709751"},
        {p: "16 M 10285", i: "ÖMER KEZKEÇ", t: "0 553 6530949"},
        {p: "16 M 10286", i: "TURGAY YARDIM", t: "0 542 4519856"},
        {p: "16 M 10287-10288", i: "MUHAMMED EMRE ALPAR", t: "0 555 8930399"},
        {p: "16 M 10289-10290-029", i: "BURHAN GÜZELTAŞ", t: "0 543 9497084"},
        {p: "16 M 10291-10292", i: "MUZAFFER AKTAŞ", t: "0 534 3675354"},
        {p: "16 M 0073-113-10279-280", i: "ZEYNİ BURKAY", t: "0 533 4376205"},
        {p: "16 M 0107-069-0175-094", i: "DAVUT İLİĞ", t: "0 535 2310199"}
    ];

    const searchInput = document.getElementById('searchInput');
    const resultsDiv = document.getElementById('results');

    // Boşlukları ve gereksiz karakterleri temizleyip aramayı kolaylaştıran fonksiyon
    function temizle(metin) {
        return metin.toLowerCase().replace(/\s+/g, '');
    }

    searchInput.addEventListener('input', function(e) {
        const aramaMetni = temizle(e.target.value);
        
        // Eğer arama kutusu boşsa sonuçları gizle
        if (aramaMetni.length === 0) {
            resultsDiv.innerHTML = '<div class="no-result">Arama yapmak için yukarıya plaka veya isim yazın.</div>';
            return;
        }

        // Veritabanında filtreleme yap
        const sonuclar = veriler.filter(kisi => {
            const plaka = temizle(kisi.p);
            const isim = temizle(kisi.i);
            const telefon = temizle(kisi.t);
            
            // "16m" kısmını çıkarıp sadece rakamlarda arama yapmak için (örneğin 171 yazdığında 00171'i bulması için)
            const sadeceRakamPlaka = plaka.replace(/[^0-9]/g, ''); 

            return sadeceRakamPlaka.includes(aramaMetni) || 
                   isim.includes(aramaMetni) || 
                   telefon.includes(aramaMetni) ||
                   plaka.includes(aramaMetni); // "16M" yazarak aranmak istenirse diye
        });

        // Ekrana yazdırma
        resultsDiv.innerHTML = '';
        if (sonuclar.length === 0) {
            resultsDiv.innerHTML = '<div class="no-result">Eşleşen sonuç bulunamadı.</div>';
        } else {
            sonuclar.forEach(kisi => {
                const card = document.createElement('div');
                card.className = 'result-card';
                card.innerHTML = `
                    <div class="name">${kisi.i}</div>
                    <div class="plate">${kisi.p}</div>
                    <div class="phone">${kisi.t}</div>
                `;
                resultsDiv.appendChild(card);
            });
        }
    });
</script>

</body>
</html>
