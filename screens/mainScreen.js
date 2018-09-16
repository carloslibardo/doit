import React, { Component } from 'react';
import { View, Platform, Image } from 'react-native';
import Expo from 'expo';
import icon from '../assets/icons/pure-icon.png'
import { STATUS_BAR_HEIGHT } from '../constants';
import Slider from '../components/slider';
import LoginFooter from '../components/loginFooter';

const cacheImages = images => images.map(image => {
    if (typeof image === 'string') {
        return Image.prefetch(image);
    }
    return Expo.Asset.fromModule(image).downloadAsync();
});

class MainScreen extends Component {
    static navigationOptions = () => ({
        title: 'Login',
        headerStyle: {
            height: Platform.OS === 'android' ? 54 + STATUS_BAR_HEIGHT : 54,
            backgroundColor: '#2196F3'
        },
        headerTitleStyle: {

            color: 'white'
        },
        headerLeft: (
            <Image
                source={icon}
                style={styles.image}
            >
            </Image>)
    });

    state = {
        AppIsReady: false
    }

    componentWillMount(){
        this._loadAssetsAsync();
    }

    async _loadAssetsAsync() {
        const imageAssets = cacheImages([icon]);
        await Promise.all([...imageAssets]);
        this.setState({AppIsReady: true});
    }
    render() {
        return (

                <View style={{ flex: 1, backgroundColor: '#ddd' }}>
                    <Slider></Slider>
                    <LoginFooter></LoginFooter>
                </View>
                
                
        )
    }
}

const styles = {
    image: {
        marginTop: 7,
        marginLeft: 10,
        width: 40,
        height: 40
    }
}

export default MainScreen;