# Decision Report

- generated_at: 2026-06-12T09:25:44.216392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6491**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=6491, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/20 | 20.0% | +3.25% | **+0.65%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.43% | **+0.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.51% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$161.50** / 初期 $100.00 (+61.50%)
- 確定: 1365件 (Win 369 / Loss 440 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $161.50

## 4. Latest Market Context

- 更新: 2026-06-12T09:25:41.473808+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=63636.1
- Funnel: target 769 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +104.13% | $148,930,884.27 |
| NAORIS/USDT:USDT | +48.36% | $3,236,349.58 |
| ESPORTS/USDT:USDT | +47.44% | $38,700,795.03 |
| XPL/USDT:USDT | +41.95% | $10,388,599.17 |
| SKYAI/USDT:USDT | +29.60% | $16,040,061.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +4.68% | +4.37% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +4.66% | +4.35% |
| XPL/USDT:USDT | below_1h_threshold | +3.53% | +3.22% |
| XMR/USDT:USDT | below_1h_threshold | +3.37% | +3.06% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.88% | +2.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
