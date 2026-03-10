// Web Worker to compute digits of π using a spigot/BBP-like algorithm.
// The worker streams digits back to the main thread so the UI can stay responsive.

self.onmessage = (event) => {
  const { type, digits, chunk } = event.data;
  if (type === "start") {
    computePi(digits, chunk || 1000);
  }
};

function isqrt(n) {
  if (n < 0n) throw new Error("sqrt of negative");
  if (n < 2n) return n;
  let x = n;
  let y = (x + 1n) >> 1n;
  while (y < x) {
    x = y;
    y = (x + n / x) >> 1n;
  }
  return x;
}

function computePi(n, chunkSize) {
  // Chudnovsky algorithm (binary splitting) for high-performance pi computation.
  // Uses BigInt and streams progress updates (based on terms computed) while working.
  const target = BigInt(n);
  const DIGITS_PER_TERM = 14.181647462725477; // approx digits added per term
  const maxTerms = Math.ceil(n / DIGITS_PER_TERM) + 1;

  let termsComputed = 0;
  let lastProgressSent = 0;

  const C0 = 640320n;
  const C3 = C0 * C0 * C0;

  function postProgress() {
    const estimated = Math.min(n, Math.floor(termsComputed * DIGITS_PER_TERM));
    const delta = estimated - lastProgressSent;
    const minDelta = Math.max(1, Math.floor(n * 0.01));
    if (delta >= minDelta || estimated === n) {
      lastProgressSent = estimated;
      postMessage({ type: "progress", produced: estimated, total: n });
    }
  }

  function bs(a, b) {
    if (b - a === 1) {
      // Base case: single term.
      const k = BigInt(a);

      if (a === 0) {
        termsComputed += 1;
        postProgress();
        return {
          P: 1n,
          Q: 1n,
          T: 13591409n,
        };
      }

      const P = (6n * k - 5n) * (2n * k - 1n) * (6n * k - 1n);
      const Q = k * k * k * C3;
      const T = (13591409n + 545140134n * k) * (a % 2 === 0 ? 1n : -1n) * P;

      termsComputed += 1;
      postProgress();
      return { P, Q, T };
    }

    const m = Math.floor((a + b) / 2);
    const left = bs(a, m);
    const right = bs(m, b);

    return {
      P: left.P * right.P,
      Q: left.Q * right.Q,
      T: right.Q * left.T + left.P * right.T,
    };
  }

  // Send an initial message to indicate computation started.
  postMessage({ type: "started", digits: n });

  const { P, Q, T } = bs(0, maxTerms);

  // Constant: 426880 * sqrt(10005)
  const precision = BigInt(n + 10);
  const one = 10n ** (precision * 2n);
  const sqrtC = isqrt(10005n * one);
  const C = 426880n * sqrtC;

  const piScaled = (C * Q) / T;
  const piStr = piScaled.toString().padStart(n + 1, "0");

  // Stream the result back in chunks.
  let sent = 0;
  while (sent < piStr.length) {
    const chunk = piStr.slice(sent, sent + chunkSize);
    sent += chunk.length;
    postMessage({ type: "chunk", digits: chunk, produced: Math.min(Number(target), sent) });
  }

  postMessage({ type: "done" });
}

  postMessage({ type: "done" });
}
