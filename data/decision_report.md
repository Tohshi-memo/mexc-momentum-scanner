# Decision Report

- generated_at: 2026-06-11T04:05:26.537521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6297**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6297, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.95% | **+0.95%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.91% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.38% | **+0.31%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1588件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T04:05:23.947875+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=62601.7
- Funnel: target 785 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +79.84% | $52,420,489.00 |
| AIO/USDT:USDT | +67.76% | $3,644,121.24 |
| BEAT/USDT:USDT | +34.71% | $195,101,151.23 |
| COLLECT/USDT:USDT | +25.98% | $1,307,315.33 |
| FIGHT/USDT:USDT | +25.29% | $1,160,673.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +2.99% | +3.08% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.58% | +2.67% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.51% | +0.60% |
| SPX/USDT:USDT | below_1h_threshold | +0.44% | +0.52% |
| KITE/USDT:USDT | below_1h_threshold | +0.34% | +0.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
