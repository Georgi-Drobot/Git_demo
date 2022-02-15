from true_or_false_Illia.game import Game
from true_or_false_Illia.game_result import GameResult
from true_or_false_Illia.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}.")
    print(f"You won!" if result.won else "You lost!")


game = Game("data\\Questions.csv", end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    # Next is not necessary since we do such check in game.py (on 40 line)
    # if game.is_last_question():
    #     print("No more questions")
    #     break

    q = game.get_next_question()
    print("\nDo you believe in the next statement or question? Enter 'y' or 'n'")
    print(q.text)

    answer = input() == 'y'

    if q.is_true == answer:
        print("Good job, you are right")
    else:
        print("Oops, actually you are mistaken. Here is explanation:")
        print(q.explanation)

    game.give_answer(answer)
