# Domino-automaton
Simple domino simulation

Każdy z symboli domina został zakodowany jako liczby w systemie trójkowym:
/ -> 0,
| -> 1,
\ -> 2.

Na podstawie bliskiego sąsiedztwa (trójek symboli domina) determinujemy jaki będzie następny stan.
Przykładowo dla trójki //| następny stan symbolu w środku to |.

Wszystkie 27 możliwych stanów domina zostały zakodowane jako zasada (liczba) w sytemie trójkowym. Dla czasu płynącego do przodu jest to liczba 222211000222211000222100000, czyli /// (0 w systemie dziesiętnym) wybieramy liczbe na zerowym miejscu odwróconej zasady - jest to 0. Dla wstecznego czasu wybrałem zasadę 222111100122111100111111110.

W kodzie jest niestety bug dla czasu wstecznego, niestety nie udało mi się w tym czasie go rozwiązać.

Program włączamy z poziomu wiersza poleceń (ja pracowałem na fedorze) w następujący sposób:

$ python main.py [domino block input] [number of steps] [time forward],

gdzie [domino block input] to symbole domina w cudzysłowiu, [number of steps] liczba naturalna kroków, [time forward] to 1 albo 0, gdzie 1 - czas płynie do przodu, 0 - czas płynie do tyłu.

Przykład:

$ python main.py "||//||\||/\|" 2 1