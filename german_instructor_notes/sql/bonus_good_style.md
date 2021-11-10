---
Titel: "Guter Stil
Lehre: 10
Übungen: 0
Fragen:
- "Was ist ein guter SQL-Stil, und wie kann ich mich an SQL-Konventionen halten?
Ziele:
- "Verstehen der Grundlagen für die Erstellung sauberer, lesbarer SQL-Abfragen": "Was ist ein guter SQL-Stil und wie kann ich mich an SQL-Konventionen halten?
Schlüsselpunkte:
- "Es gibt viele Möglichkeiten, eine SQL-Abfrage zu schreiben, aber einige sehen besser aus als andere.
---

## Eine Einführung in guten Stil

Es gibt viele Möglichkeiten, eine SQL-Abfrage zu schreiben, aber einige sehen besser aus als andere. Wenn Sie sich an gute Stilrichtlinien halten, werden Ihre SQL-Abfragen leichter lesbar, besonders wenn Sie sie mit anderen teilen.
Dies sind einige schnelle Tipps, um Ihre SQL-Abfragen sauber aussehen zu lassen.

## Wählen Sie präzise und kurze Spaltennamen

Bei der Wahl der Spaltennamen ist es wichtig, daran zu denken, dass ein großer Teil dessen, was Sie in Ihre Suchanfrage eingeben, aus Ihren Spaltennamen bestehen wird. Wenn Sie einen Spaltennamen wählen, der aus einem oder zwei Wörtern besteht (ohne Leerzeichen!), wird sichergestellt, dass Ihre Abfragen leichter einzugeben und zu lesen sind. Wenn Sie Leerzeichen in Ihre Spaltennamen einfügen, erhalten Sie eine Fehlermeldung, wenn Sie versuchen, Ihre Abfragen auszuführen. Wir empfehlen daher die Verwendung von CamelCase oder An_Underscore.

## Großschreibung (manchmal) ist wichtig

In Abschnitt zwei haben wir darüber gesprochen, dass die Groß-/Kleinschreibung von SQL-Schlüsselwörtern/Befehlen nicht berücksichtigt wird ("Wir haben die Wörter SELECT und FROM groß geschrieben, da es sich um SQL-Schlüsselwörter handelt. Dies macht für den SQL-Interpreter keinen Unterschied, da es die Groß-/Kleinschreibung nicht berücksichtigt, aber es trägt zur Lesbarkeit bei und gilt daher als guter Stil"). Aber wussten Sie, dass in einigen SQL-Programmen, je nach Einstellung, Tabellen- und Spaltennamen spaltenabhängig sind? Wenn Ihre Abfrage nicht funktioniert, überprüfen Sie die Groß-/Kleinschreibung.

## Lesbarkeit

Wie Sie vielleicht bemerkt haben, sind wir in der Lage, unsere Anfrage in eine oder mehrere Zeilen zu schreiben. Der allgemeine Konsens mit SQL ist, dass es leichter lesbar wird, wenn man es auf mehreren Zeilen in Komponenten zerlegen kann. Wenn Sie mehrere Zeilen und Einrückungen verwenden, können Sie etwas, das so aussieht, umdrehen:

~~~~~EINRÜCKUNGSBEISPIEL~~~~~

In etwas, das so aussieht:

~~~~~EINFÜGEN BEISPIEL~~~~~

In einigen Programmen (wie z.B. MySQL) wird es Werkzeuge geben, die Ihren Code automatisch "verschönern" können, um die Lesbarkeit zu verbessern.

## Kommentieren

Sie können Kommentare zu Ihren SQL-Abfragen mit einem Hashtag "#" hinzufügen. Das ist eine großartige Gelegenheit für Sie, sich selbst oder anderen gegenüber auszudrücken, was Sie tun. Es ist im Wesentlichen eine Möglichkeit, sich Notizen in Ihrem SQL zu machen. Um einen Kommentar zu erstellen, beginnen Sie in einer neuen Zeile mit einem Hashtag und setzen dann Ihre SQL-Abfrage in der nächsten Zeile fort.
~~~~~EINFÜGEN BEISPIEL~~~~~
