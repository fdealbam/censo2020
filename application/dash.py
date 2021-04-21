import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

pobsindh = 7804407
##########################################################################
#Seccion 1. Variables de POBLACION
##########################################################################



################################################################# Card

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray"}),
            html.H3("de población", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black", "font-weight": 'bold'}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            html.P(
                "Sin derechohabiencia "
              "7,804,407",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120
                      }
            ),

            
            
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),
                               html.H1(className="fas fa-male", style={"color": "#00ACC1"}),]),),
            html.Br(),
            
            html.P("42%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',
                        "color": "#00ACC1",}),
            
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),]),),
            html.Br(),
            html.P(
                "Primaria incompleta "
              "3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B388FF"}),
                          ]),),
            html.P("30%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
            
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#039BE5"}),]),),
            html.Br(),
             html.P(
                "Con discapacidad "
              "782,953",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-wheelchair", style={"color": "#DD2C00"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#DD2C00"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#DD2C00"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#DD2C00"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#DD2C00"}),]),),
             html.P("4%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),]),)
        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0" },
)
################################################################# Card2
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.H3("de población", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            html.P(
                "Sin derechohabiencia "
              "7,804,407",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120
                      }
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),
                               html.H1(className="fas fa-male"),]),),
            html.Br(),
            html.P("42%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "color": "black",
                         "font-weight": 'bold',}),
            
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),]),),
            html.Br(),
            html.P(
                "Primaria incompleta "
              "3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#B9F6CA"}),
                          ]),),
            html.P("30%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
            
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),
#                               html.H6(className="fas fa-window-minimize"),]),),
            html.Br(),
             html.P(
                "Con discapacidad "
              "782,953",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),
                               html.H1(className="fas fa-male",style={"color": "#F8BBD0"}),]),),
            
             html.P("4%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
#            dbc.Button(
#                html.Span(["", html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
#                               html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),]),)
        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0",
          "fill" : "orange"},
)
##########################################################################
#Seccion 2. Variables de vivienda
##########################################################################



