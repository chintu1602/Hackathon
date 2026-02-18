from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
employees = []

class Employee(BaseModel):
	id: int
	name: str
	role: str

@app.get('/')
def get_all_employees():
	return employeess

@app.post('/add')
def add_employee(e:Employee):
	employees.append({'id':e.id, 'name':e.name, 'role':e.role})
	return {'message':'Employee added successfully'}

@app.get('/get_details')
def get_employee(id:int):
	for e in employees:
		if e['id'] == id:
			return e
	
	return {'message':'Employee not found'}

@app.delete('/delete')
def delete_employee(id:int):
    for e in employees:
		if e['id'] == id:
			del employees[employees.index(e)]
            return {'message':'Employee deleted successfully'}

@app.put('/update')
def update_employee(id:int, name:str, role:str):
    for e in employees:
        if e['id'] == id:
            e['name'] = name
            e['role'] = role
            return {'message':'Employee updated successfully'}
    return {'message':'Employee not found'}

