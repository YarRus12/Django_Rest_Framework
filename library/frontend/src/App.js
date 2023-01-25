import React from 'react';
import './App.css';
import axios from 'axios'
import ProjectList from './components/Project.js'
import UserProjectList from './components/UserProject.js'
import UserList from './components/User.js'
import ToDoList from './components/ToDo.js'
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

const NotFound404 = ({ location }) => {
    return(
    <div>
        <h1>Страницы по адресу `{location.pathname}` отсутствует</h1>
    </div>
)}


class App extends React.Component {

    constructor(props) {
        super(props)
        const user1 = {first_name: 'Alex', last_name: 'Pak', birthday_year: 1991}
        const user2 = {first_name: 'Valys', last_name: 'Vox', birthday_year: 1990}
        const users_all = [user1, user2]
        const project1 = {name: 'First', link: 'fioiugfghjkljhgf', description: 'First one!', users: user1}
        const project2 = {name: 'Second', link: 'fioiugfghjkljhgf', description: 'Second one!', users: users_all}
        const projects_all = [project1, project2]
        const task1 = {project: 'First', text: 'Завести задачу', create_at: '2022-01-01', update_at: '2022-01-02', user:'Alex', active:1}
        const task2 = {project: 'Second', text: 'Удалить проект', create_at: '2022-01-03', update_at: '2022-01-03', user:'Alex', active:0}
        const tasks_all = [task1, task2]

        this.state = {
            'projects': projects_all,
            'users': users_all
        }
    }

//    componentDidMount() {
//        axios.get('http://127.0.0.1:8005/authors/authors') // Вот тут я долго тупил, путь должен быть на api в джанго
//        .then(response => {
//                const authors = response.data
//                    this.setState(
//                    {
//                        'authors': authors
//                    }
//                )
//            }).catch(error => console.log(error))
//        }

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
                    </ul>
                </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects_all}/>}/>
                        <Route exact path='/tasks' component={() => <ToDoList tasks={this.state.tasks_all}/>}/>
                        <Route exact path='/projects/:name' component={() => <UserProjectList projects={this.state.projects}/>}/>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;