# Decision Report

- generated_at: 2026-05-23T06:38:24.855080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4759**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=4759, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.47% | **+0.66%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.71% | **+0.60%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.18% | **+0.14%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.54% | **-0.05%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.09% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.74** / 初期 $100.00 (+22.74%)
- 確定: 605件 (Win 150 / Loss 192 / Flat 263) / skip 715件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.74

## 4. Latest Market Context

- 更新: 2026-05-23T06:38:22.954809+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=75391.4
- Funnel: target 764 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +130.12% | $62,443,272.72 |
| BEAT/USDT:USDT | +15.92% | $61,973,049.57 |
| IN/USDT:USDT | +14.72% | $1,756,383.68 |
| SKYAI/USDT:USDT | +9.82% | $2,653,573.76 |
| MYX/USDT:USDT | +8.06% | $1,500,379.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.08% | +1.16% |
| LAB/USDT:USDT | below_1h_threshold | +0.97% | +1.05% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.83% | +0.91% |
| BSB/USDT:USDT | below_1h_threshold | +0.80% | +0.88% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.78% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
