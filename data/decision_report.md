# Decision Report

- generated_at: 2026-06-24T06:52:05.343070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7465**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=7465, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.52** / 初期 $100.00 (+130.52%)
- 確定: 2096件 (Win 621 / Loss 695 / Flat 780) / skip 1930件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1618_LONG` EXPIRED account +0.00% 残高後 $230.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.82** / 初期 $100.00 (+6.82%)
- 確定: 329件 (Win 93 / Loss 88 / Flat 148) / skip 547件
- 成長率目線: 平均log +0.000200 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0443 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $106.82

## 5. Latest Market Context

- 更新: 2026-06-24T06:52:00.374258+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=62730.5
- Funnel: target 807 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +45.05% | $2,071,395.63 |
| HEI/USDT:USDT | +42.58% | $13,670,950.06 |
| BEAT/USDT:USDT | +33.10% | $76,625,474.59 |
| CLO/USDT:USDT | +18.30% | $5,282,933.73 |
| ID/USDT:USDT | +14.72% | $1,382,029.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.98% | +3.18% |
| BSB/USDT:USDT | below_1h_threshold | +2.38% | +2.59% |
| SPX/USDT:USDT | below_1h_threshold | +1.90% | +2.10% |
| CHZ/USDT:USDT | below_1h_threshold | +1.82% | +2.03% |
| INX/USDT:USDT | below_1h_threshold | +1.55% | +1.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
