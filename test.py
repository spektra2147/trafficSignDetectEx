import cv2
import numpy as np

# Tipi Bulunacak Resim
img = cv2.imread('3.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Nesneler
hiz_siniri = cv2.imread('1.jpg', 0)
tasit_giremez = cv2.imread('4.jpg', 0)
saga_don = cv2.imread('2.jpg', 0)
duz_git = cv2.imread('3.jpg', 0)


def hesapla(nesne):
    res = cv2.matchTemplate(grey_img, nesne, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9;
    return np.where(res >= threshold)


def cerceve(nesne):
    w, h = nesne.shape[::-1]
    for pt in zip(*hesapla(nesne)[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

if len(hesapla(hiz_siniri)[0]) != 0:
    print("Hız Sınırı")
    cerceve(hiz_siniri)
elif len(hesapla(tasit_giremez)[0]) != 0:
    print("Taşıt Giremez")
    cerceve(tasit_giremez)
elif len(hesapla(saga_don)[0]) != 0:
    print("Sağa Dön")
    cerceve(saga_don)
elif len(hesapla(duz_git)[0]) != 0:
    print("Düz Git")
    cerceve(duz_git)
else:
    print("Bulunamadı!")

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
