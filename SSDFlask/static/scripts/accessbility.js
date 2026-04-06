function toggleAxSidebar() {
    const panel = document.getElementById('ax-sidebar-panel');
    if (panel) panel.classList.toggle('ax-active');
}

function toggleContrast() {
    document.body.classList.remove('dark-mode');
    const isActive = document.body.classList.toggle('high-contrast');
    localStorage.setItem('high-contrast', isActive);
    localStorage.setItem('dark-mode', false);
    updateAxUI();
}

function toggleDarkMode() {
    document.body.classList.remove('high-contrast');
    const isActive = document.body.classList.toggle('dark-mode');
    localStorage.setItem('dark-mode', isActive);
    localStorage.setItem('high-contrast', false);
    updateAxUI();
}

function adjustFontSize(val) {
    document.getElementById('size-value').innerText = val + "%";
    document.body.style.fontSize = val + "%";
    localStorage.setItem('font-size', val);
}

function updateAxUI() {
    const cBtn = document.getElementById('contrast-btn');
    const dBtn = document.getElementById('dark-btn');
    if (cBtn) cBtn.setAttribute('aria-pressed', document.body.classList.contains('high-contrast'));
    if (dBtn) dBtn.setAttribute('aria-pressed', document.body.classList.contains('dark-mode'));
}

function loadSettings() {
    if (localStorage.getItem('high-contrast') === 'true') document.body.classList.add('high-contrast');
    if (localStorage.getItem('dark-mode') === 'true') document.body.classList.add('dark-mode');
    const sz = localStorage.getItem('font-size') || "100";
    adjustFontSize(sz);
    if (document.getElementById('font-slider')) document.getElementById('font-slider').value = sz;
    updateAxUI();
}

window.addEventListener('DOMContentLoaded', loadSettings);

function resetSettings() {
    localStorage.clear();
    window.location.reload();
}