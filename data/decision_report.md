# Decision Report

- generated_at: 2026-06-18T05:18:50.318216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7006**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7006, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.42% | **+0.11%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.38% | **+0.10%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.22% | **+0.17%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$214.05** / 初期 $100.00 (+114.05%)
- 確定: 1852件 (Win 516 / Loss 585 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $214.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 279件 (Win 77 / Loss 73 / Flat 129) / skip 138件
- 成長率目線: 平均log +0.000179 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0435 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-06-18T05:18:45.925017+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63944.7
- Funnel: target 793 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +105.35% | $36,066,501.30 |
| O/USDT:USDT | +62.22% | $2,161,050.38 |
| SYN/USDT:USDT | +57.09% | $4,734,612.40 |
| HOME/USDT:USDT | +39.10% | $1,669,585.38 |
| H/USDT:USDT | +29.53% | $32,128,624.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.06% | +3.91% |
| GUA/USDT:USDT | below_1h_threshold | +3.38% | +3.24% |
| CLO/USDT:USDT | below_1h_threshold | +2.25% | +2.11% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.88% | +0.73% |
| RE/USDT:USDT | below_1h_threshold | +0.46% | +0.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
