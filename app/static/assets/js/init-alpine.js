// window.data = function () {
//   function getThemeFromLocalStorage() {
//     if (window.localStorage.getItem("dark")) {
//       return JSON.parse(window.localStorage.getItem("dark"));
//     }
//     return (
//       !!window.matchMedia &&
//       window.matchMedia("(prefers-color-scheme: dark)").matches
//     );
//   }

//   function setThemeToLocalStorage(value) {
//     window.localStorage.setItem("dark", value);
//   }

//   return {
//     dark: getThemeFromLocalStorage(),
//     toggleTheme() {
//       this.dark = !this.dark;
//       setThemeToLocalStorage(this.dark);
//     },
//     isSideMenuOpen: false,
//     toggleSideMenu() {
//       this.isSideMenuOpen = !this.isSideMenuOpen;
//     },
//     closeSideMenu() {
//       this.isSideMenuOpen = false;
//     },
//     isNotificationsMenuOpen: false,
//     toggleNotificationsMenu() {
//       this.isNotificationsMenuOpen = !this.isNotificationsMenuOpen;
//     },
//     closeNotificationsMenu() {
//       this.isNotificationsMenuOpen = false;
//     },
//     isProfileMenuOpen: false,
//     toggleProfileMenu() {
//       this.isProfileMenuOpen = !this.isProfileMenuOpen;
//     },
//     closeProfileMenu() {
//       this.isProfileMenuOpen = false;
//     },
//     isPagesMenuOpen: false,
//     togglePagesMenu() {
//       this.isPagesMenuOpen = !this.isPagesMenuOpen;
//     },
//     // Modal
//     isModalOpen: false,
//     trapCleanup: null,
//     openModal() {
//       this.isModalOpen = true;
//       this.trapCleanup = focusTrap(document.querySelector("#modal"));
//     },
//     closeModal() {
//       this.isModalOpen = false;
//       this.trapCleanup();
//     },
//   };
// };


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
  // 📑 PAGES MENU
  // ----------------------------
  Alpine.data("pagesMenu", () => ({
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
  Alpine.data("modal", () => ({
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
  }));
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