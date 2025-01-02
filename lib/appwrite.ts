//Set up the appwrite client
import {Account, Avatars, Client, OAuthProvider} from "react-native-appwrite";
import * as Linking from 'expo-linking';
import {openAuthSessionAsync} from "expo-web-browser";

export const config = {
  platform: 'com.jsm.cleanmiles',
  endpoint: process.env.EXPO_PUBLIC_APPWRITE_ENDPOINT,
  projectId: process.env.EXPO_PUBLIC_APPWRITE_PROJECT_ID,
}

export const client = new Client();

client
      .setEndpoint(config.endpoint!)
      .setProject(config.projectId!)
      .setPlatform(config.platform!)

export const avatar = new Avatars(client);
export const account = new Account(client);


//login aspect
export async function login(){
  try{
    //handle deeplinks and redirect URLs
    const redirectUri = Linking.createURL('/');

    const response = await account.createOAuth2Token(OAuthProvider.Google, redirectUri);
    
    if(!response) throw new Error('Login Failed, Restart the Application ');

    //mobile brower within the app
    const browserResult = await openAuthSessionAsync(
      response.toString(),
      redirectUri
    );
    
    if(browserResult.type != 'success') throw new Error('Failed to login');

    const url = new URL(browserResult.url);

    const secret = url.searchParams.get('secret')?.toString();
    const userId = url.searchParams.get('userId')?.toString();

    if(!secret || !userId) throw new Error('Failed to login');

    const session = await account.createSession(userId, secret);

    if(!session) throw new Error('Failed to create a session');

    return session;

  } catch (error){
    console.error(error);
    return false;
  }
}

//logout aspect
export async function logout(){
  try{
      await account.deleteSession('current');
      return true;
  } catch(error) {
      console.error(error);
      return false;
  }
}

//user's profile 
export async function getCurrentUser() {
  try{
      const response = await account.get();

      if(response.$id){
          const  userAvatar = avatar.getInitials(response.name);
          return {
            ... response,
            avatar: userAvatar.toString(),
          }
      }
    return null;
  } catch(error) {
      console.log(error);
      return null;
  }

}