import React, { useState, useEffect } from 'react';
import {
  View,
  Image,
  StyleSheet,
  Text,
} from 'react-native';

export default function App() {
  // Estado para controlar el Splash
  const [isLoading, setIsLoading] = useState(true);

  // Espera 3 segundos
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  // Splash Screen
  if (isLoading) {
    return (
      <View style={styles.container}>
        <Image
          source={require('./assets/splash-icon.png')}
          style={styles.image}
          resizeMode="cover"
        />
      </View>
    );
  }

  // Pantalla principal
  return (
    <View style={styles.mainContainer}>
      <Text style={styles.title}>¡Bienvenido a GaiaLink!</Text>
      <Text style={styles.subtitle}>
        Aquí irá el contenido principal de la aplicación.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  // Splash
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },

  image: {
    width: '100%',
    height: '100%',
  },

  // Pantalla principal
  mainContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
    paddingHorizontal: 20,
  },

  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#1B5E20',
    marginBottom: 10,
  },

  subtitle: {
    fontSize: 17,
    color: '#666',
    textAlign: 'center',
  },
});