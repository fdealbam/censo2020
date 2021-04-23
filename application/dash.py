
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



#################################### Card

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray"}),
            html.H2("de población", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black", "font-weight": 'bold'}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            html.P(
                "Sin derechohabiencia "
              "  7,804,407",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   #'FontColor': 120
                      }
            ),

            
            
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),]),),
            html.Br(),
            
            html.P("42%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',
                        "color": "dark",}),
            
            html.Br(),
            html.P(
                "Primaria incompleta "
              "  3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                          ]),),
            html.P("30%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),
            

            html.Br(),
             html.P(
                "Con discapacidad "
              "  782,953",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-wheelchair", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),]),),
             html.P("4%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),

        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0" },
)





##########################################################################
#Seccion 2. Variables de vivienda
##########################################################################

#################################### Card2 HAY QUE AJUSTARLA CON....


card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población total", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H3("20,116,842", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.Br(),
     #     button_group = dbc.ButtonGroup(
    #[dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")]
#)
          
            dbc.ButtonGroup(
                html.Span(["", html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),]),),
            
        ]
    ),
    
    style={"width": "25.5rem", 
          "border": "0",
          "background-color": "orange"
          },
)



card2a = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población de 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H5("64%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "white",  
                         "font-size": "38px",
                         })]), style={"width": "25.5rem", 
                                      "border": "0",
                                      "background-color": "#0097A7",
           
          },
)


card2aa = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población de 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#B2DFDB"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#B2DFDB"}),
            html.H5("64%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "white",  
                         "font-size": "38px",
                         })]), style={"width": "25.5rem", 
                                      "border": "0",
                                      "background-color": "#B2DFDB",
           
          },
)




card2b = dbc.Card(
    dbc.CardBody(
        [
            html.P(
                "Primaria incompleta "
              "3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   #'FontColor': 120
                      }
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

        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0",
          "fill" : "orange"},
)





##########################################################################
#Seccion 3. Variables de vivienda
##########################################################################



## Tabla de variables
row1 = html.Tr([dbc.Alert("Con sanitario y con agua"), 
                html.Td("19,172,575"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("94%", color="light",
                        style={#'textAlign': 'up', 
                         #"height": "10px",
                         #"color": "light",  
                         "font-size": "30px",
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




#################################### Card3
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray"}),
            html.H2("de vivienda", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black", "font-weight": 'bold'}),
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
#card3 = dbc.Card(
#    dbc.CardBody(
#        [
#            html.P([dbc.Button([html.H1(className="fas fa-home"),
#            "  Variables de Vivienda"], 
#                    style={'textAlign': 'left',"color":"#eada79",
#                   #'FontColor': 220,
#                   "font-size": "40px",
#                          })]),
#            html.Br(),
#            
#     dbc.Table( table_body, bordered=False)
#                    ]
#        ), style={"width": "50rem", 
#          "border": "0",
#          "fill" : "orange"},
#        )
#           
           



##########################################################################
#Seccion 4 Variables de INTERNET
##########################################################################


#################################### Card2p3
card2p3 = dbc.Card(
    dbc.CardBody(
        [
         dbc.Button((["", html.H1(className="fas fa-male", style={"color": "#CFD8DC"}),
                 html.H6(" Con televisor "),
                 html.H1("97%"),
                 #html.H6("1,625,420")                      
        ])),

         dbc.Button((["", html.H1(className="fas fa-male", style={"color": "#CFD8DC"}),
                 html.H6(" Con computadora "),
                 html.H1("97%"),
                 #html.H6("1,625,420")                      
        ])),
            
         dbc.Button((["", html.H1(className="fas fa-male", style={"color": "#CFD8DC"}),
                 html.H6(" Con internet "),
                 html.H1("97%"),
                 #html.H6("1,625,420")                      
        ])),

         dbc.Button((["", html.H1(className="fas fa-male", style={"color": "#CFD8DC"}),
                 html.H6(" Con celular "),
                 html.H1("97%"),
                 #html.H6("1,625,420")                      
        ])),
            
     
        ]), style={#'textAlign': 'center','color': 'black',
                  #'FontColor': 120, 
                   "border": "0",
              "fill" : "transparent"})


        


##########################################################################
#Seccion 5 Variables de MIGRACION
##########################################################################

row1 = html.Tr([
                dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población nacida en otra entidad"], className="mb-0"), 
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
                           "    Población femenina nacida en otra entidad"], className="mb-0"), 
                html.Td("5,311,593"),
                html.Td("98%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
row3 = html.Tr([dbc.Alert([html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población masculina nacida en otra entidad"], className="mb-0"), 
                html.Td("5,162,569"),  
                html.Td("99%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

table_body = [html.Tbody([row1, row2, row3])]







#################################### Card4
card4 = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-arrows-alt"),
            #"    Variables de Migración"], 
            #        style={'textAlign': 'left',"color": "gray",
            #       'FontColor': 120}),
            "  Variables de Migración"], 
                    style={'textAlign': 'left',"color":"#D500F9",
                   #'FontColor': 220,
                   "font-size": "40px",
                           
                          }),
            
            dbc.Table(table_body, bordered=False)
         ])]),

            style={"width": "50rem", 
                  "border": "0",
                  "fill" : "orange"})

         
  


    
    
##########################################################################
#Seccion 6 Variables de EDUCACION
##########################################################################

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



#################################### card_v_edu
card_v_edu = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-book"),
            "  Variables de Educación"], 
                    style={'textAlign': 'left',"color":"#9dbf88",
                   #'FontColor': 220,
                   "font-size": "40px",
                           
                          })]),

            html.Br(),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           
    

    
    
##########################################################################
#Seccion 7. Variables de DERECHOHABIENCIA
##########################################################################

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


#################################### card_v_derechohab
card_v_derechohab = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-medkit"),
       
            "  Variables de Derechohabiencia"], 
                    style={'textAlign': 'left',"color":"#51c8e1",
                   
                   "font-size": "40px",
                           
                          })]),

            html.Br(),
          
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           

    
    
