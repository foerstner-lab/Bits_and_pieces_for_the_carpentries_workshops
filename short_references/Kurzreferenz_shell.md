# Shell-Kurzreferenz

## Syntax
```$ programm [-Optionen] [Argumente]```

**Optionen:**
* Optionen ändern das Verhalten von Programmen
* beginnen mit einem Minus (-)

**Argumente:**
* liefern dem Programm Informationen die von ihm bearbeitet werden

## Befehle
| Befehl                         | Aktion                                         |
|--------------------------------|------------------------------------------------|
| ```pwd```                          | zeigt aktuellen Ordner                         |
| ```ls```                           | listet alle Dateien und Ordner auf             |
| ```cd <Zielordner>```              | wechselt in den Zielordner                     |
| ```touch <Dateiname>```            | erstellt oder updatet Datei                    |
| ```head <Dateiname>```             | gibt die ersten 10 Zeilen der Datei aus        |
| ```tail <Dateiname>```             | gibt die letzten 10 Zeilen der Datei aus       |
| ```mv <Datei1> <Datei2>```         | verschiebt Datei1 und speichert sie als Datei2 |
| ```cp <Dateiname1> <Dateiname2>``` | kopiert Datei                                  |
| ```rm <Dateiname>```               | löscht Datei                                   |
| ```echo "Text"```                 | gibt Text in die Shell aus                     |
| ```wc <Dateiname>```            | zählt Zeilen, Wörter, Zeichen in Datei         |
| ```mkdir <Verzeichnisname>```     | erstellt Ordner                                |
| ```cat <Dateiname>```     | zeigt Inhalt von Datei an                                |

Weitere Hilfe

| Befehl            | Aktion                 |
|-------------------|------------------------|
| ```<Befehl> --help``` | zeigt Hilfe für Befehl |
| ```<Befehl> -h```     | zeigt Hilfe für Befehl |
|  ```man <Befehl>```    | zeigt Befehl Handbuch  |

## Programm Umleitungen

Die Ausgabe von Programmen muss nicht immer in der Shell ausgegeben, sondern kann auch umgeleitet werden.

| Operator | Aktion                                        | Beispiel       |
|----------|-----------------------------------------------|----------------|
| ```>```  | Umleiten der Ausgabe in eine Datei            | ```ls > datei.txt``` |
| <code>&#124;</code>|Umleiten der Ausgabe in ein weiteres Programm  | <code> wc -l *.tsv &#124; sort -n </code>|

## Tastaturkürzel
| Kürzel            | Aktion                                   |
|-------------------|:-----------------------------------------|
| TAB               | Autovervollständigung                    |
| Pfeiltaste hoch   | springt zum vorherigen Befehl            |
| Strg + a          | Cursor springt zum Zeilenanfang          |
| Strg + e          | Cursor springt zum Zeilenanende          |
| Strg + l          | leert den Inhalt des Shell Fensters      |
| Strg + c          | bricht Eingabe oder laufenden Prozess ab |
| Strg + k          | löscht die Eingabe nach dem Cursor       |
| Strg + u          | löscht die Eingabe vor dem Cursor        |
| Strg + y          | fügt Zwischenablage ein                  |

## for-Schleifen

```
$ for NAME in "Jo" "Meg" "Beth" "Amy"
> do
>    echo $NAME
> done
```


([CC-BY](https://creativecommons.org/licenses/by/3.0/de/) Felix Langer und Konrad Förstner)
