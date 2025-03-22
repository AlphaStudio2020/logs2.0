# Discord Logger Bot

## Beschreibung
Der Discord Logger Bot protokolliert verschiedene Aktivitäten in einem Discord-Server und speichert diese in separaten Log-Dateien. Er reagiert nicht auf Bots und speichert alle Informationen lokal.

## Funktionen
- **Chat-Logging**: Speichert alle gesendeten Nachrichten in kanal-spezifischen Dateien.
- **Gelöschte Nachrichten**: Protokolliert gelöschte Nachrichten mit Inhalt, Autor und Kanal.
- **Sprachkanal-Aktivitäten**: Loggt, wenn Nutzer einem Sprachkanal beitreten, ihn verlassen oder wechseln.
- **Rollenänderungen**: Speichert, wenn Nutzer Rollen hinzugefügt oder entfernt bekommen.
- **Benutzeraktionen**:
  - Beitritt zum Server
  - Verlassen des Servers
  - Bann und Entbannung von Mitgliedern

## Installation
1. Stelle sicher, dass Python 3.x installiert ist.
2. Installiere die benötigten Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Erstelle eine `.env`-Datei oder trage das Bot-Token direkt in den Code ein.
4. Starte den Bot:
   ```bash
   python bot.py
   ```

## Konfiguration
- **Log-Dateien**: Alle Logs werden im `logs/`-Ordner gespeichert.
- **Dateinamen**:
  - `chat_CHANNELNAME.log` für Chat-Nachrichten
  - `deleted_messages.log` für gelöschte Nachrichten
  - `voice.log` für Sprachkanal-Aktivitäten
  - `roles.log` für Rollenänderungen
  - `user.log` für Benutzeraktionen

## Hinweise
- Der Bot benötigt Administratorrechte oder entsprechende Berechtigungen für das Logging.
- Er postet keine Logs in Discord, sondern speichert sie nur lokal.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht.

