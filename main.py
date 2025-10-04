from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app=FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

def get_db_connection():
    conn=sqlite3.connect("tarefas.db")
    conn.row_factory=sqlite3.Row
    return conn

conn=get_db_connection()
conn.execute("""CREATE TABLE IF NOT EXISTS tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT,
             titulo TEXT NOT NULL)""")
conn.commit()
conn.close()

@app.get("/tarefas")
def listar_tarefas():
    conn=get_db_connection()
    tarefas=conn.execute("SELECT * FROM tarefas").fetchall()
    conn.close()
    return [dict(tarefa)for tarefa in tarefas]

@app.post("/tarefas")
def adicionar_tarefa(tarefa:dict):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (tarefa["titulo"],) )
    conn.commit()
    conn.close()
    return {"msg":"Tarefa adicionada com sucesso"}

@app.delete("/tarefas/{id}")
def remover_tarefa(id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return {"msg":f"Tarefa {id} removida"}



    

