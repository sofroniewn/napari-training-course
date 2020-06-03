# napari-training-course

Lectures for a napari training course

# setup

Start by downloading this repository. If you already use git, you can use the
following command to clone this repository to your local machine:

```
git clone https://github.com/sofroniewn/napari-training-course
```

If you don't already use git, you can download the whole repository as a zip
file, which you can then unzip on your computer. The file is available at:

https://github.com/sofroniewn/napari-training-course/archive/binder.zip

You also need a working Python installation. We will be using a conda
environment for this course. If you have never seen conda environments, Robert
Haase provides a simple introduction in [this
lecture](https://www.youtube.com/watch?v=MOEPe9TGBK0). You can get miniconda
[here](https://docs.conda.io/en/latest/miniconda.html).

Once you have a working conda installation, you have two options. The second
one should work in non-conda environments but only do this if you know what you
are doing!

## 1. create a conda environment for the course (recommended)

We have provided a pre-defined environment for you to use. You can create it
with the command:

```python
conda env create -f environment.yml
```

And then activate it with:

```python
conda activate napari
```

## 2. use a pre-existing conda environment

If you have a pre-existing environment that you would like to use for the
course, you should install napari, scikit-image, and tifffile:

```
pip install napari[all] scikit-image tifffile[all]
```

or you can use our provided requirements.txt file:

```
pip install -r requirements.txt
```

Of course, after the course, you can `pip install napari` into your preferred
environment.

## checking that your napari install is working

Once you have installed napari, you should test that your install is working in
two ways:

- type `napari` into a terminal with your activated environment. This should
  launch an empty napari window. You can close this window.
- navigate to the downloaded course folder (the folder containing this README
  file) and type `python check-setup.py`. Again, make sure your environment is
  activated. You should be able to see napari displaying an image of some
  cell nuclei.

## if you can't get napari to work

Because napari uses OpenGL and GPUs to render images, and there is such a huge
variety of operating systems and hardware around, it can sometimes be
challenging to get napari working on your machine. Because of the limited time
for the course, we will probably not have time to troubleshoot installation
issues during the lecture, but we will endeavour to help you get it running
before or after the course.

If you don't have a running environment before the course, you can launch this
repository on the cloud by clicking on the Binder link below. It can take time
to get the remote virtual machine to boot, so click on this link at least 15
minutes before the course starts.

**IMPORTANT NOTES WHEN RUNNING ON BINDER**

- Things are much slower on Binder, including initializing the Qt event loop.
  What this means is that you should **wait at least 5 seconds** after running
  the cell containing `%gui qt` before running any napari cells. **If you don't
  do this, you will need to restart the notebook from scratch!**
- To get the desktop on Binder, **before starting any notebooks**, click on
  "New → desktop" at the top right of the file list. This will open a desktop
  in a new tab. We recommend dragging the tab out to make it a separate window.
  Then, start the notebooks from the original file list tab. napari windows
  created from the notebooks will appear in the desktop browser window.
- Because these windows are running on a remote desktop, the performance is not
  as smooth as using local napari, but it should give you a sense of its
  capabilities and allow you to follow along with the lessons.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sofroniewn/napari-training-course/master)
