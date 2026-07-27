# Decision Report

- generated_at: 2026-07-27T17:51:27.088462+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9641**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9641, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.28% | **+0.23%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.15% | **+0.10%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.13% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +6.85% | **+2.28%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.53% | **+1.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.44% | **+1.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.38% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$456.37** / 初期 $100.00 (+356.37%)
- 確定: 3429件 (Win 1085 / Loss 1116 / Flat 1228) / skip 2773件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $456.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1828件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.69** / 初期 $100.00 (+8.69%)
- 確定: 661件 (Win 218 / Loss 250 / Flat 193) / pending 5件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000377 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $108.69

## 6. Latest Market Context

- 更新: 2026-07-27T17:51:17.344712+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=64942.2
- Funnel: target 902 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LA/USDT:USDT | +31.03% | $2,217,049.34 |
| RIF/USDT:USDT | +14.70% | $4,845,069.19 |
| JIMOTHY/USDT:USDT | +11.61% | $1,916,470.77 |
| ALLO/USDT:USDT | +5.70% | $4,384,322.22 |
| 4/USDT:USDT | +4.91% | $3,275,427.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.57% | +2.46% |
| TAG/USDT:USDT | below_1h_threshold | +1.93% | +1.82% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.34% |
| VELVET/USDT:USDT | below_1h_threshold | +1.07% | +0.96% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.91% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
