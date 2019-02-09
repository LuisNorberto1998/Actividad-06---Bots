import web
import config

db = config.db
ruta = "../../static/images/"


def get_all_horoscopos():
    try:
        return db.select('horoscopos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_horoscopos(id_signo):
    try:
        return db.select('horoscopos', where='id_signo=$id_signo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_horoscopos(id_signo):
    try:
        return db.delete('horoscopos', where='id_signo=$id_signo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_horoscopos(nombre_signo, descripcion_signo, ruta_img_signo):
    try:
        ruta_final = (ruta + ruta_img_signo)
        return db.insert('horoscopos', nombre_signo=nombre_signo,
                         descripcion_signo=descripcion_signo,
                         ruta_img_signo=ruta_final)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_horoscopos(id_signo, nombre_signo, descripcion_signo, ruta_img_signo):
    try:
        ruta_final = (ruta + ruta_img_signo)
        return db.update('horoscopos', id_signo=id_signo,
                         nombre_signo=nombre_signo,
                         descripcion_signo=descripcion_signo,
                         ruta_img_signo=ruta_final,
                         where='id_signo=$id_signo',
                         vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
