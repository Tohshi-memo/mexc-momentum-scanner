# Decision Report

- generated_at: 2026-08-27T00:56:22.804661+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12762**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=12762, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.10% | **+0.44%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.23% | **+1.17%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.09% | **+0.93%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.73% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$734.20** / 初期 $100.00 (+634.20%)
- 確定: 4658件 (Win 1414 / Loss 1527 / Flat 1717) / skip 4665件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACU/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $734.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4172件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1061 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 0件 / skip 2251件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T00:56:11.918526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=78691.0
- Funnel: target 1023 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +19.50% | $1,728,841.88 |
| SPX/USDT:USDT | +16.91% | $5,500,048.59 |
| VET/USDT:USDT | +15.66% | $2,869,292.11 |
| FARTCOIN/USDT:USDT | +11.48% | $25,457,928.26 |
| CVX/USDT:USDT | +10.80% | $1,408,607.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +2.90% | +3.28% |
| CYS/USDT:USDT | below_1h_threshold | +2.66% | +3.03% |
| PROM/USDT:USDT | below_1h_threshold | +2.61% | +2.99% |
| EUL/USDT:USDT | below_1h_threshold | +2.49% | +2.87% |
| SPX/USDT:USDT | below_1h_threshold | +2.02% | +2.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
