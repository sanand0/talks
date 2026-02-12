// ============================================================
// Data Story Visualizations
// ============================================================

const tooltip = d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);

function showTip(event, html) {
  tooltip.html(html).style("opacity", 1)
    .style("left", (event.pageX + 14) + "px")
    .style("top", (event.pageY - 14) + "px");
}
function hideTip() { tooltip.style("opacity", 0); }

// Colors
const C = {
  red: "#e03e36", blue: "#2563eb", green: "#059669", amber: "#d97706",
  gray: "#94a3b8", lightGray: "#cbd5e1", bg: "#f1f5f9"
};

// Responsive width helper
function chartWidth(sel) {
  return Math.min(952, document.querySelector(sel)?.parentElement?.clientWidth || 952) - 48;
}

// ============================================================
// CHART 1: Team Lead Time Bar Chart
// ============================================================
(function() {
  const data = [
    { team: "Platform DevOps", ai: 0.88, lt: 12.32 },
    { team: "Tool Control SW", ai: 0.82, lt: 12.83 },
    { team: "QA Automation", ai: 0.70, lt: 12.97 },
    { team: "UI & Workflows", ai: 0.79, lt: 13.14 },
    { team: "Mfg Analytics", ai: 0.74, lt: 13.83 },
    { team: "Customer Solutions", ai: 0.62, lt: 16.49 },
    { team: "Firmware & Embedded", ai: 0.76, lt: 19.56 },
    { team: "Legacy Monolith", ai: 0.48, lt: 54.46 }
  ];

  const W = chartWidth("#chart-team-leadtime"), H = 320;
  const margin = { top: 8, right: 80, bottom: 36, left: 150 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-team-leadtime").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 60]).range([0, w]);
  const y = d3.scaleBand().domain(data.map(d => d.team)).range([0, h]).padding(0.35);
  const colorScale = d3.scaleSequential(d3.interpolateBlues).domain([0.4, 0.95]);

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).ticks(6).tickFormat(d => d + "h"))
    .call(g => g.select(".domain").remove()).call(g => g.selectAll(".tick line").attr("stroke", "#ddd"));

  g.append("g").call(d3.axisLeft(y).tickSize(0).tickPadding(10))
    .call(g => g.select(".domain").remove())
    .selectAll("text").style("font-size", "13px").style("font-weight", d => d === "Legacy Monolith" ? "700" : "400");

  g.selectAll("rect.bar").data(data).join("rect")
    .attr("class", "bar").attr("x", 0).attr("y", d => y(d.team))
    .attr("width", d => x(Math.min(d.lt, 60))).attr("height", y.bandwidth())
    .attr("fill", d => d.team === "Legacy Monolith" ? C.red : colorScale(d.ai))
    .attr("rx", 3)
    .on("mouseover", (e, d) => showTip(e, `<strong>${d.team}</strong><br>Lead time: ${d.lt}h<br>AI adoption: ${d.ai}`))
    .on("mouseout", hideTip);

  g.selectAll("text.val").data(data).join("text")
    .attr("class", "val").attr("x", d => x(Math.min(d.lt, 60)) + 6)
    .attr("y", d => y(d.team) + y.bandwidth() / 2 + 5)
    .text(d => d.lt + "h").style("font-size", "12px").style("font-weight", "600")
    .style("fill", d => d.team === "Legacy Monolith" ? C.red : "#555");
})();

