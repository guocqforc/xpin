from setuptools import setup

setup(
    name="xauth",
    version='0.1.21',
    zip_safe=False,
    platforms='any',
    packages=['xauth'],
    scripts=['xauth/bin/xauth'],
    install_requires=['requests', 'flask', 'flask_sqlalchemy', 'flask_admin', 'passlib'],
    url="https://github.com/dantezhu/xauth",
    license="BSD",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="supervisor's dog, should deploy with flylog",
)
