from pyboy import PyBoy

def start_game(num_games):
    count = 0
    pylist_pyboy = []
    for i in range(num_games):
        pylist_pyboy.append(i)
    print(pylist_pyboy)
    for i in range(len(pylist_pyboy)):
        pylist_pyboy [i] = [PyBoy("Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb")]
    num_games -= 1
    while True:
        while count <= num_games:
            pylist_pyboy[count][0].tick()

            if len(pylist_pyboy) >1:
                if count <= num_games:
                    count += 1

        count = 0

if __name__ == '__main__':
    start_game()
