# TSOHA
## Vuokramökkien varaus-sovellus.

### Sovelluksen toiminnot:

1. Selaa vuokramökkejä
    - Katso koko, sijainti, hinta/per vrk ja rakennusvuosi.
    - Varatut ja vapaat mökit näkyvät erikseen.
  
2. Varaa vapaa mökki.
    - Vaatii oman käyttäjän
  
3. Luo käyttäjä.
    - Omalla käyttäjällä voit vuokrata mökin.
    - Voit laittaa mökkisi vuokralle.
    - Voit arvostella mökin.

4. Mökeille voi antaa arvosteluja joita muut vuokraajat voivat katsella.
    Arvostelut sisältää seuraavia tietoja:
    - yleinen arvosana 1-5.
    - muutamia lauseita omasta mielipiteestä

5. Sovelluksessa on myös toimintoja ilman omaa käyttäjää.
    - Mökkien, paikkakuntien ja arvosteluiden selaaminen.
    
6. Selaa paikkakuntia, jossa vuokramökit sijaitsee.
    - paikkakunta ja mökkien lukumäärä sillä paikkakunnalla.
### Fly.io
   - Sovellus ei ole testattavissa Fly.iossa


### Sovelluksen käyttö/testaaminen (komentorivillä)

Aloita kloonaamalla tämä repositorio tietokoneellesi komennolla:
```bash
git clone https://github.com/pakkanep/TSOHA.git
```


Luo sitten juurihakemistoon tiedosto .env seuraavanlaisella sisällöllä:


DATABASE_URL="postgresql://käyttäjä:salansana@localhost:5432/tietokannan_nimi"

SECRET_KEY='18fd24bf6a2ad4dac04a33963db1c42f'

Tietokannan osoite saattaa olla erilainen sinun tietokoneella ja jos et ole varma tiedoista niin
hyödyllinen komento psql komentorivillä on:
```bash
user=# \conninfo
```

Salaisen avaimen saat komentorivillä näin:
```bash
$ python3
>>> import secrets
>>> secrets.token_hex(16)
'18fd24bf6a2ad4dac04a33963db1c42f'
```

Seuraavaksi voit asentaa virtuaaliympäristön komennolla:
```bash
python3 -m venv venv
```

Virtuaaliympäristön asennuksen jälkeen aktivoi se komennolla:
```bash
 source venv/bin/activate
```

Virtuaaliympäriston ollessa aktiivinen, asenna riippuvuudet komennolla:
```bash
pip install -r ./requirements.txt
```

Määritä vielä tietokannan taulut komennolla
```bash
psql < schema.sql
```
Nyt sovelluksen käynnistäminen pitäisi onnnistua komennolla
```bash
flask run
```
