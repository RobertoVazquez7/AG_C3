# rutas disponibles para cada municipio
from datetime import timedelta

# seccion A
palenque_salida = timedelta(days=0, hours=1, minutes=5, seconds=11)
altamirano_salida = timedelta(days=0, hours=1, minutes=30, seconds=10)
reforma_salida = timedelta(days=0, hours=0, minutes=30, seconds=11)
simojovel_salida = timedelta(days=0, hours=0, minutes=49, seconds=11)
# seccion B
bochil_salida = timedelta(days=0, hours=2, minutes=4, seconds=11)
huixtla_salida = timedelta(days=0, hours=1, minutes=15, seconds=11)
amatenango_salida = timedelta(days=0, hours=1, minutes=10, seconds=11)
juarez_salida = timedelta(days=0, hours=0, minutes=35, seconds=11)
arriaga_salida = timedelta(days=0, hours=1, minutes=5, seconds=11)
# seccion C
ocosingo_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)
cintalapa_salida = timedelta(days=0, hours=12, minutes=3, seconds=41)
parral_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)
ixtapa_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)
montecristo_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)
# seccion D
acala_salida = timedelta(days=0, hours=12, minutes=3, seconds=10)
oxchuc_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)
teopisca_salida = timedelta(days=0, hours=12, minutes=3, seconds=13)
tapachula_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)

suchiapa_salida = timedelta(days=0, hours=12, minutes=3, seconds=20)
#villaflores_salida = timedelta(days=0, hours=12, minutes=3, seconds=11)

# rutas = {
#     'Acala': {'ruta':['Altamirano', 'Oxchuc']},
#     'Altamirano':{'ruta':['Acala','Ocosingo']},
#     'Amatenango':{'ruta':['Ocosingo','Bochil']},
#     'Bochil':{'ruta':['Huixtla','Amatenango','Suchiapa']},
#     'Cintalapa':{'ruta':['Ixtapa','Oxchuc','Teopisca']},
#     'Huixtla':{'ruta':['Bochil','Reforma','Palenque']},
#     'Ixtapa':{'ruta':['Tapachula','Cintalapa']},
#     'Oxchuc':{'ruta':['Acala','Cintalapa','Teopisca']},
#     'Suchiapa':{'ruta':['Bochil','Reforma','Villaflores','Parral','Teopisca']},
#     'Reforma':{'ruta':['Huixtla','Palenque','Suchiapa']},
#     'Montecristo':{'ruta':['Tapachula','Arriaga']},
#     'Parral':{'ruta':['Tapachula','Suchiapa']},
#     'Teopisca':{'ruta':['Suchiapa','Tapachula','Ocosingo','Oxchuc','Cintalapa']},
#     'Tapachula':{'ruta':['Parral','Teopisca','Montecristo','Ixtapa']},
#     'Arriaga':{'ruta':['Juarez','Villaflores','Montecristo']},
#     'Simojovel':{'ruta':['Palenque','Villaflores','Juarez']},
#     'Ocosingo':{'ruta':['Amatenango','Teopisca','Altamirano']},
#     'Juarez':{'ruta':['Simojovel','Arriaga']},
#     'Palenque':{'ruta':['Simojovel','Huixtla','Reforma']},
#     'Villaflores':{'ruta':['Simojovel','Arriaga','Suchiapa']},
# }

# rutas = {
#     'Acala': {'ruta':['Villaflores']},
#     'Altamirano':{'ruta':['Huixtla','Amatenango']},
#     'Amatenango':{'ruta':['Cintalapa','Parral']},
#     'Bochil':{'ruta':['Ocosingo','Cintalapa']},
#     'Cintalapa':{'ruta':['Acala','Oxchuc']},
#     'Huixtla':{'ruta':['Ocosingo','Cintalapa']},
#     'Ixtapa':{'ruta':['Teopisca','Tapachula']},
#     'Oxchuc':{'ruta':['Villaflores']},
#     'Suchiapa':{'ruta':['Palenque','Altamirano','Reforma','Simojovel']},
#     'Reforma':{'ruta':['Amatenango','Juarez']},
#     'Montecristo':{'ruta':['Teopisca','Tapachula']},
#     'Parral':{'ruta':['Oxchuc','Teopisca']},
#     'Teopisca':{'ruta':['Villaflores']},
#     'Tapachula':{'ruta':['Villaflores']},
#     'Arriaga':{'ruta':['Ixtapa','Montecristo']},
#     'Simojovel':{'ruta':['Juarez','Arriaga']},
#     'Ocosingo':{'ruta':['Acala','Oxchuc']},
#     'Juarez':{'ruta':['Parral','Ixtapa']},
#     'Palenque':{'ruta':['Bochil','Huixtla']},
#     'Villaflores':{'ruta':['']},
# }

