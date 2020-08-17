---
Titel: "Arbeiten mit Freitext"
Lehre: 20
Übungen: 40
Fragen:
- "Wie arbeiten wir mit komplexen Akten?"
Ziele:
- "Verwendung von Shell-Werkzeugen zur Bereinigung und Umwandlung von freiem Text".
Schlüsselpunkte:
- "Schalenwerkzeuge können wirkungsvoll kombiniert werden"
---
### Arbeiten mit freiem Text

Bisher haben wir uns damit befasst, wie man die Unix-Shell zum Manipulieren, Zählen und
Mine tabellierte Daten. Einige Bibliotheksdaten, insbesondere digitalisierte Dokumente, sind viel unordentlicher als
tabellarische Metadaten. Nichtsdestotrotz können viele der gleichen Techniken angewandt werden
auf nicht-tabellierte Daten wie freien Text. Wir müssen sorgfältig darüber nachdenken
was es ist, was wir zählen und wie wir das Beste aus der Unix-Shell herausholen können.

Glücklicherweise gibt es da draußen eine Menge Leute, die diese Art von Arbeit machen, und wir
können sich das, was sie tun, als Einführung in die Arbeit mit diesen komplexeren Akten ausleihen.
Für diese letzte Übung werden wir also einen kleinen Sprung nach vorne machen
von Schwierigkeiten zu einem Szenario, in dem wir nicht über alles lernen, was
geschieht im Detail oder diskutiert ausführlich jedes Kommando. Wir werden
Texte vorzubereiten und auseinander zu nehmen, um einige der möglichen Anwendungen der Unix-Shell zu demonstrieren. Und wo Befehle, von denen wir gelernt haben, benutzt werden,
Ich habe Ihnen einen Teil der Rechenarbeit überlassen - bitte lesen Sie also in Ihren Notizen nach, falls Sie nicht weiterkommen!

Bevor Sie weitermachen, sprechen Sie mit der Person neben Ihnen und wählen Sie aus, an welcher Art von Text Sie gemeinsam arbeiten möchten. Sie haben drei Möglichkeiten:

