from setuptools import setup, find_packages

package_name = 'robotics-exam-drive'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kimdohee',
    maintainer_email='milkyice4567@naver.com',
    description='TODO: Self-driving robot control',
    license='TODO: Self-driving robot control',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
