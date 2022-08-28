---
Titel: "Arbeiten mit Dateien und Verzeichnissen".
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich Dateien und Verzeichnisse kopieren, verschieben und löschen?
- "Wie kann ich Dateien lesen?"
Ziele:
- "Mit Dateien und Verzeichnissen von der Kommandozeile aus arbeiten".
- "Tabulatorvervollständigung verwenden, um die Eingabe einzuschränken".
- "Betrachten Sie eine Datei ganz oder teilweise über die Befehlszeile"
- "Verschieben und Kopieren von Dateien".
Schlüsselpunkte:
- "Die Shell kann zum Kopieren, Verschieben und Kombinieren mehrerer Dateien verwendet werden".
---
## Arbeiten mit Dateien und Ordnern

Wir können nicht nur in Verzeichnissen navigieren, sondern auch mit Dateien auf der Kommandozeile interagieren:
Wir können sie lesen, öffnen, ausführen und sogar bearbeiten.

Wir werden ein paar grundlegende Möglichkeiten zur Interaktion mit Dateien ausprobieren. Gehen wir zunächst in die
`shell-lesson'-Verzeichnis auf Ihrem Desktop.

~~~
$ cd
$ cd Desktop/shell-lesson
$ pwd
~~~

~~~
/Users/riley/Desktop/shell-lesson
~~~


Hier werden wir ein neues Verzeichnis erstellen und in dieses wechseln:

~~~
$ mkdir firstdir
$ ls
$ cd firstdir
~~~

Hier haben wir den Befehl `mkdir` (bedeutet 'make directory') benutzt, um ein Verzeichnis
genannt 'firstdir'. Dann sind wir mit dem `cd'-Befehl in dieses Verzeichnis umgezogen.

Aber warte! Es gibt einen Trick, um die Dinge etwas schneller zu machen. Lasst uns ein Verzeichnis nach oben gehen.

~~~
$ cd ..
~~~

Eine wichtige Sache ist: "Faulheit ist eine Tugend". Es ist gut faul zu sein, damit effizienter und eleganter arbeiten können.
Also anstatt `cd firstdir` einzugeben, sollten wir versuchen, `cd f` einzugeben und dann die Tabulator-Taste zu drücken.
Wir stellen fest, dass die Shell die Zeile zu `cd firstdir/` vervollständigt.

Das können wir immer anwenden, auch wenn wir uns im Homeverzeichnis befinden, mit cd D Tab Tab

### Lesen von Dateien

Wenn wir uns im `firstdir` befinden, benutzen wir `cd ..`, um zurück zum Verzeichnis `shell-lesson` zu gelangen.

Jetzt wollen wir uns die Dateien in shell-lesson genauer anschauen. Dazu benutzen wir wieder ls -lh.

~~~
$ ls -lh
~~~

~~~
total 33M
-rw-rw-r-- 1 riley staff 383K Feb 22 2017  201403160_01_text.json
-rw-r--r-- 1 riley staff 3.6M Jan 31 2017  2014-01-31_JA-africa.tsv
-rw-r--r-- 1 riley staff 7.4M Jan 31 2017  2014-01-31_JA-america.tsv
-rw-rw-r-- 1 riley staff 125M Jun 10 2015  2014-01_JA.tsv
-rw-r--r-- 1 riley staff 1.4M Jan 31 2017  2014-02-02_JA-britain.tsv
-rw-r--r-- 1 riley staff 582K Feb  2 2017  33504-0.txt
-rw-r--r-- 1 riley staff 598K Jan 31 2017  829-0.txt
-rw-rw-r-- 1 riley staff  18K Feb 22 2017  diary.html
drwxr-xr-x 1 riley staff  64B Feb 22 2017  firstdir
~~~


Wir sehen hier eine json Datei, tsv Dateien (tab seperated values), Text-Dateien, eine html Datei.
Unter der Haube sind all diese Dateien Plaintext Dateien, was uns den Vorteil verschafft, dass wir alle
in der Shell mit dem gleichen Tool öffnen können. Eine Word oder PDF Datei wäre keine solche klassische Plaintext Datei

Schauen wir uns eine solche Datei mal an, mit dem Befehl cat (steht für catenate)

~~~
$ cat 829-0.txt
~~~


