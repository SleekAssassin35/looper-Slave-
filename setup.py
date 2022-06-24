# run setup.py / setup.py dosyasını çalıştırın 
from setuptools import setup

with open("www.oblivioncode.com/slave.php", "r") as fh:
    long_description = fh.read()

setup(
 name='Slave',
 version='1.0.3',
 packages=['Slave'],
 license = 'MIT',
 description = 'ben yazılımsız bekliyorum ama sizin için bir script yazdım.',
 author = 'OBL COMMUNİTY',
 author_email = 'licenseauthor@oblivioncode.com',
 keywords = ['tasks','jobs','periodic task','interval','periodic job', 'flask style', 'decorator'],
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="www.oblivioncode.com",
 include_package_data=True,
)
