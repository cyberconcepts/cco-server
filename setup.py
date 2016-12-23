from setuptools import setup, find_packages


setup(name='main',
      version='1.0',
      description='main bluebream application',
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='Helmut Merz',
      author_email='helmutm@cy55.de',
      url='http://www.cyberconcepts.de',
      license='MIT',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zope.annotation',
                        'z3c.testsetup',
                        'zope.app.appsetup',
                        'zope.app.authentication',
                        'zope.app.catalog',
                        'zope.app.component',
                        'zope.app.container',
                        'zope.app.content',
                        'zope.app.debug',
                        'zope.app.dependable',
                        'zope.app.error',
                        'zope.app.folder',
                        'zope.app.intid',
                        'zope.app.pagetemplate',
                        'zope.app.schema',
                        'zope.app.publisher',
                        'zope.app.locales',
                        'zope.app.principalannotation',
                        'zope.app.basicskin',
                        'zope.app.rotterdam',
                        'zope.app.session',
                        'zope.app.testing',
                        'zope.app.wsgi',
                        'zope.app.zcmlfiles',
                        #'zope.app.zopeappgenerations',
                        'zope.authentication',
                        'zope.browserresource',
                        'zope.component',
                        'zope.contentprovider',
                        'zope.formlib',
                        'zope.i18n',
                        'zope.intid',
                        'zope.keyreference',
                        'zope.login',
                        'zope.publisher',
                        'zope.securitypolicy',
                        'zope.sendmail',
                        'zope.testbrowser',
                        'zope.thread',
                        ],
      entry_points = """
      [paste.app_factory]
      main = main.startup:application_factory

      [paste.global_paster_command]
      shell = main.debug:Shell
      """,
      )