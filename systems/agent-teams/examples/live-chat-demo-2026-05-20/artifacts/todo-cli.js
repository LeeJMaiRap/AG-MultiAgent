#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const DB_PATH = path.join(__dirname, 'todo-data.json');

function usage() {
  return [
    'Usage:',
    '  node todo-cli.js add <text>',
    '  node todo-cli.js list',
    '  node todo-cli.js done <id>',
    '  node todo-cli.js delete <id>'
  ].join('\n');
}

function readDb() {
  if (!fs.existsSync(DB_PATH)) {
    return { nextId: 1, todos: [] };
  }

  try {
    const raw = fs.readFileSync(DB_PATH, 'utf8');
    const data = JSON.parse(raw);

    if (!data || !Array.isArray(data.todos) || typeof data.nextId !== 'number') {
      throw new Error('Invalid database format');
    }

    return data;
  } catch (err) {
    console.error('Error: failed to read local data file.');
    process.exit(1);
  }
}

function writeDb(data) {
  try {
    fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2) + '\n', 'utf8');
  } catch (err) {
    console.error('Error: failed to write local data file.');
    process.exit(1);
  }
}

function addTodo(text) {
  const clean = String(text || '').trim();
  if (!clean) {
    console.error('Error: missing todo text.');
    console.error(usage());
    process.exit(1);
  }

  const db = readDb();
  const todo = {
    id: db.nextId,
    text: clean,
    completed: false,
    createdAt: new Date().toISOString()
  };

  db.todos.push(todo);
  db.nextId += 1;
  writeDb(db);

  console.log(`Added #${todo.id}: ${todo.text}`);
}

function listTodos() {
  const db = readDb();

  if (db.todos.length === 0) {
    console.log('No todos yet.');
    return;
  }

  for (const todo of db.todos) {
    const status = todo.completed ? 'completed' : 'pending';
    console.log(`#${todo.id} [${status}] ${todo.text}`);
  }
}

function doneTodo(idRaw) {
  const id = Number(idRaw);
  if (!Number.isInteger(id) || id <= 0) {
    console.error('Error: id must be positive integer.');
    console.error(usage());
    process.exit(1);
  }

  const db = readDb();
  const todo = db.todos.find((item) => item.id === id);

  if (!todo) {
    console.error(`Error: todo #${id} not found.`);
    process.exit(1);
  }

  if (todo.completed) {
    console.log(`Todo #${id} already completed.`);
    return;
  }

  todo.completed = true;
  todo.completedAt = new Date().toISOString();
  writeDb(db);

  console.log(`Done #${id}: ${todo.text}`);
}

function deleteTodo(idRaw) {
  const id = Number(idRaw);
  if (!Number.isInteger(id) || id <= 0) {
    console.error('Error: id must be positive integer.');
    console.error(usage());
    process.exit(1);
  }

  const db = readDb();
  const idx = db.todos.findIndex((item) => item.id === id);

  if (idx === -1) {
    console.error(`Error: todo #${id} not found.`);
    process.exit(1);
  }

  const [removed] = db.todos.splice(idx, 1);
  writeDb(db);

  console.log(`Deleted #${id}: ${removed.text}`);
}

function main() {
  const [, , command, ...args] = process.argv;

  switch (command) {
    case 'add':
      addTodo(args.join(' '));
      break;
    case 'list':
      listTodos();
      break;
    case 'done':
      doneTodo(args[0]);
      break;
    case 'delete':
      deleteTodo(args[0]);
      break;
    default:
      console.error('Error: invalid command.');
      console.error(usage());
      process.exit(1);
  }
}

main();
