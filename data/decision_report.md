# Decision Report

- generated_at: 2026-06-12T09:31:58.109021+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6492**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=6492, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.18% | **+0.53%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.51% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| ASK_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$162.31** / 初期 $100.00 (+62.31%)
- 確定: 1366件 (Win 370 / Loss 440 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $162.31

## 4. Latest Market Context

- 更新: 2026-06-12T09:31:54.945510+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.50% price=63755.5
- Funnel: target 769 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +104.40% | $149,369,827.41 |
| ESPORTS/USDT:USDT | +52.90% | $38,972,178.85 |
| NAORIS/USDT:USDT | +47.63% | $3,333,628.90 |
| XPL/USDT:USDT | +38.17% | $10,516,816.76 |
| AIN/USDT:USDT | +30.11% | $1,000,271.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +4.61% | +4.11% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +4.04% | +3.54% |
| NAORIS/USDT:USDT | below_1h_threshold | +4.02% | +3.52% |
| AIN/USDT:USDT | below_1h_threshold | +3.72% | +3.23% |
| XMR/USDT:USDT | below_1h_threshold | +3.20% | +2.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
