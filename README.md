![Okul Logosu](https://user-images.githubusercontent.com/77548130/140867745-a05d7bdd-85d6-4806-8a96-2f3e85aea534.png)


Proje grubu adı: BigLora

Projenin ismi : LoRaChatt



# PROJE RAPORU

## **Proje adı: LoRaChatt**


## **1 ) Proje Özeti**

Dünyada İOT (İnternet of Things) teknolojilerinin gelişmesi ile birlikte uzak mesafeye veri aktarımı ve düşük güç tüketimi önemli bir sorun haline gelmiştir. IOT nesnelere, veri gönderimi ve alımı gibi işlevleri kazandıran temel elemanlar sensörlerdir.

Sensörler, çevreden alınan herhangi bir bilgiyi işleyebilmek için anlamlı veriler haline dönüştürürler. Veri alışverişini gerçekleştirmek için bir ağ yapısı gerekir. Günümüzde daha çok wireless yani kablosuz bağlantı teknolojisi ile bu gerçekleştirilmektedir. Ancak bluetooth, kablolu, kablosuz, hücresel veri gibi günümüz bağlantıları birtakım özellikler açısından bazı dezavantajlara sahiptir. Son kullanıcıların İOT ile etkileşime geçtiği kısım daha çok mobil ve web uygulamalardır. Bluetooth ve kablolu bağlantı, alan genişliği açısından çok kısıtlı bir uzaklık sunar. Kablosuz teknolojilere baktığımızda ise hücresel veri uzaklık konusunda bir kısıt oluşturmazsa da çok fazla maliyet yükü ve güç tüketimi bildirmektedir; WiFi teknolojisi ise yine kısıtlı bir mesafede gerçekleşebilir. Burada hem &quot;mesafe&quot; problemini &quot;maliyet&quot; açısından daha uygun şekilde çözebilmek hem de &quot;güç tüketimi&quot; konusunda daha uzun yıllar verimlilik sağlamak adına LoRa ve LoRaWAN geliştirilmiştir. LoRa, rakip teknolojilere göre çok daha uzun aralıkta çift yönlü iletişime izin verir ve daha güvenilirdir.

Bu gibi büyük sorunlar göz önünde bulundurulduğunda uzak mesafeye veri aktarımı, düşük güç kullanımı ve daha güvenilir sistemli mesajlaşma platformu geliştirilmesi düşünülmektedir.

Bu sistemde 3 adet lora cihazı bulunmaktadır. Mesajları bitlere çevirip lora cihazı ile bir protokol kullanarak diğer lora cihazlarına mesajları aktaracaktır. Klasik sunucu temelli sistem yerine dağıtık haberleşme sistemi kullanılacaktır bu sayede veri güvenliği konusuna yeni bir yaklaşım getirilmektedir

Projede:

- Daha güvenli iki yönlü bağlantılar,
- Daha düşük güç tüketimi,
- Uzun iletişim aralığını
- Uzak mesafelerle kablosuz veri aktarımını sağlayabilmek

Hedeflenmektedir.

Bu sistemdeki özgünlükler şöyle sıralanabilir:

- Sunucu temelli olmayan bir sistemdir.
- Kullanılan cihazların taşınabilirliği sayesinde kurumlara ihtiyaç duyulmayacaktır.
- Kullanıcıya esneklik ve özgürlük sağlayacaktır.

Oluşturulması düşünülen bu sistemin başarıyla sonuçlanması durumunda sistem yüksek güvenlik gerektiren alanlarda, uzak mesafeli görüşmelerde, aciliyet gerektiren durumlarda kolaylık sağlayacaktır. Sistemin başarısı aynı zamanda ticari faaliyetler gerçekleşmesine vesile olabilir. Bu sistem gizlilik gerektiren, mesafe sorunu yaşanan iletişimlerde denebilir.

**Anahtar Kelimeler:** IOT, LoRa, LoRAWan, İletişim, Güvenlik, Dağıtık haberleşme, Mesafe

## **2 ) Amaç ve Hedefler**

İnternetsiz mesajlaşma uygulamaları GSM operatörleri ve baz istasyonlarının çalışmadığı, internet hatlarının sorunlu olduğu zamanlarda (afet,savaş gibi durumlarda) haberleşme sekteye uğramaktadır. Buna çözüm olarak üretilen bluetooth teknolojisinin beraberinde getirdiği mesafe problemine Lora entegreli masaüstü mesajlaşma uygulaması ile bir çözüm getirmek amaçlanmaktadır. Sistemimizde hedeflenen ise daha geniş bir alanda kablosuz veri aktarımı yapabilmek ve bu veri aktarımı sırasında

güç tüketimini en az seviyede tutabilmektir.

Bir başka hedef olarak da IoT&#39;den akıllı şehirlere kadar uzanan bir geliştirme sürecine katkı sağlamaktır.

Diğer internetsiz,kablosuz iletişim teknolojilerine göre başlıca avantajları:

- Üretim maliyeti
- Kapsama alanı
- Batarya süresi

- Mesafe

Bu proje kapsamında yer alabilecek konular şunlardır:

- Katmanlı OSI Referans Modeli ile internetsiz iletişim sağlamak
- FDTI çip kullanarak LoRa&#39;ya talimat vermek
- Peer to Peer ile haberleşme
- İletişimde Açık Anahtar Kriptografisi(PKC) kullanmak

## **3 ) Konu, Kapsam ve Literatür Özeti**

Projenin konusu internetsiz ortamda kablosuz haberleşme ihtiyacını uzun mesafede

gidermektir. Bu kapsamda geliştireceğimiz mesajlaşma uygulaması LoRa modüllerini

kullanarak kablosuz haberleşmeyi sağlayacaktır.

Projemize benzeyen güncel uygulamalar:

● MeshTalk:

OPPO'nun, 2019'da tanıttığı haberleşme uygulamasıdır. Oppo cihazlarının sinyal

aralığında olduğu yerlerde kendi aralarında LAN iletişimini destekleyen &#39;MeshTalk&#39;,

cep telefonu şebekesi, Wi-Fi veya Bluetooth olmadan 3 kilometre mesafedeki OPPO

cihazları arasında kısa mesajların, sesli mesajların ve gerçek zamanlı sesli

aramaların iletimini sağlıyor.

● Bridgefy:

Uygulama, internet olmadığı durumlarda 100 metre çapında Bluetooth üzerinden

mesajlaşmayı sağlıyor. Uygulama bluetooth ve konum servisinden yararlanarak

yakınlarınızla bir afet durumunda, önemli ve acil bir zaman diliminde mesaj

yoluyla iletişim kurmanızı amaçlıyor.

● Signal Offline Messenger:

Signal, herhangi bir internet veya yerel ağ olmadan çalışan, tek ihtiyacı başka bir

sinyal olan haberleşme uygulamasıdır. Uygulama, yakındaki cihazları keşfetmek için

bir sinyal gönderir. Cihazlar bulunduğunda, mevcut kullanıcı listesinde görünürler.

Bu uygulamalar internet olmadan çalışan mesajlaşma uygulamalarına birkaç örnek

oluşturuyor. Bunu Bluetooth, mesh networking(örgüsel ağ) gibi teknolojilerle sağlıyorlar.

Projemizde bu teknolojiler yerine güncel kablosuz haberleşme teknolojileri kullanarak bir

mesajlaşma uygulaması yapmayı hedefliyoruz. Sensörlerle izleme, veri toplamada kullanılan

bazı kablosuz haberleşme teknolojileri şöyledir: Wi-Fi, ZigBee, Bluetooth, LoRa. Biz bu

projede LoRa teknolojisini tercih ettik çünkü Wi-Fi teknolojisi yüksek güç tüketimi sebebiyle

enerji tasarruflu değildir. Bluetooth ve ZigBee teknolojisi ise enerji tasarruflu protokoller

olmalarına rağmen, bu teknolojilerde sinyal ve menzil sınırlaması vardır. Projemizde

kullanacağımız kablosuz haberleşme teknolojisi olan LoRa&#39; nın uzun menzil, düşük güç

tüketimi ve genişletilmiş kapsama alanı özellikleri projemizin ihtiyaçlarını karşılamaktadır.

Proje konusunun literatür araştırması sonucu internet bağlantısı olmadan benzer bazı

mesajlaşma uygulamalarının kullanıldığını saptadık fakat benzerlikleri olduğu kadar

farklılıklarının da olduğunu tespit ettik.

Sistemler arası farklılıklar:

● Haberleşme LoRa modüllerini kullanarak sağlanacaktır.

● Oluşturduğumuz sistemde server olmayacaktır.

## **4 ) Yöntem**

 ### **4.1 ) Genel Tasarım Aşaması**

**4.1.1 ) Sistem Sorunlarının ve Çözümlerinin Belirlenmesi**

