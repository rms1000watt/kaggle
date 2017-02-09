<hidden cmd="cd $GOPATH/src/github.com/rms1000watt/kaggle"/>
<hidden cmd="git push https://rms1000watt@github.com/rms1000watt/kaggle.git master:master"/>

# Kaggle

Documents and Scripts for [Kaggle](http://www.kaggle.com) competitions.

## Repo Layout

Aside from the top level metadata, each folder is a separate competition. Each folder has a Readme with explanations.

## Installation

Python 2.7 should already be installed on your Non-Windows machine. To install the Python libraries:

```bash
sudo pip install -r ./requirements.txt
```

## Usage

Change directory to the project you want to look at, start `jupyter`, then look at the notebook, ie.

```bash
cd titanic
jupyter notebook
```
