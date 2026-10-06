# Decision Report

- generated_at: 2026-10-06T13:06:13.128993+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16214**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16214, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.94% | **+0.09%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.55% | **+1.01%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.22% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,349.45** / 初期 $100.00 (+1249.45%)
- 確定: 6256件 (Win 1838 / Loss 2000 / Flat 2418) / skip 6519件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $1,349.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.51** / 初期 $100.00 (+176.51%)
- 確定: 3623件 (Win 1008 / Loss 848 / Flat 1767) / skip 6002件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0364 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $276.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4377件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000362 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T13:06:05.279574+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=86191.9
- Funnel: target 1074 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +58.97% | $39,693,876.49 |
| BR/USDT:USDT | +46.96% | $48,731,918.10 |
| US/USDT:USDT | +46.02% | $1,368,718.01 |
| CAP/USDT:USDT | +35.25% | $1,533,088.99 |
| NMR/USDT:USDT | +34.31% | $7,540,027.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.82% | +1.80% |
| US/USDT:USDT | below_1h_threshold | +1.45% | +1.43% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.41% | +1.40% |
| CAP/USDT:USDT | below_1h_threshold | +1.31% | +1.30% |
| TRB/USDT:USDT | below_1h_threshold | +0.66% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
