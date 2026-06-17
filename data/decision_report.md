# Decision Report

- generated_at: 2026-06-17T23:16:49.519301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6975**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=6975, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.07% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.48** / 初期 $100.00 (+1.48%)
- 確定トレード: 12件 (TP 5 / SL 7 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.48
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$199.69** / 初期 $100.00 (+99.69%)
- 確定: 1822件 (Win 497 / Loss 574 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $199.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定: 248件 (Win 65 / Loss 63 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.011% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0673 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.88

## 5. Latest Market Context

- 更新: 2026-06-17T23:16:45.246540+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64321.9
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +82.93% | $1,423,575.86 |
| ESPORTS/USDT:USDT | +51.91% | $19,146,639.14 |
| SYN/USDT:USDT | +42.57% | $4,108,084.89 |
| RE/USDT:USDT | +15.91% | $1,820,512.75 |
| MITO/USDT:USDT | +15.13% | $1,637,842.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +3.43% | +3.34% |
| KAS/USDT:USDT | below_1h_threshold | +2.77% | +2.68% |
| SIREN/USDT:USDT | below_1h_threshold | +1.81% | +1.72% |
| PLAY/USDT:USDT | below_1h_threshold | +1.66% | +1.57% |
| MITO/USDT:USDT | below_1h_threshold | +1.40% | +1.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
