import {View, Text, Image, TextInput, TouchableOpacity, Touchable} from 'react-native'
import React, {useState} from 'react'
import images from '@/constants/images';
import icons from '@/constants/icons';

interface Props {
  onPress?: () => void;
}

//Use A.I. here to add featured car first
export const FeaturedCard = ({onPress}: Props) => {
  return (
    <TouchableOpacity onPress={onPress} className="flex flex-col items-start w-60 h-80 relative">
      <Image source={images.ToyotaSuv} className="size-full rounded-2xl"/>
      <Image source={images.cardGradient} className="size-full rounded-2xl absolute bottom-0"/>

      <View className="flex flex-row items-center bg-white/90 px-3 py-1.5 rounded-full absolute top-5 right-5">
        <Image source={icons.star} className="size-3.5" />
        <Text className="text-cs font-rubik-bold text-yellow ml-1">4.4</Text> {/* Make the rating be done with A.I. */}
      </View>

      <View className="flex flex-col items-start absolute bottom-5 inset-x-5">
        <Text className="text-xl font-rubik-extrabold text-white" numberOfLines={1}>2024 Rav4</Text>
        <Text className="text-base font-rubik text-white">Toyota</Text>

        <View className="flex flex-row items-center justify-between w-full">
          <Text className="text-xl font-rubik-extrabold text-white">$12,500</Text>
          <Image source={icons.heart} className="size-5"/>
        </View> 
      </View>
    </TouchableOpacity>
  )
}

export const Card = ({ onPress }: Props) => {
  return (
    <TouchableOpacity onPress={onPress} className="flex-1 w-full mt-4 px-3 py-4 rounded-lg bg-white shadow-lg shadow-grey/70 relative">
       <View className="flex flex-row items-center absolute px-2 top-5 right-5 bg-white/90 p-1 rounded-full z-50">
        <Image source={icons.star} className="size-2.5" />
        <Text className="text-cs font-rubik-bold text-yellow ml-0.5">4.4</Text> {/* Make the rating be done with A.I. */}
      </View>

      <Image source={images.ToyotaSuvTwo} className="w-full h-40 rounded-lg" />

      <View className="flex flex-col mt-2">
        <Text className="text-base font-rubik-bold text-black" numberOfLines={1}>2015 Rav4</Text>
        <Text className="text-base font-rubik text-black">Toyota</Text>

        <View className="flex flex-row items-center justify-between mt-2">
          <Text className="text-base font-rubik-bold text-black">$12,500</Text>
          <Image source={icons.heart} className="w-5 h-5 mr-2" tintColor="#191d31"/>
        </View>
      </View>
    </TouchableOpacity>
  )
}