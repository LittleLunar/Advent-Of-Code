def run_test():
    f = open("input/2.txt",'r')
    str_inp = f.read()
    measurements = [int(x) for x in str_inp.split('\n')]
    increase_count = 0
    for i in range(1,len(measurements) - 2):

        prev_win = measurements[i-1] + measurements[i] + measurements[i+1]
        cur_win = measurements[i] + measurements[i+1] + measurements[i+2]

        if prev_win < cur_win:
            increase_count += 1

    print(increase_count)

if __name__ == '__main__':
    run_test()
