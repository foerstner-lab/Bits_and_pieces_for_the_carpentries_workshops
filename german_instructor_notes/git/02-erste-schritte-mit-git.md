---
Titel: "Erste Schritte mit Git"
Lehre: 20
Übungen: 0
Fragen:
- "Was sind Repositories und wie werden sie erstellt?"
- "Was bedeuten `Adden` und `Commit`?"
- "Wie überprüfe ich den Status meines Repositorys?"
Ziele:
- "Ein Git-Repository erstellen"
- "Änderungen an Dateien mit dem Git-Repository verfolgen"
- "Abfrage des aktuellen Status des Git-Repositorys"
Schlüsselpunkte:
- "Git-Repositories enthalten Metadaten über Dateien unter Versionskontrolle"
- "Mit diesen Metadaten können wir Änderungen an den Dateien über die Zeit verfolgen."
- "Git" verwendet einen zweistufigen Commit-Prozess. Änderungen an Dateien müssen zuerst in den Staging-Bereich eingefügt und dann in das Repository übertragen werden.
---

### Umgang mit Git

Eines der Haupthindernisse für den Einstieg in Git ist die Sprache. Obwohl einige der in Git verwendeten Sprache 
ziemlich selbsterklärend, andere Begriffe sind nicht so klar. Der beste Weg, die Sprache zu lernen - die aus einer 
Anzahl der Verben wie `add`, `commit` und `push` (mit dem Wort 'git' vorangestellt) - ist durch die Benutzung, was wir während dieser 
Lektion. Diese Befehle werden erklärt, während wir vom Einrichten eines neuen versionskontrollierten Projekts bis zur Veröffentlichung 
unsere eigene Website.

### Was machen wir jetz
- Git Repositorium in der Kommandozeile erstellen
- ein paar Änderungen machen
- nach GitHub hochpushen


### Erstellen eines Repositoriums

Wir packen unsere .ipynb Dateien in einen neuen Ordner
Dazu ein 
~~~
cd
~~~
und 
~~~
mkdir python-lesson
~~~
und 
~~~
mv *ipynb python-lesson
~~~

Jetzt wollen wir unseren Git User konfiguieren

~~~
git config --global user.name "<Your-Full-Name>"
git config --global user.email "<your-email-address>"
~~~

Wir werden nun ein leeres Git-Repository erstellen, um Änderungen an unserem Projekt zu verfolgen. Dazu werden wir den git **init** Befehl verwenden, 
was einfach die Abkürzung für *initialisieren* ist.

~~~
$ git init
~~~
{: .bash)
~~~
Initialisiertes leeres Git-Repository in <Ihrem Dateipfad>/hello-world/.git/
~~~
{: .output}

Wenn wir uns jetzt die versteckten Dateien mit ls -a anschauen sehen wir auch ein ".git" was unseren Ordner zum Git Repo macht.

### Anzeige des aktuellen Projektstatus

Wir können den `git status` Befehl ausführen, um den aktuellen Status eines Projektes anzuzeigen. Lass uns das jetzt machen.

~~~
$ Git-Status
~~~
{: .bash)
~~~
Auf Filialmeister
Noch keine Zusagen
nichts zu übergeben (Dateien erstellen/kopieren und "git add" für den Track verwenden)
~~~
{: .output}

Die Ausgabe sagt uns, dass wir uns auf dem Hauptzweig befinden und dass wir nichts zu übergeben haben (keine 
ungespeicherte Änderungen).

### Hinzufügen und Übergeben

Wir werden nun unsere erste Projektdatei erstellen und speichern. Dies ist ein zweistufiger Prozess. Zuerst **fügen wir alle Dateien hinzu, für die 
wir die Änderungen wollen in einem Staging-Bereich speichern, dann **commiten** wir diese Änderungen an das Repository. Dieser zweistufige 
Prozess gibt uns eine Kontrolle darüber, was in einen bestimmten Commit aufgenommen werden soll und was nicht.

Lasst uns eine neue Datei mit dem `touch` Befehl erstellen.
~~~
$ touch README.md
~~~
{: .bash)

Die obige `.md` Erweiterung bedeutet, dass wir uns für das Markdown-Format entschieden haben.

Lassen Sie uns den Status unseres Projekts noch einmal überprüfen.

