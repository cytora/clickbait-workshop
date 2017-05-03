# PyData 2017 Workshop

Materials for PyData workshop demonstrating the basic components of a
text learning pipeline. The aim of the workshop is to build all

## Installation

The easiest way to get python and the necessary packages is with
conda:
```
$ sh install_miniconda.sh
```

Now we create a new conda environment and activate it
```
$ conda create -n textml python=3 pandas matplotlib scikit-learn flask jupyter
$ source activate textml
```

## Getting started

Launch the jupyter notebook to get started!

```
$ jupyter notebook workshop.ipynb
```

In the notebook you'll learn to construct a text classification pipeline.
After that you can look at the `webservice` directory for an example of
providing machine learning as a service. The classifier is also used in
`exploring_classification.ipynb` to explore news data.
