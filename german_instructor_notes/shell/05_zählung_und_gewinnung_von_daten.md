---
Titel: "Zählen und Gewinnung mit der Shell"
Unterricht: 60
Übungen: 30
Fragen:
- "Wie kann ich Daten zählen?"
- "Wie kann ich Daten in Dateien finden?"
- "Wie kann ich bestehende Befehle kombinieren, um neue Dinge zu tun?"
Ziele:
- "Demonstriere das Zählen von Zeilen, Wörtern und Zeichen mit dem Shell-Befehl wc und den entsprechenden Flags".
- Strings verwenden, um Dateien zu durchsuchen und übereinstimmende Zeilen mit der Shell zu extrahieren.
- Komplexe einzeilige Befehle erstellen, indem man Shell-Befehle und reguläre Ausdrücke kombiniert, um Dateien zu durchsuchen.
- "Die Ausgabe eines Befehls in eine Datei umleiten."
- Eine Datei anstelle der Tastatureingabe mit Hilfe der Umleitung verarbeiten.
- "Befehlspipelines mit zwei oder mehr Stufen konstruieren."
- "Die Unix-Philosophie 'kleine Teile, lose verbunden' erklären."
Stichpunkte:
- "Die Shell kann verwendet werden, um Elemente von Dokumenten zu zählen"
- "Die Shell kann verwendet werden, um nach Mustern in Dateien zu suchen"
- "Mit Befehlen können beliebig viele Dateien gezählt und durchsucht werden".
- "Befehle und Flags können kombiniert werden, um komplexe Abfragen zu erstellen, die auf deine Arbeit zugeschnitten sind"

---
## Zählen und Auswerten von Daten

Jetzt, wo du weißt, wie du in der Shell navigieren kannst, werden wir uns
wie man Daten zählt und auswertet, indem man einige der Standard-Shell-Befehle verwendet.
Diese Befehle werden deine Arbeit zwar nicht revolutionieren,
aber sie sind sehr vielseitig und bilden die Grundlage für deine Arbeit in der Shell
und zum Erlernen des Programmierens. Die Befehle spiegeln auch die Arten von Bibliotheksbenutzern wider, die mit Bibliotheksdaten arbeiten.

## Zählen und Sortieren

Wir beginnen damit, den Inhalt von Dateien mit der Unix-Shell zu zählen.
Mit der Unix-Shell können wir schnell Zählungen über Dateien hinweg erstellen,
etwas, das mit den grafischen Benutzeroberflächen der Standard-Office-Programme nur schwer zu erreichen ist.

Beginnen wir damit, in das Verzeichnis zu navigieren, das unsere Daten enthält, indem wir den
Befehl "cd":

~~~
$ cd shell-lesson
~~~

Denke daran, wenn du dir nicht sicher bist, wo du dich in deiner Verzeichnisstruktur befindest,
benutze den Befehl `pwd`, um das herauszufinden:

~~~
$ pwd
~~~

~~~
/Users/riley/Desktop/shell-lesson
~~~

Schauen wir uns den Inhalt von der africa Datei an

~~~
$ less 2014-01-31_JA-africa.tsv
~~~
Der Inhalt lässt sich sich schwer erahnen. Erweitern wir den Befehl durch den Flag -S

~~~
$ less -S 2014-01-31_JA-africa.tsv
~~~

Damit sehen wir zumindest besser, was in der Datei steckt. Aber vielleicht wollen wir noch mehr Details dieser Datei kennen. Prüfen wir nun, welche Dateien sich in dem Verzeichnis befinden und wie groß sie sind mit `ls -lhS`:

~~~
$ ls -lhS
~~~

~~~
total 139M
-rw-rw-r-- 1 riley staff 126M Jun 10 2015 2014-01_JA.tsv
-rw-r--r-- 1 riley staff 7.4M Jan 31 18:47 2014-01-31_JA-america.tsv
-rw-r--r-- 1 riley staff 3.6M Jan 31 18:47 2014-01-31_JA-africa.tsv
-rw-r--r-- 1 riley staff 1.4M Jan 31 18:47 2014-02-02_JA-britain.tsv
-rw-r--r-- 1 riley staff 583K Feb 1 22:53 33504-0.txt
~~~


In diesem Abschnitt konzentrieren wir uns auf das Dataset `2014-01_JA.tsv`, das die
Metadaten von Zeitschriftenartikeln enthält, und die drei `.tsv`-Dateien, die aus dem ursprünglichen
Datensatz abgeleitet wurden. Jede dieser drei "tsv"-Dateien enthält alle Daten, die ein Schlüsselwort wie
wie "Afrika" oder "Amerika" im Feld "Titel" von "2014-01_JA.tsv" vorkommt.

