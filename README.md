# python-module-project

This is an example of python module.

* [Gradle](https://gradle.org/) manages the project depedencies and lets you to configure and automize tasks like documentation generation, unit tests, ...
* [Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is a tool that makes it easy to create intelligent and beautiful documentation.
* [Pytest](https://docs.pytest.org/en/latest/) makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
* [Conda](https://conda.io/docs/intro.html): Package, dependency and environment management for any language: Python, R, Scala, Java, Javascript, C/ C++, ...

Gradle imports and locally installs a MiniConda env with all required dependencies without any conflit with your favorite environment.

You don't need to install Gradle or Conda on your computer. Just use `gradlew` command (Gradle Wrapper), and all binaries will be downloaded. 

## Compile the Sphinx Documentation

A task **doc** is configured inside the `build.gradle` file. This task run the command `make` into the `docs/` directory to compile the documentation from `docs/Makefile`.

It will compile the doc into html, man and epub format.

```
# compile the full documentation
$ ./gradlew doc
# or compile without code profiling, test coverage, ...
$ ./gradlew docOnly
```


## Run unit tests using Pytest

In `tests/` folder, two unit test suites are available, one per module or sub-module. The test coverage is computed at the end.


```
$ ./gradlew test
```

## Optimize your code

### Generate a profil of your code

The command `./gradlew profiling` will run your module using cProfile and gprof2dot python modules. 
Then, a dot graph will be generated (available in `build/profiles` folder) and be integrated in the documentation.

See [gprof2dot](https://github.com/jrfonseca/gprof2dot) for futher details and examples.
