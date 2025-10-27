const API_URL = 'http://localhost:8000/todos/';

export async function getTodos() {
  const res = await fetch(API_URL);
  if (!res.ok) throw new Error(`GET /todos failed: ${res.status}`);
  return res.json();
}

export async function createTodo(payload) {
  const res = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error(`POST /todos failed: ${res.status}`);
  return res.json();
}

export default { getTodos, createTodo };
