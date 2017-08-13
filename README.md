# python-module-project

This is an example of python module.

* [Gradle](https://gradle.org/) manages the project depedencies and lets you to configure and automize tasks like documentation generation, unit tests, ...
* [Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is a tool that makes it easy to create intelligent and beautiful documentation.
* [Pytest](https://docs.pytest.org/en/latest/) makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. 
* [Pytest-Cov](https://github.com/pytest-dev/pytest-cov) computes test coverage (Pytest plugin).
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

## Code Profiling

The gradle task **profiling** generates a DAG from profile of code execution.
It will integrate the output (dot and commands) into the technical documentation (docs/code_profile_report.rst).

The `docs/code_profile_report.rst` file has been added to git repository but we don't want to follow runtime modifications.
To do that we use the command `git update-index --assume-unchanged [file]` (refer to [StackOverflow answer](https://stackoverflow.com/a/11430092)).
If you do any global modification (like general contents) into this file you have to run `git update-index --no-assume-unchanged [file]`

```
# generate profile
./gradlew profiling
# compile documentation
./gradlew doc
# or
./gradlew profiling doc
```

## Create a new release

It's simple to create a release of source code using gradle and git.

```
./gradlew createRelease -PtagName="myVersion" -PtagLog="git tag message"
# it will create a tag and a archive into relases/ folder
# or using git directly
git tag -a 3.0.0 -m 'my python package version 3.0.0'
mkdir releases/
git archive --format=tar.gz --prefix=mysample-3.0.0-src/ 3.0.0 >releases/mysample-3.0.0.tar.gz
```

If you want to propagate tags to your remote repository don't forget to push it: `git push -u <remote> --tags`

## Local PyPi server

If you want to use a local Pypi Server embedded into miniconda env in this repository,
you need to have \ **htpasswd**\  installed on your device.

### Installation (MiniConda env)

The Conda package **pypiserver** is available into miniconda env.
[GitHub repository](https://github.com/pypiserver/pypiserver)

To setup the Pypi Server, launch the gradle task: setupLocalPypiServer (see *Apache-like authentication* for futher details).

```
./gradlew setupLocalPypiServer
# If you want to change the password define into gradle.properties file
# you can pass it from the command line
./gradlew setupLocalPypiServer -PpypiServerPasswd=password
```

### Apache-like authentication (htpasswd)

If you don't have `htpasswd` installed on your device:

```
# RedHad System
# CentOS
yum install httpd-tools
# Fedora
dnf install httpd-tools

# Debian System
apt-get install apache2-utils
```

Create the Apache htpasswd file with at least one user/password pair with this
command (you'll be prompted for a password):

```
htpasswd -sc htpasswd.txt <some_username>
```

or if you have bogus passwords that you don't care because they are for an
internal service (which is still "bad", from a security prespective...)
you may use this public service: [htpasswd-generator](http://www.htaccesstools.com/htpasswd-generator/)

