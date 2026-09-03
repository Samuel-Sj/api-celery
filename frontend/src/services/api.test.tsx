import { apiClient, getAllTasks } from "./api";
import type {Task} from "../models/Task";

describe('getAllTasks', () => {
    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('retorna a lista de tasks quando a API responde com sucesso', async () => {
        const tasks: Task[] = [{ task_id: 'abc-123', status: 'SUCCESS' }];
        jest.spyOn(apiClient, 'get').mockResolvedValue({ data: tasks });

        const result = await getAllTasks();

        expect(apiClient.get).toHaveBeenCalledWith('/tasks');
        expect(result).toEqual(tasks);
    });

    it('retorna uma lista vazia se a requisição falhar', async () => {
        jest.spyOn(apiClient, 'get').mockRejectedValue(new Error('network error'));

        const result = await getAllTasks();

        expect(result).toEqual([]);
    });
});