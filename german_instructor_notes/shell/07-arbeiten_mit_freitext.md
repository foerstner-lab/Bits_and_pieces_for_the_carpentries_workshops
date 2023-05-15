---
Titel: "Arbeiten mit freiem Text"
Unterricht: 20
Übungen: 40
Fragen:
- "Wie arbeiten wir mit komplexen Dateien?"
Ziele:
- "Shell-Werkzeuge verwenden, um freien Text zu bereinigen und umzuwandeln"
Kernpunkte:
- "Shell-Werkzeuge können wirkungsvoll kombiniert werden"
---
### Arbeiten mit freiem Text

Bisher haben wir uns angesehen, wie man die Unix-Shell benutzt, um Daten zu manipulieren, zu zählen und
tabellarische Daten zu analysieren. Manche Bibliotheksdaten, vor allem digitalisierte Dokumente, sind viel unordentlicher als
tabellarische Metadaten. Dennoch lassen sich viele der gleichen Techniken auch auf nicht-tabellarische Daten wie Freitext angewenden.

Für diese letzte Übung machen wir also einen kleinen Sprung nach vorne, und zwar
ein Szenario, in dem wir nicht alles, was passiert, im Detail lernen oder jeden Befehl ausführlich besprechen. Wir werden Texte vorbereiten und auseinandernehmen, um einige der möglichen Anwendungen der Unix-Shell zu demonstrieren. Und wo die Befehle, die wir kennengelernt haben, verwendet werden.


## Option 1: Handschriftlicher Text

### Einen Text erfassen und bereinigen

Wir werden mit der Datei `little_women.txt` arbeiten, die wir in erstellt haben.
Du solltest (noch) im Verzeichnis `shell-lesson` arbeiten.

Schauen wir uns die Datei an.

~~~
$ less -N little_women.txt
~~~


Wir beginnen mit dem Befehl `sed`. Mit diesem Befehl kannst du Dateien direkt bearbeiten.

~~~
$ sed '9352,9714d' gulliver.txt > gulliver-nofoot.txt
~~~
{: .bash}

Der Befehl `sed` in Kombination mit dem `d`
Wert wird die Datei `gulliver.txt` durchsuchen und alle
Werte zwischen den angegebenen Zeilen. Die `>`-Aktion veranlasst dann
fordert das Skript auf, diesen bearbeiteten Text in die angegebene neue Datei zu schreiben.

~~~
$ sed '1,37d' gulliver-nofoot.txt > gulliver-noheadfoot.txt
~~~
{: .bash}

Dies macht das Gleiche wie vorher, aber für die Kopfzeile.

Du hast jetzt einen saubereren Text. Der nächste Schritt ist
ihn noch weiter für eine gründliche Analyse vorzubereiten.

Wir verwenden jetzt den Befehl `tr`, mit dem wir Zeichen übersetzen oder
Löschen von Zeichen. Tippe und führe ihn aus:

~~~
$ tr -d '[:punct:]\r' < gulliver-noheadfoot.txt > gulliver-noheadfootpunct.txt
~~~
{: .bash}

Dies verwendet den Befehl translate und eine spezielle Syntax, um alle Satzzeichen zu entfernen
(`[:punct:]`) und Zeilenumbrüche (`\r`).
Außerdem muss sowohl die Ausgabeumleitung `>`, die wir gesehen haben, als auch die Eingabeumleitung `<`, die wir nicht gesehen haben, verwendet werden.

Schließlich wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr '[:upper:]' '[:lower:]' < gulliver-noheadfootpunct.txt > gulliver-clean.txt
~~~
{: .bash}

Öffne die `gulliver-clean.txt` in einem Texteditor. Beachte, wie der Text für die Analyse umgewandelt wurde.

### Einen Text auseinandernehmen, Worthäufigkeiten zählen

Jetzt können wir den Text zerlegen.

~~~
$ tr ' ' '\n' < gulliver-clean.txt | sort | uniq -c | sort -nr > gulliver-final.txt
~~~
{.bash}

