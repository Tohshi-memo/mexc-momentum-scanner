# Decision Report

- generated_at: 2026-10-06T13:52:11.034289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16217**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16217, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.51% | **-0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 8/16 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.90% | **+0.27%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,362.97** / 初期 $100.00 (+1262.97%)
- 確定: 6258件 (Win 1840 / Loss 2000 / Flat 2418) / skip 6520件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,362.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.88** / 初期 $100.00 (+178.88%)
- 確定: 3625件 (Win 1010 / Loss 848 / Flat 1767) / skip 6003件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0244 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $278.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4380件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000362 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T13:51:57.441525+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=86426.8
- Funnel: target 1074 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +59.83% | $41,342,672.66 |
| BR/USDT:USDT | +57.30% | $52,912,097.38 |
| CAP/USDT:USDT | +42.75% | $2,018,684.72 |
| US/USDT:USDT | +41.01% | $1,438,209.02 |
| NMR/USDT:USDT | +34.28% | $8,648,549.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.59% | +3.31% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.14% | +2.86% |
| USELESS/USDT:USDT | below_1h_threshold | +2.80% | +2.52% |
| ORCA/USDT:USDT | below_1h_threshold | +1.74% | +1.46% |
| RENDER/USDT:USDT | below_1h_threshold | +1.21% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