Sorun 1 ) Mesaj gönderimi esnasında oluşabilecek güvenlik zafiyetleri.

Çözüm 1 ) Açık Anahtar Kriptografisi (PKC) yöntemi ile gönderici bilgiyi şifrelerken alıcı da şifreyi çözerek bilgiyi okuyabilecektir.

Sorun 2 ) Sadece kısa çaplı bölgelerde çalışması.

Çözüm 2 ) Bir lora cihazı menzilinin yetmediği bir cihaza bilgiyi gönderirken menzilinin yettiği cihazı ara cihaz olarak kullanır.

Sorun 3 ) Mesaj gönderirken eş zamanlı mesaj alımı yapılamaması.

Çözüm 3 ) Bu sorunu çözmek için cihazlar arasında bir zamanlaşma sistemi kuracağız.

Sorun 4 ) Server kullanılmaması :

Çözüm 4 ) Peer to peer bir sistem kullanılacaktır.

**4.1.2 ) Use Case Diyagramının Oluşturulması**

![Use Case](https://user-images.githubusercontent.com/77548130/140867885-8c97d11a-03ed-458d-926a-bc69166b595e.png)


**4.1.3 ) Requirement Diyagramının Oluşturulması**

![Requirement](https://user-images.githubusercontent.com/77548130/140867973-ffdbf649-6414-4e09-ac89-db3df50dc13f.png)


### **4.2 ) Arayüz Tasarım Aşaması**

### **4.3 ) Test Aşamaları**

### **4.4 ) Teknoloji Dökümantasyonu**

## **5 ) Proje Yönetimi ve Ekip**

### **5.1 ) Proje Yönetimi**

**5.1.1 ) Yönetim Düzeni**

