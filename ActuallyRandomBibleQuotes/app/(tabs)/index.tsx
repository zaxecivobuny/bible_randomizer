import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { useState, useEffect } from 'react';

const rawQuotes = require('../../assets/quotes.txt');
console.log('rawQuotes value:', rawQuotes);

export default function HomeScreen() {
  const [reference, setReference] = useState('');
  const [quoteText, setQuoteText] = useState('Loading...');
  const [lines, setLines] = useState<string[]>([]);

  useEffect(() => {
    loadQuotes();
  }, []);

  const loadQuotes = async () => {
    const response = await fetch(rawQuotes);
    const text = await response.text();
    const parsed = text
      .split('\n')
      .slice(2)
      .filter((line: string) => line.trim() !== '');
    setLines(parsed);
    pickRandom(parsed);
  };

  const pickRandom = (arr: string[]) => {
    const pool = arr.length > 0 ? arr : lines;
    const randomLine = pool[Math.floor(Math.random() * pool.length)];
    const [ref, ...rest] = randomLine.split('\t');
    setReference(ref.trim());
    setQuoteText(rest.join('\t').trim());
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Actually Random Bible Quotes</Text>
      <View style={styles.quoteBox}>
        <Text style={styles.quote}>{quoteText}</Text>
        <Text style={styles.reference}>— {reference}</Text>
      </View>
      <TouchableOpacity style={styles.button} onPress={() => pickRandom([])}>
        <Text style={styles.buttonText}>New Quote</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#e0c97f',
    marginBottom: 40,
    textAlign: 'center',
  },
  quoteBox: {
    backgroundColor: '#16213e',
    borderRadius: 12,
    padding: 24,
    marginBottom: 40,
    borderLeftWidth: 4,
    borderLeftColor: '#e0c97f',
  },
  quote: {
    fontSize: 18,
    color: '#ffffff',
    lineHeight: 28,
    textAlign: 'center',
    marginBottom: 16,
  },
  reference: {
    fontSize: 14,
    color: '#e0c97f',
    textAlign: 'right',
    fontStyle: 'italic',
  },
  button: {
    backgroundColor: '#e0c97f',
    paddingVertical: 14,
    paddingHorizontal: 40,
    borderRadius: 30,
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1a1a2e',
  },
});