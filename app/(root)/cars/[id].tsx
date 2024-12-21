import {View, Text} from 'react-native'
import React from 'react'
import { useLocalSearchParams } from 'expo-router'

const Car = () => {
  const { id } = useLocalSearchParams();

  return(
    <View>
      <Text>Car {id} </Text>
    </View>
  )
}
  
export default Car;