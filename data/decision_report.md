# Decision Report

- generated_at: 2026-07-07T23:12:33.932702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8456**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=8456, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.47% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |
| ASK | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.36% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.56** / 初期 $100.00 (+1.56%)
- 確定トレード: 70件 (TP 24 / SL 45 / EXP 1)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.56
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.92** / 初期 $100.00 (+220.92%)
- 確定: 2661件 (Win 846 / Loss 897 / Flat 918) / skip 2356件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPELL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $320.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1226件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T23:12:27.839163+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63593.4
- Funnel: target 847 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +20.74% | $44,316,118.98 |
| EDGE/USDT:USDT | +14.52% | $12,877,912.15 |
| SPELL/USDT:USDT | +8.71% | $2,162,433.97 |
| SYN/USDT:USDT | +6.38% | $4,489,161.39 |
| PENGSTOCK/USDT:USDT | +5.90% | $1,401,220.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +1.87% | +1.74% |
| SPELL/USDT:USDT | below_1h_threshold | +1.27% | +1.14% |
| EDGE/USDT:USDT | below_1h_threshold | +1.13% | +1.00% |
| POL/USDT:USDT | below_1h_threshold | +0.61% | +0.49% |
| APE/USDT:USDT | below_1h_threshold | +0.57% | +0.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
