import "./App.css";
import React, { useEffect, useState } from "react";
import { getTodos, createTodo } from "./api/todos";

export function App() {
  const [todos, setTodos] = useState([]);
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    load();
  }, []);

  async function load() {
    setLoading(true);
    try {
      const data = await getTodos();
      setTodos(data || []);
    } catch (err) {
      console.error("Failed to fetch todos", err);
    } finally {
      setLoading(false);
    }
  }

  async function handleAdd(e) {
    e.preventDefault();
    const title = text.trim();
    if (!title) return;
    try {
      const created = await createTodo({ title });
      setTodos((prev) => [created, ...prev]);
      setText("");
    } catch (err) {
      console.error("Failed to create todo", err);
    }
  }

  return (
    <div className="App">
      <section>
        <h1>List of TODOs</h1>
          <ul className="no-bullets">
          <li>Learn Docker</li>
          <li>Learn React</li>
        </ul>


        {loading ? (
          <div>Loading...</div>
        ) : (
          <ul className="no-bullets">
            {todos.length === 0 && <li>No todos</li>}
            {todos.map((todo) => (
              <li key={todo._id}>{todo.title}</li>
            ))}
          </ul>
        )}
      </section>

      <section style={{ marginTop: 20 }}>
        <h1>Create a ToDo</h1>
        <form onSubmit={handleAdd}>
          <label htmlFor="todo">ToDo: </label>
          <input
            id="todo"
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button type="submit" style={{ marginLeft: "10px" }}>
            Add ToDo!
          </button>
        </form>
      </section>
    </div>
  );
}

export default App;
