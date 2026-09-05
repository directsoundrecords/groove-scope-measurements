(() => {
  const cards = document.querySelectorAll("[data-fingerprint-card]");

  cards.forEach((card) => {
    const image = card.querySelector("[data-fingerprint-image]");
    const status = card.querySelector("[data-channel-status]");
    const buttons = card.querySelectorAll("[data-channel]");

    if (!image || buttons.length === 0) return;

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const channel = button.dataset.channel;
        const sourceKey = channel === "right" ? "sourceRight" : "sourceLeft";
        const altKey = channel === "right" ? "altRight" : "altLeft";

        image.src = image.dataset[sourceKey];
        image.alt = image.dataset[altKey];

        buttons.forEach((candidate) => {
          const selected = candidate === button;
          candidate.setAttribute("aria-pressed", String(selected));
        });

        if (status) {
          status.textContent = `${channel === "right" ? "Right" : "Left"} channel selected`;
        }
      });
    });
  });
})();
