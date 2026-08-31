import { useState } from "react"
import { getTaskID } from "../services/api"
import type TaskStatus from "../models/TaskStatus"


export default function Endpoint() {
    const [TaskID, setTaskID] = useState("");
    const [result, setResult] = useState<TaskStatus | undefined>(undefined);


    return (
        <div className="endpointPanel">
            <span className="endpointSpan">Task Id</span>

            <input className="inputEndpoint"
                value={TaskID}
                onChange={(e) => setTaskID(e.target.value)}
                spellCheck={false} />

            <button className="btn-send-request" onClick={async () => setResult(await getTaskID(TaskID))} type="button">
                Enviar Solicitação
            </button>

            {result && (
                <div className="endpoint-result">
                    <span>Status: {result.status} !</span>

                </div>
            )}
        </div>
    )
}