# Decision Report

- generated_at: 2026-05-14T13:13:09.556539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4290**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=4290, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +2.72% | **+1.26%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.96% | **+0.91%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.53% | **+1.09%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.59% | **+0.64%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.37** / 初期 $100.00 (+20.37%)
- 確定: 346件 (Win 95 / Loss 125 / Flat 126) / skip 505件
- 成長率目線: 平均log +0.000536 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.37

## 4. Latest Market Context

- 更新: 2026-05-14T13:13:05.617751+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=79840.8
- Funnel: target 763 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +53.65% | $7,897,851.77 |
| TROLLSOL/USDT:USDT | +27.38% | $2,232,548.47 |
| UP/USDT:USDT | +25.37% | $1,740,855.73 |
| CSCOSTOCK/USDT:USDT | +17.97% | $5,687,112.85 |
| PLAY/USDT:USDT | +16.83% | $1,681,676.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +1.38% | +1.22% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.14% | +0.99% |
| UB/USDT:USDT | below_1h_threshold | +1.05% | +0.89% |
| SUI/USDT:USDT | below_1h_threshold | +0.98% | +0.83% |
| BILL/USDT:USDT | below_1h_threshold | +0.85% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
