# Toteutusdokumentti

### Ohjelman rakenne
Ohjelma (tieteellinen_laskin) sisältää kolme luokkaa, jotka vastaavat toimintalogiikasta, sekä käyttöliittymästä vastaavan `UI`-luokan. `InputHandler`-luokka käsittelee ensin merkkijonomuotoisen syötteen (validoi syötteen ja muuntaa listaksi), jonka ohjelman käyttäjä syöttää laskimeen. Tämän jälkeen syöte annetaan listana luokalle `Rpn`, joka vastaa syötteen muuntamisesta käänteiseksi puolalaiseksi notaatioksi. Tässä käytetään Edsger Dijkstran *shunting_yard* -algoritmin toteutusta. `Rpn`-luokan palauttama lista annetaan `Calculator`-luokalle, joka palauttaa kyseisen matemaattisen lausekkeen arvon. Arvo annetaan lopuksi käyttöliittymälle, joka näyttää sen käyttäjälle. Jos mikä tahansa luokka palauttaa virheen, tulee näkyville sana 'error'.  
### Aikavaativuudet
Ohjelman aikavaativuuksia ei vielä testattu.
### Parannusehdotukset
Ohjelman tulisi voida käsitellä funktioita ja mahdollisesti myös tukea omien muuttujien käyttöä.
### Lähteet
https://en.wikipedia.org/wiki/Shunting_yard_algorithm

