import requests

parameters = {
    'amount':10,
    'type':'boolean',

}

response = requests.get('https://opentdb.com/api.php',params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']


# question_data = [
# {
# "category": "Geography",
# "type": "boolean",
# "difficulty": "medium",
# "question": "Seoul is the capital of North Korea.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "Entertainment: Video Games",
# "type": "boolean",
# "difficulty": "easy",
# "question": "There are 6 legendary cards in &quot;Clash Royale&quot;.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "Science & Nature",
# "type": "boolean",
# "difficulty": "medium",
# "question": "Type 1 diabetes is a result of the liver working improperly.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "General Knowledge",
# "type": "boolean",
# "difficulty": "easy",
# "question": "The Sun rises from the North.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "History",
# "type": "boolean",
# "difficulty": "hard",
# "question": "The fourth funnel of the RMS Titanic was fake designed to make the ship look more powerful and symmetrical.",
# "correct_answer": "True",
# "incorrect_answers": [
# "False"
# ]
# },
# {
# "category": "General Knowledge",
# "type": "boolean",
# "difficulty": "easy",
# "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
# "correct_answer": "True",
# "incorrect_answers": [
# "False"
# ]
# },
# {
# "category": "Politics",
# "type": "boolean",
# "difficulty": "medium",
# "question": "Helen Clark was the 37th Prime Minister of Australia.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "Entertainment: Music",
# "type": "boolean",
# "difficulty": "medium",
# "question": "Nick Mason is the only member to appear on every Pink Floyd album.",
# "correct_answer": "True",
# "incorrect_answers": [
# "False"
# ]
# },
# {
# "category": "Science: Mathematics",
# "type": "boolean",
# "difficulty": "easy",
# "question": "A scalene triangle has two sides of equal length.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "category": "General Knowledge",
# "type": "boolean",
# "difficulty": "easy",
# "question": "A pasodoble is a type of Italian pasta sauce.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# }
# ]
