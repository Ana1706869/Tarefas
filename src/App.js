import React,{useState,useEffect} from "react"

function App(){
  const [tarefas,setTarefas]=useState([])
  const [titulo,setTitulo]=useState("")

  const carregarTarefas=()=>{
    fetch("http://127.0.0.1:8000/tarefas").then(res=>res.json())
    .then(data=>setTarefas(data))
  }
  useEffect(()=>{
    carregarTarefas()
  },[])

  const adicionarTarefa=()=>{
    fetch("http://127.0.0.1:8000/tarefas",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify({titulo})
    }).then(()=>{
      setTitulo("")
      carregarTarefas()
    })

  }
  const removerTarefa=(id)=>{
    fetch(`http://127.0.0.1:8000/tarefas/${id}`,{
      method: "DELETE"}).then(()=>carregarTarefas())
    }
    return(
      <div style={{padding:20}}>
        <h1>Lista de Tarefas</h1>
        <input value={titulo} onChange={(e)=>setTitulo(e.target.value)} placeholder="Nova tarefa"/>
        <button onClick={adicionarTarefa}>Adicionar</button>
        <ul>
          {tarefas.map((tarefa)=>(
            <li key={tarefa.id}>{tarefa.titulo}
            <button onClick={()=>removerTarefa(tarefa.id)}>Remover</button>
            </li>
          ))}
        </ul>
      </div>
    )
  }
  export default App

  

