from time import sleep


def intro_text(text):
    """Prints title of game in a typewriter style"""
    words = text

    for char in words:
        sleep(0.25)
        print(char, end="", flush=True)

intro_text("balls")