"""
Tämä tiedosto esittelee luokan Teorialauta, joka vastaa shakkipelin
teoreettisesta pyörittämisestä. Tätä tiedostoa on kehitetty vastaamaan niin
graafisen käyttöliittymän kuin shakkikoneen tarpeisiin.
"""

import numpy as np


class Teorialauta:
    # Vakiobittilautoja
    RUUTU_A1 = np.uint64(0x0000000000000001)
    RUUTU_B1 = np.uint64(0x0000000000000002)
    RUUTU_C1 = np.uint64(0x0000000000000004)
    RUUTU_D1 = np.uint64(0x0000000000000008)
    RUUTU_E1 = np.uint64(0x0000000000000010)
    RUUTU_F1 = np.uint64(0x0000000000000020)
    RUUTU_G1 = np.uint64(0x0000000000000040)
    RUUTU_H1 = np.uint64(0x0000000000000080)
    RUUTU_A8 = np.uint64(0x0100000000000000)
    RUUTU_B8 = np.uint64(0x0200000000000000)
    RUUTU_C8 = np.uint64(0x0400000000000000)
    RUUTU_D8 = np.uint64(0x0800000000000000)
    RUUTU_E8 = np.uint64(0x1000000000000000)
    RUUTU_F8 = np.uint64(0x2000000000000000)
    RUUTU_G8 = np.uint64(0x4000000000000000)
    RUUTU_H8 = np.uint64(0x8000000000000000)

    SARAKE_A = np.uint64(0x0101010101010101)
    SARAKE_B = np.uint64(0x202020202020202)
    SARAKE_G = np.uint64(0x4040404040404040)
    SARAKE_H = np.uint64(0x8080808080808080)

    RIVI_1 = np.uint64(0x00000000000000FF)
    RIVI_8 = np.uint64(0xFF00000000000000)

    # Aloitusasemat
    V_SOTILAAT = np.uint64(0x000000000000FF00)
    V_TORNIT = np.uint64(0x0000000000000081)
    V_RATSUT = np.uint64(0x0000000000000042)
    V_LAHETIT = np.uint64(0x0000000000000024)
    V_KUNINGATAR = RUUTU_D1
    V_KUNINGAS = RUUTU_E1

    M_SOTILAAT = np.uint64(0x00FF000000000000)
    M_TORNIT = np.uint64(0x8100000000000000)
    M_RATSUT = np.uint64(0x4200000000000000)
    M_LAHETIT = np.uint64(0x2400000000000000)
    M_KUNINGATAR = RUUTU_D8
    M_KUNINGAS = RUUTU_E8

    def __init__(self, siirtonumero=None, v_sotilaat=None, v_tornit=None,
                 v_ratsut=None, v_lahetit=None, v_kuningatar=None,
                 v_kuningas=None, m_sotilaat=None, m_tornit=None,
                 m_ratsut=None, m_lahetit=None, m_kuningatar=None,
                 m_kuningas=None, vv_torni_lahtoasemassa=None,
                 vv_reitti_uhattuna=None, vo_torni_lahtoasemassa=None,
                 vo_reitti_uhattuna=None, v_kuningas_lahtoasemassa=None,
                 mv_torni_lahtoasemassa=None, mv_reitti_uhattuna=None,
                 mo_torni_lahtoasemassa=None, mo_reitti_uhattuna=None,
                 m_kuningas_lahtoasemassa=None, v_shakissa=None,
                 m_shakissa=None):
        """
        Rakentaa teorialaudan eli aloittaa uuden teoreettisen shakkipelin
        lähtöasemasta.
        """

        # Tästä voidaan päätellä, että peli ei ole alkanut
        if not siirtonumero:
            self.__siirtonumero = 1

            self.__v_sotilaat = self.V_SOTILAAT
            self.__v_tornit = self.V_TORNIT
            self.__v_ratsut = self.V_RATSUT
            self.__v_lahetit = self.V_LAHETIT
            self.__v_kuningatar = self.V_KUNINGATAR
            self.__v_kuningas = self.V_KUNINGAS

            self.__m_sotilaat = self.M_SOTILAAT
            self.__m_tornit = self.M_TORNIT
            self.__m_ratsut = self.M_RATSUT
            self.__m_lahetit = self.M_LAHETIT
            self.__m_kuningatar = self.M_KUNINGATAR
            self.__m_kuningas = self.M_KUNINGAS

            self.__vv_torni_lahtoasemassa = True  # valkoisen vasen
            self.__vv_reitti_uhattuna = False
            self.__vo_torni_lahtoasemassa = True
            self.__vo_reitti_uhattuna = False
            self.__v_kuningas_lahtoasemassa = True
            self.__mv_torni_lahtoasemassa = True
            self.__mv_reitti_uhattuna = False
            self.__mo_torni_lahtoasemassa = True  # mustan oikea
            self.__mo_reitti_uhattuna = False
            self.__m_kuningas_lahtoasemassa = True

            self.__v_shakissa = False
            self.__m_shakissa = False

        else:
            self.__siirtonumero = siirtonumero

            self.__v_sotilaat = v_sotilaat
            self.__v_tornit = v_tornit
            self.__v_ratsut = v_ratsut
            self.__v_lahetit = v_lahetit
            self.__v_kuningatar = v_kuningatar
            self.__v_kuningas = v_kuningas

            self.__m_sotilaat = m_sotilaat
            self.__m_tornit = m_tornit
            self.__m_ratsut = m_ratsut
            self.__m_lahetit = m_lahetit
            self.__m_kuningatar = m_kuningatar
            self.__m_kuningas = m_kuningas

            self.__vv_torni_lahtoasemassa = vv_torni_lahtoasemassa
            self.__vv_reitti_uhattuna = vv_reitti_uhattuna
            self.__vo_torni_lahtoasemassa = vo_torni_lahtoasemassa
            self.__vo_reitti_uhattuna = vo_reitti_uhattuna
            self.__v_kuningas_lahtoasemassa = v_kuningas_lahtoasemassa
            self.__mv_torni_lahtoasemassa = mv_torni_lahtoasemassa
            self.__mv_reitti_uhattuna = mv_reitti_uhattuna
            self.__mo_torni_lahtoasemassa = mo_torni_lahtoasemassa
            self.__mo_reitti_uhattuna = mo_reitti_uhattuna
            self.__m_kuningas_lahtoasemassa = m_kuningas_lahtoasemassa

            self.__v_shakissa = v_shakissa
            self.__m_shakissa = m_shakissa

        self.__linnoittaminen = False
        self.__voittaja = None

    def siirtonumero(self):
        """
        Apufunktio, joka palauttaa senhetkisen siirtonumeron.

        :return: int, siirtonumero.
        """

        return self.__siirtonumero

    def asemat(self):
        """
        Apufunktio, joka palauttaa listat molempien puolien varaamista
        ruuduista.

        :return: [int, ...], listat jokaisen nappulatyypin bittilaudoista.
        """

        return [self.__v_sotilaat, self.__v_tornit, self.__v_ratsut,
                self.__v_lahetit, self.__v_kuningatar, self.__v_kuningas,
                self.__m_sotilaat, self.__m_tornit, self.__m_ratsut,
                self.__m_lahetit, self.__m_kuningatar, self.__m_kuningas]

    def liikkumistiedot(self):
        """
        Apufunktio, joka palauttaa liikkumistiedot, joita seurataan
        linnoittamisen varalta.

        :return: [bool, ...]; onko jokin nappuloista liikkunut.
        """

        return [self.__vv_torni_lahtoasemassa, self.__vv_reitti_uhattuna,
                self.__vo_torni_lahtoasemassa, self.__vo_reitti_uhattuna,
                self.__v_kuningas_lahtoasemassa, self.__mv_torni_lahtoasemassa,
                self.__mv_reitti_uhattuna, self.__mo_torni_lahtoasemassa,
                self.__mo_reitti_uhattuna, self.__m_kuningas_lahtoasemassa]

    def shakit(self):
        """
        Apufunktio, joka palauttaa tiedon shakkitilanteesta.

        return: bool, bool, onko kuninkaat shakissa.
        """

        return [self.__v_shakissa, self.__m_shakissa]

    def voittaja(self):
        """
        Apufunktio, joka palauttaa tiedon voittajasta.

        return: str/None, voittanut puoli.
        """

        return self.__voittaja

    def puolten_kokonaismateriaali(self):
        """
        Apufunktio, joka määrittää puolten materiaalin arvon yleisesti
        käytetyllä taulukolla:
        Sotilas = 1 piste
        Ratsu = 3 pistettä
        Lähetti = 3 pistettä
        Torni = 5 pistettä
        Kuningatar = 9 pistettä

        :return: int, int; materiaalin arvo kokonaislukuna.
        """

        valkoisen_materiaali = bin(self.__v_sotilaat).count('1') \
            + bin(self.__v_tornit).count('1')*5 \
            + bin(self.__v_ratsut).count('1')*3 \
            + bin(self.__v_lahetit).count('1')*3 \
            + bin(self.__v_kuningatar).count('1')*9

        mustan_materiaali = bin(self.__m_sotilaat).count('1') \
            + bin(self.__m_tornit).count('1')*5 \
            + bin(self.__m_ratsut).count('1')*3 \
            + bin(self.__m_lahetit).count('1')*3 \
            + bin(self.__m_kuningatar).count('1')*9

        return valkoisen_materiaali, mustan_materiaali

    def ruudun_nappulan_tiedot(self, asema):
        """
        Apufunktio, joka palauttaa tietoa annetusta ruudussa olevasta
        nappulasta.

        :param asema: int, bittilauta, jossa vain etsittävä nappula on.
        :return: str, str, int; nappulan väri, tyyppi sekä bittilauta sen
                 mahdollisista siirroista.
        """

        vari = "White"
        tyyppi = ""
        siirrot = 0

        asemat = self.asemat()

        for i in range(0, 12):
            if i == 6:
                vari = "Black"

            if asemat[i] & asema:
                if i == 0 or i == 6:
                    tyyppi = "Sotilas"
                    siirrot = self.sotilaan_liike(asema)
                elif i == 1 or i == 7:
                    tyyppi = "Torni"
                    siirrot = self.tornin_liike(asema)
                elif i == 2 or i == 8:
                    tyyppi = "Ratsu"
                    siirrot = self.ratsun_liike(asema)
                elif i == 3 or i == 9:
                    tyyppi = "Lähetti"
                    siirrot = self.lahetin_liike(asema)
                elif i == 4 or i == 10:
                    tyyppi = "Kuningatar"
                    siirrot = self.kuningattaren_liike(asema)
                elif i == 5 or i == 11:
                    tyyppi = "Kuningas"
                    siirrot = self.kuninkaan_liike(asema)

                return vari, tyyppi, siirrot

    def puolen_kaikki_siirrot(self, puoli, esta_shakki=False):
        """
        Apufunktio, joka palauttaa puolen kaikki mahdolliset siirrot.

        :param puoli: str, valittu puoli, musta tai valkoinen.
        :param esta_shakki: poistetaanko siirtojen joukosta häviävät siirrot.
        :return: {int: int}, sanakirja nappulan sijainnin bittilaudasta
                 linkitettyinä sen mahdollisten siirtymäruutujen bittilautaan.
        """

        kaikki_siirrot = {}
        asemat = self.asemat()

        if puoli == "valkoinen":
            alku = 0
            loppu = 6
        else:
            alku = 6
            loppu = 12

        for i in range(alku, loppu):
            for asema in bittien_bittilaudat(asemat[i]):
                siirrot = np.uint64(0)

                if i == 0 or i == 6:
                    siirrot |= self.sotilaan_liike(asema, esta_shakki)
                elif i == 1 or i == 7:
                    siirrot |= self.tornin_liike(asema, esta_shakki)
                elif i == 2 or i == 8:
                    siirrot |= self.ratsun_liike(asema, esta_shakki)
                elif i == 3 or i == 9:
                    siirrot |= self.lahetin_liike(asema, esta_shakki)
                elif i == 4 or i == 10:
                    siirrot |= self.kuningattaren_liike(asema, esta_shakki)
                elif i == 5 or i == 11:
                    siirrot |= self.kuninkaan_liike(asema, esta_shakki)

                if siirrot:
                    kaikki_siirrot.update({asema: siirrot})

        return kaikki_siirrot

    def sotilaan_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii valkoisen sotilaan liikkumismahdollisuuksia
        annetusta <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Sotilaat voivat liikkua
        kaksi askelta eteen ensimmäisellä siirrollaan, sen jälkeen vain
        yhden. Sotilas voi myös syödä vastustajan pelinappulan yhden
        askeleen päästä viistottain.

        :param asema: int, bittilauta ruudulle, josta sotilas lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        asemat = self.asemat()
        siirrot = np.uint64(0)

        valkoiset = np.uint64(0)
        for i in range(0, 6):
            valkoiset |= asemat[i]

        mustat = np.uint64(0)
        for i in range(6, 12):
            mustat |= asemat[i]

        if valkoiset & asema:
            omat = valkoiset
            vastustajat = mustat

        else:
            omat = mustat
            vastustajat = valkoiset

        varatut = omat | vastustajat

        if omat == valkoiset:
            # Suoraan eteenpäin siirtäminen
            siirto = asema << 8

            if not varatut & siirto:
                siirrot |= siirto

                # Kaksi askelta eteenpäin siirtäminen
                siirto = asema << 16
                if (not varatut & siirto) and (asema & self.RIVI_1 << 8):
                    siirrot |= siirto

            # Syöminen
            if not asema & self.SARAKE_A:
                siirto = asema << 7
                if siirto & vastustajat:
                    siirrot |= siirto

            if not asema & self.SARAKE_H:
                siirto = asema << 9
                if siirto & vastustajat:
                    siirrot |= siirto

        # Sama mustalle
        if omat == mustat:
            siirto = asema >> 8

            if not varatut & siirto:
                siirrot |= siirto

                siirto = asema >> 16
                if (not varatut & siirto) and (asema & self.RIVI_8 >> 8):
                    siirrot |= siirto

            # Syöminen
            if not asema & self.SARAKE_A:
                siirto = asema >> 9
                if siirto & vastustajat:
                    siirrot |= siirto

            if not asema & self.SARAKE_H:
                siirto = asema >> 7
                if siirto & vastustajat:
                    siirrot |= siirto

        # Estetään shakkiin siirtäminen, jos vaadittu
        if esta_shakki:
            return self.esta_siirtaminen_shakkiin(asema, siirrot)

        return siirrot

    def tornin_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii tornin liikkumismahdollisuuksia annetusta
        <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Torni voi liikkua
        suorasti niin pitkälle, kunnes kohtaa seinän tai nappulan.

        :param asema: int, bittilauta ruudulle, josta torni lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        asemat = self.asemat()
        siirrot = np.uint64(0)

        valkoiset = np.uint64(0)
        for i in range(0, 6):
            valkoiset |= asemat[i]

        mustat = np.uint64(0)
        for i in range(6, 12):
            mustat |= asemat[i]

        if valkoiset & asema:
            omat = valkoiset
            vastustajat = mustat

        else:
            omat = mustat
            vastustajat = valkoiset

        for suunta in [8, -8, 1, -1]:
            siirto = asema
            while True:
                # Ylös
                if suunta == 8:
                    siirto = siirto << 8

                # Alas
                if suunta == -8:
                    siirto = siirto >> 8

                # Ylä- tai alareunan ylittäminen
                if not siirto:
                    break

                # Oikealle
                if suunta == 1:
                    # Sivureunan saavuttaminen
                    if siirto & self.SARAKE_H:
                        break

                    siirto = siirto << 1

                # Vasemmalle
                if suunta == -1:
                    if siirto & self.SARAKE_A:
                        break

                    siirto = siirto >> 1

                # Tutkitaan jokaiselle suunnalle, onko oma nappula tiellä
                if siirto & omat:
                    break

                # Nyt tiedetään, että siirto on mahdollinen
                siirrot |= siirto
                # Tutkitaan jokaiselle suunnalle, aiheuttaako syöminen
                # pysähtymisen
                if siirto & vastustajat:
                    break

        # Estetään shakkiin siirtäminen, jos vaadittu
        if esta_shakki:
            return self.esta_siirtaminen_shakkiin(asema, siirrot)

        return siirrot

    def ratsun_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii ratsun liikkumismahdollisuuksia annetusta
        <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Ratsu voi liikkua
        L-kirjaimen mukaisesti eli kaksi eteen, yhden sivulle.

        :param asema: int, bittilauta ruudulle, josta ratsu lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        # Viitataan ratsun mahdollisiin siirtoihin näin:
        # * y1 * y2 *
        # v1 * * * o1
        # *  * R *  *
        # v2 * * * o2
        # * a1 * a2 *

        asemat = self.asemat()
        siirrot = np.uint64(0)

        y1 = np.uint64(0)
        y2 = np.uint64(0)
        v1 = np.uint64(0)
        v2 = np.uint64(0)
        o1 = np.uint64(0)
        o2 = np.uint64(0)
        a1 = np.uint64(0)
        a2 = np.uint64(0)

        if not asema & self.SARAKE_A:
            y1 |= asema << 15
            a1 |= asema >> 17

            if not asema & self.SARAKE_B:
                v1 |= asema << 6
                v2 |= asema >> 10

        if not asema & self.SARAKE_H:
            y2 |= asema << 17
            a2 |= asema >> 15

            if not asema & self.SARAKE_G:
                o1 |= asema >> 6
                o2 |= asema << 10

        siirrot |= (y1 | y2 | v1 | v2 | o1 | o2 | a1 | a2)

        # Lopuksi poistetaan siirroista sellaiset ruudut,
        # jotka ovat varattuina omille nappuloille
        if asemat[2] & asema:
            alku = 0
            loppu = 6
        else:
            alku = 6
            loppu = 12

        omat = np.uint64(0)
        for i in range(alku, loppu):
            omat |= asemat[i]

        siirrot &= ~omat

        # Estetään shakkiin siirtäminen, jos vaadittu
        if esta_shakki:
            return self.esta_siirtaminen_shakkiin(asema, siirrot)

        return siirrot

    def lahetin_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii lähetin liikkumismahdollisuuksia annetusta
        <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Lähetti voi liikkua
        viistottain niin pitkälle, kunnes kohtaa seinän tai nappulan.

        :param asema: int, bittilauta ruudulle, josta lähetti lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        asemat = self.asemat()
        siirrot = np.uint64(0)

        valkoiset = np.uint64(0)
        for i in range(0, 6):
            valkoiset |= asemat[i]

        mustat = np.uint64(0)
        for i in range(6, 12):
            mustat |= asemat[i]

        if valkoiset & asema:
            omat = valkoiset
            vastustajat = mustat

        else:
            omat = mustat
            vastustajat = valkoiset

        for suunta in [7, -7, 9, -9]:
            siirto = asema
            while True:
                # Aiheuttaako sivureuna pysähtymisen
                if (suunta == 7 or suunta == -9) and (siirto & self.SARAKE_A):
                    break

                if (suunta == 9 or suunta == -7) and (siirto & self.SARAKE_H):
                    break

                siirto = (siirto << suunta if suunta > 0 else
                          siirto >> -suunta)

                # Ylä- tai alareunan ylittäminen
                if not siirto:
                    break

                # Onko oma nappula tiellä
                if siirto & omat:
                    break

                # Nyt tiedetään, että siirto on mahdollinen
                siirrot |= siirto

                # Aiheuttaako syöminen pysähtymisen
                if siirto & vastustajat:
                    break

        # Estetään shakkiin siirtäminen, jos vaadittu
        if esta_shakki:
            return self.esta_siirtaminen_shakkiin(asema, siirrot)

        return siirrot

    def kuningattaren_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii kuningattaren liikkumismahdollisuuksia
        annetusta <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Kuningattaren liikkeessä
        yhdistyvät tornin sekä lähetin liikkumismahdollisuudet,
        joten funktiokin on myös toteutettu siten.

        :param asema: int, bittilauta ruudulle, josta kuningatar lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        return self.tornin_liike(asema, esta_shakki) | self.lahetin_liike(
            asema, esta_shakki)

    def kuninkaan_liike(self, asema, esta_shakki=True):
        """
        Apufunktio, joka tutkii kuninkaan liikkumismahdollisuuksia annetusta
        <asema>:sta eli pelilaudan ruudusta. Palauttaa kaikki
        siirtomahdollisuudet sisältävän bittilaudan. Kuningas voi liikkua
        yhden askeleen joka suuntaan laudalla.

        :param asema: int, bittilauta ruudulle, josta kuningas lähtee.
        :param esta_shakki: bool, eliminoidaanko pelin häviävät siirrot.
        :return: int, bittilauta siirtomahdollisuuksista.
        """

        asemat = self.asemat()
        siirrot = np.uint64(0)

        valkoiset = np.uint64(0)
        for i in range(0, 6):
            valkoiset |= asemat[i]

        mustat = np.uint64(0)
        for i in range(6, 12):
            mustat |= asemat[i]

        omat = valkoiset if valkoiset & asema else mustat

        for suunta in [1, -1, 8, -8, 7, -7, 9, -9]:
            siirto = asema
            # Aiheuttaako sivureuna pysähtymisen
            if ((suunta == -1 or suunta == 7 or suunta == -9) and
                    (siirto & self.SARAKE_A)):
                continue

            if ((suunta == 1 or suunta == -7 or suunta == 9) and
                    (siirto & self.SARAKE_H)):
                continue

            siirto = (siirto << suunta if suunta > 0 else
                      siirto >> -suunta)

            # Ylä- tai alareunan ylittäminen
            if not siirto:
                continue

            # Onko oma nappula tiellä
            if siirto & omat:
                continue

            # Nyt tiedetään, että siirto on mahdollinen
            siirrot |= siirto

        # Tutkitaan vielä linnoittamisen mahdollisuutta
        varatut = valkoiset | mustat

        # Valkoiselle
        if self.__v_kuningas_lahtoasemassa and omat == valkoiset:
            if (self.__vv_torni_lahtoasemassa and
                not self.__vv_reitti_uhattuna and
                    not varatut & (self.RUUTU_B1 | self.RUUTU_C1 |
                                   self.RUUTU_D1)):
                siirrot |= self.RUUTU_C1
                self.__linnoittaminen = True

            if (self.__vo_torni_lahtoasemassa and
                not self.__vo_reitti_uhattuna and
                    not varatut & (self.RUUTU_F1 | self.RUUTU_G1)):
                siirrot |= self.RUUTU_G1
                self.__linnoittaminen = True

        # Mustalle
        if self.__m_kuningas_lahtoasemassa and omat == mustat:
            if (self.__mv_torni_lahtoasemassa and
                not self.__mv_reitti_uhattuna and
                    not varatut & (self.RUUTU_B8 | self.RUUTU_C8 |
                                   self.RUUTU_D8)):
                siirrot |= self.RUUTU_C8
                self.__linnoittaminen = True

            if self.__mo_torni_lahtoasemassa and \
                not self.__mo_reitti_uhattuna and \
                    not varatut & (self.RUUTU_F8 | self.RUUTU_G8):
                siirrot |= self.RUUTU_G8
                self.__linnoittaminen = True

        # Estetään shakkiin siirtäminen, jos vaadittu
        if esta_shakki:
            return self.esta_siirtaminen_shakkiin(asema, siirrot)

        return siirrot

    def esta_siirtaminen_shakkiin(self, asema, siirrot):
        """
        Apufunktio, joka suodattaa pois automaattisesti häviävät siirrot.

        :param asema: int, bittilauta ruudulle, jossa nappula on.
        :param siirrot: int, bittilauta siirtomahdollisuuksista.
        :return: int, bittilauta suodatetuista siirtomahdollisuuksista.
        """

        asemat = self.asemat()
        liikkumistiedot = self.liikkumistiedot()
        shakit = self.shakit()

        for siirto in bittien_bittilaudat(siirrot):
            vuorossa = self.__siirtonumero % 2 == 0
            uusi_lauta = Teorialauta(self.__siirtonumero, *asemat,
                                     *liikkumistiedot, *shakit)

            uusi_lauta.tee_siirto(asema, siirto)

            if (not vuorossa and uusi_lauta.__v_shakissa) or \
                    (vuorossa and uusi_lauta.__m_shakissa):
                siirrot -= siirto

        return siirrot

    def tee_siirto(self, asema, siirto):
        """
        Funktio, jolla asemat muuttuvat annetun siirron mukaisesti.

        :param asema: int, bittilauta, jossa on vain sijaintiruutu.
        :param siirto: int, bittilauta, jossa on vain siirtotiruutu.
        """

        asemat = self.asemat()
        valkoisen_siirto = self.__siirtonumero % 2 == 1

        indeksi = 0
        siirto_loytyi = False
        asema_loytyi = False

        for i in range(0, 12):
            if asemat[i] & siirto:
                asemat[i] -= siirto
                siirto_loytyi = True

            if asemat[i] & asema:
                asemat[i] |= siirto
                asemat[i] -= asema
                indeksi = i
                asema_loytyi = True

            if siirto_loytyi and asema_loytyi:
                break

        # Linnoittamista varten:
        if (indeksi == 1 and asema == self.RUUTU_A1) or \
                (indeksi >= 6 and siirto == self.RUUTU_A1):
            self.__vv_torni_lahtoasemassa = False

        if (indeksi == 1 and asema == self.RUUTU_H1) or \
                (indeksi >= 6 and siirto == self.RUUTU_H1):
            self.__vo_torni_lahtoasemassa = False

        if (indeksi == 7 and asema == self.RUUTU_A8) or \
                (indeksi < 6 and siirto == self.RUUTU_A8):
            self.__mv_torni_lahtoasemassa = False

        if (indeksi == 7 and asema == self.RUUTU_A8) or \
                (indeksi < 6 and siirto == self.RUUTU_A8):
            self.__mo_torni_lahtoasemassa = False

        if indeksi == 5 or (indeksi >= 6 and siirto == self.RUUTU_E1):
            self.__v_kuningas_lahtoasemassa = False
        if indeksi == 11 or (indeksi < 6 and siirto == self.RUUTU_E8):
            self.__m_kuningas_lahtoasemassa = False

        # Jos linnoittaminen tapahtuu, myös tornit siirtyvät
        if self.__linnoittaminen:

            if indeksi == 5 and siirto == self.RUUTU_C1:
                asemat[1] -= self.RUUTU_A1
                asemat[1] |= self.RUUTU_D1

            elif indeksi == 5 and siirto == self.RUUTU_G1:
                asemat[1] -= self.RUUTU_H1
                asemat[1] |= self.RUUTU_F1

            elif indeksi == 11 and siirto == self.RUUTU_C8:
                asemat[7] -= self.RUUTU_A8
                asemat[7] |= self.RUUTU_D8

            elif indeksi == 11 and siirto == self.RUUTU_G8:
                asemat[7] -= self.RUUTU_H8
                asemat[7] |= self.RUUTU_F8

            else:
                self.__linnoittaminen = False

        # Kuningattareksi nousu sotilaalle laudan päädyssä
        if siirto & asemat[0] & self.RIVI_8:
            asemat[0] -= siirto
            asemat[4] |= siirto

        if siirto & asemat[6] & self.RIVI_1:
            asemat[6] -= siirto
            asemat[10] |= siirto

        # Päivitä nappuloiden paikat, shakkitilanne ja siirtonumero
        self.__v_sotilaat = asemat[0]
        self.__v_tornit = asemat[1]
        self.__v_ratsut = asemat[2]
        self.__v_lahetit = asemat[3]
        self.__v_kuningatar = asemat[4]
        self.__v_kuningas = asemat[5]
        self.__m_sotilaat = asemat[6]
        self.__m_tornit = asemat[7]
        self.__m_ratsut = asemat[8]
        self.__m_lahetit = asemat[9]
        self.__m_kuningatar = asemat[10]
        self.__m_kuningas = asemat[11]

        self.tarkista_shakit()
        self.__siirtonumero += 1

        if valkoisen_siirto:
            if self.__v_shakissa or not asemat[5]:
                self.__voittaja = "musta"

        else:
            if self.__m_shakissa or not asemat[11]:
                self.__voittaja = "valkoinen"

    def tarkista_shakit(self):
        """
        Apufunktio, jolla voi päivittää, onko kuninkaat shakitettuina.
        """

        asemat = self.asemat()

        self.__m_shakissa = False

        for siirrot in self.puolen_kaikki_siirrot("valkoinen").values():

            if siirrot & asemat[11]:
                self.__m_shakissa = True

            if siirrot & (self.RUUTU_B8 | self.RUUTU_C8 | self.RUUTU_D8):
                self.__mv_reitti_uhattuna = True

            if siirrot & (self.RUUTU_F8 | self.RUUTU_G8):
                self.__mo_reitti_uhattuna = True

        self.__v_shakissa = False

        for siirrot in self.puolen_kaikki_siirrot("musta").values():

            if siirrot & asemat[5]:
                self.__v_shakissa = True

            if siirrot & (self.RUUTU_B1 | self.RUUTU_C1 | self.RUUTU_D1):
                self.__vv_reitti_uhattuna = True

            if siirrot & (self.RUUTU_F1 | self.RUUTU_G1):
                self.__vo_reitti_uhattuna = True


def bittien_indeksit(bittilauta):
    """
    Apufunktio bittilaudan indeksien hakemiseen.

    :param bittilauta: int, bittilauta, jonka bittien indeksit etsitään.
    :return: [int, ...]: indeksit, joissa bittilaudalla on ykkösiä.
    """

    if not bittilauta:
        return []

    indeksit = []
    while bittilauta:
        bitti = bittilauta & ~(bittilauta-1)
        indeksit.append(np.log2(bitti).astype(int))

        bittilauta &= bittilauta-1

    return indeksit


def bittien_bittilaudat(bittilauta):
    """
    Apufunktio bittilaudan bittien erottelemiseen omiksi laudoikseen.

    :param bittilauta: int, bittilauta, jonka bitit erotellaan.
    :return: [int, ...]: bittilaudat, joissa vain yksi bitti on asetettuna.
    """

    if not bittilauta:
        return []

    bittilaudat = []
    while bittilauta:
        bitti = bittilauta & ~(bittilauta-1)
        bittilaudat.append(np.uint64(bitti))

        bittilauta &= bittilauta - 1

    return bittilaudat
