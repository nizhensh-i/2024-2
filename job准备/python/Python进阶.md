协程

是一个函数。

名言---  

> **你孤注一掷写代码，要么完全避免阻塞，要么纯属浪费时间**

> &nbsp;你孤注一掷写代码，要么完全避免阻塞，要么纯属浪费时间**

解释： 因为协程， 使用 asyncio `/æsɪŋkioʊ/`的Python代码**只有一个执行流**，除非显示启动额外的线程和进程。这意味着，在任意一个时刻，都只有一个协程在执行。

想实现并发，则要把控制器由一个协程传给另外一个协程（通过**事件循环**来驱动其他待定协程）



并发：

派生一堆独立线程，通过队列收集结果





声名狼藉的**GIL**

1.对对象引用计数和解释器其他内部状态的访问受一个锁的控制，这个锁就是“全局解释器”（GIL）。

​    任意时间点上只有一个Python线程可以持有GIL。这意味着，任意时间点上只有一个线程可以执行Python代码，与CPU核数量无关。**每个Python进程都有自己的GIL**。

2.为了防止一个Python线程无限持有GIL，Python字节码解释器默认**每5毫秒暂停当前的线程，释放GIL**。被暂停的线程可以再次尝试获取GIL，但如果有其他线程等待，那么操作系统调度程序可能会从中挑选一个线程开展工作。

3.我们编写的代码无法控制GIL。但是，耗时的任务可有内置函数或C语言扩展释放。

4.Python**标准库发起的系统调用函数均可以释放GIL**。这包括所有执行磁盘I／Ｏ、网络Ｉ／Ｏ的函数，以及time.sleep()。以及Zlib,bz2执行压缩和解压操作的函数，也都释放GIL。

5.GIL对Python使用网络编程的影响较小，因为I/O函数释放GIL，而且与读写内存相比，网络读写的延迟始终很高。

6.若想在多核上运行CPU密集型Python代码，必须使用多个进程



多线程的实现

1.直接使用threading包的Thread类。将目标函数作为实例化Thread类的形参传进去

2.自己创建类继承Thread类，并重写run()函数	

线程中的**信号机制***： 使用threading.Event类





多进程的实现

1.直接使用multiprocessing包的Process类。将目标函数作为实例化Process类的形参传进去



协程的实现

1. 以    **async def **   定义的函数
2. 使用asyncio创建事件循环



并发执行器：

1.concurrent.futures模块的功能主要由ThreadPoolExecutor和ProcessPoolExecutor类提供。这两个类内部维护着一个工作线程或进程池，以及分配任务和收集结果的队列。

ThreadPoolExecutor.map方法:  返回一个生成器，通过迭代可以获取各个函数调用返回的值

~~~
with futures.ThreadPoolExecutor() as executor:         
	res = executor.map(download_one, sorted(cc_list))
~~~



也可以用executor.submit和future.as_completed代替ThreadPoolExecutor.map

以上两种方法的区别：ThreadPoolExecutor.map传入的是同一个可迭代对象，只是传递的参数不同。而用executor.submit可以传递不同的可迭代对象。





**实现进度条**

使用tqdm库。需要配合executor.submit和future.as_completed一起

~~~
      with futures.ThreadPoolExecutor() as executor:
            for url in sorted(all_url):
                res = executor.submit(fetch, url)
                task_list.append(res)

            done_iter = tqdm.tqdm(futures.as_completed(task_list), total=len(all_url))
            for future in done_iter:
                r = future.result()
~~~







原生协程：使用**async def**定义的协程函数。在原生协程中可以使用await关键字委托另外一个原生协程。await关键字不能在原生协程外部使用

经典协程：一种生成器函数，在表达式中使用**yield**读取my_coro.send(data)调用发送的数据。经典协程可以使用yield from 委托其他经典协程。经典协程不能由wait驱动，而且asynicio库不再支持



可异步调用对象：

for 关键字处理**可迭代对象**，await关键字处理**可异步调用对象**

两种常见的可异步调用对象：

1.原生协程对象，通过调用原生协程函数得到

2.asyncio.Task   通常把协程对象传给asyncio.create_task()得到



分析程序：理解常规函数和协程在程序中的作用

asynicio.gather(iters) : 接受的参数是一个或多个可异步调用对象，等待全部执行完毕，以可异步调用对象的提交顺序返回结果列表 





原生协程的秘密

1.asynicio事件循环在背后调用.send驱动你的协程，而你的协程使用await等待其他协程，包括库提供的协程（比如代码中使用了HTTPX库）。

使用asynicio.gather和asynicio.create_task等函数可以启动多个并发await通道，在单个线程内由单个事件循环驱动多个I/O 操作并发执行



异步上下文管理器

使用**asynic with**   ,以协程实现 \__aenter\__ 和\__aexit\__ 方法的对象。



信号量

应用：网络客户端应该限流，以免对服务器发起过多并发请求。使用**信号量**限制请求。

一个信号量可由多个协程持有，因此特别适用于限制活动的并发协程数量。



Python 标准库中有 3 个Semaphore 类，threading、multiprocessing 和 asyncio中各有一个，现在讨论的是最后一个。

asyncio.Semaphore 有一个内部计时器。每次使用 await 处理协程方法 .acquire()，计时器递减；每次调用 .release() 方
法（不是协程，因为永不阻塞），计时器递增。计时器的初始值在实例化 Semaphore 时设定。

~~~
semaphore = asyncio.Semaphore(concur_req)
~~~

一般不直接调用这些方法，把 semaphore 当作异步上下文管理器使用更安全

~~~
async with semaphore:
	image = await get_flag(client, base_url, cc)
~~~



使用协程逐个执行异步任务：

**await** 关键字： 一个异步请求**结束后**驱动另一个异步请求，共用驱动协程的局部作用域



把任务委托给执行器

在node.js中，为所有I/O提供了异步编程。但在Python中，只为网络I/O提供了异步编程，一不小心，那么文件I/O可以明显降低异步应用程序的性能水平，因为在主线程中读写存储器会阻塞事件循环

~~~
# >= 3.9
await asyncio.to_thread(save_flag, image, f'{cc}.gif')
~~~

