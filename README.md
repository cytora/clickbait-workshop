# PyData 2017 Workshop

Materials for PyData workshop demonstrating the basic components of a
text learning pipeline. The aim of the workshop is to build all

## Installation

The easiest way to get python and the necessary packages is with
conda. [Go here](conda.io/docs/download.html) for installation instructions. Be
sure to get the python 3 versions.

Now we create a new conda environment from the environment file that contains the dependencies
```
$ conda env create -f environment.yml
$ source activate textml
$ python tests/test.py
```

## Getting started

Launch the jupyter notebook to get started!

```
$ jupyter notebook tutorial.ipynb
```

In the notebook you'll learn to construct a text classification pipeline.
After that you can look at the `webservice` directory for an example of
providing machine learning as a service. The classifier is also used in
`advanced.ipynb` to explore news data.
