OHJE KÄYTTÖÖN
-------------------------------------------------------------------------------
Tallentamalla tiedostot samaan kansioon ja ajamalla gui.py voit testata shakin
ja shakkikoneen toimintaa. Vaihtoehtoisesti voi ajaa shakkikone.py:tä
valitsemillaan parametreilla, jolloin saa tietoa shakkikoneen nopeudesta.
-------------------------------------------------------------------------------
PROJEKTISTA
-------------------------------------------------------------------------------
Tämä shakkiprojekti koostuu kolmesta rajapinnasta:
- teorialauta.py
- gui.py (graafinen käyttöliittymä)
- shakkikone.py

Alkuperäinen ohjelma oli lisätehtävä kurssille. Se oli toteutettu yhtenä
luokkana ja tiedostona. Kehittämisen jatkuessa, oli järkevintä erotella pelin
teoreettinen ja graafinen pyöritys omiin luokkiinsa ja tiedostoihinsa.
Myöhemmin lähdin kehittelemään shakkikonetta ja yksinpelimahdollisuutta
tavoitteenani ymmärtää koneoppimista paremmin käytännössä, minkä takia olen
vältellyt tyypillisiä koneoppimiskirjastoja.

-------------------------------------------------------------------------------
VERSIOHISTORIA
-------------------------------------------------------------------------------
1.0 Graafisena käyttöliittymänä toteutettu shakkipeli.
-------------------------------------------------------------------------------
1.1 Teorialauta ja graafinen käyttöliittymä eroteltuina,
    muutamia muita laadullisia parannnuksia.
-------------------------------------------------------------------------------
1.2 Muutettu kaikki tietorakenteet merkkijonokoordinaateista (esim. "a1")
    bittilaudoiksi (esim. np.uint64(0x0000000000000001)).
-------------------------------------------------------------------------------
1.3 Lisätty shakkikone, joka toimii alpha-beta minimax -algoritmilla.
-------------------------------------------------------------------------------
(kehitettävää) Shakkikoneen nopeutus/parantelu, graafisen käyttöliittymän
    viimeistely.
-------------------------------------------------------------------------------