row1 = html.Tr([dbc.Alert("Con sanitario y con agua"), 
                html.Td("19,172,575"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("94%", color="light",
                        style={#'textAlign': 'up', 
                         #"height": "10px",
                         #"color": "light",  
                         "font-size": "40px",
                         #"font-weight": 'bold',
                        })])

row2 = html.Tr([dbc.Alert("Viviendas habitadas"), 
                html.Td("5,311,593"),
                html.Td("98%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row3 = html.Tr([dbc.Alert("Con luz eléctrica"),
                html.Td("5,162,569"),  
                html.Td("99%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

row4 = html.Tr([dbc.Alert("Con agua entubada"), 
                html.Td("4,973,950"),  
                html.Td("92%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row5 = html.Tr([dbc.Alert("Con drenaje"), 
                html.Td("5,115,669"),  
                html.Td("96%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row5 = html.Tr([dbc.Alert("Con sanitario"), html.Td("5,132,288"),  
                html.Td("97%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
table_body = [html.Tbody([row1, row2, row3, row4,row5])]




################################################################ Card 3
card3 = dbc.Card(
    dbc.CardBody(
        [
            dbc.Button(html.Span(["",html.H1(className="fas fa-home"),]),),
            html.H4("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.H5("de vivienda", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           
           
######################################################### Migración

row1 = html.Tr([
                dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población nacida en otra entidad"], color="warning"), 
                html.Td("19,172,575"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("94%", 
                        style={#'textAlign': 'up', 
                         #"height": "10px",
                         "color":"#D500F9",
                         "font-size": "40px",
                         "font-weight": "bolder",
                         #"font-color": "#D500F9"   ,
                        })])

row2 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población femenina nacida en otra entidad"], color="warning"), 
                html.Td("5,311,593"),
                html.Td("98%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row3 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población masculina nacida en otra entidad"], color="warning"), 
                html.Td("5,162,569"),  
                html.Td("99%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

table_body = [html.Tbody([row1, row2, row3])]







card4 = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Alert([html.P(className="fa fa-arrows-alt"),
            "Variables"], 
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.P("de Migración", 
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
            
            dbc.Table(table_body, bordered=False)
         ])]),

            style={"width": "50rem", 
                  "border": "0",
                  "fill" : "orange"})
######################################################### Educación

row1 = html.Tr([
                dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    De 15 años y más alfabeta"], color="warning"), 
                html.Td("14,123,123"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("96%", 
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold', })])

row2 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    De 15 años y más con educación básica completa"], color="warning"), 
                html.Td("3,123,123"),
                html.Td("27%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row3 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    De 15 años y más analfabeta"], color="warning"), 
                html.Td("123,123"),
                html.Td("4%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
table_body = [html.Tbody([row1, row2, row3])]



card_v_edu = dbc.Card(
    dbc.CardBody(
        [
            dbc.Button(html.Span(["",html.H1(className="fa fa-book"),]),),
            html.H4("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.H5("de Educación", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           
######################################################### Derechohabiencia

row1 = html.Tr([
                dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población derchohabiente del IMSS"], color="warning"), 
                html.Td("6,851,070"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("47%", 
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold', })])

row2 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población derechohabiente del Seguro Popular o Seguro Médico para una Nueva Generación"], color="warning"), 
                html.Td("2,088,735"),
                html.Td("31%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
table_body = [html.Tbody([row1, row2, ])]



card_v_derechohab = dbc.Card(
    dbc.CardBody(
        [
            dbc.Button(html.Span(["",html.H1(className="fa fa-medkit"),]),),
            html.H4("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.H5("de Derechohabiencia", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           
  ######################################################### Hogares Censales

row1 = html.Tr([
                dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población en hogares con jefa(e) de 30 a 59 años"], color="warning"), 
                html.Td("13,833,033"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("72%", 
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold', })])

row2 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población en hogares con jefa(e) de 60 años y más"], color="warning"), 
                html.Td("3,983,622"),
                html.Td("18%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row3 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población en hogares con jefatura femenina"], color="warning"), 
                html.Td("1,412,824"),  
                html.Td("23%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

row4 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población en hogares con jefa e hijos menores de 18 años"], color="warning"), 
                html.Td("262,459"),  
                html.Td("21%%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
table_body = [html.Tbody([row1, row2, row3, row4])]







card_v_hog_cens = dbc.Card(
    dbc.CardBody(
        [
            dbc.Button(html.Span(["",html.H1(className="fa fa-child"),]),),
            html.H4("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray",
                   'FontColor': 120}),
            html.H5("Hogares censales", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           

# identificadores

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX, FONT_AWESOME], server=server)

body = html.Div([

    html.Br(),
    html.Br(),
    dbc.Row(
        [
        dbc.Col(html.H1(" ",
             style={"size":  "auto",  "offset": 3, })),
        
        ], justify="center"),

    
    # SECCION 1 VARIABLES DE POBLACION ###################################
    dbc.Row(
     [
        dbc.Col(dbc.Card(card, color="gray", inverse=True,  ),
         sm={  "offset": 1, }),
        dbc.Col(dbc.Card(card2, color="gray", inverse=True,  ),
         sm={  "offset": 1, }),
      
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    dbc.Row(
     [
        dbc.Col(dbc.Card(card3, color="white", inverse=True,  ),
         sm={  "offset": 1, }),
       
      
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    # SECCION 4 CON INTERNET ###########    

    dbc.Row(
     [
        dbc.Col(dbc.Card(card2p3, color="green"),
         sm={  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    html.Br(),
    html.Br(),
    html.Br(),

    
    # SECCION 4  ###########    
    dbc.Row(
     [
        dbc.Col(dbc.Card(card4, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    # SECCION 1 (3a pag)  ###########    
    dbc.Row(
     [
        dbc.Col(dbc.Card(card_v_edu, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    # SECCION 2 (3a pag)  ###########    
    dbc.Row(
     [
        dbc.Col(dbc.Card(card_v_derechohab, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    # SECCION 3 (3a pag)  ###########    
    dbc.Row(
     [
        dbc.Col(dbc.Card(card_v_hog_cens, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    

    
         ])
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
