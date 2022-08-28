---
Titel: "Durch das Dateisystem navigieren"
Lehre: 20
Übungen: 10
Fragen:
- "Wie bewegen Sie sich in der Shell durch das Dateisystem?
Ziele:
- "Benutzen Sie Shell-Befehle, um mit Verzeichnissen und Dateien zu arbeiten": "Wie bewegen Sie sich im Dateisystem in der Shell?
- "Verwenden Sie Shell-Befehle, um Daten zu finden und zu manipulieren"
Schlüsselpunkte:
- "Zu wissen, wo Sie sich in Ihrer Verzeichnisstruktur befinden, ist der Schlüssel zur Arbeit mit der Shell".
---
## In der Shell navigieren

Wir beginnen mit den Grundlagen der Navigation in der Unix-Shell.

Beginnen wir damit, die Shell zu öffnen. Dann siehst du wahrscheinlich ein schwarzes oder weißes Fenster mit einem blinkenden Cursor neben einem Dollarzeichen.
Das ist unsere Befehlszeile, und das "$" ist die Eingabeaufforderung, um zu zeigen, dass das System bereit für unsere Eingaben ist.
Das Aussehen der Eingabeaufforderung variiert von System zu System, je nachdem, wie das System konfiguriert wurde.
Andere übliche Prompts sind die Zeichen `%` oder `#`, aber wir werden in dieser Lektion `$` verwenden, um den Prompt allgemein darzustellen.

Wenn du in der Shell arbeitest, befindest du dich immer *irgendwo* im Dateisystem deines Computers
Dateisystem, in einem Ordner (Verzeichnis). Deshalb werden wir zunächst herausfinden
herauszufinden, wo wir uns befinden, indem wir den Befehl `pwd` verwenden, den du immer dann
wo du dich befindest. Er steht für "print working directory" und das Ergebnis des
Befehls wird auf deiner Standardausgabe, also dem Bildschirm, ausgegeben.

Gib `pwd` ein und drücke die Eingabetaste, um den Befehl auszuführen
(Beachte, dass das `$`-Zeichen verwendet wird, um einen Befehl anzuzeigen, der an der Eingabeaufforderung eingegeben werden soll,
 Wir geben aber nie das "$"-Zeichen selbst ein, sondern nur das, was danach kommt.):

~~~
$ pwd
~~~

~~~
/Users/muellerr
~~~


Die Ausgabe wird ein Pfad zu Ihrem Homeverzeichnis (home directory) sein. Lasst uns überprüfen, ob wir ihn erkennen
indem wir uns den Inhalt des Verzeichnisses ansehen. Um das zu tun, benutzen wir den Befehl `ls`. 
Dies steht für "list" und das Ergebnis ist ein Ausdruck des gesamten Inhalts des Verzeichnisses:

~~~
$ ls
~~~

~~~
Applications Documents    Library      Music        Public
Desktop      Downloads    Movies       Pictures
~~~


Vielleicht möchten wir mehr Informationen als nur eine Liste von Dateien und Verzeichnissen.
Wir können dies erhalten, indem wir verschiedene **Flags** (auch bekannt als  `Parameter`, oder `Argumente`), die zu unseren Grundbefehlen passen.
Argumente verändern die Funktionsweise des Befehls.

Wenn wir `ls -l` eingeben und die Eingabetaste drücken, gibt der Computer eine Liste von Dateien zurück, die folgendes enthält:
die Größe der Dateien in Bytes, das Datum ihrer Erstellung oder letzten Änderung und den Dateinamen.

~~~
$ ls -l
~~~

~~~
total 0
drwx------+  6 riley  staff   204 Jul 16 11:50 Desktop
drwx------+  3 riley  staff   102 Jul 16 11:30 Documents
drwx------+  3 riley  staff   102 Jul 16 11:30 Downloads
drwx------@ 46 riley  staff  1564 Jul 16 11:38 Library
drwx------+  3 riley  staff   102 Jul 16 11:30 Movies
drwx------+  3 riley  staff   102 Jul 16 11:30 Music
drwx------+  3 riley  staff   102 Jul 16 11:30 Pictures
drwxr-xr-x+  5 riley  staff   170 Jul 16 11:30 Public
~~~


