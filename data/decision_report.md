# Decision Report

- generated_at: 2026-05-23T08:14:01.916216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4762**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=4762, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.44% | **+0.79%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.19% | **-0.13%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.55% | **-0.25%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.52** / 初期 $100.00 (+21.52%)
- 確定: 608件 (Win 150 / Loss 194 / Flat 264) / skip 715件
- 成長率目線: 平均log +0.000321 / 幾何平均 +0.032% per trade / maxDD +4.21%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $121.52

## 4. Latest Market Context

- 更新: 2026-05-23T08:13:59.793608+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=74551.8
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +125.36% | $65,624,230.73 |
| GMTTOKEN/USDT:USDT | +27.01% | $1,626,168.28 |
| IN/USDT:USDT | +17.72% | $1,860,514.89 |
| BEAT/USDT:USDT | +14.35% | $64,063,903.27 |
| SKYAI/USDT:USDT | +10.20% | $2,278,849.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.32% | +2.35% |
| MYX/USDT:USDT | below_1h_threshold | +2.14% | +2.16% |
| UB/USDT:USDT | below_1h_threshold | +1.16% | +1.19% |
| GMTTOKEN/USDT:USDT | below_1h_threshold | +0.98% | +1.01% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.87% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
