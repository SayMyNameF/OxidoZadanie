#1. Importujemy bibliotekę openai  - w końcu bez niej nie moglibyśmy się połączyć
import openai

#2. Ustawienie klucza API - klucz do autoryzacji
openai.api_key = 'proszę wprowadzić swój klucz API'

#3. Funkcja read_article(file_path) - ustalenie ścieżki pliku, odczytania zawartości i zwrócenia jako pojedyńczy ciąg tekstowy w formacie UTF-8

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

#4. Funkcja process_article_with_openai(article_text, prompt) - ustalamy zawartość arykułu który chcemy przetworzyć i zapytanie jakie wyślemy do AI. PRzy pomyślnym przetworzeniu zwrócony tekst zostanie pozbawiony białych znaków.
def process_article_with_openai(article_text, prompt):
    """Funkcja do wysłania artykułu i promptu do OpenAI API."""
    try:
        # Użycie modelu gpt-3.5-turbo lub gpt-4, korzystając z v1/chat/completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Możesz użyć gpt-4, jeśli masz dostęp
            messages=[
                {"role": "system", "content": "Cześć AI!, jak się dzisiaj masz? Mam do Ciebie małą prośbę"},
                {"role": "user", "content": f"{prompt}\n{article_text}"}
            ],
            max_tokens=1500,  # Liczba tokenów do przetworzenia
            temperature=0.7,  # Kontroluje kreatywność odpowiedzi
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

#5. Funkcja save_to_html(content, output_file) - tekst generowany przez OpenAi jest zapisywany w pliku html. Dodaję od siebie nagłówek po czym wkleja zawartość z OpenAI
def save_to_html(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        html_content = f"""
        <h1>Przetworzony Artykuł zadania Oxido</h1>
        {content}
        """
        file.write(html_content)

#6. Funkcja main() - ustalenie ścieżki do pliku z artykułem, odczytanie artykułu (wywołanie funkcji), prompt do OpenAI(przekazany do funkcji z pkt.4), przetworzony artykuł zapisuje do html(wywołanie funkcji), jak się nie powiedzie wyświetla błąd.
def main():
    file_path = 'text.txt'
    article_text = read_article(file_path)

    if article_text:
        prompt = (
            "Proszę stworzyć HTML do poniższego artykułu, "
            "który będzie odpowiednio sformatowany z tagami HTML. "
            "Zwróć uwagę na następujące wytyczne: "
            "- Użyj odpowiednich tagów HTML do strukturyzacji treści (np. <h1>, <h2>, <p>, <ul>, <li>). "
            "- Dodaj miejsca na grafiki w tagach <img> z atrybutem src='image_placeholder.jpg' oraz alt w dokładnym opisie promptu do generowania grafiki. "
            "- Dodaj podpisy pod obrazkami z użyciem tagu <figcaption>. "
            "- Zwróć tylko kod HTML do wstawienia w <body>, bez CSS i JavaScript."
        )
        processed_content = process_article_with_openai(article_text, prompt)

        if processed_content:
            save_to_html(processed_content, 'artykul.html')
            print("Artykuł został zapisany w pliku artykul.html")
        else:
            print("Błąd podczas przetwarzania artykułu.")
    else:
        print("Nie udało się odczytać pliku text.txt.")

#7. Uruchomienie skryptu(funkcji main())
if __name__ == "__main__":
    main()
