/* ======================================
   BLOODCARE DASHBOARD SCRIPT
====================================== */

document.addEventListener("DOMContentLoaded", function () {

  console.log("BloodCare Dashboard Loaded ✅");

  highlightActiveNav();
  animateStatCards();
  animateProgressBars();
  addHoverEffects();

});

/* ======================================
   NAVIGATION ACTIVE LINK
====================================== */

function highlightActiveNav() {
  const navLinks = document.querySelectorAll(".nav-link");
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
}

/* ======================================
   STAT CARDS ANIMATION
====================================== */

function animateStatCards() {
  const cards = document.querySelectorAll(".stat-card");

  cards.forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";
    card.style.transition = "all 0.6s ease";

    setTimeout(() => {
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, index * 150);
  });
}

/* ======================================
   PROGRESS BAR ANIMATION
====================================== */

function animateProgressBars() {
  const bars = document.querySelectorAll(".progress-fill");

  bars.forEach(bar => {
    const width = bar.style.width;
    bar.style.width = "0%";

    setTimeout(() => {
      bar.style.transition = "width 1.5s ease-in-out";
      bar.style.width = width;
    }, 300);
  });
}

/* ======================================
   HOVER EFFECTS
====================================== */

function addHoverEffects() {
  const statCards = document.querySelectorAll(".stat-card");
  const contentCards = document.querySelectorAll(".content-card");

  statCards.forEach(card => {
    card.addEventListener("mouseenter", () => {
      card.style.transform = "scale(1.03)";
      card.style.transition = "0.3s ease";
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "scale(1)";
    });
  });

  contentCards.forEach(card => {
    card.addEventListener("mouseenter", () => {
      card.style.boxShadow = "0 8px 20px rgba(0,0,0,0.08)";
      card.style.transition = "0.3s ease";
    });

    card.addEventListener("mouseleave", () => {
      card.style.boxShadow = "0 4px 12px rgba(0,0,0,0.05)";
    });
  });
}

/* ======================================
   SIMPLE LIVE CLOCK (Optional Feature)
====================================== */

function startClock() {
  const clockContainer = document.getElementById("liveClock");

  if (!clockContainer) return;

  setInterval(() => {
    const now = new Date();
    clockContainer.innerText = now.toLocaleString();
  }, 1000);
}

startClock();

/* ======================================
   TABLE ROW HIGHLIGHT
====================================== */

const tableRows = document.querySelectorAll(".data-table tbody tr");

tableRows.forEach(row => {
  row.addEventListener("mouseenter", () => {
    row.style.backgroundColor = "#f9f9f9";
  });

  row.addEventListener("mouseleave", () => {
    row.style.backgroundColor = "transparent";
  });
});
// Auto year in footer
const year = document.getElementById("year");
if (year) {
  year.textContent = new Date().getFullYear();
}