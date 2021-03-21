import React from 'react';
import './App.css';
import {UserList, UserList2} from './components/Users.js'
import ProjectsList from './components/Projects.js'
import TodoList from './components/Todo2'
import NotFound404 from './components/404'
import axios from 'axios'
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'

class App extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

   async componentDidMount() {

   await axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users.results
               }
           )
       }).catch(error => console.log(error))

   await axios.get('http://127.0.0.1:8000/api/projects/')
       .then(response => {
           const projects = response.data
               this.setState(
               {
                   'projects': projects.results
               }
           )
       }).catch(error => console.log(error))

   await axios.get('http://127.0.0.1:8000/api/todo/')
       .then(response => {
           const todo = response.data
               this.setState(
               {
                   'todo': todo.results
               }
           )
       }).catch(error => console.log(error))

   }

   render () {
       return (
           <div className="App">
                <BrowserRouter>
                   <nav>
                    <ul>
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todo'>Todo</Link>
                        </li>
                    </ul>
                </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <TodoList todo={this.state.todo} />} />
                        <Route path='/users/:id' component={() => <UserList2 users={this.state.users} />}/>
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
           </div>
       )
   }
}

export default App;