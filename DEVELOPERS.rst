Development mode
================

To install project in development mode, use command:

.. code:: bash

    python setup.py develop

Example:

.. code:: bash

    % py setup.py develop --user
    running develop
    running egg_info
    writing pybitrot.egg-info/PKG-INFO
    writing top-level names to pybitrot.egg-info/top_level.txt
    writing dependency_links to pybitrot.egg-info/dependency_links.txt
    file pybitrot.py (for module pybitrot) not found
    reading manifest file 'pybitrot.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'pybitrot.egg-info/SOURCES.txt'
    running build_ext
    Creating /home/user/.local/lib/python2.7/site-packages/pybitrot.egg-link (link to .)
    pybitrot 0.1.0 is already the active version in easy-install.pth

    Installed /myproject/pybitrot
    Processing dependencies for pybitrot==0.1.0
    Finished processing dependencies for pybitrot==0.1.0

To uninstall when already installed in development mode, type:

.. code::bash

    % py setup.py develop --uninstall --user
    running develop
    Removing /home/user/.local/lib/python2.7/site-packages/pybitrot.egg-link (link to .)
    Removing pybitrot 0.1.0 from easy-install.pth file

