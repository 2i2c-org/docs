// Loads the Freshdesk support widget and renders a button that opens it.
// Use via the {support-button} directive (defined in src/support-button.mjs),
// whose options become the model values that prefill the ticket form.
// The instance in parts/footer.md loads the floating widget on every page.
// ref: https://support.freshdesk.com/en/support/solutions/articles/239273-setting-up-your-help-widget
// ref: https://support.freshdesk.com/en/support/solutions/articles/50000001015-launching-the-widget-when-a-button-is-clicked

const WIDGET_ID = 80000009162;

function loadFreshworks() {
  if (typeof window.FreshworksWidget === "function") return;
  window.fwSettings = { widget_id: WIDGET_ID };
  const n = function () {
    n.q.push(arguments);
  };
  n.q = [];
  window.FreshworksWidget = n;
  const script = document.createElement("script");
  script.src = `https://euc-widget.freshworks.com/widgets/${WIDGET_ID}.js`;
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);
}

export default {
  render({ model, el }) {
    loadFreshworks();
    const button = document.createElement("button");
    button.textContent = model.get("label") || "Open a support ticket";
    // The widget renders in a shadow DOM, so style the element inline.
    button.style.cssText =
      "border-radius: .5em; padding: 1em; background: rgb(29, 78, 245); color: white; font-weight: bold; border: none; cursor: pointer;";
    button.addEventListener("click", () => {
      const prefill = {};
      // Map model keys to Freshdesk ticket form fields
      for (const [key, field] of [
        ["name", "name"],
        ["email", "email"],
        ["subject", "subject"],
        ["description", "description"],
        ["type", "type"],
        ["hub_url", "cf_hub_url"],
      ]) {
        const value = model.get(key);
        if (value) prefill[field] = value;
      }
      if (Object.keys(prefill).length) {
        window.FreshworksWidget("prefill", "ticketForm", prefill);
      }
      window.FreshworksWidget("open");
    });
    el.appendChild(button);
  },
};
