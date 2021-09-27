---
Titel: "Mit Schleifen das Langweilige automatisieren"
Lehre: 20
Übungen: 10
Fragen:
- "Was ist eine Schleife?"
- "Wie kann eine Schleife verwendet werden, um eine Aufgabe zu wiederholen?
Zielsetzungen:
- "Erstellen Sie ein Konzept dafür, wie Schleifen zur Wiederholung von Aufgaben verwendet werden können".
- "Implementieren Sie eine Schleife, um mehrere Dateien umzubenennen"
Schlüsselpunkte:
- "Schleifen sind die Grundlage für intelligenteres Arbeiten mit der Kommandozeile"
- "Schleifen helfen uns, das Gleiche (oder Ähnliche) mit einem Haufen von Gegenständen zu tun".
- Die Anführungszeichen sind nicht immer nötig, aber gute Praxis um Gefahren entgegenzuwirken - in diesem Fall ginge es auch ohne
---
### Eine For-Loop schreiben

**For Loops** sind eine einfach Art der Automatisierung, da sie es uns ermöglichen
Befehle wiederholt auszuführen. Das erspart uns außerdem jede Menge Schreibarbeiten (und Schreibfehlern).

Was wir gleich machen werden lässt sich auch auf eine sehr große Anzahl von Dateien übertragen. Wir machen das gleich
in einem sehr kleinen Beispiel, dennoch kann es genauso für einen Ordner mit zehntausenden Dateien verwendet werden, die man 
alle auf einmal umwandeln könnte.

Was man in einer Schleife macht ist, 
man nimmt eine Liste von Sachen und definiert eine Sammlung von Aktionen und sagt, rolle diese Aktionen auf die Liste der Sachen aus.

Dazu werden wir jetzt ein paar Dummy Dateien mit dem Befehl "touch" erstellen.

Lassen Sie uns zuerst diese Dateien erstellen:

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
