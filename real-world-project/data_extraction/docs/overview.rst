Project Overivew
=================

1. Project Description
1.1 User Experience
----------------------
- The project will use CLI application to fine-tunned data collected
- Expected command line should look smth like:
.. code-block:: bash

    % python src/acquire.py -o quartet Anscombe_quartet_data.csv

- The `-o quartet` specifies the directory where returning extraction will be stored
- The positional argument `Anscombe_quartet_data.csv` is the input file to be processed
- TODO: Add multiple file handling, e.g. `-o quartet file1.csv file2.csv`
1.2 Source data
----------------------
- The source data is come from this `a link`_.
.. _a link: https://www.kaggle.com/datasets/carlmcbrideellis/data-anscombes-quartet

1.3 Output Data
- The output data will be stored in the json format. 