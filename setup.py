from setuptools import setup

setup(name='Twilist',
            version='0.1',
            description='A little to that parse and show the streams on twitch. Open it with you favorite browser.',
            url='https://github.com/kursion/twilist',
            author='Yves Lange',
            author_email='kursion@gmail.com',
            license='MIT',
            packages=['twilist'],
            install_requires=[
                'colorama',
            ],
            zip_safe=False,
            entry_points={'console_scripts': [
                'twilist = twilist.__init__:main'
            ]}
)
