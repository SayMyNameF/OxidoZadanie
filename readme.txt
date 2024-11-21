Dzień dobry

Skrypt został uruchomiony na wersji OpenAI 0.28.0
Zainstalować tą wersję można z poziomu powershella na Windowsie komendą "pip install openai==0.28"

Konieczna jest instalacja pythona na świeżym komputerze, czy mamy pythona na komputerze możemy zobaczyć w powershellu komendą "python". Zainstalowany python pokaże jaka jest jego wersja, niezainstalowany przekieruje nas do Microsoft store gdzie możemy wybrać wersję do instalacji. W moim przypadku użyłem wersji 3.11

Uruchomić skrypt możemy z poziomu IDE (ja użyłem do tego PyCharma Community Edition) lub konsoli systemowej będąc w folderze ze skryptem wpisując komendę "python <nazwa_skryptu>". W tym przypadku "python skrypt.py"

Wykorzystałem własny klucz API, przyda się tak czy siak do własnych celów na różne zabawy :)
Do odpalenia skryptu proszę uzupełnić swój klucz w pliku skrypt.py.

Skrypt dzieli się na poszczególne segmenty, opiszę go etapami.

1. Importujemy bibliotekę openai - w końcu bez niej nie moglibyśmy się połączyć
2. Ustawienie klucza API - klucz do autoryzacji
3. Funkcja read_article(file_path) - ustalenie ścieżki pliku, odczytania zawartości i zwrócenia jako pojedyńczy ciąg tekstowy w formacie UTF-8
4. Funkcja process_article_with_openai(article_text, prompt) - ustalamy zawartość arykułu który chcemy przetworzyć i zapytanie jakie wyślemy do AI. PRzy pomyślnym przetworzeniu zwrócony tekst zostanie pozbawiony białych znaków.
5. Funkcja save_to_html(content, output_file) - tekst generowany przez OpenAi jest zapisywany w pliku html. Dodaję od siebie nagłówek po czym wkleja zawartość z OpenAI
6. Funkcja main() - ustalenie ścieżki do pliku z artykułem, odczytanie artykułu (wywołanie funkcji), prompt do OpenAI(przekazany do funkcji z pkt.4), przetworzony artykuł zapisuje do html(wywołanie funkcji), jak się nie powiedzie wyświetla błąd.
7. Uruchomienie skryptu(funkcji main())