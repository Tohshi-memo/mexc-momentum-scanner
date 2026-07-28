# Decision Report

- generated_at: 2026-07-28T11:56:28.837380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9695, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_BB3S | 7/19 | 36.8% | +0.45% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.71% | **+2.44%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定トレード: 149件 (TP 51 / SL 93 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.38
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$472.47** / 初期 $100.00 (+372.47%)
- 確定: 3465件 (Win 1093 / Loss 1123 / Flat 1249) / skip 2791件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $472.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1881件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0828 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.83** / 初期 $100.00 (+8.83%)
- 確定: 715件 (Win 232 / Loss 273 / Flat 210) / pending 6件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.83

## 6. Latest Market Context

- 更新: 2026-07-28T11:56:20.112629+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63439.9
- Funnel: target 898 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +55.43% | $19,474,142.11 |
| ON/USDT:USDT | +26.73% | $18,659,972.70 |
| DEXE/USDT:USDT | +22.91% | $16,609,537.52 |
| SOONNETWORK/USDT:USDT | +17.31% | $1,897,200.88 |
| VANRY/USDT:USDT | +16.26% | $1,377,093.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEOPLE/USDT:USDT | below_1h_threshold | +3.21% | +3.22% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.03% | +3.03% |
| AKE/USDT:USDT | below_1h_threshold | +2.48% | +2.48% |
| COAI/USDT:USDT | below_1h_threshold | +2.32% | +2.33% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.81% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
