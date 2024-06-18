#my_answers2 = [3, 2, 3, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 4, 4, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 5, 4, 3, 2, 2, 4, 2, 2, 1, 1, 1, 4, 2, 1, 1, 2, 1, 2, 1, 4, 2, 2, 1, 1, 2, 3, 3, 3, 4, 1, 1, 4, 3, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 4]


my_answers = [3,2,3,2,2,1,1,1,1,1,1,1,1,1,1,2,1,1,4,2,2,2,2,2,2,1,1,1,2,2,1,2,2,6,4,3,2,2,4,2,2,1,1,1,4,2,1,1,2,2,2,2,4,2,2,1,1,2,3,1,3,4,1,4,1,4,1,2,2,1,2,1,1,1,2,2,1,1,1,2,2,1,2,1,1,1,2,1,2,2,2,4]





def multiple_answer(questions: int, points: float) -> list[float]:
    return [points / questions] * questions


labels = ['1', '2', '3', '4', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '7', '8', '9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.7', '11', '12', '13', '14', '15', '16', '17.1', '17.2', '17.3', '17.4', '17.5', '18', '19.1', '19.2', '19.3', '19.4', '19.5', '19.6', '19.7', '20', '21.1', '21.2', '21.3', '21.4', '21.5', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33.1', '33.2', '33.3', '33.4', '33.5', '34.1', '34.2', '34.3', '34.4', '34.5', '34.6', '34.7', '35.1', '35.2', '35.3', '35.4', '36.1', '36.2', '36.3', '36.4', '36.5', '36.6', '37']
correct_answers = [[3], [2], [3], [1], [2], [1], [1], [1], [2], [1], [2], [1], [1], [1], [2], [1], [2], [1], [4], [3, 4, 5], [2], [2], [1], [2], [1], [1], [1], [1], [2], [2], [1], [2], [2], [5], [4], [3], [2], [2], [4], [2], [2], [1], [1], [1], [4], [2], [1], [1], [2], [2], [2], [1], [1], [2], [2], [1], [1], [2], [3], [1], [3], [4], [1], [4], [1], [3], [2], [3], [1], [1], [2], [1], [1], [1], [2], [2], [1], [1], [1], [2], [2], [1], [1], [1], [2], [1], [2], [1], [2], [2], [2], [4]]
points_per_question = [2, 2, 2, 2, *multiple_answer(questions=7, points=5), *multiple_answer(questions=7, points=5), 3, 3, *multiple_answer(questions=6, points=2), *multiple_answer(questions=7, points=3), 6, 4, 3, 6, 5, 2, *multiple_answer(questions=5, points=4), 4, *multiple_answer(questions=7, points=4), 6, *multiple_answer(questions=5, points=3), 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, *multiple_answer(questions=5, points=5), *multiple_answer(questions=7, points=6), *multiple_answer(questions=4, points=5), *multiple_answer(questions=6, points=6), 3]

if len(my_answers) == 0:
    for label, correct_choices, points in zip(labels, correct_answers, points_per_question):
        while True:
            try:
                my_answer = int(input(f'{label}: '))
                if my_answer not in range(1, 8):
                    raise ValueError
                break
            except ValueError:
                print('Please enter a number between 1 and 7.')

        if my_answer in correct_choices:
            print(f'Correct! (+{points:.2f} points)')
        else:
            print(f'Wrong! Correct answer was {", ".join(map(str, correct_choices))} (0 points)')
        my_answers.append(my_answer)
else:
    for my_answer, correct_choices, points in zip(my_answers, correct_answers, points_per_question):
        print(f'Correct answer: {", ".join(map(str, correct_choices))} Your answer: {my_answer} ({points if my_answer in correct_choices else 0:.2f} points)')

points_total = sum(points for my_answer, correct_choices, points in zip(my_answers, correct_answers, points_per_question) if my_answer in correct_choices)

max_points = sum(points_per_question)
print(f'Total points: {points_total:.2f} = {points_total / max_points * 100:.2f}%')