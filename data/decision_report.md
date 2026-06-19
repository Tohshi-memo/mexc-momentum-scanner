# Decision Report

- generated_at: 2026-06-19T08:29:36.547596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7112**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=7112, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.13% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$103.50** / 初期 $100.00 (+3.50%)
- 確定トレード: 20件 (TP 9 / SL 11 / EXP 0)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.73** / 初期 $100.00 (+122.73%)
- 確定: 1932件 (Win 552 / Loss 622 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $222.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 214件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T08:29:29.244097+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62631.5
- Funnel: target 795 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +83.16% | $7,786,518.68 |
| HEI/USDT:USDT | +61.17% | $4,687,455.49 |
| BTW/USDT:USDT | +27.35% | $3,082,640.47 |
| BASED/USDT:USDT | +22.75% | $6,996,935.80 |
| ZEREBRO/USDT:USDT | +14.24% | $3,929,187.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +4.59% | +4.52% |
| JTO/USDT:USDT | below_1h_threshold | +4.03% | +3.97% |
| HIGH/USDT:USDT | below_1h_threshold | +1.45% | +1.39% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.42% | +1.35% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.39% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
