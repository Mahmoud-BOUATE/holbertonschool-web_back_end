export default function hasValuesFromArray(set, array) {
  for (const nbr of array) {
    if (!set.has(nbr)) {
      return false;
    }
  }
  return true;
}
