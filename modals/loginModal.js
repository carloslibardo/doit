import React, { Component } from 'react';
import { View, Modal, TextInput } from 'react-native';
import { Button, Text } from 'react-native-elements';
import { connect } from 'react-redux';
import { closeLoginModal } from '../actions';
import { SCREEN_HEIGHT, SCREEN_WIDTH } from '../constants';

class LoginModal extends Component {
    constructor(props){
      super(props);
      this.state = {
        username: '',
        password: ''
      }
    }

    requestLogin() {
      let input_username = this.state.username;
      let input_password = this.state.password;
      let input_unique_id = 'admin';
      fetch('http://192.168.15.7:5000/app/login', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: input_username,
          password: input_password,
          unique_id: input_unique_id,
        }),
      }).then((response) => response.json());
    }

    render() {
        const {
            modalStyle,
            containerStyle,
            buttonContainerStyle
        } = styles;

        return (
            <Modal
                transparent
                animationType={'slide'}
                visible={this.props.modal.loginModalIsOpen}
                onRequestClose={() => this.props.closeLoginModal()}
            >
                <View style={modalStyle}>
                    <View style={containerStyle}>
                        <View style={buttonContainerStyle}>
                            <Button
                                raised
                                title="Close"
                                backgroundColor="#2196F3"
                                onPress={() => this.props.closeLoginModal()}
                            />
                        </View>

                        <Text style={styles.boxTitle}>Faça seu login</Text>
                        <TextInput
                            ref={(el) => {this.username = el; }}
                            onChangeText={(username) => this.setState(state => ({username}))}
                            value={this.state.username}
                            autoFocus
                            autoCapitalize="none"
                            style={styles.boxInput}
                            placeholder="Digite seu usuário"
                        >
                        </TextInput>
                        <TextInput
                            ref={(el) => {this.password = el; }}
                            onChangeText={(password) => this.setState(state => ({password}))}
                            value={this.state.password}
                            autoCapitalize="none"
                            style={styles.boxInput}
                            placeholder="Digite sua senha"
                        >
                        </TextInput>
                        <Button
                            raised
                            title="Entrar"
                            backgroundColor="#2196F3"
                            onPress={() => this.requestLogin()}
                        />
                    </View>
                </View>
            </Modal>
        );
    }
}

const marginPerc = 0.05;

const styles = {
    modalStyle: {
        flex: 1,
        backgroundColor: 'rgba(0, 0, 0, 0.5)'
    },
    containerStyle: {
        flex: 1,
        marginTop: SCREEN_HEIGHT * marginPerc,
        marginBottom: SCREEN_HEIGHT * marginPerc,
        marginLeft: SCREEN_WIDTH * marginPerc,
        marginRight: SCREEN_WIDTH * marginPerc,
        backgroundColor: 'white'
    },
    buttonContainerStyle: {
        paddingBottom: 10
    },
    boxTitle: {
        fontWeight: 'bold',
        fontSize: 16,
    },
    boxInput: {
        alignSelf: 'stretch',
        marginTop: 10,
        paddingVertical: 0,
        paddingHorizontal: 20,
        borderWidth: 1,
        borderColor: '#DDD',
        height: 40,
        borderRadius: 3
    },
};

const mapStateToProps = ({ modal }) => ({ modal });

export default connect(mapStateToProps, { closeLoginModal })(LoginModal);
