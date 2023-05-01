import random

#result = random.sample(range(1, 46), k = 6)

def getLottoNum():
    return random.sample(range(1, 46), k = 6)

if __name__ == '__main__':
    print(getLottoNum())