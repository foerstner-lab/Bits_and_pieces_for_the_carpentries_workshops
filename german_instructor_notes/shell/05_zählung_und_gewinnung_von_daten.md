---
Titel: "Zähleung und Gewinnung mit der Shell"
Unterricht: 60
Übungen: 30
Fragen:
- "Wie kann ich Daten zählen?"
- "Wie kann ich Daten in Dateien finden?"
- "Wie kann ich bestehende Befehle kombinieren, um neue Dinge zu tun?
Ziele:
- "Demonstration des Zählens von Zeilen, Wörtern und Zeichen mit dem Shell-Befehl wc und entsprechenden Flags".
- "Verwenden Sie Zeichenketten zum Minen von Dateien und extrahieren Sie passende Zeilen mit der Shell".
- "Erstellen Sie komplexe einzeilige Befehle, indem Sie Shell-Befehle und reguläre Ausdrücke zu Minen-Dateien kombinieren".
- "Die Ausgabe eines Befehls in eine Datei umleiten".
- "Verarbeiten Sie eine Datei anstelle von Tastatureingaben mit Umleitung."
- "Befehlspipelines mit zwei oder mehr Stufen konstruieren."
- "Erklären Sie die Unix-Philosophie der 'kleinen Stücke, lose verbunden'."
Schlüsselpunkte:
- " "Die Shell kann verwendet werden, um Elemente von Dokumenten zu zählen".
- "Die Shell kann verwendet werden, um nach Mustern innerhalb von Dateien zu suchen"
- "Mit den Befehlen kann eine beliebige Anzahl von Dateien gezählt und abgebaut werden"
- "Befehle und Flags können kombiniert werden, um komplexe Abfragen speziell für Ihre Arbeit zu erstellen".

---
## Zählung und Gewinnung von Daten

Nun, da Sie wissen, wie Sie sich in der Shell zurechtfinden, kommen wir zu
Erlernen des Zählens und Minensuchens von Daten mit einigen der Standard-Shell-Befehle.
Es ist zwar unwahrscheinlich, dass diese Befehle allein Ihre Arbeit revolutionieren werden,
sie sind sehr vielseitig und werden zu Ihrer Grundlage für die Arbeit in der Schale beitragen
und für das Erlernen des Programmierens. Die Befehle replizieren auch die Art der Verwendung, die Bibliotheksbenutzer von Bibliotheksdaten machen können.

## Zählen und Sortieren

Wir werden damit beginnen, den Inhalt von Dateien unter Verwendung der Unix-Shell zu zählen.
Wir können die Unix-Shell verwenden, um schnell Zählungen aus verschiedenen Dateien zu erzeugen,
etwas, das mit den grafischen Benutzeroberflächen von Standard-Büro-Suiten nur schwer zu erreichen ist.

Beginnen wir damit, zu dem Verzeichnis zu navigieren, das unsere Daten enthält, indem wir die
Befehl `cd`:

~~~
$ cd shell-lesson
~~~
{: .bash}

Denken Sie daran, wenn Sie sich zu irgendeinem Zeitpunkt nicht sicher sind, wo Sie sich in Ihrer Verzeichnisstruktur befinden,
benutzen Sie den Befehl `pwd`, um es herauszufinden:

~~~
$ pwd
~~~
{: .bash}
~~~
/Users/riley/Desktop/shell-lesson
~~~
{: .output}

Und lassen Sie uns einfach überprüfen, welche Dateien sich im Verzeichnis befinden und wie groß sie sind
sind mit `ls -lhS`:

~~~
$ ls -lhS
~~~
{: .bash}
~~~
total 139M
-rw-rw-r-- 1 riley staff 126M Jun 10  2015 2014-01_JA.tsv
-rw-r--r-- 1 riley staff 7.4M Jan 31 18:47 2014-01-31_JA-america.tsv
-rw-r--r-- 1 riley staff 3.6M Jan 31 18:47 2014-01-31_JA-africa.tsv
-rw-r--r-- 1 riley staff 1.4M Jan 31 18:47 2014-02-02_JA-britain.tsv
-rw-r--r-- 1 riley staff 598K Jan 31 18:47 gulliver.txt
-rw-r--r-- 1 riley staff 583K Feb  1 22:53 33504-0.txt
drwxr-xr-x 2 riley staff   68 Feb  2 00:58 backup
~~~
{: .output}

In dieser Episode werden wir uns auf den Datensatz `2014-01_JA.tsv` konzentrieren, der Folgendes enthält
die Metadaten der Zeitschriftenartikel und die drei vom Original abgeleiteten `.tsv'-Dateien
Datensatz. Jede dieser drei `.tsv'-Dateien enthält alle Daten, bei denen ein Schlüsselwort wie
als `Afrika` oder `Amerika` im Feld 'Titel' von `2014-01_JA.tsv` erscheint.

