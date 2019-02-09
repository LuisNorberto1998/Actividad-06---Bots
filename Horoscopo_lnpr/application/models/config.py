import web

db_host = 'localhost'
db_name = 'horoscopo_lnpr'
db_user = 'horoscopo'
db_pw = 'horoscopo.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )