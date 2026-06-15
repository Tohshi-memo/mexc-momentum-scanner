# Decision Report

- generated_at: 2026-06-15T03:59:28.599959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6736**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6736, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.11% | **+1.90%** |
| ASK | 20/20 | 100.0% | +1.41% | **+1.41%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.49% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.02** / 初期 $100.00 (+73.02%)
- 確定: 1609件 (Win 423 / Loss 502 / Flat 684) / skip 1688件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $173.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.19** / 初期 $100.00 (+0.19%)
- 確定: 103件 (Win 24 / Loss 17 / Flat 62) / skip 44件
- 成長率目線: 平均log +0.000019 / 幾何平均 +0.002% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.35% 残高後 $100.19

## 5. Latest Market Context

- 更新: 2026-06-15T03:59:21.833773+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=65867.2
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 92.8 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 78.7 >= 65=1, 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +115.03% | $1,874,843.70 |
| EVAA/USDT:USDT | +59.00% | $18,491,160.64 |
| RIF/USDT:USDT | +37.05% | $4,759,723.96 |
| CLO/USDT:USDT | +36.02% | $2,085,461.11 |
| GRASS/USDT:USDT | +19.04% | $1,080,701.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.54% | +4.87% |
| USELESS/USDT:USDT | below_1h_threshold | +2.34% | +1.67% |
| JTO/USDT:USDT | below_1h_threshold | +2.24% | +1.57% |
| NEAR/USDT:USDT | below_1h_threshold | +1.58% | +0.92% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.35% | +0.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
