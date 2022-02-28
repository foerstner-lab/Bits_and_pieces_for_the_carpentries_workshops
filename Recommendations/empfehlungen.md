# Empfehlungen rund um die Workshop Themen

## Python-Library-Empfehlungen
Python - Standard Libraries - Third Party Libraries
- [Python Standard Libraries](https://docs.python.org/3/library/)
  * [pathlib](https://docs.python.org/3/library/pathlib.html)
- [Selenium](https://pypi.org/project/selenium/)
- [Seaborn](https://seaborn.pydata.org/)
- [bokeh](https://docs.bokeh.org/en/latest/index.html)
- [black](https://pypi.org/project/black/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NLTK](https://www.nltk.org/)
- [Django](https://www.djangoproject.com/)
- [flask](https://www.fullstackpython.com/flask.html)
- [Camelot](https://camelot-py.readthedocs.io/en/master/)

## Lese-/Hör-/Seh-Empfehlungen

### Lesen
- Buch [Automate boring stuff with Python](https://automatetheboringstuff.com/) (komplett online CC-BY); Deutsche version "Routineaufgaben mit Python automatisieren"
- Buch [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/) (fortgeschritten)
 - Buch [Weniger schlecht progammieren](https://www.oreilly.de/buecher/120174/9783897215672-weniger-schlecht-programmieren.html)
- [PyCoders Weekly](https://pycoders.com) Newsletter
- Buch [Seven languages in seven weeks](https://pragprog.com/book/btlang/seven-languages-in-seven-weeks)
- [The 35 Words You Need to Python](https://yawpitchroll.com/posts/the-35-words-you-need-to-python/)
- Buch [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/)
- Buch https://git-scm.com/book/en/v2
- [Oh Shit, Git?!?](https://ohshitgit.com/de)
- [GitHub Pages](https://pages.github.com/)

### Podcasts
- [Command Line Heros](https://www.redhat.com/en/command-line-heroes) (en) - "Command Line Heroes tells the epic true tales of how developers, programmers, hackers, geeks, and open source rebels are revolutionizing the technology landscape." Z. B.
  * [Python's Tale](https://www.redhat.com/en/command-line-heroes/season-3/pythons-tale)
  * [Heroes in a Bash Shell](https://www.redhat.com/en/command-line-heroes/season-3/heroes-in-a-bash-shell)
- [Talk Python to me](https://talkpython.fm/) (en)
- [PythonBytes](https://pythonbytes.fm/) (en)

### Videos
- [PyCon](https://www.youtube.com/results?search_query=pycon&search_type=) - Talks, Tutorial und vieles mehr von den PyCon-Konferenzen

## Text-Editoren/IDEs (integrated development environment)

1) [PyCharm](https://www.jetbrains.com/pycharm/)
2) [Spyder](https://www.spyder-ide.org/)
3) [Atom](https://atom.io/)
4) [Emacs](https://www.gnu.org/software/emacs/)
5) [Geany](https://www.geany.org/)
6) [Visual Studio Code](https://code.visualstudio.com/) / [VSCodium](https://github.com/VSCodium/vscodium) (binary releases of VS Code without MS branding/telemetry/licensing )
7) [Notepad ++](https://notepad-plus-plus.org/)
8) ... [viele mehr](https://en.wikipedia.org/wiki/List_of_text_editors)
### Anforderungen an einen guten Editor/IDE
- Quellcode speichern und wieder laden 
    - Eine IDE oder ein Editor muss Deine Arbeit speichern und alles später wieder öffnen, und zwar in demselben Zustand, in dem es sich zuvor befand, um so Zeit für die Entwicklung zu sparen.
- Ausführung von innerhalb der Umgebung
    - Es sollte einen eingebauten Compiler haben, um den Code auszuführen. Wenn er nicht in der gleichen Software ausgeführt wird, dann ist es wahrscheinlich ein Texteditor. 
- Debugging-Unterstützung
    - Der Debugger in den meisten IDEs bietet die Möglichkeit, schrittweise durch den Code zu gehen und Haltepunkte um den Code teilweise auszuführen. 
- Syntax-Hervorhebung
    - Die Fähigkeit, Schlüsselwörter, Variablen und Symbole in Ihrem Code schnell zu erkennen, erleichtert das Lesen und Verstehen des Codes erheblich.
- Automatische Code-Formatierung
    - Dies ist ein interessantes Merkmal; der Code rückt sich selbst ein, wenn der Entwickler Schleifen, Funktionen oder einen anderen Blockcode verwendet.
    
## Wie kann man weitermachen:
 
 - Lektionen selbstständig reproduzieren
 - kleine alltägliche Aufgabe finden, die man mit Hilfe des Gelernten lösen kann, so das sie automatisch abläuft
 - [HackyHour](https://hackyhour.github.io/Cologne/) organisieren 
 - Bei Problemen melden (wir helfen gerne falls möglich)

### Beispiele für Einsatz von Python(-Skripten) im Biblioteksalltag:

### Mögliche Projekte:
- Linkchecker
- Manipulation von großen Excel-Dateien / wiederkehrende Arbeiten in Excel
- Sicherung von wichtigen Dateien
- Änderung der Namensansetzung fürs Katalogisieren, Beispiel:
  - IN: "Wolfgang Amadeus Mozart"
  - OUT: "Mozart, Wolfgang Amadeus"
- Identifizierung von Lücken in der Signaturenvergabe

### Python-Funktionen:
Beispiel-Projekt: Liste mit Bestellungen auf Zeitschriftenartikel soll mit pandas verarbeitet werden. Um die Liste auswerten zu können, benötigt man einen eindeutigen Wert. Bei Zeitschriften bietet sich da bspw. die ISSN an.
  - ISSNs bereinigen:
    - **.astype(str)**: ISSNs bestehen aus Ziffern, einem Bindestrich und ggf. einem X und sind somit kein Integer oder floar. Das Umwandeln in einen String beugt Verwirrungen vor.
    - **.upper()**: ISSNs, welche auf "X" enden sind in der vorliegenden Liste inkonsistent, da händisch erfasst oder aus verschiedenen Quellen stammend (Bsp. "0000-123X" und "0000-123x"). Mit .upper() kann man alle Xe groß schreiben.
    - **.replace()**: ISSNs sind auch inkonsistent in der Schreibweise (Bsp.: "0000-1234" und "0000 - 1234"), mit .replace() kann die Schreibweise vereinheitlicht werden
  - Struktur der Liste bearbeiten:
    - **.keys()**: zeigt alle Spaltenüberschriften an
    - **.rename()**: ändert Spaltennamen
    - **.drop()**: löscht Spalten oder Reihen
    - **.groupby()**: gruppiert nach Werten
    - **.drop_duplicates()**: löscht Reihen nach dubletten Werten
  - Liste auswerten:
    - **.count()**: benutzt, um bspw. Bestellzahlen auf ISSNs zu ermitteln, wie oft wird eine ISSN in der Datei genannt? => Anzahl der Bestellungen
    - **.to_excel()**: speichert das Ergebnis als Excel-Datei ab
    
## Tipps & Tricks

- [Unix Subsystem unter Windows 10](https://docs.microsoft.com/de-de/windows/wsl/install-win10)
- [Python 3 Quick Tip: The easy way to deal with file paths on Windows, Mac and Linux](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)
- [GitHub Email privacy issue auflösen](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address)
### Binder
#### Ausweichmöglichkeit, falls Anaconda nicht funktioniert
Gehe auf https://mybinder.org/. Kopiere die URL 
https://github.com/foerstner-lab/Bits_and_pieces_for_the_carpentries_workshops 
nach "GitHub-Repositorium-Name oder URL"
und füge "empty_jupyter_notebook_for_binder.ipynb" in 
"Pfad zu einer Notebook-Datei" ein.

Klicke auf "launch".

### Wie man Python in Windows startet
In der Bash
ZBMED-Konfiguration:
```
$ /c/ProgramData/Anaconda3/python
```
