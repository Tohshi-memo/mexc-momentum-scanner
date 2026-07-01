# Decision Report

- generated_at: 2026-07-01T22:13:34.496198+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8022**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8022, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.70% | **+0.55%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_10PCT | 4/20 | 20.0% | +1.36% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.90% | **+0.32%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.23% | **+0.18%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$281.98** / 初期 $100.00 (+181.98%)
- 確定: 2419件 (Win 743 / Loss 802 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $281.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 537件 (Win 135 / Loss 126 / Flat 276) / skip 896件
- 成長率目線: 平均log +0.000123 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0295 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $106.83

## 5. Latest Market Context

- 更新: 2026-07-01T22:13:29.540319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=60799.9
- Funnel: target 825 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +67.77% | $3,688,020.59 |
| TAIKO/USDT:USDT | +63.01% | $25,007,132.99 |
| NOM/USDT:USDT | +23.28% | $5,388,556.07 |
| LIT/USDT:USDT | +22.95% | $8,504,230.91 |
| COOKIE/USDT:USDT | +18.21% | $1,023,996.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +2.15% | +2.15% |
| GRASS/USDT:USDT | below_1h_threshold | +2.09% | +2.08% |
| COOKIE/USDT:USDT | below_1h_threshold | +1.97% | +1.97% |
| O/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |
| ZEC/USDT:USDT | below_1h_threshold | +1.31% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
