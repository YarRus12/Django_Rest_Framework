import React from 'react';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8005/authors/authors') // Вот тут я долго тупил, путь должен быть на api в джанго
        .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
        }

    render () {
        return (
            <div>
                <AuthorList authors={this.state.authors} />
            </div>
        )
    }
}

export default App;