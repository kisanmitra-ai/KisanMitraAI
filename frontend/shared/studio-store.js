window.KisanMitraStudioStore = {
  key: "KISANMITRA_STUDIO_STATE",
  get() {
    try { return JSON.parse(localStorage.getItem(this.key)) || {}; }
    catch { return {}; }
  },
  set(nextState) {
    const current = this.get();
    const merged = { ...current, ...nextState, updatedAt: new Date().toISOString() };
    localStorage.setItem(this.key, JSON.stringify(merged));
    return merged;
  }
};