// ============================================================
// CHART 2: Weekly Lead Time Trend
// ============================================================
(function() {
  const high = [
    [0,14.88],[1,15.63],[2,15.05],[3,15.45],[4,15.23],[5,15.89],[6,15.84],[7,16.01],
    [8,15.66],[9,15.36],[10,14.47],[11,15.79],[12,14.86],[13,13.57],[14,12.1],[15,12.54],
    [16,12.68],[17,12.07],[18,11.83],[19,11.21],[20,11.8],[21,11.21],[22,11.51],[23,11.35],
    [24,12.07],[25,12.75]
  ];
  const low = [
    [0,82.96],[1,63.01],[2,55.44],[3,62.83],[4,45.14],[5,43.02],[6,64.35],[7,72.37],
    [8,39.68],[9,52.38],[10,53.82],[11,54.15],[12,55.77],[13,22.31],[14,44.79],[15,45.03],
    [16,54.35],[17,60.87],[18,51.85],[19,63.63],[20,47.35],[21,58.98],[22,44.57],[23,48.85],
    [24,142.74],[25,69.66]
  ];

  const W = chartWidth("#chart-weekly-leadtime"), H = 280;
  const margin = { top: 12, right: 20, bottom: 36, left: 50 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-weekly-leadtime").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 25]).range([0, w]);
  const y = d3.scaleLinear().domain([0, 100]).range([h, 0]);

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).ticks(13).tickFormat(d => "W" + d))
    .call(g => g.select(".domain").remove()).selectAll("text").style("font-size", "10px");
  g.append("g").call(d3.axisLeft(y).ticks(5).tickFormat(d => d + "h")).call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").clone().attr("x2", w).attr("stroke", "#eee"));

  const line = d3.line().x(d => x(d[0])).y(d => y(Math.min(d[1], 100))).curve(d3.curveMonotoneX);

  g.append("path").datum(low).attr("d", line).attr("fill", "none").attr("stroke", C.red)
    .attr("stroke-width", 2).attr("stroke-dasharray", "6,4").attr("opacity", 0.7);
  g.append("path").datum(high).attr("d", line).attr("fill", "none").attr("stroke", C.blue).attr("stroke-width", 2.5);

  g.selectAll("circle.hi").data(high).join("circle").attr("cx", d => x(d[0])).attr("cy", d => y(d[1]))
    .attr("r", 3).attr("fill", C.blue)
    .on("mouseover", (e, d) => showTip(e, `Week ${d[0]}<br>High-AI: ${d[1]}h`)).on("mouseout", hideTip);
})();

// ============================================================
// CHART 3: Build Success Rate
// ============================================================
(function() {
  const legacy = [
    [0,93.17],[1,92.35],[2,92.91],[3,92.75],[4,92.42],[5,93.15],[6,93.04],[7,92.9],
    [8,93.41],[9,92.98],[10,92.81],[11,92.87],[12,93.0],[13,92.71],[14,91.26],[15,92.21],
    [16,92.02],[17,92.98],[18,89.73],[19,91.41],[20,94.15],[21,88.71],[22,90.18],[23,93.16],
    [24,92.79],[25,90.95]
  ];
  const v2 = [
    [12,96.94],[13,96.83],[14,96.29],[15,96.13],[16,96.11],[17,95.09],[18,95.94],[19,96.38],
    [20,95.95],[21,96.2],[22,95.18],[23,96.32],[24,95.16],[25,95.83]
  ];

  const W = chartWidth("#chart-build-success"), H = 260;
  const margin = { top: 12, right: 20, bottom: 36, left: 50 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-build-success").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 25]).range([0, w]);
  const y = d3.scaleLinear().domain([87, 100]).range([h, 0]);

  // Week 12 marker
  g.append("line").attr("x1", x(12)).attr("x2", x(12)).attr("y1", 0).attr("y2", h)
    .attr("stroke", "#ddd").attr("stroke-dasharray", "4,3");
  g.append("text").attr("x", x(12) + 4).attr("y", 12).text("v2 rollout").style("font-size", "10px").style("fill", "#aaa");

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).ticks(13).tickFormat(d => "W" + d))
    .call(g => g.select(".domain").remove()).selectAll("text").style("font-size", "10px");
  g.append("g").call(d3.axisLeft(y).ticks(5).tickFormat(d => d + "%")).call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").clone().attr("x2", w).attr("stroke", "#eee"));

  const line = d3.line().x(d => x(d[0])).y(d => y(d[1])).curve(d3.curveMonotoneX);

  g.append("path").datum(legacy).attr("d", line).attr("fill", "none").attr("stroke", C.gray).attr("stroke-width", 2);
  g.append("path").datum(v2).attr("d", line).attr("fill", "none").attr("stroke", C.blue).attr("stroke-width", 2.5);

  g.selectAll("circle.v2").data(v2).join("circle").attr("cx", d => x(d[0])).attr("cy", d => y(d[1]))
    .attr("r", 3).attr("fill", C.blue)
    .on("mouseover", (e, d) => showTip(e, `Week ${d[0]}<br>Pipeline v2: ${d[1]}%`)).on("mouseout", hideTip);
  g.selectAll("circle.leg").data(legacy).join("circle").attr("cx", d => x(d[0])).attr("cy", d => y(d[1]))
    .attr("r", 2.5).attr("fill", C.gray)
    .on("mouseover", (e, d) => showTip(e, `Week ${d[0]}<br>Legacy: ${d[1]}%`)).on("mouseout", hideTip);
})();