Hier machen wir erweiterten Gebrauch von den Pipes, die wir in [Zählen und Mining mit der Shell]({{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben. Der erste Teil dieses Skripts verwendet wieder den translate-Befehl, diesmal um jedes Leerzeichen in `\n` zu übersetzen, was als neue Zeile dargestellt wird. Jedes Wort in der Datei hat jetzt seine eigene Zeile.

Der zweite Teil verwendet den Befehl `sort`, um den Text aus seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung zu bringen.

Im dritten Teil wird `uniq`, ein weiterer neuer Befehl, in Kombination mit dem Flag `-c` verwendet, um doppelte Zeilen zu entfernen und eine Wortzählung dieser Duplikate zu erstellen.

Der vierte und letzte Teil sortiert den Text wieder nach der Anzahl der Duplikate, die in Schritt drei erzeugt wurden.

> ## Herausforderung
> Es sind noch einige Satzzeichen im Text übrig. Sie werden "intelligente" oder "geschweifte" Anführungszeichen genannt.
> Kannst du sie mit `sed` entfernen?
>
> Hinweis: Diese Anführungszeichen gehören nicht zu den 128 Zeichen des ASCII-Standards,
> deshalb werden sie in der Datei mit einem anderen Standard, UTF-8, kodiert.
> Für `sed` ist das kein Problem, aber das Fenster, in das du eintippst, versteht vielleicht kein UTF-8.
> In diesem Fall musst du ein Bash-Skript verwenden; wir haben es am Ende von Folge 4 kennengelernt,
> "Das Mühsame mit Schleifen automatisieren".
>
> Zur Erinnerung: Verwende einen Texteditor deiner Wahl, um eine Datei zu schreiben, die wie folgt aussieht:
> > ```
> > #!/bin/bash
> > # Dieses Skript entfernt die Anführungszeichen aus gulliver-clean.txt und speichert das Ergebnis als gulliver-noquotes.txt
> > (ersetze diese Zeile mit deiner Lösung)
> > ```
> > {: .bash}
> Speichere die Datei als `remove-quotes.sh` und führe sie wie folgt von der Kommandozeile aus:
> > ```
> > bash remove-quotes.sh
> > ```
> > {: .bash}
>
> > ## Lösung
> > ```
> > #!/bin/bash
> > ## Dieses Skript entfernt die Anführungszeichen aus gulliver-clean.txt und speichert das Ergebnis als gulliver-noquotes.txt
> > sed -Ee 's/[""'']//g' gulliver-clean.txt > gulliver-noquotes.txt
> > ```
> > {: .bash}
> > Wenn das bei dir nicht funktioniert, musst du vielleicht überprüfen, ob dein Texteditor
> > Dateien mit der Kodierung UTF-8 speichern kann.
> {: .solution}
{: .challenge}

Jetzt haben wir den Text auseinandergenommen und eine
Zählung für jedes Wort im Text. Das sind Daten, die wir durchstöbern und
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und mit anderen Texten vergleichen können, die auf die gleiche Weise bearbeitet wurden.
Und wenn wir für eine andere Analyse eine andere Umwandlung durchführen müssen
eine andere Analyse durchführen müssen, können wir zu "gulliver-clean.txt" zurückkehren, um diese Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten unscheinbaren, aber sehr mächtigen Kommandozeile.

## Option 2: Optische Zeichenerkennung von Text

## Einen Text erfassen und bereinigen

Wir arbeiten mit der Datei "201403160_01_text.json".

Schauen wir uns die Datei an.

~~~
$ less -N 201403160_01_text.json
~~~
{: .bash}
~~~
      1 [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, "A GENERAL RE
      1 PORT ON THE PHYSIOGRAPHY OF MARYLAND A DISSERTATION PRESENTED TO THE PRE
      1 SIDENTEN UND DER FAKULTÄT DER JOHNS HOPKINS UNIVERSITÄT FÜR DEN DOKTORGRAD DER
      1 TOR OF PHILOSOPHY BY CLEVELAND ABBE, Jr. BALTIMORE, MD. MAY, 1898."], [8
      1 , ""], [9, ""], [10, "A MAP S H OW I N G THE PHYSIOGRAPHIC PROVINCES OF
      1 MARYLAND AND Their Subdivisions Scale 1 : 2,000.000. 32 Miles-1 Inch"],
      1 [11, "A GENERAL REPORT ON THE PHYSIOGRAPHY OF MARYLAND A DISSERTATION PR
      1 ESENTED TO THE PRESIDENT AND FACULTY OF THE JOHNS HOPKINS UNIVERSITY FOR
      1 DEN DOKTOR DER PHILOSOPHIE VON CLEVELAND ABBE, Jr. BALTIMORE, MD
      1 . MAI, 1898."], [12, "PRINTED BY tL%t jfricbcnrtxifti Compang BALTIMORE,
      1 MD, U. S. A. GEDRUCKT AUS dem Bericht des Maryland State Weather Service,
      1 Vol. 1, 1899, pp. 41-216."], [13, "EIN ALLGEMEINER BERICHT ÜBER DIE PHYSIOGRAPHIE
      1 VON MARYLAND Physiographische Prozesse. EINLEITUNG. Seit den frühesten Zeiten
      1 en haben die Menschen die verschiedenen Phänomene der Natur mehr oder weniger genau
      1 turelle Phänomene mehr oder weniger genau beobachtet und versucht, eine Erklärung für sie zu finden. Zu den
      1 e interessantesten dieser Phänomene waren die, die sich auf die
      1 Entwicklung der Oberflächenmerkmale der Erde oder ihrer Topografie. Im
      1 Beeindruckt von der Größe und Erhabenheit der Berge, ihren zerklüfteten Kämmen und
      1 und den zerklüfteten Flanken neigten die frühen Geographen dazu
      1 ihren Ursprung auf große Erschütterungen der Erdkruste, Erdbeben
      1 kes und Vulkanausbrüche. Eine Generation nach der anderen kommt und geht
      1 und doch ragen die Berge immer wieder in dieselben Höhen, die
      1 e Flüsse fließen in denselben Bahnen die Berghänge hinunter und folgen dem
~~~
{: .output}

Wir beginnen mit dem Befehl `tr`, der zum Übersetzen oder
Löschen von Zeichen. Gib ihn ein und führe ihn aus:

~~~
$ tr -d '[:punct:]' < 201403160_01_text.json > 201403160_01_text-nopunct.txt
~~~
{: .bash}

Dies verwendet den Befehl translate und eine spezielle Syntax, um alle Satzzeichen zu entfernen.
Außerdem muss sowohl die Ausgabeumleitung `>`, die wir gesehen haben, als auch die Eingabeumleitung `<`, die wir nicht gesehen haben, verwendet werden.

Schließlich wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr '[:upper:]' '[:lower:]' < 201403160_01_text-nopunct.txt > 201403160_01_text-clean.txt
~~~
{: .bash}

Öffne die `201403160_01_text-clean.txt` in einem Texteditor. Beachte, wie der Text für die Analyse umgewandelt wurde.

### Einen Text auseinandernehmen, Worthäufigkeiten zählen

Jetzt können wir den Text zerlegen.

~~~
$ tr ' ' '\n' < 201403160_01_text-clean.txt | sort | uniq -c | sort -nr > 201403160_01_text-final.txt
~~~
{: .bash}

Hier machen wir erweiterten Gebrauch von den Pipes, die wir in [Zählen und Mining mit der Shell]({{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben. Der erste Teil dieses Skripts verwendet wieder den translate-Befehl, diesmal um jedes Leerzeichen in `\n` zu übersetzen, was als neue Zeile dargestellt wird. Jedes Wort in der Datei hat jetzt seine eigene Zeile.

Der zweite Teil verwendet den Befehl `sort`, um den Text aus seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung zu bringen.

Im dritten Teil wird `uniq`, ein weiterer neuer Befehl, in Kombination mit dem Flag `-c` verwendet, um doppelte Zeilen zu entfernen und eine Wortzählung dieser Duplikate zu erstellen.

Der vierte und letzte Teil sortiert den Text wieder nach der Anzahl der Duplikate, die in Schritt drei erzeugt wurden.

**Hinweis: Deine endgültige Ausgabe wird ein Problem haben - nicht alle gezählten Wörter sind echte Wörter (siehe die Wörter, die nur 1 oder 2 Mal gezählt wurden). Um besser zu verstehen, was passiert ist, kannst du im Internet mehr über die optische Zeichenerkennung von Texten herausfinden**

Auf jeden Fall haben wir den Text auseinandergenommen und eine
Zählung für jedes Wort erstellt. Das sind Daten, die wir durchstöbern und
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und mit anderen Texten vergleichen können, die auf die gleiche Weise bearbeitet wurden.
Und wenn wir für eine andere Analyse eine andere Umwandlung durchführen müssen
eine andere Analyse durchführen müssen, können wir zu `201403160_01_text-clean.txt` zurückkehren, um diese Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten unscheinbaren, aber sehr mächtigen Kommandozeile.

## Option 3: Eine Webseite

### Einen Text greifen, ihn bereinigen

Wir werden mit `diary.html` arbeiten.

Schauen wir uns die Datei an.

~~~
$ less -N tagebuch.html
~~~
{: .bash}
~~~
      1 <!-- Dieses Dokument wurde mit HomeSite v2.5 erstellt -->
      2 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//DE">
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
     13 <title>Pipers Tagebuch</title>
     14 <meta name="description"
     15 content="Komm und besuche unseren Shih Tzu, Piper.  Er hat seine ganz eigene Fotogalerie
     15 ary, ein monatliches Tagebuch, einen Newsletter und einen Hundeseiten-Award.  Außerdem unterhält er d
     15 og Buchbesprechungen und Zitate.  Schau ihn dir an!">
     16 <meta name="keywords"
     17 content="shih tzu, hund, haustier, zitate, award, tagebuch, ratschläge, buch, rev
     17 iew, piper">
     18 <style TYPE="text/css" TITLE="Basic Fonts">

~~~
{: .output}

Wir beginnen mit dem Befehl `sed`. Der Befehl ermöglicht es dir, Dateien direkt zu bearbeiten.

~~~
$ sed '265,330d' diary.html > diary-nofoot.txt
~~~
{: .bash}

Der Befehl `sed` in Kombination mit dem `d`
Wert sieht sich `diary.html` an und löscht alle
Werte zwischen den angegebenen Zeilen. Die Aktion `>` veranlasst dann
fordert das Skript auf, diesen bearbeiteten Text in die angegebene neue Datei zu schreiben.

~~~
$ sed '1,221d' diary-nofoot.txt > diary-noheadfoot.txt
~~~
{: .bash}

Dies macht das Gleiche wie vorher, aber für die Kopfzeile.

Du hast jetzt einen saubereren Text. Der nächste Schritt ist
den Text noch weiter für eine strenge Analyse vorzubereiten.

Zuerst entfernen wir alle html-Tags. Tippe und führe aus:

~~~
$ sed -e 's/<[^>]*>//g' diary-noheadfoot.txt > diary-notags.txt
~~~
{: .bash}

Hier verwenden wir einen regulären Ausdruck (siehe die [Lektion über reguläre Ausdrücke in der Bibliothek](https://librarycarpentry.org/lc-data-intro/01-regular-expressions/), um alle gültigen html-Tags (alles innerhalb von spitzen Klammern) zu finden und zu löschen). Dies ist ein komplexer regulärer Ausdruck, also mach dir nicht zu viele Gedanken darüber, wie er funktioniert! Das Skript erfordert außerdem die Verwendung des Output Redirects `>`, den wir gesehen haben, und des Input Redirects `<`, den wir nicht gesehen haben.

Wir beginnen mit dem Befehl `tr`, der zum Übersetzen oder
Löschen von Zeichen. Gib ihn ein und führe ihn aus:

~~~
$ tr -d '[:punct:]\r' < tagebuch-notags.txt > tagebuch-notagspunct.txt
~~~
{: .bash}

Dies verwendet den Befehl translate und eine spezielle Syntax, um alle Satzzeichen zu entfernen
(`[:punct:]`) und Zeilenumbrüche (`\r`).

Schließlich wird der Text regularisiert, indem alle Großbuchstaben entfernt werden.

~~~
$ tr '[:upper:]' '[:lower:]' < tagebuch-notagspunct.txt > tagebuch-clean.txt
~~~
{: .bash}

Öffne die `diary-clean.txt` in einem Texteditor. Beachte, wie der Text für die Analyse umgewandelt wurde.

### Einen Text auseinandernehmen, Worthäufigkeiten zählen

Jetzt können wir den Text zerlegen.

~~~
$ tr ' ' '\n' < diary-clean.txt | sort | uniq -c | sort -nr > diary-final.txt
~~~
{: .bash}

Hier machen wir erweiterten Gebrauch von den Pipes, die wir in [Zählen und Mining mit der Shell] ({{ page.root }}{% link _episodes/05-counting-mining.md %}) gesehen haben. Der erste Teil dieses Skripts verwendet wieder den translate-Befehl, diesmal um jedes Leerzeichen in `\n` zu übersetzen, was als neue Zeile dargestellt wird. Jedes Wort in der Datei hat jetzt seine eigene Zeile.

Der zweite Teil verwendet den Befehl `sort`, um den Text aus seiner ursprünglichen Reihenfolge in eine alphabetische Anordnung zu bringen.

Im dritten Teil wird `uniq`, ein weiterer neuer Befehl, in Kombination mit dem Flag `-c` verwendet, um doppelte Zeilen zu entfernen und eine Wortzählung dieser Duplikate zu erstellen.

Der vierte und letzte Teil sortiert den Text wieder nach der Anzahl der Duplikate, die in Schritt drei erzeugt wurden.

Jetzt haben wir den Text auseinandergenommen und eine
Zählung für jedes Wort im Text. Das sind Daten, die wir durchstöbern und
und visualisieren, die die Grundlage für unsere Untersuchungen bilden können,
und mit anderen Texten vergleichen können, die auf die gleiche Weise bearbeitet wurden.
Und wenn wir für eine andere Analyse eine andere Umwandlung durchführen müssen
eine andere Analyse durchführen müssen, können wir zu `diary-final.txt` zurückkehren, um diese Arbeit zu beginnen.

Und das alles mit ein paar Befehlen auf einer ansonsten unscheinbaren, aber sehr mächtigen Kommandozeile.

## Wo geht's weiter?

Deborah S. Ray und Eric J. Ray, *Unix and Linux: visual quickstart guide*, 4. Auflage (2009).
Als Nachschlagewerk von unschätzbarem Wert (und nicht teuer) - vor allem, wenn du die Kommandozeile nur sporadisch benutzt!

[The Command Line Crash Course](https://learncodethehardway.org/unix/)
'Learn UNIX the Hard Way' - gut, um sich an die Grundlagen zu erinnern.

[Automate the Boring Stuff](https://automatetheboringstuff.com/)

Ein weiterer Coursera-Kurs, [Programming for Everybody (Python)](https://www.coursera.org/course/pythonlearn)
ist verfügbar und dauert 10 Wochen, wenn du 2-4 Stunden pro Woche Zeit hast.
Python ist in der Forschungsprogrammierung sehr beliebt, da es gut lesbar, relativ einfach und sehr leistungsstark ist.

Bill Turkel und die Digital History Community im Allgemeinen.
Die zweite Lektion, die du heute gemacht hast, basierte auf einer Lektion, die Bill auf [seiner Website](https://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/) anbietet. Bill ist auch einer der Herausgeber des [Programming Historian](https://programminghistorian.org/project-team). The Programming Historian ist ein offenes, gemeinschaftliches Buch mit dem Ziel, Historikern Programmierunterricht zu geben. Obwohl sich die Lektionen an den Problemen von Historikern orientieren, sind die Lektionen - die verschiedene Programmiersprachen abdecken - breit anwendbar. Der heutige Kurs basiert auf zwei Lektionen, die ich zusammen mit Ian Milligan, einem Historiker in Waterloo, Kanada, für ProgHist geschrieben habe. Bill hat auch ein wunderbares Tutorial über ['Named Entity Recognition with Command Line Tools in Linux'] (http://williamjturkel.net/2013/06/30/named-entity-recognition-with-command-line-tools-in-linux/), das ich dir wärmstens empfehlen kann, wenn du Namen, Orte und Organisationen in Textdateien automatisch finden, markieren und zählen möchtest...

## Fazit

In dieser Lektion hast du gelernt, dich in der Unix-Shell zurechtzufinden, einige
Dateizählung, -verkettung und -löschung, die Abfrage von Daten nach allgemeinen
Daten nach gemeinsamen Zeichenketten abzufragen, Ergebnisse und abgeleitete Daten zu speichern und Textdaten für eine strenge rechnerische Analyse vorzubereiten.

Das ist nur ein kleiner Ausschnitt dessen, was die Unix-Umgebung zu leisten vermag.
Wir hoffen jedoch, dass diese Sitzung einen Vorgeschmack gegeben hat, der
zu weiteren Untersuchungen und produktiven Spielen anregen.

Vergiss nicht, dass das volle Potenzial der Tools erst dann zum Tragen kommt
erst dann zum Vorschein kommen, wenn du diese Fähigkeiten in echte Projekte einbindest. Nichtsdestotrotz,
die Möglichkeit, Tausende von Dateien zu manipulieren, zu zählen und zu durchsuchen, ist äußerst nützlich.
Selbst eine große Sammlung von Dateien, die keine alphanumerischen Datenelemente enthalten
nummerische Datenelemente enthalten, wie z. B. Bilddateien, lassen sich leicht sortieren, auswählen und abfragen.
der Metadaten, die in jedem Dateinamen enthalten sind.
Wenn das keine Voraussetzung für die Arbeit mit Unix ist, solltest du dir die Zeit nehmen
Daten auf konsistente und vorhersehbare Weise zu strukturieren, ist
ist sicherlich ein wichtiger Schritt, um das Beste aus den Unix
Befehle zu nutzen. Und wenn du einen Weg findest, die Unix-Shell regelmäßig zu benutzen - vielleicht
vielleicht nur zum Kopieren oder Ändern von Dateien - hältst du die Grundlagen frisch, sodass du
das nächste Mal, wenn du die Unix-Shell für komplexere Befehle verwenden musst,
brauchst du sie nicht noch einmal neu zu lernen.

## Referenzen

James Baker und Ian Milligan, 'Counting and mining research data with Unix', *The Programming Historian* ([2014](https://programminghistorian.org/lessons/research-data-with-unix))

Ian Milligan und James Baker, 'Introduction to the Bash Command Line', *The Programming Historian* ([2014](https://programminghistorian.org/lessons/intro-to-bash))

William J. Turkel, 'Named Entity Recognition with Command Line Tools in Linux' ([30. Juni 2013](http://williamjturkel.net/2013/06/30/named-entity-recognition-with-command-line-tools-in-linux/)). Der Abschnitt 'NER-Demo' ist hiervon abgeleitet und steht unter einer [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-nc-sa/3.0/).

William J. Turkel, 'Basic Text Analysis with Command Line Tools in Linux' ([15. Juni 2013](https://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/)). Die Abschnitte "Einen Text greifen, ihn bereinigen" und "Einen Text auseinanderziehen, Worthäufigkeiten zählen" sind hiervon abgeleitet und werden unter einer [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-nc-sa/3.0/) geteilt.
