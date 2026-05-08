# Decision Report

- generated_at: 2026-05-08T08:02:48.371241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3756**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=3756, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.52% | **+1.52%** |
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_ATR | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.08% | **+0.04%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.12% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 127件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T08:02:45.010835+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=79638.2
- Funnel: target 771 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +33.68% | $4,535,456.07 |
| BSB/USDT:USDT | +32.47% | $5,474,640.97 |
| NOT/USDT:USDT | +22.29% | $10,311,612.57 |
| SATO/USDT:USDT | +20.30% | $9,035,076.99 |
| STRK/USDT:USDT | +18.89% | $11,358,283.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +0.79% | +0.79% |
| NIL/USDT:USDT | below_1h_threshold | +0.78% | +0.78% |
| MOVR/USDT:USDT | below_1h_threshold | +0.64% | +0.64% |
| JTO/USDT:USDT | below_1h_threshold | +0.53% | +0.53% |
| CHIP/USDT:USDT | below_1h_threshold | +0.52% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
