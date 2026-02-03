# Asynchronous Code
Asynchronous code just means that the language has a way to tell the computer / program that at some point in the code, it will have to wait for something else to finish somewhere else.   
That "wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

- the data from the client to be sent through the network
- the data sent by your program to be received by the client through the network
- the contents of a file in the disk to be read by the system and given to your program
- the contents your program gave to the system to be written to disk
a remote API operation
- a database operation to finish
- a database query to return the results
- etc.

It's called "asynchronous" because the computer / program doesn't have to be "synchronized" with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work.  
For "synchronous" (contrary to "asynchronous") they commonly also use the term "sequential", because the computer / program follows all the steps in sequence before switching to a different task, even if those steps involve waiting.  
This idea of asynchronous code described above is also sometimes called "concurrency". It is different from "parallelism".  
Concurrency and parallelism both relate to "different things happening more or less at the same time"  

## Is concurrency better than parallelism?
Concurrency is different than parallelism. And it is better on specific scenarios that involve a lot of waiting. Because of that, it generally is a lot better than parallelism for web application development. But not for everything.

## Concurrency + Parallelism: Web + Machine Learning 
With FastAPI you can take advantage of concurrency that is very common for web development (the same main attraction of NodeJS).  
But you can also exploit the benefits of parallelism and multiprocessing (having multiple processes running in parallel) for CPU bound workloads like those in Machine Learning systems.

# Async and Await
Modern versions of Python have a very intuitive way to define asynchronous code. This makes it look just like normal "sequential" code and do the "awaiting" for you at the right moments.  
When there is an operation that will require waiting before giving the results and has support for these new Python features, you can code it like:

```python
burgers = await get_burgers(2)
```

The key here is the `await`. It tells Python that it has to wait for `get_burgers(2)` to finish doing its thing before storing the results in burgers. With that, Python will know that it can go and do something else in the meanwhile (like receiving another request).

For await to work, it has to be inside a function that supports this asynchronicity. To do that, you just declare it with `async def`:

```python
async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
```

With async def, Python knows that, inside that function, it has to be aware of await expressions, and that it can "pause" the execution of that function and go do something else before coming back.

## How do you call the first async function?
If you are working with FastAPI you don't have to worry about that, because that "first" function will be your path operation function, and FastAPI will know how to do the right thing.

# Coroutines
Coroutine is just the very fancy term for the thing returned by an `async def` function.   
But all this functionality of using asynchronous code with async and await is many times summarized as using "coroutines". It is comparable to the main key feature of Go, the "Goroutines".


