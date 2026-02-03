from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct year(s_datetime) as year 
                    FROM sighting 
                    WHERE year(s_datetime) >= 1910 and year(s_datetime)<=2014 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_shape(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct shape as forma
                    from sighting 
                    where year(s_datetime) = %s """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(row["forma"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_state():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct name, id
                    FROM state"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["name"], row["id"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_neighbors(anno,forma):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT n.state1, n.state2, count(*) as peso 
        FROM neighbor n, sighting s 
        where (n.state1=s.state or n.state2= s.state) 
        and year(s.s_datetime )= %s and s.shape = %s
        group by n.state1, n.state2 
        having count(*)>0"""

        cursor.execute(query,(anno,forma,))

        for row in cursor:
            result.append((row["state1"], row["state2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_coordinate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select state, AVG(latitude) AS lat, AVG(longitude) AS lon
                    from sighting
                    GROUP BY state"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["state"], row["lat"], row["lon"]))

        cursor.close()
        conn.close()
        return result
