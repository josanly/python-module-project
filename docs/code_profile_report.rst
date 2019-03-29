Code profile report
===================

.. note:: To generate the actual profile of sample:

    .. code:: bash

       ./gradlew profiling
       # or with specific parameters
       ./gradlew profiling -Pfoo='test' -Pbar=10

Profile:

.. graphviz:: ../build/profiles/python-module-project_profile.dot

Generated from :

.. code:: bash

   # from profiling task
