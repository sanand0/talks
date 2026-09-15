import { readFileSync, writeFileSync } from "node:fs";

// Inline outline icons follow Lucide's visual language (24px, currentColor, rounded strokes).
const svg = (body) => `<svg class="talk-resource-icon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
const icons = {
  page: svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/>'),
  video: svg('<circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4z"/>'),
  audio: svg('<path d="M4 14a8 8 0 0 1 16 0"/><path d="M18 19c0 1.1-.9 2-2 2h-1v-7h3a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2z"/><path d="M6 19c0 1.1.9 2 2 2h1v-7H6a2 2 0 0 0-2 2v1a2 2 0 0 0 2 2z"/>'),
  transcript: svg('<path d="M21 15a4 4 0 0 1-4 4H8l-5 3V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z"/><path d="M8 8h8"/><path d="M8 12h6"/>'),
  slides: svg('<path d="M2 3h20"/><path d="M4 3v13h16V3"/><path d="m8 21 4-5 4 5"/>'),
  screencast: svg('<rect x="2" y="3" width="20" height="14" rx="2"/><path d="m10 8 5 3-5 3z"/><path d="M8 21h8"/><path d="M12 17v4"/>'),
  code: svg('<path d="m8 9-4 3 4 3"/><path d="m16 9 4 3-4 3"/><path d="m14 5-4 14"/>'),
};

function addResource(html, emoji, type, icon, label = "") {
  const pattern = label
    ? new RegExp(`(<a\\b[^>]*>)${emoji}\\s+${label}`, "g")
    : new RegExp(`(<a\\b[^>]*>)${emoji}\\s+`, "g");
  const suffix = label || "";
  return html.replace(pattern, (match, open) => {
    const tagged = open.replace("<a", `<a class="talk-resource talk-resource-${type}"`);
    return `${tagged}${icon}${suffix}`;
  });
}

function structureTalkLists(fragment) {
  fragment = fragment.replace(/<ul>/g, '<ul class="talk-list">');
  return fragment.replace(/<li>([\s\S]*?)<\/li>/g, (match, body) => {
    const lines = body.split("<br>");
    if (!/^\d{2} [A-Z][a-z]{2} \d{4}[.:]/.test(lines[0])) return match;

    const heading = lines[0].replace(
      /^(\d{2} [A-Z][a-z]{2} \d{4})([.:])\s*/,
      '<span class="talk-date">$1</span>$2 '
    );
    const resources = lines.at(-1)?.includes("talk-resource-icon") ? lines.pop() : "";
    lines[0] = heading;
    const details = lines.slice(1).join("<br>");

    return `<li class="talk-item"><div class="talk-heading">${heading}</div>${details ? `<div class="talk-details">${details}</div>` : ""}${resources ? `<div class="talk-resources">${resources}</div>` : ""}</li>`;
  });
}

let html = readFileSync("index.html", "utf8");
html = addResource(html, "💻", "code", icons.code, "Code");
html = addResource(html, "💻", "screencast", icons.screencast);
html = addResource(html, "📖", "page", icons.page);
html = addResource(html, "⏯️", "video", icons.video);
html = addResource(html, "🎧", "audio", icons.audio);
html = addResource(html, "💬", "transcript", icons.transcript);
html = addResource(html, "🪧", "slides", icons.slides);
html = html.replace(
  /(<!-- BEGIN GENERATED TALKS -->)([\s\S]*?)(<!-- END GENERATED TALKS -->)/,
  (_, start, fragment, end) => `${start}${structureTalkLists(fragment)}${end}`
);
writeFileSync("index.html", html);
