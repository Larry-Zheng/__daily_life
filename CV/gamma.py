import cv2


def make_table(gamma):
    assert gamma>0, 'Invalid gamma!'
    table = dict()
    for i in range(256):
        value = (i+0.5)/256
        value = value**(1/gamma)
        value = int(value*256 - 0.5)
        table[i] = value
    
    return table


def gamma_trans(gamma,img):
    img_copy = img.copy()
    table = make_table(gamma)
    for i in range(256):
        img[img_copy==i] = table[i]
    return img

if __name__ == '__main__':
    img = cv2.imread('./pics/1.jpg')
    img = gamma_trans(10,img)
    cv2.imshow('res',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()