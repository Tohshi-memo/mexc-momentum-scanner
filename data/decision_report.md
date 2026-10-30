# Decision Report

- generated_at: 2026-10-30T04:56:26.799985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17826**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17826, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.34% | **+0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.13% | **-0.08%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -1.39% | **-0.21%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.50% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.76% | **+0.70%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.10% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6805件 (Win 1975 / Loss 2181 / Flat 2649) / skip 7582件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.03** / 初期 $100.00 (+264.03%)
- 確定: 4343件 (Win 1169 / Loss 980 / Flat 2194) / skip 6894件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0038 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $364.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5986件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T04:56:11.827259+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78230.5
- Funnel: target 1086 → liquid 195 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +57.42% | $7,386,915.61 |
| Q/USDT:USDT | +46.31% | $24,744,876.33 |
| SOXS/USDT:USDT | +17.89% | $69,753,795.16 |
| RUNE/USDT:USDT | +12.73% | $1,326,472.64 |
| BLESS/USDT:USDT | +11.43% | $14,305,310.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PREDICT/USDT:USDT | below_1h_threshold | +4.08% | +4.04% |
| RUNE/USDT:USDT | below_1h_threshold | +3.02% | +2.98% |
| JCT/USDT:USDT | below_1h_threshold | +1.56% | +1.52% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.50% |
| INIT/USDT:USDT | below_1h_threshold | +0.49% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
