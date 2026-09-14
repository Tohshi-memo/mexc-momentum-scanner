# Decision Report

- generated_at: 2026-09-14T07:26:31.798292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14500, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.65% | **+0.82%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.57% | **+0.54%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.68% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.84% | **+2.42%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +3.41% | **+2.38%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.68% | **+2.01%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.01% | **+1.21%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.55% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,083.39** / 初期 $100.00 (+983.39%)
- 確定: 5435件 (Win 1636 / Loss 1762 / Flat 2037) / skip 5626件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $1,083.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4920件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.86** / 初期 $100.00 (+26.86%)
- 確定: 2881件 (Win 859 / Loss 1114 / Flat 908) / pending 6件 / skip 3087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.86

## 6. Latest Market Context

- 更新: 2026-09-14T07:26:19.631239+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=77696.0
- Funnel: target 1068 → liquid 145 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1, 4h RSI 84.4 >= 65=1, 4h RSI 76.9 >= 65=1, 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +52.34% | $1,515,618.13 |
| CATE/USDT:USDT | +50.13% | $1,772,282.17 |
| BR/USDT:USDT | +43.23% | $5,306,557.04 |
| MTL/USDT:USDT | +30.07% | $1,468,379.92 |
| ARK/USDT:USDT | +27.16% | $4,623,026.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +3.55% | +3.37% |
| USELESS/USDT:USDT | below_1h_threshold | +3.09% | +2.90% |
| PUNDIX/USDT:USDT | below_1h_threshold | +2.98% | +2.80% |
| UAI/USDT:USDT | below_1h_threshold | +2.63% | +2.45% |
| PONS/USDT:USDT | below_1h_threshold | +1.85% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
