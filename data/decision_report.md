# Decision Report

- generated_at: 2026-08-05T04:51:45.270869+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10359**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10359, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.70% | **+3.70%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.50% | **+2.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.32% | **+1.74%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.28% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$609.18** / 初期 $100.00 (+509.18%)
- 確定: 3756件 (Win 1191 / Loss 1228 / Flat 1337) / skip 3164件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $609.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.98** / 初期 $100.00 (+41.98%)
- 確定: 1296件 (Win 364 / Loss 302 / Flat 630) / skip 2474件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0978 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $141.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.50** / 初期 $100.00 (+18.50%)
- 確定: 1112件 (Win 358 / Loss 429 / Flat 325) / pending 6件 / skip 719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000415 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.50

## 6. Latest Market Context

- 更新: 2026-08-05T04:51:24.882307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64129.6
- Funnel: target 939 → liquid 185 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +89.58% | $10,057,211.21 |
| HFT/USDT:USDT | +46.35% | $1,215,643.77 |
| BLESS/USDT:USDT | +37.18% | $23,678,219.25 |
| TAKE/USDT:USDT | +35.11% | $1,582,500.70 |
| CASHCAT/USDT:USDT | +35.02% | $1,207,951.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.49% | +3.51% |
| HEI/USDT:USDT | below_1h_threshold | +3.14% | +3.17% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.89% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.87% |
| MVLL/USDT:USDT | below_1h_threshold | +2.82% | +2.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
