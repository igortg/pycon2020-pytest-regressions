
## About Me

## Rocky

In ESSS we have a strong testing culture...

## Whetting Your Appetite

So, let's get a quick glance on what I'll be showing in this talk...


### before...

### after...

...this single line, and make the test more complete, more maintanable and easier to 
debug in case of failure.

### 

Before we dive into the code, just a quick discussion about the concept
of Data Regression Testing.

### Resgression Testing

At first I thought in using just the term "Regressions Testing" for this talk

### Data regression testing

So, data regression testing mean that we'll prevent regression by comparing
the output data. 

I couldn't find the term "data regression" in any of the
"classical literature", but I found some blog posts that indicate many teams 
do that. 

### pytest
Our implementation of data regression testing is... 

I'll find out that the concept is far from complex, so we can implement a version 
of it for other testing framework.

### pytest graph

Having sad that.... pytest is the de facto testing framework for Python right now

### When "test first" doesn't fit

There's this rule from TDD... 

but there are cases where this is not possible, or is very hard to do. In
some complex areas like machine learning and numerical simulation you'll
be facing this situation more often than not.

# Bezier

So, I'll be using one of these cases as an example

# Naive approach

In the "test first" approach