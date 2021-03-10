from Question import Question

question_prompts = [
    "다음 설명 중 틀린 것은? \n1)세포는 살아 있다.\n2)동물의 세포는 세포벽이 없다.\n3)세포는 유성생식을 통해 번식한다.\n4)세포는 핵을 가지고 있다.\n",
    "다음 중 세포의 구성이 아닌 것은? \n1)세포핵\n2)골기체\n3)미톤콘드리아\n4)마이봄선\n\n",
    "다음 중 혈액 구성이 아닌 것은? \n1)모양체\n2)호중구\n3)혈소판\n4)적혈구\n\n"
]

questions = [
    Question(question_prompts[0], "3"),
    Question(question_prompts[1], "4"),
    Question(question_prompts[2], "1")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("당신은 " + str(len(questions)) + "문제 중" + str(score) + "문제를 맞추었습니다.")


run_test(questions)
