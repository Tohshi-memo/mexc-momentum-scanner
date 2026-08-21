# Decision Report

- generated_at: 2026-08-21T18:21:22.237337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12234**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12234, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.13% | **+0.34%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.69% | **+2.02%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.00% | **+1.95%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.90% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$646.75** / 初期 $100.00 (+546.75%)
- 確定: 4363件 (Win 1338 / Loss 1434 / Flat 1591) / skip 4432件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $646.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.11** / 初期 $100.00 (+57.11%)
- 確定: 1845件 (Win 512 / Loss 438 / Flat 895) / skip 3800件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0899 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $157.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1889件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000301 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T18:21:15.100036+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77464.0
- Funnel: target 1018 → liquid 212 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +32.21% | $10,965,508.17 |
| JIMOTHY/USDT:USDT | +28.11% | $1,071,481.99 |
| BLESS/USDT:USDT | +11.58% | $7,078,131.94 |
| BEAT/USDT:USDT | +11.03% | $54,974,414.76 |
| PEPE/USDT:USDT | +9.79% | $390,952,396.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZORA/USDT:USDT | below_1h_threshold | +3.24% | +3.13% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.19% | +3.09% |
| ALIGN/USDT:USDT | below_1h_threshold | +2.91% | +2.80% |
| GPS/USDT:USDT | below_1h_threshold | +2.74% | +2.63% |
| EVAA/USDT:USDT | below_1h_threshold | +2.23% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
