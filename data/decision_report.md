# Decision Report

- generated_at: 2026-09-16T15:26:29.120026+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14703**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14703, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.24% | **+0.23%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.26% | **+0.21%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +3.82% | **+3.18%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.16% | **+2.84%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.38% | **+2.71%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.32% | **+2.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,181.61** / 初期 $100.00 (+1081.61%)
- 確定: 5580件 (Win 1674 / Loss 1804 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,181.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.40** / 初期 $100.00 (+141.40%)
- 確定: 3107件 (Win 862 / Loss 735 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1886 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $241.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3221件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000590 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T15:26:13.825884+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=75690.6
- Funnel: target 1059 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +138.97% | $26,753,590.82 |
| BR/USDT:USDT | +128.50% | $34,269,671.89 |
| LSK/USDT:USDT | +56.90% | $30,042,927.41 |
| BULLA/USDT:USDT | +25.58% | $3,905,294.81 |
| HEI/USDT:USDT | +23.00% | $1,152,038.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.28% | +3.24% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.84% | +1.80% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.33% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.84% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.84% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
