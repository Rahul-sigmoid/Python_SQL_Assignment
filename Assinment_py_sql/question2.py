# importing the necessary libraries
import psycopg2
from openpyxl.workbook import Workbook
import pandas as pd
from dataclasses import dataclass, replace


@dataclass(frozen=True)

class Compensation:

    def com(self):
        try:
            # connecting postgres database to intellij
            conn = psycopg2.connect(
                database="sql",
                user="postgres",
                password="rahul")

            cursor = conn.cursor()
            # below is query
            script = """
            select emp.ename, emp.empno, dept.dname, (case when enddate is not null then ((enddate-startdate+1)/30)*(jobhist.sal) else ((current_date-startdate+1)/30)*(jobhist.sal) end)as Total_Compensation,
            (case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp 
            where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno
            """
            # executing the query
            cursor.execute(script)
            # listing the columns
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            # converting data to datafarame
            df = pd.DataFrame(list(data), columns=columns)
            # Create a Pandas Excel writer
            writer = pd.ExcelWriter('question2.xlsx')
            # Convert the dataframe to an XlsxWriter Excel object
            df.to_excel(writer, sheet_name='bar')
            # closing the excel writer and output the excel file
            writer.save()

        except Exception as e:
            # if exception thrown in try block
            print("Error", e)

        finally:

            if conn is not None:
                # after completion of above block closing the connection
                cursor.close()
                conn.close()

        return True

