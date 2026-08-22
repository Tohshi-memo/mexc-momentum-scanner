# Decision Report

- generated_at: 2026-08-22T04:56:52.374005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12321**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12321, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.04% | **+0.99%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.83% | **+0.85%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.48% | **+1.36%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$728.52** / 初期 $100.00 (+628.52%)
- 確定: 4439件 (Win 1362 / Loss 1447 / Flat 1630) / skip 4443件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZAMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $728.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.92** / 初期 $100.00 (+57.92%)
- 確定: 1927件 (Win 531 / Loss 460 / Flat 936) / skip 3805件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2122 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $157.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.28** / 初期 $100.00 (+18.28%)
- 確定: 1856件 (Win 549 / Loss 699 / Flat 608) / pending 5件 / skip 1947件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000470 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.28

## 6. Latest Market Context

- 更新: 2026-08-22T04:56:36.273343+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=78510.8
- Funnel: target 1018 → liquid 222 → pre 50 → checked 50 → surge 8 → strict 1
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.1 >= 65=2, 4h RSI 86.6 >= 65=1, 4h RSI 90.7 >= 65=1, 4h RSI 89.6 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +250.61% | $4,491,573.08 |
| CATE/USDT:USDT | +74.52% | $11,649,066.31 |
| TRUMPOFFICIAL/USDT:USDT | +72.45% | $54,151,523.73 |
| MUBARAK/USDT:USDT | +36.81% | $1,580,541.21 |
| ZAMA/USDT:USDT | +29.10% | $1,081,180.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POL/USDT:USDT | below_1h_threshold | +4.97% | +4.83% |
| PEPE/USDT:USDT | below_1h_threshold | +4.50% | +4.35% |
| OP/USDT:USDT | below_1h_threshold | +4.48% | +4.33% |
| ADA/USDT:USDT | below_1h_threshold | +4.34% | +4.19% |
| WIF/USDT:USDT | below_1h_threshold | +4.27% | +4.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
