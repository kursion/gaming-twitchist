from setuptools import setup

setup(name='Twichist',
            version='0.2.2',
            description='A little to that parse and show the streams on twitch. Open it with you favorite browser.',
            url='https://github.com/kursion/twichist',
            author='Yves Lange',
            author_email='kursion@gmail.com',
            license='MIT',
            packages=['twichist'],
            install_requires=[
                'colorama',
            ],
            zip_safe=False,
            entry_points={'console_scripts': [
                'twichist = twichist.__init__:main'
            ]}
)
