Python Interview Questions
============================

Memory Management in Python
    Python is a high-level programming language that’s implemented in the C programming language. The Python memory manager manages Python’s memory allocations. There’s a private heap that contains all Python objects and data structures. The Python memory manager manages the Python heap on demand. The Python memory manager has object-specific allocators to allocate memory distinctly for specific objects such as int, string, etc… Below that, the raw memory allocator interacts with the memory manager of the operating system to ensure that there’s space on the private heap.
    The Python memory manager manages chunks of memory called “Blocks”. A collection of blocks of the same size makes up the “Pool”. Pools are created on Arenas, chunks of 256kB memory allocated on heap=64 pools. If the objects get destroyed, the memory manager fills this space with a new object of the same size.
    Methods and variables are created in Stack memory. A stack frame is created whenever methods and variables are created. These frames are destroyed automatically whenever methods are returned.
    Objects and instance variables are created in Heap memory. As soon as the variables and functions are returned, dead objects will be garbage collected.
    It is important to note that the Python memory manager doesn’t necessarily release the memory back to the Operating System, instead memory is returned back to the python interpreter. Python has a small objects allocator that keeps memory allocated for further use. In long-running processes, you may have an incremental reserve of unused memory.

