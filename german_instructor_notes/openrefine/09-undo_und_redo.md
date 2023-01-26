---
Titel: "Transformationen - Rückgängig und Wiederholen"
Unterricht: 5
Übungen: 0
Fragen:
- "Wie funktionieren die Funktionen Rückgängig und Wiederherstellen?"
Ziele:
- "Erkläre, wie man Rückgängig und Wiederherstellen benutzt, um seine Schritte zurückzuverfolgen"
Stichpunkte:
- "Du kannst Rückgängig und Wiederholen verwenden, um deine Schritte zurückzuverfolgen.
- "Mit den Funktionen 'Extrahieren' und 'Anwenden' kannst du einen Satz von Schritten speichern und auf einen neuen Satz von Daten anwenden"
---

## Rückgängig und Wiederholen
Mit OpenRefine kannst du alle Schritte, die du beim Bereinigen der Daten gemacht hast, rückgängig machen und wiederholen. 
Das bedeutet, dass du jederzeit Transformationen ausprobieren und bei Bedarf "rückgängig" machen kannst. Die Art und Weise, 
wie OpenRefine die von dir durchgeführten Schritte aufzeichnet, ermöglicht es dir sogar, die Schritte, die du an einem Datensatz 
durchgeführt hast, durch Kopieren und Einfügen auf einen anderen Datensatz anzuwenden.

Die Optionen "Rückgängig machen" und "Wiederherstellen" werden über das linke Bedienfeld aufgerufen.

Im Feld Rückgängig/Wiederherstellen sind alle Schritte aufgelistet, die du bisher gemacht hast. 
Um Schritte rückgängig zu machen, klickst du in der Liste auf den letzten Schritt, den du beibehalten möchtest. 
Dadurch werden alle Änderungen, die seit diesem Schritt vorgenommen wurden, automatisch rückgängig gemacht.

Die verbleibenden Schritte werden weiterhin in der Liste angezeigt, sind aber ausgegraut und du kannst sie erneut anwenden, 
indem du auf den letzten Schritt klickst, den du anwenden möchtest.

Wenn du jedoch eine Reihe von Schritten "rückgängig" machst und dann mit neuen Transformationen beginnst, 
verschwinden die ausgegrauten Schritte und du hast nicht mehr die Möglichkeit, diese Schritte "wiederherzustellen".

Wenn du eine Reihe von Schritten speichern möchtest, um sie später wieder anzuwenden, z. B. in einem anderen Projekt, 
kannst du auf die Schaltfläche ``Extract`` klicken. Damit kannst du die Schritte auswählen, die du speichern möchtest, 
und den Code für diese Schritte in einem Format namens "JSON" extrahieren. Du kannst das extrahierte JSON kopieren und 
als einfache Textdatei speichern (z. B. in Notepad). Wenn du OpenRefine Version 3.6.0 oder höher verwendest, kannst du auch
auf die Schaltfläche ``Exportieren`` im Fenster "Vorgangsverlauf extrahieren" klicken, um einen Speicherdialog zu öffnen und 
das JSON direkt zu speichern, anstatt es erst in eine Textdatei zu kopieren.

Um eine Reihe von Schritten, die du kopiert oder in diesem "JSON"-Format gespeichert hast, anzuwenden, 
klicke auf die Schaltfläche ``Apply `` und füge das JSON ein. Auf diese Weise kannst du Transformationen 
zwischen Projekten und mit anderen Personen austauschen.

Wenn du das Projekt das nächste Mal öffnest, kannst du auf den gesamten Verlauf deiner Schritte zugreifen 
und sie auf dieselbe Weise rückgängig machen oder wiederherstellen.
