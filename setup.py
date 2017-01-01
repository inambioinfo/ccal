from setuptools import setup
from setuptools.command.install import install


class InstallCommand(install):
    def run(self):
        install.run(self)
        from distutils import log
        log.set_verbosity(log.DEBUG)

setup(name='ccal',
      description='Computational Cancer Analysis Library',
      packages=['ccal'],
      version='0.0.1',
      author='Huwate (Kwat) Yeerna (Medetgul-Ernar)',
      author_email='kwat.medetgul.ernar@gmail.com',
      license='MIT',
      url='https://github.com/KwatME/ccal',
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.5'],
      keywords=['computational cancer biology bioinformatics machine learning statistics'],
      install_requires=['jupyter', 'notebook>=4.2.0','IPython', 'matplotlib', 'seaborn'],
      cmdclass={'install': InstallCommand},
      package_data={})
