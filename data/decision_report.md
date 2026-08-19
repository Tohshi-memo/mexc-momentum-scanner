# Decision Report

- generated_at: 2026-08-19T01:41:27.558948+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11936**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=11936, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.88% | **+1.87%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.00% | **+1.70%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.29% | **+1.22%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4211件 (Win 1295 / Loss 1375 / Flat 1541) / skip 4286件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3526件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.12** / 初期 $100.00 (+18.12%)
- 確定: 1724件 (Win 516 / Loss 657 / Flat 551) / pending 0件 / skip 1685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account +0.01% 残高後 $118.12

## 6. Latest Market Context

- 更新: 2026-08-19T01:41:15.593718+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64434.4
- Funnel: target 993 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UNITREE/USDT:USDT | +27.05% | $4,568,618.25 |
| TRIA/USDT:USDT | +20.91% | $3,939,027.69 |
| NIULAI/USDT:USDT | +17.87% | $5,898,523.14 |
| PUMPFUN/USDT:USDT | +10.45% | $27,841,181.19 |
| BTW/USDT:USDT | +10.19% | $23,628,243.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +3.92% | +3.96% |
| ATOM/USDT:USDT | below_1h_threshold | +1.13% | +1.17% |
| US/USDT:USDT | below_1h_threshold | +1.11% | +1.15% |
| SKDD/USDT:USDT | below_1h_threshold | +1.10% | +1.14% |
| ACE/USDT:USDT | below_1h_threshold | +1.03% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
