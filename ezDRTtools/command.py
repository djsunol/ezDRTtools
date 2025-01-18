import pyDRTtools
import pyDRTtools.runs
import csv


def ExportDRT(eisdata, path):
    if eisdata is None:
        return

    # select path to save the results

    if eisdata.method == 'simple':
        with open(path, 'w', newline='') as save_file:
            writer = csv.writer(save_file)

            # first save L and R
            writer.writerow(['L', eisdata.L])
            writer.writerow(['R', eisdata.R])
            writer.writerow(['lambda_value', eisdata.lambda_value])
            writer.writerow(['tau', 'gamma'])

            # after that, save tau and gamma
            for n in range(eisdata.out_tau_vec.shape[0]):
                writer.writerow([eisdata.out_tau_vec[n], eisdata.gamma[n]])

    elif eisdata.method == 'credit':
        with open(path, 'w', newline='') as save_file:
            writer = csv.writer(save_file)

            # first save L and R
            writer.writerow(['L', eisdata.L])
            writer.writerow(['R', eisdata.R])
            writer.writerow(['tau', 'MAP', 'Mean', 'Upperbound', 'Lowerbound'])

            # after that, save tau, gamma, mean, upper bound, and lower bound
            for n in range(eisdata.out_tau_vec.shape[0]):
                writer.writerow([eisdata.out_tau_vec[n], eisdata.gamma[n],
                                 eisdata.mean[n], eisdata.upper_bound[n],
                                 eisdata.lower_bound[n]])

    elif eisdata.method == 'BHT':
        with open(path, 'w', newline='') as save_file:
            writer = csv.writer(save_file)

            # first save L and R
            writer.writerow(['L', eisdata.mu_L_0])
            writer.writerow(['R', eisdata.mu_R_inf])
            writer.writerow(['tau', 'gamma_Re', 'gamma_Im'])

            # after that, save tau, gamma_re, and gamma_im
            for n in range(eisdata.out_tau_vec.shape[0]):
                writer.writerow([eisdata.out_tau_vec[n],
                                 eisdata.mu_gamma_fine_re[n],
                                 eisdata.mu_gamma_fine_im[n]])


def main():
    eisdata = pyDRTtools.runs.EIS_object.from_file("X:\\SAI\\DRT\\DRT data\\Sim 12861 R-RC-RC.txt")
    pyDRTtools.runs.simple_run(eisdata)
    ExportDRT(eisdata, "X:\\SAI\\DRT\\DRT data\\Sim 12861 R-RC-RC_DRTexport.txt")


if __name__ == "__main__":
    main()