##########################################################################
#Seccion 8. Variables de HOGARES CENSALES
##########################################################################

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




#################################### card_v_hog_cens
card_v_hog_cens = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-child"),
            "  Variables de Hogares censales"], 
                    style={'textAlign': 'left',"color":"#f0bdeb",
                   #'FontColor': 220,
                   "font-size": "40px",
                          })]),
            html.Br(),
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           

    
    
    
    
##########################################################################
#Seccion 9. Variables de DISCAPACIDAD
##########################################################################

row1 = html.Tr([
                dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Religión católica"], color="warning"), 
                html.Td("16,123,123"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("85%", 
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold', })])

row2 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Protestantes, Evangélicas y Otras"], color="warning"), 
                html.Td("2,088,735"),
                html.Td("7%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])
table_body = [html.Tbody([row1, row2,])]



#################################### card_v_discapacidad
card_v_discapacidad = dbc.Card(
    dbc.CardBody(
        [
 
            html.P([dbc.Button([html.H1(className="fa fa-wheelchai"),
            #"    Variables de Migración"], 
            #        style={'textAlign': 'left',"color": "gray",
            #       'FontColor': 120}),
            "  Variables de Discapacidad"], 
                    style={'textAlign': 'left',"color":"#a58ca3",
                   #'FontColor': 220,
                   "font-size": "40px",
                           
                          })]),

            html.Br(),
            
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)


##########################################################################
#Seccion 10. Variables de ECONOMIA
##########################################################################

row1 = html.Tr([
                dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población ocupada"], color="warning"), 
                html.Td("16,123,123"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("85%", 
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold', })])

row2 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población masculina ocupada"], color="warning"), 
                html.Td("2,088,735"),
                html.Td("31%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

row3 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Población femenina ocupada"], color="warning"), 
                html.Td("3,088,735"),
                html.Td("40%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

row4 = html.Tr([dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    12 años y más no económicamente activa estudiante"], color="warning"), 
                html.Td("1,088,735"),
                html.Td("32%",
                        style={'textAlign': 'center',
                         "color": "black",  
                         "font-size": "30px",
                         "font-weight": 'bold',})])

table_body = [html.Tbody([row1, row2, row3, row4])]



#################################### card_v_economia
card_v_economia = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-transgender-alt"),
            "  Variables de Economía"], 
                    style={'textAlign': 'left',"color":"#51c8e1",
                   #'FontColor': 220,
                   "font-size": "40px",
                           
                          })]),

            html.Br(),
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
           

    
##########################################################################
#Seccion 11. Variables de RELIGION
##########################################################################

row1 = html.Tr([
                dbc.Alert([#html.P(className="fas fa-male", style={"color": "#D500F9"}),
                           "    Religión católica"], color="warning"), 
                html.Td("16,123,123"),#,style={'textAlign': 'bottom'}),
                dbc.Alert("85%", 
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




#################################### card_v_religion
card_v_religion = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fa fa-transgender-alt"),
            "  Variables de Religión"], 
                    style={'textAlign': 'left',"color":"#51c8e1",
                   "font-size": "40px",
                           
                          })]),

            html.Br(),
            dbc.Table( table_body, bordered=False)
                    ]
    ),
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)
       
     
##########################################################################
# A P P 
##########################################################################



# identificadores

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX, FONT_AWESOME], server=server)

body = html.Div([

    html.Br(),
    html.Br(),
    

    
    ################## SECCION 1 (pag1)_VARIABLES DE POBLACION
    dbc.Row([
        dbc.Col(dbc.Card(card), sm={  "offset": 1, }),
        dbc.Col(dbc.Card(card2),                      #población total
               style={#'margin-top': '-540px',       #arriba
                      'margin-left': '-100px', 
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ], className="blockquote"),
    
    dbc.Row([
        dbc.Col(dbc.Card(card2a),
                style={'margin-top': '-628px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),

     dbc.Row([
       dbc.Col(dbc.Card(card2aa),
               style={'margin-top': '-473px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '50%',
                     })
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(card2a),
                style={'margin-top': '-318px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),

     dbc.Row([
       dbc.Col(dbc.Card(card2aa),
               style={'margin-top': '-222px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '50%',
                     })
    ]),
    
    
    
    ################## SECCION 2 (pag1)_VARIABLES DE VIVIENDA
    dbc.Row([
        
        dbc.Col(dbc.Card(card3, color="white", inverse=True,  ),
         sm={  "offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),


    
    ################## SECCION 4 (pag1)_VARIABLES DE INTERNET

    dbc.Row([
        dbc.Col(dbc.Card(card2p3, color="green"#, outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
    
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    html.Br(),
    

    
    ################## SECCION 5 (pag1)__VARIABLES DE MIGRACION
    dbc.Row([
        dbc.Col(dbc.Card(card4),
         sm={"size": 9,  "offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    
    
    #############################>>>>>>> II <<<<<<<<<#############################
    
    ################## SECCION 1 (pag 2)__VARIABLES DE DISCAPACIDAD
    dbc.Row([
        dbc.Col(dbc.Card(card_v_discapacidad, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={"size": 9,  "offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    
    ################## SECCION 2 (pag 2)__VARIABLES DE ECONOMIA
    dbc.Row(
     [
        dbc.Col(dbc.Card(card_v_economia, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={"size": 9,  "offset": 1, }),
         
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    
    ################## SECCION 3 (pag 2)__VARIABLES DE RELIGION
    dbc.Row([
        dbc.Col(dbc.Card(card_v_religion, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={"size": 9,  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    #############################>>>>>>> III <<<<<<<<<#############################
    
    ################## SECCION 1 (3a pag)__VARIABLES DE EDUCACION      
    dbc.Row([
        dbc.Col(dbc.Card(card_v_edu, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    ################## SECCION 2 (3a pag)__VARIABLES DE DERECHOHABIENCIA
    dbc.Row([
        dbc.Col(dbc.Card(card_v_derechohab, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    ################## SECCION 3 (3a pag)__VARIABLES DE HOGARES CENSALES 
    dbc.Row([
        dbc.Col(dbc.Card(card_v_hog_cens, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
         ])
    
app.layout = html.Div([body])
#app.layout = html.Div(children=[html.Img(className='icon')])

if __name__ == '__main__':
    app.run_server(use_reloader = False)