~~~
$ Git-Status
~~~
{: .bash)
~~~
Auf Filialmeister
Noch keine Zusagen
Ungekennzeichnete Dateien:
  (benutzen Sie "git add <file>..." um in das einzuschließen, was übertragen wird)

    README.md

nichts zum Übertragen hinzugefügt, aber ungetrackte Dateien vorhanden (verwenden Sie "git add" zum Tracken)
~~~
{: .output}

Dieser Status sagt uns, dass git eine neue Datei in unserem Verzeichnis bemerkt hat, die wir noch nicht verfolgen. Mit eingefärbter 
Ausgabe erscheint der Dateiname in rot. Um dies zu ändern, und um Git mitzuteilen, dass wir alle Änderungen, die wir an 
README.md, wir benutzen `git add`.

~~~
$ git add README.md
~~~
{: .bash)

Dies fügt unsere Markdown-Datei zum **Staging-Area** (der Bereich, in dem git nach Dateiänderungen sucht) hinzu. Um dies zu bestätigen, wollen wir wieder `git status` verwenden.

~~~
$ Git-Status
~~~
{: .bash)
~~~
Auf Filialmeister

Noch keine Zusagen

Änderungen, die verpflichtet werden müssen:
  (benutzen Sie "git rm --cached <file>..." zum Unstage)

    neue Datei: README.md
~~~
{: .output}

Wenn wir eine farbige Ausgabe verwenden, werden wir sehen, dass der Dateiname seine Farbe geändert hat (von rot zu grün). Git sagt uns auch, dass dort
ist eine neue Datei, die übergeben werden soll, aber bevor wir das tun, lasst uns der Datei etwas Text hinzufügen.

Wir öffnen die Datei `README.md` mit Nano

~~~
nano README.md
~~~

Nun speichern wir die Datei im Texteditor und überprüfen, ob Git
hat die Veränderungen erkannt.

~~~
$ Git-Status
~~~
{: .bash)
~~~
Auf Filialmeister

Noch keine Zusagen

Änderungen, die verpflichtet werden müssen:
  (benutzen Sie "git rm --cached <file>..." zum Unstage)

	neue Datei: index.md

Änderungen nicht für die Übergabe bereitgestellt:
  (benutzen Sie "git add <file>..." um zu aktualisieren, was übertragen wird)
  (benutzen Sie "git checkout -- <file>..." um Änderungen im Arbeitsverzeichnis zu verwerfen)

	geändert: README.md
~~~
{: .output}

Dies lässt uns wissen, dass Git tatsächlich die Änderungen an unserer Datei entdeckt hat, aber dass es sie noch nicht inszeniert hat, also lasst uns hinzufügen 
die neue Version der Datei in den Bereitstellungsbereich.

~~~
$ git add README.md
~~~
{: .bash)

Jetzt sind wir bereit, unsere ersten Änderungen zu **commiten**. 
Commit ist ähnlich wie das 'Speichern' einer Datei in Git. 
Allerdings bietet ein Commit im Vergleich zum Speichern viel mehr Informationen über die Änderungen, die wir gemacht haben,
und diese Informationen bleiben auch später für uns sichtbar.


~~~
$ git commit -m 'Add README.md'
~~~
{: .bash)
~~~
[master (root-commit) e9e8fd3] index.md hinzufügen
 1 Datei geändert, 1 Einfügen(+)
 Erstellungsmodus 100644 index.md
~~~
{: .output}

Wir können sehen, dass sich eine Datei geändert hat und dass wir eine Einfügung gemacht haben.
Wir können
siehe auch die Commit-Meldung 'Add index.md', die wir mit dem `-m` Flag nach `git commit` hinzugefügt haben.
Die Commit-Nachricht wird benutzt, um eine kurze, beschreibende und spezifische Zusammenfassung dessen aufzuzeichnen, was wir getan haben, um uns später daran zu erinnern, ohne auf die tatsächlichen Änderungen schauen zu müssen.
Wenn wir einfach `git commit` ohne die `-m` Option ausführen, wird Git nano (oder jeden anderen Editor, den wir als `core.editor` konfiguriert haben) starten.
damit wir eine längere Nachricht schreiben können.

Nachdem wir einen Commit gemacht haben, haben wir nun eine permanente Aufzeichnung der Änderungen,
zusammen mit Metadaten darüber, wer die Übergabe gemacht hat und zu welcher Zeit. Das können wir uns auch mit

~~~
git log
~~~
anschauen
