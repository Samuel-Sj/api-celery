import { useState } from "react";
import { createTask } from "../services/api";
import type Task from "../models/Task";

interface TaskCreateProps {
    onTaskCreated: (task: Task) => void;
}

export default function TaskCreate({ onTaskCreated }: TaskCreateProps) {
    const [x, setX] = useState('');
    const [y, setY] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const [error, setError] = useState<string | null>(null);

    async function handleSubmit() {
        setError(null);
        const xi = parseInt(x, 10);
        const yi = parseInt(y, 10);
        if (Number.isNaN(xi) || Number.isNaN(yi)) {
            setError("Informe dois números inteiros válidos.");
            return;
        }
        setSubmitting(true);
        const task = await createTask(xi, yi);
        setSubmitting(false);
        if (!task) {
            setError("Não foi possível enfileirar a task.");
            return;
        }
        onTaskCreated(task);
        setX('');
        setY('');
    }

    return (
        <div className="task-panel">
            <span className="task-create-panel">Criar nova task no Celery</span>
            <div className="task-panel-field">
                <label htmlFor="task-x">X</label>
                <input id="task-x" className="task-number" type="number"
                    value={x} onChange={(e) => setX(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSubmit()} placeholder='0' />
            </div>
            <div className="task-panel-field">
                <label htmlFor="task-y">Y</label>
                <input id="task-y" className="task-number" type="number"
                    value={y} onChange={(e) => setY(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSubmit()} placeholder="0" />
            </div>
            <button className="button-submit-task" type="button" onClick={handleSubmit} disabled={submitting}>
                {submitting ? "Enviando..." : "Enfileirar"}
            </button>
            {error && <p className="task-error">{error}</p>}
        </div>
    );
}