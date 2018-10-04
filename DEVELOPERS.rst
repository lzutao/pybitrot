Development mode
================

To install project in development mode, use command::

    python setup.py develop

Example::

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

To uninstall when already installed in development mode, type::

    % py setup.py develop --uninstall --user
    running develop
    Removing /home/user/.local/lib/python2.7/site-packages/pybitrot.egg-link (link to .)
    Removing pybitrot 0.1.0 from easy-install.pth file

Upload package to PIP
=====================

Read more about it in `this link <https://packaging.python.org/tutorials/packaging-projects/>`_.

Generating distribution archives
--------------------------------

The next step is to generate distribution packages for the package.
These are archives that are uploaded to the Package Index and can
be installed by pip.

Make sure you have the latest versions of ``setuptools`` and ``wheel``
installed::

    python3 -m pip install --user --upgrade setuptools wheel

**Tip**: IF you have trouble installing these, see the
`Installing Packages <https://packaging.python.org/tutorials/installing-packages/>`_
tutorial.

Now run this command from the same directory where ``setup.py`` is located::

    python3 setup.py sdist bdist_wheel

This command should output a lot of text and once completed should
generate two files in the dist directory::

    dist/
      example_pkg-0.0.1-py3-none-any.whl
      example_pkg-0.0.1.tar.gz


The ``tar.gz file`` is a source archive whereas the ``.whl`` file is a
built distribution. Newer pip versions preferentially install built distributions,
but will fall back to source archives if needed. You should always upload a source
archive and provide built archives for the platforms your project is compatible with.
In this case, our example package is compatible with Python on any platform so only
one built distribution is needed.

Uploading the distribution archives
-----------------------------------

Finally, it's time to upload your package to the Python Package Index!

The first thing you'll need to do is register an account on PyPI.

Now that you are registered, you can use twine to upload the distribution packages.
You'll need to install Twine::

    python3 -m pip install --user --upgrade twine

Once installed, run Twine to upload all of the archives under ``dist``::

    twine upload dist/*

You will be prompted for the username and password you registered with PyPI.
After the command completes, you should see output similar to this::

    Enter your username: [your username]
    Enter your password:
    Uploading distributions to https://upload.pypi.org/legacy/
    Uploading pybitrot-0.1.0-py3.6.egg
    100%|██████████████████████████████████| 7.84k/7.84k [00:01<00:00, 4.97kB/s]

**Note**: Remove the ``dist`` folder, and regenerate the archives.
