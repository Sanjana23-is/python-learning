# Q5. Weather Activity Suggestion:
# Sunny → Go for a walk, Rainy → Read a book, Snowy → Build a snowman

weather = input("enter weather:").lower()

match weather:
    case "sunny": 
        print("go for a walk")
    case "rainy":
        print("read a book")
    case "snowy":
        print("build a snowman")
    