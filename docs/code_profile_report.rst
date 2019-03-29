Code profile report
===================

.. note:: To generate the actual profile of mysqlBagManager:

    .. code:: bash

       ./gradlew profiling
       # or with specific parameters
       ./gradlew profiling -PsqlTask='myfile.task' -Pslots=10

Profile:

.. graphviz:: ../../build/profiles/python-module-project_profile.dot

Generated from :

.. code:: bash

   # from profiling task
