# ezDRTtools

ezDRTtools is derived from the pyDRTtools program created by the lab of Prof. Francesco Ciucci (University of Bayreuth, formerly at The Hong Kong University of Science and Technology). 
https://www.fc.uni-bayreuth.de/en/team/index.html

NOTE - If you use ezDRTtools, you should cite the relevant scientific references for pyDRTtools listed at https://github.com/ciuccislab/pyDRTtools

**What is the ezDRTtools? Why would I want it?**

The ezDRTtools program is designed to simplify the installation on a Windows PC using a single download and requires no knowledge of Python. 
• The ezDRTtools installer is freely available from www.scribner.com.
• The application is assembled using pyInstaller into a isolated Python environment that contains all the necessary libraries.
•	A Help Menu has been added for easy access to the code versions, readme files, example data files, the exDRTtools AppNote and the pyDRTtools manual. 
•	The name of the loaded data file is listed on the title bar.
•	ezDRTtools is synchronized with modifications to pyDRTtools code in its github.com repository. 
•	ezDRTtools provides a desktop icon to directly launch the application. 

## Distribution and Release Information

The packaged ezDRTtools installer is freely available from www.scribner.com.

All Python code related to the ezDRTtools project is freely available under the MIT license from this site.
The following inctructions are for downloading and running the Python code related to ezDRTtools

**System requirements**

To install and run ezDRTtools, you need: Python >= 3

**Installation details**

To install and run the ezDRTtools Python code, the following procedure is suggested.

create a Python instance
create a Python environment named exDRTtools

**Run the following on anaconda prompt:**
```
conda create --name ezDRT python
conda activate ezDRT
pip install ipython pandas matplotlib scikit-learn spyder cvxopt PyQt5
pip install pyDRTtools
```
**ipython**
```
!launchGUI
```
**How to cite this work?**

Cite the relevant scientific references for pyDRTtools listed at https://github.com/ciuccislab/pyDRTtools

**How to get support?**

Write to derek@scribner.com
