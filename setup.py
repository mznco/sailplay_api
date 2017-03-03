from setuptools import setup

setup(name='sailplay_api',
      version='0.3',
      description='A Python wrapper for the SailPlay API',
      url='https://github.com/mznco/sailplay_api',
      author='mznco',
      author_email='admin@mznco.net',
      license='GPL-3.0',
      packages=['sailplay_api'],
	  install_requires=[
		'urllib',
		'urllib2',
		'logging',
		'json',
	  ],
      zip_safe=False)