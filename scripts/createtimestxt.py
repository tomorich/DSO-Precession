#!/usr/bin/env python

def main():
    with open("times.txt",'w') as f:
        for i in range(2000):
            f.write(str(i)+' '+str(i*1.0/30.0)+'\r\n')
    print('aaa')






if __name__ == '__main__':
    main()
