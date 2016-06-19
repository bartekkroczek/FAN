# Test rozumowania przez analogię (FAN)

Test służy pomiarowi sprawności rozumowania w prostych figuralnych problemach analogicznych i ma taką unikatową
cechę, że wśród błędnych opcji odpowiedzi precyzyjnie manipuluje się odległością od poprawnego rozwiązania.

## Bodźce
Prezentowane są po lewej stronie ekranu, kolejno pod sobą, trzy układy figur geometrycznych (A, B, C; wybieranych z
zestawu 16 dostępnych figur), każdy zawierający cztery figury w matrycy 2×2 na białym tle, oraz dużego znaku
zapytania, a po prawej stronie sześciu możliwych opcji odpowiedzi (w matrycy 3×2). Układ B zawiera te same figury co A,
tylko że wszystkie te figury zajmują inne losowo wybrane miejsca, a dla każdej z 2, 3, albo 4 losowo wybranych figur
(zmienna złożoność relacyjna problemu) zmieniono od jednej do trzech percepcyjnych cech figury (losowo, z tym że
przynajmniej dla jednej figury zmieniono dokładnie 2 cechy). Owe cechy to: rotacja elementu (0, 90, albo 180), jasność
(biały, jasno szary albo ciemno szary) oraz czarne obramowanie (cienkie, średnie albo grube).
Kluczowe jest to, że układ zmian każdej ze zmienianych figur jest unikatowy względem innych układów zmian o tej samej
liczbie zmienianych cech. Np. dla poziomu złożoności 4 dla jednej figury może zmieniać się rotacja i jasność, dla drugiej –
rotacja i ramka, dla trzeciej – 1 wybrana cecha, a dla czwartej – wszystkie 3 cechy naraz. Istotne jest nie tylko to, które
cechy się zmieniły dla danej figury, ale też o ile poziomów i w którym kierunku się zmieniły. Układ C zawiera 4 losowo
wybrane figury spośród pozostałych figur (=pomijając figury użyte w A/B).

## Zasady testu i opcje odpowiedzi

Wśród prezentowanych rozwiązań znajduje się rozwiązanie (opcja poprawna, D), dla którego taka sama liczba figur jak w
A/B jest zmieniona za pomocą dokładnie tych samych zestawów i poziomów cech (tzn. np. jeśli dla złożoności 2, w
układzie B jednej figurze pogrubia się ramka o 1 poziom, a drugiej – kolor blednie o 2 poziomy i następuje obrót o 90
stopni), to w układzie D tak samo, dla jednej losowo wybranej figury pogrubia się ramka o 1 poziom, a dla drugiej – kolor
blednie o 2 poziomy i następuje obrót o 90 stopni). Figury w D (tożsame co do kształtu z C), podobnie jak w układach
A/B zajmują inne losowo wybrane miejsca (we wszystkich opcjach odpowiedzi te same). Zadaniem osoby badanej jest
wybór tej właśnie poprawnej opcji, czyli opcji, w której dla tej samej liczby figur, które zmieniają się w B, pewne figury z
C zmieniają się względem tych samych pojedynczych, par, albo trójek cech, które zmieniły się dla obiektów w B o tę
samą liczbę poziomów. Dodatkowo, dana zmiana liczby poziomów (tzn. -2, -1, +1, +2) może wystąpić w układzie tylko
raz. Te unikalne układy zmian cech będą ułatwiać jednoznaczne zmapowanie figur w A/B na figury w C/D.

Oprócz opcji poprawnej, wśród opcji znajduje się 5 opcji błędnych (o tych samych lokalizacjach figur jak w D), o pewnej
różnicy względem opcji D. Łącznie prezentowane są (na losowych miejscach po prawej stronie ekranu):
1. Opcja poprawna – powyżej opisana opcja D.
2. Opcja, która jest identyczna z D za wyjątkiem tego, że jedna ze zmian cech dla jednej z figur, z tych którym zmieniono
1 lub 2 cechy, jest zmianą innej cechy niż w A/B (np. jeśli w A/B dwie figury zmieniono tak, że jednej zmieniono rotację i
jasność, a drugiej rotację i ramkę, to w opcji 2 jednej wciąż zmieniono rotację i jasność, ale drugiej – jasność i ramkę).
3. Opcja, która jest identyczna z D za wyjątkiem tego, że dla jednej z figur, z tych którym zmieniono 2 albo 3 cechy,
dokładnie jedna z tych cech nie zostaje zmieniona (tzn. jest taka sama jak w C).
4. Opcja, która jest identyczna z C za wyjątkiem tego, że poprawnie zmieniona (czyli tak jak w A/B) jest tylko jedna figura
z 2 albo 3 cechami.
5. Opcja, która jest identyczna z C za wyjątkiem tego, że poprawnie zmieniona (czyli tak jak w A/B) tylko jedna cecha
jednej figury z 1 albo 2 cechami.
6. Opcja, która zawiera te same figury co układ C (tyle że, jak wspomniano, na innych miejscach).

