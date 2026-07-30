class MoodError(Exception):
    pass

mood=["angry","sad","excited","disappointed"]
i=int(input("Enter your mood index(0-3): "))

if mood[i] == "disappointed":
    raise MoodError("She will beat me")
elif mood[i] == "angry":
    raise MoodError("She will not talk to me")
print("Mood:", mood[i])
