// Loads the Freshdesk support widget and renders a button that opens it.
// Use via the {support-button} directive (defined in src/support-button.mjs),
// whose options become the model values that prefill the ticket form.
// A transform in src/support-button.mjs also appends a hidden instance to
// every page, so the floating "Help" launcher loads site-wide.
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
    // Hidden instances only load the floating widget, no button.
    if (model.get("hidden")) return;
    const button = document.createElement("button");
    button.textContent = model.get("label") || "Open a support ticket";
    // The widget renders in a shadow DOM, so style the element inline.
    button.style.cssText =
      "border-radius: .5em; padding: 1em; background: rgb(29, 78, 245); color: white; font-weight: bold; border: none; cursor: pointer;";
    button.addEventListener("click", () => {
      const prefill = {};
      // Map model keys to Freshdesk ticket form fields. Always send every
      // field (empty by default): the form state is global, so a partial
      // prefill would leak values from a previously clicked button.
      for (const [key, field] of [
        ["name", "name"],
        ["email", "email"],
        ["subject", "subject"],
        ["description", "description"],
        ["type", "type"],
        ["hub_url", "cf_hub_url"],
      ]) {
        prefill[field] = model.get(key) || "";
      }
      window.FreshworksWidget("prefill", "ticketForm", prefill);
      window.FreshworksWidget("open");
    });
    el.appendChild(button);
  },
};
