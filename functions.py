from time import sleep, time as currentTime

def getInput(msg):
    text = input(msg)
    sleep(1)

    return text

def log(startT, letter):
    print(f'{letter} - ASCI {ord(letter)} [{round(currentTime() - startT, 2)}s]')

def stats(startT, text):
    print(f'Words: {len(str.split(text))}')
    print(f'WPM: {round(len(str.split(text)) / round(currentTime() - startT, 2) * 60, 2)}wpm')
    print(f'Time: {round(currentTime() - startT, 2)}s')

    return input('')
