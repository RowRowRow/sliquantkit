from setuptools import setup,find_packages

setup(name = 'sliquantkit',
      version = '0.1',
      description = "Sida.Li's personal quant kit",
      author='Sida Li',
      author_email='szlsd123@163.com',
      license='MIT',
      packages=find_packages(include = ['sliquantkit','sliquantkit.*']),
      zip_safe=False)
    