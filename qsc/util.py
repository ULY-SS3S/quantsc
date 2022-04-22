import qsc
def change_backend(backend):
    if backend not in ['matplotlib','plotly']:
        raise("Plotting backend must be in " + str(qsc.config.config['supported_plot_backend']))
    qsc.config.config['plot_backend'] = backend