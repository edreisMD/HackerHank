

# Key Competencies: 

# Samples - Ability to obtain a sample mean. Sampling is a process used in statistical analysis in which a predetermined number of observations are taken from a larger group. A sample is refers to a smaller, manageable version of a larger group. 


# Outliers - An understanding of an outlier, an observation that lies an abnormal distance from other values in a random sample. 


# Statistical bias - Statistical bias is a feature of a statistical technique or of its results whereby the expected value of the results differs from the true underlying quantitative parameter being estimated. Basic familiarity with Selection bias, Survivorship bias, Omitted variable bias, Recall bias, Observer bias, and Funding bias.


# Common distributions - The distribution of a statistical data set is a listing or function showing all the possible values (or intervals) of the data and how often they occur. An understanding of basic types of distribution such as Bernoulli Distribution, Uniform Distribution, Binomial Distribution, Normal Distribution, Poisson Distribution, and Exponential Distribution.

# -- Binomial distribution
import math

def binomialDistribution(k, n, p): # where p is the probability of a successful trial
  return math.comb(n, k) * p ** k * (p-1) ** (n-k)

# -- Gemoetric distribution - special negative binomial distribution when you are looking for the first positive after n number of Bernoulli trials 

def geometricDistribution(n, p): # where p is the probability of a successful trial
  return (1-p) ** (n-1) * p

# -- Poison Distribution



# Central limit theorem - Familiarity with applying the Central Limit Theorem (CLT), which is a statistical concept that states that the sample mean distribution of a random variable will assume a near-normal or normal distribution if the sample size is large enough.

# Measures of Central tendency - A measure of central tendency is a single value that attempts to describe a set of data by identifying the central position within that set of data. 
# -- Mean - The mean is the average or the most common value in a collection of numbers. 

def mean(arr):
  return sum(arr) / len(arr)


# -- Median - In statistics and probability theory, the median is the value separating the higher half from the lower half of a data sample, a population, or a probability distribution. For a data set, it may be thought of as "the middle" value.

def median(arr):
  sortedArr = sorted(arr)
  if len(arr) % 2 != 0:
    return sortedArr[len(arr) // 2]
  return (sortedArr[len(arr) // 2] + sortedArr[(len(arr) -1) // 2]) / 2

# -- Mode - The mode is the value that appears most often in a set of data values.  

def mode(arr):
  dct = {}
  for i in arr:
    if not i in dct:
      dct[i] = 1
    else:
      dct[i] += 1
  return max(dct, key=dct.get)
  

# IQR - In descriptive statistics, the interquartile range, also called the mid-spread, middle 50%, or H‑spread, is a measure of statistical dispersion, being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles, IQR = Q₃ − Q₁.

# -- Quatiles

# -- Interquantile Range (or mid-spread, middle 50%, H-spread

# -- Range - The range of a set of data is the difference between the largest and smallest values.

# -- Variance - Variance is the expectation of the squared deviation of a random variable from its mean.

# -- Standard deviation - The standard deviation is a measure of the amount of variation or dispersion of a set of values. A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range.


# Bivariate Analysis - Bivariate analysis is a kind of statistical analysis when two variables are observed against each other. Ability to compute the Correlation, Covariance, Least Square method, Regression analysis, Goodness of fit.
# Commonly used error metrics - A statistical error is the (unknown) difference between the retained value and the true value. An understanding of some common error metrics: Mean Squared Error (MSE) Root Mean Square Error (RMSE) Mean Absolute Scaled Error (MASE). 
# Bias/Variance - In statistics and machine learning, the bias–variance tradeoff is the property of a model that the variance of the parameter estimates across samples can be reduced by increasing the bias in the estimated parameters.
# Type - 1 / Type - 2 - In statistical hypothesis testing, a type I error is the rejection of a true null hypothesis, while a type II error is the non-rejection of a false null hypothesis.
# Noise - Statistical noise refers to variability within a sample, stochastic disturbance in a regression equation, or estimation error. This noise is often represented as a random variable. Y = m (X ǀ θ) + ε, with E (ε) = 0, the random variable ε is called a disturbance or error term and reflects statistical noise.
# Regularization - Regularization refers to a wide variety of techniques used to bring structure to statistical models in the face of data size, complexity and sparseness. Regularization is used to allow models to usefully model such data without overfitting.
# Hypothesis Testing - A statistical hypothesis is a hypothesis that is testable on the basis of observed data modelled as the realised values taken by a collection of random variables. Familiarity with p-value and its applications, z-test, t-test (one and two sample), and chi-squared test.
