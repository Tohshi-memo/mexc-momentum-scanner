# Decision Report

- generated_at: 2026-06-07T22:10:24.721135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6001**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=6001, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.68% | **+0.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.23% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.64% | **+2.64%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.16% | **+0.93%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.96** / 初期 $100.00 (+51.96%)
- 確定: 1118件 (Win 272 / Loss 337 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.96

## 4. Latest Market Context

- 更新: 2026-06-07T22:10:21.735912+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=61841.0
- Funnel: target 768 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +23.60% | $13,519,023.88 |
| BANK/USDT:USDT | +22.82% | $3,823,544.00 |
| BEAT/USDT:USDT | +19.11% | $71,145,222.06 |
| EPIC/USDT:USDT | +15.86% | $1,367,298.88 |
| PIPPIN/USDT:USDT | +14.19% | $3,632,835.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +2.57% | +2.43% |
| BEAT/USDT:USDT | below_1h_threshold | +2.39% | +2.25% |
| ZEC/USDT:USDT | below_1h_threshold | +2.13% | +1.99% |
| BLESS/USDT:USDT | below_1h_threshold | +1.74% | +1.60% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.60% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
