# Sample Calculator

Sample Calculator is a command line tool to calculate characteristic values of a sample.

It provides the following features:
- Reading sample values from command line and CSV (Colon Separated Values) files.
- Performing statistic calculations such as average, variance, and deviation.
- Configurable logging of results and interim results.
- Easy integration of new input sources and calculations.

> **Please note:**
> The current version is only an initial alpha version which is **NOT** suited for production use.

## How can I use it?

We assume that you have installed the following tools:

- [Python >= 3.6.1](https://www.python.org/downloads/)
- [Git command line client](https://git-scm.com/downloads)

### 1. Checkout the code

`git clone <GIT REPOSITORY URL>`

### 2. Run the script

```
cd sample-calculator
python sample_calculator.py example-data/sample-values.csv
average: 3
variance: 2.5
deviation: 1.581138830084189665999446772
```

You can run it without input file as well.
In this case you are asked to enter the sample values manually.
For more information on the used CSV format, see [the provided example input file](example-data/sample-values.csv). 

## Contributing

Please see the [contribution guidelines](CONTRIBUTING.md) if you want to contribute.

## Changes

Please see the [Changelog](CHANGELOG.md) for notable changes.
