**Kacper Kubica**

[//]: # ()
[//]: # (Celem zadania jest implementacja aplikacji, która znajduje wszystkie pary liczb)

[//]: # (naturalnych, których suma wynosi 12. Raz wykorzystana liczba do stworzenia pary)

[//]: # (nie może być częścią kolejnej.)

[//]: # ()
[//]: # (**Dane wejściowe**:)

[//]: # (Zbiór N liczb naturalnych o wartościach od 0 do 12)

[//]: # ()
[//]: # (**Dane wyjściowe**:)

[//]: # (Pary liczb sumujące się do 12. Parą mogą być zwracane w dowolnej kolejności.)

[//]: # (Pierwsza liczba pary powinna być nie większa od drugiej.)

[//]: # ()
[//]: # ()
[//]: # (**Założenia**:)

[//]: # (Liczba 0 należy do zbioru liczb naturalnych.)

[//]: # ()
[//]: # (**Wnioski**:)

[//]: # (Szukamy następujących par liczb: [0,12], [1,11], [2,10], [3,9], [4,8], [5,7], [6,6])

[//]: # ()
[//]: # (**Pomysł #1**:)

[//]: # (Zliczać występowanie każdej liczby.)

[//]: # (Performance: trzeba przejrzeć zbiór tylko raz)

[//]: # (Memory: wystarczy 13 zmiennych INT &#40;lub mniejszych&#41;)

[//]: # ()
[//]: # (**Pomysł #2**:)

[//]: # (Otwierasz plik wejściowy i wyjściowy.)

[//]: # (Masz 7 zmiennych:)

[//]: # (Jeśli trafię na 0, to inkremetuję zmienną zerową, jeśli na 12, to ją dekrementuję.)

[//]: # (Jeżeli inkrementacja/dekrementacja zbliży mnie do zera, to printuję parę do pliku.)

This app finds pairs of natural numbers (including 0) that add up to the given sum (e.g. 12).
The app is:
- **generic** (given sum can be any natural number),
- ready for **stream processing** (processes each number separately and if a pair is loaded immediately after it is found),
- resistant to value errors - handled error occurrences are **logged** in diag_<timestamp>.log file in diagnostic_logs directory
- tested with every push by **GitHub Actions** (unit tests, an integrity test and a performance test).

**How to run it - interface:**

`import pair_finder`  
`pair_finder.PairFinder.run()`

Pair Finder is a "static" class.  
`run()` class method can take 4 parameters: `run(input_file_path, output_file_path, sum_of_numbers, separator)`,
where the default values are:
- input_file_path = './txt_files/input.txt',
- output_file_path = './txt_files/output.txt',
- sum_of_numbers = 12, 
- separator = ','

**Algorythm iteration:**
1. read next number from a .txt file
2. checks if there is a match (if this number adds up with any previous not used number to the given sum)
3. write the pair to a .txt file (if found)

**How the check works?**

Explanation below assumes the given sum equals 12, but it is the same for any natural number.  
Finding pairs that add up to 12 mean finding pairs: [n, 12-n], where "n" is a natural number in the range [0,12].  
Important to note is that for even numbers like 12, there is one pair of the same numbers: [n/2, n/2] ([6,6] in case of 12).

The algorythm uses an "offset" array. In case of 12 it is a 7-fields array.  
First 6 fields track the difference in occurrence of corresponding numbers like 0 and 12, 1 and 11 and so forth.  
Seventh field equals 0 or 1 depending on whether number 6 is waiting for the pair.

If a number from the range [0,5] is read, a corresponding value in the offset array is **increased**.
First field is for 0, second for 1 and so on.  
If a number from the range [7,12] is read, a corresponding value in the offset array is **decreased**.
First field is for 12, second for 11 and so on.  
If number 6 is read, the last value in the offset array is changed (from 0 to 1 or from 1 to 0).  
And if a value in the offset array has been changed to a value closer to 0 (if new absolute value is lower),
it means a pair is found.