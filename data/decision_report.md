# Decision Report

- generated_at: 2026-08-20T20:56:48.863445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12098, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.02% | **+1.72%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.21% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$651.05** / 初期 $100.00 (+551.05%)
- 確定: 4311件 (Win 1323 / Loss 1409 / Flat 1579) / skip 4348件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $651.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3687件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.17** / 初期 $100.00 (+17.17%)
- 確定: 1786件 (Win 530 / Loss 678 / Flat 578) / pending 5件 / skip 1782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.17

## 6. Latest Market Context

- 更新: 2026-08-20T20:56:30.370741+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=72580.1
- Funnel: target 1011 → liquid 201 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.0 >= 65=1, 4h RSI 93.4 >= 65=1, 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +55.73% | $2,726,557.20 |
| ONG/USDT:USDT | +49.33% | $9,549,199.24 |
| ONT/USDT:USDT | +35.87% | $1,393,067.58 |
| PEOPLE/USDT:USDT | +17.87% | $2,876,792.02 |
| COLLECT/USDT:USDT | +8.10% | $1,738,480.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEOPLE/USDT:USDT | below_1h_threshold | +4.24% | +4.35% |
| MVLL/USDT:USDT | below_1h_threshold | +3.56% | +3.66% |
| GRASS/USDT:USDT | below_1h_threshold | +3.54% | +3.64% |
| CRV/USDT:USDT | below_1h_threshold | +3.40% | +3.50% |
| MUU/USDT:USDT | below_1h_threshold | +3.38% | +3.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
