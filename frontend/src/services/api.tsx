import axios from "axios";
import type TaskStatus from "../models/TaskStatus";
import type Task from "../models/Task";

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
);

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const isLoginRequest = error.config?.url?.includes("/token");
    if (error.response?.status === 401 && !isLoginRequest) {
      localStorage.removeItem("token");
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);



async function getAllTasks (): Promise<Task[] | []> {
    try {
        const response = await apiClient.get<Task[]>("/task");
        return response.data;
    } catch (error) {
        console.error(`Erro ao buscar todas as task: ${error}`)
        return [];
        
    }
}

async function getTaskID(task_id: string): Promise<TaskStatus | undefined> {
    try {
        const response = await apiClient.get<TaskStatus>(`/status/${task_id}`);
        return response.data;
    } catch (error) {
        console.error(`Erro ao fazer requisição pela task id ${task_id}:`, error);
        return undefined;
    }
}

async function createAddTask(x: number, y: number): Promise<Task | undefined> {
    try {
        const response = await apiClient.post<Task>('/add', null, { params: { x, y } });
        return response.data;
    } catch (error) {
        console.error(`Erro ao criar task (${x} + ${y}):`, error);
        return undefined;
    }
}

async function createSubtractTask(x: number, y: number): Promise <Task | undefined>{
    try {
        const response = await apiClient.post<Task>('/subtract',null, {params: {x,y}});
        return response.data;
    } catch (error) {
        console.error (`Erro ao criar task (${x} - ${y}):`,error);
        return undefined;
        
    }
}

async function createMultiplyTask(x: number, y: number): Promise <Task | undefined>{
    try {
        const response = await apiClient.post<Task>('/multiply',null, {params:{x,y}});
        return response.data;
        
    } catch (error) {
        console.error (`Erro ao criar task (${x} - ${y}):`,error);
        return undefined;
        
    }
}

async function createDivisionTask (x: number, y: number): Promise<Task | undefined>{
    try {
        const response = await apiClient.post<Task>('/division',null, {params: {x,y}});
        return response.data;
    } catch (error) {
        console.error (`Erro ao criar task (${x} - ${y}):`,error);
        return undefined;
        
    }
}

export { apiClient, getTaskID, createAddTask,createSubtractTask, createDivisionTask,createMultiplyTask, getAllTasks };