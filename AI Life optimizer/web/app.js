const state = {
  userId: null,
  userEmail: null,
  userName: null,
};

function setStatus(element, message) {
  element.textContent = message;
}

function setError(element, message) {
  setStatus(element, `Error: ${message}`);
}

async function createOrLoadUser(email, fullName) {
  const payload = { email, full_name: fullName };
  const resp = await fetch('/api/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(err.detail || resp.statusText);
  }

  return resp.json();
}

async function submitMetric(userId, key, value) {
  const payload = {
    metric_key: key,
    metric_value: parseFloat(value),
    recorded_at: new Date().toISOString(),
  };

  const resp = await fetch(`/api/users/${userId}/metrics`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return resp.json();
}

async function fetchRecommendations(userId) {
  const resp = await fetch(`/api/users/${userId}/recommendations`);
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(err.detail || resp.statusText);
  }
  return resp.json();
}

function setDisabled(element, disabled) {
  if (disabled) {
    element.classList.add('disabled');
    element.disabled = true;
  } else {
    element.classList.remove('disabled');
    element.disabled = false;
  }
}

function updateUIForUser(user) {
  state.userId = user.id;
  state.userEmail = user.email;
  state.userName = user.full_name;

  const userInfo = document.getElementById('userInfo');
  userInfo.textContent = `Loaded user ${user.full_name || user.email} (id: ${user.id})`;

  const metricForm = document.getElementById('metricForm');
  setDisabled(metricForm, false);

  const refreshBtn = document.getElementById('refreshRecommendations');
  setDisabled(refreshBtn, false);
}

async function handleUserForm(event) {
  event.preventDefault();

  const email = document.getElementById('userEmail').value.trim();
  const name = document.getElementById('userName').value.trim();
  const status = document.getElementById('userInfo');

  if (!email) {
    setError(status, 'Email is required');
    return;
  }

  setStatus(status, 'Loading user...');
  try {
    const user = await createOrLoadUser(email, name);
    updateUIForUser(user);
  } catch (error) {
    setError(status, error.message);
  }
}

async function handleMetricForm(event) {
  event.preventDefault();

  const status = document.getElementById('metricStatus');
  const key = document.getElementById('metricKey').value.trim();
  const value = document.getElementById('metricValue').value;

  if (!state.userId) {
    setError(status, 'No user selected');
    return;
  }

  setStatus(status, 'Submitting metric...');

  try {
    await submitMetric(state.userId, key, value);
    setStatus(status, 'Metric submitted successfully.');
    await refreshRecommendations();
  } catch (error) {
    setError(status, error.message);
  }
}

async function refreshRecommendations() {
  const recContainer = document.getElementById('recommendations');
  const refreshButton = document.getElementById('refreshRecommendations');

  if (!state.userId) {
    setStatus(recContainer, 'Create or load a user to see recommendations.');
    return;
  }

  setStatus(recContainer, 'Loading recommendations...');
  setDisabled(refreshButton, true);

  try {
    const data = await fetchRecommendations(state.userId);
    setStatus(recContainer, JSON.stringify(data, null, 2));
  } catch (error) {
    setError(recContainer, error.message);
  } finally {
    setDisabled(refreshButton, false);
  }
}

function init() {
  document.getElementById('userForm').addEventListener('submit', handleUserForm);
  document.getElementById('metricForm').addEventListener('submit', handleMetricForm);
  document.getElementById('refreshRecommendations').addEventListener('click', refreshRecommendations);
}

window.addEventListener('DOMContentLoaded', init);
