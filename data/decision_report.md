# Decision Report

- generated_at: 2026-08-25T08:11:20.598311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12593**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12593, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.04% | **+0.02%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.13% | **-0.05%** |
| LIMIT_BB3S | 2/15 | 13.3% | -0.82% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.02%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.05% | **+0.62%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.03% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.08** / 初期 $100.00 (+609.08%)
- 確定: 4573件 (Win 1391 / Loss 1498 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WIF/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $709.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4027件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0745 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.87** / 初期 $100.00 (+15.87%)
- 確定: 1923件 (Win 564 / Loss 730 / Flat 629) / pending 6件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.87

## 6. Latest Market Context

- 更新: 2026-08-25T08:11:13.257273+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=79839.9
- Funnel: target 1023 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +71.61% | $4,489,815.54 |
| JIMOTHY/USDT:USDT | +64.76% | $1,113,471.79 |
| TAC/USDT:USDT | +35.49% | $5,528,928.12 |
| ONG/USDT:USDT | +34.33% | $5,515,899.88 |
| CASHCAT/USDT:USDT | +19.83% | $3,024,227.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +4.83% | +4.61% |
| STORJ/USDT:USDT | below_1h_threshold | +4.44% | +4.22% |
| TUT/USDT:USDT | below_1h_threshold | +4.23% | +4.01% |
| RE/USDT:USDT | below_1h_threshold | +0.86% | +0.64% |
| BTR/USDT:USDT | below_1h_threshold | +0.80% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
