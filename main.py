import cv2 as cv
import numpy as np


def kmeans(slika, k=3, iteracije=10):
    '''Izvede segmentacijo slike z uporabo metode k-means.'''
    pass


def meanshift(slika, velikost_okna, dimenzija):
    '''Izvede segmentacijo slike z uporabo metode mean-shift.'''
    pass


def izracunaj_centre(slika, izbira, dimenzija_centra, T):
    '''Izračuna centre za metodo kmeans.'''

    h, w, _ = slika.shape

    options = []
    for y in range(h):
        for x in range(w):
            color = slika[y, x]
            if dimenzija_centra == 3:
                options.append(color)
            elif dimenzija_centra == 5:
                options.append(np.concatenate((color, [x, y])))

    options = np.array(options)

    if izbira == 'ročna':
        print("Izberite centre:")
        tocke = []

        def on_mouse(event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                barva = slika[y, x].astype(np.float32)
                if dimenzija_centra == 3:
                    tocke.append(barva)
                else:
                    tocke.append(np.concatenate([barva, [x, y]]))

        cv.namedWindow("Klikni centre")
        cv.setMouseCallback("Klikni centre", on_mouse)

        while True:
            cv.imshow("Klikni centre", slika)
            if cv.waitKey(20) & 0xFF == 27:  # Esc za konec
                break

        cv.destroyAllWindows()
        centri = tocke

    elif izbira == "naključna":
        np.random.shuffle(options)
        centri = [options[0]]

        for kandidat in options[1:]:
            razlike = [np.linalg.norm(kandidat - c) for c in centri]
            if all(razlika >= T for razlika in razlike):
                centri.append(kandidat)
            if len(centri) >= 10:  # ali neka želena količina centrov
                break
    else:
        raise ValueError("Neveljavna izbira: izberi 'ročna' ali 'naključna'")

    return np.array(centri)


if __name__ == "__main__":
    pass