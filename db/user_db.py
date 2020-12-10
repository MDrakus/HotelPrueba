from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    nombre: str
    ubicacion: str
    estrellas: str
    habitaciones:int
    tipoHabitacion:Dict[str,Dict[str,int]]
    servadicional:Dict[str,str]
    porc_ocu_ult_anno:Dict[str,int]

database_users = Dict[str, UserInDB]

database_users = {
    "Hotel1": UserInDB(**{"nombre":"Hotel1",
                            "ubicacion":"Colombia",
                            "estrellas":"cinco",
                            "habitaciones":30,
                            "tipoHabitacion":[{"sencilla":[{"cantidad":15,
                                                            "preciopromin":120000}],
                                                   "doble":[{"cantidad":10,
                                                             "preciopromin":200000}],
                                                   "triple":[{"cantidad":5,
                                                             "preciopromin":250000}]
                                                                }],
                            "servadicional":[{"lavanderia":"si",
                                                     "restaurante":"si",
                                                     "bar":"si",
                                                     "wifi":"si",
                                                     "cable":"si"}],
                            "porc_ocu_ult_anno":[{"enero":95,
                                                  "febrero":80,
                                                  "marzo":60,
                                                  "abril":70,
                                                  "mayo":50,
                                                  "junio":100,
                                                  "julio":100,
                                                  "agosto":70,
                                                  "septiembre":60,
                                                  "octubre":70,
                                                  "noviembre":80,
                                                  "diciembre":100
                                                }]
                                            }),

                                                "Hotel1": UserInDB(**{"nombre":"Hotel1",
                            "ubicacion":"Colombia",
                            "estrellas":"tres",
                            "habitaciones":12,
                            "tipoHabitacion":[{"sencilla":[{"cantidad":4,
                                                            "preciopromin":70000}],
                                                   "doble":[{"cantidad":4,
                                                             "preciopromin":110000}],
                                                   "triple":[{"cantidad":4,
                                                             "preciopromin":150000}]
                                                                }],
                            "servadicional":[{"lavanderia":"si",
                                                     "restaurante":"si",
                                                     "bar":"no",
                                                     "wifi":"no",
                                                     "cable":"no"}],
                            "porc_ocu_ult_anno":[{"enero":80,
                                                  "febrero":70,
                                                  "marzo":60,
                                                  "abril":75,
                                                  "mayo":60,
                                                  "junio":85,
                                                  "julio":90,
                                                  "agosto":80,
                                                  "septiembre":60,
                                                  "octubre":70,
                                                  "noviembre":80,
                                                  "diciembre":100
                                                }]
                                            }),
}

def get_user(nombre: str):
    if nombre in database_users.keys():
        return database_users[nombre]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
