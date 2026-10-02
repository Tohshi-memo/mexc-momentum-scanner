# Decision Report

- generated_at: 2026-10-02T17:36:30.104799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16014, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.22% | **+0.64%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.48% | **+0.24%** |
| LIMIT_BB3S | 3/11 | 27.3% | +0.83% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.54% | **+0.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.89% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,339.06** / 初期 $100.00 (+1239.06%)
- 確定: 6119件 (Win 1807 / Loss 1961 / Flat 2351) / skip 6456件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,339.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5820件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0501 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4175件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T17:36:18.623819+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=84695.0
- Funnel: target 1099 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +18.46% | $17,777,699.95 |
| SOXS/USDT:USDT | +3.21% | $35,981,587.75 |
| SAND/USDT:USDT | +2.51% | $61,643,404.24 |
| NIGHT/USDT:USDT | +2.48% | $7,602,061.45 |
| MANA/USDT:USDT | +2.22% | $6,676,068.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.63% | +2.14% |
| ENJ/USDT:USDT | below_1h_threshold | +1.37% | +1.88% |
| BTW/USDT:USDT | below_1h_threshold | +1.33% | +1.84% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.17% | +1.69% |
| USOIL/USDT:USDT | below_1h_threshold | +0.63% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
