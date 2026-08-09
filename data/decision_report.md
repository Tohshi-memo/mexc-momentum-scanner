# Decision Report

- generated_at: 2026-08-09T19:21:39.512565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11081**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11081, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.97% | **-3.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 19/20 | 95.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |
| LIMIT_6PCT | 3/20 | 15.0% | -2.04% | **-0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | -4.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +5.03% | **+3.27%** |
| MARKET_LONG | 20/20 | 100.0% | +2.97% | **+2.97%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +5.62% | **+2.53%** |
| LIMIT_4PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 4/20 | 20.0% | +4.80% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3711件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 2979件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1646 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1281件 (Win 395 / Loss 493 / Flat 393) / pending 2件 / skip 1274件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000493 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: INX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-09T19:21:24.769850+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65185.8
- Funnel: target 961 → liquid 149 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 84.3 >= 65=1, 4h RSI 73.1 >= 65=1, 4h RSI 98.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +45.05% | $2,190,377.02 |
| TUT/USDT:USDT | +44.15% | $78,456,192.45 |
| BMT/USDT:USDT | +40.75% | $13,685,296.59 |
| COOKIE/USDT:USDT | +30.92% | $7,873,792.60 |
| 4/USDT:USDT | +15.26% | $1,759,890.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.51% | +3.48% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.48% | +3.45% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.43% | +3.41% |
| AKE/USDT:USDT | below_1h_threshold | +2.01% | +1.98% |
| BTW/USDT:USDT | below_1h_threshold | +1.52% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
