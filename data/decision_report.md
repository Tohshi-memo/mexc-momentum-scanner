# Decision Report

- generated_at: 2026-05-13T18:48:38.303878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4245**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=4245, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.35% | **+1.29%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.83% | **+0.21%** |
| ASK | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.09% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$98.19** / 初期 $100.00 (-1.81%)
- 確定トレード: 39件 (TP 10 / SL 26 / EXP 3)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 464件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T18:48:35.149366+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79512.3
- Funnel: target 761 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +25.97% | $1,125,416.15 |
| GUA/USDT:USDT | +13.17% | $3,673,781.72 |
| BEAT/USDT:USDT | +12.07% | $2,036,240.96 |
| GIGA/USDT:USDT | +10.98% | $2,037,140.85 |
| UP/USDT:USDT | +9.71% | $4,771,564.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.77% | +4.71% |
| GIGA/USDT:USDT | below_1h_threshold | +4.70% | +4.65% |
| BEAT/USDT:USDT | below_1h_threshold | +3.37% | +3.32% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.54% | +2.49% |
| UP/USDT:USDT | below_1h_threshold | +2.53% | +2.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
