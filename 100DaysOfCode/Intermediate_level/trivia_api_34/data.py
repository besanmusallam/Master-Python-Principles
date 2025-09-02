import requests

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_data =    [
#      {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "General Knowledge",
#       "question": "Dihydrogen Monoxide is a dangerous chemical.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "Amazon acquired Twitch in August 2014 for $970 million dollars.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "In the game &quot;Until Dawn&quot; Emily is the only playable character who can be killed by another playable character directly.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Cucumbers are usually more than 90% water.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "hard",
#       "category": "Science: Mathematics",
#       "question": "In Topology, the complement of an open set is a closed set.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "The French word to travel is &quot;Travail&quot;",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "In &quot;Super Mario World&quot;, the rhino mini-boss, Reznor, is named after the lead singer of the band &quot;Nine Inch Nails&quot;.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "In &quot;Call Of Duty: Zombies&quot;, you can upgrade the &quot;Apothicon Servant&quot; in the &quot;Shadows Of Evil&quot; map.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "hard",
#       "category": "History",
#       "question": "Japan was part of the Allied Powers during World War I.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "History",
#       "question": "Brezhnev was the 5th leader of the USSR.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "Entertainment: Film",
#       "question": "In the movie The Revenant, DiCaprio&#039;s character hunts down the killer of his son.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "&quot;Return to Castle Wolfenstein&quot; was the only game of the Wolfenstein series where you don&#039;t play as William &quot;B.J.&quot; Blazkowicz.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Geography",
#       "question": "Vietnam is the only country in the world that starts with V. ",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "Geography",
#       "question": "Alaska is the largest state in the United States.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "hard",
#       "category": "Mythology",
#       "question": "Janus was the Roman god of doorways and passageways.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     }
#   ]

