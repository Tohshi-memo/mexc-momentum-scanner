# Decision Report

- generated_at: 2026-09-09T13:21:30.146184+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14072**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14072, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.87% | **-0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +2.35% | **+1.30%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_BB3S | 3/16 | 18.8% | +4.00% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.75% | **+1.49%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.24%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.97% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5320件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.77** / 初期 $100.00 (+91.77%)
- 確定: 2668件 (Win 733 / Loss 627 / Flat 1308) / skip 4815件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $191.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 2620件 (Win 765 / Loss 1001 / Flat 854) / pending 0件 / skip 2923件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account -0.09% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-09-09T13:21:17.436796+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=79497.5
- Funnel: target 1064 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +66.50% | $1,769,141.47 |
| IOST/USDT:USDT | +40.47% | $7,648,682.90 |
| OL/USDT:USDT | +20.54% | $2,376,299.51 |
| RAY/USDT:USDT | +19.33% | $6,124,762.05 |
| BR/USDT:USDT | +18.73% | $1,889,492.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_1h_threshold | +2.60% | +2.69% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.11% | +2.19% |
| XPT/USDT:USDT | below_1h_threshold | +1.77% | +1.85% |
| APT/USDT:USDT | below_1h_threshold | +1.69% | +1.78% |
| ATOM/USDT:USDT | below_1h_threshold | +1.45% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
