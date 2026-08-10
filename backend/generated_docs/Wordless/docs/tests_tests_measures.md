# Module : tests/tests_measures

11 fichier(s), 92 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : assert_zeros, get_test_text, test__get_dists, test__z_test_p_val, test_aari, test_ald, test_arf, test_ari, test_awt, test_bayes_factor_log_likelihood_ratio_test, test_bayes_factor_students_t_test_2_sample, test_bormuths_cloze_mean, test_bormuths_gp, test_brunets_index, test_carrolls_d2
- **Dépendances** : math, numpy, scipy, tests, tests.tests_measures, wordless.wl_measures

## Détail des fichiers

### `test_measure_utils.py`

Module Python. Nombre de lignes: 129. Elements detectés: def test_to_measure_code, def test_to_measure_text, def test_to_freqs_sections_1_sample

**Fonctions** : test_to_measure_code, test_to_measure_text, test_to_freqs_sections_1_sample, test_to_freqs_sections_dispersion, test_to_freqs_sections_adjusted_freq, test_to_freqs_sections_2_sample, test_to_freqs_sections_statistical_significance, test_to_freqs_sections_bayes_factor, test_numpy_divide, test_numpy_log, test_numpy_log2, test_numpy_log10
**Dépendances** : numpy, tests, wordless.wl_measures

### `test_measures_adjusted_freq.py`

Module Python. Nombre de lignes: 78. Elements detectés: def test_fald, def test_farf, def test_fawt

**Fonctions** : test_fald, test_farf, test_fawt, test_carrolls_um, test_juillands_u, test_rosengres_kf, test_engwalls_fm, test_kromers_ur
**Dépendances** : tests, tests.tests_measures, wordless.wl_measures

### `test_measures_bayes_factor.py`

Module Python. Nombre de lignes: 44. Elements detectés: def test_bayes_factor_log_likelihood_ratio_test, def test_bayes_factor_students_t_test_2_sample

**Fonctions** : test_bayes_factor_log_likelihood_ratio_test, test_bayes_factor_students_t_test_2_sample
**Dépendances** : numpy, tests, wordless.wl_measures

### `test_measures_dispersion.py`

Module Python. Nombre de lignes: 76. Elements detectés: def test__get_dists, def test_ald, def test_arf

**Fonctions** : test__get_dists, test_ald, test_arf, test_awt, test_carrolls_d2, test_griess_dp, test_juillands_d, test_lynes_d3, test_rosengrens_s, test_zhangs_distributional_consistency
**Dépendances** : tests, wordless.wl_measures

### `test_measures_effect_size.py`

Module Python. Nombre de lignes: 308. Elements detectés: def test_get_numpy_log, def assert_zeros, def test_conditional_probability

**Fonctions** : test_get_numpy_log, assert_zeros, test_conditional_probability, test_delta_p, test_dice_sorensen_coeff, test_diff_coeff, test_jaccard_index, test_kilgarriffs_ratio, test_log_dice, test_log_ratio, test_mi_log_f, test_min_sensitivity, test_me, test_mi, test_nmi
**Dépendances** : math, numpy, tests, wordless.wl_measures

### `test_measures_lexical_density_diversity.py`

Module Python. Nombre de lignes: 186. Elements detectés: def get_test_text, def test_brunets_index, def test_cttr

**Fonctions** : get_test_text, test_brunets_index, test_cttr, test_fishers_index_of_diversity, test_herdans_vm, test_hdd, test_honores_stat, test_lexical_density, test_logttr, test_msttr, test_mtld, test_mattr, test_popescu_macutek_altmanns_b1_b2_b3_b4_b5, test_popescus_r1, test_popescus_r2
**Dépendances** : numpy, scipy, tests, wordless.wl_measures

### `test_measures_misc.py`

Module Python. Nombre de lignes: 28. Elements detectés: def test_modes

**Fonctions** : test_modes
**Dépendances** : tests, wordless.wl_measures

### `test_measures_readability.py`

Module Python. Nombre de lignes: 552. Elements detectés: def test_rd, def test_aari, def test_ari

**Fonctions** : test_rd, test_aari, test_ari, test_bormuths_cloze_mean, test_bormuths_gp, test_coleman_liau_index, test_colemans_readability_formula, test_crawfords_readability_formula, test_x_c50, test_danielson_bryans_readability_formula, test_dawoods_readability_formula, test_drp, test_devereux_readability_index, test_dickes_steiwer_handformel, test_elf
**Dépendances** : math, numpy, tests, wordless.wl_measures

### `test_measures_statistical_significance.py`

Module Python. Nombre de lignes: 284. Elements detectés: def test_get_freqs_marginal, def test_get_freqs_expected, def test_get_alt

**Fonctions** : test_get_freqs_marginal, test_get_freqs_expected, test_get_alt, test_fishers_exact_test, test_log_likelihood_ratio_test, test_mann_whitney_u_test, test_pearsons_chi_squared_test, test_students_t_test_1_sample, test_students_t_test_2_sample, test__z_test_p_val, test_z_test, test_z_test_berry_rogghe
**Dépendances** : numpy, tests, wordless.wl_measures

### `test_measures_syntactic_complexity.py`

Module Python. Nombre de lignes: 45. Elements detectés: def test_mdd, def test_ndd

**Fonctions** : test_mdd, test_ndd
**Dépendances** : numpy, wordless.wl_measures
