import random

def add_card(cards):
    print("Choose a category:")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Mathematics")
    print("4. Computer Science")
    print("5. Biology")
    print("6. General Knowledge")

    cat_choice = input("Enter number (1-6): ")

    if cat_choice == "1":
        category = "Physics"
    elif cat_choice == "2":
        category = "Chemistry"
    elif cat_choice == "3":
        category = "Mathematics"
    elif cat_choice == "4":
        category = "Computer Science"
    elif cat_choice == "5":
        category = "Biology"
    elif cat_choice == "6":
        category = "General Knowledge"
    else:
        print("Invalid category.")
        return

    q = input("Enter the question: ")
    a = input("Enter the answer: ")

    if q == "" or a == "":
        print("Both question and answer are required.")
    else:
        cards.append({
            "category": category,
            "question": q,
            "answer": a
        })
        print("Flashcard added!")

def show_cards(cards):
    if len(cards) == 0:
        print("No flashcards yet.")
    else:
        num = 1
        for c in cards:
            print(str(num) + ". [" + c["category"] + "] Q: " + c["question"] + " | A: " + c["answer"])
            num = num + 1
    print()


def quiz(cards):
    if len(cards) == 0:
        print("You have no cards to quiz.")
        return

    print("Quiz started! Type 'exit' to stop.")
    print("")

    questions = cards[:]
    random.shuffle(questions)

    correct = 0
    total = 0

    for card in questions:
        print("[" + card["category"] + "] Q:", card["question"])

        user = input("Your answer: ")
        user = user.strip()

        if user.lower() == "exit":
            break

        total = total + 1

        if user.lower() == card["answer"].lower():
            print("Correct!")
            correct = correct + 1
        else:
            print("Wrong! Correct answer is:", card["answer"])
        print("")

    print("Quiz ended.")
    print("Total questions answered:", total)
    print("Correct answers:", correct)

    if total > 0:
        percent = (correct * 100) / total
        print("Score:", percent, "%")
    print("")

def delete_card(cards):
    if len(cards) == 0:
        print("No flashcards to delete.")
        return

    show_cards(cards)

    num = input("Enter the number of the card to delete: ")

    if not num.isdigit():
        print("Please enter a valid number.")
        return

    index = int(num)

    if index < 1 or index > len(cards):
        print("Number out of range.")
        return

    removed = cards.pop(index - 1)
    print("Deleted flashcard:", removed["question"])
    print("")
