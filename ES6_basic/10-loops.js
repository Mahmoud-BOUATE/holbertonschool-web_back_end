export default function appendToEachArrayValue(array, appendString) {
  for (const idx in array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
