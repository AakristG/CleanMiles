import { Card, FeaturedCard } from "@/components/cards";
import Search from "@/components/search";
import icons from "@/constants/icons";
import images from "@/constants/images";
import { useGlobalContext } from "@/lib/global-provider";
import { Link } from "expo-router";
import { Text, View, Image, TouchableOpacity } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export default function Index() {
  const {user, refetch } = useGlobalContext();
  
  return (
    <SafeAreaView className="bg-white h-full">
      <View className="px-5">
        <View className="flex flex-row items-center justify-between mt-5">
          <View className="flex flex-row items-center">
            <Image source={{uri: user?.avatar}} className="size-12 rounded-full"/>
            <View className="flex flex-col items-start ml-2 justify-center">
              <Text className="text-xs font-rubik text-grey"> Good Morning </Text>
              <Text className="text-base font-rubik-medium text-black"> {user?.name}</Text>
            </View>
          </View>
          <Image source={icons.bell} className="size-6" />
        </View>
        <Search />
        <View className="my-5">
          <View className="flex flex-row items-center justify-between">
            <Text className="text-xl font-rubik-bold text-black">Featured</Text>
            <TouchableOpacity>
              <Text className="text-base font-rubik-bold text-brown"> See All </Text>
            </TouchableOpacity>
          </View>
          
          <View className="flex flex-row gap-5 mt-5">
            <FeaturedCard />
            <FeaturedCard />
          </View>
        
        </View>

        <View className="flex flex-row items-center justify-between">
            <Text className="text-xl font-rubik-bold text-black">Our Recommendation</Text>
            <TouchableOpacity>
              <Text className="text-base font-rubik-bold text-brown"> See All </Text>
            </TouchableOpacity>
        </View>

        <View className="flex flex-row gap-5 mt-5">
            <Card />
            <Card />
        </View>
      </View>
    </SafeAreaView>
  );
}
