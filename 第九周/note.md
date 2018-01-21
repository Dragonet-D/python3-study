#> aa
    志不坚者智不达
    
#> 线程
    线程是操作系统能够进行运算调度的最小单位.它包含在进程之中,是进程中的实际运作单位.一条线程指的是进程中一个单一顺序的控制流,一个进程中可以并发多个线程,每条线程并行执行不同的任务.
    是一串指令的集合

#> 知识
    CPU负责运算;
    线程就是操作系统调用的最小单位;
    时钟频率 每秒钟执行27亿次的运算 2.7GHZ;
    画图软件的内存不能访问QQ的内存, 为了安全;
    每一个程序的内存是独立的,互相不能直接访问的;

#> 进程
    qq要以一个整体的形式暴露给操作系统管理,里面包含对各种资源的调用,内存的管理,网络接口的调用等,对各种资源管理的集合,就可以成为进程
    进程要操作CPU,必须要先创建一个线程;
    进程就是这个屋子,我们每个在房间里面的每个人就是线程,房间各个位置就是内存空间,屋子里面很多其他的东西就是资源,数据,进程本身不会执行,只是资源的集合,一个进程至少要有一个线程;
    A thread线程 is an execution执行 context上下文, which is all the information a CPU needs to execute执行 a stream流 of instructions指令.
    线程就是CPU执行时所需要的

    Suppose假设 you're reading a book, and you want to take a break right now, but you want to be able to come back and resume恢复 reading from the exact point准确的位置 where you stopped. One way to achieve that is by jotting down the page number, line number, and word number. So your execution context for reading a book is these 3 numbers.

    If you have a roommate, and she's using the same technique, she can take the book while you're not using it, and resume reading from where she stopped. Then you can take it back, and resume it from where you were.

    Threads work in the same way. A CPU is giving you the illusion that it's doing multiple computations at the same time. It does that by spending a bit of time on each computation. It can do that because it has an execution context for each computation. Just like you can share a book with your friend, many tasks can share a CPU.

    On a more technical level, an execution context (therefore a thread) consists of the values of the CPU's registers.

    Last: threads are different from processes. A thread is a context of execution, while a process is a bunch of resources associated with a computation. A process can have one or many threads.

    Clarification: the resources associated with a process include memory pages (all the threads in a process have the same view of the memory), file descriptors (e.g., open sockets), and security credentials (e.g., the ID of the user who started the process).