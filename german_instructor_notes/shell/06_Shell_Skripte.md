---
Titel: "Skripte in der Shell schreiben".
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich Skripte aus der Kommandozeile heraus mit einem Texteditor schreiben?
- "Wie kann ich die Skripte in der Shell ausführen?"
Ziele:
- "Mit Nano von der Kommandozeile aus arbeiten".
- "sh-Dateien von der Kommandozeile aus ausführen"
- "Zeilen auskommentieren".

Schlüsselpunkte:
- "Die Shell kann zum Erstellen von Skripten benutzt werden und so Prozesse automatisieren und reproduzierbar machen".
---
## ein Shell Skript in Nano schreiben

Jetzt lernen wir eine Möglichkeit für Reproduzierbarkeit kennen. Wieder einmal können wir mit kleinem Aufwand 
mit Plain Text-Dateien arbeiten.
Das Shell Skript ist auch nichts anderes als eine solche Plaintext Datei, in der wir Befehle definieren können 
und diese dann ausführen lassen.

Dafür brauchen wir einen Text-Editor. Ihr kennt vielleicht auch Editoren wie Notepad oder 
Notepad ++. Wenn man sehr viel mit solchen Dingen arbeitet, sollte man sich einen mächtigen
Texteditor aussuchen. Wir haben auch eine Liste an Text-Editoren in unserem Pad hinterlegt.

Wir werden jetzt "nano" benutzen, ein relativ kleine Editor, dennoch gut genug für das was wir jetzt tun möchten 
und auch bei uns allen in der Bash dabei.

~~~
$ nano mein_bash_skript.sh
~~~

Wir nehmen den Begriff "nano" und versehen ihn mit einem Argument, dass meine neue Datei definiert. Mit Enter 
rufen wir dann diese Datei in dem nano Texteditor auf. Mit der Endung **sh** legen wir fest, dass es sich 
um ein shell script handelt.

In Nano können wir jetzt Befehle schreiben

~~~
echo "hallo zusammen"
~~~

Um die Änderung zu Speichern drücken wir <kbd>Ctrl</kbd> + <kbd>o</kbd>. Nano fragt uns ob wen Dateinamen behalten wollen und 
wir bestätigen mit <kbd>Enter</kbd>.

Wir können die Editor jetzt wieder verlassen mit <kbd>Ctrl</kbd> <kbd>x</kbd>.  

Jetzt können wir unser Skript ausführen.

~~~
$ bash mein_bash_skript.sh
~~~
{: .bash}

Als Output wird uns unser Echo-Befehl in der unteren Zeile angezeigt.

~~~
$ hallo zusammen
~~~
{: .output}

Herzlichen Glückwunsch. Wir haben das erste mal programmiert!

Machen wir folgendes. Gehen wir noch einmal in unsere Datei. Wir können uns den Befehl wieder mit Pfeiltaste nach Oben zurückholen.

~~~
$ nano mein_bash_skript.sh
~~~

## Kommentare nutzen

Idealerweise beschreiben wir unsere Skripte so gut, dass wir sie zu einem späteren Zeitpunkt immer noch verstehen. Oder auch eine andere Person, 
die die Befehle zum ersten Mal sieht. Um das zu tun können wir mit einem vorangesetzten <kbd>#</kbd> Kommentare in unseren Code einfügen.  

~~~
# Mit diesem Skript begrüße ich euch
echo "hallo zusammen"
~~~

Der Hashtag sagt der Shell, dass diese Zeile bei der Codeausführung ignoriert werden soll. Andernfalls würden wir eine Fehlermeldung bekommen, 
weil die Bash sagen wird, "Diesen Befehl verstehe ich nicht".

## For Schleifen im Shell Skript

Auch hier können wir unsere For-Schleife mit einbauen.

~~~
# Mit diesem Skript begrüße ich euch
echo "hallo zusammen"

for FILE in *txt
do
    echo "$FILE"
    head -n 2 "$FILE"
    tail -n 2 "$FILE"
done
~~~

Wir speichern unsere Datei erneut ab. Wenn wir sie jetzt ausführen, werden uns zusätzlich die ersten und letzten beiden Zeilen 
aller txt-Dateien in unserem shell-lesson Ordner angezeigt.

~~~
hallo zusammen
829-0.txt
The Project Gutenberg eBook, Gulliver's Travels, by Jonathan Swift

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.

33504-0.txt
The Project Gutenberg EBook of Opticks, by Isaac Newton

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.

pg514.txt
The Project Gutenberg EBook of Little Women, by Louisa May Alcott

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
~~~

Damit haben wir unsere Shell-Skript geschrieben. Hiermit können wir nachhaltig und reproduzierbar Prozesse ablegen.
Das können z. B. auch das Herunterladen von Statistiken sein oder das Umwandeln von Dateien. Außerdem haben wir die damit auch die 
Möglichkeit unsere Prozesse leicht mit anderen zu teilen.



