from setuptools import setup, find_packages

setup(
    name="countries",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['Load_Graph'],

    entry_points={
        'Graph.Load': [
            'load_csv = Load_Graph.Load_Graph_Data:LoadGraphData'
        ],
    },
    zip_safe=True
)
