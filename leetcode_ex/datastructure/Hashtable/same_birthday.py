import random
import time


def calc_prob_same_birthday():
    TRAILS = 100000
    same_birthdays = 0
    for _ in range(TRAILS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)
    print(f'{same_birthdays / TRAILS * 100}%')


def main():
    start = time.time()
    calc_prob_same_birthday()
    end = time.time()
    print(end-start, " sec")


if __name__ == "__main__":
    main()
