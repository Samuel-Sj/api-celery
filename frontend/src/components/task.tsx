import { useState } from "react";
import  { createTask } from "../services/api";

export default function TaskCreate() {
    const [y, setY] = useState('');
    const [x, setX] = useState('');

    return (
        <div className="task-panel">
            <span className="task-create-panel">Criar nova task no Celery</span>
            <div className="task-panel-field">
                <label htmlFor="task-panel-x">X</label>
                <input
                    id="task-x"
                    className="task-number"
                    type="number"
                    value={x}
                    onChange={(e) => setX(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter'}
                    placeholder='0' />
            </div>
            <div className="task-panel-field">
                <label htmlFor="task-panel-y">Y</label>
                <input
                    id="task-y"
                    className="task-number"
                    type="number"
                    value={y}
                    onChange={(e) => setY(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter'}
                    placeholder="0" />
            </div>
            <button className="button-submit-task" onClick={() =>createTask(x,y)} disabled={false} type="button">Enfileirar</button>
        </div>
    )

}