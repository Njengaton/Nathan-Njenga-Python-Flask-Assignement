This project analyses road accident data using
python and it presents the result through
visualisations and a Flask Web application.It
uses a csv dataset to identify patterns and 
trends in road accidents.
OBJECTIVES
1.Analyse road accident data using python
2.process and explore the csv dataset
3.create data visualisations
develop a Flask Web application
DATASET
The project uses a road accident statistics.csv
created by the author in Jupyter notebook.The
dataset contains
1.Accident ID
2.Time of day
3.Number of Accidents
4.Severity
5.Accident Type
The dataset is processed using pandas and
visualised using matplotlib.
three charts were created:
1.bar chart;compares accident number across
categories.
2.pie chart;shows distribution of accident
severity.
3.scatter plot;shows the relationship between
time of day and frequency.
FLASK WEB APPLICATION
the analysis is presented through a Flask
Web app with:
1.home page-displaying the accident data.
2.statistics page-displaying the charts.
The Flask app serves template files
which are:
 base.html-the parent template
index.html-child template extending to base.html
statistics.html-a child template extending to
base.html
there is the static folder which is responsible 
for the structure and styling of thr Web
it has style.css and the files responsible for
the chart images that are fetched by statistics.html.




