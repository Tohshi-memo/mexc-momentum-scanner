# Decision Report

- generated_at: 2026-06-16T19:18:35.943966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6880**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=6880, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.61% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.32% | **+0.29%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.96% | **+0.14%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.94%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.36% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$186.13** / 初期 $100.00 (+86.13%)
- 確定: 1753件 (Win 463 / Loss 550 / Flat 740) / skip 1688件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $186.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.02** / 初期 $100.00 (-1.98%)
- 確定: 157件 (Win 29 / Loss 30 / Flat 98) / skip 134件
- 成長率目線: 平均log -0.000127 / 幾何平均 -0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $98.02

## 5. Latest Market Context

- 更新: 2026-06-16T19:18:29.826455+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=65576.0
- Funnel: target 782 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +13.62% | $58,791,954.89 |
| VELVET/USDT:USDT | +12.96% | $26,157,010.55 |
| BLESS/USDT:USDT | +9.38% | $1,048,207.39 |
| PLAY/USDT:USDT | +9.08% | $1,132,651.73 |
| ESPORTS/USDT:USDT | +7.59% | $1,667,053.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +1.85% | +2.22% |
| MYX/USDT:USDT | below_1h_threshold | +1.81% | +2.18% |
| BLESS/USDT:USDT | below_1h_threshold | +0.96% | +1.34% |
| BR/USDT:USDT | below_1h_threshold | +0.96% | +1.34% |
| VELVET/USDT:USDT | below_1h_threshold | +0.67% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
