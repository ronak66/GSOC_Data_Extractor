from flask import render_template, url_for, flash, redirect
from gsoc_extractor import app
from gsoc_extractor.forms import Search
from gsoc_extractor.utils import check, query


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
        print (answer)
        # return render_template("search_result.html", answer=answer)
        return redirect(url_for('search_results', answer=answer))
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
        answer = query("co",str(form.search.data))
        print (answer)
        return render_template("search_result.html", answer=answer)
    return render_template("compare_org.html", form=form)

@app.route('/search_results', methods=["GET", "POST"])
def search_results(answer):
    return render_template("search_result.html", answer=answer)
    

