from setuptools import setup, find_packages

setup(
    name="wResourceAuth",
    version='0.1',
    description="와이솔 Oauth2 Python OpenId 인증 모듈",
    author="backho",
    author_email="XXXX@wisol.co.kr",
    packages=find_packages("ResourceAuth"),
    requires=[
        "django",
        "djangorestframework",
        'PyJWT==2.6.0',
        'cryptography==38.0.3'
    ],
)
