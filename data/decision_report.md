# Decision Report

- generated_at: 2026-08-22T02:26:24.869070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12295**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12295, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.49% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.22% | **+2.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.43% | **+1.34%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.83% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$694.25** / 初期 $100.00 (+594.25%)
- 確定: 4413件 (Win 1351 / Loss 1442 / Flat 1620) / skip 4443件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $694.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.47** / 初期 $100.00 (+54.47%)
- 確定: 1901件 (Win 523 / Loss 455 / Flat 923) / skip 3805件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2293 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $154.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.98** / 初期 $100.00 (+17.98%)
- 確定: 1844件 (Win 546 / Loss 696 / Flat 602) / pending 5件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.98

## 6. Latest Market Context

- 更新: 2026-08-22T02:26:13.665941+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=78175.0
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.9 >= 65=1, 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +270.41% | $3,904,546.78 |
| CATE/USDT:USDT | +59.07% | $12,010,172.32 |
| TRB/USDT:USDT | +31.77% | $4,088,094.76 |
| AGI/USDT:USDT | +28.67% | $1,755,228.56 |
| ZEC/USDT:USDT | +24.38% | $313,694,857.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +4.90% | +4.43% |
| ZEN/USDT:USDT | below_1h_threshold | +4.85% | +4.38% |
| GALA/USDT:USDT | below_1h_threshold | +4.57% | +4.10% |
| ORDI/USDT:USDT | below_1h_threshold | +4.00% | +3.52% |
| PEPE/USDT:USDT | below_1h_threshold | +3.20% | +2.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
