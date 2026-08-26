# Decision Report

- generated_at: 2026-08-26T21:31:24.599506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12747**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=12747, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.73% | **+1.55%** |
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.51% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +3.06% | **+3.06%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$720.43** / 初期 $100.00 (+620.43%)
- 確定: 4644件 (Win 1410 / Loss 1523 / Flat 1711) / skip 4664件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $720.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4157件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0875 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 0件 / skip 2239件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-26T21:31:12.495246+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=78666.9
- Funnel: target 1023 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONT/USDT:USDT | +11.77% | $3,941,287.66 |
| CASHCAT/USDT:USDT | +11.73% | $1,196,576.14 |
| ONG/USDT:USDT | +11.40% | $32,608,703.86 |
| EDEN/USDT:USDT | +10.74% | $9,247,756.91 |
| HEI/USDT:USDT | +9.75% | $3,061,122.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CVX/USDT:USDT | below_1h_threshold | +3.76% | +3.44% |
| GRASS/USDT:USDT | below_1h_threshold | +3.53% | +3.22% |
| KORU/USDT:USDT | below_1h_threshold | +3.37% | +3.05% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.24% | +2.93% |
| MONAD/USDT:USDT | below_1h_threshold | +3.21% | +2.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
