import type Task from "../models/Task";

interface TaskHistoryProps {
    tasks: Task[];
}

export default function TaskHistory({ tasks = [] }: TaskHistoryProps) {
    return (
        <div className="task-history">
            <span className="task-hist">Histórico de Tasks</span>
            {tasks.length === 0 ? (
                <p className="task-history-empty">Nenhuma task enviada ainda.</p>
            ) : (
                <ul className="task-history-list">
                    {tasks.map((t) => (
                        <li key={t.task_id} className="task-history-item">
                            {t.task_id}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}