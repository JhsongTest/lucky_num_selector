import random

def getLotto():
    return random.sample(range(1,45+1), k=6)

if __name__ == '__main__':
    itv_times = int(input('Enter interval number: '))
    for i in range(itv_times):
        print(getLotto())