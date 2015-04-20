from setuptools import setup

setup(name='Twichist',
            version='0.2.4',
            description='A little tool that parse and show the streams from twitch.tv. Open it with you favorite browser or livestreamer.',
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
