// MyST plugin providing the {support-button} directive: a button that opens
// the Freshdesk support widget, with options to prefill the ticket form.
//
// Example usage:
// 
//   :::{support-button}
//   :label: Click here to request a feature
//   :subject: Request a feature for my hub
//   :type: Feature Request
//   :::
//
// This is basically a simple wrapper around the anywidget directive, but
// our own directive allows us to avoid hand-writing anywidget data in each body.

let count = 0;

const supportButton = {
  name: 'support-button',
  doc: 'A button that opens the 2i2c support widget. Options prefill the ticket form.',
  options: {
    label: { type: String, doc: 'Text shown on the button' },
    subject: { type: String, doc: 'Prefilled ticket subject' },
    type: { type: String, doc: 'Prefilled ticket type, e.g. "Feature Request"' },
  },
  run(data) {
    return [
      {
        type: 'anywidget',
        esm: '/src/support-widget.mjs',
        model: { ...data.options },
        id: `support-button-${count++}`,
      },
    ];
  },
};

const plugin = {
  name: '2i2c support button',
  directives: [supportButton],
  transforms: [
    {
      name: 'support-widget-loader',
      doc: 'Append a hidden support widget to every page so the floating "Help" launcher loads site-wide.',
      stage: 'document',
      plugin: () => (tree) => {
        tree.children.push({
          type: 'anywidget',
          esm: '/src/support-widget.mjs',
          model: { hidden: true },
          id: `support-loader-${count++}`,
        });
      },
    },
  ],
};
export default plugin;