> ## CSV- und TSV-Dateien
> CSV (Comma-separated values) ist ein gängiges Textformat zum Speichern von tabellarischen
> Daten, wobei jeder Datensatz eine Zeile einnimmt und die Werte durch Kommas getrennt werden.
> TSV (Tab-getrennte Werte) ist dasselbe, nur dass die Werte durch
> Tabulatoren und nicht durch Kommas getrennt werden. Verwirrenderweise wird der Begriff CSV manchmal sowohl für CSV als auch für
> TSV und Variationen davon. Die Einfachheit der Formate macht sie ideal für
> Austausch und Archivierung. Sie sind nicht an ein bestimmtes Programm gebunden (im Gegensatz zu Excel
> Dateien gibt es kein "CSV"-Programm, sondern viele Programme, die das Format
> die das Format unterstützen, Darunter übrigens auch Excel.), und du hättest keine
> Probleme haben, eine 40 Jahre alte Datei zu öffnen, wenn du heute auf eine stößt.

Schauen wir uns zunächst die größte Datei an und verwenden die Werkzeuge, die wir bereits kennen:

~~~
$ cat 2014-01_JA.tsv
~~~


Wie bei `829-0.txt` zuvor, stürzt der ganze Datensatz vorbei und ich kann nicht wirklich einen
Sinn aus dieser Menge an Text machen. Um diese laufende Kon`cat`enation abzubrechen, oder überhaupt jeden
Prozess in der Unix-Shell abzubrechen, drücke <kbd>Strg</kbd>+<kbd>C</kbd>.

In den meisten Datendateien verrät ein kurzer Blick auf die ersten Zeilen bereits viel über die
über die Struktur des Datensatzes, zum Beispiel die Tabellen-/Spaltenüberschriften:

~~~
$ head -n 3 2014-01_JA.tsv
~~~

~~~
File Creator Issue Volume Journal ISSN ID Citation Title Place Labe Language Publisher Date
Geschichte_1a-rdf.tsv Doolittle, W. E. 1 59 KIVA -ARIZONA- 0023-1940 (Uk)RN001571862 KIVA -ARIZONA- 59(1), 7-26. (1993) A Method for Distinguishing between Prehistoric and Recent Water and Soil Control Features xxu eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY 1993
Geschichte_1a-rdf.tsv Nelson, M. C. 1 59 KIVA -ARIZONA- 0023-1940 (Uk)RN001571874 KIVA -ARIZONA- 59(1), 27-48. (1993) Classic Mimbres Land Use in the Eastern Mimbres Region, Southwestern New Mexico xxu eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY 1993

~~~


In der Kopfzeile sehen wir die üblichen Metadatenfelder von wissenschaftlichen Arbeiten: `Creator`, `Issue`, `Citation`, etc.

Als Nächstes lernen wir ein grundlegendes Werkzeug zur Datenanalyse kennen:
`wc` ist der Befehl "word count": Er zählt die Anzahl der Zeilen, Wörter und Bytes.
Da wir den Wildcard-Operator lieben, führen wir den Befehl
`wc *.tsv` aus, um die Zählungen für alle `.tsv` Dateien im aktuellen Verzeichnis zu erhalten
(es dauert ein bisschen, bis der Vorgang abgeschlossen ist):

~~~~
$ wc *.tsv
~~~~

~~~
    13712 511261 3773660 2014-01-31_JA-afrika.tsv
    27392 1049601 7731914 2014-01-31_JA-america.tsv
   507732 17606310 131122144 2014-01_JA.tsv
     5375 196999 1453418 2014-02-02_JA-britain.tsv
   554211 19364171 144081136 insgesamt
~~~


Die ersten drei Spalten enthalten die Anzahl der Zeilen, Wörter und Bytes.

Wenn wir nur eine Handvoll Dateien zu vergleichen haben, ist es vielleicht schneller oder bequemer
mit Microsoft Excel, OpenRefine oder deinem Lieblingstexteditor zu überprüfen, aber
Wenn wir aber zehn, hunderte oder tausende von Dokumenten haben, hat die Unix-Shell einen klaren
Geschwindigkeitsvorteil. Die wahre Stärke der Shell liegt in der Möglichkeit, Befehle zu kombinieren
und Aufgaben zu automatisieren. Darauf werden wir gleich noch eingehen.

Zunächst werden wir sehen, wie wir eine einfache Pipeline erstellen können, um die kürzeste Datei zu finden
in Bezug auf die Anzahl der Zeilen zu finden. Wir fangen an, indem wir das Flag "l" (el) hinzufügen, um nur die
Anzahl der Zeilen und nicht die Anzahl der Wörter und Bytes:

