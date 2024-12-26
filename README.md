# YMG-1: Flask Tabanlı RESTful API Uygulaması

YMG-1, Python tabanlı Flask framework'ü kullanarak geliştirilen bir RESTful API uygulamasıdır. Bu proje, belirli matematiksel işlemleri (toplama ve çarpma) gerçekleştiren uç noktalar (endpoints) sağlar.

## Proje Özeti

YMG-1, iki ana uç nokta içerir:
1. **`/iki_topla`**: Bu uç nokta, iki sabit sayıyı (2 + 2) toplayarak sonucu döner.
2. **`/carp`**: Çarpma işlemi yapabilen bir uç nokta sağlar. Bu uç nokta, POST isteği ile bir sayı listesi alır ve bu sayıların çarpımını döner.

## Özellikler

- **GET `/iki_topla`**: Sabit 2 + 2 işlemi ile sonucu döner.
- **POST `/carp`**: JSON formatında bir sayı listesi alır ve bu sayıların çarpımını döner.

## Kullanım

### Uygulamayı Çalıştırma

1. **Python ve Gerekli Kütüphaneler**
   
   YMG-1 uygulamasını çalıştırabilmek için Python 3.x yüklü olmalıdır. Ayrıca, projenin gerekli kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:
   
   ```bash
   pip install -r requirements.txt

2. **Servis Kurulumu (Debian)**
YMG-1 uygulamasını bir Debian sistemi üzerine servis olarak kurmak için aşağıdaki adımları takip edebilirsiniz:

a. **Uygulama Dosyalarını Yerleştirme:**

YMG-1 uygulama dosyalarını /opt/ymg1/ dizinine yerleştirin.

b. **Systemd Servisi Oluşturma:**

Aşağıdaki içeriği kullanarak bir ymg1.service dosyası oluşturun ve /lib/systemd/system/ dizinine yerleştirin

c. **Servisi Başlatma ve Etkinleştirme:**

Servisi başlatmak ve etkinleştirmek için aşağıdaki komutları kullanabilirsiniz:

```bash
sudo systemctl daemon-reload
sudo systemctl start ymg1.service
sudo systemctl enable ymg1.service
