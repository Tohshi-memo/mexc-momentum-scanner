# Decision Report

- generated_at: 2026-09-22T19:31:34.632781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15354**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15354, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.66% | **-1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.45% | **+0.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.17% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.19% | **+0.87%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.93% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.93** / 初期 $100.00 (+1055.93%)
- 確定: 5838件 (Win 1727 / Loss 1877 / Flat 2234) / skip 6077件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,155.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5412件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.37** / 初期 $100.00 (+22.37%)
- 確定: 3110件 (Win 913 / Loss 1219 / Flat 978) / pending 6件 / skip 3720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000087 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUSEBOOK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $122.37

## 6. Latest Market Context

- 更新: 2026-09-22T19:31:23.434330+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=86427.7
- Funnel: target 1058 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +20.44% | $1,044,061.02 |
| MUBARAK/USDT:USDT | +19.70% | $14,557,330.17 |
| 4/USDT:USDT | +15.54% | $1,727,996.09 |
| CHR/USDT:USDT | +15.31% | $3,977,043.78 |
| BR/USDT:USDT | +14.35% | $6,256,587.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +3.81% | +3.79% |
| BEAT/USDT:USDT | below_1h_threshold | +2.69% | +2.67% |
| PONS/USDT:USDT | below_1h_threshold | +2.57% | +2.54% |
| PENGU/USDT:USDT | below_1h_threshold | +2.46% | +2.43% |
| LTC/USDT:USDT | below_1h_threshold | +2.33% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