> ## CSV- und TSV-Dateien
> CSV (Comma-separated values) ist ein gebräuchliches Klartextformat zum Speichern tabellarischer
> Daten, wobei jeder Datensatz eine Zeile belegt und die Werte durch Kommata getrennt sind.
> TSV (Tab-getrennte Werte) ist genau dasselbe, außer dass die Werte durch
> Tabulatoren anstelle von Kommas. Verwirrenderweise wird manchmal CSV verwendet, um auf beide CSV zu verweisen,
> TSV und Variationen davon. Die Einfachheit der Formate macht sie großartig für
> Austausch und Archivierung. Sie sind nicht an ein bestimmtes Programm gebunden (im Gegensatz zu Excel
> Dateien, sagen wir, es gibt kein `CSV'-Programm, nur sehr, sehr viele Programme, die
> unterstützen das Format, übrigens auch Excel), und Sie hätten keine
> Probleme beim Öffnen einer 40 Jahre alten Akte, wenn Sie heute auf eine solche gestoßen sind.
{: .callout}
<!-- hm, erinnert mich an MARC -->

Werfen wir zunächst einen Blick auf die größte Datendatei, wobei wir die Werkzeuge verwenden, die wir in
Lesen von Dateien]({{{ page.root }}/03-arbeiten mit Dateien und Ordnern/#Lesen von Dateien):

~~~
$ cat 2014-01_JA.tsv
~~~
{: .bash}

Wie `829-0.txt` vorher, kaskadiert der gesamte Datensatz vorbei und kann nicht wirklich
Gefühl für diese Menge an Text. Um diese laufende Con`cat`enation, oder auch nur irgendeine
Prozess in der Unix-Shell, drücken Sie <kbd>Ctrl</kbd>+<kbd>C</kbd>.

In den meisten Datendateien sagt uns ein kurzer Blick auf die ersten paar Zeilen bereits eine Menge
über die Struktur des Datenbestands, zum Beispiel die Tabellen-/Spaltenüberschriften:

~~~
$ head -n 3 2014-01_JA.tsv
~~~
{: .bash}
~~~
File    Creator    Issue    Volume    Journal    ISSN    ID    Citation    Title    Place    Labe    Language    Publisher    Date
History_1a-rdf.tsv  Doolittle, W. E.  1 59  KIVA -ARIZONA-  0023-1940 (Uk)RN001571862 KIVA -ARIZONA- 59(1), 7-26. (1993)  A Method for Distinguishing between Prehistoric and Recent Water and Soil Control Features  xxu eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY 1993
History_1a-rdf.tsv  Nelson, M. C. 1 59  KIVA -ARIZONA-  0023-1940 (Uk)RN001571874 KIVA -ARIZONA- 59(1), 27-48. (1993) Classic Mimbres Land Use in the Eastern Mimbres Region, Southwestern New Mexico xxu eng ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY 1993

~~~
{: .output}

In der Kopfzeile sehen wir die gemeinsamen Metadatenfelder von wissenschaftlichen Arbeiten: `Schöpfer`, `Thema`, `Zitat`, etc.

Als nächstes lernen wir ein grundlegendes Werkzeug zur Datenanalyse kennen:
`wc` ist der Befehl "word count": er zählt die Anzahl der Zeilen, Wörter und Bytes.
Da wir den Wildcard-Operator lieben, lassen Sie uns den Befehl
`wc *.tsv`, um Zählwerte für alle `.tsv'-Dateien im aktuellen Verzeichnis zu erhalten
(es braucht ein wenig Zeit zum Ausfüllen):

~~~~
$ wc *.tsv
~~~~
{: .bash}
~~~
    13712    511261   3773660 2014-01-31_JA-africa.tsv
    27392   1049601   7731914 2014-01-31_JA-america.tsv
   507732  17606310 131122144 2014-01_JA.tsv
     5375    196999   1453418 2014-02-02_JA-britain.tsv
   554211  19364171 144081136 total
~~~
{: .output}

Die ersten drei Spalten enthalten die Anzahl der Zeilen, Wörter und Bytes.

Wenn wir nur eine Handvoll Dateien zum Vergleichen haben, könnte es schneller oder bequemer sein
um einfach mit Microsoft Excel, OpenRefine oder Ihrem bevorzugten Texteditor zu prüfen, aber
Wenn wir Dutzende, Hunderte oder Tausende von Dokumenten haben, hat die Unix-Shell eine klare
Geschwindigkeitsvorteil. Die wahre Stärke der Shell liegt in der Fähigkeit, Befehle zu kombinieren
und Aufgaben zu automatisieren. Wir werden dies ein wenig berühren.

Vorerst werden wir sehen, wie wir eine einfache Pipeline aufbauen können, um die kürzeste Datei zu finden
in Bezug auf die Anzahl der Zeilen. Wir beginnen mit dem Hinzufügen der Flagge `-l`, um nur die
Anzahl der Zeilen, nicht die Anzahl der Wörter und Bytes:

~~~~
$ wc -l *.tsv
~~~~
{: .bash}
~~~
    13712 2014-01-31_JA-africa.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
     5375 2014-02-02_JA-britain.tsv
   554211 total
~~~
{: .output}

Der Befehl `wc` selbst hat kein Flag, um die Ausgabe zu sortieren, aber da wir
Sehen Sie, wir können drei verschiedene Shell-Befehle kombinieren, um das zu bekommen, was wir wollen.

Als erstes haben wir den Befehl `wc -l *.tsv`. Wir speichern die Ausgabe von diesem
Befehl in einer neuen Datei. Um das zu tun, *umleiten* wir die Ausgabe des Befehls
in eine Datei mit dem "Größer als"-Zeichen (>), wie so:

~~~
$ wc -l *.tsv > lengths.txt
~~~
{: .bash}

Es gibt jetzt keine Ausgabe mehr, da die Ausgabe in die Datei `lengths.txt` ging, aber
können wir überprüfen, ob die Ausgabe tatsächlich in der Datei gelandet ist, indem wir `cat` oder `less` verwenden
(oder Notepad oder einem beliebigen Texteditor).

~~~~
$ cat lengths.txt
~~~~
{: .bash}
~~~
    13712 2014-01-31_JA-africa.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
     5375 2014-02-02_JA-britain.tsv
   554211 total
~~~
{: .bash}

Als nächstes gibt es den Befehl `sortieren`. Wir werden das `-n` Flag benutzen, um festzulegen, dass wir
numerische, nicht lexikalische Sortierung wünschen, geben wir die Ergebnisse aus in
noch eine weitere Datei, und wir benutzen `cat`, um die Ergebnisse zu überprüfen:

~~~~
$ sort -n lengths.txt > sorted-lengths.txt
$ cat sorted-lengths.txt
~~~~
{: .bash}
~~~
     5375 2014-02-02_JA-britain.tsv
    13712 2014-01-31_JA-africa.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
   554211 total
~~~
{: .output}

Endlich haben wir unseren alten Freund `Kopf`, den wir benutzen können, um die erste Zeile zu bekommen
der `sorted-lengths.txt`:

~~~~
$ head -n 1 sorted-lengths.txt
~~~~
{: .bash}
~~~
     5375 2014-02-02_JA-britain.tsv
~~~
{: .output}

Aber wir sind wirklich nur am Endergebnis interessiert, nicht am Zwischenergebnis.
Ergebnisse werden jetzt in `lengths.txt` und `sortred-lengths.txt` gespeichert. Was wäre, wenn wir
die Ergebnisse aus dem ersten Befehl (`wc -l *.tsv`) direkt an den nächsten senden
Befehl (`sortieren -n`) und dann die Ausgabe dieses Befehls an `Kopf -n 1`?
Glücklicherweise können wir ein Konzept namens pipes verwenden. Auf der Kommandozeile machen Sie einen
Pfeife mit dem vertikalen Strichzeichen `|`. Versuchen wir es zuerst mit einer Pipe:

~~~~
$ wc -l *.tsv | sort -n
~~~~
{: .bash}
~~~
     5375 2014-02-02_JA-britain.tsv
    13712 2014-01-31_JA-africa.tsv
    27392 2014-01-31_JA-america.tsv
   507732 2014-01_JA.tsv
   554211 total
~~~
{: .output}

Beachten Sie, dass dies genau die gleiche Ausgabe ist, die in unserer `sorted-lengths.txt` gelandet ist.
früher. Lassen Sie uns eine weitere Pfeife hinzufügen:

~~~~
$ wc -l *.tsv | sort -n | head -n 1
~~~~
{: .bash}
~~~
     5375 2014-02-02_JA-britain.tsv
~~~
{: .output}

Es kann einige Zeit dauern, Rohre vollständig zu erfassen und effizient zu nutzen, aber es ist ein
sehr mächtiges Konzept, das Sie nicht nur in der Schale, sondern auch in den meisten
Programmiersprachen.

![Redirects and Pipes](../fig/redirects-and-pipes.png)

> ## Rohre und Filter
> Diese einfache Idee ist der Grund, warum Unix so erfolgreich ist. Anstatt enorme
> Programme, die versuchen, viele verschiedene Dinge zu tun, konzentrieren sich Unix-Programmierer auf das Erstellen
> viele einfache Werkzeuge, die jeweils eine Aufgabe gut erledigen und die gut miteinander funktionieren.
> Dieses Programmiermodell wird "Pipes und Filter" genannt. Wir haben bereits Pipes gesehen; ein
> Filter ist ein Programm wie `wc` oder `sort`, das einen Eingabestrom in einen
> Strom der Ausgabe. Fast alle Standard-Unix-Werkzeuge können auf diese Weise arbeiten: es sei denn
> aufgefordert, etwas anderes zu tun, sie lesen aus Standardinputs, machen etwas mit dem, was sie
> lesen und in die Standardausgabe schreiben.
>
> Der Schlüssel ist, dass jedes Programm, das Textzeilen aus der Standardeingabe liest und schreibt
> Textzeilen zur Standardausgabe können mit jedem anderen Programm kombiniert werden, das
> verhält sich auch auf diese Weise. Sie können und sollten Ihre Programme auf diese Weise schreiben, damit
> können Sie und andere Leute diese Programme in Pipes stecken, um ihre Macht zu vervielfachen.
{: .callout}
<!-- Copied from https://swcarpentry.github.io/shell-novice/04-pipefilter/ -->

## Hinzufügen einer weiteren Pipe
> Wir haben unsere `wc -l *.tsv | sort -n | head -n 1` Pipeline. Was würde passieren
> wenn Sie das in "Katze" übertragen würden? Versuchen Sie es!
>
> > ## Lösung
> > Der Befehl `cat` gibt einfach aus, was immer er als Eingabe erhält, also erhalten Sie genau
> > die gleiche Ausgabe von
> >
> > ~~~
> > $ wc -l *.tsv | sort -n | head -n 1
> > ~~~
> > {: .bash}
> >
> > and
> >
> > ~~~
> > $ wc -l *.tsv | sort -n | head -n 1 | cat
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Zählen, sortieren und drucken (verblasstes Beispiel)
>Um die Gesamtzeilen in jeder `tsv`-Datei zu zählen, die Ergebnisse zu sortieren und dann die erste Zeile der Datei auszudrucken, verwenden wir folgendes:
>
>~~~
>wc -l *.tsv | sort -n | head -n 1
>~~~
>{: .bash}
>
>
>Nun wollen wir das Szenario ändern. Wir wollen die 10 Dateien wissen, die _die meisten_ Wörter enthalten. Füllen Sie die Leerzeichen unten aus, um die Wörter für jede Datei zu zählen, ordnen Sie sie in eine Reihenfolge und erstellen Sie dann eine Ausgabe der 10 Dateien mit den meisten Wörtern (Hinweis: Der Sortierbefehl sortiert standardmäßig in aufsteigender Reihenfolge).
>
>~~~
>__ -w *.tsv | sort __ | ____
>~~~
>{: .bash}
>
> > ## Lösung
> >
> > Hier verwenden wir den Befehl `wc` mit dem Flag `-w` (word) auf allen `tsv`-Dateien, `sortieren` sie und geben dann die letzten 11 Zeilen (10 Dateien und die Gesamtsumme) mit dem Befehl `tail` aus.
> >~~~
> > wc -w *.tsv | sort -n | tail -n 11
> >~~~
> {: .solution}
>{: .bash}
{: .challenge}


> ## Zählen der Anzahl der Dateien, Teil I
> Lasst uns eine andere Pipeline machen. Sie wollen herausfinden, wie viele Dateien und
> Verzeichnisse, die sich im aktuellen Verzeichnis befinden. Versuchen Sie, ob Sie
> die Ausgabe von `ls` in `wc`, um die Antwort zu finden, oder etwas in der Nähe der
> Antwort.
>
> > ## Lösung
> > Sie nähern sich mit
> >
> > ~~~
> > $ ls -l | wc -l
> > ~~~~
> > {: .bash}
> >
> > aber die Zahl wird um eins zu hoch sein, da die "Gesamt"-Zeile aus `ls`
> > wird in die Zählung einbezogen. Wir werden später auf eine Möglichkeit zurückkommen, das zu beheben.
> > wenn wir von dem `Grep`-Kommando erfahren haben.
> {: .solution}
{: .challenge}

> ## Schreiben in Dateien
> Der Befehl `date` gibt das aktuelle Datum und die Uhrzeit aus. Können Sie den Befehl
> aktuelles Datum und Uhrzeit in eine neue Datei namens `logfile.txt`? Prüfen Sie dann
> den Inhalt der Datei.
>
> > ## Lösung
> > ~~~
> > $ date > logfile.txt
> > $ cat logfile.txt
> > ~~~~
> > {: .bash}
> > Um den Inhalt zu überprüfen, könnten Sie auch `less` oder viele andere Befehle verwenden.
> >
> > Vorsicht, dass `>` eine bestehende Datei ohne Vorwarnung gerne überschreibt,
> > also seien Sie bitte vorsichtig.
> {: .solution}
{: .challenge}

> ## An eine Datei anhängen
Während `>>" in eine Datei schreibt, hängt `>>" etwas an eine Datei an. Versuchen Sie, die
> aktuelles Datum und Uhrzeit in die Datei `logfile.txt`?
>
> > ## Lösung
> > ~~~
> > $ date >> logfile.txt
> > $ cat logfile.txt
> > ~~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Zählen der Anzahl der Wörter
>
> Suchen Sie im Handbuch nach dem Befehl `wc` (entweder mit `man wc` oder `wc --help`)
> um zu sehen, ob Sie herausfinden können, welche Flagge Sie zum Ausdrucken der Wortanzahl verwenden können
> (aber nicht die Anzahl der Zeilen und Bytes). Versuchen Sie es mit den `.tsv'-Dateien.
>
> Wenn Sie Zeit haben, können Sie auch versuchen, die Ergebnisse zu sortieren, indem Sie sie per Pipeline `sortieren`.
> Und/oder erkunden Sie die anderen Flaggen von `wc`.
>
> > ## Lösung
> >
> > Von `man wc` aus werden Sie sehen, dass es eine `-w` Flagge gibt, um die Anzahl von
> > Wörter:
> >
> > ~~~
> > -w Die Anzahl der Wörter in jeder Eingabedatei wird in den Standard geschrieben
> > Ausgabe.
> > ~~~
> > {: .output}
> >
> > So drucken Sie die Wortzahlen der `.tsv'-Dateien aus:
> >
> > ~~~
> > $ wc -w *.tsv
> > ~~~
> > {: .bash}
> > ~~~
> >   511261 2014-01-31_JA-africa.tsv
> >  1049601 2014-01-31_JA-america.tsv
> > 17606310 2014-01_JA.tsv
> >   196999 2014-02-02_JA-britain.tsv
> > 19364171 total
> > ~~~
> > {: .output}
> >
> > Und um die Zeilen numerisch zu sortieren:
> >
> > ~~~
> > $ wc -w *.tsv | sort -n
> > ~~~
> > {: .bash}
> > ~~~
> >   196999 2014-02-02_JA-britain.tsv
> >   511261 2014-01-31_JA-africa.tsv
> >  1049601 2014-01-31_JA-america.tsv
> > 17606310 2014-01_JA.tsv
> > 19364171 total
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

## Bergbau oder Suche

Die Suche nach etwas in einer oder mehreren Dateien ist etwas, das wir oft tun müssen,
also lassen Sie uns einen Befehl dafür einführen: `grep` (kurz für **global regular
Ausdruck drucken**). Wie der Name schon sagt, unterstützt es reguläre Ausdrücke und
ist daher nur begrenzt durch Ihre Vorstellungskraft, die Form Ihrer Daten und - wenn
bei der Arbeit mit Tausenden oder Millionen von Dateien - die Rechenleistung, die Ihnen zur Verfügung steht.

Um mit der Benutzung von `grep` zu beginnen, navigieren Sie zunächst zum Verzeichnis `shell-lesson`, falls noch nicht geschehen
dort. Erstellen Sie dann ein neues Verzeichnis "results":

~~~
$ mkdir results
~~~
{: .bash}


Nun wollen wir unsere erste Suche versuchen:

~~~
$ grep 1999 *.tsv
~~~
{: .bash}

Denken Sie daran, dass die Shell `*.tsv` zu einer Liste aller `.tsv'-Dateien in der
Verzeichnis. `grep` wird diese dann nach Instanzen der Zeichenkette "1999" durchsuchen und
die übereinstimmenden Zeilen drucken.

> ## Zeichenketten
> Eine Zeichenfolge ist eine Folge von Zeichen oder "ein Stück Text".
{: .callout}

Drücken Sie einmal auf den Pfeil nach oben, um zu Ihrer letzten Aktion zurückzukehren.
Ändern Sie `grep 1999 *.tsv` in `grep -c 1999 *.tsv` und drücken Sie Enter.

~~~
$ grep -c 1999 *.tsv
~~~
{: .bash}
~~~
2014-01-31_JA-africa.tsv:804
2014-01-31_JA-america.tsv:1478
2014-01_JA.tsv:28767
2014-02-02_JA-britain.tsv:284
~~~
{: .output}

Die Shell gibt nun die Anzahl der Male aus, die die Zeichenfolge 1999 in jeder Datei erschien.
Wenn Sie sich die Ausgabe des vorhergehenden Befehls ansehen, bezieht sich dies tendenziell auf die
Datumsfeld für jeden Zeitschriftenartikel.

Wir werden eine weitere Suche versuchen:

~~~
$ grep -c revolution *.tsv
~~~
{: .bash}
~~~
2014-01-31_JA-africa.tsv:20
2014-01-31_JA-america.tsv:34
2014-01_JA.tsv:867
2014-02-02_JA-britain.tsv:9
~~~
{: .output}

Wir haben die Zählungen der Instanzen der Zeichenkette `Revolution` innerhalb der Dateien zurückbekommen.
Ändern Sie nun den obigen Befehl in den folgenden und beobachten Sie, wie die Ausgabe der einzelnen unterschiedlich ist:

~~~
$ grep -ci revolution *.tsv
~~~
{: .bash}
~~~
2014-01-31_JA-africa.tsv:118
2014-01-31_JA-america.tsv:1018
2014-01_JA.tsv:9327
2014-02-02_JA-britain.tsv:122
~~~
{: .output}

Dadurch wird die Abfrage wiederholt, aber ein Fall gedruckt.
unempfindliche Zählung (einschließlich der Fälle sowohl von "Revolution" als auch von "Revolution" und anderer Varianten).
Beachten Sie, wie sich die Zählung bei diesen Zeitschriftenartikeln um fast das 30-fache erhöht hat
Titel, die das Schlüsselwort 'Amerika' enthalten. Wie zuvor, Radfahren zurück und
Durch Hinzufügen von `> results/`, gefolgt von einem Dateinamen (idealerweise im .txt-Format), werden die Ergebnisse in einer Datendatei gespeichert.

Bisher haben wir Zeichenketten in Dateien gezählt und auf die Shell oder in
diese Zählungen einreichen. Aber die wahre Macht von `grep` liegt darin, dass man
verwenden Sie es auch, um Untermengen von tabellarischen Daten (oder sogar beliebige Daten) zu erstellen
aus einer oder mehreren Dateien.  

~~~
$ grep -i revolution *.tsv
~~~
{: .bash}

Dieses Skript sucht in den definierten Dateien und druckt alle Zeilen, die `Revolution` enthalten.
(ohne Rücksicht auf den Fall) auf die Schale. Wir lassen die Hülle das heutige Datum in die
Dateiname:

~~~
$ grep -i revolution *.tsv > results/$(date "+%Y-%m-%d")_JAi-revolution.tsv
~~~
{: .bash}

Dadurch werden die untergeordneten Daten in einer neuen Datei gespeichert.

> ## Alternative Datumsbefehle
> Diese Art, Daten zu schreiben, ist so verbreitet, dass auf einigen Plattformen (nicht macOS X)
> können Sie dasselbe Ergebnis erhalten, wenn Sie `$(Datum -I)` anstelle von
> `$(date "+%Y-%m-%d")`.
{: .callout}

Wenn wir uns jedoch diese Datei ansehen, enthält sie jede Instanz der
Zeichenkette 'Revolution', auch als einzelnes Wort und als Teil anderer Wörter
wie zum Beispiel "revolutionär". Das ist vielleicht nicht so nützlich, wie wir dachten...
Glücklicherweise weist die `-w"-Flagge `grep` an, nur nach ganzen Wörtern zu suchen,
was uns eine größere Präzision bei unserer Suche ermöglicht.

~~~
$ grep -iw revolution *.tsv > results/$(date "+%Y-%m-%d")_JAiw-revolution.tsv
~~~
{: .bash}

Dieses Skript sucht sowohl in den definierten Dateien als
exportiert alle Zeilen, die das ganze Wort `Revolution` enthalten (ohne Rücksicht auf den Fall)
auf die angegebene `.tsv'-Datei.

Wir können den Unterschied zwischen den von uns erstellten Dateien zeigen.

~~~
$ wc -l results/*.tsv
~~~
{: .bash}
~~~
   10585 2016-07-19_JAi-revolution.tsv
    7779 2016-07-19_JAiw-revolution.tsv
   18364 total
~~~
{: .output}

> ## Automatisches Hinzufügen eines Datumspräfix
> Beachten Sie, dass wir das heutige Datum nicht selbst eingetippt haben, sondern die
> Das Kommando `date` erledigt diese sinnlose Aufgabe für uns. Informieren Sie sich über die
> `"+%Y-%m-%d"` Option und alternative Optionen, die wir hätten nutzen können.
>
> > ## Lösung
> > Die Verwendung von `date --help` wird Ihnen zeigen, dass die Option `+` einführt
> > ein Datumsformat, wobei `%Y`, `%m` und `%d` durch die Jahreszahl ersetzt werden,
> > Monat bzw. Tag. Es gibt viele andere Prozent-Codes
> > die Sie verwenden könnten.
> >
> > Vielleicht sehen Sie auch, dass `-I` die Abkürzung für
> > [--iso-8601](https://en.wikipedia.org/wiki/ISO_8601), die
> > vermeidet im Wesentlichen die Verwirrung zwischen den europäischen
> > und den amerikanischen Datumsformaten `TT.MM.JJJJ" und `MM/TT/JJJJ".
> {: .solution}
{: .challenge}

Schließlich werden wir die **Syntax für reguläre Ausdrücke** verwenden, die bereits behandelt wurde, um nach ähnlichen Wörtern zu suchen.

> ## Einfache, erweiterte und PERL-kompatible reguläre Ausdrücke
> Es gibt leider [verschiedene Arten, reguläre Ausdrücke zu schreiben] (https://www.gnu.org/software/grep/manual/html_node/Regular-Expressions.html).
> Über seine verschiedenen Versionen hinweg unterstützt `grep` "basic", mindestens zwei Arten von "extended",
> und "PERL-kompatible" reguläre Ausdrücke. Dies ist ein häufiger Grund für Verwirrung, da
> die meisten Tutorials, einschließlich unseres, lehren reguläre Ausdrücke, die mit dem PERL kompatibel sind
> Programmiersprache, aber `grep` verwendet standardmäßig Basic.
> Sofern Sie sich nicht an die Details erinnern wollen, machen Sie sich das Leben einfach, indem Sie immer die
> die fortgeschrittensten regulären Ausdrücke, die Ihre Version von `grep` unterstützt (Flagge `-E` auf
> macOS X, `-P` auf den meisten anderen Plattformen) oder bei komplexeren Aufgaben
> als die Suche nach einer einfachen Zeichenfolge.
{: .callout}

Der reguläre Ausdruck "fr[ae]nc[eh]" wird mit "france", "french", aber auch mit "frence" und "franch" übereinstimmen.
Es ist im Allgemeinen eine gute Idee, den Ausdruck in einfache Anführungszeichen zu setzen, da
die sicherstellt, dass die Shell sie direkt an grep sendet, ohne jegliche Verarbeitung (wie z.B. der Versuch
erweitern Sie den Wildcard-Operator *).

~~~
$ grep -iwE 'fr[ae]nc[eh]' *.tsv
~~~
{: .bash}

Die Shell druckt jede übereinstimmende Zeile aus.

Wir fügen das `-o` Flag ein, um nur den passenden Teil der Zeilen auszudrucken, z.B.
(praktisch zum Isolieren/Überprüfen von Ergebnissen):

~~~
$ grep -iwEo 'fr[ae]nc[eh]' *.tsv
~~~
{: .bash}

Schließen Sie sich mit Ihrem Nachbarn zusammen und arbeiten Sie an diesen Übungen:

> ## Groß-/Kleinschreibung beachten
> Suche nach allen case sensitive Instanzen von
> ein ganzes Wort, das Sie in allen vier abgeleiteten `.tsv'-Dateien in diesem Verzeichnis auswählen.
> Drucken Sie Ihre Ergebnisse in die Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -w hero *.tsv
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Groß-/Kleinschreibung bei der Suche in ausgewählten Dateien beachten
> Suche nach allen Groß- und Kleinschreibung berücksichtigenden Instanzen eines Wortes, das Sie in
> die 'Amerika' und 'Afrika' `.tsv'-Dateien in diesem Verzeichnis.
> Drucken Sie Ihre Ergebnisse in die Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep hero *a.tsv
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Wörter zählen (Groß-/Kleinschreibung beachten)
> Zählen Sie alle case-sensitive Instanzen eines Wortes, das Sie in
> die 'Amerika' und 'Afrika' `.tsv'-Dateien in diesem Verzeichnis.
> Drucken Sie Ihre Ergebnisse in die Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -c hero *a.tsv
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Wörter zählen (Groß-/Kleinschreibung wird nicht berücksichtigt)
> Zählen Sie alle nicht auf Groß- und Kleinschreibung achtenden Fälle dieses Wortes in den `.tsv'-Dateien `Amerika' und `Afrika'
> in diesem Verzeichnis. Drucken Sie Ihre Ergebnisse in die Shell aus.
>
> > ## Lösung
> > ~~~
> > $ grep -ci hero *a.tsv
> > ~~~
> > {: .bash}
> {: .lösung}
{: .herausfordern}

> ## Groß-/Kleinschreibung bei der Suche in ausgewählten Dateien
> Suche nach allen case-insensitiven Instanzen davon
> Wort in den 'Amerika' und 'Afrika' `.tsv'-Dateien in diesem Verzeichnis. Drucken Sie Ihre Ergebnisse in eine Datei `results/hero.tsv` aus.
>
> > ## Lösung
> > ~~~
> > $ grep -i hero *a.tsv > results/hero.tsv
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Groß-/Kleinschreibung bei der Suche in ausgewählten Dateien (ganzes Wort)
> Suche nach allen case-insensitiven Instanzen dieses ganzen Wortes
> in den `.tsv'-Dateien 'Amerika' und 'Afrika' in diesem Verzeichnis. Drucken Sie Ihre Ergebnisse in eine Datei `results/hero-i.tsv` aus.
>
> > ## Lösung
> > ~~~
> > $ grep -iw hero *a.tsv > results/hero-i.tsv
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Suche mit regulären Ausdrücken
> Verwenden Sie reguläre Ausdrücke, um alle ISSN-Nummern zu finden
(vier Ziffern, gefolgt von einem Bindestrich, gefolgt von vier Ziffern) > (vier Ziffern, gefolgt von einem Bindestrich, gefolgt von vier Ziffern)
> in `2014-01_JA.tsv` und drucken Sie die Ergebnisse in eine Datei `results/issns.tsv` aus.
> Beachten Sie, dass Sie möglicherweise das Flag `-E` (oder `-P` bei einigen Versionen
> von `grep`, z.B. mit Git Bash unter Windows).
>
> > ## Lösung
> > ~~~
> > $ grep -Eo '\d{4}-\d{4}' 2014-01_JA.tsv > issns.tsv
> > ~~~
> > {: .bash}
> >
> > or
> >
> > ~~~
> > $ grep -Po '\d{4}-\d{4}' 2014-01_JA.tsv > issns.tsv
> > ~~~
> > {: .bash}
> >
> > Es lohnt sich, die Datei zu überprüfen, um sicherzustellen, dass `grep` das Muster interpretiert hat
> > richtig. Sie könnten dafür den Befehl `less` verwenden.
> >
> > Die `-o`-Flagge bedeutet, dass nur die ISSN selbst ausgedruckt wird, statt der
> > ganze Zeile.
> >
> > Wenn Ihnen etwas Fortschrittlicheres eingefallen wäre, vielleicht einschließlich Wortgrenzen,
> > bitte teilen Sie Ihr Ergebnis im gemeinsamen Dokument mit und klopfen Sie sich selbst auf die Schulter.
> >
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Eindeutige Werte finden
> Wenn Sie etwas über die Pipeline an den Befehl `uniq` übergeben, filtert er benachbarte doppelte Zeilen heraus.
> Damit der 'uniq'-Befehl jedoch nur eindeutige Werte zurückgibt, muss er verwendet werden
> mit dem Befehl 'sort'. Versuchen Sie, die Ausgabe des Befehls aus der letzten Übung
> zu `sortieren` und dann diese Ergebnisse über die Pipeline zu 'uniq' und dann `wc -l`, um die Anzahl der eindeutigen ISSN-Werte zu zählen.
>
> > ## Lösung
> > ~~~
> > $ grep -Eo '\d{4}-\d{4}' 2014-01_JA.tsv | sort | uniq | wc -l
> > ~~~
> > {: .bash}
> >
> > oder
> > ~~~
> > $ grep -Po '\d{4}-\d{4}' 2014-01_JA.tsv | sort | uniq | wc -l
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

> ## Zählen der Anzahl der Dateien, Teil II
> In der früheren Zählübung in dieser Episode haben Sie versucht, die Zahl
> von Dateien und Verzeichnissen im aktuellen Verzeichnis.
>
> * Erinnern Sie sich, dass der Befehl `ls -l | wc -l` uns ziemlich weit brachte, aber das Ergebnis war eins
> zu hoch, weil es die "Gesamt"-Zeile in die Zeilenzählung einbezogen hat.
* Können Sie mit dem Wissen von `grep` herausfinden, wie Sie die "Total"-Zeile ausschließen können?
> Zeile aus der Ausgabe `ls -l`?
> Hinweis: Sie möchten jede Zeile ausschließen, die *beginnt*.
> mit dem Text "total". Das Hat-Zeichen (^) wird verwendet
> in regulären Ausdrücken, um den Anfang einer Zeile anzugeben.
>
> > ## Lösung
> > Um alle Zeilen zu finden, die mit "total" beginnen, würden wir
> >
> > ~~~
> > $ ls -l | grep -E '^total'
> > ~~~
> > {: .bash}
> >
> > Um *diese Zeilen auszuschließen, fügen wir das `-v` Flag hinzu:
> >
> > ~~~
> > $ ls -l | grep -v -E '^total'
> > ~~~
> > {: .bash}
> >
> > Das große Finale besteht darin, dies in `wc -l` zu verwandeln:
> >
> > ~~~
> > $ ls -l | grep -v -E '^total' | wc -l
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

### Verwendung einer Schleife zum Zählen von Wörtern

Wir werden nun eine Schleife verwenden, um die Zählung bestimmter Wörter innerhalb eines Dokuments zu automatisieren. Dazu werden wir das _[Kleine Frauen](http://www.gutenberg.org/cache/epub/514/pg514.txt)_ E-Book von [Project Gutenberg](https://www.gutenberg.org/) verwenden. Die Datei befindet sich im Ordner `shell-lesson` und heißt `pg514.txt`. Benennen wir die Datei in `littlewomen.txt` um. 

~~~
$ mv pg514.txt littlewomen.txt
~~~

Dadurch wird die Datei in etwas umbenannt, das einfacher einzugeben ist.

Nun lassen Sie uns unsere Schleife erstellen. In der Schleife werden wir den Computer bitten, den Text durchzugehen und nach dem Namen jedes Mädchens zu suchen,
und zählen Sie, wie oft es erscheint. Die Ergebnisse werden auf dem Bildschirm ausgedruckt.

~~~
$ for name in "Jo" "Meg" "Beth" "Amy"
> do
>    echo "$name"
>    grep -wo "$name" littlewomen.txt | wc -l
> done
~~~

{: .bash}

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
{: .output}

Was geschieht in der Schleife?  
+ `echo "$name"` gibt den aktuellen Wert von `$name` aus
+ `grep "$name" littlewomen.txt` findet jede Zeile, die den in `$name` gespeicherten Wert enthält. Die Flagge `-w` findet nur das ganze Wort, das den in `$name` gespeicherten Wert enthält, und die Flagge `-o` holt diesen Wert aus der Zeile heraus, in der er sich befindet, um Ihnen die eigentlichen Wörter zu geben, die als Zeilen an sich zu zählen sind.
+ Die Ausgabe des Befehls `grep` wird mit der Pipe `|` umgeleitet (ohne die Pipe und den Rest der Zeile würde die Ausgabe von `grep` direkt auf den Bildschirm ausgegeben).
+ `wc -l` zählt die Anzahl der _Zeilen_ (weil wir die Flagge `-l` verwendet haben), die von `grep` gesendet wurden. Da `grep` nur Zeilen zurückgab, die den in `$name` gespeicherten Wert enthielten, entspricht `wc -l` der Anzahl der Vorkommnisse des Namens jedes Mädchens.

> ## Warum werden die Variablen hier doppelt zitiert?
>
> a) In [Episode 4]({{{{ page.root }}{% link _episodes/04-loops.md %}) haben wir gelernt
> benutze `"$..."` als Schutz vor Fehlinterpretationen des Weißraums.
> Warum _könnten_ wir die `"` -Zitate im obigen Beispiel weglassen?
> 
> b) Was passiert, wenn Sie `"Louisa May Alcott"` in die erste Zeile von
> der Schleife und entfernen Sie das `"`` von `$name` im Code der Schleife?
> 
>> ## Lösungen
>> 
>> a) Weil wir die Namen nach `in` explizit auflisten,
>> und diese enthalten keine Leerzeichen. Aus Gründen der Konsistenz
>> es ist besser, eher einmal zu oft als einmal zu selten zu verwenden.
>> 
>> b) Ohne `"`-quoting `$name` wird die letzte Schleife versuchen,
>> `grep Louisa May Alcott littlewomen.txt`. `grep` interpretiert nur die
>> erstes Wort als Suchmuster, aber `May` und `Alcott` als Dateinamen.
>> Dies führt zu zwei Fehlern und einer möglicherweise nicht vertrauenswürdigen Zählung:
>> ~~~
>> ...
>> Louisa May Alcott
>> grep: May: No such file or directory
>> grep: Alcott: No such file or directory
>> 4
>> ~~~
>> {: .bash}
> {: .solution}
{: .challenge}

> ## Auswählen von Spalten aus unserem Artikeldatensatz
> Wenn Sie Daten erhalten, werden diese oft mehr Spalten oder Variablen enthalten, als Sie für Ihre Arbeit benötigen. Wenn Sie nur die Spalten auswählen möchten, die Sie für Ihre Analyse benötigen, können Sie dazu den Befehl `cut` verwenden. `cut` ist ein Werkzeug zum Extrahieren von Abschnitten aus einer Datei. Nehmen wir zum Beispiel an, wir möchten nur die Spalten `Creator`, `Volume`, `Journal` und `Citation` aus unseren Artikeldaten beibehalten. Mit `cut` würden wir:
>~~~
> cut -f 2,4,5,8 2014-01_JA.tsv | head
>~~~
>{: .bash}
>
>~~~
> Creator	Volume	Journal	Citation
> Doolittle, W. E.  59  KIVA -ARIZONA-  KIVA -ARIZONA- 59(1), 7-26. (1993)
> Nelson, M. C.	59	KIVA -ARIZONA-	KIVA -ARIZONA- 59(1), 27-48. (1993)
> Deegan, A. C.	59	KIVA -ARIZONA-	KIVA -ARIZONA- 59(1), 49-64. (1993)
> Stone, T.	59	KIVA -ARIZONA-	KIVA -ARIZONA- 59(1), 65-82. (1993)
> Adams, W. Y.	1	NORTHEAST AFRICAN STUDIES	NORTHEAST AFRICAN STUDIES 1(2/3), 7-18. (1994)
> Beswick, S. F.	1	NORTHEAST AFRICAN STUDIES	NORTHEAST AFRICAN STUDIES 1(2/3), 19-48. (1994)
> Cheeseboro, A. Q.	1	NORTHEAST AFRICAN STUDIES	NORTHEAST AFRICAN STUDIES 1(2/3), 49-74. (1994)
> Duany, W.	1	NORTHEAST AFRICAN STUDIES	NORTHEAST AFRICAN STUDIES 1(2/3), 75-102. (1994)
> Mohamed Ibrahim Khalil	1	NORTHEAST AFRICAN STUDIES	NORTHEAST AFRICAN STUDIES 1(2/3), 103-118. (1994)
>~~~
>{: .output}
>
> Oben haben wir `cut` und die `-f` Flagge benutzt, um anzugeben, welche Spalten wir beibehalten wollen. `cut` funktioniert standardmäßig bei tabulatorgetrennten Dateien. Wir können die Flagge `-d` benutzen, um dies in ein Komma, ein Semikolon oder ein anderes Trennzeichen zu ändern.
> Wenn Sie sich über Ihre Spaltenposition unsicher sind und die Datei Überschriften in der ersten Zeile hat, können wir `head -n 1 <Dateiname>` benutzen, um diese auszudrucken.
> ### Jetzt sind Sie dran
>Wählen Sie die Spalten `Issue`, `Volume`, `Language`, `Publisher` und leiten Sie die Ausgabe in eine neue Datei um. Sie können sie etwa `2014-01_JA_ivlp.tsv` nennen.
>> ## Lösung
>> Lassen Sie uns zunächst sehen, wo unsere gewünschten Spalten sind:
>>
>>~~~
>> head -n 1 2014-01_JA.tsv
>>~~~
>>{: .bash}
>>
>>~~~
>>File	Creator	Issue	Volume	Journal	ISSN	ID	Citation	Title	Place Labe	Language	Publisher	Date
>>~~~
>>{: .output}
>>
>>OK, jetzt wissen wir, dass `Thema` Spalte 3, `Band` 4, `Sprache` 11 und `Herausgeber` 12 ist.
>> Wir benutzen diese positionellen Spaltennummern, um unseren Befehl `cut` zu konstruieren:
>>```
>> cut -f 3,4,11,12 2014-01_JA.tsv > 2014-01_JA_ivlp.tsv
>>```
>> Wir können bestätigen, dass dies funktioniert hat, indem wir den Kopf auf die Akte legen:
>>```
>>head 2014-01_JA_ivlp.tsv
>>```
>>~~~
>>Issue	Volume	Language	Publisher
>>1	59	eng	ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY
>>1	59	eng	ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY
>>1	59	eng	ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY
>>1	59	eng	ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY
>>~~~
>>{: .output}
> {: .solution}
{: .challenge}
