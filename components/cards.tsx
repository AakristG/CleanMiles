import {View, Text, Image, TextInput, TouchableOpacity, Touchable} from 'react-native'
import React, {useState} from 'react'
import images from '@/constants/images';
import icons from '@/constants/icons';

interface Props {
  onPress: () => void;
}

//Use A.I. here to add featured car first
export const FeaturedCard = ({onPress}: Props) => {
  return (
    <TouchableOpacity onPress={onPress} className="flex flex-col items-start w-60 h-80 relative">
      <Image source={images.japan} className="size-full rounded-2xl"/>
      <Image source={images.cardGradient} className="size-full rounded-2xl absolute bottom-0"/>

      <View className="flex flex-row items-center bg-white/90 px-3 py-1.5 rounded-full absolute top-5 right-5">
        <Image source={icons.star} className="size-3.5" />
        <Text className="text-cs font-rubik-bold text-yellow ml-1">4.4</Text> {/* Make the rating be done with A.I. */}
      </View>

      <View className="flex flex-col items-start absolute bottom-5 inset-x-5">
        <Text className="text-xl font-rubik-extrabold text-white" numberOfLines={1}>2024 Rav4</Text>
        <Text className="text-base font-rubik text-white"> 
          Toyota
        </Text>

        <View className="flex flex-row items-center justify-between w-full">
          <Text className="text-xl font-rubik-extrabold text-white">
            $12,500
          </Text>
          <Image source={icons.heart} className="size-5"/>
        </View>
      </View>
    </TouchableOpacity>
  )
}

export const Card = () => {
  return (
    <View>
      <Text>Just Card</Text>
    </View>
  )
}