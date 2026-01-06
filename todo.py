#!/usr/bin/env python3
"""A simple todo app."""
import json
from pathlib import Path
import click

TODO_FILE = Path.home() / ".todo.json"


def load_todos():
    """Load todos from file."""
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE) as f:
        return json.load(f)


def save_todos(todos):
    """Save todos to file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


@click.group()
def cli():
    """A simple todo manager."""
    pass


@cli.command()
@click.argument("text")
def add(text):
    """Add a new todo."""
    todos = load_todos()
    next_id = max([t["id"] for t in todos], default=0) + 1
    todos.append({"id": next_id, "text": text, "done": False})
    save_todos(todos)
    click.echo(f"Added: {text}")


@cli.command()
def list():
    """List all todos."""
    todos = load_todos()
    if not todos:
        click.echo("No todos yet!")
        return
    
    for todo in todos:
        status = "[x]" if todo["done"] else "[ ]"
        click.echo(f"{status} {todo['id']}  {todo['text']}")


@cli.command()
@click.argument("todo_id", type=int)
def done(todo_id):
    """Mark a todo as done."""
    todos = load_todos()

    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            save_todos(todos)
            click.echo(f"Completed: {todo['text']}")
            return

    click.echo(f"Todo {todo_id} not found")


if __name__ == "__main__":
    cli()
