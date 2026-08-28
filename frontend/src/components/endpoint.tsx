import { use, useState } from "react"
import {apiClient,getTaskID} from "../services/api"


export default function Endpoint (){
    const [TaskID,setTaskID] = useState("".trim());

    return (
        <div className="endpointPanel">
            <span className="endpointSpan">Endpoint da API</span>

            <input className="inputEndpoint"
            value={apiClient.defaults.baseURL}
            onChange={(e)=>setTaskID(e.target.value)}
            spellCheck={false}/>

            <button className="btn-send-request" onClick={() => getTaskID(TaskID)} type="button">
                Enviar Solicitação
            </button>

        </div>
    )
}