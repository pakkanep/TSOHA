# TSOHA
## Vuokramökkien varaus-sovellus.

### Sovelluksen toiminnot:

1. Selaa vuokramökkejä
    - Katso koko, sijainti, hinta/per vrk. Kuvia mökistä(?). Onko mökki vapaana vai varattu.
  
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
- Sovelluksen olisi tarkoitus toimia niin että käyttäjä itse määrittelee manuaalisesti yhdistettävän tietokannan (nimet käyttäjät jne).

- Itse määrittelin yhteyden näin: app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:salasana@localhost:5432/postgres"

- Sovellus myös olettaa, että tietokannasta löytyisi seuraavanlainen taulu:

CREATE TABLE cabins(id SERIAL PRIMARY KEY, name TEXT, location TEXT, year INT, availability INT)

- Sovellus on vielä todella vaiheessa eikä siinä juurikaan ole toimintoja.
  
