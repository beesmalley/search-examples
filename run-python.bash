#!/bin/bash

# package needed for visualization
pip install graphviz

# visualize example graph --- it will be found in "example.pdf"
python3 -c "import sys,graph; graph.visualize(open('example.csv','r'), start='s', goal='g', filename='example')"

# run BFS and DFS on example graph
python3 driver.py example.csv
