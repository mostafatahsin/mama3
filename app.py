import json

from flask import Flask
from bokeh.plotting import figure, output_notebook, show, save

from bokeh.models.tools import HoverTool
from bokeh.transform import cumsum
from bokeh.models import Text
from flask import render_template
from bokeh.embed import components

import pandas as pd
import math

app = Flask(__name__, template_folder='templates')
# 5000
def make_plot():

    pi = math.pi

    # x=[1,2,3,4]
    # y=[4,5,7,5]

    # x = {
    #     'Telemedicine': 200,
    #     'Education':    200,
    #     'Transportation':   200,
    #     'Banking':  200,
    #     'Hospitals':    200,
    #     'Domestic': 500,
    #     'Exports':  500,
    #     'Freelance':    1000
    # }


    # data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})

    data = pd.DataFrame()
    list1=['Telemedicine','Education','Transportation','Banking','Hospitals','Domestic','Exports','Freelance']
    list2=[200,200,200,200,200,500,500,1000]
    data['country'] = list1
    data['value'] =list2


    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#fbbb3c','#f0901a','#de5050']
    data['skill_1'] = ["Full-stack developers","IT courses-instructors","Full-stack developers","Hardware and Network system skills","Java, Android and IOS development","Web Application","Web Application",'Software development']
    data['skill_2'] = ['Mobile, web & cloud-based application development', 'IT-enabling of administrative services', 'Software quality assurance, Testing and Technical support', 'MS Office Suite', 'Linux, Windows and Virtualization (in particular, ESXi)40', 'Web Design', 'Mobile Application', 'Web design and development' ]
    data['skill_3'] = ['Database administration', 'IT-enabling of accounting services', 'network-related activities-CISCO/Microsoft certified applicants', 'Accessing networks/servers', 'Routing, Switching for Networking', 'Mobile Application','ERP development', 'System architecture' ]
    data['skill_4'] = ['Data analytics', 'Data entry', 'MS office', 'Java and C++', 'V-LAN for Networking', 'Hardware, Server Installation and Maintenance','QA Testing', 'Graphic design']
    data['skill_5'] = ['Problem-solving mindset and adaptability', 'Administrative skills', 'Communication and presentation skills', 'Hardware, software and network troubleshooting', 'Basic computer literacy for staff', 'ERP development ','Web Design', 'Java & Html related product/services ']
    # data = data.sort_values('value')

    
    # Add plot
    p = figure(plot_height=500, plot_width=500, title="Top Five IT Industry Skills",
               tools="pan, zoom_in,zoom_out,save,reset", x_range = (-0.5,1))

    p.wedge(x=0, y=1, radius=0.35, 
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)

    
    p.axis.axis_label=None
    p.axis.visible=None
    p.grid.grid_line_color = None

    

    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
      <div>
        <h3>Top Five Skills</h3>
        <div>1. @skill_1</div>
        <div>2. @skill_2</div>
        <div>3. @skill_3</div>
        <div>4. @skill_4</div>
        <div>5. @skill_5</div>
      </div>
    """

    p.add_tools(hover)

    #show(p)
    #output_notebook()

    script, div = components(p)
    return script, div

@app.route('/')
def mainPage():

    plots = []
    plots.append(make_plot())   
    return  render_template('dashboard.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)