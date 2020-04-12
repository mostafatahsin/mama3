import json

from flask import Flask
from bokeh.plotting import figure, output_notebook, show, save

from bokeh.models.tools import HoverTool
from bokeh.transform import cumsum
from bokeh.models import Text,Label
from flask import render_template
from bokeh.embed import components

import pandas as pd
import math

app = Flask(__name__, template_folder='templates')

def make_plot():

    pi = math.pi

    data = pd.DataFrame()
    list1=['Telemedicine','Education','Transportation','Banking','Hospitals','Domestic','Exports','Freelance']
    list2=[200,200,200,200,200,500,500,1000]
    data['country'] = list1
    data['value'] =list2

    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#fbbb3c','#f0901a','#de5050']
    data['skill_1'] = ["Full-stack developers","IT courses-instructors","Full-stack developers","Hardware and Network system skills","Java, Android and IOS development","Web Application","Web Application",'Software development']
    data['skill_2'] = ['Mobile, Web & Cloud-based App development', 'IT-enabling of administrative services', 'Software Quality Assurance, Testing and Technical support', 'MS Office Suite', 'Linux, Windows and Virtualization (ESXi)', 'Web Design', 'Mobile Application', 'Web design and development' ]
    data['skill_3'] = ['Database administration', 'IT-enabling of accounting services', 'CISCO/Microsoft certification', 'Accessing networks/servers', 'Routing, Switching for Networking', 'Mobile Application','ERP development', 'System architecture' ]
    data['skill_4'] = ['Data analytics', 'Data entry', 'MS office', 'Java and C++', 'V-LAN for Networking', 'Hardware, Server Installation and Maintenance','QA Testing', 'Graphic design']
    data['skill_5'] = ['Problem-solving mindset and adaptability', 'Administrative skills', 'Communication and presentation skills', 'Hardware, Software and Network troubleshooting', 'Basic computer literacy', 'ERP development ','Web Design', 'HTML & JAVA programming language']

    # Add plot
    p = figure(plot_height=500, plot_width=700,
                tools="pan,zoom_in,zoom_out,save,reset", x_range = (-0.5,1))

    p.wedge(x=0.15, y=1, radius=0.35, 
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)

    #text=['FE firms', 'BE firms','freelancers']

    citation1 = Label(x=0.3, y=1.54, x_units='data', y_units='data',
                     text='Front End firms', render_mode='css',
                     border_line_color='black', border_line_alpha=1.0,
                     background_fill_color='#6baed6', background_fill_alpha=1.0)

    citation2 = Label(x=-0.4, y=0.95, x_units='data', y_units='data',
                     text='Back End firms', render_mode='css',
                     border_line_color='black', border_line_alpha=1.0,
                     background_fill_color='#fbbb3c', background_fill_alpha=1.0)

    # citation3 = Label(x=0.2, y=0.65, x_units='data', y_units='data',
    #                  text='Freelance', render_mode='css',
    #                  border_line_color='black', border_line_alpha=1.0,
    #                  background_fill_color='#ef6565', background_fill_alpha=1.0)

    p.add_layout(citation1)
    p.add_layout(citation2)
    # p.add_layout(citation3)


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

    script, div = components(p)
    return script, div

@app.route('/')
def mainPage():

    plots = []
    plots.append(make_plot())   
    return  render_template('dashboard.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
