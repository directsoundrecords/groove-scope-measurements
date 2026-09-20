(() => {
  "use strict";

  const latest = document.getElementById("latest");
  const results = document.getElementById("library-results");
  const status = document.getElementById("catalogue-status");
  const search = document.getElementById("search");
  const sort = document.getElementById("sort");
  const empty = document.getElementById("empty-state");
  const tabs = Array.from(document.querySelectorAll("[data-view]"));
  if (!latest || !results || !status || !search || !sort || !empty) return;

  const state = { catalogue: null, view: "systems" };
  const labels = {
    cartridges: "Cartridge",
    turntables: "Turntable",
    tonearms: "Tonearm",
    phono_stages: "Phono stage",
  };
  const componentLabels = {
    turntable: "Turntable",
    tonearm: "Tonearm",
    cartridge: "Cartridge",
    phono_stage: "Phono Stage",
  };

  const escapeHTML = (value) => String(value ?? "")
    .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;").replaceAll("'", "&#039;");
  const normalise = (value) => String(value ?? "").normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase();
  const componentName = (measurement, key) => measurement.components?.[key]?.display_name || "Not recorded";
  const formatDate = (value) => {
    if (!value) return "Date not recorded";
    const date = new Date(`${value}T12:00:00Z`);
    return new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" }).format(date);
  };
  const metricValue = (metric) => {
    const decimals = metric.unit === "RPM" ? 2 : metric.identifier.includes("wow_flutter") ? 3 : 2;
    const signed = ["playback_speed_error_percent", "channel_balance_db"].includes(metric.identifier);
    const number = Number(metric.value).toFixed(decimals).replace(/(\.\d*[1-9])0+$/, "$1").replace(/\.00$/, "");
    return `${signed && metric.value > 0 ? "+" : ""}${number}`;
  };
  const metricByID = (measurement, identifier) => measurement.headline_metrics.find((item) => item.identifier === identifier);
  const metricMarkup = (metric) => metric ? `
    <div class="metric"><dt>${escapeHTML(metric.display_label)}</dt><dd>${escapeHTML(metricValue(metric))}<small>${escapeHTML(metric.unit)}</small></dd></div>` : "";

  function renderLatest(measurement) {
    if (!measurement) {
      latest.innerHTML = '<div class="error-panel">No measurements are visible under the current publication policy.</div>';
      latest.removeAttribute("aria-busy");
      return;
    }
    const heroMetrics = [
      "playback_rpm", "playback_speed_error_percent", "din_shaped_wow_flutter_percent",
      "channel_balance_db", "average_channel_separation_db", "thd_left_percent", "thd_right_percent",
    ].map((id) => metricByID(measurement, id)).filter(Boolean);
    const thdLeft = metricByID(measurement, "thd_left_percent");
    const thdRight = metricByID(measurement, "thd_right_percent");
    const metrics = heroMetrics.filter((item) => !item.identifier.startsWith("thd_"));
    if (thdLeft && thdRight) {
      metrics.push({ identifier: "thd_channels", display_label: "THD", value: `${metricValue(thdLeft)}% L / ${metricValue(thdRight)}% R`, unit: "" });
    }
    const renderHeroMetric = (metric) => metric.identifier === "thd_channels"
      ? `<div class="metric"><dt>THD</dt><dd class="paired">${escapeHTML(metric.value)}</dd></div>`
      : metricMarkup(metric);
    const components = Object.entries(componentLabels).map(([key, label]) => `
      <div><dt>${label}</dt><dd>${escapeHTML(componentName(measurement, key))}</dd></div>`).join("");
    latest.innerHTML = `
      <div class="latest-photo">
        <img src="${escapeHTML(measurement.images.hero.url)}" width="2400" height="1800" alt="Documented ${escapeHTML(measurement.system_title)} measurement system." fetchpriority="high">
        <span class="latest-label">Latest measurement</span>
      </div>
      <div class="latest-copy">
        <div class="latest-title-row"><span class="measurement-id">${escapeHTML(measurement.measurement_id)}</span><span class="status-pill status-${escapeHTML(measurement.publication_status)}">${escapeHTML(measurement.status_label)}</span></div>
        <h2 id="latest-heading">${escapeHTML(measurement.system_title)}</h2>
        <p class="measurement-type">${escapeHTML(measurement.measurement_type)}</p>
        <p class="measured-with">Measured with <strong>${escapeHTML(componentName(measurement, "phono_stage"))}</strong></p>
        <dl class="component-strip">${components}</dl>
        <dl class="metric-strip">${metrics.map(renderHeroMetric).join("")}</dl>
        <div class="hero-actions"><a class="primary-action" href="${escapeHTML(measurement.measurement_url)}">View Full Measurement <span aria-hidden="true">→</span></a><a class="secondary-action" href="${escapeHTML(measurement.technical_record_url)}">Technical record <span aria-hidden="true">↗</span></a></div>
      </div>`;
    latest.removeAttribute("aria-busy");
  }

  function sortedMeasurements(measurements) {
    const ordered = [...measurements];
    const key = sort.value;
    ordered.sort((a, b) => {
      if (key === "cartridge") return componentName(a, "cartridge").localeCompare(componentName(b, "cartridge"));
      if (key === "turntable") return componentName(a, "turntable").localeCompare(componentName(b, "turntable"));
      const comparison = String(a.measurement_date || "").localeCompare(String(b.measurement_date || ""));
      return key === "oldest" ? comparison : -comparison;
    });
    return ordered;
  }

  function matchingMeasurements() {
    const terms = normalise(search.value).trim().split(/\s+/).filter(Boolean);
    return sortedMeasurements(state.catalogue.measurements.filter((measurement) => {
      const haystack = normalise(`${measurement.search_text} ${measurement.title} ${measurement.summary}`);
      return terms.every((term) => haystack.includes(term));
    }));
  }

  function systemCard(measurement) {
    const metrics = ["playback_rpm", "din_shaped_wow_flutter_percent", "average_channel_separation_db"]
      .map((id) => metricByID(measurement, id)).filter(Boolean);
    return `
      <article class="system-card">
        <a class="card-image" href="${escapeHTML(measurement.measurement_url)}"><img src="${escapeHTML(measurement.images.card.url)}" width="1200" height="675" alt="${escapeHTML(measurement.system_title)} documented measurement system." loading="lazy" decoding="async"></a>
        <div class="card-copy">
          <div class="card-meta"><span class="measurement-id">${escapeHTML(measurement.measurement_id)}</span><span class="status-dot">${escapeHTML(measurement.status_label)}</span></div>
          <h3><a href="${escapeHTML(measurement.measurement_url)}">${escapeHTML(measurement.system_title)}</a></h3>
          <p class="card-phono">${escapeHTML(componentName(measurement, "phono_stage"))}</p>
          ${metrics.length ? `<dl class="card-metrics">${metrics.map(metricMarkup).join("")}</dl>` : ""}
          <div class="card-footer"><span>Measured · ${escapeHTML(formatDate(measurement.measurement_date))}</span><a href="${escapeHTML(measurement.measurement_url)}" aria-label="View ${escapeHTML(measurement.measurement_id)}">View <span aria-hidden="true">→</span></a></div>
        </div>
      </article>`;
  }

  function componentCards(measurements) {
    const visibleIDs = new Set(measurements.map((measurement) => measurement.measurement_id));
    return (state.catalogue.components[state.view] || []).map((component) => {
      const linked = component.measurement_ids
        .filter((id) => visibleIDs.has(id))
        .map((id) => state.catalogue.measurements.find((measurement) => measurement.measurement_id === id))
        .filter(Boolean);
      if (!linked.length) return "";
      const lead = linked[0];
      const links = linked.map((measurement) => `<li><a href="${escapeHTML(measurement.measurement_url)}"><span>${escapeHTML(measurement.measurement_id)}</span><strong>${escapeHTML(measurement.system_title)}</strong><small>Measured ${escapeHTML(formatDate(measurement.measurement_date))}</small></a></li>`).join("");
      return `
        <article class="component-card">
          <div class="component-card-head"><span class="component-kind">${escapeHTML(labels[state.view])}</span><span>${linked.length} ${linked.length === 1 ? "system" : "systems"}</span></div>
          <h3>${escapeHTML(component.display_name)}</h3>
          <p>Documented measurement ${linked.length === 1 ? "session" : "sessions"} containing this ${escapeHTML(labels[state.view].toLocaleLowerCase())}.</p>
          <ul>${links}</ul>
          <img src="${escapeHTML(lead.images.card.url)}" width="1200" height="675" alt="" loading="lazy" decoding="async">
        </article>`;
    }).filter(Boolean);
  }

  function renderLibrary() {
    if (!state.catalogue) return;
    const measurements = matchingMeasurements();
    const cards = state.view === "systems" ? measurements.map(systemCard) : componentCards(measurements);
    results.classList.toggle("component-grid", state.view !== "systems");
    results.innerHTML = cards.join("");
    empty.hidden = cards.length !== 0;
    const noun = state.view === "systems" ? (measurements.length === 1 ? "documented system" : "documented systems") : (cards.length === 1 ? labels[state.view].toLocaleLowerCase() : `${labels[state.view].toLocaleLowerCase()}s`);
    status.textContent = `${state.view === "systems" ? measurements.length : cards.length} ${noun}`;
  }

  tabs.forEach((tab) => tab.addEventListener("click", () => {
    state.view = tab.dataset.view;
    tabs.forEach((candidate) => candidate.setAttribute("aria-selected", String(candidate === tab)));
    renderLibrary();
  }));
  search.addEventListener("input", renderLibrary);
  sort.addEventListener("change", renderLibrary);

  fetch("catalog.json", { headers: { Accept: "application/json" } })
    .then((response) => {
      if (!response.ok) throw new Error(`Catalogue request failed (${response.status})`);
      return response.json();
    })
    .then((catalogue) => {
      if (!Array.isArray(catalogue.measurements)) throw new Error("Catalogue has no measurements array");
      state.catalogue = catalogue;
      const newest = catalogue.measurements.find((item) => item.measurement_id === catalogue.latest_measurement_id) || catalogue.measurements[0];
      renderLatest(newest);
      renderLibrary();
    })
    .catch((error) => {
      latest.innerHTML = `<div class="error-panel"><strong>Reference Library unavailable.</strong><span>${escapeHTML(error.message)}</span><a href="catalog.json">Open the JSON feed</a></div>`;
      latest.removeAttribute("aria-busy");
      status.textContent = "Catalogue unavailable";
    });
})();
