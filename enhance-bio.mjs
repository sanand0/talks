import { readFileSync, writeFileSync } from "node:fs";

// The bio uses the homepage's Markdown renderer, stylesheet, and JS, but lives one level deeper.
let html = readFileSync("bio/index.html", "utf8");
function replaceOnce(pattern, replacement) {
  const matches = html.match(pattern);
  if (!matches || matches.length !== 1) throw new Error(`Expected one match for ${pattern}`);
  html = html.replace(pattern, replacement);
}

const url = "https://talks.s-anand.net/bio/";
const title = "Bio for talks | S Anand";
const description = "S Anand's speaker bio, photos, presentation logistics, and honorarium preferences.";
replaceOnce(/<title>[^<]+<\/title>/g, `<title>${title}</title>`);
for (const name of ["description", "twitter:description"]) {
  replaceOnce(new RegExp(`<meta name="${name}" content="[^"]*">`, "g"), `<meta name="${name}" content="${description}">`);
}
for (const name of ["og:description", "og:title", "og:url"]) {
  const value = name === "og:description" ? description : name === "og:title" ? "Bio for talks" : url;
  replaceOnce(new RegExp(`<meta property="${name}" content="[^"]*">`, "g"), `<meta property="${name}" content="${value}">`);
}
replaceOnce(/<meta name="twitter:title" content="[^"]*">/g, '<meta name="twitter:title" content="Bio for talks">');
replaceOnce(/<link rel="canonical" href="[^"]*">/g, `<link rel="canonical" href="${url}">`);
replaceOnce(/<link rel="alternate" hreflang="en" href="[^"]*">/g, `<link rel="alternate" hreflang="en" href="${url}">`);
replaceOnce(/<link rel="alternate" type="text\/markdown" href="[^"]*">/g, '<link rel="alternate" type="text/markdown" href="https://raw.githubusercontent.com/sanand0/talks/main/bio.md">');
for (const rel of ["icon", "apple-touch-icon", "mask-icon"]) {
  const pattern = new RegExp(`(<link rel="${rel}"[^>]*href=")favicon\\.svg("[^>]*>)`, "g");
  replaceOnce(pattern, '$1../favicon.svg$2');
}
replaceOnce(/<script src="talks\.js"><\/script>/g, '<script src="../talks.js"></script>');
writeFileSync("bio/index.html", html);
