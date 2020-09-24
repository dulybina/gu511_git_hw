import datetime
 
def hello_world():
    print('hello world!')
    now = datetime.datetime.now()
    print(f'it is {now}')
 
if __name__ == "__main__":
    hello_world()
