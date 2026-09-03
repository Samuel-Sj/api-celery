import { useEffect, useState } from "react";
import type Task from "./models/Task";
import Endpoint from "./components/endpoint";
import Header from "./components/header";
import TaskHistory from "./components/history";
import TaskCreate from "./components/task";
import './app.css'
import { getAllTasks } from "./services/api";

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() =>{
    getAllTasks().then(setTasks);
  }, []);

  function handleTaskCreated(task: Task) {
    setTasks((prev) => [task, ...prev]);
  }

  return (
    <div className="app">
      <Header />
      <Endpoint />
      <TaskCreate onTaskCreated={handleTaskCreated} />
      <TaskHistory tasks={tasks} />
    </div>
  )
}