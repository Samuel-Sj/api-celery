import { apiClient}from "./api";
import type TokenResponse from "../models/TokenResponse"

export async function loginRequest(username: string, password: string){
    const body = new URLSearchParams({username,password});
    const {data} = await apiClient.post<TokenResponse>("/token",body);
    return data.access_token;
}