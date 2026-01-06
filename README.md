# terminal-todo

A minimal CLI todo manager. Fast task management without leaving the terminal.

## Installation

```bash
pip install .
```

After installation, the `todo` command will be available globally.

## Usage

### Add a todo

```bash
$ todo add "Buy groceries"
Added: Buy groceries
```

### List all todos

```bash
$ todo list
[ ] 1  Buy groceries
[ ] 2  Write blog post
[x] 3  Call dentist
```

Completed todos appear in green with `[x]`, pending todos in yellow with `[ ]`.

### Mark a todo as done

```bash
$ todo done 1
Completed: Buy groceries

$ todo list
[x] 1  Buy groceries
[ ] 2  Write blog post
[x] 3  Call dentist
```

### Remove a todo

```bash
$ todo remove 3
Removed: Call dentist

$ todo list
[x] 1  Buy groceries
[ ] 2  Write blog post
```

## Storage

Todos are stored locally in `~/.todo.json`. The file is human-readable and safe to edit manually:

```json
[
  {
    "id": 1,
    "text": "Buy groceries",
    "done": true
  },
  {
    "id": 2,
    "text": "Write blog post",
    "done": false
  }
]
```

## Implementation

Everything lives in `todo.py` (~92 lines). Simple, readable, and easy to extend.

## License

MIT