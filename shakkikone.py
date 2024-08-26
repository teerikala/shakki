"""
Tässä tiedostossa on pohja shakkikoneen kouluttamiselle. Nykyinen
toiminta perustuu alpha-beta-karsittuun minimax-algoritmiin.
"""

from teorialauta import *
import time

# Globaalit vakiot
PELIEN_MAKSIMI = 100
ARVIOINNIN_SYVYYS = 3

AARETON = 9999


def muodosta_pelitilanteen_arvo(pelilauta):
    """
    Tämä funktio muodostaa yksinkertaisen pelitilanteen arvon voittaneen
    puolen tai kokonaismateriaalien avulla.

    :return: int, pelitilanteen arvo lukuna.
    """

    if pelilauta.voittaja() == "valkoinen":
        return AARETON

    if pelilauta.voittaja() == "musta":
        return -AARETON

    valkoisen_materiaali, mustan_materiaali = (
        pelilauta.puolten_kokonaismateriaali())

    return valkoisen_materiaali - mustan_materiaali


def alphabeta(pelilauta, syvyys, alpha, beta, vuorossa):
    """
    Minimax-algoritmi on yleisin vuoropohjaisten pelien siirtojen
    arviointialgoritmi, ja sen yleisin optimointimenetelmä on ns.
    alpha-beta-karsiminen (alpha-beta pruning). Vuorossa oleva pelaaja
    arvioi parhaan siirron tulevien parhaiden siirtojen perusteella.
    Implementaatio perustuu verkossa saatavilla olevaan pseudokoodiin
    https://en.wikipedia.org/wiki/Minimax#Pseudocode.

    :param pelilauta: Teorialauta, pelitilanne, jossa parasta siirtoa etsitään.
    :param syvyys: int, kuinka monta siirtoa eteenpäin peliä luetaan.
    :param alpha: int, paras arvo valkoisen kannalta.
    :param beta: int, paras arvo mustan kannalta.
    :param vuorossa: bool, True=valkoinen vuorossa, False=musta vuorossa.
    :return: int, paras siirto vuorossa olevalle pelaajalle.
    """

    if syvyys == 0 or pelilauta.voittaja():
        return muodosta_pelitilanteen_arvo(pelilauta)

    siirtonumero = pelilauta.siirtonumero()
    asemat = pelilauta.asemat()
    liikkumistiedot = pelilauta.liikkumistiedot()
    shakit = pelilauta.shakit()

    if vuorossa:
        maksimi = -AARETON

        for sijainti, siirrot in pelilauta.puolen_kaikki_siirrot(
                "valkoinen").items():

            for siirto in bittien_bittilaudat(siirrot):

                uusi_lauta = Teorialauta(siirtonumero, *asemat,
                                         *liikkumistiedot, *shakit)
                uusi_lauta.tee_siirto(sijainti, siirto)

                arvo = alphabeta(uusi_lauta, syvyys-1, alpha, beta, False)
                maksimi = max(maksimi, arvo)
                alpha = max(alpha, arvo)

                if arvo >= beta:
                    break

        return maksimi

    else:
        minimi = AARETON
        for sijainti, siirrot in pelilauta.puolen_kaikki_siirrot(
                "musta").items():

            for siirto in bittien_bittilaudat(siirrot):

                uusi_lauta = Teorialauta(siirtonumero, *asemat,
                                         *liikkumistiedot, *shakit)
                uusi_lauta.tee_siirto(sijainti, siirto)

                arvo = alphabeta(uusi_lauta, syvyys-1, alpha, beta, True)
                minimi = min(minimi, arvo)
                beta = min(beta, arvo)

                if arvo <= alpha:
                    break

        return minimi


def arvioi_paras_siirto(pelilauta, syvyys):
    """
    Funktio parhaan siirron löytämiseen.

    :param pelilauta: Teorialauta, pelitilanne, josta parasta siirtoa etsitään.
    :param syvyys: int, kuinka monta siirtoa eteenpäin peliä luetaan.
    :return: int, int / None, None; ruudut, josta lähdetään ja johon
                                    siirrytään.
    """

    paras_siirto = None, None

    if pelilauta.siirtonumero() % 2 == 1:
        puoli = "valkoinen"
        paras_arvo = -AARETON
        vuorossa = True
    else:
        puoli = "musta"
        paras_arvo = AARETON
        vuorossa = False

    siirtonumero = pelilauta.siirtonumero()
    asemat = pelilauta.asemat()
    liikkumistiedot = pelilauta.liikkumistiedot()
    shakit = pelilauta.shakit()

    for sijainti, siirrot in pelilauta.puolen_kaikki_siirrot(puoli).items():
        for siirto in bittien_bittilaudat(siirrot):

            uusi_lauta = Teorialauta(siirtonumero, *asemat, *liikkumistiedot,
                                     *shakit)
            uusi_lauta.tee_siirto(sijainti, siirto)

            arvo = alphabeta(uusi_lauta, syvyys-1, -AARETON, AARETON, vuorossa)

            if (vuorossa and arvo > paras_arvo) or (not vuorossa and arvo <
                                                    paras_arvo):
                paras_arvo = arvo
                paras_siirto = sijainti, siirto

    return paras_siirto


def testaa():
    """
    Tällä funktiolla voi testata shakkikoneen nopeutta.
    """

    pelinumero = 1

    while True:

        if pelinumero == PELIEN_MAKSIMI:
            print("Testipelit päättyivät.")
            break

        print(pelinumero, ". peli", sep="")

        pelilauta = Teorialauta()
        aloitusaika = time.time()

        # Tehdään siirtoja niin kauan, kuin peli on käynnissä
        while True:
            siirtonumero = pelilauta.siirtonumero()
            print(siirtonumero, ". siirto", sep="")

            # Rajoitetaan pelin pituus sataan siirtoon per puoli
            if siirtonumero == 200:
                print("Tasapeli.")
                break

            # Arvioidaan vuorossa olevalle puolelle paras siirto
            sijainti, siirto = arvioi_paras_siirto(pelilauta,
                                                   ARVIOINNIN_SYVYYS)

            if siirto:
                pelilauta.tee_siirto(sijainti, siirto)
                voittaja = pelilauta.voittaja()

            else:
                if siirtonumero % 2 == 1:
                    voittaja = "musta"
                else:
                    voittaja = "valkoinen"

            # Suoritetaan pelin päätöstoimenpiteet, jos voittaja löytyi.
            if voittaja:
                suoritusaika = time.time() - aloitusaika

                # Tulostetaan ottelun tietoja
                print("Voittaja:", voittaja)
                print("Siirtoja:", siirtonumero)
                print("Suoritusaika:", suoritusaika, "s")
                print("Suoritusaika per siirto:", suoritusaika/siirtonumero,
                      "s/siirto")

                break

        pelinumero += 1


def main():
    testaa()


if __name__ == "__main__":
    main()