rutas = {
    'Acala': {'ruta':['Villaflores']},
    'Altamirano':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga']},
    'Amatenango':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']},
    'Bochil':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']},
    'Cintalapa':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula']},
    'Huixtla':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']},
    'Ixtapa':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula']},
    'Oxchuc':{'ruta':['Villaflores']},
    'Suchiapa':{'ruta':['Palenque','Altamirano','Reforma','Simojovel']},
    'Reforma':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga']},
    'Montecristo':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula']},
    'Parral':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula']},
    'Teopisca':{'ruta':['Villaflores']},
    'Tapachula':{'ruta':['Villaflores']},
    'Arriaga':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']},
    'Simojovel':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga']},
    'Ocosingo':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula']},
    'Juarez':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']},
    'Palenque':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga']},
    'Villaflores':{'ruta':['']},
}

# rutas = {
#     'Acala': {'ruta':['Villaflores'],'hora':[acala_salida]},
#     'Altamirano':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga'],'hora':[timedelta(days=0, hours=1, minutes=30, seconds=10)]},
#     'Amatenango':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo'],'hora':[amatenango_salida]},
#     'Bochil':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo'],'hora':[bochil_salida]},
#     'Cintalapa':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula'],'hora':[cintalapa_salida]},
#     'Huixtla':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo'],'hora':[huixtla_salida]},
#     'Ixtapa':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula'],'hora':[ixtapa_salida]},
#     'Oxchuc':{'ruta':['Villaflores'],'hora':[oxchuc_salida]},
#     'Suchiapa':{'ruta':['Palenque','Altamirano','Reforma','Simojovel'],'hora':[suchiapa_salida]},
#     'Reforma':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga'],'hora':[reforma_salida]},
#     'Montecristo':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula'],'hora':[montecristo_salida]},
#     'Parral':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula'],'hora':[parral_salida]},
#     'Teopisca':{'ruta':['Villaflores'],'hora':[teopisca_salida]},
#     'Tapachula':{'ruta':['Villaflores'],'hora':[tapachula_salida]},
#     'Arriaga':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo'],'hora':[arriaga_salida]},
#     'Simojovel':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga'],'hora':[simojovel_salida]},
#     'Ocosingo':{'ruta':['Acala','Oxchuc','Teopisca','Tapachula'],'hora':[ocosingo_salida]},
#     'Juarez':{'ruta':['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo'],'hora':[juarez_salida]},
#     'Palenque':{'ruta':['Bochil','Huixtla','Amatenango','Juarez','Arriaga'],'hora':[palenque_salida]},
#     'Villaflores':{'ruta':['']},
# }

horas = {
    'Acala': {'hora':['']},
    'Altamirano':{'hora':['']},
    'Amatenango':{'hora':['']},
    'Bochil':{'hora':['']},
    'Cintalapa':{'hora':['']},
    'Huixtla':{'hora':['']},
    'Ixtapa':{'hora':['']},
    'Oxchuc':{'hora':['']},
    'Suchiapa':{'hora':['']},
    'Reforma':{'hora':['']},
    'Montecristo':{'hora':['']},
    'Parral':{'hora':['']},
    'Teopisca':{'hora':['']},
    'Tapachula':{'hora':['']},
    'Arriaga':{'hora':['']},
    'Simojovel':{'hora':['']},
    'Ocosingo':{'hora':['']},
    'Juarez':{'hora':['']},
    'Palenque':{'hora':['']},
    'Villaflores':{'hora':['']},
}