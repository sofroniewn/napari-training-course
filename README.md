# napari-training-course

Lectures for a napari training course

# setup

We will be using a conda environment for this course. If you have never seen
conda environments, Robert Haase provides a simple introduction in [this
lecture](https://www.youtube.com/watch?v=MOEPe9TGBK0). You can get miniconda
[here](https://docs.conda.io/en/latest/miniconda.html).

## create a conda environment for the course (recommended)

We have provided a pre-defined environment for you to use. You can create it
with the command:

```python
conda env create -f environment.yml
```

And then activate it with:

```python
conda activate napari
```

## use a pre-existing conda environment

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
