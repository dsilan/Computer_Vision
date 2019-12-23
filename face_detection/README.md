Haar cascade bir resim veya videodaki objeleri tanýmlamak için kullanýlan metottur. Bu metot görüntüdeki pixelleri kareler halinde analiz ederek tanýmlamayý gerçekleþtirir. Görsel inputun farklý lokasyonlarýna Haar özellikleri uygulanarak algoritma ilerler ve böylece tanýmlanacak objeye adým adým yaklaþýlmýþ olunur.

Source: https://www.youtube.com/watch?v=PmZ29Vta7Vc http://www.willberger.org/cascade-haar-explained/

dnn OpenCV içerisinde yer alan, görüntü datalarý için preprocessing yaparken ve önceden eðitilmiþ deep learning modelleriyle sýnýflandýrma yaparken kullanabildiðimiz bir modüldür.
Caffe, Darknet, Tensorflow gibi modelleri de dnn modülüyle birlikte kullanabiliyoruz.
detect_faces_image.py kodunu çalýþtýrmak için komut:

python detect_faces_image.py --image ./deep-learning-face-detection/deneme.jpg --prototxt ./deep-learning-face-detection/deploy.prototxt.txt  --model ./deep-learning-face-detection/res10_300x300_ssd_iter_140000.caffemodel


Source: https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/
