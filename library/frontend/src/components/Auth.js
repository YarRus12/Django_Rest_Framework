import React from 'react'

class LoginForm extends React.Component{
    constructor(props) {
    super(props);
    this.state = {login: '', password: ''}
    }

    handleChange(event) {
        this.setState(
        {
            [event.target.name]: event.target.value
        }
        )
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
        <form onSubmit={(event) => this.handleSubmit(event)}>
            <input type="text" name="login" placeholder="login" value={this.state.login}
                    on Change={(event) => this.handleChange(event)}/>
            <input type="password" name="password" placeholder="password" value={this.state.password}
                    on Change={(event) => this.handleChange(event)}/>
            <input type="sub,it" value="Login"/>
        </form>
        )
    }
}

export default LoginForm
