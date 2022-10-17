# Tieteellinen laskin
## CI ja testikattavuus
[![CircleCI](https://circleci.com/gh/samvancart/tieteellinen_laskin.svg?style=svg)](https://app.circleci.com/pipelines/gh/samvancart/tieteellinen_laskin)

[![codecov](https://codecov.io/gh/samvancart/tieteellinen_laskin/branch/main/graph/badge.svg?token=969DQIMFTE)](https://codecov.io/gh/samvancart/tieteellinen_laskin)
## Dokumentaatio
[Määrittelydokumentti](https://github.com/samvancart/tieteellinen_laskin/blob/main/dokumentaatio/maarittelydokumentti.md)  
[Testausdokumentti](https://github.com/samvancart/tieteellinen_laskin/blob/main/dokumentaatio/testausdokumentti.md)  
[Toteutusdokumentti](https://github.com/samvancart/tieteellinen_laskin/blob/main/dokumentaatio/toteutusdokumentti.md)  
[Käyttöohje](https://github.com/samvancart/tieteellinen_laskin/blob/main/dokumentaatio/kayttoohje.md)  
### Viikkoraportit
[viikko_1](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_1.md)  
[viikko_2](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_2.md)  
[viikko_3](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_3.md)  
[viikko_4](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_4.md)  
[viikko_5](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_5.md)  
[viikko_6](https://github.com/samvancart/tieteellinen_laskin/blob/main/viikkoraportit/viikko_6.md)  
## Ohjelman asennus
### Projektin kloonaaminen
Avaa komentorivi (Windowsilla Git Bash). Luo projektille hakemisto tietokoneellesi ja kloonaa projekti hakemistoon kommennolla  
`git clone https://github.com/samvancart/tieteellinen_laskin`  
Siirry kloonatun projektin juurihakemistoon komennolla  
`cd tieteellinen_laskin`
### Riippuvuuksien asennus
`poetry install`

### Ohjelman suorittaminen

`poetry run invoke start`

### Testien suorittaminen

`poetry run invoke test`

### Testikattavuusraportti

`poetry run invoke coverage-report`

Generoitu raportti löytyy _htmlcov_-hakemistosta.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

`poetry run invoke lint`