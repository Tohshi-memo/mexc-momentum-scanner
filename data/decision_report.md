# Decision Report

- generated_at: 2026-09-05T18:36:29.175510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13770**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13770, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.23% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.28% | **+0.15%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.11% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.71** / 初期 $100.00 (+754.71%)
- 確定: 5076件 (Win 1522 / Loss 1655 / Flat 1899) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $854.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.66** / 初期 $100.00 (+87.66%)
- 確定: 2515件 (Win 700 / Loss 594 / Flat 1221) / skip 4666件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0379 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $187.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.53** / 初期 $100.00 (+19.53%)
- 確定: 2387件 (Win 708 / Loss 906 / Flat 773) / pending 2件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.53

## 6. Latest Market Context

- 更新: 2026-09-05T18:36:16.919680+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79942.6
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +27.23% | $25,663,378.23 |
| MAGMA/USDT:USDT | +22.48% | $2,412,884.36 |
| BASECAT/USDT:USDT | +10.71% | $2,095,586.55 |
| UNI/USDT:USDT | +9.79% | $36,584,857.88 |
| NIULAI/USDT:USDT | +8.99% | $2,771,532.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.90% | +4.01% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.43% | +3.54% |
| UNI/USDT:USDT | below_1h_threshold | +3.32% | +3.43% |
| UAI/USDT:USDT | below_1h_threshold | +2.82% | +2.93% |
| ARB/USDT:USDT | below_1h_threshold | +2.18% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