~~~~
$ wc -l *.tsv
~~~~

~~~
    13712 2014-01-31_JA-afrika.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
     5375 2014-02-02_JA-britain.tsv
   554211 insgesamt
~~~


Der Befehl `wc` selbst hat kein Flag, um die Ausgabe zu sortieren, aber wir werden sehen, dass wir drei verschiedene Shell-Befehle kombinieren können, um das zu bekommen, was wir wollen.

Zuerst haben wir den Befehl "wc -l *.tsv". Wir speichern die Ausgabe dieses
Befehls in einer neuen Datei speichern. Dazu leiten wir die Ausgabe des Befehls in eine Datei um, indem wir das "Größer als"-Zeichen (>) verwenden, etwa so

~~~
$ wc -l *.tsv > lengths.txt
~~~


Jetzt gibt es keine Ausgabe mehr, da die Ausgabe in die Datei `lengths.txt` gegangen ist, aber
aber wir können überprüfen, ob die Ausgabe tatsächlich in der Datei gelandet ist, indem wir `cat` oder `less` verwenden
(oder Notepad oder einem anderen Texteditor) überprüfen.

Um Notepad über GitBash zu öffnen, müsst ihr den Pfas angeben, wo sich der exe File von Notepad befindet:

```
/c/WINDOWS/system32/notepad.exe lengths.txt
```

etwas umständlich auf Windows. Linux und Max lösen es anders mit dem `open` Befehl. Stattdessen könnt ihr auch wieder den `explorer .` Befehl nutzen, um euren File-Explorer an der Stelle, wo sich die Datei befindet, zu öffnen.

~~~~
$ cat lengths.txt
~~~~

~~~
    13712 2014-01-31_JA-afrika.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
     5375 2014-02-02_JA-britain.tsv
   554211 insgesamt
~~~


Als Nächstes gibt es den Befehl `sort`. Wir benutzen den `-n` Flag, um anzugeben, dass wir numerisch und nicht alphabetisch sortieren wollen, wir geben die Ergebnisse in
eine weitere Datei aus, und wir benutzen `cat`, um die Ergebnisse zu überprüfen:

~~~~
$ sort -n lengths.txt > sort-lengths.txt
$ cat sort-lengths.txt
~~~~

~~~
     5375 2014-02-02_JA-britain.tsv
    13712 2014-01-31_JA-afrika.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
   554211 insgesamt
~~~


Endlich haben wir unseren alten Freund `head`, mit dem wir die erste Zeile
der `sorted-lengths.txt` zu erhalten:

~~~~
$ head -n 1 sortierte-längen.txt
~~~~

~~~
     5375 2014-02-02_JA-britain.tsv
~~~


Aber wir sind wirklich nur am Endergebnis interessiert, nicht an den Zwischen
Zwischenergebnisse, die jetzt in `lengths.txt` und `sorted-lengths.txt` gespeichert sind. Was wäre, wenn wir
die Ergebnisse des ersten Befehls (`wc -l *.tsv`) direkt an den nächsten
Befehl (`sort -n`) und dann die Ausgabe dieses Befehls an `head -n 1`?
Zum Glück können wir das, indem wir ein Konzept namens Pipes verwenden. In der Befehlszeile machst du eine
Pipe mit dem vertikalen Balkenzeichen `|`. Versuchen wir es zuerst mit einer Pipe:

~~~~
$ wc -l *.tsv | sort -n
~~~~

~~~
     5375 2014-02-02_JA-britain.tsv
    13712 2014-01-31_JA-afrika.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
   554211 insgesamt
~~~


Beachte, dass dies genau die gleiche Ausgabe ist, die in unserer `sorted-lengths.txt` gelandet ist
landete. Fügen wir eine weitere Pipe hinzu:

~~~~
$ wc -l *.tsv | sort -n | head -n 1
~~~~

~~~
     5375 2014-02-02_JA-britain.tsv
~~~


Es kann einige Zeit dauern, bis man Pipes vollständig verstanden hat und sie effizient nutzen kann, aber es ist ein
aber es ist ein sehr mächtiges Konzept, das du nicht nur in der Shell, sondern auch in den meisten
Programmiersprachen.

