from setuptools import setup, find_packages

setup(
  name = 'python_common_logger',
  packages = find_packages(),
  include_package_data = True,
  install_requires=[
    'starlette',
    'werkzeug'
  ],
  version = '1.0',
  license='None',
  description = 'Common Python Logger for Simpplr packages',
  author = 'Team Delta',
  author_email = 'team.delta@simpplr.com',
  url = 'https://github.com/Simpplr/python-common-logger',
  keywords = ['PYTHON', 'SIMPPLR', 'COMMON', 'LOGGER'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.8',
  ],
)