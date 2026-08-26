# Decision Report

- generated_at: 2026-08-26T18:01:21.858396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12737**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=12737, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.12% | **+1.90%** |
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +4.44% | **+2.53%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.41%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.72% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$721.52** / 初期 $100.00 (+621.52%)
- 確定: 4634件 (Win 1409 / Loss 1522 / Flat 1703) / skip 4664件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $721.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4147件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0864 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 0件 / skip 2228件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-26T18:01:12.835457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78375.6
- Funnel: target 1023 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +17.15% | $5,429,078.67 |
| S/USDT:USDT | +6.56% | $1,018,511.47 |
| ACU/USDT:USDT | +6.38% | $1,900,057.11 |
| ONT/USDT:USDT | +5.56% | $2,255,471.29 |
| UAI/USDT:USDT | +4.93% | $2,345,310.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.38% | +1.42% |
| ONT/USDT:USDT | below_1h_threshold | +1.30% | +1.34% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.13% | +1.17% |
| ZMSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.15% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +0.96% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