> ## Pipes und Filter
> Diese einfache Idee ist der Grund, warum Unix so erfolgreich ist. Anstatt riesige Programme zu erstellen
> Programme zu entwickeln, die viele verschiedene Dinge tun, konzentrieren sich die Unix-Programmierer auf
> viele einfache Werkzeuge zu entwickeln, die jeweils eine Aufgabe gut erledigen und gut miteinander zusammenarbeiten.
> Dieses Programmiermodell wird "Pipes und Filter" genannt. Pipes haben wir schon gesehen; ein
> Filter ist ein Programm wie `wc` oder `sort`, das einen Eingabestrom in einen Ausgabestrom umwandelt.
> Ausgabestrom umwandelt. Fast alle Unix-Standardprogramme können auf diese Weise arbeiten: Wenn
> Wenn sie nicht anders angewiesen werden, lesen sie von der Standardeingabe, machen etwas damit
> und schreiben dann in die Standardausgabe.
>
> Der Schlüssel ist, dass jedes Programm, das Textzeilen von der Standardeingabe liest und
> Zeilen Text auf die Standardausgabe schreibt, mit jedem anderen Programm kombiniert werden kann, das
> sich ebenfalls so verhält. Du kannst und solltest deine Programme auf diese Weise schreiben, damit
> du und andere Leute diese Programme in Pipes einbinden können, um ihre Leistung zu vervielfachen.

<!-- Kopiert von https://swcarpentry.github.io/shell-novice/04-pipefilter/ -->

> ## Hinzufügen einer weiteren Pipe
> Wir haben unsere `wc -l *.tsv | sort -n | head -n 1` Pipeline. Was würde passieren
> wenn du diese Pipeline in `cat` einfügst? Probiere es aus!
>
> > ## Lösung
> > Der Befehl `cat` gibt nur das aus, was er als Eingabe bekommt, du bekommst also genau
> > die gleiche Ausgabe von
> >
> > ~~~
> > $ wc -l *.tsv | sort -n | head -n 1
> > ~~~
> > 
> >
> > und
> >
> > ~~~
> > $ wc -l *.tsv | sort -n | head -n 1 | cat
> > ~~~
> > 
> 



> ## Zählen der Anzahl der Dateien
> Lass uns eine andere Pipeline erstellen. Du willst herausfinden, wie viele Dateien und
> Verzeichnisse es im aktuellen Verzeichnis gibt. Versuche, ob du die Ausgabe von
> die Ausgabe von `ls` in `wc` leiten kannst, um die Antwort zu finden.
>
> > ## Lösung
> > ~~~
> > $ ls | wc -l
> > ~~~~
> >
> 


> ## Schreiben in Dateien
> Der Befehl "date" gibt das aktuelle Datum und die Uhrzeit aus. Kannst du das
> aktuelle Datum und die Uhrzeit in eine neue Datei namens "logfile.txt" schreiben? Dann überprüfe
> den Inhalt der Datei.
>
> > ## Lösung
> > ~~~
> > $ date > logfile.txt
> > $ cat logfile.txt
> > ~~~~
> > 
> > Um den Inhalt zu überprüfen, kannst du auch `less` oder viele andere Befehle verwenden.
> >
> > Pass auf, dass `>` gerne eine bestehende Datei überschreibt, ohne dich zu warnen,
> > sei also bitte vorsichtig.
> 


> ## Anhängen an eine Datei
> Während >` in eine Datei schreibt, fügt >>` etwas an eine Datei an. Versuche, das
> aktuelle Datum und die Uhrzeit an die Datei `logfile.txt` anzuhängen?
>
> > ## Lösung
> > ~~~
> > $ date >> logfile.txt
> > $ cat logfile.txt
> > ~~~~
> >
>


> ## Zählen der Anzahl der Wörter
>
> Schau im Handbuch für den Befehl `wc` nach (entweder mit `man wc` oder `wc --help`)
> um herauszufinden, welches Flag du verwenden musst, um die Anzahl der Wörter auszugeben
> (aber nicht die Anzahl der Zeilen und Bytes). Versuche es dann auf die `.tsv` Dateien im Verzeichnis anzuwenden.
>
> Wenn du Zeit hast, kannst du auch versuchen, die Ergebnisse zu sortieren, indem du sie an `sort` weiterleitest.
> Und / oder die anderen Flags von `wc` ausprobieren.
>
> > ## Lösung
> >
> > In `man wc` siehst du, dass es ein `-w` Flag gibt, um die Anzahl der
> > Wörter:
> >
> > ~~~
> > -w Die Anzahl der Wörter in jeder Eingabedatei wird auf die Standard
> > Ausgabe geschrieben.
> > ~~~
> >
> >
> > So werden die Wortzahlen der `.tsv`-Dateien ausgegeben:
> >
> > ~~~
> > $ wc -w *.tsv
> > ~~~
> >
> > ~~~
> > 511261 2014-01-31_JA-africa.tsv
> > 1049601 2014-01-31_JA-america.tsv
> > 17606310 2014-01_JA.tsv
> > 196999 2014-02-02_JA-britain.tsv
> > 19364171 gesamt
> > ~~~
> >
> >
> > Und um die Zeilen numerisch zu sortieren:
> >
> > ~~~
> > $ wc -w *.tsv | sort -n
> > ~~~
> >
> > ~~~
> > 196999 2014-02-02_JA-britain.tsv
> > 511261 2014-01-31_JA-afrika.tsv
> > 1049601 2014-01-31_JA-america.tsv
> > 17606310 2014-01_JA.tsv
> > 19364171 gesamt
> > ~~~
> > 
> 


