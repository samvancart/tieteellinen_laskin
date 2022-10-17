# Toteutusdokumentti

### Ohjelman rakenne
Ohjelma (tieteellinen_laskin) sisältää kuusi luokkaa, jotka vastaavat toimintalogiikasta, sekä käyttöliittymästä vastaavan `UI`-luokan. `InputHandler`-luokka käsittelee ensin merkkijonomuotoisen syötteen (validoi syötteen ja muuntaa listaksi), jonka ohjelman käyttäjä syöttää laskimeen. Tämän jälkeen syöte annetaan listana luokalle `Rpn`, joka vastaa syötteen muuntamisesta käänteiseksi puolalaiseksi notaatioksi. Tässä käytetään Edsger Dijkstran *shunting_yard* -algoritmin toteutusta. `Rpn`-luokan palauttama lista annetaan `Calculator`-luokalle, joka palauttaa kyseisen matemaattisen lausekkeen arvon. Arvo annetaan lopuksi käyttöliittymälle, joka näyttää sen käyttäjälle. Jos mikä tahansa luokka palauttaa virheen, tulee näkyville sana 'error'. Muuttujien luomisesta vastaavat luokat- `Variable` ja `VariableHandler`. Lisäksi on vielä `InputStack`-luokka joka on pino, joka sisältää käyttäjän syöttämät merkit. Pinon avulla syötettyjä merkkejä voi poistaa merkki kerrallaan.   
### Aikavaativuudet
Ohjelman aikavaativuuksia ei testattu.
### Parannusehdotukset
Ohjelmaan voisi lisätä uusia funktioita ja mahdollistaa omien muuttujien poistamisen.
### Lähteet
https://en.wikipedia.org/wiki/Shunting_yard_algorithm  