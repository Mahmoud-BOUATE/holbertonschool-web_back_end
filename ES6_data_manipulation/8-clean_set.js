export default function cleanSet(set, startString) {
  if (startString === "") return "";

  let result = "";

  for (const a of set) {
    if (a.startsWith(startString)) {
      const slice = a.slice(startString.length);

      if (slice !== "") {
        if (result === "") {
          result = slice;
        } else {
          result += "-" + slice;
        }
      }
    }
  }

  return result;
}
