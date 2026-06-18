window.KisanMitraStudioBridge = {
  brand: window.KISANMITRA_BRAND,
  modules: window.KISANMITRA_MODULES,
  store: window.KisanMitraStudioStore,

  getModules(target) {
    return this.modules.filter(m => m[target] === true);
  },

  renderModuleCards(containerId, target) {
    const el = document.getElementById(containerId);
    if (!el) return;

    el.innerHTML = this.getModules(target).map(m => `
      <div class="km-module-card">
        <div class="km-module-top">
          <strong>${m.name}</strong>
          <span class="km-status ${m.status}">${m.status}</span>
        </div>
        <p>${m.description}</p>
        <small>Source: ${m.dataSource}</small>
      </div>
    `).join("");
  }
};
