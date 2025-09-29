// Register Alpine stores & components on init
document.addEventListener("alpine:init", () => {
  // ----------------------------
  // 🌙 THEME HANDLER
  // ----------------------------
  Alpine.data("theme", () => ({
    dark: getThemeFromLocalStorage(),

    toggleTheme() {
      this.dark = !this.dark;
      setThemeToLocalStorage(this.dark);
    },
  }));

  // ----------------------------
  // 📂 SIDEBAR HANDLER
  // ----------------------------
  Alpine.data("sidebar", () => ({
    isOpen: false,

    toggle() {
      this.isOpen = !this.isOpen;
    },
    close() {
      this.isOpen = false;
    },
  }));

  // ----------------------------
  // 🔔 NOTIFICATIONS MENU
  // ----------------------------
  Alpine.data("notificationsMenu", () => ({
    isOpen: false,

    toggle() {
      this.isOpen = !this.isOpen;
    },
    close() {
      this.isOpen = false;
    },
  }));

  // ----------------------------
  // 👤 PROFILE MENU
  // ----------------------------
  Alpine.data("profileMenu", () => ({
    isOpen: false,

    toggle() {
      this.isOpen = !this.isOpen;
    },
    close() {
      this.isOpen = false;
    },
  }));

  // ----------------------------
  // 📑 MENUS WITH SUBMENU
  // ----------------------------
  Alpine.data("sidebarSubMenu", () => ({
    isOpen: false,

    toggle() {
      this.isOpen = !this.isOpen;
    },
    close() {
      this.isOpen = false;
    },
  }));

  // ----------------------------
  // 💬 MODAL HANDLER
  // ----------------------------
  /*Alpine.data("modal", () => ({
    isOpen: false,
    trapCleanup: null,

    open() {
      this.isOpen = true;
      this.trapCleanup = focusTrap(document.querySelector("#modal"));
    },
    close() {
      this.isOpen = false;
      if (this.trapCleanup) this.trapCleanup();
    },
  }));*/
  Alpine.store("modals", {
    profileInfo: false,
    profileAddress: false,
    userProfileInfo: false,
  });
});

// ----------------------------
// 🔧 Helper Functions
// ----------------------------
function getThemeFromLocalStorage() {
  if (window.localStorage.getItem("dark")) {
    return JSON.parse(window.localStorage.getItem("dark"));
  }
  return (
    !!window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  );
}

function setThemeToLocalStorage(value) {
  window.localStorage.setItem("dark", value);
}
