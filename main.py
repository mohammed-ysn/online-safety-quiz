import random
import json


class Quiz:
    def __init__(self):
        # Store score
        self.score = 0

        # Store current question number
        self.q_num = 0

        # Read json file into dict
        with open('quiz_data.json') as json_file:
            self.quiz_data = json.load(json_file)

        # Create list with question numbers
        self.q_order = list(range(len(self.quiz_data['data_list'])))

        random.shuffle(self.q_order)

        self.show_title()

        self.ask_username()

        self.welcome_user()

        self.display_instructions()

        self.start_quiz()

        self.display_score()

    def show_title(self):
        print('-' * 20)
        print('Online safety quiz')
        print('-' * 20)

        print()

    def ask_username(self):
        self.username = input('Username: ')

        print()

    def welcome_user(self):
        print(f'Welcome {self.username}!')

        print()

    def display_instructions(self):
        print('-' * 20)
        print('Instructions')
        print('-' * 20)

        print()

        print('You will answer a series of questions regarding online safety. Each question is multiple choice. To denote your answer, enter the respective answer number (e.g. 2). Each correct answer scores you 4 points. Your score will be displayed at the end.')

        print()

    def start_quiz(self):
        # Loop until all questions have been asked
        while (self.q_num < len(self.q_order)):
            self.display_q()

            self.display_ans()

            self.get_user_ans()

            self.check_ans()

            self.q_num += 1

    def display_q(self):
        print(self.quiz_data['data_list']
              [self.q_order[self.q_num]]['question'])

    def display_ans(self):
        # Store list of answers
        ans_list = self.quiz_data['data_list'][self.q_order[self.q_num]]['answers']

        # Create the display order of answers
        ans_order = list(
            range(len(ans_list)))

        random.shuffle(ans_order)

        # Store the correct answer number
        self.correct_ans = ans_order.index(0) + 1

        # Display answers
        for i, j in enumerate(ans_order):
            print(f'{i + 1}. {ans_list[j]}')

        print()

    def get_user_ans(self):
        # Loop until a number is entered
        while(True):
            try:
                self.user_ans = int(input('Answer: '))

                print()

                break
            except ValueError:
                print('Invalid answer. Please input a number.')

                print()

    def check_ans(self):
        if self.user_ans == self.correct_ans:
            self.score += 4

    def display_score(self):
        print('-' * 20)
        print('Score')
        print('-' * 20)

        print()

        print(f'{self.username}, you scored: {self.score}')


if __name__ == "__main__":
    quiz = Quiz()