Jetzt wurde uns jede Menge Text um die Ohren gehauen und so richtig hat uns das nicht geholfen.

Häufig möchten wir nur einen kurzen Blick auf den ersten oder letzten Teil einer Datei werfen, um
eine Vorstellung davon zu bekommen, worum es in der Datei geht. Um uns das zu ermöglichen, gibt es 
die Befehle `head` und `tail`.

~~~
$ head 829-0.txt
~~~

~~~
The Project Gutenberg eBook, Gulliver's Travels, by Jonathan Swift


This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org
~~~


Dies gibt einen Überblick über die ersten zehn Zeilen,
während `tail 829-0.txt` eine Perspektive auf die letzten zehn Zeilen bietet:

~~~
$ tail 829-0.txt
~~~

~~~
Most people start at our Web site which has the main PG search facility:

    http://www.gutenberg.org

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
~~~


Wenn zehn Zeilen nicht ausreichen (oder zu viel), würden wir `head -n 20` eingeben.

## Wiederverwendung von Befehlen

Drücken wir in einer leeren Eingabeaufforderung die Pfeiltaste nach oben erscheint der vorherige Befehl. Wir können die Taste
mehrmals drücken, um durch Ihre vorherigen Befehle zu blättern. Der Pfeil nach unten schaltet zurück
auf Ihr jüngstes Kommando zu. Dies ist eine weitere wichtige arbeitssparende
Funktion und etwas, das wir viel nutzen werden.

