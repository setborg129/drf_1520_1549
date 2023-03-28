import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import TodoList from "./components/Todo.js";
import ProjectTodoList from "./components/ProjectTodo"
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation}
    from 'react-router-dom'
import Menu from "./components/Menu";



const PageNotFound = () => {
  let {pathname} = useLocation()

  return (
      <div>
          Page "{pathname}" not found!
      </div>
  )
}

class App extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
          'users': [],
          'projects': [],
          'TODO': [],
      }
  }

  componentDidMount() {
      axios
          .get('http://localhost:8000/api_users/')
          .then(response => {

              const users = response.data
              this.setState(
                  {
                    'users': users
                    }
            )
          })
          .catch(error => console.log(error))

      axios
          .get('http://localhost:8000/api_Project/')
          .then(response => {
              const projects = response.data
              this.setState(
                  {
                    'Project': projects
                    }
            )
          })
          .catch(error => console.log(error))

      axios
          .get('http://localhost:8000/api_TODO/')
          .then(response => {
              const todos = response.data
              this.setState(
                  {
                    'TODO': todos
                    }
            )
          })
          .catch(error => console.log(error))
  }

    render() {
      return (
          <div className="sub_body">
              <div className="top App_header">
                <hr></hr>
                  <BrowserRouter>
                      <nav>
                          <li> <Link to='/'>Project list</Link> </li>
                          <li> <Link to='/TODO'>TODO list</Link> </li>
                          <li> <Link to='/users'>User list</Link> </li>
                      </nav>

                    <Routes>
                      <Route exact path='/' element={<Navigate to='/projects' />} />
                      <Route exact path='/users' element={<UserList users={this.state.users} />} />
                      <Route exact path='/TODO' element={<TodoList todos={this.state.todos} />} />
                      <Route path='/projects'>
                        <Route index element={<ProjectList projects={this.state.projects} />} />
                        <Route path=':projectId' element={<ProjectTodoList todos={this.state.todos} />} />
                      </Route>
                      <Route path='*' element={<PageNotFound />} />
                    </Routes>
                  </BrowserRouter>
              </div>
          </div>
      );
  }
}

export default App;
