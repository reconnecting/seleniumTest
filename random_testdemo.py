import time




def time_sleep_decorator(func):
    def wrapper(*args,**kwargs):
        print("系统等待3秒")
        time.sleep(3)
        return func(*args,**kwargs)
    print("看看执行顺序")
    return wrapper

@time_sleep_decorator
def menthod_test():
    print("这是被装饰的函数")

def iter_dict(dict):
    for x, y in dict.items():
        print(x,y)


def get_unique(target):
    container = {}
    for x in target:
        if x in container:
            container[x] +=1
            if container[x]>=5:
                print(x,container[x])
                break
        else:
            container[x] =1
    print(container)

def fibo(target):
    a =0
    b=1
    for x in range(target-1):
        a ,b =b,a+b
    print(b)


def test_2():
    pass

if __name__ == '__main__':
    fibo(10)