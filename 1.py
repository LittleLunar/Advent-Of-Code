def run_test():
    f = open("input/1.txt",'r')
    t = f.read()
    measurements = [int(x) for x in t.split('\n')]
    increase_count = 0
    prev_measure = measurements[0]
    for i in measurements:
        if prev_measure < i:
            increase_count += 1
        prev_measure = i

    print(increase_count)

if __name__ == '__main__':
    run_test()