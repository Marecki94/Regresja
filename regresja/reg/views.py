from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
import pandas as pd
import statsmodels.formula.api as sm
import statsmodels.api as smg
import matplotlib.pyplot as plt, mpld3
# Create your views here.
def regresja(request):
   aircsv = pd.read_csv('E:/Django/Air.csv')
   regetest=sm.ols(formula="czestotliwosc ~ poziom_halasu", data=aircsv).fit()
   figure = smg.graphics.abline_plot(model_results=regetest)
   fig=mpld3.fig_to_html(figure, None, None, True,"simple")
   temp = loader.get_template('regresja.html')
   summary=regetest.summary()
   context = {}
   context['fig']=fig
   context['sum']=summary
   html = temp.render(context)
   return HttpResponse(html)
   

   
   