.. include:: ../../_resources.rst

.. _kotori-release:

##################
Make a new release
##################


Update changelog
================
Reflect the upcoming release within the ``CHANGES.rst`` file in the
root directory of the repository. Then, commit the changes to this file.


Cut release
===========
Bump version number in various files, commit them, add tag reflecting
the version number and finally push the repository to its origin::

    make release bump=minor

.. note:: We try to adhere to `Semantic Versioning`_.


Build and publish packages
==========================
After cutting a release, we're ready to proceed to :ref:`kotori-build`.