// ============================================================
// CHART 4: VB-7734 Defect Spikes
// ============================================================
(function() {
  const data = [
    {w:0,vb:0,other:3223},{w:1,vb:0,other:3092},{w:2,vb:0,other:3168},{w:3,vb:0,other:3214},
    {w:4,vb:0,other:3150},{w:5,vb:0,other:3127},{w:6,vb:0,other:3163},{w:7,vb:0,other:3160},
    {w:8,vb:1058,other:2839},{w:9,vb:1031,other:2799},{w:10,vb:1055,other:2775},
    {w:11,vb:0,other:3107},{w:12,vb:0,other:3061},{w:13,vb:0,other:3172},{w:14,vb:0,other:3108},
    {w:15,vb:0,other:3217},{w:16,vb:0,other:3217},{w:17,vb:0,other:3251},{w:18,vb:0,other:3171},
    {w:19,vb:0,other:3209},{w:20,vb:1069,other:2935},{w:21,vb:1078,other:2815},
    {w:22,vb:0,other:3008},{w:23,vb:0,other:3114},{w:24,vb:0,other:3111},{w:25,vb:0,other:3159}
  ];

  const W = chartWidth("#chart-defect-spikes"), H = 280;
  const margin = { top: 12, right: 20, bottom: 36, left: 56 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-defect-spikes").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleBand().domain(data.map(d => d.w)).range([0, w]).padding(0.2);
  const y = d3.scaleLinear().domain([0, 4500]).range([h, 0]);

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).tickValues([0,4,8,12,16,20,24]).tickFormat(d => "W" + d))
    .call(g => g.select(".domain").remove()).selectAll("text").style("font-size", "10px");
  g.append("g").call(d3.axisLeft(y).ticks(5).tickFormat(d3.format(","))).call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").clone().attr("x2", w).attr("stroke", "#eee"));

  // Stacked bars
  g.selectAll("rect.other").data(data).join("rect")
    .attr("x", d => x(d.w)).attr("y", d => y(d.other)).attr("width", x.bandwidth())
    .attr("height", d => h - y(d.other)).attr("fill", C.lightGray).attr("rx", 2);

  g.selectAll("rect.vb").data(data).join("rect")
    .attr("x", d => x(d.w)).attr("y", d => y(d.other + d.vb)).attr("width", x.bandwidth())
    .attr("height", d => y(d.other) - y(d.other + d.vb)).attr("fill", C.red).attr("rx", 2)
    .on("mouseover", (e, d) => {
      if (d.vb > 0) showTip(e, `<strong>Week ${d.w}</strong><br>VB-7734: ${d3.format(",")(d.vb)}<br>Other: ${d3.format(",")(d.other)}<br>Total: ${d3.format(",")(d.vb + d.other)}`);
    }).on("mouseout", hideTip);

  // Spike annotations
  g.append("text").attr("x", x(9) + x.bandwidth()/2).attr("y", y(4200)).text("Spike 1")
    .style("font-size", "11px").style("fill", C.red).style("text-anchor", "middle").style("font-weight", "600");
  g.append("text").attr("x", x(20) + x.bandwidth()/2).attr("y", y(4200)).text("Spike 2")
    .style("font-size", "11px").style("fill", C.red).style("text-anchor", "middle").style("font-weight", "600");
})();

