import os
import numpy as np
import cv2 as cv
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from skimage.color import rgb2lab, lab2rgb


def getSelftrainedModel(model_path):
    # Mudeli laadimine
    model = os.path.join(os.path.abspath(''), model_path)
    net = load_model(model)

    return net


def getSelftrainedModelFaces(model_path):
    # Mudeli laadimine
    model = os.path.join(os.path.abspath(''), model_path)
    net = load_model(model)

    return net


def getPretrainedModel(prototxt_path, model_path, points_path):
    prototxt = os.path.join(os.path.abspath(''), prototxt_path)
    model = os.path.join(os.path.abspath(''), model_path)
    points = os.path.join(os.path.abspath(''), points_path)

    # Loeme sisse eeltreenitud mudeli
    net = cv.dnn.readNetFromCaffe(prototxt, model)
    # Loeme sisse klastri keskpunktid
    pts = np.load(points)

    # Lisame klastri keskpunktid mudelisse
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(net.getLayerId('class8_ab')).blobs = [pts.astype(np.float32)]
    net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]

    return net


def readImageFromFile(image_path):
    # Loeme sisse pildi (BGR formaadis)
    image_path = os.path.abspath(image_path)
    image = cv.imread(image_path)
    return cv.cvtColor(image, cv.COLOR_BGR2RGB)


def colorizeImage(model, image, modelName):
    if modelName == 'pretrained':
        return colorizeImagePretrained(model, image)
    elif modelName == 'selftrained':
        return colorizeImageSelftrained(model, image)


# Algoritm: http://richzhang.github.io/colorization/
def colorizeImagePretrained(model, image):
    # Võtame pildi kõrguse ja laiuse
    (img_h, img_w) = image.shape[:2]

    # Normaliseerime pildi
    scaled = image.astype(np.float32) / 255.0
    # Teisendame pildi Lab värviformaati
    lab = cv.cvtColor(scaled, cv.COLOR_RGB2LAB)

    # Teisendame pildi 224x224 mõõtmeteks (eeltreenitud mudeli nõue)
    resized = cv.resize(lab, (224, 224))
    # Võtame suurendatud või vähendatult pildilt välja 'L' kanali
    L = resized[:, :, 0]
    # Mean centering
    L -= 50

    # Edastame pildi 'L' kanali mudelile
    model.setInput(cv.dnn.blobFromImage(L))
    # Ennustab 'ab' kanalid
    ab = model.forward()[0, :, :, :].transpose((1, 2, 0))
    # Teisendame pildi tagasi algsuuruseks
    ab = cv.resize(ab, (img_w, img_h))

    # Võtame algse pildi 'L' kanali ja liidame ennustatud 'ab' kanalitega
    L = lab[:, :, 0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    # Tagasi BGR formaati
    colorized = cv.cvtColor(colorized, cv.COLOR_LAB2BGR)
    # Eemaldama väärtused, mis pole [0, 1] vahemikus
    colorized = np.clip(colorized, 0, 1)
    # Pikslid tagasi [0, 255] vahemikku
    colorized = (255 * colorized).astype(np.uint8)

    return colorized


def colorizeImageSelftrained(model, image):
    # Pildi mõõtmed
    (img_h, img_w) = image.shape[:2]
    # Pildi normaliseerimine
    image = image / 255
    # Teisendatakse 256x256 mõõtmeteks
    image = cv.resize(image, (256, 256), interpolation=cv.INTER_AREA)
    # Pilt numpy massiiviks
    image = img_to_array(image)
    # Pilt Lab värviformaati
    lab = rgb2lab(image)
    # Võtame välja 'L' kanali
    bnw = lab[:, :, 0]
    bnw = [bnw]
    bnw = np.array(bnw)
    bnw = bnw.reshape(bnw.shape + (1,))

    # Ennustame 'ab' kanalid
    output = model.predict(bnw)
    output = output * 128

    # Võtame algse pildi 'L' kanali ja liidame ennustatud 'ab' kanalitega
    colorized = np.zeros((256, 256, 3))
    colorized[:, :, 0] = bnw[0][:, :, 0]
    colorized[:, :, 1] = output[0][:, :, 0]
    colorized[:, :, 2] = output[0][:, :, 1]
    # Pilt tagasi RGB formaati
    colorized = lab2rgb(colorized) * 255
    colorized = cv.resize(colorized, (img_w, img_h), interpolation=cv.INTER_AREA)

    return colorized
