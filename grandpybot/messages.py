import random

def random_messages():
    """from a list, select randomly a message added before wiki extract """

    messages = ["le savais-tu? ", "Ah! il y a quelque chose à savoir à propos de ce lieu. ", "Mes transistors s'affole! je me souviens de quelque chose à propos de ce lieu. "]

    return random.choice(messages)

if __name__ == "__main__":
    print(random_messages())
