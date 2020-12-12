from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
  name='recviz',
  version='0.0.1',
  description='Simple visualization for recursive functions in Python.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/arpitbbhayani/recviz',
  author='Arpit Bhayani',
  author_email='arpit.b.bhayani@gmail.com',
  classifiers=[  # Optional
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 5 - Production/Stable',

      # Indicate who your project is intended for
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',

      # Pick your license as you wish
      'License :: OSI Approved :: MIT License',

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate you support Python 3. These classifiers are *not*
      # checked by 'pip install'. See instead 'python_requires' below.
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3 :: Only',
  ],

  keywords='function visualization, utility',

  # When your source code is in a subdirectory under the project root, e.g.
  # `src/`, it is necessary to specify the `package_dir` argument.
  package_dir={'': 'src'},  # Optional

  # You can just specify package directories manually here if your project is
  # simple. Or you can use find_packages().
  #
  # Alternatively, if you just want to distribute a single Python file, use
  # the `py_modules` argument instead as follows, which will expect a file
  # called `my_module.py` to exist:
  #
  #   py_modules=["my_module"],
  #
  packages=find_packages(where='src'),  # Required

  # Specify which Python versions you support. In contrast to the
  # 'Programming Language' classifiers above, 'pip install' will check this
  # and refuse to install the project if the version does not match. See
  # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
  python_requires='>=3.5, <4',

  # This field lists other packages that your project depends on to run.
  # Any package you put here will be installed by pip when your project is
  # installed, so they must be valid existing projects.
  #
  # For an analysis of "install_requires" vs pip's requirements files see:
  # https://packaging.python.org/en/latest/requirements.html
  install_requires=[],

  # List additional groups of dependencies here (e.g. development
  # dependencies). Users will be able to install these using the "extras"
  # syntax, for example:
  #
  #   $ pip install sampleproject[dev]
  #
  # Similar to `install_requires` above, these must be valid existing
  # projects.
  extras_require={  # Optional
      'dev': ['check-manifest'],
      'test': ['coverage'],
  },

  # If there are data files included in your packages that need to be
  # installed, specify them here.
  package_data={  # Optional
      'sample': ['package_data.dat'],
  },

  data_files=[],

  project_urls={
      'Bug Reports': 'https://github.com/arpitbbhayani/recviz/issues',
      # 'Funding': 'https://donate.pypi.org',
      # 'Say Thanks!': 'http://saythanks.io/to/example',
      'Source': 'https://github.com/arpitbbhayani/recviz',
  },
)
