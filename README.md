# 🎲 Number Guessing Game in Python

Dieses kleine Python-Programm ist ein **Zahlenratespiel**, bei dem der Computer zufällig eine Zahl innerhalb eines vom Spieler gewählten Bereichs generiert.  
Der Spieler muss dann die richtige Zahl erraten – mit Hinweisen, ob seine Eingabe zu hoch oder zu niedrig ist.

---

## 📌 Features
- Benutzer kann den Zahlenbereich (`low` bis `high`) selbst festlegen.
- Zufällige Zahl wird automatisch generiert.
- Beliebig viele Versuche, bis die richtige Zahl erraten wird.
- Feedback nach jedem Versuch:
  - _"Your number is too low baby"_ – Zahl ist zu klein
  - _"Your number is too high baby"_ – Zahl ist zu groß
  - _"You got it babygirl."_ – richtige Zahl erraten 🎉

---

## ▶️ Installation & Ausführung

1. Stelle sicher, dass **Python 3** auf deinem System installiert ist.  
   Überprüfen mit:

   ```bash
   python --version
   ```

   oder

   ```bash
   python3 --version
   ```

2. Lade das Skript herunter oder clone die Repository, z. B.:

   ```bash
   git clone <Link von meiner Repository>
   ```

3. Starte das Spiel mit:

   ```bash
   py index.py
   ```

---

## 🕹️ Spielablauf

1. Nach dem Start wirst du nach dem unteren Grenzwert gefragt.  
   Beispiel:  

   ```text
   Your lowest number: 1
   ```

2. Danach nach dem oberen Grenzwert.  
   Beispiel:  

   ```text
   Your highest number: 100
   ```

3. Das Programm wählt nun eine Zufallszahl zwischen diesen Grenzen.

4. Du gibst deine Vermutung ein:  

   ```text
   Guess 1: 50
   ```

---

## 💡 Beispiel

```text
Welcome to Number guessing game in Python!
Type which range you want to play: 
Your lowest number: 1
Your highest number: 10
L:1
H:10
Guess 1: 5
false. Try again
Your number is too low baby
Guess 2: 8
false. Try again
Your number is too high baby
Guess 3: 7
You got it babygirl.
Target: 7
```

---

## 📚 Anforderungen

- Python 3.x
- Keine zusätzlichen Bibliotheken (nur `random`, in der Standardbibliothek enthalten)
