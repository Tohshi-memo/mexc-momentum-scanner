# Decision Report

- generated_at: 2026-06-01T05:07:20.856486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5276**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=5276, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.87% | **+2.87%** |
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.64% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.36% | **-0.13%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 943件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T05:07:18.532925+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73471.1
- Funnel: target 777 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +182.30% | $29,814,792.96 |
| H/USDT:USDT | +63.06% | $22,574,268.45 |
| FHE/USDT:USDT | +28.44% | $1,217,980.36 |
| STG/USDT:USDT | +26.74% | $23,143,253.51 |
| HOME/USDT:USDT | +23.13% | $4,042,511.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +2.05% | +2.08% |
| INJ/USDT:USDT | below_1h_threshold | +0.77% | +0.81% |
| CTR/USDT:USDT | below_1h_threshold | +0.61% | +0.64% |
| OFC/USDT:USDT | below_1h_threshold | +0.51% | +0.55% |
| FET/USDT:USDT | below_1h_threshold | +0.33% | +0.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
