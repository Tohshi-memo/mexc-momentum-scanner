# Decision Report

- generated_at: 2026-09-08T01:56:35.993190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13936**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13936, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.06% | **+0.82%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.71% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.83% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.68% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$982.02** / 初期 $100.00 (+882.02%)
- 確定: 5209件 (Win 1568 / Loss 1691 / Flat 1950) / skip 5288件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $982.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4775件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1597 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.37** / 初期 $100.00 (+22.37%)
- 確定: 2526件 (Win 746 / Loss 948 / Flat 832) / pending 5件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000452 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.37

## 6. Latest Market Context

- 更新: 2026-09-08T01:56:18.865585+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79357.6
- Funnel: target 1062 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1, 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +40.20% | $2,317,199.91 |
| MEMEROBINHOOD/USDT:USDT | +37.96% | $6,946,226.71 |
| BONER/USDT:USDT | +27.83% | $4,396,980.29 |
| AERO/USDT:USDT | +17.24% | $4,276,630.04 |
| INJ/USDT:USDT | +14.49% | $48,350,938.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.24% | +3.15% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.17% | +3.08% |
| BR/USDT:USDT | below_1h_threshold | +2.98% | +2.89% |
| UNI/USDT:USDT | below_1h_threshold | +2.93% | +2.84% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
