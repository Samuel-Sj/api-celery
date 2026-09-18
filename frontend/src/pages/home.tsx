import { useEffect, useState } from "react";
import type Task from "../models/Task";
import Endpoint from "../components/endpoint";
import Header from "../components/header";
import TaskHistory from "../components/history";
import TaskCreate from "../components/task";
import { getAllTasks } from "../services/api";
import { useAuth } from "../contexts/AuthContext";

export default function Home() {
  const { signOut } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    getAllTasks().then(setTasks);
  }, []);

  function handleTaskCreated(task: Task) {
    setTasks((prev) => [task, ...prev]);
  }

  return (
    <div className="app">
      <Header />
      <button onClick={signOut}>Sair</button>
      <Endpoint />
      <TaskCreate onTaskCreated={handleTaskCreated} />
      <TaskHistory tasks={tasks} />
    </div>
  );
}