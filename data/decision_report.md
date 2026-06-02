# Decision Report

- generated_at: 2026-06-02T12:02:32.717203+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5450**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5450, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.36% | **-0.09%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.30% | **-0.09%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.43% | **-0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.38% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.32** / 初期 $100.00 (+33.32%)
- 確定: 962件 (Win 226 / Loss 291 / Flat 445) / skip 1049件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.32

## 4. Latest Market Context

- 更新: 2026-06-02T12:02:29.999059+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=69430.6
- Funnel: target 773 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +41.66% | $3,364,709.56 |
| EPIC/USDT:USDT | +37.71% | $2,728,823.58 |
| USELESS/USDT:USDT | +27.80% | $2,498,980.47 |
| CLO/USDT:USDT | +24.02% | $1,047,014.15 |
| LAB/USDT:USDT | +23.67% | $169,639,435.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +1.01% | +1.01% |
| JTO/USDT:USDT | below_1h_threshold | +0.70% | +0.70% |
| OPG/USDT:USDT | below_1h_threshold | +0.52% | +0.52% |
| USELESS/USDT:USDT | below_1h_threshold | +0.39% | +0.39% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
