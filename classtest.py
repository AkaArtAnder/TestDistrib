""" В файле реализован класс для тестирования последовательностей на нормальнность TestDistrib """

from matplotlib import pyplot as plt
from scipy import stats
import sys
import seaborn as sb
import pandas as pd
import numpy as np
import statistics as st


class TestDistrib(object):
	""" Класс реализует методы предназначенные для тестирования последовательности на нормальность """

	def __init__(self, **kwargs):
		""" Конструктор """

		try:
			r_file = open(kwargs['fileread'])
			self.data = list(map(float, r_file.read().splitlines()[:1000000]))
			self.name_distrib = kwargs['distrib']
			self.folderwrite = kwargs['folderwrite']
		except FileNotFoundError as error:
			print(error)
			sys.exit()
		except ValueError as error:
			print(error)
			sys.exit()
		else:
			r_file.close()

	@property
	def hist(self):
		""" Построение гистограммы для полученных данных """

		plt.figure()
		sb.set()
		sb.distplot(self.data)
		plt.title("Гистограмма анализируемых данных")
		plt.savefig("%shist.png" % (self.folderwrite))

	@property
	def qqplot(self):
		""" Построение квантиль-квантиль графика, показывающего отклонение от идеальных значений нормального распределения """

		plt.figure()
		sb.set()
		stats.probplot(self.data, plot=plt, dist=self.name_distrib)
		plt.title("Квантиль график для %s" % (self.name_distrib))
		plt.savefig("%sqqplot.png" % (self.folderwrite))

	@property
	def tests_on_normal(self):
		""" Набор тестов для проверки последовательности на нормальность """

		_mean = st.mean(self.data)
		_deviations = st.variance(self.data, _mean)
		_param_data = pd.DataFrame([
			[st.mean(self.data), st.variance(self.data, _mean)]],
			columns=["Мат.ожидание", "Дисперсия"])
		_param_data.to_excel("%sparam_data.xls" %
							 (self.folderwrite), encoding="utf-8")

		_w_nt, _p_value_nt = stats.normaltest(self.data)
		_w_st, _p_value_st = stats.shapiro(self.data)
		_w_kt, _p_value_kt = stats.kstest(self.data, "norm")
		_result_tests = pd.DataFrame([
			["D'Agostino-Pirson", _w_nt, _p_value_nt],
			["Shapiro-Wilk", _w_st, _p_value_st],
			["Kolmogorov-Smirnov", _w_kt, _p_value_kt]],
			columns=["Name", "Test_statistic", "P_value"])
		_result_tests.to_excel("%stest_result.xls" %
							   (self.folderwrite), encoding="utf-8")


if __name__ == "__main__":
	print(TestDistrib.__doc__)