// ============================================================
// CHART 5: Detection Stage Comparison
// ============================================================
(function() {
  const data = [
    { group: "VB-7734", stage: "InLine", pct: 47.8 },
    { group: "VB-7734", stage: "FinalTest", pct: 31.9 },
    { group: "VB-7734", stage: "Customer", pct: 20.3 },
    { group: "Normal", stage: "InLine", pct: 73.8 },
    { group: "Normal", stage: "FinalTest", pct: 20.0 },
    { group: "Normal", stage: "Customer", pct: 6.1 },
  ];

  const W = chartWidth("#chart-detection-stage"), H = 200;
  const margin = { top: 28, right: 20, bottom: 36, left: 90 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-detection-stage").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const groups = ["VB-7734", "Normal"];
  const stages = ["InLine", "FinalTest", "Customer"];
  const colors = { InLine: C.green, FinalTest: C.amber, Customer: C.red };

  const y0 = d3.scaleBand().domain(groups).range([0, h]).padding(0.4);
  const x = d3.scaleLinear().domain([0, 100]).range([0, w]);

  g.append("g").call(d3.axisLeft(y0).tickSize(0).tickPadding(10)).call(g => g.select(".domain").remove())
    .selectAll("text").style("font-size", "13px").style("font-weight", "600");

  // Stage labels at top
  const stageLegend = svg.append("g").attr("transform", `translate(${margin.left}, 10)`);
  stages.forEach((s, i) => {
    stageLegend.append("rect").attr("x", i * 120).attr("y", 0).attr("width", 12).attr("height", 12).attr("rx", 2).attr("fill", colors[s]);
    stageLegend.append("text").attr("x", i * 120 + 16).attr("y", 10).text(s).style("font-size", "11px").style("fill", "#666");
  });

  groups.forEach(group => {
    let cumX = 0;
    stages.forEach(stage => {
      const d = data.find(r => r.group === group && r.stage === stage);
      g.append("rect")
        .attr("x", x(cumX)).attr("y", y0(group))
        .attr("width", x(d.pct)).attr("height", y0.bandwidth())
        .attr("fill", colors[stage]).attr("rx", 2)
        .on("mouseover", (e) => showTip(e, `<strong>${group}</strong><br>${stage}: ${d.pct}%`))
        .on("mouseout", hideTip);

      if (d.pct > 8) {
        g.append("text").attr("x", x(cumX + d.pct / 2)).attr("y", y0(group) + y0.bandwidth() / 2 + 4)
          .text(d.pct + "%").style("font-size", "12px").style("fill", "#fff").style("text-anchor", "middle").style("font-weight", "600");
      }
      cumX += d.pct;
    });
  });
})();

// ============================================================
// CHART 6: LOC Risk Tipping Point
// ============================================================
(function() {
  const data = [
    { bucket: "<500", rate: 0.82, n: 1709 },
    { bucket: "500-1K", rate: 1.40, n: 3004 },
    { bucket: "1K-2K", rate: 3.20, n: 3468 },
    { bucket: "2K-3K", rate: 7.41, n: 1484 },
    { bucket: "3K-5K", rate: 10.54, n: 1034 },
    { bucket: "5K+", rate: 15.58, n: 565 }
  ];

  const W = chartWidth("#chart-loc-risk"), H = 300;
  const margin = { top: 12, right: 20, bottom: 48, left: 56 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-loc-risk").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleBand().domain(data.map(d => d.bucket)).range([0, w]).padding(0.3);
  const y = d3.scaleLinear().domain([0, 18]).range([h, 0]);

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).tickSize(0).tickPadding(10))
    .call(g => g.select(".domain").remove()).selectAll("text").style("font-size", "11px");
  g.append("text").attr("x", w / 2).attr("y", h + 42).text("Lines of Code Changed").style("font-size", "12px")
    .style("text-anchor", "middle").style("fill", "#888");

  g.append("g").call(d3.axisLeft(y).ticks(5).tickFormat(d => d + "%")).call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").clone().attr("x2", w).attr("stroke", "#eee"));

  // Danger zone shading
  g.append("rect").attr("x", x("3K-5K")).attr("y", 0).attr("width", x("5K+") + x.bandwidth() - x("3K-5K"))
    .attr("height", h).attr("fill", "#fef2f2").attr("rx", 4);
  g.append("text").attr("x", (x("3K-5K") + x("5K+") + x.bandwidth()) / 2).attr("y", 14)
    .text("Danger Zone").style("font-size", "10px").style("fill", C.red).style("text-anchor", "middle").style("font-weight", "600");

  const colorFn = d => d.rate > 10 ? C.red : d.rate > 5 ? C.amber : C.blue;

  g.selectAll("rect.bar").data(data).join("rect")
    .attr("class", "bar").attr("x", d => x(d.bucket)).attr("y", d => y(d.rate))
    .attr("width", x.bandwidth()).attr("height", d => h - y(d.rate))
    .attr("fill", colorFn).attr("rx", 3).attr("opacity", 0.85)
    .on("mouseover", (e, d) => showTip(e, `<strong>${d.bucket} LOC</strong><br>Incident rate: ${d.rate}%<br>Deployments: ${d3.format(",")(d.n)}`))
    .on("mouseout", hideTip);

  g.selectAll("text.val").data(data).join("text")
    .attr("x", d => x(d.bucket) + x.bandwidth() / 2).attr("y", d => y(d.rate) - 6)
    .text(d => d.rate + "%").style("font-size", "12px").style("font-weight", "600")
    .style("text-anchor", "middle").style("fill", colorFn);
})();

