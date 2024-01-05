import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hat=cv2.imread('E:/personal files/senscript/AI projects/Insta_flters_with_python/Filters/hat.png')
glass=cv2.imread('E:/personal files/senscript/AI projects/Insta_flters_with_python/Filters/glasses.png')
dog=cv2.imread('E:/personal files/senscript/AI projects/Insta_flters_with_python/Filters/dog.png')
spiderman= cv2.imread('E:/personal files/senscript/AI projects/Insta_flters_with_python/Filters/kk.png')
# christmas_hat= cv2.imread('E:/personal files/senscript/AI projects/Insta_flters_with_python/Filters/images 1.png')

def put_spiderman_filter(spiderman, fc, x, y, w, h):
    face_width = w
    face_height = h

    spiderman = cv2.resize(spiderman, (int(face_width * 1.75), int(face_height * 2.2)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if spiderman[i][j][k] < 235:
                    try:
                        fc[y + i - int(.3 * h) - 1][x + j - int(0.45 * w)][k] = spiderman[i][j][k]
                    except:
                        continue
    return fc


def put_dog_filter(dog, fc, x, y, w, h):
    face_width = w
    face_height = h

    dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if dog[i][j][k] < 235:
                    try:
                        fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
                    except:
                        continue
    return fc


def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    hat = cv2.resize(hat, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
    return fc

def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    glass = cv2.resize(glass, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
    return fc


webcam = cv2.VideoCapture(0)
k=0

while True:
    size=4
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray,1.19,7)

    cv2.putText(im, 'Press ENTER Key for Hat & Glass Filter', (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(im, 'Press ESC key to Quit', (3, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('original image', im)

    key = cv2.waitKey(10)

    if key == 27:  # The Esc key
        webcam.release()
        cv2.destroyAllWindows()
        quit()

    if key == 13:
        k = 1
        # print("gggggggggggg")

    if k==1:
        while True:
            size = 4
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fl = face.detectMultiScale(gray, 1.19, 7)

            key = cv2.waitKey(10)

            for (x, y, w, h) in fl:
                im = put_hat(hat, im, x, y, w, h)
                im = put_glass(glass, im, x, y, w, h)

            cv2.putText(im, 'Press ENTER Key for Dog Filter', (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(im, 'Press ESC key to Quit', (3, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2, cv2.LINE_AA)

            cv2.imshow('Hat & glasses', im)

            if key == 13:
                k=2
                # print("cccccccccccc")
                break

            if key==27:
                webcam.release()
                cv2.destroyAllWindows()
                quit()

        if k==2:
            while True:
                size = 4
                (rval, im) = webcam.read()
                im = cv2.flip(im, 1, 0)
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                fl = face.detectMultiScale(gray, 1.19, 7)

                key = cv2.waitKey(10)

                for (x, y, w, h) in fl:
                    im = put_dog_filter(dog, im, x, y, w, h)
                    # im = put_christmas_hat_filter(christmas_hat, im, x, y, w, h)
                cv2.putText(im, 'Press ENTER Key for SpiderMan Filter', (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(im, 'Press ESC Key to Quit', (3, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2, cv2.LINE_AA)

                cv2.imshow('Dog Filter', im)

                if key == 13:
                    k=3
                    break
                if key == 27:
                    webcam.release()
                    cv2.destroyAllWindows()
                    quit()
        if k==3:
            while True:
                size = 4
                (rval, im) = webcam.read()
                im = cv2.flip(im, 1, 0)
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                fl = face.detectMultiScale(gray, 1.19, 7)

                key = cv2.waitKey(10)

                for (x, y, w, h) in fl:
                    # im = put_dog_filter(dog, im, x, y, w, h)
                    im = put_spiderman_filter(spiderman, im, x, y, w, h)
                cv2.putText(im, 'Press ENTER Key for Original Image', (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(im, 'Press ESC Key to Quit', (3, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2, cv2.LINE_AA)

                cv2.imshow('SpiderMan Filter', im)

                if key == 13:
                    k=0
                    break
                if key == 27:
                    webcam.release()
                    cv2.destroyAllWindows()
                    quit()
