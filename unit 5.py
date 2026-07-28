#Unit 5 The High-Score Tracker Game

while True:
    score = input("Enter a game score next to the flashing cursor")
    if score == "stop":
        print("Game session ended!")
        break
    else:
        score = int(input("Enter a game score next to the flashing cursor number"))
        if score > 100:
            print("Wow! Thats a new high score!")
        elif score < 100:
            print("Good try, keep playing!")
