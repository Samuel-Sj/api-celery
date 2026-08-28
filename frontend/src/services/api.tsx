import axios from "axios";
import type TaskStatus  from "../models/TaskStatus";

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

async function getTaskID(task_id: string): Promise<TaskStatus | undefined> {
    try {
        const response = await apiClient.get<TaskStatus>(`/status/${task_id}`);

        return response.data;
    } catch (error) {
        console.error(
            `Erro ao fazer requisição pela task id ${task_id}:`,
            error
        );

        return undefined;
    }
}

export { apiClient, getTaskID };
