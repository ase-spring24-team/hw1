# Automated Software Engineering - Homework Week 2

## Quick Guide
To run use the following commands:
```
cd src
```
Usage: 
```
python gate.py [OPTIONS]
```

Options:
```
    -c --cohen  small effect size               = .35
    -f --file   csv data file name              = ../data/auto93.csv
    -h --help   show help                       = False
    -k --k      low class frequency kludge      = 1
    -m --m      low attribute frequency kludge  = 2
    -s --seed   random number seed              = 31210
    -t --test   start up action                 = help
```
To view help:
```
python gate.py -h
```
To list all available tests:
```
python gate.py -t egs
```
To run all tests:
```
python gate.py -t all
```

## Homework Tasks
### HW2
#### Task 1
To get the stats:
```
 python gate.py -f ../data/auto93.csv -t stats
```
### HW3
#### Task 1
To print the little ascii table:
```
python gate.py -f ../data/diabetes.csv -t ascii_table
python gate.py -f ../data/soybean.csv -t ascii_table
```
#### Task 3
To execute bayes on `diabetes.csv`:
```
python gate.py -t bayes
```
#### Task 4
To explore low frequency settings on `soybean.csv`:
```
python gate.py -t km
```
- Recommended low frequency settings for `soybean.csv` are `k=2` and `m=1`, as they return the best accuracy of 85%.
- Accuracy of 73% is obtained on `diabetes.csv` for low frequency settings `k ∈ {0,1,2,3}` and `m ∈ {0,1,2,3}`

### HW4
#### Question 1
Does SMO do better than the random baselines?

Answer: 
First, look to [Link Text](hw/w4/gate20.out)

#### Question 2
How many y row evaluations are required for finding the absolute best?

Answer: The number of evaluations required finding the absolute best is `O(#yColumns × #Data)`. For the the `auto93.csv` file, `#yColumns = 3` and `#Data = 398`. So the number of evaluation is `1194`.

#### Question 3
How does SMO do compared to absolute best?

Answer:

Our sample data shows that SMO does quite well. It often produces optimal rows nearly equal to the absolute best row calculated by evaluating all y values. Despite not being quite as perfect as the absolute best row, SMO can calculate these optimal rows in a fraction of the time. This is especially apparent when you consider that in the real world, evaluating each y-value may take a significant amount of time, and using SMO reduces the number of y-value evaluations significantly.

## Team members:

- Sai Raj Thirumalai (sthirum4)
- Sam Kwiatkowski-Martin (slkwiatk)
- Sathiya Narayanan Venkatesan (svenka32)
