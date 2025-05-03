# Kursinis darbas - Tic Tac Toe

## Įvadas

Šio darbo tikslas – sukurti klasikinio „Tic Tac Toe“ žaidimo programą, naudojant objektiškai orientuotą programavimą (OOP). Darbe įgyvendinti visi keturi OOP principai, pritaikytas dizaino šablonas (Singleton), panaudota kompozicija tarp klasių, realizuotas grafinis vartotojo sąsajos (GUI) valdymas bei vieneto testavimas.

### Kaip paleisti programą

1. Reikalavimai: `Python 3.10+`, bibliotekos `pygame`, `tkinter`.
2. Paleiskite pagrindinį failą:

```bash
python main.py
```

### Kaip naudotis programa

- Pasirinkite žaidimo režimą pagrindiniame lange (PVP ar prieš kompiuterį, pasirinkus kompiuterį, atitinkamai pasirinkite sunkumo lygį).
- Žaidimas vyksta langelyje su grafika ir garsais (vykstant ėjimui bei pasiekus pergalei).
- Rezultatai automatiškai nuskaitomi bei saugomi CSV faile.

---

## Analizė

### 1. OOP principai

- **Encapsulation (Inkapsuliacija)**: Klasės `Player`, `Board`, `AIPlayer` valdo savo duomenis per kintamuosius ir metodus.
- **Inheritance (Paveldėjimas)**: `AIPlayer` klasė paveldi iš `Player`, taip perima bendrą elgseną.
- **Polymorphism (Polimorfizmas)**: Abi klasės (`Player`, `AIPlayer`) turi metodą `get_move`, kuris iškviečiamas vienodai, nepriklausomai nuo objekto tipo.
- **Abstraction (Abstrakcija)**: Sudėtinga logika, pvz., laimėjimo patikra `check_win()`, paslėpta paprastuose metoduose.

### 2. Dizaino šablonas

Naudotas **Singleton** šablonas užtikrina, kad tam tikras objektas (pvz., `Board`) turi tik vieną egzempliorių visoje programos eigoje. Testai `test_singleton.py` patvirtina jo taikymą.

### 3. Kompozicija ir Agregacija

- `GUIGame` klasė naudoja `Board`, `Player`, `AIPlayer`, `FileHandler` – tai rodo objekto kompoziciją.
- Kiekvienas komponentas sukurtas taip, kad bendradarbiautų per aiškiai apibrėžtas sąsajas.

### 4. Failų operacijos

- Naudojamas `results.csv` failas rezultatų saugojimui bei vėliasniam jų nuskaitymui.
- Failai tvarkomi su `file_handler.py`, užtikrinant duomenų įrašymą ir nuskaitymą.

### 5. Testavimas

- Vieneto testai sukurti `unittest` pagrindu.
- Kiekviena pagrindinė komponentė testuojama atskirai: AI elgsena, lentos veikimas, failai ir t. t.

### 6. Kodo stilius

- Kodas atitinka `PEP8` standartus.
- Naudojami prasmingi pavadinimai, teisingas įtraukimas, modulų struktūra aiški ir logiška.

---

## Rezultatai

- ✅ Sukurtas veikiantis GUI žaidimas su PVP ir AI režimais.
- ✅ Pritaikyti visi OOP principai.
- ✅ Naudotas Singleton dizaino šablonas.
- ✅ Sukurti vieneto testai.
- ✅ Įgyvendintos failų operacijos.
- ✅ Palaikomas grafinis ir garsinis sąsajos palaikymas.

---

## Išvados

Darbas parodė gilų OOP principų ir Python kalbos išmanymą. Sukurta programa ne tik veikia praktiškai, bet ir atitinka aukštus programinės įrangos kūrimo standartus. Ateityje žaidimą galima plėsti įtraukiant:

- Didesnes lentas (5x5, 10x10),
- Sudėtingesnį AI (Minimax),
- Tinklinį žaidimą (multiplayer per internetą),
- Rezultatų analizės sistemą.

---

## Šaltiniai

- [Python dokumentacija](https://docs.python.org/3/)
- [PEP8 stiliaus gidas](https://peps.python.org/pep-0008/)
- [Unit testing](https://docs.python.org/3/library/unittest.html)
- [Tkinter dokumentacija](https://docs.python.org/3/library/tkinter.html)
- [Pygame dokumentacija](https://www.pygame.org/docs/)
