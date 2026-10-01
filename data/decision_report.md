# Decision Report

- generated_at: 2026-10-01T19:41:46.133435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15938**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15938, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.99% | **+0.50%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +3.03% | **+3.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.58% | **+1.93%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.99% | **+1.69%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.13% | **+1.38%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,323.70** / 初期 $100.00 (+1223.70%)
- 確定: 6047件 (Win 1794 / Loss 1950 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,323.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$281.83** / 初期 $100.00 (+181.83%)
- 確定: 3591件 (Win 1003 / Loss 834 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $281.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4106件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000365 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T19:41:33.513675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=84626.7
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +110.43% | $1,666,048.15 |
| MAGMA/USDT:USDT | +21.46% | $1,095,464.39 |
| LONGXIA/USDT:USDT | +12.50% | $11,102,036.75 |
| ZRO/USDT:USDT | +7.59% | $6,300,531.33 |
| MUU/USDT:USDT | +7.13% | $20,709,943.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +1.31% | +1.47% |
| KORU/USDT:USDT | below_1h_threshold | +1.25% | +1.42% |
| TRB/USDT:USDT | below_1h_threshold | +1.14% | +1.30% |
| GRASS/USDT:USDT | below_1h_threshold | +1.09% | +1.25% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
