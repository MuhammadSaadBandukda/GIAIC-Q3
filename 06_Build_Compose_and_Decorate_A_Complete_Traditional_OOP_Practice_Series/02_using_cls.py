class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f'Total instances are {cls.count}')
    

def main():
    c1 = Counter()
    c1.display_count()
    c2 = Counter()
    c2.display_count()
    c3 = Counter()
    c1.display_count()
    c3.display_count()


if __name__ == '__main__':
    main()
