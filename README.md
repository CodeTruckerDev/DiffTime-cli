# DiffTime-cli

A tiny CLI tool inspired by the Unix philosophy that calculates the difference between two dates.

The order of the dates does not matter.


Prosty skrypt konsolowy do obliczania różnicy czasu między dwoma momentami.  
Napisany głównie dla kierowców – szybkie liczenie przerwy między godzinami rozpoczęcia i zakończenia jazdy.

Powstał jako lekka wersja mobilnego [DiffTime](https://github.com/CodeTruckerDev/DiffTime) – do szybkiego użycia w trasie na laptopie lub w terminalu.
Żadnych bajerów, żadnych zależności, tylko działający kod.

## Co robi

- Przyjmuje dwa argumenty w formacie: DD-MM HH:MM  
  (rok nie jest wymagany – liczy w obrębie tego samego roku lub prosty przypadek)
- Wyświetla wynik w godzinach i minutach (np. 8h 25m)
- Obsługuje dowolną kolejność dat
- Działa z pipe'em i plikami tekstowymi

---

## Wymagania
Python 3 (standardowa biblioteka – bez zewnętrznych zależności)

---

# Format:  DD-MM HH:MM

---

# How to run

```bash
python3 difftime.py "date1" "date2"
```

or

```bash
chmod +x difftime.py
./difftime.py "date1" "date2"
```

---

# Examples:

```bash
difftime "07-03 10:15" "07-03 18:40"
```

```bash
echo -e "07-03 10:15\n07-03 18:40" | difftime
```

```bash
# Sample file 
cat dates.txt
07-03 18:40
07-03 10:15

# Usage of difftime
cat dates.txt | difftime
```

Output:
```bash
8h 25m
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file.

**Attribution appreciated:** If you use this code, a link back to this repo
would be awesome (but not required). It helps other developers find the original
work and supports independent creators like me.

---

An Android APK version is available here:
https://github.com/CodeTruckerDev/DiffTime
