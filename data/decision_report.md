# Decision Report

- generated_at: 2026-06-02T15:23:37.270509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5461**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5461, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.96% | **+0.91%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_BB3S | 3/18 | 16.7% | +0.85% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.28% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.37** / 初期 $100.00 (+32.37%)
- 確定: 973件 (Win 229 / Loss 297 / Flat 447) / skip 1049件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $132.37

## 4. Latest Market Context

- 更新: 2026-06-02T15:23:34.918145+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=67617.7
- Funnel: target 773 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +47.84% | $5,292,120.93 |
| MRVLSTOCK/USDT:USDT | +30.73% | $9,427,824.00 |
| USELESS/USDT:USDT | +29.92% | $4,378,865.24 |
| LAB/USDT:USDT | +24.80% | $174,786,812.65 |
| PIEVERSE/USDT:USDT | +24.79% | $4,793,125.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.15% | +3.69% |
| US/USDT:USDT | below_1h_threshold | +2.72% | +3.27% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.70% | +3.25% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.09% | +2.64% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +2.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
