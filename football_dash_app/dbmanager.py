import cx_Oracle

def db_connect():


    dsn_tns = cx_Oracle.makedsn('dbserver.mif.pg.gda.pl', '1521',
                                service_name='ORACLEMIF')
    conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)

    cursor = conn.cursor()
    return cursor


