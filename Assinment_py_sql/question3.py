# importing the necessary libraries
import psycopg2
import xlrd
#from openpyxl.workbook import Workbook
import openpyxl
import os
import pandas as pd
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Department:

    def dept(self):

        try:
            # connecting postgres database to intellij
            df= pd.read_excel("question2.xlsx")
            #sheet = df.sheet_by_name("Source")
            conn = psycopg2.connect (database = "sql", user="postgres", password="rahul")#, host="localhost", port="5432")

            cursor = conn.cursor()
            query1="""
            CREATE TABLE Compensat (
	            emp_name varchar(10) ,
	            emp_no integer PRIMARY KEY,
	            dept_name VARCHAR ( 50 ) ,
	            total_compensation numeric,
	            months_spent numeric
            );
            """
            query = """INSERT INTO Compensat (emp_name, emp_no, dept_name, Total_Compensation, Months_Spent) VALUES (%s, %s, %s, %s, %s
            )"""

            for r in range(1,len(df)):
                emp_name=df['ename'][r]
                emp_no=df['empno'][r]
                dept_name=df['dname'][r]
                total_compensation = df['total_compensation'][r]
                months_spent=df['months_spent'][r]

            values = (emp_name, emp_no, dept_name, total_compensation, months_spent)

            # executing the queries
            cursor.execute(query1)
            cursor.execute(query, values)
            print(df)

        except Exception as e:
            # if exception thrown in try block
            print("Error", e)

        finally:

            if conn is not None:
                # after completion of above block closing the connection
                cursor.close()
                conn.close()

        return True


