# Decision Report

- generated_at: 2026-05-23T04:33:28.694682+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4755**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4755, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.79% | **+0.36%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 601件 (Win 149 / Loss 191 / Flat 261) / skip 715件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-23T04:33:26.889626+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=75617.9
- Funnel: target 764 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +124.08% | $58,942,358.80 |
| IN/USDT:USDT | +32.70% | $1,445,294.79 |
| BEAT/USDT:USDT | +25.18% | $57,530,529.10 |
| BILL/USDT:USDT | +19.07% | $18,291,004.30 |
| TAG/USDT:USDT | +13.04% | $1,368,245.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.33% | +4.31% |
| TAG/USDT:USDT | below_1h_threshold | +3.67% | +3.65% |
| H/USDT:USDT | below_1h_threshold | +2.26% | +2.23% |
| AGT/USDT:USDT | below_1h_threshold | +1.42% | +1.40% |
| CHIP/USDT:USDT | below_1h_threshold | +1.12% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
