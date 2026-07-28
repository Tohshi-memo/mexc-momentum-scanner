# Decision Report

- generated_at: 2026-07-28T19:06:28.454812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9720**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9720, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.72% | **+0.25%** |
| LIMIT_BB3S | 11/18 | 61.1% | +0.08% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.92% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.42% | **+0.73%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +1.92% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.29** / 初期 $100.00 (+394.29%)
- 確定: 3490件 (Win 1104 / Loss 1132 / Flat 1254) / skip 2791件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $494.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1905件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1035 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.75** / 初期 $100.00 (+9.75%)
- 確定: 738件 (Win 239 / Loss 281 / Flat 218) / pending 4件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000449 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.75

## 6. Latest Market Context

- 更新: 2026-07-28T19:06:23.527944+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=63812.7
- Funnel: target 904 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +22.00% | $1,257,898.96 |
| ON/USDT:USDT | +19.59% | $30,648,786.39 |
| BTW/USDT:USDT | +14.73% | $5,700,836.65 |
| RIF/USDT:USDT | +10.09% | $4,846,102.37 |
| BULLA/USDT:USDT | +6.87% | $2,866,159.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +0.98% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.79% | +0.63% |
| RE/USDT:USDT | below_1h_threshold | +0.75% | +0.59% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +0.58% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.64% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
