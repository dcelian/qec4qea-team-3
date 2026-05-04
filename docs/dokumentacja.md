# Specyfikacja projektu – Error Mitigation w obliczeniach kwantowych

## 1. Cel projektu

Celem projektu jest zaprojektowanie i implementacja systemu umożliwiającego analizę oraz poprawę jakości wyników obliczeń kwantowych poprzez zastosowanie wybranych metod mitigacji błędów z wykorzystaniem biblioteki Qiskit.

---

## 2. Zakres projektu

Projekt obejmuje:

- implementację przykładowych obwodów kwantowych  
- przeprowadzenie symulacji w środowisku bezszumowym i zaszumionym  
- zastosowanie wybranych metod mitigacji błędów:
  - Measurement Error Mitigation  
  - Zero-Noise Extrapolation  
- analizę i porównanie wyników przed i po zastosowaniu mitigacji  

---

## 3. Funkcjonalności systemu

System będzie umożliwiał:

- generowanie obwodów kwantowych  
- uruchamianie obliczeń na symulatorze oraz backendzie rzeczywistym  
- zbieranie wyników pomiarów  
- zastosowanie metod mitigacji błędów  
- porównanie wyników  
- wizualizację danych  

---

## 4. Technologie i narzędzia

W ramach realizacji projektu planowane jest wykorzystanie następujących technologii programowych oraz środowisk obliczeniowych:

- **Qiskit (IBM Quantum)**  
  Framework programistyczny w języku Python przeznaczony do tworzenia, symulacji oraz uruchamiania obwodów kwantowych na rzeczywistych procesorach kwantowych oraz symulatorach.  
  Umożliwia implementację technik mitigacji błędów oraz analizę wyników pomiarowych.

- **Python** -Język programowania wykorzystywany do:
  - implementacji algorytmów  
  - przetwarzania danych pomiarowych  
  - wizualizacji wyników  

- **Symulatory kwantowe (np. Aer Simulator)**  
  - porównania wyników idealnych (bezszumowych)  
  - analizy wyników obarczonych błędami  

- **Rzeczywiste backendy kwantowe IBM Quantum**  
  - zaprezentowania wpływu szumów sprzętowych  
  - oceny skuteczności metod mitigacji błędów  

- **Narzędzia do wizualizacji danych (np. matplotlib)**  
  - prezentacji wyników  
  - analizy eksperymentów  

---

## 5. Architektura rozwiązania

System będzie składał się z następujących etapów:

1. Przyjęcie obwodu kwantowego wygenerowanego przez moduł transpilatora  
2. Uruchomienie symulacji (z uwzględnieniem szumu oraz w środowisku idealnym)  
3. Zebranie wyników pomiarów  
4. Zastosowanie wybranych metod mitigacji błędów  
5. Analiza oraz wizualizacja wyników  

---

## 6. Wymagania funkcjonalne

System musi:

- umożliwiać przyjmowanie obwodów kwantowych z modułu transpilatora  
- wykonywać obliczenia w środowisku Qiskit  
- przeprowadzać symulacje z uwzględnieniem szumu oraz bez szumu  
- stosować wybrane metody mitigacji błędów  
- porównywać wyniki przed i po zastosowaniu mitigacji  

---

## 7. Wymagania niefunkcjonalne

- system powinien być napisany w języku Python  
- kod powinien być modularny i czytelny  
- wyniki powinny być powtarzalne  
- czas wykonania powinien być możliwie krótki  

---

## 8. Ograniczenia systemu

- ograniczona liczba kubitów  
- wysoki poziom szumu  
- ograniczony dostęp do backendów  
- wysoki koszt obliczeniowy metod (np. ZNE)  

---

## 9. Analiza ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ |
|--------|------------------|-------|
| Wysoki poziom szumu | Wysokie | Wysoki |
| Brak dostępu do backendu | Średnie | Wysoki |
| Błędy implementacyjne | Średnie | Średni |

---

## 10. Plan implementacji


1. **Przygotowanie środowiska**
   - konfiguracja środowiska Python  
   - instalacja i konfiguracja biblioteki Qiskit  
   - dostęp do symulatorów oraz backendów IBM Quantum  

2. **Integracja z modułem transpilatora**
   - przygotowanie interfejsu do przyjmowania obwodów kwantowych  
   - weryfikacja poprawności otrzymanych obwodów  
   - przygotowanie prostych obwodów referencyjnych do testów  

3. **Uruchomienie symulacji**
   - wykonanie obliczeń na symulatorze bez szumu (wynik referencyjny)  
   - wykonanie obliczeń z uwzględnieniem szumu  
   - opcjonalne uruchomienie na rzeczywistym backendzie  

4. **Implementacja metod mitigacji błędów**
   - implementacja Measurement Error Mitigation  
   - implementacja Zero-Noise Extrapolation  
   - przygotowanie struktury pod ewentualne rozszerzenia  

5. **Analiza wyników**
   - porównanie wyników przed i po mitigacji  
   - ocena skuteczności metod  
   - wizualizacja danych (wykresy, histogramy)   