Opcje 1 – 3 to odpowiedzi relacyjne (albo osoba badana przeprowadziła poprawne rozumowanie relacyjne, albo prawie
poprawne – pominęła 1 cechę), a opcje 4 – 6 to odpowiedzi percepcyjne (prawdopodobnie osoba badana w ogóle nie
przeprowadziła rozumowania relacyjnego, a tylko kierowała się podobieństwem figur do układu C). Każda opcja ma
wartość podobieństwa (SIMILARITY) do opcji D (od „0” dla opcji 6 do „1” dla opcji D), która jest równa stosunkowi liczby
zmienionych cech w danej opcji do liczby cech w opcji D, z tym, że niepoprawnie zmieniona cecha w opcji 2 jest liczona
jako pół cechy. Przykładowo, jeśli w opcji D zmieniono 5 cech, to pozostałe opcje mają następujące wartości
podobieństwa: 2 – 0.90, 3 – 0.80, 4 – 0.60 albo 0.40 (zależnie czy zmieniono figurę z 2 albo 3 cechami), 5 – 0.20. Opcja
wybrana myszką przez osobę badaną zostaje zaznaczona pogrubioną ramką. Zatwierdzenie odpowiedzi i przejście do
kolejnego problemu odbywa się przez kliknięcie w przycisk „Zatwierdź odpowiedź” w prawym dolnym rogu ekranu.

## Parametry programu:

Program umożliwia utworzenie listy k problemów, gdzie dla każdego problemu w kolejności definiuje się: TIME (czas
prezentacji – czas na odpowiedź), REL (złożoność relacyjna), FEEDB (0/1 – nie/wyświetla wynik(u) „poprawnie/
niepoprawnie” po danym problemie, 2 – zlicza wyniki dla wszystkich problemów z 2 i pokazuje „% poprawnych
rozwiązań” na koniec całego testu), WAIT (czas przerwy między próbami, gdy 0 program wyświetla „naciśnij przycisk” i
czeka na jego naciśnięcie), EXP (1 to problem eksperymentalny, 0 – treningowy). Osobną kategorią zdarzeń jest
Instrukcja N (z treścią jako tekst i/lub bmp oraz czasem prezentacji, dla czas=0 „znika po kliknięciu”). Dla każdego
problemu zdefiniowana jest też wskazówka tekstowa, wyświetlana przez X sek. (X=0 czeka się na naciśnięcie przycisku,
dla X=-1 nie wyświetla się wskazówki). Lista problemów i instrukcji może być potem prezentowana w podanej lub
losowej kolejności (opcja do zakliknięcia), z tym że losowane są tylko problemy z EXP=1 pomiędzy dwoma problemami z
EXP=0 albo instrukcją N albo końcem sekwencji (tzn. jeśli mamy np. dwa warunki testu, które chcemy pokazywać po
sobie, ale każdy musi być poprzedzony instrukcją i przetrenowany, to dla przykładowej sekwencji EXP =
N001111N001111 program najpierw zawsze pokazuje N i dwa pierwsze problemy 0, potem losuje kolejność czterech
problemów z 1, potem znów pokazuje kolejno N i dwa z 0, i znów losuje kolejność dla ostatnich czterech 1). Inne
parametry: kolor tła w teście i czy program działa w trybie okulografu. Na początku program pyta o ID, PŁEĆ i WIEK i
zapisuje je w nazwie pliku (np. A101K29.txt).

## Zapis wyników

Tabela w pliku txt o kolejnych problemach w wierszach i następujących polach: NR (nr kolejny), TIME, REL, FEEDB, WAIT,
EXP, POS (pozycja z sześciu, na której była prezentowana opcja D), LATENCY (czas odpowiedzi – naciśnięcia „zatwierdź
odpowiedź”), OPT1 (0 albo 1 gdy wybrano opcję 1), OPT2 (0 albo 1 gdy wybrano opcję 2), OPT3 (0 albo 1 gdy wybrano
opcję 3), OPT4 (0 lub 1 albo wybrano opcję 4), OPT5 (0 albo 1 gdy wybrano opcję 5), OPT6 (0 albo 1 gdy wybrano opcję
6), NORESP (0 albo 1 gdy nie wybrano żadnej opcji), TOTAL (liczba cech zmienionych w opcji D), SIMILARITY (0..1). Po
ustawieniu parametru, program podczas testu komunikuje się z okulografem, ROI to A, B, C i poszczególne opcje.