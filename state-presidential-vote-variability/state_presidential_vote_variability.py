import pandas
import matplotlib.pyplot as plt

def save_plot(series, plot_name):
    plt.figure()
    plot = series.plot()
    plot.get_figure().savefig(plot_name + '.png')

def iqr(data):
    range = lambda x: x.max() - x.min()
    return data.quantile([0.25, 0.75]).apply(range)

state_data_path = 'percent_for_winning_candidate_1828_2012.csv'
# The spreadsheet is in reverse chronological order, so we reverse it
state_data = pandas.read_csv(state_data_path) \
                   .set_index('State') \
                   .drop('Washington DC') \
                   .ix[::,::-1]

save_plot(state_data.var(), plot_name='state_results_variance')
save_plot(state_data.mad(), plot_name='state_results_mad')
save_plot(iqr(state_data), plot_name='state_results_iqr')
