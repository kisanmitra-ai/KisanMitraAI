window.KISANMITRA_MODULES = [
  { id:"farmer-registry", name:"Farmer Registry", status:"ready", admin:true, app:true, web:true, dataSource:"backend", description:"Farmer onboarding and identity records" },
  { id:"farm-boundary", name:"Farm Boundary", status:"ready", admin:true, app:true, web:true, dataSource:"backend", description:"Boundary trace, save, and farm ID linking" },
  { id:"master-farm-registry", name:"Master Farm Registry", status:"ready", admin:true, app:false, web:true, dataSource:"backend", description:"Central verified farm database" },
  { id:"crop-expert", name:"Crop Expert", status:"active", admin:true, app:true, web:true, dataSource:"ai", description:"Crop advisory, disease, pest and planning AI" },
  { id:"weather-intelligence", name:"Weather Intelligence", status:"active", admin:true, app:true, web:true, dataSource:"weather_api", description:"Temperature, humidity, rain and forecast logic" },
  { id:"ndvi", name:"NDVI / Satellite Intelligence", status:"pending", admin:true, app:true, web:true, dataSource:"satellite", description:"Satellite crop health and vegetation intelligence" },
  { id:"soil-water", name:"Soil & Water Intelligence", status:"pending", admin:true, app:true, web:true, dataSource:"soil_water_api", description:"Soil, water, risk and suitability intelligence" },
  { id:"buyer-matching", name:"Buyer Matching", status:"active", admin:true, app:true, web:true, dataSource:"backend", description:"Buyer discovery and crop-to-cash matching" },
  { id:"logistics", name:"Logistics Engine", status:"active", admin:true, app:true, web:true, dataSource:"backend", description:"Pickup, transport, distance and delivery flow" },
  { id:"whatsapp-center", name:"WhatsApp Center", status:"active", admin:true, app:true, web:true, dataSource:"whatsapp", description:"Farmer-buyer WhatsApp communication center" }
];
