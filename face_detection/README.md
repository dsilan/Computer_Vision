Haar cascade bir resim veya videodaki objeleri tan�mlamak i�in kullan�lan metottur. Bu metot g�r�nt�deki pixelleri kareler halinde analiz ederek tan�mlamay� ger�ekle�tirir. G�rsel inputun farkl� lokasyonlar�na Haar �zellikleri uygulanarak algoritma ilerler ve b�ylece tan�mlanacak objeye ad�m ad�m yakla��lm�� olunur.

Source: https://www.youtube.com/watch?v=PmZ29Vta7Vc http://www.willberger.org/cascade-haar-explained/

dnn OpenCV i�erisinde yer alan, g�r�nt� datalar� i�in preprocessing yaparken ve �nceden e�itilmi� deep learning modelleriyle s�n�fland�rma yaparken kullanabildi�imiz bir mod�ld�r.
Caffe, Darknet, Tensorflow gibi modelleri de dnn mod�l�yle birlikte kullanabiliyoruz.
detect_faces_image.py kodunu �al��t�rmak i�in komut:

python detect_faces_image.py --image ./deep-learning-face-detection/deneme.jpg --prototxt ./deep-learning-face-detection/deploy.prototxt.txt  --model ./deep-learning-face-detection/res10_300x300_ssd_iter_140000.caffemodel


Source: https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/
