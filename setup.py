# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

requires_core = [
    'Twisted[tls]==17.1.0',
    'pyOpenSSL==16.2.0',
]

if sys.platform == 'darwin':
    requires_core = [
        'Twisted==17.1.0',
    ]

requires = requires_core + [

    # Core
    #'Twisted[tls]==17.1.0',
    #'Twisted==17.1.0',
    'pyramid==1.5.7',               # 1.8.3
    'pyramid_jinja2==2.5',          # 2.7
    'cornice==1.0.0',               # 1.2.1, 2.4.0
    'simplejson==3.8.2',            # 3.10.0
    'Jinja2==2.8',                  # 2.9.5
    'Bunch==1.0.1',
    'appdirs==1.4.0',               # 1.4.3
    'json-store==2.1',
    'python-dateutil==2.6.0',
    'arrow==0.10.0',
    'funcy==1.7.2',                 # 1.7.3

    # Bus adapters
    #'twisted-mqtt==0.1.4',         # 0.2.1
    'paho-mqtt==1.2',
    'autobahn[twisted]==0.13.0',    # 0.17.2
    'msgpack-python==0.4.7',        # 0.4.8

    # Misc
    'setuptools==22.0.5',           # 34.3.3; setuptools>=18.3.1 is required by set(['crossbar'])
    'distlib==0.2.4',
    'docopt==0.6.2',

    # More dependencies (required for running on Ubuntu 16.04)
    #'pyOpenSSL==16.2.0',
    #'cryptography==1.3.4',
    'pyasn1==0.2.3',
    'pycparser==2.17',
    'pyparsing==2.2.0',

]

extras = {
    'daq': [
        'influxdb==4.0.0',
        'grafana_api_client==0.1.4',
        'requests==2.13.0',
        #'grafana-dashboard-builder==0.1.0a7',      # evaluated, but not suitable
        #'txmongo==16.3.0',
        'pymongo==3.4.0',
    ],
    'daq_geospatial': [
        'Geohash==1.0',
        'geopy==1.11.0',
        'Beaker==1.8.1',
        'tqdm==4.11.2',
    ],
    'daq_binary': [
        'pyclibrary==0.1.3',
        'tabulate==0.7.5',          # 0.7.7
        'sympy==0.7.6.1',           # 1.0
    ],
    'storage_plus': [
        'alchimia==0.4',            # 0.7.0
    ],

    # Data export: Basic formats
    'export': [
        'pyinfluxql==0.0.1',
        'pandas==0.18.1',           # 0.19.2
        'numpy>=1.8.2',             # 1.12.1
        'XlsxWriter==0.9.2',        # 0.9.6
    ],

    'plotting': [
        #'dyplot==0.8.8',

        # sudo port install py27-matplotlib
        'matplotlib>=1.4.2',        # 2.0.0
        #'cairocffi>=0.5.4',
        'bokeh==0.12.4',
        'vincent==0.4.4',
    ],

    # Data export: Scientific data formats like HDF5 and NetCDF and plots from ggplot
    'scientific': [

        # Data
        # ----
        # HDF5
        # "PyTables" requires HDF5 libraries
        # sudo port install hdf5
        'tables>=3.1.1',            # 3.3.0

        # NetCDF (Network Common Data Form)
        'xarray==0.7.2',            # 0.9.1
        # sudo port install netcdf
        'netCDF4==1.2.4',           # 1.2.7
        #'h5netcdf==0.2.2',

        # Algorithms
        # ----------
        # sudo port install py27-scipy
        'scipy>=0.14.0',            # 0.19.0
        'ggplot==0.9.7',            # 0.11.5

        # gfortran
        # aptitude install libatlas-base-dev lapack-dev gfortran or
        # https://gcc.gnu.org/wiki/GFortranBinaries

        # Visualization
        # -------------
        #'seaborn==0.7.1',

    ],

    'firmware': [
        'GitPython==2.0.5',         # 2.1.3
        'plumbum==1.6.1.post0',     # 1.6.3
    ],

}

setup(name='kotori',
      version='0.20.0',
      description='Kotori data acquisition, routing and graphing toolkit',
      long_description='Kotori data acquisition, routing and graphing toolkit',
      license="AGPL 3, EUPL 1.2",
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Pyramid",
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Internet :: MQTT",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: System :: Archiving",
        "Topic :: System :: Networking :: Monitoring",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
      author='Andreas Motl',
      author_email='andreas.motl@elmyra.de',
      url='https://getkotori.org/',
      keywords='data acquisition graphing export plotting daq routine engine' +
               'mqtt wamp http rest sql web html csv json cdf hdf5 png ' +
               'twisted pyramid autobahn influxdb mosquitto grafana mongodb matplotlib ggplot ',
      packages=find_packages(),
      include_package_data=True,
      package_data={
        'kotori': [
          'daq/graphing/resources/*.json',
          'io/export/*.html',
        ],
      },
      zip_safe=False,
      test_suite='kotori.test',
      install_requires=requires,
      extras_require=extras,
      dependency_links=[
          'https://github.com/jjmalina/pyinfluxql/tarball/d92db4ab8c#egg=pyinfluxql-0.0.1',
      ],
      entry_points={
          'console_scripts': [
              'kotori              = kotori:run',
              #'kotori-master      = kotori.master.server:run',
              #'kotori-node        = kotori.node.nodeservice:run',
              #'kotori-wamp-client = kotori.master.client:run_wamp_client',
              'h2m-csv-udp-client  = kotori.vendor.hydro2motion.client:run_udp_client',
              'h2m-csv-udp-fuzzer  = kotori.vendor.hydro2motion.client:run_udp_fuzzer',
              'lst-message         = kotori.vendor.lst.shell:message',
              'luftdaten-to-mqtt   = kotori.vendor.luftdaten.luftdaten_api_to_mqtt:main',
          ],
          'paste.app_factory': [
              'main = kotori.frontend.app:main',
          ],
      },
)
