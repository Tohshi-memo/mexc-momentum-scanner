# Decision Report

- generated_at: 2026-08-07T11:56:32.481584+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10708**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10708, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.51% | **+0.76%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.76% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.88% | **+1.87%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.20% | **+1.54%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.19% | **+0.66%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.16% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3471件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2663件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0029 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.07** / 初期 $100.00 (+17.07%)
- 確定: 1163件 (Win 373 / Loss 457 / Flat 333) / pending 4件 / skip 1017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000333 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.07

## 6. Latest Market Context

- 更新: 2026-08-07T11:56:21.791038+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=64987.5
- Funnel: target 961 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KGEN/USDT:USDT | +36.38% | $1,595,828.86 |
| SKYAI/USDT:USDT | +34.06% | $73,775,131.25 |
| CATE/USDT:USDT | +31.59% | $4,372,701.41 |
| TUT/USDT:USDT | +30.91% | $1,003,687.50 |
| BICO/USDT:USDT | +29.43% | $28,515,871.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +3.19% | +3.01% |
| ALLO/USDT:USDT | below_1h_threshold | +2.36% | +2.18% |
| BEAT/USDT:USDT | below_1h_threshold | +2.29% | +2.10% |
| BSB/USDT:USDT | below_1h_threshold | +2.27% | +2.09% |
| ON/USDT:USDT | below_1h_threshold | +2.19% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
