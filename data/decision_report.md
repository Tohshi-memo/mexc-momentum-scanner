# Decision Report

- generated_at: 2026-07-16T15:36:14.420022+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8812**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8812, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.37% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.42% | **+0.88%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.97% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$109.02** / 初期 $100.00 (+9.02%)
- 確定トレード: 106件 (TP 40 / SL 64 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$339.63** / 初期 $100.00 (+239.63%)
- 確定: 2927件 (Win 912 / Loss 945 / Flat 1070) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $339.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.75** / 初期 $100.00 (+6.75%)
- 確定: 774件 (Win 178 / Loss 171 / Flat 425) / skip 1449件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $106.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 81件 (Win 23 / Loss 54 / Flat 4) / pending 3件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $97.60

## 6. Latest Market Context

- 更新: 2026-07-16T15:36:08.417582+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=64736.3
- Funnel: target 880 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +76.99% | $8,419,361.66 |
| AKE/USDT:USDT | +30.30% | $41,400,122.97 |
| MANTRA/USDT:USDT | +21.77% | $2,740,768.92 |
| ROAM/USDT:USDT | +20.92% | $6,109,654.73 |
| US/USDT:USDT | +20.41% | $15,782,812.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_relative_strength | +5.31% | +4.96% |
| RAVE/USDT:USDT | below_1h_threshold | +3.38% | +3.03% |
| MYX/USDT:USDT | below_1h_threshold | +2.59% | +2.24% |
| RE/USDT:USDT | below_1h_threshold | +2.55% | +2.20% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.89% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
