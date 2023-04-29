# TSOHA
## Vuokramökkien varaus-sovellus.

### Sovelluksen toiminnot:

1. Selaa vuokramökkejä
    - Katso koko, sijainti, hinta/per vrk. Kuvia mökistä(?). Mökit näkyvät vain jos ne ovat vuokrattavissa.
  
2. Varaa vapaa mökki.

3. Luo tarkennettu haku. Tarkennettuja tietoja voisi olla vaikka:
    -  neliömäärä min/max.
    -  hinta min/max.
    -  sijainti.
    -  näytä vain vapaana olevat mökit.
  
4. Luo käyttäjä, jonka kanssa voit varata mökin.

5. Mökeille voi antaa arvosteluja joita muut vuokraajat voivat katsella.
Arvostelut voisivat sisältää seuraavia tietoja:
    - yleinen arvosana 1-10.
    - muutamia lauseita omasta mielipiteestä


### Sovelluksen käyttö/testaaminen

Aloita kloonaamalla tämä repositorio tietokoneellesi komennolla:
```bash
$ git clone https://github.com/pakkanep/TSOHA.git
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
$ python3 -m venv venv
```

Virtuaaliympäristön asennuksen jälkeen aktivoi se komennolla:
```bash
 $ source venv/bin/activate
```

Virtuaaliympäriston ollessa aktiivinen, asenna riippuvuudet komennolla:
```bash
(venv) $ pip install -r ./requirements.txt
```

Määritä vielä tietokannan taulut komennolla
```bash
(venv) $ psql < schema.sql
```
Nyt sovelluksen käynnistäminen pitäisi onnnistua komennolla
```bash
(venv) $ flask run
```
