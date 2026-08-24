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
  home.title = "S Anand";
  logo.append(home);

  const themeToggle = document.querySelector("dark-mode");
  if (themeToggle) logo.append(themeToggle);

  nav.append(logo);
  header.append(nav);
  document.body.prepend(header);
});
