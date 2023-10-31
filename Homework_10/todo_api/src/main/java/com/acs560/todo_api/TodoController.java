package com.acs560.todo_api;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("todos")
@RestController
public class TodoController {
	@Autowired
	private TodoService service;

	@GetMapping()
	public List<Todo> getTodos(){
		return service.getTodoList();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Todo> getTodo(@PathVariable("id") int id){
		Todo todo = service.getTodo(id);
		return todo != null ? new ResponseEntity<>(todo, HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
	@PostMapping()
	public ResponseEntity<String> addTodo(@RequestBody Todo todo){
		return service.storeTodo(todo) != null ? new ResponseEntity<>("Saved Successfully!", HttpStatus.OK)
				: new ResponseEntity<>("Not Saved Successfully!", HttpStatus.OK);
	}
	@PutMapping("/{id}")
	public ResponseEntity<String> updateTodo(@PathVariable("id") int id, @RequestBody Todo todo){
		Todo exTodo = service.getTodo(id);
		todo.setId(id);
		return exTodo != null ? service.storeTodo(todo) != null
				? new ResponseEntity<>("Updated Successfully", HttpStatus.OK)
				: new ResponseEntity<>("Not updated Successfully", HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
	@DeleteMapping("/{id}")
	public ResponseEntity<String> deleteTodo(@PathVariable("id") int id){
		Todo exTodo = service.getTodo(id);
		return exTodo != null ? service.deleteTodo(id)
				? new ResponseEntity<>("Deleted Successfully!", HttpStatus.OK)
				: new ResponseEntity<>("Not Deleted Successfully!", HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
}
