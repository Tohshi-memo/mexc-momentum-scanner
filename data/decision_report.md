# Decision Report

- generated_at: 2026-08-15T01:21:25.823617+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11623**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=11623, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.56% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.30% | **+0.09%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.07% | **+0.05%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | -0.06% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$645.65** / 初期 $100.00 (+545.65%)
- 確定: 4091件 (Win 1283 / Loss 1346 / Flat 1462) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $645.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.52** / 初期 $100.00 (+52.52%)
- 確定: 1686件 (Win 482 / Loss 408 / Flat 796) / skip 3348件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0803 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $152.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 1571件 (Win 478 / Loss 601 / Flat 492) / pending 1件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-15T01:21:15.168144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62983.0
- Funnel: target 985 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +17.23% | $1,096,142.50 |
| US/USDT:USDT | +16.73% | $6,736,188.63 |
| ONE/USDT:USDT | +12.11% | $1,488,732.66 |
| CAP/USDT:USDT | +10.85% | $21,563,120.24 |
| AIO/USDT:USDT | +10.75% | $1,048,455.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +3.56% | +3.58% |
| MYX/USDT:USDT | below_1h_threshold | +1.03% | +1.05% |
| LINK/USDT:USDT | below_1h_threshold | +0.68% | +0.70% |
| BANK/USDT:USDT | below_1h_threshold | +0.60% | +0.62% |
| ZRO/USDT:USDT | below_1h_threshold | +0.52% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
