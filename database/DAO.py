from database.DB_connect import DBConnect
from model.arco import Arco
from model.object import Object


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM objects o"
        cursor.execute(query)

        for row in cursor:
            result.append(Object(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdgesPeso( idMapAO):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo.object_id as o1, eo2.object_id as o2, count(*) as peso
from exhibition_objects eo , exhibition_objects eo2 
where eo.exhibition_id = eo2.exhibition_id 
and eo.object_id < eo2.object_id 
group by eo.object_id, eo2.object_id
 order by peso desc"""
        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMapAO[row["o1"]],idMapAO[row["o2"]],row["peso"]))
        cursor.close()
        cursor.close()
        conn.close()
        if len(result) == 0:
            return None
        return result

