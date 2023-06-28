from collections import deque

def person_is_seller(char_name):
    return char_name[-1] == 'r'

char_graph = {"Shepard": ["Garrus", "Liara", "Wrex"],
              "Garrus": ["Grunt"],
              "Liara": ["Grunt", "Shadow Broker"],
              "Wrex": ["Mordin", "Tali"],
              "Shadow Broker": [],
              "Grunt": [],
              "Mordin": [],
              "Tali": []}

def search_seller(char_name):
    search_queue = deque()
    search_queue += char_graph[char_name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return print(person + " is a mango seller!")
            else:
                search_queue += char_graph[person]
                # А также этот персонаж "person" добавляется в список "searched",
                # чтобы избежать повторной проверки этого персонажа.
                # ----------
                # And also this character "person" is added to the list "searched"
                # to avoid re-checking this character.
                searched.append(person)
    return print("There is no mango seller among the characters")
search_seller("Shepard")