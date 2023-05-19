import time
import random


def time_play(delta: int) -> float:  # the waiting or on time game
    start_typing = input()
    while start_typing != '':
        start_typing = input()
    start_time = time.time()
    end_typing = input()
    while end_typing != '':
        end_typing = input()
    end_typing = time.time()

    if int(end_typing - start_time) > delta:
        print("Too slow")
    elif int(end_typing - start_time) < delta:
        print("Too fast")
    else:
        print("On time!")

    return end_typing - start_time


def on_time_game():
    target = random.randint(2, 4)  # integer between 2 and 4
    print('\nYour target time is {} second'.format(target))

    input('--Press Enter to Begin--')
    start = time.perf_counter()

    input('\n...Press Enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start

    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))

    if elapsed == target:
        print("U are on time")
    elif elapsed < target:
        print('{0:.3f} seconds too fast'.format(target - elapsed))
    else:
        print('{0:.3f} seconds too slow'.format(elapsed - target))


# delta = int(input("Enter time in seconds for waiting: "))
# print("Waiting time is", delta)
# print("Time measure: ", time_play(delta))


on_time_game()