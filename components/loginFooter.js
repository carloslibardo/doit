import React, { Component } from 'react';
import {
    View,
    Text,
    TouchableOpacity,
    StyleSheet,
} from 'react-native';

import {connect} from 'react-redux';

 class LoginFooter extends Component {
    render() {
        return (
            <View style={styles.loginContainer}>
                    <View style={styles.buttonContainer}>
                        <TouchableOpacity
                            activeOpacity={0.8}
                            style={[styles.button, styles.registerButton]}
                            onPress={() => { }}
                        >
                            <Text style={styles.buttonText}>Registrar</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            activeOpacity={0.8}
                            style={[styles.button, styles.loginButton]}
                            onPress={() => {this.props.enableModal()}}
                        >
                            <Text style={styles.buttonText}>Entrar</Text>
                        </TouchableOpacity>
                    </View>
            </View>
        )
    }
}

function mapStateToProps(state){
    return {
        modalVisible: state.modalVisible
    }
}

function mapDispatchToProps(dispatch){
    enableModal : () => dispatch({type: 'ENABLE_MODAL'});
}

export default connect(mapStateToProps)(LoginFooter)

const styles = StyleSheet.create({ 
    loginContainer: {
        backgroundColor: '#FFFFFF',
        width: 360,
        height: 170,
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonContainer: {
        marginTop: 10,
        height: 85,
        flexDirection: 'row',
        paddingHorizontal: 20
    },
    button: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: 1,
    },
    registerButton: {
        backgroundColor: '#696969',
        marginRight: 10,
    },
    loginButton: {
        backgroundColor: '#70BD85',
        marginLeft: 10,
    },
    buttonText: {
        fontWeight: 'bold',
        color: "#FFF",
        fontSize: 25,
    }

})