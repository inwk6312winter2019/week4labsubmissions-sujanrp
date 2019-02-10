class time:
   def print_time(t):
       print("Time is %.2d:%.2d:%.2d"%(t.hour,t.minute,t.second))

def main():
    t=time()
    t.hour=12
    t.minute=5
    t.second=9
    print_time(t)

if __name__ == '__main__':
    main()
