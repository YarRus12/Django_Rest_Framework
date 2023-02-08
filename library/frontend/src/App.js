import React from 'react';
import './App.css';
import axios from 'axios'
import ProjectList from './components/Project.js'
import UserProjectList from './components/UserProject.js'
import UserList from './components/User.js'
import ToDoList from './components/ToDo.js'
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie'

const NotFound404 = ({ location }) => {
    return(
    <div>
        <h1>Страницы по адресу `{location.pathname}` отсутствует</h1>
    </div>
)}


class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'projects': [],
            'users ': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated(){
        return this.state.token != ''
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8005/api-token-auth/', {username: login, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        })
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json',
        }
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
    const headers = this.get_headers()
        axios.get('http://127.0.0.1:8005/api/users', {headers}) // Вот тут я долго тупил, путь должен быть на api в джанго
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users['results']
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8005/api/projects', {headers}) // Вот тут я долго тупил, путь должен быть на api в джанго
            .then(response => {
                const projects = response.data
                    this.setState(
                    {
                        'projects': projects['results']
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
        }

    render () {
        return (
            <div className='Application'>
                <HashRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/tasks'>ToDo</Link>
                        </li>
                        <li>
                            {this.is_authenticated()? <button onClick={()=> this.logout()}>Logout</button>: <Link to='/login'>login</Link>}
                        </li>
                    </ul>
                </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList items={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects_all}/>}/>
                        <Route exact path='/tasks' component={() => <ToDoList items={this.state.tasks_all}/>}/>
                        <Route exact path='/projects/:name' component={() => <UserProjectList items={this.state.projects}/>}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)}/> }/>
                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;