![Yönetim Düzeni](https://user-images.githubusercontent.com/77548130/140868087-95252bff-0389-4d19-84f5-86b2764c866d.png)


**5.1.2 ) Zaman Yönetimi Çizelgesi**

**5.1.3 ) Grup İçi Notlandırma Yöntemi**

Grup içi notlandırmaya herkese eşit puan (50) vererek başladık. Her hafta grup üyelerinin toplantılara katılmalarına ve verilen görevleri yerine getirmelerine bakılarak üyelere &quot;+&quot; ve &quot;-&quot; verilecektir. Her hafta notlandırma toplantısında artı ve eksiler göz önüne alınarak grup liderinin kararıyla 100 üzerinden verilen, notların ortalaması 50 olacak şekilde bir notlandırma yapılacak ve kişilere bildirilecektir.

![Grui İçi Notlandırma](https://user-images.githubusercontent.com/77548130/140868151-d245ea51-b482-4550-86e8-8175cfa28b8b.png)


**5.1.4 ) Başarı Ölçütleri**

                                                    **BAŞARI ÖLÇÜTLERİ TABLOSU (\*)**

| IP No | İş Paketi Hedefi | Başarı Ölçütü (%,sayı,ifade,vb.) | Projenin Başarısındaki Önemi (%) |
|----------|-----------|---------|-----------|
| 1 | Proje Analizi | %100 | 25 |
| 2 | Proje Tasarımı | %100 | 20 |
| 3 | Kodlama | %100 | 20 |
| 4 | Test Aşaması | %80 | 15|
| 5 | Dökümantasyon ve Sunum | %80 | 20|

**5.1.5 ) Risk Yönetimi Tablosu**

                                                       **RİSK YÖNETİMİ TABLOSU (\*)**

| IP No | En Önemli Risk(ler)| B Planı|      
|-------|--------------------|--------|
| 1 | Kablosuz haberleşme sisteminde biraz gecikme yapılabilir . | Gecikmelerin önüne geçilmesi için birbirinden farklı portlar kullanılacaktır. |
| 2 | Projenin zamanında yetişmemesi. | Çalışmalar üç gruba ayrıldı ve her grup iki katmana odaklanacak.|
| 3 | Projenin gereksinimlerine ulaşılamaması ya da performansında düşüklük olması. | Her alt grup görevine odaklanacak ve tüm gereksinimlerii karşılamaya çalışacak. |
| 4 | P2P kullanırken veri akışı tıkanıklığı, güvenlik problemi ya da verinin kaynağının göze çarpan olmaması gibi sorunlar yaşanabilir. | Veri akışı tıkanıklığı engellemek için CSMA/CA yöntemi kullanılacak, güvenlik konusunda public key cryptography kullanılacak. |

**Kaynakça:**


[**https://www.aa.com.tr/**](https://www.aa.com.tr/) **tr/sirkethaberleri/bilisim/oppo-ekran-alti-kamera-ve-meshtalk-teknolojilerini-tanitti/651971**

**https://bridgefy.me/**

**https://play.google.com/store/apps/details?id=com.raxis.signalapp&amp;hl=tr&amp;gl=US**

**https://tez.yok.gov.tr/UlusalTezMerkezi/tezDetay.jsp?id=sRGAR8lV6UG9d19rMhf2IQ&amp;no=hHMEgJGV8aruu0AAajVK2A**
