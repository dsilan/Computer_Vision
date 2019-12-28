opencv_tutorial_1.py dosyasında bir resim üzerinde bazı temel opencv kütüphanesi alıştırmaları üzerinde çalıştım. Kullandığım bazı özellik ve metotlar:
image.shape, (h, w, d) formatında resim boyutunu öğrenmemize yarar. Yüksekliğin genişlikten önce gelmesinin sebebi resmi bir matrix (row x column) gibi düşünürsek row/satır sayısı height’a, column/sütun sayısının width’e karşılık gelmesindendir.

image[h, w], BGR düzeninde pixelin renk bilgisini döndürür. RGB veya başka bir standart yerine BGR standardının kullanılmasının sebebi OpenCV’inin eskiden beri BGR’ı kullanması ve bunun değiştirilmemesidir.

Resim olarak çok sevdiğim filmlerden biri olan A.I. Artificial Intelligence’dan bir kareyi kullandım. 

        image = cv2.imread("../../images/ai_movie.jpg")
        cv2.imshow("Image",image)
        
Bildiğiniz üzere satırlar ile resmi görüntüleyebiliyoruz.

  <img src="/opencv_tutorial/output/image.png" width="400px" >
Resim bir matrix ise doğru koordinatları verdiğimiz zaman o matrixin sadece bir bölümünü ayırabiliriz. Resimde Jude Law’ın yüzünü görüntülemek istediğimizde yapmamız gereken ROI array slicing işlemidir. ROI resim üzerinde belli bir alanı elde etmek için kullanılır. Bu durumda image[startY:endY, startX:endX] formatında noktaları girmemiz gerekir.
  <img src="/opencv_tutorial/output/jude_face.png" width="200px">
Opencv’nin resize fonksiyonuna resmi ve istediğimiz en boyu vererek çok kolay bir şekilde resmi yeniden boyutlandırabiliriz. Ama eğer en boy oranını kullanarak kolayca boyutlandırmak istersek imutils paketinin resize fonksiyonunu kullanabiliriz.

        i_resized = imutils.resize(image, width=300)

Aynı şekilde döndürmek istersek imutils.rotate metotunu çağırabiliriz.

        rotated = imutils.rotate(image, -45)
        
Bu satır saat yönünde 45 derece resmi döndürür. (negatif açı, saat yönünde döndürür; pozitif açı ise saat yönünün tersinde)
Bulanıklaştırmak istersek basit bir yol olarak opencv’nin meşhur efekterinden olan GaussianBlur’u kullanabiliriz.

        blurred = cv2.GaussianBlur(image, (15, 15), 0)
        
ortadaki ksize ne kadar büyütülürse resim de o kadar bulanıklaşır.

<img src="/opencv_tutorial/output/blurred.png" width="400px">
Eğer resimde bir dikdörtgen çizmek istersek -örneğin yüzü dikdörtgen içerisine alalım- rectangle fonksiyonuna çizeceğimiz dikdörtgenin köşegen koordinatlarını vermeliyiz. (sol üst, sağ alt)

<img src="/opencv_tutorial/output/rec.jpeg" width="400px">

        output = image.copy()
        cv2.rectangle(output, (620,0), (800,190), (255,0,0), 2) 
        cv2.imshow("2px thick blue rectangle surrounding the face",output)
        
çıktı:

<img src="/opencv_tutorial/output/rectangle.png" width="400px">

Source: https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
