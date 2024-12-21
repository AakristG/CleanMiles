import {View, Text, ScrollView, Image, TouchableOpacity} from 'react-native'
import React from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'

import images from '@/constants/images';
import icons from '@/constants/icons';

const SignIn = () => {
  const handleLogin = () => {

  };

  return(
    <SafeAreaView className="bg-white h-full">
      <ScrollView contentContainerClassName="h-full ">
        <Image source={images.signIn} className="w-full h-4/6 ml-2" resizeMode="contain" />
        <View className="px-10"> 
          <Text className="text-base text-center uppercase font-rubik"> 
            Welcome to CleanMiles
            </Text>
          <Text className="text-3xl font-rubik-bold text-center mt-2">
              Let's Get You To Drive {"\n"}   
              <Text className="text-green"> Eco Friendly </Text>Cars
          </Text>
          <Text className="text-lg font-rubik text-grey text-center mt-12">
            Login with CleanMiles with Google
          </Text>

          <TouchableOpacity onPress={handleLogin} className="bg-white shadow-md shadow-zinc-300 rounded-full w-full py-4 mt-5">
            <View className="flex flex-row items-center justify-center">
              <Image 
                source={icons.google}
                className="w-5 h-5"
                resizeMode="contain"
              />
              <Text className="text-lg font-rubik-medium text-black ml-2">
                Continue with Google
              </Text>
            </View>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  )
}

export default SignIn