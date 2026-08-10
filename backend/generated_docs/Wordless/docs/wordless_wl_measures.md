# Module : wordless/wl_measures

11 fichier(s), 93 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _get_dists, _z_test_p_val, aari, ald, arf, ari, awt, bayes_factor_log_likelihood_ratio_test, bayes_factor_students_t_test_2_sample, bormuths_cloze_mean, bormuths_gp, brunets_index, carrolls_d2, carrolls_um, coleman_liau_index
- **Dépendances** : PyQt5, bisect, collections, copy, math, numpy, random, re, scipy, scipy.special, scipy.stats, wordless.wl_checks

## Détail des fichiers

### `wl_measure_utils.py`

Module Python. Nombre de lignes: 111. Elements detectés: def to_measure_code, def to_measure_text, def to_freqs_sections_1_sample

**Fonctions** : to_measure_code, to_measure_text, to_freqs_sections_1_sample, to_freqs_sections_dispersion, to_freqs_sections_adjusted_freq, to_freqs_sections_2_sample, to_freqs_sections_statistical_significance, to_freqs_sections_bayes_factor, numpy_divide, numpy_log, numpy_log2, numpy_log10
**Dépendances** : collections, numpy, PyQt5, wordless.wl_nlp

### `wl_measures_adjusted_freq.py`

Module Python. Nombre de lignes: 71. Elements detectés: def fald, def farf, def fawt

**Fonctions** : fald, farf, fawt, carrolls_um, juillands_u, rosengrens_kf, engwalls_fm, kromers_ur
**Dépendances** : numpy, scipy.special, wordless.wl_measures

### `wl_measures_bayes_factor.py`

Module Python. Nombre de lignes: 46. Elements detectés: def bayes_factor_log_likelihood_ratio_test, def bayes_factor_students_t_test_2_sample

**Fonctions** : bayes_factor_log_likelihood_ratio_test, bayes_factor_students_t_test_2_sample
**Dépendances** : numpy, wordless.wl_measures

### `wl_measures_dispersion.py`

Module Python. Nombre de lignes: 129. Elements detectés: def _get_dists, def ald, def arf

**Fonctions** : _get_dists, ald, arf, awt, carrolls_d2, griess_dp, juillands_d, lynes_d3, rosengrens_s, zhangs_distributional_consistency
**Dépendances** : numpy, scipy.stats, wordless.wl_measures

### `wl_measures_effect_size.py`

Module Python. Nombre de lignes: 235. Elements detectés: def get_numpy_log, def conditional_probability, def delta_p

**Fonctions** : get_numpy_log, conditional_probability, delta_p, dice_sorensen_coeff, diff_coeff, jaccard_index, kilgarriffs_ratio, log_dice, log_ratio, mi_log_f, min_sensitivity, me, mi, nmi, mu_val
**Dépendances** : math, numpy, wordless.wl_measures

### `wl_measures_lexical_density_diversity.py`

Module Python. Nombre de lignes: 396. Elements detectés: def brunets_index, def cttr, def fishers_index_of_diversity

**Fonctions** : brunets_index, cttr, fishers_index_of_diversity, herdans_vm, hdd, honores_stat, lexical_density, logttr, msttr, mtld, mattr, popescu_macutek_altmanns_b1_b2_b3_b4_b5, popescus_r1, popescus_r2, popescus_r3
**Dépendances** : collections, random, numpy, PyQt5, scipy, wordless.wl_nlp

### `wl_measures_misc.py`

Module Python. Nombre de lignes: 28. Elements detectés: def modes

**Fonctions** : modes
**Dépendances** : numpy

### `wl_measures_readability.py`

Module Python. Nombre de lignes: 1211. Elements detectés: def get_nums, def get_num_words_ltrs, def get_num_words_syls

**Fonctions** : get_nums, get_num_words_ltrs, get_num_words_syls, pos_tag_words, get_num_words_pos_tag, get_nums_words_pos_tags, get_num_words_outside_list, get_num_sentences_sample, rd, aari, ari, bormuths_cloze_mean, bormuths_gp, coleman_liau_index, colemans_readability_formula
**Dépendances** : bisect, copy, math, random, re, numpy, PyQt5, wordless.wl_checks, wordless.wl_nlp, wordless.wl_utils

### `wl_measures_statistical_significance.py`

Module Python. Nombre de lignes: 192. Elements detectés: def get_freqs_marginal, def get_freqs_expected, def yatess_correction

**Fonctions** : get_freqs_marginal, get_freqs_expected, yatess_correction, get_alt, fishers_exact_test, log_likelihood_ratio_test, mann_whitney_u_test, pearsons_chi_squared_test, students_t_test_1_sample, students_t_test_2_sample, _z_test_p_val, z_test, z_test_berry_rogghe
**Dépendances** : numpy, PyQt5, scipy.stats, wordless.wl_measures

### `wl_measures_syntactic_complexity.py`

Module Python. Nombre de lignes: 70. Elements detectés: def mdd, def ndd

**Fonctions** : mdd, ndd
**Dépendances** : numpy
