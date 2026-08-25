// @ts-check
const root = document.documentElement;
const savedTheme = localStorage.getItem("pref-theme");
root.dataset.colorMode = savedTheme ?? (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

const moon = `<svg id="moon" xmlns="http://www.w3.org/2000/svg" width="24" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
const sun = `<svg id="sun" xmlns="http://www.w3.org/2000/svg" width="24" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;

document.addEventListener("DOMContentLoaded", () => {
  const header = document.createElement("header");
  header.className = "site-header";

  const nav = document.createElement("nav");
  nav.className = "site-nav";

  const logo = document.createElement("div");
  logo.className = "site-logo";

  const home = document.createElement("a");
  home.href = "https://www.s-anand.net/";
  home.textContent = "S Anand";
  home.title = "S Anand (Alt + H)";
  home.accessKey = "h";

  const themeToggle = document.createElement("button");
  themeToggle.id = "theme-toggle";
  themeToggle.type = "button";
  themeToggle.accessKey = "t";
  themeToggle.title = "(Alt + T)";
  themeToggle.ariaLabel = "Toggle theme";
  themeToggle.innerHTML = moon + sun;
  themeToggle.addEventListener("click", () => {
    root.dataset.colorMode = root.dataset.colorMode === "dark" ? "light" : "dark";
    localStorage.setItem("pref-theme", root.dataset.colorMode);
  });

  logo.append(home, themeToggle);
  nav.append(logo);
  header.append(nav);
  document.body.prepend(header);
});
