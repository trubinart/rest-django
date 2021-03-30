import React from 'react';
import './App.css';
import {UserList, UserList2} from './components/Users.js'
import ProjectsList from './components/Projects.js'
import TodoList from './components/Todo2'
import NotFound404 from './components/404'
import LoginForm from './components/Auth.js'
import axios from 'axios'
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'
import Cookies from 'universal-cookie';

class App extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

   load_data() {
        const headers = this.get_headers()
         axios.get('http://127.0.0.1:8000/api/users/', {headers})
       .then(response => {
           console.log(response)
           const users = response.data
               this.setState(
               {
                   'users': users.results
               }
           )
       }).catch(error => {
           console.log(error)
            this.setState({'users': ''})
       })

    axios.get('http://127.0.0.1:8000/api/projects/', {headers})
       .then(response => {
           const projects = response.data
               this.setState(
               {
                   'projects': projects.results
               }
           )
       }).catch(error => {
           console.log(error)
            this.setState({'projects': ''})
       })

    axios.get('http://127.0.0.1:8000/api/todo/', {headers})
       .then(response => {
           const todo = response.data
               this.setState(
               {
                   'todo': todo.results
               }
           )
       }).catch(error => {
            this.setState({'todo': ''})
       })
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token}, ()=>this.load_data())
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
  if (this.is_authenticated())
    {
        headers['Authorization'] = 'Token ' + this.state.token
    }
  console.log('get_headers ' + headers['Authorization'])
  return headers
  }

   componentDidMount() {
        this.get_token_from_storage()
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
                        <li>
                            {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                    </ul>
                </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <TodoList todo={this.state.todo} />} />
                        <Route path='/users/:id' component={() => <UserList2 users={this.state.users} />}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
           </div>
       )
   }
}

export default App;