// Web Worker to compute digits of π using a spigot/BBP-like algorithm.
// The worker streams digits back to the main thread so the UI can stay responsive.

self.onmessage = (event) => {
  const { type, digits, chunk } = event.data;
  if (type === "start") {
    computePi(digits, chunk || 1000);
  }
};

function computePi(n, chunkSize) {
  // Use BigInt for precision.
  // This implementation emits digits in base 10^4 to reduce loop count.
  const target = BigInt(n);
  const BASE = 10000n;
  const BASE_DIGITS = 4;

  let q = 1n;
  let r = 0n;
  let t = 1n;
  let k = 1n;
  let nDigit = 3n;
  let l = 3n;

  let produced = 0n;
  const buffer = [];

  // Send an initial message to indicate computation started.
  postMessage({ type: "started", digits: n });

  while (produced < target) {
    if (4n * q + r - t < nDigit * t) {
      // Digit output in blocks (base 10^4) for faster calculation.
      const digitStr = produced === 0n
        ? nDigit.toString()
        : nDigit.toString().padStart(BASE_DIGITS, "0");

      // Cut the last block if it would exceed requested digits.
      const remaining = target - produced;
      const append = remaining < BigInt(digitStr.length)
        ? digitStr.slice(0, Number(remaining))
        : digitStr;

      buffer.push(append);
      produced += BigInt(append.length);

      const qNew = q * BASE;
      const rNew = BASE * (r - nDigit * t);
      const nNew = (BASE * (3n * q + r)) / t - BASE * nDigit;

      q = qNew;
      r = rNew;
      nDigit = nNew;
    } else {
      const qNew = q * k;
      const rNew = (2n * q + r) * l;
      const tNew = t * l;
      const nNew = (q * (7n * k + 2n) + r * l) / (t * l);

      q = qNew;
      r = rNew;
      t = tNew;
      k += 1n;
      nDigit = nNew;
      l += 2n;
    }

    if (buffer.length >= chunkSize || produced >= target) {
      const sent = Number(produced > target ? target : produced);
      postMessage({ type: "chunk", digits: buffer.join(""), produced: sent });
      buffer.length = 0;
    }
  }

  postMessage({ type: "done" });
}
