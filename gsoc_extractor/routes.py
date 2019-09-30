from flask import render_template, url_for, flash, redirect
from gsoc_extractor import app, db
from gsoc_extractor.forms import Search
from gsoc_extractor.utils import check, query
from gsoc_extractor.model import Data
from datetime import datetime

now = datetime.now()

@app.route('/', methods=['GET','POST'])
@app.route('/search_tech', methods=['GET','POST'])
def search_tech():
    form = Search()
    if form.validate_on_submit():
        year = str(form.search_type.data)
        year_list = ['2018','2017','2016']
        if year not in year_list:
            flash("Year {} not available, please use 2016 or 2017 or 2018".format(year), 'danger')
            return redirect(url_for('search_tech'))
        answer = query("gt "+str(form.search_type.data),str(form.search.data))
        # print answer
        d = str(form.search_type.data) + ";" + str(form.search.data) + ";" + str(now.strftime("%d/%m/%Y %H:%M:%S"))
        file1 = open("Data/allquery.txt","a+")
        file1.write(d +"\n")
        file1.close()
        return render_template("search_result.html", answer=answer)
    return render_template("search_tech.html", form=form)
    

@app.route('/compare_org', methods=['GET','POST'])
def compare_org():
    form = Search()
    if form.validate_on_submit():
        year_list = ['2018','2017','2016']
        query_years = str(form.search.data).split(',')
        for year in query_years:
            if year not in year_list:
                flash("Incorrect year or query format, please use 2018 or 2017 or 2016 in format <year1>,<year2>,...",'danger')
                return redirect(url_for('compare_org')) 
        answer = query("co",form.search.data)
        # print answer
        d = str(form.search.data) + ";" + str(now.strftime("%d/%m/%Y %H:%M:%S"))
        file1 = open("Data/allquery.txt","a+")
        file1.write(d +"\n")
        file1.close()
        return render_template("search_result.html", answer=answer)
    return render_template("compare_org.html", form=form)

@app.route('/allqueries')
def queries():
    querys=[]
    with open("Data/allquery.txt") as d:
        i=0
        for l in d:
            l = l.split(";")
            print (l)
            if(len(l)==2):
                d = {
                    "id": i,
                    "year": l[0],
                    "type":0,
                    "time": l[1]
                }
                querys.append(d)
            else:
                d = {
                    "id": i,
                    "year": l[0],
                    "technology": l[1],
                    "type":1,
                    "time":l[2]
                }
                querys.append(d)
            i+=1
    return render_template('all_queries.html', data=querys)