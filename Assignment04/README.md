# Assignment03
 
Upload your url to your folder that you create.

1. Create a folder called "Assignment04"
2. The task is to compute an approximation to $\pi$ using [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method).

    Use no imports besides

    `import numpy as np`

    Your hints are as follows:

    * If $U$ is a bivariate uniform random variable on the unit square $(0,1)^2$, then the probability that $U$ lies in a subset $B$ of $(0,1)^2$ is equal to the area of $B$
    
    * If $U_1\ldots U_n$ are IID copies of $U$, then, as $n$ gets large, the fraction that falls in $B$, converges to the probability of landing in $B$.

    * For a circle $Area=\pi r^2$, 

    * You'll need `np.random.uniform()`
