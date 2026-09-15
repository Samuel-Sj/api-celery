import { useState } from "react";
import { createAddTask, createSubtractTask, createMultiplyTask, createDivisionTask } from "../services/api";
import type Task from "../models/Task";

interface TaskCreateProps {
    onTaskCreated: (task: Task) => void;
}

type OperationId = 'add' | 'subtract' | 'multiply' | 'divide';

const OPERATIONS: { id: OperationId; label: string; run: (x: number, y: number) => Promise<Task | undefined> }[] = [
    { id: 'add', label: 'Adição', run: createAddTask },
    { id: 'subtract', label: 'Subtração', run: createSubtractTask },
    { id: 'multiply', label: 'Multiplicação', run: createMultiplyTask },
    { id: 'divide', label: 'Divisão', run: createDivisionTask },
];

export default function TaskCreate({ onTaskCreated }: TaskCreateProps) {
    const [x, setX] = useState('');
    const [y, setY] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const [operation, setOperation] = useState<OperationId | null>(null);
    const [error, setError] = useState<string | null>(null);

    function chooseOperation(id: OperationId) {
        setOperation(id);
    }

    async function handleSubmit() {
        setError(null);

        if (!operation) {
            setError("Escolha uma operação antes de enfileirar.");
            return;
        }
        const xi = parseInt(x, 10);
        const yi = parseInt(y, 10);
        if (Number.isNaN(xi) || Number.isNaN(yi)) {
            setError("Informe dois números inteiros válidos.");
            return;
        }

        const selected = OPERATIONS.find((op) => op.id === operation)!;
        setSubmitting(true);
        const task = await selected.run(xi, yi);
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
            <div className="task-options-panel">
                {OPERATIONS.map((op) => (
                    <button
                        key={op.id}
                        className={`button-option-choose ${operation === op.id ? 'selected' : ''}`}
                        type="button"
                        onClick={() => chooseOperation(op.id)}
                    >
                        {op.label}
                    </button>
                ))}
            </div>
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