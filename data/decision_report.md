# Decision Report

- generated_at: 2026-07-28T19:46:29.159078+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9723**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9723, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.22% | **-1.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_BB3S | 11/18 | 61.1% | +0.62% | **+0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.64% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.42% | **+2.18%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.03% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.42% | **+0.73%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$504.23** / 初期 $100.00 (+404.23%)
- 確定: 3493件 (Win 1106 / Loss 1132 / Flat 1255) / skip 2791件
- 成長率目線: 平均log +0.000463 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $504.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1908件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1317 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.51** / 初期 $100.00 (+10.51%)
- 確定: 741件 (Win 241 / Loss 281 / Flat 219) / pending 5件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000483 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $110.51

## 6. Latest Market Context

- 更新: 2026-07-28T19:46:21.395889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63665.7
- Funnel: target 904 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +32.44% | $1,375,921.77 |
| ON/USDT:USDT | +27.06% | $33,381,034.38 |
| BTW/USDT:USDT | +15.02% | $5,878,641.52 |
| RIF/USDT:USDT | +13.87% | $5,055,215.51 |
| RAVE/USDT:USDT | +7.51% | $1,524,287.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +4.58% | +4.65% |
| RAVE/USDT:USDT | below_1h_threshold | +3.44% | +3.51% |
| RIF/USDT:USDT | below_1h_threshold | +2.86% | +2.93% |
| LIT/USDT:USDT | below_1h_threshold | +2.04% | +2.11% |
| ACH/USDT:USDT | below_1h_threshold | +1.70% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
