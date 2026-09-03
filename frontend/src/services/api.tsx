import axios from "axios";
import type TaskStatus from "../models/TaskStatus";
import type Task from "../models/Task";

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

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

async function createTask(x: number, y: number): Promise<Task | undefined> {
    try {
        const response = await apiClient.post<Task>('/add', null, { params: { x, y } });
        return response.data;
    } catch (error) {
        console.error(`Erro ao criar task (${x} + ${y}):`, error);
        return undefined;
    }
}

export { apiClient, getTaskID, createTask, getAllTasks };