## Mining oder Suche

Wir werden oft nach etwas in einer oder mehreren Dateien suchen müssen,
Deshalb wollen wir einen Befehl einführen, der dies ermöglicht: `grep` (kurz für **globaler regulärer
expression print**). Wie der Name schon sagt, unterstützt er reguläre Ausdrücke und
ist daher nur durch deine Vorstellungskraft, die Form deiner Daten und - wenn du mit Tausenden oder Millionen von Dateien arbeitest - durch die Rechenleistung, die dir zur Verfügung steht.

Um mit `grep` zu beginnen, wechsle zunächst in das Verzeichnis `shell-lesson`. Erstelle dann ein neues Verzeichnis "results":

~~~
$ mkdir results
~~~



Versuchen wir nun unsere erste Suche:

~~~
$ grep 1999 *.tsv
~~~

Grep" sucht dann in diesen Dateien nach der Zeichenkette "1999" und
druckt die passenden Zeilen aus.

> ## Zeichenketten
> Eine Zeichenkette ist eine Folge von Zeichen oder "ein Stück Text".


Drücke einmal den Pfeil nach oben, um zu deiner letzten Aktion zurückzukehren.
Ändere `grep 1999 *.tsv` in `grep -c 1999 *.tsv` und drücke Enter.

~~~
$ grep -c 1999 *.tsv
~~~

~~~
2014-01-31_JA-africa.tsv:804
2014-01-31_JA-america.tsv:1478
2014-01_JA.tsv:28767
2014-02-02_JA-britain.tsv:284
~~~


Die Shell gibt nun aus, wie oft die Zeichenkette 1999 in jeder Datei vorkommt.
Wenn du dir die Ausgabe des vorherigen Befehls ansiehst, bezieht sich das auf das
Datumsfeld für jeden Zeitschriftenartikel.

Wir versuchen eine andere Suche:

~~~
$ grep -c revolution *.tsv
~~~

~~~
2014-01-31_JA-africa.tsv:20
2014-01-31_JA-america.tsv:34
2014-01_JA.tsv:867
2014-02-02_JA-britain.tsv:9
~~~


Wir haben die Anzahl der Instanzen der Zeichenkette "Revolution" in den Dateien zurückbekommen.
Ändere nun den obigen Befehl in den folgenden ab und beobachte, wie sich die Ausgabe der beiden unterscheidet:

~~~
$ grep -ci revolution *.tsv
~~~

~~~
2014-01-31_JA-africa.tsv:118
2014-01-31_JA-america.tsv:1018
2014-01_JA.tsv:9327
2014-02-02_JA-britain.tsv:122
~~~


Dies wiederholt die Abfrage, druckt aber unabhängig von der Groß- und Kleinschreibung aus (einschließlich der Instanzen von `revolution` und `Revolution` und anderer Varianten).
Beachte, dass die Anzahl der Zeitschriftenartikel, die das Schlüsselwort "Amerika" enthalten, um fast das 30-fache unterscheidet. 
Wie zuvor kannst du zurückgehen und > results/" eingeben, gefolgt von einem Dateinamen (idealerweise im .txt-Format), um die Ergebnisse in einer Datei zu speichern.

Bisher haben wir die Zeichenketten in den Dateien gezählt und die Ergebnisse in der Shell oder in einer Datei ausgegeben. Aber die wahre Stärke von `grep` liegt darin, dass du damit auch Teilmengen von tabellarischen Daten (oder beliebigen Daten) aus einer oder mehreren Dateien erstellen kannst.  

~~~
$ grep -i revolution *.tsv
~~~


Dieses Skript sucht in den definierten Dateien und gibt alle Zeilen, die `revolution` enthalten
(ohne Rücksicht auf Groß- und Kleinschreibung) an die Shell. Wir lassen die Shell das heutige Datum an den
Dateinamen hinzufügen:

~~~
$ grep -i revolution *.tsv > results/$(date "+%Y-%m-%d")_JAi-revolution.tsv
~~~


Dies speichert die unterteilten Daten in einer neuen Datei.

> ## Alternative Datumsbefehle
> Diese Art, Daten zu schreiben, ist so verbreitet, dass du auf einigen Plattformen (nicht macOS X)
> dass du das gleiche Ergebnis erhältst, wenn du `$(date -I)` anstelle von
> `$(date "+%Y-%m-%d")`.


