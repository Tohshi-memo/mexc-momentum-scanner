# Decision Report

- generated_at: 2026-05-12T16:27:54.468630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4142**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4142, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.38% | **+0.35%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.32% | **+1.06%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.41%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.53% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.74** / 初期 $100.00 (+18.74%)
- 確定: 278件 (Win 79 / Loss 96 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000618 / 幾何平均 +0.062% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VIC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $118.74

## 4. Latest Market Context

- 更新: 2026-05-12T16:27:50.912653+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80236.1
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1, 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +18.34% | $2,000,364.67 |
| UP/USDT:USDT | +5.56% | $1,724,300.88 |
| XNY/USDT:USDT | +4.19% | $1,326,257.71 |
| LAB/USDT:USDT | +3.61% | $171,045,279.40 |
| ASTEROID/USDT:USDT | +3.03% | $2,470,216.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +4.20% | +4.28% |
| LAB/USDT:USDT | below_1h_threshold | +3.50% | +3.58% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.04% | +3.12% |
| COAI/USDT:USDT | below_1h_threshold | +3.03% | +3.11% |
| RAVE/USDT:USDT | below_1h_threshold | +2.85% | +2.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
