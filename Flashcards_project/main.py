from storage import load_cards, save_cards
from logic import add_card, show_cards, quiz, delete_card

def main():
    cards = load_cards()

    while True:
        print("====== Flashcards ======")
        print("1. Add flashcard")
        print("2. Show all flashcards")
        print("3. Quiz me")
        print("4. Delete a flashcard")
        print("5. Save & exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_card(cards)
        elif choice == "2":
            show_cards(cards)
        elif choice == "3":
            quiz(cards)
        elif choice == "4":
            delete_card(cards)
        elif choice == "5":
            save_cards(cards)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid option.")
            print("")

if __name__ == "__main__":
    main()
