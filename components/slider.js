import React, { Component } from 'react'
import {
    Text,
    View,
    Image,
} from 'react-native'

import Swiper from 'react-native-swiper'
import { WINDOW_WIDTH } from '../constants';

const Slider = props => (<View style={styles.container}>
    <Image style={styles.image} source={props.uri} />
    <Text style={styles.text}>{props.content}</Text>
</View>
)

const styles = {
    container: {
        flex: 1,
        justifyContent: 'center'
    },
    image: {
        flex: 1,
        width: WINDOW_WIDTH
    },
    text:{
        backgroundColor: '#FFFFFF',
        textAlign: 'center',
        fontSize: 20
    }
}

export default class extends Component {
    constructor(props) {
        super(props)

        this.state = {
            imagesSlider: [
                require('../assets/sliderImages/image1.jpg'),
                require('../assets/sliderImages/image2.jpg'),
                require('../assets/sliderImages/image3.jpg')
            ]
        }
    }
    render() {
        return (
            <View style={{ flex: 1 }}>
                <Swiper
                    height={240}
                >
                    {
                        this.state.imagesSlider.map((image, index) => 
                            <Slider
                                uri={image}
                                key={index}
                                content={index}
                            >
                            </Slider>
                        )
                    }
                </Swiper>
            </View>
        )
    }
}