# kodlama.io
kodlama.io eğitimleri ödevleri için oluşturulmuş alan


Pytest, Python için bir test çerçevesidir ve test yazmanızı kolaylaştırmak için birçok özellik sağlar. 
Pytest, testlerinizi dekoratörler kullanarak özelleştirmenize olanak tanır. Bazı yaygın kullanılan pytest dekoratörleri şunlardır:

@pytest.fixture: Bu dekoratör, test fonksiyonlarının ihtiyaç duydukları bağımlılıkları ayarlamak için kullanılır. 
Örneğin, bir test fonksiyonunun bir veritabanı bağlantısına ihtiyacı varsa, bu bağımlılığı @pytest.fixture ile bir bağımlılık olarak tanımlayabilirsiniz.

@pytest.mark.parametrize: Bu dekoratör, aynı test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır. 
Örneğin, bir fonksiyonun farklı giriş değerlerini test etmek istiyorsanız, @pytest.mark.parametrize kullanarak bu değerleri belirleyebilirsiniz.

@pytest.mark.skip: Bu dekoratör, belirli bir testin çalıştırılmasını atlamak için kullanılır. 
Örneğin, bir test henüz tamamlanmadıysa veya hatalar içeriyorsa, bu testi atlamak için @pytest.mark.skip kullanabilirsiniz.

@pytest.mark.xfail: Bu dekoratör, bir testin başarısız olması beklenen durumlarda kullanılır. 
Örneğin, bir testin bir hata döndürmesi bekleniyorsa, bu testi @pytest.mark.xfail ile işaretleyebilirsiniz.

@pytest.mark.timeout: Bu dekoratör, bir testin belirli bir zaman sınırı içinde tamamlanmasını sağlar. 
Örneğin, bir testin 5 saniye içinde tamamlanması gerekiyorsa, @pytest.mark.timeout(5) kullanarak bu sınırı belirleyebilirsiniz.

Bu dekoratörlerin yanı sıra, Pytest'te daha birçok dekoratör mevcuttur. Bu dekoratörlerin kullanımı, 
testlerinizi özelleştirmenize ve daha okunaklı ve anlaşılır hale getirmenize yardımcı olabilir.
