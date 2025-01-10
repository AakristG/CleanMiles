import {Text, TouchableOpacity, ScrollView} from 'react-native'
import React, {useState} from 'react'
import images from '@/constants/images';
import icons from '@/constants/icons';
import { router, useLocalSearchParams } from 'expo-router';
import { categories } from '@/constants/data';

export const Filters = () => {

  const params = useLocalSearchParams<{filter?: string}>();
  const [selectedCategory, setSelectedCategory] = useState(params.filter || 'All');

  const handleCategoryPress = (category: string) => {
    if (selectedCategory === category) {
        setSelectedCategory('All');
        router.setParams({filters: 'All'});
        return;
    }

    setSelectedCategory(category);
    router.setParams({filter: category})
  }

  return (
    <ScrollView horizontal showsHorizontalScrollIndicator={false} className="mt-3 mb-2">
      {categories.map((item, index) => (
        <TouchableOpacity onPress={() => handleCategoryPress(item.category)} className={`flex flex-col items-start mr-4 px-4 py-2 rounded-full ${selectedCategory === item.category ? 'bg-green' : 'bg-white border border-yellow'}`}>
          <Text className={`text-sm ${selectedCategory === item.category ? 'text-white font-rubik-bold mt-0.5' : 'text-black'}`}>{item.title}</Text>
        </TouchableOpacity>
      ) )}
    </ScrollView>
  )
}

export default Filters