import requests
import html
import random
EDUCATION_CATEGORY_ID=9
API_URL = f'https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple'
def get_education_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
        return None
def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("falied!to fetch questions!")
        return
    score = 0
    print("Welcome to the Education quiz!1!0!1!:}")

    for i,q in enumerate(questions,1):
      question = html.unescape(q['question'])
      correct = html.unescape(q['correct_answer'])
      incorrects = [html.unescape(a) for a in q['incorrect_answers']]
      options = incorrects + [correct]
      random.shuffle(options)
      print(f"Question{i}:{question}")
      for idx, option in enumerate(options,1):
          print(f"{idx}.{option}")
      while True:
        try:
            choice = int(input("\nYour answers(1-4) : "))
            if 1<= choice <= 4:
                break
        except ValueError:
            pass
            print("Invalid input!!")

      if option[choice-1] == correct:
        print("Correct")
        score += 1
      else:
        print(f"Wrong,correct answer is: {correct} ")
    print("Final score is : {score}/{len(questions)}")
if __name__ == "__main__":
  run_quiz()