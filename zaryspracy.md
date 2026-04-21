# Error Mitigation
#### Projekt inżynierski
##### Liliana Rybińska, Dawid Celian, informatyka kwantowa 2026
### 1. Wprowadzenie

Z uwagi na ograniczoną liczbę dostępnych kubitów oraz brak możliwości implementacji pełnej korekcji błędów kwantowych, w praktycznych zastosowaniach coraz większą rolę odgrywają techniki mitigacji błędów (error mitigation). 

Celem tych metod nie jest całkowite usunięcie błędów na poziomie sprzętowym, lecz poprawa jakości wyników obliczeń poprzez odpowiednie przetwarzanie i analizę danych pomiarowych. W odróżnieniu od korekcji błędów, nie wymagane są dodatkowe kubity, co pozwala na pracę na obecnym sprzęcie kwantowych.


### 2. Zakras pracy
Celem niniejszej pracy jest:

omówienie podstaw teoretycznych mitigacji błędów,
przedstawienie wybranych technik mitigacji wykorzystywanych w praktyce,
analiza zalet i ograniczeń tych metod,
porównanie mitigacji błędów z korekcją błędów kwantowych.

---
### 3. Metody
#### 3.1. Mitigacja błędów pomiarowych (Measurement Error Mitigation)

Metoda polegająca na kalibracji błędów pomiarowych poprzez wykonanie dodatkowych obwodów referencyjnych, a następnie zastosowanie macierzy korekcyjnej do wyników pomiarów.  

Technika ta pozwala znacząco poprawić dokładność wyników bez zwiększania złożoności obwodu kwantowego.

---

#### 3.2. Zero-Noise Extrapolation (ZNE)

Technika polegająca na sztucznym zwiększaniu poziomu szumu w obwodzie kwantowym (np. poprzez powielanie bramek), a następnie ekstrapolacji wyników do granicy zerowego szumu.  

Metoda ta:
- nie wymaga dodatkowych kubitów  
- zwiększa koszt próbkowania obliczeń  
- pozwala oszacować wynik idealny  

---

### 3.3. I/Q Classifier 

Polega na wykorzystaniu alghorytmów uczenia maszynowego w celu znajdywania optymalnej granicy decyzyjnej między chmurami punktów dla stanów 0 i 1.
Potrzebne jednak będą otrzymane na procesorze surowe dane, które umożliwią klasyfikację wyników już na poziomie fizycznym.

---

#### 3.4. Probabilistic Error Cancellation (PEC)

Metoda oparta na probabilistycznym odtwarzaniu idealnych operacji kwantowych poprzez liniową kombinację operacji obarczonych szumem.  

Ze względu na:
- bardzo wysoki koszt obliczeniowy  
- dużą złożoność implementacyjną  

technika ta zostanie omówiona głównie w ujęciu teoretycznym, bez pełnej implementacji praktycznej.

### 4. Technologie i narzędzia wykorzystane w projekcie

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
### 5. Ograniczenia sprzętowe

Podczas realizacji projektu należy uwzględnić ograniczenia aktualnych komputerów kwantowych:

- Wysoki poziom szumów (noise)  
- Ograniczona liczba kubitów  
- Błędy bramek kwantowych  
- Krótki czas koherencji  
- Ograniczona dostępność backendów  

Ograniczenia te wpływają bezpośrednio na jakość wyników oraz efektywność zastosowanych metod mitigacji błędów.

### 6. Analiza ryzyka

W projekcie zidentyfikowano następujące potencjalne ryzyka:

| Ryzyko | Prawdopodobieństwo | Wpływ | Opis |
|--------|------------------|-------|------|
| Wysoki poziom szumu | Wysokie | Wysoki | Może zniekształcić wyniki obliczeń |
| Ograniczony dostęp do backendów | Średnie | Wysoki | Ograniczona liczba uruchomień |
| Błędy implementacyjne | Średnie | Średni | Niepoprawna implementacja algorytmów |
| Długi czas obliczeń | Wysokie | Średni | Szczególnie dla ZNE i PEC |

#### Strategie minimalizacji ryzyka:
- Wykorzystanie symulatorów do wstępnych testów  
- Ograniczenie liczby eksperymentów na realnym sprzęcie  
- Testowanie kodu na małych przykładach  

