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
import ProjectForm from './components/ProjectForm'

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
        this.setState({'token': token}, () => this.load_data())
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
        this.setState({'token': token}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        console.log('get_headers ' + headers['Authorization'])
        return headers
    }

    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers, headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((item) => item.id !== id)})
            }).catch(error => console.log(error))
    }

    deleteTodo(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers, headers})
            .then(response => {
                this.setState({todo: this.state.todo.filter((item) => item.id !== id)})
            }).catch(error => console.log(error))
    }

    createProject(name, text, users) {
        const headers = this.get_headers()
        const data = {name: name, text: text, users: users}
        axios.post(`http://127.0.0.1:8000/api/projects/`, data, {headers, headers})
            .then(response => {
                let new_project = response.data
                const project = this.state.projects.filter((item) => item.id === new_project.project)[0]
                new_project.project = project
                this.setState({projects: [...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }


    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
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
                                <Link to='/project/create'>Create project</Link>
                            </li>
                            <li>
                                <Link to='/todo'>Todo</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>

                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects}
                                                                                     deleteProject={(id) => this.deleteProject(id)}/>}/>
                        <Route exact path='/todo' component={() => <TodoList todo={this.state.todo}
                                                                             deleteTodo={(id) => this.deleteTodo(id)}/>}/>
                        <Route path='/users/:id' component={() => <UserList2 users={this.state.users}/>}/>
                        <Route exact path='/project/create' component={() => <ProjectForm users={this.state.users}
                                                                                          createProject={(name, text, users) => this.createProject(name, text, users)}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route component={NotFound404}/>

                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;