from setuptools import setup

package_name = 'min_video_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pcraichl',
    maintainer_email='assispeta7@seznam.cz',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = min_video_publisher.video_publisher:main',
            'image_publisher = min_video_publisher.image_publisher:main',
        ],
    },
)