// ============================================================
// CHART 7: AI Code Review Effect
// ============================================================
(function() {
  const data = [
    { label: "Without AI Review", rate: 14.45, n: 616, color: C.red },
    { label: "With AI Review", rate: 10.99, n: 983, color: C.green }
  ];

  const W = chartWidth("#chart-ai-review"), H = 150;
  const margin = { top: 8, right: 80, bottom: 12, left: 160 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-ai-review").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 18]).range([0, w]);
  const y = d3.scaleBand().domain(data.map(d => d.label)).range([0, h]).padding(0.4);

  g.append("g").call(d3.axisLeft(y).tickSize(0).tickPadding(10)).call(g => g.select(".domain").remove())
    .selectAll("text").style("font-size", "13px").style("font-weight", "600");

  g.selectAll("rect.bar").data(data).join("rect")
    .attr("x", 0).attr("y", d => y(d.label)).attr("width", d => x(d.rate)).attr("height", y.bandwidth())
    .attr("fill", d => d.color).attr("rx", 3).attr("opacity", 0.85);

  g.selectAll("text.val").data(data).join("text")
    .attr("x", d => x(d.rate) + 6).attr("y", d => y(d.label) + y.bandwidth() / 2 + 5)
    .text(d => d.rate + "% (n=" + d.n + ")").style("font-size", "12px").style("font-weight", "600").style("fill", "#555");

  // Arrow annotation
  const arrowX = x(12.7), arrowY1 = y("Without AI Review") + y.bandwidth(), arrowY2 = y("With AI Review");
  g.append("line").attr("x1", arrowX).attr("x2", arrowX).attr("y1", arrowY1 + 2).attr("y2", arrowY2 - 2)
    .attr("stroke", C.blue).attr("stroke-width", 2).attr("marker-end", "url(#arrowhead)");
  g.append("text").attr("x", arrowX + 8).attr("y", (arrowY1 + arrowY2) / 2 + 4)
    .text("-24%").style("font-size", "13px").style("fill", C.blue).style("font-weight", "700");

  // Arrowhead
  svg.append("defs").append("marker").attr("id", "arrowhead").attr("viewBox", "0 0 10 10")
    .attr("refX", 5).attr("refY", 5).attr("markerWidth", 6).attr("markerHeight", 6).attr("orient", "auto")
    .append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", C.blue);
})();

// ============================================================
// CHART 8: Service Scatter (Monolith highlight)
// ============================================================
(function() {
  const data = [
    { name: "recipe-manager", deploys: 1206, rate: 4.89, lt: 14.0 },
    { name: "build-pipeline", deploys: 1314, rate: 3.27, lt: 13.5 },
    { name: "config-service", deploys: 1294, rate: 4.25, lt: 14.2 },
    { name: "tool-scheduler", deploys: 1165, rate: 3.18, lt: 13.8 },
    { name: "customer-portal", deploys: 1036, rate: 3.57, lt: 15.0 },
    { name: "firmware-updater", deploys: 919, rate: 4.03, lt: 19.5 },
    { name: "qa-orchestrator", deploys: 904, rate: 3.87, lt: 13.2 },
    { name: "telemetry-ingest", deploys: 902, rate: 4.88, lt: 14.5 },
    { name: "fault-analyzer", deploys: 869, rate: 3.80, lt: 13.0 },
    { name: "reporting-pack", deploys: 807, rate: 5.08, lt: 14.8 },
    { name: "case-routing", deploys: 694, rate: 4.61, lt: 16.5 },
    { name: "monolith-core", deploys: 154, rate: 13.64, lt: 54.5 }
  ];

  const W = chartWidth("#chart-service-scatter"), H = 340;
  const margin = { top: 12, right: 20, bottom: 48, left: 56 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-service-scatter").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 60]).range([0, w]);
  const y = d3.scaleLinear().domain([0, 16]).range([h, 0]);
  const r = d3.scaleSqrt().domain([100, 1400]).range([6, 22]);

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).ticks(6).tickFormat(d => d + "h"))
    .call(g => g.select(".domain").remove());
  g.append("text").attr("x", w / 2).attr("y", h + 40).text("Median Lead Time (hours)").style("font-size", "12px")
    .style("text-anchor", "middle").style("fill", "#888");

  g.append("g").call(d3.axisLeft(y).ticks(5).tickFormat(d => d + "%")).call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").clone().attr("x2", w).attr("stroke", "#eee"));
  g.append("text").attr("transform", "rotate(-90)").attr("x", -h / 2).attr("y", -44).text("Incident Rate (%)")
    .style("font-size", "12px").style("text-anchor", "middle").style("fill", "#888");

  const colorFn = d => d.name === "monolith-core" ? C.red : C.blue;

  g.selectAll("circle").data(data).join("circle")
    .attr("cx", d => x(d.lt)).attr("cy", d => y(d.rate)).attr("r", d => r(d.deploys))
    .attr("fill", colorFn).attr("opacity", d => d.name === "monolith-core" ? 0.85 : 0.3)
    .attr("stroke", colorFn).attr("stroke-width", 1.5)
    .on("mouseover", (e, d) => showTip(e, `<strong>${d.name}</strong><br>Deploys: ${d.deploys}<br>Incident rate: ${d.rate}%<br>Lead time: ${d.lt}h`))
    .on("mouseout", hideTip);

  // Label monolith
  g.append("text").attr("x", x(54.5) - 4).attr("y", y(13.64) - 16)
    .text("monolith-core").style("font-size", "12px").style("font-weight", "700").style("fill", C.red).style("text-anchor", "end");
  g.append("text").attr("x", x(14)).attr("y", y(4) - 20)
    .text("microservices cluster").style("font-size", "11px").style("fill", "#888").style("text-anchor", "middle");
})();

