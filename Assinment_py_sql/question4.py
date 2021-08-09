# importing the necessary libraries
import psycopg2
from openpyxl.workbook import Workbook
import pandas as pd
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Department:

    def dept(self):
        try:
            # connecting postgres database to intellij
            conn = psycopg2.connect(
                database="sql",
                user="postgres",
                password="rahul")

            cursor = conn.cursor()
            # below is query
            script = """
                    select dept.deptno, dept_name, sum(total_compensation) from Compensation, dept
                    where Compensation.dept_name=dept.dname
                    group by dept_name, dept.deptno
                    """
            # executing the query
            cursor.execute(script)
            # listing the columns
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            # converting data to datafarame
            df = pd.DataFrame(list(data), columns=columns)
            # Create a Pandas Excel writer
            writer = pd.ExcelWriter('question4.xlsx')
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


