# Decision Report

- generated_at: 2026-10-02T19:56:33.940743+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16017**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16017, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.07% | **+0.73%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.80% | **+0.44%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.63% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.21% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.35% | **+0.81%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.61% | **+0.55%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.42% | **+0.24%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.47% | **+0.23%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,339.06** / 初期 $100.00 (+1239.06%)
- 確定: 6122件 (Win 1807 / Loss 1961 / Flat 2354) / skip 6456件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,339.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5823件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0433 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000138 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T19:56:19.704943+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=84204.4
- Funnel: target 1099 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1, 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +9.22% | $1,073,509.53 |
| LONGXIA/USDT:USDT | +3.72% | $18,466,969.95 |
| CT/USDT:USDT | +3.17% | $10,108,925.65 |
| SOXS/USDT:USDT | +2.83% | $32,671,725.64 |
| NMR/USDT:USDT | +2.14% | $1,475,207.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NMR/USDT:USDT | below_1h_threshold | +3.85% | +3.87% |
| CT/USDT:USDT | below_1h_threshold | +2.57% | +2.59% |
| BTW/USDT:USDT | below_1h_threshold | +1.42% | +1.44% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.68% | +0.70% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.63% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