// ============================================================
// CHART 9: Convergence Multi-Line
// ============================================================
(function() {
  const defectRate = [
    [0,.0117],[1,.011],[2,.0115],[3,.0115],[4,.0114],[5,.0112],[6,.0114],[7,.0114],
    [8,.0184],[9,.018],[10,.018],[11,.0111],[12,.0109],[13,.0114],[14,.011],[15,.0117],
    [16,.0117],[17,.0116],[18,.0115],[19,.0115],[20,.0185],[21,.0182],[22,.0112],[23,.0112],
    [24,.0114],[25,.0112]
  ];
  const cases = [
    [0,210],[1,175],[2,170],[3,134],[4,159],[5,137],[6,126],[7,155],
    [8,249],[9,232],[10,211],[11,93],[12,91],[13,73],[14,61],[15,74],
    [16,82],[17,79],[18,75],[19,60],[20,131],[21,119],[22,44],[23,42],
    [24,54],[25,46]
  ];
  const onTrack = [
    [0,1],[1,1],[2,1],[3,.875],[4,1],[5,.929],[6,.867],[7,.75],
    [8,.75],[9,.7],[10,.75],[11,.7],[12,.7],[13,.65],[14,.7],[15,.55],
    [16,.7],[17,.45],[18,.5],[19,.4],[20,.35],[21,.25],[22,.25],[23,.25],
    [24,.2],[25,.2]
  ];

  const W = chartWidth("#chart-convergence"), H = 320;
  const margin = { top: 12, right: 60, bottom: 36, left: 56 };
  const w = W - margin.left - margin.right, h = H - margin.top - margin.bottom;

  const svg = d3.select("#chart-convergence").append("svg").attr("viewBox", `0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, 25]).range([0, w]);

  // Three y-axes
  const yDefect = d3.scaleLinear().domain([0.008, 0.022]).range([h, 0]);
  const yCases = d3.scaleLinear().domain([0, 280]).range([h, 0]);
  const yTrack = d3.scaleLinear().domain([0, 1.1]).range([h, 0]);

  // Spike shading
  [[8, 10], [20, 21]].forEach(([a, b]) => {
    g.append("rect").attr("x", x(a - 0.4)).attr("y", 0)
      .attr("width", x(b + 0.4) - x(a - 0.4)).attr("height", h)
      .attr("fill", "#fef2f2").attr("rx", 4);
  });

  g.append("g").attr("transform", `translate(0,${h})`).call(d3.axisBottom(x).ticks(13).tickFormat(d => "W" + d))
    .call(g => g.select(".domain").remove()).selectAll("text").style("font-size", "10px");

  // Left axis: defect rate
  g.append("g").call(d3.axisLeft(yDefect).ticks(4).tickFormat(d3.format(".3f")))
    .call(g => g.select(".domain").remove())
    .selectAll("text").style("fill", C.red).style("font-size", "10px");

  // Right axis: on-track ratio
  g.append("g").attr("transform", `translate(${w},0)`).call(d3.axisRight(yTrack).ticks(5).tickFormat(d3.format(".0%")))
    .call(g => g.select(".domain").remove())
    .selectAll("text").style("fill", C.blue).style("font-size", "10px");

  const lineDefect = d3.line().x(d => x(d[0])).y(d => yDefect(d[1])).curve(d3.curveMonotoneX);
  const lineCases = d3.line().x(d => x(d[0])).y(d => yCases(d[1])).curve(d3.curveMonotoneX);
  const lineTrack = d3.line().x(d => x(d[0])).y(d => yTrack(d[1])).curve(d3.curveMonotoneX);

  g.append("path").datum(defectRate).attr("d", lineDefect).attr("fill", "none").attr("stroke", C.red).attr("stroke-width", 2.5);
  g.append("path").datum(cases).attr("d", lineCases).attr("fill", "none").attr("stroke", C.amber).attr("stroke-width", 2).attr("stroke-dasharray", "6,3");
  g.append("path").datum(onTrack).attr("d", lineTrack).attr("fill", "none").attr("stroke", C.blue).attr("stroke-width", 2.5);

  // Dots for interaction
  g.selectAll("circle.dr").data(defectRate).join("circle").attr("cx", d => x(d[0])).attr("cy", d => yDefect(d[1]))
    .attr("r", 3).attr("fill", C.red).attr("opacity", 0)
    .on("mouseover", function(e, d) {
      d3.select(this).attr("opacity", 1);
      const ci = cases.find(c => c[0] === d[0]);
      const ot = onTrack.find(c => c[0] === d[0]);
      showTip(e, `<strong>Week ${d[0]}</strong><br>Defect rate: ${d[1].toFixed(4)}<br>Cases: ${ci?ci[1]:'-'}<br>On-track: ${ot?(ot[1]*100).toFixed(0)+'%':'-'}`);
    }).on("mouseout", function() { d3.select(this).attr("opacity", 0); hideTip(); });

  // Annotations
  g.append("text").attr("x", x(9)).attr("y", yDefect(0.0205)).text("VB-7734").style("font-size", "10px")
    .style("fill", C.red).style("text-anchor", "middle").style("font-weight", "600");
})();
