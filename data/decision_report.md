# Decision Report

- generated_at: 2026-09-04T09:46:50.553699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13599**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=13599, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.46% | **+1.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.64% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.14% | **+0.91%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.91% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5010件 (Win 1516 / Loss 1644 / Flat 1850) / skip 5150件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.90** / 初期 $100.00 (+85.90%)
- 確定: 2414件 (Win 681 / Loss 576 / Flat 1157) / skip 4596件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.02** / 初期 $100.00 (+16.02%)
- 確定: 2252件 (Win 667 / Loss 878 / Flat 707) / pending 4件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000066 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SPX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $116.02

## 6. Latest Market Context

- 更新: 2026-09-04T09:46:36.718389+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=81173.9
- Funnel: target 1052 → liquid 163 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1, 4h RSI 93.4 >= 65=1, 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +51.36% | $36,604,128.07 |
| TRIA/USDT:USDT | +42.82% | $6,758,724.59 |
| HNT/USDT:USDT | +21.57% | $13,437,841.06 |
| SKR/USDT:USDT | +19.59% | $4,831,526.96 |
| PONS/USDT:USDT | +16.18% | $10,590,745.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +5.00% | +4.92% |
| TRIA/USDT:USDT | below_1h_threshold | +4.55% | +4.48% |
| UAI/USDT:USDT | below_1h_threshold | +3.72% | +3.65% |
| HNT/USDT:USDT | below_1h_threshold | +3.64% | +3.56% |
| BTR/USDT:USDT | below_1h_threshold | +3.50% | +3.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
