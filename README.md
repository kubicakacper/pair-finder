Kacper Kubica

Celem zadania jest implementacja aplikacji, która znajduje wszystkie pary liczb
naturalnych, których suma wynosi 12. Raz wykorzystana liczba do stworzenia pary
nie może być częścią kolejnej.

**Dane wejściowe**:
Zbiór N liczb naturalnych o wartościach od 0 do 12

**Dane wyjściowe**:
Pary liczb sumujące się do 12. Parą mogą być zwracane w dowolnej kolejności.
Pierwsza liczba pary powinna być nie większa od drugiej.


**Założenia**:
Liczba 0 należy do zbioru liczb naturalnych.

**Wnioski**:
Szukamy następujących par liczb: [0,12], [1,11], [2,10], [3,9], [4,8], [5,7], [6,6]

**Pomysł #1**:
Zliczać występowanie każdej liczby.
Performance: trzeba przejrzeć zbiór tylko raz
Memory: wystarczy 13 zmiennych INT (lub mniejszych)

**Pomysł #2**:
Otwierasz plik wejściowy i wyjściowy.
Masz 7 zmiennych:
Jeśli trafię na 0, to inkremetuję zmienną zerową, jeśli na 12, to ją dekrementuję.
Jeżeli inkrementacja/dekrementacja zbliży mnie do zera, to printuję parę do pliku.

Myślę, że to nie jest problem odpowiedni dla OOP, ale niech będzie



Kacper Kubica

This app finds pairs of natural numbers (including 0) that add up to the given sum (e.g. 12).
The app is:
- **generic** (given sum can be any natural number),
- ready for **stream processing** (processes each number separately and if a pair is loaded immediately after it is found),
- resistant to value errors - handled error occurrences are logged in diag_<timestamp>.log file in diagnostic_logs directory
- 

How to run it - interface:


Algorythm iteration:
1. read next number from a .txt file - separator can be set, comma is default
2. checks if there is a match (if this number adds up with any previous not used number to the given sum)
3. write the pair to a .txt file (if found)

How the check works?