Drücke den Pfeil nach oben, bis du zum Befehl `head 829-0.txt` gelangst. Ein Leerzeichen hinzufügen
und dann `33504-0.txt` (Erinnern Sie sich an Ihren Freund Tab? Gebe `3` gefolgt von Tab ein, um den folgenden Befehl zu erzeugen:

~~~
$ head 829-0.txt 33504-0.txt
~~~

~~~
==> 829-0.txt <==
The Project Gutenberg eBook, Gulliver's Travels, by Jonathan Swift


This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


==> 33504-0.txt <==
The Project Gutenberg EBook of Opticks, by Isaac Newton

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: Opticks
       or, a Treatise of the Reflections, Refractions, Inflections,
~~~

## Less Befehl

Eine andere Möglichkeit, in Dateien zu navigieren, besteht darin, den Inhalt Bildschirm für Bildschirm zu betrachten.
Geben wir `less 829-0.txt` ein, um den ersten Bildschirm zu sehen, `spacebar`, um die
nächster Bildschirm und so weiter, dann `q` zum Beenden (Rückkehr zur Eingabeaufforderung).

~~~
$ less 829-0.txt
~~~

Wie viele andere Shell-Befehle können auch die Befehle `cat`, `head`, `tail` und `less`
eine beliebige Anzahl von Argumenten annehmen (sie können mit einer beliebigen Anzahl von Dateien arbeiten).
Wir werden sehen, wie wir die ersten Zeilen mehrerer Dateien auf einmal erhalten können.
Um uns das Tippen zu ersparen, führen wir zunächst einen sehr nützlichen Trick ein.

> ## Befehle wiederverwenden
> Bei einer leeren Eingabeaufforderung drückst du die Pfeiltaste nach oben und bemerkst, dass der vorherige
> Befehl, den du eingegeben hast, vor deinem Cursor erscheint. Wir können weiterhin die
> Pfeil nach oben drücken, um durch deine vorherigen Befehle zu gehen. Der Pfeil nach unten führt zurück
> zu deinem letzten Befehl. Das ist eine weitere wichtige arbeitssparende
> Funktion, die wir oft benutzen werden.


Drücke den Pfeil nach oben, bis du zu dem Befehl "head 829-0.txt" gelangst. Füge ein Leerzeichen
und dann `33504-0.txt` (Erinnerst du dich an deinen Freund Tab? Tippe `3` gefolgt von Tab, um
um `33504-0.txt` zu erhalten), um den folgenden Befehl zu erhalten:

~~~
$ head 829-0.txt 33504-0.txt
~~~

Soweit alles gut, aber wenn wir *viele* Bücher hätten, wäre es mühsam, alle Dateinamen einzugeben.
alle Dateinamen einzugeben. Zum Glück unterstützt die Shell Wildcards! Das `?` (entspricht genau
ein Zeichen) und `*` (passt auf null oder mehr Zeichen) kennst du wahrscheinlich
von Suchsystemen für Bibliotheken. Wir können den Platzhalter `*` verwenden, um den obigen `head`
Befehl kompakter zu schreiben:

~~~
$ head *.txt
~~~

> ## Mehr über Wildcards
> Wildcards sind eine Funktion der Shell und funktionieren daher mit *jedem* Befehl.
> Die Shell expandiert Wildcards zu einer Liste von Dateien und/oder Verzeichnissen, bevor
> bevor der Befehl ausgeführt wird, und der Befehl sieht die Wildcards nie.
> Wenn ein Platzhalterausdruck nicht auf eine Datei passt, gibt die Bash den Ausdruck als Parameter weiter.
> den Ausdruck als Parameter an den Befehl weiter, wie er ist. Zum Beispiel
> Die Eingabe von `ls *.pdf` führt zu einer Fehlermeldung, dass es keine Datei namens *.pdf gibt.

### Verschieben, Kopieren und Löschen von Dateien

Für unsere Dateien wollen auch immer gute Namen. Und apropos gute Namen. Das Datum in dieser Form ist ein guter Name.
Diese Schreibweise ist der ISO 8601. https://xkcd.com/1179/
Einer enormer Vorteil ist, dass die Dateien hierbei automatisch chronologisch sortiert werden (ls -1).

Zurück zum guten Dateiennamen: Möglicherweise möchten wir auch den Dateinamen in etwas Beschreibenderes ändern.
Wir können ihn mit dem Befehl `mv` oder move auf einen neuen Namen **verschieben**,
mit dem alten Namen als erstes Argument und dem neuen Namen als zweites
Argument:

~~~
$ mv 829-0.txt gulliver.txt
~~~

Dies entspricht der Funktion 'Datei umbenennen'.

Wenn wir danach einen `ls'-Befehl ausführen, werden wir sehen, dass er jetzt `gulliver.txt` heißt:

~~~
$ ls
~~~

~~~
2014-01-31_JA-africa.tsv   2014-02-02_JA-britain.tsv  gulliver.txt
2014-01-31_JA-america.tsv  33504-0.txt
2014-01_JA.tsv
~~~


## Challenge: Kopieren einer Datei

Ganz ähnlich verhält es sich mit dem Befehl cp. Damit können Dateien kopiert werden.
Genau wie der Befehl `mv` benötigt der Befehl `cp` zwei Argumente: den alten Namen
und den neuen Namen. Wie würden Sie eine Kopie der Datei `gulliver.txt` namens
`gulliver-backup.txt`?
> Antwort
> ~~~
> cp gulliver.txt gulliver-backup.txt
> ~~~



## Challenge: Umbenennen eines Verzeichnisses

Das Umbenennen eines Verzeichnisses funktioniert auf die gleiche Weise wie das Umbenennen einer Datei. Versuche es mit dem
`mv` Befehl, um das Verzeichnis `firstdir` in `backup` umzubenennen.
> Antwort
> ~~~
> mv firstdir backup
> ~~~


## Verschieben einer Datei in ein Verzeichnis

Mit mv können Dateien nicht nur umbenannt sondern auch bewegt werden (move).

Wenn das letzte Argument, das Sie dem Befehl `mv` geben, ein Verzeichnis und keine Datei ist,
wird die im ersten Argument angegebene Datei in dieses Verzeichnis verschoben. Versuchen wir
unter Verwendung des Befehls `mv`, um die Datei `gulliver-backup.txt` in die
Ordner `backup`.

~~~
mv gulliver-backup.txt backup
~~~



## Verwendung von `history`
Mit dem Befehl "history" kannst du dir eine Liste aller Befehle anzeigen lassen, die du während der > aktuellen Sitzung eingegeben hast. 
> aktuellen Sitzung eingegeben hast. Du kannst auch <kbd>Strg</kbd> + <kbd>r</kbd> verwenden, um eine Rückwärtssuche durchzuführen. Drücke <kbd>Strg</kbd> + <kbd>r</kbd>, 
> und beginne dann, einen beliebigen Teil des gesuchten Befehls einzutippen. Der letzte Befehl wird 
> automatisch vervollständigt. Drücke "Enter", um den Befehl erneut auszuführen, oder drücke die Pfeiltasten, um den Befehl zu > bearbeiten. 
> Bearbeiten des Befehls. Wenn mehrere vergangene Befehle den von dir eingegebenen Text enthalten, kannst du 
> <kbd>Strg</kbd> + <kbd>r</kbd> wiederholt drücken, um sie zu durchlaufen. Wenn du in der Rückwärtssuche nicht findest, wonach du suchst 
> in der Rückwärtssuche nicht findest, benutze <kbd>Strg</kbd> + <kbd>c</kbd>, um zur Eingabeaufforderung zurückzukehren. Wenn du den Verlauf speichern willst 
> deinen Verlauf speichern willst, um vielleicht einige Befehle zu extrahieren, aus denen du später ein Skript bauen kannst, kannst du 
> kannst du das mit `history > history.txt` tun. Dies gibt den gesamten Verlauf in eine Textdatei 
> namens "history.txt", die du später bearbeiten kannst. Um einen Befehl aus der History aufzurufen, gibst du 
> `History` ein. Notiere die Befehlsnummer, z.B. 2045. Rufe den Befehl auf, indem du 
> `!2045`. Dadurch wird der Befehl ausgeführt.

> ## Challenge: Verwenden des Befehls "echo
> Der Befehl "echo" gibt einfach einen Text aus, den du angibst. Probiere es aus: `echo 'Library Carpentry is awesome!'`.
> Interessant, nicht wahr?
>
> Du kannst auch eine Variable angeben. Tippe zuerst `NAME=`, gefolgt von deinem Namen, und drücke die Eingabetaste.
> Gib dann `echo "$NAME ist ein fantastischer Bibliotheksschüler"` ein und drücke die Eingabetaste. Was passiert?
>
> Du kannst sowohl Text- als auch normale Shell-Befehle mit `echo` kombinieren, zum Beispiel den
> `pwd`-Befehl, den du heute schon gelernt hast. Das machst du, indem du einen Shell
> Befehl in `$(` und `)` einschließt, zum Beispiel `$(pwd)`. Probiere nun Folgendes aus:
> `echo "Endlich ist es schön und sonnig am" $(Datum)`.
> Beachte, dass die Ausgabe des Befehls `date` zusammen mit dem Text
> den du angegeben hast. Das Gleiche kannst du mit einigen anderen Befehlen ausprobieren, die du bisher gelernt hast.
>
> **Warum denkst du, dass der echo-Befehl in der Shell-Umgebung eigentlich so wichtig ist?**
>
> > ## Antwort
> > Du denkst vielleicht, dass ein so einfacher Befehl wie `echo` nicht viel wert ist. Aber von dem Moment an, in dem du
> > mit dem Schreiben von automatisierten Shell-Skripten beginnst, wird er sehr nützlich. Zum Beispiel musst du oft
> > Text auf dem Bildschirm ausgeben, zum Beispiel den aktuellen Status eines Skripts.
> >
> > Außerdem hast du gerade zum ersten Mal eine Shell-Variable verwendet, mit der du Informationen temporär speichern kannst,
> > die du später wiederverwenden kannst. Das gibt dir viele Möglichkeiten, sobald du anfängst, automatisierte Skripte zu schreiben.

## Dateien löschen

Schließlich zum Löschen, der Befehl lautet `rm`, oder entfernen.

~~~
rm gulliver.txt
~~~

Diese Datei ist jetzt weg. Nicht im Papierkorb, sondern weg weg. Um hier Spiderman zu zitieren, "Aus großer Kraft, folgt große Verantwortung".
Mit Platzhaltern können wir sogar viele Dateien löschen. Und durch Hinzufügen des `-r`-Flags können wir Ordner mit ihrem gesamten Inhalt löschen.

~~~
rm -r backup
~~~


Wenn wir etwas vorsichtiger sein wollen können die das Argument "-i" benutzen. Dann werden wir noch einmal gefragt, ob wir die Datei wirklich löschen 
wollen und müssen dies bestätigen oder verneinen mit y oder n.

~~~
rm -i pg514.txt
~~~

