# Decision Report

- generated_at: 2026-08-13T16:31:36.787251+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11459**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11459, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +0.46% | **+0.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.26% | **+1.58%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.28% | **+1.48%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.06% | **+1.22%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.57% | **+0.89%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$609.46** / 初期 $100.00 (+509.46%)
- 確定: 3977件 (Win 1240 / Loss 1302 / Flat 1435) / skip 4043件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.34% 残高後 $609.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.99** / 初期 $100.00 (+50.99%)
- 確定: 1647件 (Win 471 / Loss 395 / Flat 781) / skip 3223件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0485 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $150.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.89** / 初期 $100.00 (+16.89%)
- 確定: 1461件 (Win 431 / Loss 550 / Flat 480) / pending 5件 / skip 1469件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.89

## 6. Latest Market Context

- 更新: 2026-08-13T16:31:25.608332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63390.0
- Funnel: target 978 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1, 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +8.98% | $9,120,418.65 |
| BICO/USDT:USDT | +4.09% | $4,580,953.95 |
| BEAT/USDT:USDT | +4.00% | $36,646,948.32 |
| ACU/USDT:USDT | +3.52% | $8,479,266.43 |
| BLESS/USDT:USDT | +3.45% | $9,954,719.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.10% | +4.09% |
| BEAT/USDT:USDT | below_1h_threshold | +4.00% | +4.00% |
| ACU/USDT:USDT | below_1h_threshold | +3.63% | +3.63% |
| BLESS/USDT:USDT | below_1h_threshold | +3.45% | +3.45% |
| AVAAI/USDT:USDT | below_1h_threshold | +2.85% | +2.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
