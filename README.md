# DiffTime-CLI

A tiny CLI tool inspired by the Unix philosophy that calculates the difference between two dates.

The order of the dates does not matter.

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

An Android APK version is available here:
https://github.com/CodeTruckerDev/DiffTime
