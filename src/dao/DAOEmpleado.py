import pymysql

class DAOEmpleado:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self, codigo):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            if codigo == None:
                cursor.execute("SELECT * FROM empleados order by nombre asc")
            else:
                cursor.execute("SELECT * FROM empleados where codigo = %s order by nombre asc", (codigo,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO empleados(nombre,apellido,correo,telefono,puesto,salario) VALUES(%s, %s, %s, %s, %s, %s)", (data['nombre'],data['apellido'],data['correo'],data['telefono'],data['puesto'],data['salario']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, codigo, data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE empleados set nombre = %s, apellido = %s, correo = %s, telefono = %s, puesto = %s, salario = %s where codigo = %s", (data['nombre'],data['apellido'],data['correo'],data['telefono'],data['puesto'],data['salario'],codigo,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, codigo):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleados where codigo = %s", (codigo,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
