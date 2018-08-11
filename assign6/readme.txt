Elizabeth Han
004815046
readme.txt

To make the srt implementation more efficient, we made the code multithreaded, 
by linking with lpthread (adding -lpthread to the CFLAGS section of the
 makefile) and modifying the main.c file.

In the original code, the main function calculates the color values of each 
pixel in the image individually.  This work can be divided up between multiple
threads to make printing the final image significantly faster.

I had a bit of difficulty trying to divide the work.  I first divided the total
amount of pixels (131*131, or 17161 pixels) by the number of thread specified, 
and then tried to work out at exactly what pixel each thread had to start at 
for each thread to have an equal amount of work. Eventually, I figured it might
 be easier to allow only full columns instead of using quarter-or-half-or-third
-or-however-it-divides-columns.  

I toyed with the idea of having a loop calculate the number of columns and the
starting columns each column had to have and storing the results in a global
array that the thread routine could access.  I ended up deciding to save the
thread id of each thread in an array, and have so that every n thread
calculated the colors any n*mth column (m being any number), stopping when n*m
 exceeded the number of columns.

This was all stored in a global 3D array, that contained the x,y coordinates of
each pixel as well as its three associated color values.

I also originally had the thread ids and the thread_t arrays be dynamic arrays.
That was causing issues, but for some reason p_thread numThreads[nthreads] and 
int thread_id[nthreads] worked well enough.  It might have something to do with 
the fact that nthreads is, essentially, an argument passed in through argv.  It 
might have something to do with the fact that I used threads.  Will have to 
figure out why at a later date.

After all this, I somehow had a segmentation fault.  After a bit of searching,
 I realized that I was creating the scene after I created the threads that used 
the scene, which was a bit of an issue.  I moved around some other lines as,
which somehow affected the code working.

I'd say that this srt implementation worked fairly well.  Before making the 
code multithreaded, timing the srt implementation had:
  
real	0m43.889s
	user	0m43.879s
	sys	0m0.003s

Essentially, the results of the implementation using only one thread. When
using multiple threads: 

2 threads:
real    0m21.477s
user    0m42.854s
sys     0m0.001s

4 threads:
real    0m11.478s
user    0m45.110s
sys     0m0.000s

8 threads:

The actual elapsed time it takes to perform the srt implementations gets 
progressively shorter with each addition of a thread, though a certain point,
the execution will slow down as the threads begin to exceed the amount of 
cores.  

For example, when testing 70 threads, we can see that the real time is:
	real	0m2.934s
But when testing 75 threads, we see:
	real	0m2.869s


