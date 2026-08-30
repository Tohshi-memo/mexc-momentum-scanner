# Decision Report

- generated_at: 2026-08-30T07:21:18.483312+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13033**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13033, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.21% | **-1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 13/18 | 72.2% | +1.66% | **+1.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.29% | **+0.07%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.14% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.93% | **+0.65%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$790.43** / 初期 $100.00 (+690.43%)
- 確定: 4803件 (Win 1463 / Loss 1580 / Flat 1760) / skip 4791件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $790.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.48** / 初期 $100.00 (+72.48%)
- 確定: 2117件 (Win 591 / Loss 517 / Flat 1009) / skip 4327件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.52** / 初期 $100.00 (+17.52%)
- 確定: 2075件 (Win 610 / Loss 804 / Flat 661) / pending 5件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.52

## 6. Latest Market Context

- 更新: 2026-08-30T07:21:09.093757+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78209.7
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +84.56% | $37,141,963.02 |
| NIULAI/USDT:USDT | +69.50% | $3,042,766.06 |
| PONS/USDT:USDT | +60.11% | $1,694,176.35 |
| FONE/USDT:USDT | +48.84% | $1,450,689.50 |
| PROM/USDT:USDT | +31.26% | $15,501,917.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +4.17% | +4.22% |
| JASMY/USDT:USDT | below_1h_threshold | +1.71% | +1.76% |
| BTR/USDT:USDT | below_1h_threshold | +1.26% | +1.31% |
| HNT/USDT:USDT | below_1h_threshold | +1.25% | +1.30% |
| UAI/USDT:USDT | below_1h_threshold | +1.16% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