Im alltäglichen Gebrauch sind wir eher an Maßeinheiten wie Kilobyte, Megabyte und Gigabyte gewöhnt.
Glücklicherweise gibt es ein weiteres Flag `-h` (steht für **human readable**, das, wenn es zusammen mit der Option -l verwendet wird, Einheiten-Suffixe verwendet:
Byte, Kilobyte, Megabyte, Gigabyte, Terabyte.

Also, indem Sie `ls -lh` tippen und eingeben, erhalten wir eine Ausgabe in einem von Menschen lesbaren Format.

~~~
$ ls -lh
~~~

~~~
total 0
drwx------+  6 riley  staff   204B Jul 16 11:50 Desktop
drwx------+  3 riley  staff   102B Jul 16 11:30 Documents
drwx------+  3 riley  staff   102B Jul 16 11:30 Downloads
drwx------@ 46 riley  staff   1.5K Jul 16 11:38 Library
drwx------+  3 riley  staff   102B Jul 16 11:30 Movies
drwx------+  3 riley  staff   102B Jul 16 11:30 Music
drwx------+  3 riley  staff   102B Jul 16 11:30 Pictures
drwxr-xr-x+  5 riley  staff   170B Jul 16 11:30 Public
~~~


Wir haben jetzt sehr viel Zeit in unserem Heimatverzeichnis verbracht.
Lass uns woanders hingehen. Wir können das mit dem Befehl `cd` oder Change Directory tun:

~~~
$ cd Desktop
~~~


Hier fällt uns auf, dass der Befehl gar nichts ausgegeben hat (no news is good news). Lassen Sie uns das mit `pwd` überprüfen:

~~~
$ pwd
~~~

~~~
/Users/riley/Desktop
~~~


Wäre jedoch etwas schief gegangen, hätte das Kommando es uns gesagt. Lasst uns das testen, 
indem wir versuchen, in ein nicht existierendes Verzeichnis zu wechseln:

~~~
$ cd "Teuflischer Plan"
~~~

~~~
bash: cd: Teuflischer Plan: No such file or directory
~~~


Wie wir sehen, ich habe leider keinen teuflischen Plan. Was wir hier auch sehen können ist, 
dass ich den Namen in Anführungszeichen gesetzt habe. Damit sage ich der Shell dass es sich um einen einzigen Ordner handelt und nicht zwei verschiedene Argumente. 

Wir haben jetzt gesehen, dass wir uns in die tiefen des Verzeichnisses bewegen können. 
Wenn wir zurückgehen wollen, können wir `cd ..` eingeben. Das ".." steht für den Elternordner darüber.
Das verschiebt uns ein Verzeichnis "nach oben" und bringt uns wieder dorthin zurück, wo wir angefangen haben.
**Wenn wir jemals komplett verloren gehen, bringt der Befehl `cd` ohne Argumente
uns direkt zurück zum Homeverzeichnis, dem Ort, an dem wir angefangen haben.**

> ## Vorheriges Verzeichnis
> Um zwischen zwei Verzeichnissen hin und her zu wechseln, benutzen wir `cd -`.

Die Fähigkeit, im Dateisystem zu navigieren, ist sehr wichtig für die effektive Nutzung der Unix-Shell.
Da wir immer komfortabler werden, können wir sehr schnell zu dem Verzeichnis gelangen, das wir wollen.

## Challenge
>
> Bewege dich auf dem Computer, gewöhne dich daran, dich in Verzeichnissen zu bewegen und sie zu verlassen,
> Sieh dir an, wie verschiedene Dateitypen in der Unix-Shell erscheinen. Benutze unbedingt die Befehle "pwd" und
> `cd` und die verschiedenen Flags für den Befehl `ls`, die du bisher gelernt hast.
>
> Wenn du mit Windows arbeitest,
> versuche auch `explorer .` einzugeben, um den Explorer für das aktuelle Verzeichnis zu öffnen
> (der einzelne Punkt bedeutet "aktuelles Verzeichnis"). Wenn du mit einem Mac arbeitest,
> versuche es mit `open .` und unter Linux mit `xdg-open .`, um den grafischen Dateimanager zu öffnen.

## Hilfe erhalten
>
> Verwenden Sie den Befehl `man`, um die Manual-Seite (Dokumentation) für einen Shell-Befehl aufzurufen.
> Zum Beispiel zeigt `man ls` alle Argumente an, die Ihnen zur Verfügung stehen - das spart
> dass Sie sich an sie alle erinnern! Versuchen Sie dies für jedes Kommando, das Sie bisher gelernt haben.
> Verwenden Sie die <kbd>Leertaste</kbd>, um durch die Handbuchseiten zu navigieren. Benutzen Sie <kbd>q</kbd> jederzeit zum Beenden.
>
> ***Hinweis*: dieser Befehl ist nur für Mac- und Linux-Benutzer**. Er funktioniert nicht direkt für Windows-Benutzer.
> Wenn Sie Windows benutzen, können Sie nach dem Shell-Befehl auf [http://man.he.net/](http://man.he.net/) suchen,
> und sehen Sie sich die zugehörige Handbuchseite an. In einigen Systemen wird der Befehlsname gefolgt von `--help` funktionieren, z.B. `ls --help`.

## Challenge: Erfahre mehr über fortgeschrittene `ls`-Befehle
>
> Finde mit Hilfe der Manual Page heraus, wie du die Dateien in einem
> Verzeichnis nach ihrer Dateigröße sortiert auflistet. Probiere es in verschiedenen Verzeichnissen aus. Kannst du es kombinieren
> mit dem `-l` *Argument* kombinieren, das du vorher gelernt hast?
>
> Danach,
> finde heraus, wie du eine Liste von Dateien nach dem Datum ihrer letzten Änderung ordnen kannst.
> Versuche, Dateien in verschiedenen Verzeichnissen zu ordnen.
>
> > ## Antwort
> >
> > Um Dateien in einem Verzeichnis nach ihrer Dateigröße zu ordnen, in Kombination mit dem Argument `-l`:
> >
> > ~~~
> > ls -lS
> > ~~~
> > 
> >
> > Beachte, dass das "S" **Groß- und Kleinschreibung beachtet!**
> >
> > Um Dateien in einem Verzeichnis nach ihrem letzten Änderungsdatum zu ordnen, in Kombination mit dem Argument "l":
> >
> > ~~~
> > ls -lt
> > ~~~
> > 
> 

