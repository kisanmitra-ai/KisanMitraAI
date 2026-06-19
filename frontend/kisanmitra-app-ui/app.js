const $ = (sel) => document.querySelector(sel);
let gpsPoint = null;

const langText = {
  English: {
    welcomeFarmer: "Welcome, Farmer!",
    started: "Let's get you started",
    fullName: "Full Name",
    mobile: "Mobile Number",
    language: "Language",
    locationTitle: "Share Your Location",
    locationHelp: "Allow access to your location so we can give you local weather, crop advice and nearby market prices.",
    gps: "Share GPS Location",
    safe: "Your location is safe with us and will never be shared.",
    continue: "Continue",
    saved: "Farmer saved. App language applied."
  },
  Hindi: {
    welcomeFarmer: "स्वागत है, किसान!",
    started: "चलिए शुरू करते हैं",
    fullName: "पूरा नाम",
    mobile: "मोबाइल नंबर",
    language: "भाषा",
    locationTitle: "अपना स्थान साझा करें",
    locationHelp: "स्थानीय मौसम, फसल सलाह और नजदीकी बाजार भाव के लिए GPS स्थान दें।",
    gps: "GPS स्थान साझा करें",
    safe: "आपका स्थान सुरक्षित रहेगा।",
    continue: "आगे बढ़ें",
    saved: "किसान सेव हो गया। भाषा लागू हो गई।"
  },
  Bengali: {
    welcomeFarmer: "স্বাগতম, কৃষক!",
    started: "চলুন শুরু করি",
    fullName: "পুরো নাম",
    mobile: "মোবাইল নম্বর",
    language: "ভাষা",
    locationTitle: "আপনার অবস্থান দিন",
    locationHelp: "স্থানীয় আবহাওয়া, ফসল পরামর্শ এবং কাছের বাজারদর পেতে GPS দিন।",
    gps: "GPS অবস্থান দিন",
    safe: "আপনার অবস্থান নিরাপদ থাকবে।",
    continue: "চালিয়ে যান",
    saved: "কৃষক সংরক্ষিত হয়েছে। ভাষা প্রয়োগ হয়েছে।"
  }
};

function showScreen(id) {
  document.querySelectorAll(".screen").forEach((screen) => screen.classList.remove("active"));
  $(id).classList.add("active");
  $(id).scrollTop = 0;
}

function applyLanguage(lang) {
  const selected = langText[lang] ? lang : "English";
  localStorage.setItem("kisanmitra_app_language", selected);
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    node.textContent = langText[selected][node.dataset.i18n] || node.textContent;
  });
}

function openFarmerRegister() {
  applyLanguage(localStorage.getItem("kisanmitra_app_language") || "English");
  $("#farmerLanguage").value = localStorage.getItem("kisanmitra_app_language") || "English";
  showScreen("#farmerRegisterScreen");
}

function setStatus(message) {
  $("#saveStatus").textContent = message || "";
}

document.addEventListener("click", (event) => {
  const go = event.target.closest("[data-go]");
  if (go) {
    if (go.dataset.go === "farmer") openFarmerRegister();
    if (go.dataset.go === "buyer") setStatus("");
  }
  if (event.target.closest("[data-back]")) showScreen("#welcomeScreen");
});

$("#farmerLanguage").addEventListener("change", (event) => {
  applyLanguage(event.target.value);
});

$("#gpsBtn").addEventListener("click", () => {
  if (!navigator.geolocation) {
    setStatus("GPS not available in this browser.");
    return;
  }
  setStatus("Requesting GPS location...");
  navigator.geolocation.getCurrentPosition((pos) => {
    gpsPoint = { lat: pos.coords.latitude, lng: pos.coords.longitude };
    setStatus("GPS captured.");
  }, () => {
    gpsPoint = null;
    setStatus("GPS permission not granted. You can continue.");
  }, { enableHighAccuracy: true, timeout: 8000 });
});

$("#farmerForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const language = $("#farmerLanguage").value || "English";
  applyLanguage(language);
  const payload = {
    full_name: $("#farmerName").value.trim(),
    mobile: $("#farmerMobile").value.trim(),
    language,
    gps_permission: Boolean(gpsPoint),
    lat: gpsPoint && gpsPoint.lat,
    lng: gpsPoint && gpsPoint.lng,
    created_at: new Date().toISOString()
  };
  if (!payload.full_name || !payload.mobile) {
    setStatus("Name and mobile number are required.");
    return;
  }
  setStatus("Saving farmer to Supabase...");
  try {
    const response = await fetch("http://127.0.0.1:8010/api/mobile-app/farmer-register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!data.ok) {
      setStatus("Save failed: " + (data.error || data.message || "Backend/Supabase issue"));
      return;
    }
    setStatus((langText[language] || langText.English).saved + " " + data.owner_id);
  } catch (error) {
    setStatus("Backend not reachable on 8010.");
  }
});

applyLanguage(localStorage.getItem("kisanmitra_app_language") || "English");