- Ein Beispiel für von Hand transkribierten Text: *Gullivers Reisen* (1735)
- Ein Beispiel für Text, der durch einen optischen Zeichenerkennungsprozess erfasst wurde: *Generaler Bericht über die Physiographie von Maryland. Eine Dissertation, etc. (Nachgedruckt aus Report of Maryland State Weather Service.) [Mit Karten und Abbildungen.]* 1898 (aus [https://doi.org/10.21250/db12](https://doi.org/10.21250/db12))
- Ein Beispiel für eine Webseite: Piper's World (eine GeoCities-Seite von 1999, gespeichert unter [archive.org](http://wayback.archive.org/web/20091020080943/http:/geocities.com/Heartland/Hills/7649/diary.html))

## Option 1: Von Hand transkribierter Text

### Einen Text schnappen, aufräumen

Wir werden mit der Datei `gulliver.txt` arbeiten, die wir in der vorherigen Lektion erstellt haben.
Sie sollten (noch) im Verzeichnis `hell-lesson` arbeiten.

Sehen wir uns die Datei an.

~~~
$ less -N gulliver.txt
~~~
{: .bash}
~~~
      1 <U+FEFF>The Project Gutenberg eBook, Gulliver's Travels, by Jonatha
      1 n Swift
      2
      3
      4 This eBook is for the use of anyone anywhere at no cost and with
      5 almost no restrictions whatsoever.  You may copy it, give it away o
      5 r
      6 re-use it under the terms of the Project Gutenberg License included
      7 with this eBook or online at www.gutenberg.org
      8
      9
     10
     11
     12
     13 Title: Gulliver's Travels
     14        into several remote nations of the world
     15
     16
     17 Author: Jonathan Swift
     18
     19
     20
     21 Release Date: June 15, 2009  [eBook #829]
     22
     23 Language: English
     24
     25 Character set encoding: UTF-8
     26
     27
     28 ***START OF THE PROJECT GUTENBERG EBOOK GULLIVER'S TRAVELS***
     29
     30
     31 Transcribed from the 1892 George Bell and Sons edition by David Pri
     31 ce,
     32 email ccx074@pglaf.org
     33
     34
     35
~~~
{: .output}

Wir beginnen mit dem Befehl `sed`. Der Befehl erlaubt es Ihnen, Dateien direkt zu bearbeiten.

~~~
$ sed '9352,9714d' gulliver.txt > gulliver-nofoot.txt
~~~
{: .bash}

Das Kommando `sed` in Kombination mit dem `d`
Wert schaut sich `gulliver.txt` an und löscht alle
Werte zwischen den angegebenen Zeilen. Die Aktion `>` dann
fordert das Skript zu diesem bearbeiteten Text in der angegebenen neuen Datei auf.

~~~
$ sed '1,37d' gulliver-nofoot.txt > gulliver-noheadfoot.txt
~~~
{: .bash}

Dies macht dasselbe wie vorher, aber für den Kopfball.

Sie haben jetzt einen saubereren Text. Der nächste Schritt ist
sie noch weiter für eine rigorose Analyse vorzubereiten.

Wir verwenden jetzt den Befehl `tr`, der zum Übersetzen oder
Löschen von Zeichen. Tippen und ausführen:

~~~
$ tr -d '[:punct:]\r' < gulliver-noheadfoot.txt > gulliver-noheadfootpunct.txt
~~~
{: .bash}

Dabei werden der Befehl translate und eine spezielle Syntax verwendet, um alle Satzzeichen zu entfernen
(`[:punct:]`) und Zeilenumbrüche (`\r`).
Es erfordert auch die Verwendung sowohl des Ausgabe-Redirects `>`, den wir gesehen haben, als auch des Eingabe-Redirects `<`, den wir nicht gesehen haben.

Schließlich wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr [:upper:] [:lower:] < gulliver-noheadfootpunct.txt > gulliver-clean.txt
~~~
{: .bash}

Öffnen Sie die `gulliver-clean.txt` in einem Texteditor. Beachten Sie, wie der Text für die Analyse transformiert wurde.

### Auseinanderziehen eines Textes, Worthäufigkeiten zählen

Wir sind jetzt bereit, den Text auseinander zu ziehen.

~~~
$ tr ' ' ' '\n' < gulliver-clean.txt | sort | uniq -c | sort -nr > gulliver-final.txt
~~~
{: .bash}

Hier haben wir die Rohre, die wir in [Zählen und Bergbau mit der Schale]({{{{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben, ausgiebig genutzt. Der erste Teil dieses Skripts verwendet wieder den Befehl translate, diesmal, um jede Leerstelle in `\n` zu übersetzen, was als neue Zeile gerendert wird. Jedes Wort in der Datei wird zu diesem Zeitpunkt eine eigene Zeile haben.

Der zweite Teil verwendet den Befehl `sort`, um den Text von seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung umzuordnen.

Der dritte Teil benutzt `uniq`, ein weiteres neues Kommando, in Kombination mit dem Flag `-c`, um doppelte Zeilen zu entfernen und eine Wortzahl dieser Duplikate zu erzeugen.

Der vierte und letzte Teil sortiert den Text erneut nach der Anzahl der in Schritt drei erzeugten Duplikate.

> ## Herausforderung
> Es sind noch einige Interpunktionszeichen im Text vorhanden. Sie werden 'intelligente' oder 'geschweifte' Anführungszeichen genannt.
> Können Sie sie mit `sed` entfernen?
>
> Hinweis: Diese Anführungszeichen gehören nicht zu den 128 Zeichen des ASCII-Standards,
> so dass sie in der Datei mit einem anderen Standard, UTF-8, kodiert sind.
> Während dies für `sed` kein Problem darstellt, versteht das Fenster, in das Sie tippen, möglicherweise nicht UTF-8.
> Wenn dies der Fall ist, müssen Sie ein Bash-Skript verwenden; wir sind am Ende von Episode 4 darauf gestoßen,
> 'Das Langweilige mit Schleifen automatisieren'.
>
> Zur Erinnerung: Benutzen Sie den Texteditor Ihrer Wahl, um eine Datei zu schreiben, die wie diese aussieht:
> > ```
> > #!/bin/bash
> > # Dieses Script entfernt die Anführungszeichen aus gulliver-clean.txt und speichert das Ergebnis als gulliver-noquotes.txt
> > (ersetzen Sie diese Zeile durch Ihre Lösung)
> > ```
> > {: .bash}
> Speichern Sie die Datei als `remove-quotes.sh` und starten Sie sie von der Befehlszeile aus wie folgt:
> > ```
> > bash remove-quotes.sh
> > ```
> > {: .bash}
>
> > ## Lösung
> > ```
> > #!/bin/bash
> > # Dieses Script entfernt die Anführungszeichen aus gulliver-clean.txt und speichert das Ergebnis als gulliver-noquotes.txt
> > sed -Ee 's/[""'']//g' gulliver-clean.txt > gulliver-noquotes.txt
> > ```
> > {: .bash}
> > Wenn das bei Ihnen nicht funktioniert, müssen Sie eventuell prüfen, ob Ihr Texteditor
> > Dateien mit der UTF-8-Kodierung speichern.
> {: .lösung}
{: .herausfordern}

Wir haben den Text jetzt auseinandergenommen und eine
zählen für jedes Wort darin. Das sind Daten, die wir stupsen und durchstöbern können
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und kann sich mit anderen auf die gleiche Weise bearbeiteten Texten vergleichen.
Und wenn wir einen anderen Transformationssatz für
eine andere Analyse, können wir zu `gulliver-clean.txt` zurückkehren, um mit dieser Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten anspruchslosen, aber sehr mächtigen Befehlszeile.

## Option 2: Text mit optischer Zeichenerkennung

### Einen Text schnappen, aufräumen

Wir werden mit `201403160_01_text.json` arbeiten.

Sehen wir uns die Akte an.

~~~
$ less -N 201403160_01_text.json
~~~
{: .bash}
~~~
      1 [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, "A GENERAL RE
      1 PORT ON THE PHYSIOGRAPHY OF MARYLAND A DISSERTATION PRESENTED TO THE PRE
      1 SIDENT AND FACULTY OF THE JOHNS HOPKINS UNIVERSITY FOR THE DEGREE OF DOC
      1 TOR OF PHILOSOPHY BY CLEVELAND ABBE, Jr. BALTIMORE, MD. MAY, 1898."], [8
      1 , ""], [9, ""], [10, "A MAP S H OW I N G THE PHYSIOGRAPHIC PROVINCES OF
      1 MARYLAND AND Their Subdivisions Scale 1 : 2,000.000. 32 Miles-1 Inch"],
      1 [11, "A GENERAL REPORT ON THE PHYSIOGRAPHY OF MARYLAND A DISSERTATION PR
      1 ESENTED TO THE PRESIDENT AND FACULTY OF THE JOHNS HOPKINS UNIVERSITY FOR
      1  THE DEGREE OF DOCTOR OF PHILOSOPHY BY CLEVELAND ABBE, Jr. BALTIMORE, MD
      1 . MAY, 1898."], [12, "PRINTED BY tL%t jfricbcnrtxifti Compang BALTIMORE,
      1  MD., U. S. A. REPRINTED FROM Report of Maryland State Weather Service,
      1 Vol. 1, 1899, pp. 41-216."], [13, "A GENERAL REPORT ON THE PHYSIOGRAPHY
      1 OF MARYLAND Physiographic Processes. INTRODUCTION. From the earliest tim
      1 es men have observed more or less closely the various phenomena which na
      1 ture presents, and have sought to find an explanation for them. Among th
      1 e most interesting of these phe nomena have been those which bear on the
      1  development of the sur face features of the earth or its topography. Im
      1 pressed by the size and grandeur of the mountains, their jagged crests a
      1 nd scarred sides, early students of geographical features were prone to
      1 ascribe their origin to great convulsions of the earth's crust, earthqua
      1 kes and vol canic eruptions. One generation after another comes and goes
      1 , yet the mountains continue to rear their heads to the same heights, th
      1 e rivers to run down the mountain sides in the same courses and follow t
~~~
{: .output}

Wir beginnen mit dem `tr'-Befehl, der zum Übersetzen oder
Löschen von Zeichen. Tippen und ausführen:

~~~
$ tr -d [:punct:] < 201403160_01_text.json > 201403160_01_text-nopunct.txt
~~~
{: .bash}

Dabei werden der Befehl translate und eine spezielle Syntax verwendet, um alle Satzzeichen zu entfernen.
Es erfordert auch die Verwendung sowohl der Ausgabe-Umleitung `>`, die wir gesehen haben, als auch der Eingabe-Umleitung `<`, die wir nicht gesehen haben.

Abschließend wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr [:upper:] [:lower:] < 201403160_01_text-nopunct.txt > 201403160_01_text-clean.txt
~~~
{: .bash}

Öffnen Sie die `201403160_01_text-clean.txt` in einem Texteditor. Beachten Sie, wie der Text für die Analyse transformiert wurde.

### Auseinanderziehen eines Textes, Worthäufigkeiten zählen

Wir sind jetzt bereit, den Text auseinander zu ziehen.

~~~
$ tr ' ' '\n' < 201403160_01_text-clean.txt | sort | uniq -c | sort -nr > 201403160_01_text-final.txt
~~~
{: .bash}

Hier haben wir die Rohre, die wir in [Zählen und Bergbau mit der Schale]({{{{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben, ausgiebig genutzt. Der erste Teil dieses Skripts verwendet wieder den Befehl translate, diesmal, um jede Leerstelle in `\n` zu übersetzen, was als neue Zeile gerendert wird. Jedes Wort in der Datei wird zu diesem Zeitpunkt eine eigene Zeile haben.

Der zweite Teil verwendet den Befehl `sort`, um den Text von seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung umzuordnen.

Der dritte Teil benutzt `uniq`, ein weiteres neues Kommando, in Kombination mit dem Flag `-c`, um doppelte Zeilen zu entfernen und eine Wortzahl dieser Duplikate zu erzeugen.

Der vierte und letzte Teil sortiert den Text erneut nach der Anzahl der in Schritt drei erzeugten Duplikate.

**Anmerkung: Ihre endgültige Ausgabe wird ein Problem haben - nicht alle gezählten Wörter sind echte Wörter (siehe die Wörter, die nur 1 oder 2 Mal gezählt wurden). Um besser zu verstehen, was passiert ist, suchen Sie online, um mehr über die optische Zeichenerkennung von Texten zu erfahren**

So oder so haben wir jetzt den Text auseinandergenommen und eine
zählen für jedes Wort darin. Das sind Daten, die wir stupsen und durchstöbern können
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und kann sich mit anderen auf die gleiche Weise bearbeiteten Texten vergleichen.
Und wenn wir einen anderen Transformationssatz für
eine andere Analyse, können wir zu `201403160_01_text-clean.txt` zurückkehren, um mit dieser Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten anspruchslosen, aber sehr mächtigen Befehlszeile.

## Option 3: Eine Webseite

### Einen Text schnappen, aufräumen

Wir werden mit `Tagebuch.html` arbeiten.

Sehen wir uns die Datei an.

~~~
$ less -N diary.html
~~~
{: .bash}
~~~
      1 <!-- This document was created with HomeSite v2.5 -->
      2 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
      3 <html>
      4
      5 <head>
      6
      7
      8 <script type="text/javascript" src="/static/js/analytics.js"></script>
      9 <script type="text/javascript">archive_analytics.values.server_name="www
      9 b-app6.us.archive.org";archive_analytics.values.server_ms=105;</script>
     10 <link type="text/css" rel="stylesheet" href="/static/css/banner-styles.c
     10 ss"/>
     11
     12
     13 <title>Piper's Diary</title>
     14 <meta name="description"
     15 content="Come visit our shih tzu, Piper.  He has his very own photo gall
     15 ary, monthly diary, newsletter, and dog site award.  He also maintains d
     15 og book reviews and quotations.  Come check him out!">
     16 <meta name="keywords"
     17 content="shih tzu, dog, pet, quotations, award, diary, advice, book, rev
     17 iew, piper">
     18 <style TYPE="text/css" TITLE="Basic Fonts">

~~~
{: .output}

Wir beginnen mit dem Befehl `sed`. Der Befehl erlaubt es Ihnen, Dateien direkt zu bearbeiten.

~~~
$ sed '265,330d' diary.html > diary-nofoot.txt
~~~
{: .bash}

Das Kommando `sed` in Kombination mit dem `d`
Wert schaut sich `diary.html` an und löscht alle
Werte zwischen den angegebenen Zeilen. Die Aktion `>` dann
fordert das Skript zu diesem bearbeiteten Text in der angegebenen neuen Datei auf.

~~~
$ sed '1,221d' diary-nofoot.txt > diary-noheadfoot.txt
~~~
{: .bash}

Dies macht dasselbe wie vorher, aber für den Kopfball.

Sie haben jetzt einen saubereren Text. Der nächste Schritt ist
sie noch weiter für eine rigorose Analyse vorzubereiten.

Zuerst werden wir alle html-Tags entfernen. Tippen und ausführen:

~~~
$ sed -e 's/<[^>]*>//g' diary-noheadfoot.txt > diary-notags.txt
~~~
{: .bash}

Hier verwenden wir einen regulären Ausdruck (siehe die [Library Carpentry Lektion über reguläre Ausdrücke]({{{{ page.root }}}/lc-data-intro/04-regular-expressions/), um alle gültigen html-Tags (alles innerhalb spitzer Klammern) zu finden und sie zu löschen. Dies ist ein komplexer regulärer Ausdruck, machen Sie sich nicht allzu viele Gedanken darüber, wie er funktioniert! Das Skript erfordert auch die Verwendung sowohl des Output-Redirects `>`, den wir gesehen haben, als auch des Input-Redirects `<`, den wir nicht gesehen haben.

Wir beginnen mit der Verwendung des Befehls `tr`, der für die Übersetzung oder
Löschen von Zeichen. Tippen und ausführen:

~~~
$ tr -d '[:punct:]\r' < diary-notags.txt > diary-notagspunct.txt
~~~
{: .bash}

Dabei werden der Befehl translate und eine spezielle Syntax verwendet, um alle Satzzeichen zu entfernen
(`[:punct:]`) und Zeilenumbrüche (`\r`).

Schließlich wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr [:upper:] [:lower:] < diary-notagspunct.txt > diary-clean.txt
~~~
{: .bash}

Öffnen Sie die Datei `diary-clean.txt` in einem Texteditor. Notieren Sie, wie der Text für die Analyse transformiert wurde.

### Auseinanderziehen eines Textes, Worthäufigkeiten zählen

Wir sind jetzt bereit, den Text auseinander zu ziehen.

~~~
$ tr ' ' '\n' < diary-clean.txt | sort | uniq -c | sort -nr > diary-final.txt
~~~
{: .bash}

Hier haben wir die Rohre, die wir in [Zählen und Bergbau mit der Schale]({{{{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben, ausgiebig genutzt. Der erste Teil dieses Skripts verwendet wieder den Befehl translate, diesmal, um jede Leerstelle in `\n` zu übersetzen, was als neue Zeile gerendert wird. Jedes Wort in der Datei wird zu diesem Zeitpunkt eine eigene Zeile haben.

Der zweite Teil verwendet den Befehl `sort`, um den Text von seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung umzuordnen.

Der dritte Teil benutzt `uniq`, ein weiteres neues Kommando, in Kombination mit dem Flag `-c`, um doppelte Zeilen zu entfernen und eine Wortzahl dieser Duplikate zu erzeugen.

Der vierte und letzte Teil sortiert den Text erneut nach der Anzahl der in Schritt drei erzeugten Duplikate.

Wir haben nun den Text auseinandergenommen und eine Liste der Dubletten erstellt.
zählen für jedes Wort darin. Das sind Daten, die wir stupsen und durchstöbern können
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und kann sich mit anderen auf die gleiche Weise bearbeiteten Texten vergleichen.
Und wenn wir einen anderen Transformationssatz für
eine andere Analyse, können wir zu `Diary-final.txt` zurückkehren, um mit dieser Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten unscheinbaren, aber sehr mächtigen Befehlszeile.

## Wohin als Nächstes?

Deborah S. Ray und Eric J. Ray, *Unix und Linux: visuelle Schnellstartanleitung*, 4. Auflage (2009).
Unschätzbar wertvoll (und nicht teuer) als Nachschlagewerk - besonders wenn Sie die Kommandozeile nur sporadisch benutzen!

[Der Kommandozeilen-Crashkurs](https://learncodethehardway.org/unix/)
'UNIX auf die harte Tour lernen' - gut geeignet, um an die Grundlagen zu erinnern.

[Langweilige Sachen automatisieren] (https://automatetheboringstuff.com/)

Ein weiterer Coursera-Kurs, [Programmieren für jedermann (Python)] (https://www.coursera.org/course/pythonlearn)
ist verfügbar und dauert 10 Wochen, wenn Sie 2-4 Stunden pro Woche zur Verfügung haben.
Python ist in der Forschungsprogrammierung beliebt, da es lesbar, relativ einfach und sehr leistungsfähig ist.

Bill Turkel und die Digital History-Gemeinschaft im weiteren Sinne.
Die zweite Lektion, die Sie heute gehalten haben, basierte auf einer Lektion, die Bill auf [seiner Website] (https://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/) gehalten hat, und Bill ist auch allgemeiner Herausgeber des [Programmierhistoriker] (https://programminghistorian.org/project-team). Der Programming Historian ist ein offenes, gemeinschaftlich verfasstes Buch, das darauf abzielt, Historikern Programmierunterricht zu erteilen. Obwohl sich die Lektionen um Probleme drehen, die Historiker haben, haben ihre Lektionen - die verschiedene Programmiersprachen abdecken - eine breite Anwendbarkeit - in der Tat basiert der heutige Kurs auf zwei Lektionen, die ich zusammen mit Ian Milligan, einem Historiker in Waterloo, Kanada, für ProgHist geschrieben habe. Bill hat auch ein wunderbares Tutorial über ['Named Entity Recognition with Command Line Tools in Linux'] (http://williamjturkel.net/2013/06/30/named-entity-recognition-with-command-line-tools-in-linux/), das ich sehr empfehle, wenn Sie Namen, Orte und Organisationen in Textdateien automatisch finden, markieren und zählen wollen...

## Schlussfolgerung

In dieser Sitzung haben Sie gelernt, sich in der Unix-Shell zurechtzufinden, einige
einfaches Zählen, Verketten und Löschen von Dateien, um datenübergreifend nach gemeinsamen
Strings, um Ergebnisse und abgeleitete Daten zu speichern und Textdaten für eine strenge rechnergestützte Analyse vorzubereiten.

Dies kratzt nur an der Oberfläche dessen, wozu die Unix-Umgebung in der Lage ist.
Es ist jedoch zu hoffen, dass diese Sitzung einen Vorgeschmack geliefert hat, der ausreicht, um
weitere Untersuchungen und produktives Spiel anregen.

Denken Sie daran, dass das volle Potenzial, das die Instrumente bieten können, möglicherweise nur
entstehen, wenn diese Fähigkeiten in reale Projekte eingebettet werden. Nichtsdestotrotz,
Die Möglichkeit, Tausende von Dateien zu manipulieren, zu zählen und zu verminen, ist äußerst nützlich.
Selbst eine große Sammlung von Dateien, die keine alphanumerischen Daten enthalten
Elemente, wie z.B. Bilddateien, können leicht sortiert, ausgewählt und abgefragt werden
über den Umfang der Beschreibung, der in jedem Dateinamen enthaltenen Metadaten.
Wenn nicht eine Voraussetzung für die Arbeit mit Unix, dann nehmen Sie sich die Zeit
Ihre Daten auf konsistente und vorhersehbare Weise zu strukturieren, ist
sicherlich ein bedeutender Schritt, um das Beste aus Unix herauszuholen
Befehle. Und wenn Sie einen Weg finden können, die Unix-Shell regelmäßig zu benutzen - vielleicht
nur um Dateien zu kopieren oder zu ändern - Sie halten die Grundlagen frisch, was bedeutet, dass
wenn Sie das nächste Mal Anlass haben, die Unix-Shell für komplexere Befehle zu verwenden,
sollten Sie nicht alles noch einmal lernen müssen.

## References

James Baker and Ian Milligan, 'Counting and mining research data with Unix', *The Programming Historian* ([2014](https://programminghistorian.org/lessons/research-data-with-unix))

Ian Milligan and James Baker, 'Introduction to the Bash Command Line', *The Programming Historian* ([2014](https://programminghistorian.org/lessons/intro-to-bash))

William J. Turkel, 'Named Entity Recognition with Command Line Tools in Linux' ([30 June 2013](http://williamjturkel.net/2013/06/30/named-entity-recognition-with-command-line-tools-in-linux/)). The section 'NER Demo' is adapted from this and shared under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-nc-sa/3.0/).

William J. Turkel, 'Basic Text Analysis with Command Line Tools in Linux' ([15 June 2013](https://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/)). The sections 'Grabbing a text, cleaning it up' and 'Pulling a text apart, counting word frequencies' are adapted from this and shared under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-nc-sa/3.0/).
