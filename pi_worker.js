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
  let q = 1n;
  let r = 0n;
  let t = 1n;
  let k = 1n;
  let nDigit = 3n;
  let l = 3n;

  let produced = 0;
  let buffer = "";

  // Send an initial message to indicate computation started.
  postMessage({ type: "started", digits: n });

  while (produced < n) {
    if (4n * q + r - t < nDigit * t) {
      buffer += nDigit.toString();

      const qNew = q * 10n;
      const rNew = 10n * (r - nDigit * t);
      const nNew = (10n * (3n * q + r)) / t - 10n * nDigit;

      q = qNew;
      r = rNew;
      nDigit = nNew;

      produced += 1;
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

    if (buffer.length >= chunkSize || produced >= n) {
      postMessage({ type: "chunk", digits: buffer });
      buffer = "";
    }
  }

  postMessage({ type: "done" });
}
