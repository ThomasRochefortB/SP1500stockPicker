# SP1500stockPicker
This project incorporates a random forest algorithm which can emit monthly buy signals from the fundamentals of the companies listed on the S&P1500.

### Objective
The objective of this project is to beat the performance of the Standard & Poor 500, the most commonly used benchmark in the finance industry. 

## Getting Started

All the required code is found in the SP1500stockPicker.ipynb file. You can run it using Jupyter Notebook which comes with the Anaconda distribution which you can find at https://www.anaconda.com/distribution/#download-section. The code is running on Python 3.7.

The data used in the program can also be found in the various csv files in the repo:

* ratios_1990_2019.csv
* yield_1962_2019.csv
* SP1500constituents.csv
* ^GSPC.csv

### Requirements

* python==

* matplotlib==

* datetime==

* progressbar==

* multiprocessing==

* scikit-learn==0.21.2

* pandas==0.24.2

* matplotlib==3.1.1

* numpy==1.16.4



### Running

The critical functions of the program (merging database and machine learning) use multiprocessing to accelerate the different task. The entire notebook takes about 2.5h to run on a 24 thread computer with 128gb RAM installed. Performance will therefore vary depending on your hardware. 

In **Jupyter**, hit "Run All Cells" to execute the entire script. You will find intermediate steps after the data cleaning and feature selection to skip unecessary work for the CPU when changing components of the code.


## Built With

* [sklearn](https://scikit-learn.org/stable/) - Machine Learning package for Python
* [feature_selector](https://github.com/WillKoehrsen/feature-selector) - Feature Selection


## Contributing

Feel free to reach out to me by email at thomas.rochefort-beaudoin@polymtl.ca for suggestions or questions about the repo.

## Authors

* **Thomas Rochefort-Beaudoin** - *Initial work* 

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Robert Normand**, *Teacher at Polytechnique Montréal and researcher at CIRANO Montréal*, for his insights and help.


