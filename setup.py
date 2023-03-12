from setuptools import setup


setup(name='clean_folder',
      version='0.1.0',
      description='Very useful code',
      url='https://github.com/remmover/HW_07_goit',
      author='remmover',
      author_email='igorm.200323@gmail.com',
      license='MIT',
      entry_points = {"console_scripts":["clean-folder = clean_folder.clean:main"]})