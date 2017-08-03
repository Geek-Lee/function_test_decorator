import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print("%s cost %s second"%(fn.__name__, time.clock() - start))
    return _wrapper

#这个装饰器可以在方便地统计函数运行的耗时。用来分析脚本的性能是最好不过了。
#这样用：

@time_me
def test():
    time.sleep(0.1)

@time_me
def test2():
    time.sleep(0.2)

test()
test2()

#test cost 0.1063977326290412 second
#test2 cost 0.19918087160151154 second
