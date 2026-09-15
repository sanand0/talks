import { readFileSync, writeFileSync } from "node:fs";

const START = "<!-- BEGIN GENERATED TALKS -->";
const END = "<!-- END GENERATED TALKS -->";
const config = JSON.parse(readFileSync("config.json", "utf8"));

const escapeLabel = (text) => text.replaceAll("\\", "\\\\").replaceAll("[", "\\[").replaceAll("]", "\\]");
const mdLink = (label, link) => `[${escapeLabel(label)}](${link.url}${link.ignore ? ' ":ignore"' : ""})`;
const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const dateLabel = (date) => {
  const [year, month, day] = date.split("-");
  return `${day} ${months[Number(month) - 1]} ${year}`;
};

const defaults = {
  page: ["📖", "Page"],
  video: ["⏯️", "Video"],
  audio: ["🎧", "Audio"],
  transcript: ["💬", "Transcript"],
  slides: ["🪧", "Slides"],
  screencast: ["💻", "Screencast"],
  code: ["💻", "Code"],
  chat: ["💬", "Chat"],
};
const resourceOrder = { page: 0, video: 1, screencast: 2, slides: 3, transcript: 4, audio: 5, code: 6, chat: 7 };

function resourceLabel(link) {
  const [icon, fallback] = defaults[link.type] ?? ["🔗", link.type];
  const label = link.label ?? fallback;
  return `${icon} ${label}${link.minutes ? ` (${link.minutes}m)` : ""}`;
}

function resources(talk) {
  return [...talk.links]
    .filter((link) => !link.primary)
    .sort((a, b) => (resourceOrder[a.type] ?? 99) - (resourceOrder[b.type] ?? 99))
    .map((link) => mdLink(resourceLabel(link), link))
    .join(" · ");
}

function title(talk) {
  const primary = talk.links.find((link) => link.primary);
  return primary ? mdLink(talk.title, primary) : escapeLabel(talk.title);
}

function speakers(talk) {
  if (!talk.speakers?.length) return "";
  const items = talk.speakers.map((person) => person.url ? mdLink(person.name, person) : escapeLabel(person.name));
  if (items.length === 1) return items[0];
  if (items.length === 2) return `${items[0]} and ${items[1]}`;
  return `${items.slice(0, -1).join(", ")}, and ${items.at(-1)}`;
}

function venue(talk) {
  const event = talk.event?.name
    ? (talk.event.url ? mdLink(talk.event.name, talk.event) : escapeLabel(talk.event.name))
    : "";
  if (event && talk.location) return `at ${event}, ${talk.location}.`;
  if (event) return `at ${event}.`;
  if (talk.location) return `in ${talk.location}.`;
  return "";
}

const inCategory = (category) => config.talks
  .filter((talk) => talk.categories.includes(category))
  .sort((a, b) => b.date.localeCompare(a.date));

function renderTalk(talk, { showSpeakers = false } = {}) {
  const byline = showSpeakers && talk.speakers?.length ? ` — ${speakers(talk)}` : "";
  const where = venue(talk);
  const heading = `- ${dateLabel(talk.date)}. **${title(talk)}**${byline}${where ? ` ${where}` : ""}  `;
  const lines = [heading];
  if (talk.details) lines.push(`  ${talk.details}  `);
  const links = resources(talk);
  if (links) lines.push(`  ${links}`);
  return lines.join("\n");
}

const renderLatest = () => inCategory("latest").map((talk) => renderTalk(talk)).join("\n");
const renderArchive = () => inCategory("archive").map((talk) => renderTalk(talk)).join("\n");
const renderVideos = () => inCategory("videos").map((talk) => renderTalk(talk)).join("\n");
const renderOthers = () => inCategory("others").map((talk) => renderTalk(talk, { showSpeakers: true })).join("\n");

const playlist = `https://www.youtube.com/playlist?list=${config.youtube_playlist}`;
const generated = `${START}
## Latest talks

${renderLatest()}

## Archives

I'll migrate old talks here over time. This [YouTube Playlist](${playlist}) has many.

${renderArchive()}

## Videos from past talks

${renderVideos()}

## Others' Talks

${renderOthers()}
${END}`;

let readme = readFileSync("README.md", "utf8");
if (readme.includes(START) && readme.includes(END)) {
  readme = readme.replace(new RegExp(`${START}[\\s\\S]*?${END}`), generated);
} else {
  const start = readme.indexOf("## Latest talks");
  const footerMarkers = ["<!--\n\n## WIP", "## Bio for talks"];
  const end = footerMarkers.map((marker) => readme.indexOf(marker, start)).find((index) => index >= 0);
  if (start < 0 || end == null) throw new Error("Could not locate generated catalog boundaries in README.md");
  readme = `${readme.slice(0, start)}${generated}\n\n${readme.slice(end)}`;
}
const previousReadme = readFileSync("README.md", "utf8");
if (readme !== previousReadme) writeFileSync("README.md", readme);
