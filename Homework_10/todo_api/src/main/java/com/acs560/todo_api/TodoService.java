package com.acs560.todo_api;

import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

//Application won't run if you forgot to add @Service
@Service
public class TodoService {

	@Autowired
	private TodoRepository repository;
	
	public List<Todo> getTodoList(){
		return (List<Todo>) repository.findAll();
	}
	
	public Todo getTodo(int id) {
		Optional<Todo> todo = repository.findById(id);
		return todo.orElse(null);
	}
	
	public Todo storeTodo(Todo todo) {
		return repository.save(todo);
	}
	
	public boolean deleteTodo(int id) {
		boolean deleted = false;
		Optional<Todo> todo = repository.findById(id);
		if (todo.isPresent()) {
			repository.delete(todo.get());
			deleted = true;
		}
		return deleted;
	}
}