Wenn wir uns jedoch diese Datei ansehen, enthält sie jede Instanz der
Zeichenfolge "Revolution", sowohl als einzelnes Wort als auch als Teil anderer Wörter
wie z. B. "revolutionär". Das ist vielleicht doch nicht so nützlich, wie wir dachten...
Zum Glück weist das `-w` Flag `grep` an, nur nach ganzen Wörtern zu suchen,
So können wir unsere Suche präziser gestalten.

~~~
$ grep -iw revolution *.tsv > results/$(date "+%Y-%m-%d")_JAiw-revolution.tsv
~~~


Dieses Skript sucht in den  Dateien und exportiert alle Zeilen, die das ganze Wort "Revolution" enthalten 
in die angegebene `.tsv`-Datei.

Wir können den Unterschied zwischen den von uns erstellten Dateien anzeigen.

~~~
$ wc -l results/*.tsv
~~~

~~~
   10585 2016-07-19_JAi-revolution.tsv
    7779 2016-07-19_JAiw-revolution.tsv
   18364 insgesamt
~~~


> ## Automatisches Hinzufügen eines Datumspräfixes
> Beachte, dass wir das heutige Datum nicht selbst eingegeben haben, sondern dass der
> Befehl "date" diese sinnlose Aufgabe für uns erledigen. Erfahre mehr über die
> "+%Y-%m-%d"-Option und alternative Optionen, die wir hätten verwenden können.
>
> > ## Lösung
> > Wenn du `date --help` verwendest, wirst du sehen, dass die Option `+` ein
> > ein Datumsformat einführt, bei dem `%Y`, `%m` und `%d` durch das Jahr, > > Monat und Tag ersetzt werden,
> > Monat bzw. Tag ersetzt werden. Es gibt viele andere Prozent-Codes
> > die du verwenden kannst.
> >
> > Du kannst auch sehen, dass `-I` die Abkürzung für
> > [--iso-8601](https://en.wikipedia.org/wiki/ISO_8601), was
> > die Verwirrung zwischen dem europäischen
> > und amerikanischen Datumsformaten `DD.MM.YYYY` und `MM/DD/YYYY`.
> 


Zum Schluss verwenden wir die Syntax der **regulären Ausdrücke**, die wir bereits behandelt haben, um nach ähnlichen Wörtern zu suchen.

Der reguläre Ausdruck "fr[ae]nc[eh]" passt auf "france", "french", aber auch auf "frence" und "franch".
Im Allgemeinen ist es eine gute Idee, den Ausdruck in einfache Anführungszeichen zu setzen, da
Dies stellt sicher, dass die Shell den Ausdruck direkt an grep sendet, ohne ihn zu verarbeiten (z. B. indem sie versucht, den Wildcard-Operator * zu erweitern).

~~~
$ grep -iwE 'fr[ae]nc[eh]' *.tsv
~~~

E steht für regular expressions, i wieder und Groß und Kleinschreibweise zu ignorieren und w um nur nach ganzen Wörtern zu suchen.

Die Shell wird jede übereinstimmende Zeile ausdrucken.

Wir fügen das `-o` Flag hinzu, um nur den übereinstimmenden Teil der Zeilen auszugeben, z.B.
(praktisch, um Ergebnisse zu isolieren/überprüfen):

~~~
$ grep -iwEo 'fr[ae]nc[eh]' *.tsv
~~~

## Breakout Session
Mach dich mit deinem Nachbarn zusammen und bearbeite diese Aufgaben:

> ## Suche nach Groß- und Kleinschreibung
> Suche nach allen case-sensitive Instanzen von
> einem ganzen Wort, das ihr in allen vier abgeleiteten `.tsv`-Dateien in diesem Verzeichnis wählt.
> Gib deine Ergebnisse auf der Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -w hero *.tsv
> > ~~~
> >
> 


> ## Suche nach Groß- und Kleinschreibung in tsv-Dateien
> Suche nach allen case sensitive Instanzen eines Wortes, das du in
> den Dateien "Amerika" und "Afrika" `.tsv" in diesem Verzeichnis.
> Gib deine Ergebnisse auf der Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep hero *a.tsv
> > ~~~
> >
> 


> ## Wörter zählen (Groß- und Kleinschreibung beachten)
> Zähle alle Instanzen eines Wortes in den
> `.tsv'-Dateien "Amerika" und "Afrika" in diesem Verzeichnis.
> Gib deine Ergebnisse auf der Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -c hero *a.tsv
> > ~~~
> >
> 


> ## Wörter zählen (Groß-/Kleinschreibung nicht beachten)
> Zähle alle Instanzen dieses Wortes in den `.tsv'-Dateien "Amerika" und "Afrika" ohne Berücksichtigung der Groß- und Kleinschreibung
> Gib deine Ergebnisse auf der Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -ci hero *a.tsv
> > ~~~
> >
> 


> ## Groß- und Kleinschreibung nicht beachtende Suche in Select-Dateien
> Suche nach allen Instanzen dieses Wortes ohne Unterscheidung der Groß- und Kleinschreibung
> Wortes in den `.tsv'-Dateien "Amerika" und "Afrika" in diesem Verzeichnis. Lege deine Ergebnisse in einer tsv Datei im Ordner results ab.
>
> > ## Lösung
> > ~~~
> > $ grep -i hero *a.tsv > results/hero.tsv
> > ~~~
> >
>


> ## Suche nach Groß- und Kleinschreibung in Select-Dateien (ganzes Wort)
> Suche nach allen case insensitive Instanzen des ganzen Wortes
> in den `.tsv'-Dateien "Amerika" und "Afrika" in diesem Verzeichnis. Lege deine Ergebnisse in einer neuen tsv Datei im Ordner results ab.
>
> > ## Lösung
> > ~~~
> > $ grep -iw hero *a.tsv > results/hero-i.tsv
> > ~~~
> >
> 


### Eine Schleife zum Zählen von Wörtern verwenden

Wir werden nun eine Schleife verwenden, um das Zählen bestimmter Wörter in einem Dokument zu automatisieren. Dazu verwenden wir das E-Book _[Little Women](http://www.gutenberg.org/cache/epub/514/pg514.txt)_ vom [Project Gutenberg](https://www.gutenberg.org/). Die Datei befindet sich im Ordner `shell-lesson` und heißt `pg514.txt`. Benennen wir die Datei in `littlewomen.txt` um. 

~~~
$ mv pg514.txt littlewomen.txt
~~~

Damit wird die Datei in etwas umbenannt, das leichter zu tippen ist.

Jetzt erstellen wir unsere Schleife. In der Schleife bitten wir den Computer, den Text nach dem Namen eines jeden Mädchens zu durchsuchen,
und zu zählen, wie oft er vorkommt. Die Ergebnisse werden auf dem Bildschirm ausgegeben.

~~~
$ for name in "Jo" "Meg" "Beth" "Amy"
> do
> echo "$name"
> grep -wo "$name" littlewomen.txt | wc -l
> done
~~~

~~~
Jo
1355
Meg
683
Beth
459
Amy
645
~~~


Was passiert in der Schleife?  
+ `echo "$name"` gibt den aktuellen Wert von `$name` aus
+ `grep "$name" littlewomen.txt` findet jede Zeile, die den in `$name` gespeicherten Wert enthält. Das `-w`-Flag findet nur das ganze Wort, das den Wert in `$name` enthält, und das `-o`-Flag zieht diesen Wert aus der Zeile heraus, in der er steht, damit du die eigentlichen Wörter als eigene Zeilen zählen kannst.
+ Die Ausgabe des Befehls `grep` wird mit der Pipe `|` umgeleitet (ohne die Pipe und den Rest der Zeile würde die Ausgabe von `grep` direkt auf den Bildschirm ausgegeben)
+ `wc -l` zählt die Anzahl der _Zeilen_ (weil wir das `-l` Flag benutzt haben), die von `grep` gesendet wurden. Da `grep` nur Zeilen zurückgab, die den in `$name` gespeicherten Wert enthielten, entspricht `wc -l` der Anzahl der Vorkommen des Namens jedes Mädchens.

> ## Warum sind die Variablen hier in doppelten Anführungszeichen?
>
> a) In [Folge 4]({{ page.root }}{% link _episodes/04-loops.md %}) haben wir gelernt, dass
> "$..."` als Schutz gegen die Fehlinterpretation von Leerzeichen zu verwenden.
> Warum _könnten_ wir die `"`-Anführungszeichen im obigen Beispiel weglassen?
> 
> b) Was passiert, wenn du "Louisa May Alcott" in die erste Zeile der Schleife einfügst
> der Schleife hinzufügst und das "`"` aus "$name" im Code der Schleife entfernst?
> 
>> ## Lösungen
>> 
>> a) Weil wir explizit die Namen nach `in` auflisten,
>> und diese keine Leerzeichen enthalten. Allerdings ist es für die Konsistenz
>> ist es besser, lieber einmal zu oft als einmal zu selten zu verwenden.
>> 
>> b) Ohne die Anführung von `$name` wird die letzte Schleife versuchen
>> `grep Louisa May Alcott littlewomen.txt`. `grep` interpretiert nur das
>> erste Wort als Suchmuster, aber `May` und `Alcott` als Dateinamen.
>> Das führt zu zwei Fehlern und einer möglicherweise nicht vertrauenswürdigen Anzahl:
>> ~~~
>> ...
>> Louisa May Alcott
>> grep: May: No such file or directory
>> grep: Alcott: No such file or directory
>> 4
>> ~~~
>>
> 


> ## Auswählen von Spalten aus unserem Artikeldatensatz
> Wenn du Daten erhältst, enthalten sie oft mehr Spalten oder Variablen, als du für deine Arbeit brauchst. Wenn du nur die Spalten auswählen willst, die du für deine Analyse brauchst, kannst du den Befehl `cut` verwenden. Mit dem Befehl "cut" kannst du Abschnitte aus einer Datei extrahieren. Nehmen wir zum Beispiel an, dass wir nur die Spalten "creator", "volume", "jornal" und "Citation" aus unseren Artikeldaten behalten wollen. Mit "cut" würden wir das tun:
>~~~
> cut -f 2,4,5,8 2014-01_JA.tsv | head
>~~~
>
>
>~~~
> Ersteller Band Journal Citation
> Doolittle, W. E. 59 KIVA -ARIZONA- KIVA -ARIZONA- 59(1), 7-26. (1993)
> Nelson, M. C. 59 KIVA -ARIZONA- KIVA -ARIZONA- 59(1), 27-48. (1993)
> Deegan, A. C. 59 KIVA -ARIZONA- KIVA -ARIZONA- 59(1), 49-64. (1993)
> Stone, T. 59 KIVA -ARIZONA- KIVA -ARIZONA- 59(1), 65-82. (1993)
> Adams, W. Y. 1 NORTHEAST AFRICAN STUDIES NORTHEAST AFRICAN STUDIES 1(2/3), 7-18. (1994)
> Beswick, S. F. 1 NORTHEAST AFRICAN STUDIES NORTHEAST AFRICAN STUDIES 1(2/3), 19-48. (1994)
> Cheeseboro, A. Q. 1 NORTHEAST AFRICAN STUDIES NORTHEAST AFRICAN STUDIES 1(2/3), 49-74. (1994)
> Duany, W. 1 NORTHEAST AFRICAN STUDIES NORTHEAST AFRICAN STUDIES 1(2/3), 75-102. (1994)
> Mohamed Ibrahim Khalil 1 NORTHEAST AFRICAN STUDIES NORTHEAST AFRICAN STUDIES 1(2/3), 103-118. (1994)
>~~~
>
>
> Oben haben wir `cut` und das Flag `-f` benutzt, um anzugeben, welche Spalten wir behalten wollen. Standardmäßig funktioniert "cut" bei tabulatorgetrennten Dateien. Mit dem Flag `-d` können wir dies in ein Komma, ein Semikolon oder ein anderes Trennzeichen ändern.
> Wenn du dir über die Position deiner Spalten nicht sicher bist und die Datei Kopfzeilen in der ersten Zeile hat, können wir diese mit `head -n 1 <Dateiname>` ausgeben.

> ### Jetzt bist du dran
>Wähle die Spalten `Issue`, `Volume`, `Language`, `Publisher` und leite die Ausgabe in eine neue Datei. Du kannst sie z.B. `2014-01_JA_ivlp.tsv` nennen.
>> ## Lösung
>> Schauen wir zuerst, wo unsere gewünschten Spalten sind:
>>
>>~~~
>> head -n 1 2014-01_JA.tsv
>>~~~
>>
>>
>>~~~
>>File Creator Issue Volume Journal ISSN ID Citation Title Place Labe Language Publisher Date
>>~~~
>>
>>
>>Ok, jetzt wissen wir, dass `Creator` Spalte 3, `Band` 4, `Sprache` 11 und `Verlag` 12 ist.
>> Wir benutzen diese Spaltennummern, um unseren `cut`-Befehl zu konstruieren:
>>```
>> cut -f 3,4,11,12 2014-01_JA.tsv > 2014-01_JA_ivlp.tsv
>>```
>> Wir können bestätigen, dass dies funktioniert hat, indem wir head auf die Datei anwenden:
>>```
>>head 2014-01_JA_ivlp.tsv
>>```
>>~~~
>>Ausgabe Band Sprache Herausgeber
>>1 59 eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY
>>1 59 eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY (ARCHÄOLOGISCHE UND HISTORISCHE GESELLSCHAFT)
>>1 59 eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY (ARCHÄOLOGISCHE UND HISTORISCHE GESELLSCHAFT)
>>1 59 eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY (ARCHÄOLOGISCHE UND HISTORISCHE GESELLSCHAFT)
>>~~~
>>
> 

