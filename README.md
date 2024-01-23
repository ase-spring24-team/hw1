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

## Team members:

- Sai Raj Thirumalai (sthirum4)
- Sam Kwiatkowski-Martin (slkwiatk)
- Sathiya Narayanan Venkatesan (svenka32)
