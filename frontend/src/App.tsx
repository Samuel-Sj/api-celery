import Endpoint from "./components/endpoint";
import Header from "./components/header";
import TaskHistory from "./components/history";
import TaskCreate from "./components/task";
import './app.css'

export default function App(){

  return (
    <div className="app">
      <Header/>
      <Endpoint/>
      <TaskCreate/>
      <TaskHistory/>
    </div>
  )
}