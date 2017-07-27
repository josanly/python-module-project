# python-module-project

This is an example of python module.

* [Gradle](https://gradle.org/) manages the project depedencies and lets you to configure and automize tasks like documentation generation, unit tests, ...
* [Sphinx](http://www.sphinx-doc.org/en/stable/index.html) generates the project documentation.
* [Pytest](https://docs.pytest.org/en/latest/) manages unit tests.
* [Conda](https://conda.io/docs/intro.html): Package, dependency and environment management for any language: Python, R, Scala, Java, Javascript, C/ C++, FORTRAN

Gradle imports and installs locally a MiniConda env to install dependencies without any conflit with your favorite environment.

You don't need to install Gradle or Conda on your computer. Just use `gradlew` command (Gradle Wrapper). 

## Compile the Sphinx Documentation

A task **doc** is configured inside the `build.gradle` file. This task run the command `make` into the `docs/` directory to compile the documentation from `docs/Makefile`.

It will compile the doc into html, man and epud format.

```
$ ./gradlew doc
```


## Run unit tests using Pytest

In `tests/` folder, 2 unit test suites are available, one per module or sub-module. 


```
$ ./gradlew test
```

