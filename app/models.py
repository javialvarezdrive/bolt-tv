from typing import TypedDict, List, Optional
from datetime import date

class Agent(TypedDict):
    id: int
    nip: str
    nombre: str
    apellidos: str
    seccion: str
    grupo: str
    email: str
    telefono: str
    is_monitor: bool
    created_at: str

class Activity(TypedDict):
    id: int
    name: str

class GymReservation(TypedDict):
    id: int
    activity_date: date
    shift: str
    monitor_id: int
    activity_id: int
    created_at: str

class AgentActivity(TypedDict):
    id: int
    agent_id: int
    reservation_id: int
    created_at: str
