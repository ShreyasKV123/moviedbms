from secrets import choice
import sqlite3


class DataBase:

    def __init__(self):#database initialisation through init
        self.conn = sqlite3.connect("movie.db")

    def tableCreation(self):
        cur = self.conn.cursor()#cur to use for connection with database

        cur.execute('''CREATE TABLE IF NOT EXISTS Movie
        (Movie_Name varchar2(30),
        Lead_actor varchar2(30),
        Lead_actress varchar2(30),
        Director_name varchar2(20),
        Year_Of_Release number,
        PRIMARY KEY(Movie_Name))''')



    def insertToMovies(self, moviename,leadactor,leadactress,dirname,yor):
        self.conn.execute("INSERT INTO Movie (Movie_Name,Lead_actor,Lead_actress,Director_name, Year_Of_Release) VALUES (?, ?, ?,?,?)", (moviename,leadactor,leadactress,dirname,yor))
        self.conn.commit()
        self.conn.close()
    def retrievemovie(self):#query to select movies from 2022
        cur = self.conn.cursor()
        cur.execute("SELECT Movie_Name ,Lead_actor  ,Lead_actress , Director_name from Movie where Year_Of_Release=2022 ")
        movies2022= cur.fetchall()
        return movies2022
    def retrievebyactorname(self):#query to select movies of AA
        cur = self.conn.cursor()
        cur.execute("SELECT Movie_Name ,Lead_actor  ,Lead_actress , Director_name,Year_Of_Release from Movie where Lead_actor='AA' ")
        movies2022= cur.fetchall()
        return movies2022





db = DataBase()

# db.tableCreation()
def insertion():
        mname=input("enter movie name")
        lactor=input("enter movie's lead actor")
        lactress=input("enter movie's lead actress")
        dirname=input("enter director name")
        year=int(input("enter movie release year"))
        db.insertToMovies(mname,lactor,lactress,dirname,year)

# db.insertToMovies('RRR', 'RC_NTR','jenny','ssr' ,2022)
# db.insertToMovies('pushpa', 'AA','Rashmika','Sukumar' ,2021)
print(db.retrievemovie())
print(db.retrievebyactorname())
# insertion()  to insert a new movie details
    
