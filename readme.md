This code generates two reports based on sales data: one for teams and one for products. The code requires 5 input files to run:

TeamMap file
ProductMaster file
Sales file
TeamReport file (output)
ProductReport file (output)
To run this code, follow the steps below:

Install the required libraries: csv and argparse.
Save the code to a Python file (e.g. report_generator.py).
Open the command prompt or terminal and navigate to the directory where the Python file is saved.
Run the code using the following command:
<pre>
python report_generator.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report TeamReport.csv --product-report ProductReport.csv
</pre>

Note: Replace the names of the input files (TeamMap.csv, ProductMaster.csv, and Sales.csv) with the actual names of your files. Replace the names of the output files (TeamReport.csv and ProductReport.csv) with the desired names of your reports.