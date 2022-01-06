# MediaTrak
<hr>

Written using Python 3.9.

Python libraries utilized: [blessed](https://pypi.org/project/blessed/) and [pynput](https://pypi.org/project/pynput/)

## Notes
<hr>

Before running the program, run the ***create.py*** file to create the needed database and 
then the ***load.py*** file to load example data into the database.

## Issues
<hr>

* Click logic is implemented with hard-coded coordinate values specific to the monitor used to test the program (1440p monitor)
  * May not work on other monitors if they have a slightly different setup or zoom level when running the program
  * This is due to how we are using the [pynput](https://pypi.org/project/pynput/) library
