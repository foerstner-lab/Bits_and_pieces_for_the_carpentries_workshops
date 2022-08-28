---
Titel: "Das Mühsame mit Schleifen automatisieren"
Unterricht: 20
Übungen: 10
Fragen:
- "Was ist eine Schleife?"
- "Wie kann eine Schleife verwendet werden, um eine Aufgabe zu wiederholen?"
Ziele:
- "Beschreibe, wie Schleifen verwendet werden können, um Aufgaben zu wiederholen".
- "Implementiere eine Schleife, um mehrere Dateien umzubenennen".
Kernpunkte:
- "Schleifen sind die Grundlage für intelligenteres Arbeiten mit der Kommandozeile"
- Schleifen helfen uns dabei, dieselben (oder ähnliche) Dinge mit einer Reihe von Objekten zu tun"
---
### Eine For-Loop schreiben

**For Loops oder Schleifen** sind der Schlüssel zur Produktivitätssteigerung durch Automatisierung, denn sie ermöglichen es uns, Befehle wiederholt auszuführen.
Befehle wiederholend auszuführen. Ähnlich wie bei Platzhaltern und der Tabulatorvervollständigung reduziert die Verwendung von Schleifen auch die
Tipparbeit (und Tippfehler).
Nehmen wir an, wir haben mehrere hundert Dokumentendateien mit den Namen "projekt_1825.txt", "projekt_1863.txt", "XML_projekt.txt" und so weiter.
Wir möchten diese Dateien ändern, aber auch eine Version der Originaldateien speichern und die Kopien so benennen
Backup_Projekt_1825.txt" und so weiter.

Dafür können wir eine **Schleife** verwenden.
Hier ist ein einfaches Beispiel, das nacheinander eine Sicherungskopie von vier Textdateien erstellt.

Erstellen wir zuerst diese Dateien:

~~~
$ touch a.doc b.doc c.doc d.doc
$ ls
~~~
Dadurch werden vier leere Dateien mit diesen Namen erstellt.

Jetzt werden wir eine Schleife verwenden, um eine Backup-Datei zu erstellen. 
Dabei könnten wir jetzt
~~~
$ cp a.doc backup-a.doc 
$ ls
~~~

benutzen. Das ist bei 4 Dateien noch im Rahmen, bei 10 Dateien wird es nervig, bei 50 Dateien schon eher hässlich und bei 1000 hat man keine Lust mehr darauf.

Deshalb nutzen wir jetzt unsere For Loop.
Wir können dies auf unser Beispiel so anwenden:


~~~
$ for FILE in a.doc b.doc c.doc d.doc
> do
>    echo $FILE
>    cp "$FILE" backup_"$FILE"
> done
~~~
{: .bash}

- Mit "for" sagen wir der Shell, dass ein Befehl in einer Liste wiederholt werden muss.
- Mit FILE benennen wir unsere Variable. Hier könnte auch Lasagne stehen, aber wir versuchen hier immer einen Namen zu wählen,
der zu unseren Listen-Elementen passt, damit wir uns besser erinnern können, was hier passiert und auch andere unseren Befehl besser verstehen.
- a.doc b.doc c.doc ist unsere Liste.
- Wir drücken Enter und es ändert sich ein Zeichen, das sagt uns dass etwas kommen muss und die Schleife noch nicht abgeschlossen ist.
- Wir eröffnen dann unsere Aktion mit "do".
- Jetzt können wir schreiben was wir machen wollen und nehmen dafür unser "echo". Echo gibt uns einen String aus.
- Durch das Dollarzeichen sagen wir der Shell das jetzt unsere Variable, die wir oben definiert haben, kommt.
- Dann drücke ich Enter und kann einen weiteren Befehl angeben. Das mache ich hier mit cp.
- Mit "done" beende ich dann meine Schleife und sie wird ausgeführt.

Durch die Ausgabe sehe ich unseren Echo-Befehl und durch 

~~~
$ ls
~~~

sehen wir unsere backup Dateien.
Das gleiche kann ich auch mit Wildcards machen.

~~~
$ for FILE in *.doc
> do
>    echo $FILE ist eine tolle Datei!
>    echo "-------------------------"
> done
~~~
{: .bash}

Welche Dateien werden jetzt angesprochen? Genau auf alle acht Dateien!
Damit haben wir das Prinzip der For-Schleifen abgeschlossen.

Wie schon erwähnt, das hier war ein kleines Dummy-Experiment, kann aber durchaus mit nur wenigen Zeilen Code
auf eine Vielzahl von Dateien angewendet werden und gibt uns ein super Möglichkeit schneller zu Arbeiten.

> ## Zeichen in der Prompt
>
> Der Shell-Prompt wechselt von `$` zu `>` und wieder zurück, während wir
> Tippen in unserer Schleife. Der zweite Prompt, `>`, ist anders, um uns daran zu erinnern
> uns daran zu erinnern, dass wir noch nicht mit der Eingabe eines vollständigen Befehls fertig sind. Ein Semikolon, `;`,
> kann verwendet werden, um zwei Befehle zu trennen, die in einer einzigen Zeile stehen.

> ## Challenge: For-Schleife Lückentext
> Fülle die Leerzeichen in der folgenden for-Schleife aus, um den Namen, die erste Zeile und die letzte Zeile
> jeder Textdatei im aktuellen Verzeichnis ausgeben. **Ihr findet die For-Schleife im Pad**
>
> ```
> ___ FILE in *.txt
> __
> echo "_FILE"
> head -n 1 _______
> ____ __ _ _______
> ____
> ```
>
> > ## Lösung
> > ```
> > for FILE in *.txt
> > do
> > echo "$FILE"
> > head -n 1 "$FILE"
> > tail -n 1 "$FILE" 
> > done
> > ```
