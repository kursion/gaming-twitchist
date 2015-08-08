from setuptools import setup

setup(name='twitchist',
            version='0.2.4',
            description='A little tool that parse and show the streams from twitch.tv. Open it with you favorite browser or livestreamer.',
            url='https://github.com/kursion/twitchist',
            author='Yves Lange',
            author_email='kursion@gmail.com',
            license='MIT',
            packages=['twitchist'],
            install_requires=[
                'colorama',
            ],
            zip_safe=False,
            entry_points={'console_scripts': [
                'twitchist = twitchist.__init__:main'
            ]}
)
